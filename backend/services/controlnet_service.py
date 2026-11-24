"""ControlNet Cloud Inference Service for SketchSpace AI.
Integrates live pretrained ControlNet Scribble + Stable Diffusion models
running on GPU-accelerated cloud infrastructure.

Guarantees:
- Diagnostic logging for hostname, URL, and exception type without ever logging access tokens.
- Deprecated hostnames (api-inference.huggingface.co) completely removed.
- Never falls back to Pix2Pix on failure. Raises ControlNetAPIError with status and explanation.
"""

import base64
import io
import json
import logging
import os
import time
import urllib.parse
from pathlib import Path
from typing import Optional, Tuple

import numpy as np
from PIL import Image

try:
    import httpx
    HTTPX_AVAILABLE = True
except ImportError:
    httpx = None
    HTTPX_AVAILABLE = False

logger = logging.getLogger("ControlNetService")


class ControlNetAPIError(Exception):
    """Exception containing HTTP status code and diagnostic detail."""
    def __init__(self, status_code: int, detail: str):
        self.status_code = status_code
        self.detail = detail
        super().__init__(f"HTTP {status_code}: {detail}")


# Active cloud endpoints hosting ControlNet scribble pipelines
CONTROLNET_SPACE_URL = "https://bytedance-hyper-sd15-scribble.hf.space"
CONTROLNET_ROUTER_URL = "https://router.huggingface.co/hf-inference/models/lllyasviel/control_v11p_sd15_scribble"

# Interior design prompt engineering for realistic generation
INTERIOR_PROMPT = (
    "photorealistic interior design photograph, modern furnished room, "
    "natural lighting through windows, hardwood flooring, elegant furniture "
    "with detailed wood grain and fabric textures, clearly defined chairs "
    "tables sofas and cabinets, architectural digest quality, "
    "high resolution, sharp focus, professional interior photography, 8k"
)

NEGATIVE_PROMPT = (
    "blurry, low quality, distorted, deformed, sketch lines visible, "
    "black and white, monochrome, drawing, cartoon, anime, painting, "
    "watercolor, pencil, artifacts, noise, pixelated, oversaturated, "
    "unrealistic colors, bad architecture, collapsed walls"
)


class ControlNetService:
    """Cloud-based ControlNet inference via Hugging Face GPU infrastructure."""

    def __init__(
        self,
        hf_token: Optional[str] = None,
        model_variant: str = "scribble",
        output_dir: Optional[Path] = None,
    ):
        self.hf_token = hf_token or os.environ.get("HF_TOKEN", "") or os.environ.get("HUGGINGFACE_HUB_TOKEN", "")
        self.model_variant = model_variant
        self.model_id = "lllyasviel/control_v11p_sd15_scribble"
        
        # Live endpoint URL (deprecated api-inference.huggingface.co permanently removed)
        self.space_url = CONTROLNET_SPACE_URL
        self.router_url = CONTROLNET_ROUTER_URL

        self.output_dir = output_dir or Path(__file__).resolve().parent.parent.parent / "outputs" / "controlnet_generated"
        self.output_dir.mkdir(parents=True, exist_ok=True)

        self.is_available = bool(self.hf_token)

    def set_token(self, token: str) -> None:
        """Update active HF token."""
        if token:
            self.hf_token = token.strip()
            self.is_available = True

    def preprocess_sketch(self, pil_image: Image.Image, target_size: int = 512) -> Image.Image:
        """Prepare sketch for ControlNet: resize to target resolution, ensure RGB."""
        img = pil_image.convert("RGB")
        img = img.resize((target_size, target_size), Image.LANCZOS)
        return img

    def _log_request(self, method: str, url: str):
        """Diagnostic logging of outgoing request without logging tokens."""
        parsed = urllib.parse.urlparse(url)
        logger.info(
            f"[ControlNet Outgoing Request] Method={method} | "
            f"Host={parsed.hostname} | Port={parsed.port or (443 if parsed.scheme == 'https' else 80)} | "
            f"Path={parsed.path}"
        )

    def _log_error(self, method: str, url: str, exc: Exception):
        """Diagnostic logging of exception type and host without logging tokens."""
        parsed = urllib.parse.urlparse(url)
        logger.error(
            f"[ControlNet Outgoing Error] Host={parsed.hostname} | URL={url} | "
            f"ExceptionType={type(exc).__name__} | Error={str(exc)}"
        )

    @staticmethod
    def _categorize_network_exception(exc: Exception, url: str) -> Tuple[int, str]:
        """Categorize network/connection exceptions into distinct, actionable error diagnoses."""
        hostname = urllib.parse.urlparse(url).hostname or "Hugging Face Cloud Host"
        err_str = str(exc)
        exc_name = type(exc).__name__

        # 1. DNS Resolution Failure (Errno 11001, gaierror, getaddrinfo failed)
        if "11001" in err_str or "getaddrinfo failed" in err_str or "gaierror" in exc_name.lower():
            return (
                503,
                f"DNS Resolution Error: Unable to resolve cloud host '{hostname}'. "
                "The server environment cannot perform DNS lookup. If running inside a local sandbox or behind a firewall, "
                "ensure outbound network connectivity is enabled (run with BypassSandbox: true or check internet connection)."
            )

        # 2. Connection Refused / Connect Error
        if "connection refused" in err_str.lower() or "connecterror" in exc_name.lower():
            return (
                502,
                f"Network Connection Failed: Could not establish TCP connection to '{hostname}'. "
                "The remote host may be unreachable, blocked by a local proxy/firewall, or temporarily offline."
            )

        # 3. Timeouts (ConnectTimeout, ReadTimeout)
        if "timeout" in err_str.lower() or "timeouterror" in exc_name.lower():
            return (
                504,
                f"Gateway Timeout: Request to '{hostname}' timed out while waiting for cloud response. "
                "Cloud GPU servers may be experiencing high queue congestion or latency."
            )

        # 4. SSL / TLS Verification Errors
        if "ssl" in err_str.lower() or "certificate" in err_str.lower():
            return (
                502,
                f"TLS/SSL Handshake Error: Failed to establish secure connection to '{hostname}': {err_str}"
            )

        # 5. Invalid / Malformed Header Value
        if "illegal header" in err_str.lower() or "localprotocolerror" in exc_name.lower():
            return (
                400,
                "Invalid Authentication Token: The Hugging Face token contains invalid characters or formatting."
            )

        # Generic network error
        return (
            502,
            f"Failed to connect to ControlNet cloud host ({hostname}): {exc_name} - {err_str}"
        )

    def check_zerogpu_quota_status(self, client: "httpx.Client", auth_headers: dict) -> Tuple[bool, str]:
        """Probes the Gradio queue to detect if ZeroGPU quota is exhausted."""
        try:
            safe_headers = dict(auth_headers or {})
            if safe_headers.get("Authorization", "").strip() in ("", "Bearer", "Bearer "):
                safe_headers.pop("Authorization", None)

            probe_session = f"quota_probe_{int(time.time() * 1000)}"
            probe_payload = {
                "data": [1, "quota_probe", 1.0, 1.0, 42, None, 1],
                "fn_index": 0,
                "session_hash": probe_session
            }
            join_resp = client.post(
                f"{self.space_url}/gradio_api/queue/join",
                headers=safe_headers,
                json=probe_payload,
                timeout=10.0
            )
            if join_resp.status_code == 200:
                with client.stream(
                    "GET",
                    f"{self.space_url}/gradio_api/queue/data?session_hash={probe_session}",
                    headers=auth_headers,
                    timeout=10.0
                ) as s:
                    for line in s.iter_lines():
                        if not line:
                            continue
                        if "output" in line and "ZeroGPU quota" in line:
                            try:
                                d = json.loads(line[5:])
                                err_msg = d.get("output", {}).get("error", "ZeroGPU quota exceeded")
                                return True, err_msg
                            except Exception:
                                return True, "ZeroGPU quota exceeded"
        except Exception as e:
            logger.debug(f"Quota probe exception: {e}")
        return False, ""

    def generate(
        self,
        pil_image: Image.Image,
        hf_token: Optional[str] = None,
        prompt: Optional[str] = None,
        negative_prompt: Optional[str] = None,
        num_inference_steps: int = 4,
        guidance_scale: float = 7.5,
        controlnet_conditioning_scale: float = 0.8,
        max_retries: int = 3,
    ) -> Tuple[np.ndarray, str]:
        """Generate a realistic interior image from a sketch using ControlNet.

        Returns (image_array_uint8, filename) on success.
        Raises ControlNetAPIError on failure (NEVER falls back to Pix2Pix).
        """
        token = (hf_token or "").strip() or self.hf_token or os.environ.get("HF_TOKEN", "")
        if not token:
            raise ControlNetAPIError(
                400,
                "HuggingFace API token is required for ControlNet generation. "
                "Please enter your token (starts with 'hf_') in the token field."
            )

        self.hf_token = token
        self.is_available = True

        if not HTTPX_AVAILABLE:
            raise ControlNetAPIError(500, "httpx library is required for ControlNet inference.")

        # 1. Preprocess input sketch to 512x512
        sketch_512 = self.preprocess_sketch(pil_image, target_size=512)
        buf = io.BytesIO()
        sketch_512.save(buf, format="PNG")
        sketch_bytes = buf.getvalue()

        final_prompt = prompt or INTERIOR_PROMPT
        auth_headers = {"Authorization": f"Bearer {token}"}

        # Attempt primary GPU Space pipeline
        with httpx.Client(timeout=120.0, follow_redirects=True) as client:
            upload_url = f"{self.space_url}/gradio_api/upload"
            self._log_request("POST", upload_url)

            try:
                upload_resp = client.post(
                    upload_url,
                    headers=auth_headers,
                    files={"files": ("sketch.png", sketch_bytes, "image/png")},
                    timeout=45.0,
                )
            except Exception as e:
                self._log_error("POST", upload_url, e)
                code, detail = self._categorize_network_exception(e, upload_url)
                raise ControlNetAPIError(code, detail)

            if upload_resp.status_code == 401:
                raise ControlNetAPIError(401, "Hugging Face authentication failed (HTTP 401). Please verify that your token is valid and active.")
            elif upload_resp.status_code == 429:
                raise ControlNetAPIError(429, "Hugging Face rate limit or ZeroGPU quota exceeded (HTTP 429). Please wait for quota refresh or provide a valid token.")
            elif upload_resp.status_code != 200:
                raise ControlNetAPIError(
                    upload_resp.status_code,
                    f"ControlNet sketch upload failed with HTTP {upload_resp.status_code}: {upload_resp.text[:200]}"
                )

            uploaded_path = upload_resp.json()[0]

            # 2. Dispatch ControlNet inference call
            call_url = f"{self.space_url}/gradio_api/call/process_image"
            file_obj = {
                "path": uploaded_path,
                "orig_name": "sketch.png",
                "mime_type": "image/png",
                "meta": {"_type": "gradio.FileData"},
            }
            payload = {
                "data": [
                    num_inference_steps,
                    final_prompt,
                    controlnet_conditioning_scale,
                    1.0,  # eta
                    42,   # seed
                    {
                        "background": file_obj,
                        "layers": [],
                        "composite": file_obj,
                    },
                    1     # num_images
                ]
            }

            self._log_request("POST", call_url)
            try:
                call_resp = client.post(call_url, headers=auth_headers, json=payload, timeout=45.0)
            except Exception as e:
                self._log_error("POST", call_url, e)
                code, detail = self._categorize_network_exception(e, call_url)
                raise ControlNetAPIError(code, f"Failed to dispatch inference job: {detail}")

            if call_resp.status_code == 401:
                raise ControlNetAPIError(401, "Hugging Face authentication failed (HTTP 401) during inference dispatch.")
            elif call_resp.status_code == 429:
                raise ControlNetAPIError(429, "Hugging Face ZeroGPU quota exhausted during job dispatch (HTTP 429).")
            elif call_resp.status_code != 200:
                raise ControlNetAPIError(
                    call_resp.status_code,
                    f"ControlNet dispatch failed with HTTP {call_resp.status_code}: {call_resp.text[:200]}"
                )

            event_id = call_resp.json().get("event_id")
            if not event_id:
                raise ControlNetAPIError(502, "ControlNet service did not return a valid job event ID.")

            # 3. Stream result until completion
            stream_url = f"{self.space_url}/gradio_api/call/process_image/{event_id}"
            self._log_request("GET", stream_url)

            image_file_path = None
            quota_err = ""
            try:
                with client.stream("GET", stream_url, headers=auth_headers, timeout=120.0) as stream:
                    for line in stream.iter_lines():
                        if not line:
                            continue
                        # Detect ZeroGPU quota error in stream payload
                        if "ZeroGPU quota" in line or "quota" in line.lower() and "exceeded" in line.lower():
                            try:
                                d = json.loads(line[5:]) if line.startswith("data:") else json.loads(line)
                                quota_err = d.get("output", {}).get("error", "ZeroGPU quota exceeded")
                            except Exception:
                                quota_err = "You have exceeded your ZeroGPU quota allowance"
                            break

                        if line.startswith("data:"):
                            try:
                                data = json.loads(line[5:])
                                if isinstance(data, list) and len(data) > 0:
                                    item = data[0]
                                    if isinstance(item, list) and len(item) > 0:
                                        img_info = item[0].get("image", {})
                                        image_file_path = img_info.get("path")
                                        if image_file_path:
                                            break
                            except Exception:
                                pass
            except Exception as e:
                self._log_error("GET", stream_url, e)
                code, detail = self._categorize_network_exception(e, stream_url)
                raise ControlNetAPIError(code, f"Stream connection error waiting for ControlNet result: {detail}")

            if quota_err:
                raise ControlNetAPIError(
                    429,
                    f"Hugging Face ZeroGPU quota exhausted: {quota_err}. "
                    "The cloud GPU allowance has been consumed. Please wait for quota refresh or provide a valid Hugging Face token."
                )

            if not image_file_path:
                # Probe queue status to distinguish ZeroGPU quota exhaustion from generic network failure
                is_quota, quota_msg = self.check_zerogpu_quota_status(client, auth_headers)
                if is_quota:
                    raise ControlNetAPIError(
                        429,
                        f"Hugging Face ZeroGPU quota exhausted: {quota_msg}. "
                        "The cloud GPU allowance has been consumed. Please wait for the quota reset or provide a Hugging Face token."
                    )
                raise ControlNetAPIError(502, "ControlNet generation failed: output image was not returned in stream.")

            # 4. Download generated image
            download_url = f"{self.space_url}/gradio_api/file={image_file_path}"
            self._log_request("GET", download_url)

            try:
                dl_resp = client.get(download_url, headers=auth_headers, timeout=60.0)
            except Exception as e:
                self._log_error("GET", download_url, e)
                code, detail = self._categorize_network_exception(e, download_url)
                raise ControlNetAPIError(code, f"Failed to download rendered ControlNet image: {detail}")

            if dl_resp.status_code != 200:
                raise ControlNetAPIError(
                    dl_resp.status_code,
                    f"Failed to fetch rendered image: HTTP {dl_resp.status_code}"
                )

            # 5. Process and save output image
            result_image = Image.open(io.BytesIO(dl_resp.content)).convert("RGB").resize((512, 512), Image.LANCZOS)
            result_np = np.array(result_image)

            # Strict quality check: ensure output is neither blank nor solid black/dark
            mean_val = float(result_np.mean())
            std_val = float(result_np.std())
            max_val = float(result_np.max())
            if std_val < 8.0 or mean_val < 10.0 or max_val < 25.0:
                raise ControlNetAPIError(
                    502,
                    f"Generated image failed quality check (output was blank or solid black: mean={mean_val:.1f}, std={std_val:.1f}, max={max_val:.1f})."
                )

            import uuid
            filename = f"controlnet_{uuid.uuid4().hex[:10]}.png"
            save_path = self.output_dir / filename
            result_image.save(save_path, format="PNG")

            logger.info(
                f"[ControlNet Success] Shape={result_np.shape} | Std={result_np.std():.1f} | Saved={filename}"
            )
            return result_np, filename

    def get_status(self) -> dict:
        """Return service status info."""
        parsed = urllib.parse.urlparse(self.space_url)
        return {
            "available": bool(self.hf_token),
            "model": "ControlNet Scribble + Stable Diffusion (Cloud GPU)",
            "endpoint_host": parsed.hostname,
            "has_token": bool(self.hf_token),
            "output_resolution": "512x512",
        }
