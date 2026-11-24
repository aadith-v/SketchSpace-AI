"""Local ControlNet Service for SketchSpace AI.
Executes Stable Diffusion 1.5 + ControlNet Scribble strictly offline via venv_diffusion.

Key Features:
- 100% Offline (local snapshots, HF_HUB_OFFLINE=1, no cloud APIs or tokens).
- Concurrency Control: Strictly one generation at a time using a thread lock; returns 503 if busy.
- Memory Isolation: Runs worker in venv_diffusion subprocess, releasing memory immediately on completion.
- Category-Aware Interior Prompts: Tailored presets for bedroom, living room, office, kitchen, bathroom.
- Fail-Fast Guarantee: Never falls back to Pix2Pix or placeholders; returns explicit diagnostic errors.
"""

import json
import logging
import os
import subprocess
import threading
import time
from pathlib import Path
from typing import Dict, Optional, Tuple, Any

from PIL import Image

PROJECT_ROOT = Path(__file__).resolve().parent.parent.parent
from configs.config import OUTPUTS_DIR

logger = logging.getLogger("LocalControlNetService")

# Presets for high-fidelity photorealistic room synthesis
CATEGORY_PROMPTS: Dict[str, str] = {
    "bedroom": (
        "photorealistic modern bedroom interior, comfortable bed, pillows, "
        "bedside table and lamp, natural daylight from window, hardwood floor, "
        "architectural digest quality, high resolution, sharp focus, 8k"
    ),
    "living_room": (
        "photorealistic modern living room interior, stylish sofa, coffee table, "
        "indoor plants, natural daylight, hardwood flooring, elegant decor, "
        "architectural digest quality, high resolution, sharp focus, 8k"
    ),
    "office": (
        "photorealistic modern office workspace, executive desk, ergonomic chair, "
        "computer monitors and bookshelf, clean minimalist design, natural window lighting, "
        "high resolution, sharp focus, 8k"
    ),
    "kitchen": (
        "photorealistic modern kitchen interior, marble countertops, modern cabinets, "
        "stainless steel appliances, warm recessed lighting, clean minimalist surfaces, "
        "high resolution, sharp focus, 8k"
    ),
    "bathroom": (
        "photorealistic modern bathroom interior, porcelain sink, vanity mirror, "
        "glass shower enclosure, ceramic wall tiles, clean chrome fixtures, "
        "bright sanitary illumination, high resolution, sharp focus, 8k"
    ),
    "dining": (
        "photorealistic modern dining room, elegant dining table, designer chairs, "
        "pendant lighting, hardwood floor, architectural digest photography, "
        "high resolution, sharp focus, 8k"
    ),
}

DEFAULT_NEGATIVE_PROMPT = (
    "sketch, drawing, line art, cartoon, 3d render, blurry, deformed, "
    "distorted architecture, duplicate furniture, noisy textures, oversaturated, "
    "low quality, watermark, text"
)


class LocalControlNetError(Exception):
    """Raised when local ControlNet inference fails."""
    def __init__(self, status_code: int, detail: str):
        self.status_code = status_code
        self.detail = detail
        super().__init__(f"HTTP {status_code}: {detail}")


class LocalControlNetBusyError(LocalControlNetError):
    """Raised when an inference is already actively in progress."""
    def __init__(self):
        super().__init__(
            status_code=503,
            detail="Local GPU ControlNet is currently busy synthesizing an image. Please wait a few seconds and try again."
        )


class LocalControlNetService:
    """Manages offline ControlNet execution via venv_diffusion."""

    _instance: Optional["LocalControlNetService"] = None
    _lock = threading.Lock()

    def __init__(self):
        self.venv_python = PROJECT_ROOT / "venv_diffusion" / "Scripts" / "python.exe"
        self.worker_script = Path(__file__).resolve().parent / "local_controlnet_worker.py"
        self.output_dir = OUTPUTS_DIR / "web_generated"
        self.output_dir.mkdir(parents=True, exist_ok=True)
        self.is_busy = False

        self.sd_snapshot = Path(r"Z:\SketchSpace_AI_Models\huggingface\hub\models--stable-diffusion-v1-5--stable-diffusion-v1-5\snapshots\451f4fe16113bff5a5d2269ed5ad43b0592e9a14")
        self.cn_snapshot = Path(r"Z:\SketchSpace_AI_Models\huggingface\hub\models--lllyasviel--control_v11p_sd15_scribble\snapshots\3564ec7b87dd706d5fc760d21c9e90bb160d1e9f")

    @classmethod
    def get_instance(cls) -> "LocalControlNetService":
        if cls._instance is None:
            cls._instance = LocalControlNetService()
        return cls._instance

    def get_status(self) -> Dict[str, Any]:
        return {
            "available": self.venv_python.exists() and self.sd_snapshot.exists() and self.cn_snapshot.exists(),
            "venv_python": str(self.venv_python),
            "venv_ready": self.venv_python.exists(),
            "sd_ready": self.sd_snapshot.exists(),
            "controlnet_ready": self.cn_snapshot.exists(),
            "is_busy": self.is_busy,
            "offline_mode": True,
            "vram_limit": "4GB (Offloaded to CPU)",
            "categories": list(CATEGORY_PROMPTS.keys()),
        }

    def normalize_category(self, cat_raw: Optional[str]) -> str:
        """Normalize category strings including aliases."""
        if not cat_raw:
            return "bedroom"
        c = cat_raw.strip().lower().replace("-", "_").replace(" ", "_")
        if c in CATEGORY_PROMPTS:
            return c
        if "office" in c or "work" in c or "desk" in c:
            return "office"
        if "bed" in c:
            return "bedroom"
        if "living" in c:
            return "living_room"
        if "kitchen" in c or "cook" in c:
            return "kitchen"
        if "bath" in c or "wash" in c or "toilet" in c:
            return "bathroom"
        if "dining" in c:
            return "dining"
        return "bedroom"

    def detect_category(self, filename: Optional[str]) -> str:
        """Infer room category from filename if available."""
        if not filename:
            return "bedroom"
        return self.normalize_category(filename)

    def get_prompt_for_category(self, category: Optional[str]) -> str:
        cat_key = self.normalize_category(category)
        return CATEGORY_PROMPTS.get(cat_key, CATEGORY_PROMPTS["bedroom"])

    def generate(
        self,
        pil_image: Image.Image,
        category: Optional[str] = None,
        custom_prompt: Optional[str] = None,
        custom_negative_prompt: Optional[str] = None,
        num_inference_steps: int = 15,
        guidance_scale: float = 7.0,
        conditioning_scale: float = 1.0,
        seed: int = 42,
        input_filename: Optional[str] = None,
    ) -> Tuple[str, Dict[str, Any]]:
        """Run local ControlNet generation.
        
        Guaranteed Concurrency Control: Only 1 task executes at a time.
        Returns: (output_filename, metrics_dict)
        """
        if not self.venv_python.exists():
            raise LocalControlNetError(500, f"Diffusion virtual environment not found at: {self.venv_python}")

        # Non-blocking lock check
        acquired = self._lock.acquire(blocking=False)
        if not acquired:
            raise LocalControlNetBusyError()

        self.is_busy = True
        try:
            timestamp = int(time.time() * 1000)
            in_cat = category or self.detect_category(input_filename)
            gen_filename = f"local_cn_{in_cat}_{timestamp}.png"
            out_file = self.output_dir / gen_filename

            # Save input sketch to temporary file for worker
            temp_sketch_path = OUTPUTS_DIR / "web_uploads" / f"temp_input_{timestamp}.png"
            temp_sketch_path.parent.mkdir(parents=True, exist_ok=True)
            pil_image.convert("RGB").save(temp_sketch_path, format="PNG")

            prompt = (custom_prompt or "").strip() or self.get_prompt_for_category(in_cat)
            negative_prompt = (custom_negative_prompt or "").strip() or DEFAULT_NEGATIVE_PROMPT

            cmd = [
                str(self.venv_python),
                str(self.worker_script),
                "--sketch-path", str(temp_sketch_path),
                "--output-path", str(out_file),
                "--prompt", prompt,
                "--negative-prompt", negative_prompt,
                "--steps", str(num_inference_steps),
                "--guidance-scale", str(guidance_scale),
                "--conditioning-scale", str(conditioning_scale),
                "--seed", str(seed),
            ]

            logger.info(f"Launching local ControlNet inference: {prompt[:60]}...")
            proc = subprocess.run(
                cmd,
                capture_output=True,
                text=True,
                timeout=180,  # 3 minute timeout
            )

            # Cleanup temp input
            if temp_sketch_path.exists():
                try:
                    temp_sketch_path.unlink()
                except Exception:
                    pass

            if proc.returncode != 0:
                err_detail = "Inference process failed."
                for line in proc.stderr.splitlines():
                    if "__ERROR_JSON__" in line:
                        try:
                            idx = line.find("__ERROR_JSON__")
                            err_info = json.loads(line[idx + len("__ERROR_JSON__"):])
                            err_detail = f"{err_info.get('error_type')}: {err_info.get('error_detail')}"
                            break
                        except Exception:
                            pass
                if err_detail == "Inference process failed." and proc.stderr.strip():
                    # Extract last meaningful error line from stderr
                    stderr_lines = [l.strip() for l in proc.stderr.splitlines() if l.strip()]
                    if stderr_lines:
                        err_detail = stderr_lines[-1]
                if "CUDA out of memory" in proc.stderr:
                    err_detail = "CUDA out of memory error on RTX 3050. Ensure no other GPU programs are consuming VRAM."
                logger.error(f"Local ControlNet worker failed: {proc.stderr}")
                raise LocalControlNetError(500, f"Local ControlNet synthesis failed: {err_detail}")

            # Parse metrics from stdout
            metrics = {}
            for line in proc.stdout.splitlines():
                if line.startswith("__RESULT_JSON__"):
                    try:
                        metrics = json.loads(line[len("__RESULT_JSON__"):])
                    except Exception:
                        pass

            if not out_file.exists():
                raise LocalControlNetError(500, "Local ControlNet worker exited with 0 but output image was not found.")

            metrics["category"] = in_cat
            metrics["prompt"] = prompt
            return gen_filename, metrics

        finally:
            self.is_busy = False
            self._lock.release()
