"""FastAPI API Routes for SketchSpace AI.
Provides:
- GET  /api/health
- GET  /api/status
- GET  /api/examples
- GET  /api/sketches/example/{filename}
- POST /api/upload
- POST /api/generate
- POST /api/generate?model=controlnet
- GET  /api/models
- POST /api/switch-model
- GET  /api/image/{filename}
"""

import io
import os
from pathlib import Path
from typing import Optional
from fastapi import APIRouter, File, UploadFile, HTTPException, Query
from fastapi.responses import FileResponse, JSONResponse
from PIL import Image

PROJECT_ROOT = Path(__file__).resolve().parent.parent.parent
from configs.config import (
    OUTPUTS_DIR,
    CHECKPOINTS_DIR,
    CHECKPOINTS_EXP1_DIR,
    CHECKPOINTS_EXP2_DIR,
    CHECKPOINTS_EXP4_DIR,
    CHECKPOINTS_EXP5_DIR,
    FILTERED_EXP2_TEST_SKETCHES_DIR,
    FILTERED_TEST_SKETCHES_DIR,
    TEST_SKETCHES_DIR,
    TRAIN_SKETCHES_DIR
)
from backend.services.model_service import ModelService
from backend.services.sketch_service import SketchService, UPLOAD_DIR
from backend.services.controlnet_service import ControlNetService, ControlNetAPIError
from backend.services.local_controlnet_service import LocalControlNetService, LocalControlNetError, LocalControlNetBusyError

router = APIRouter()

# Singleton ControlNet service
_controlnet_service = None

def get_controlnet_service() -> ControlNetService:
    global _controlnet_service
    if _controlnet_service is None:
        _controlnet_service = ControlNetService()
    return _controlnet_service


@router.get("/health")
def health_check():
    """Health check endpoint."""
    return {"status": "healthy", "service": "SketchSpace AI"}


@router.get("/status")
def model_status():
    """Returns current model checkpoint and device status."""
    service = ModelService.get_instance()
    cn_service = get_controlnet_service()
    local_cn_service = LocalControlNetService.get_instance()
    status = service.get_status()
    status["controlnet"] = cn_service.get_status()
    status["local_controlnet"] = local_cn_service.get_status()
    return status


@router.get("/controlnet/diagnostics")
def controlnet_diagnostics():
    """Diagnostic check for DNS resolution, HTTPS reachability, and Space availability."""
    import socket
    import urllib.request
    import urllib.parse

    cn_service = get_controlnet_service()
    host = urllib.parse.urlparse(cn_service.space_url).hostname

    dns_ok = False
    dns_info = ""
    try:
        ip = socket.gethostbyname(host)
        dns_ok = True
        dns_info = f"Resolved {host} to {ip}"
    except Exception as e:
        dns_info = f"DNS failed: {type(e).__name__} - {str(e)}"

    https_ok = False
    https_info = ""
    if dns_ok:
        try:
            req = urllib.request.Request(
                f"{cn_service.space_url}/config",
                headers={"User-Agent": "SketchSpaceDiagnostic/1.0"}
            )
            with urllib.request.urlopen(req, timeout=8) as resp:
                https_ok = (resp.status == 200)
                https_info = f"HTTP {resp.status} OK (Gradio config accessible)"
        except Exception as e:
            https_info = f"HTTPS connection failed: {type(e).__name__} - {str(e)}"
    else:
        https_info = "Skipped due to DNS failure"

    return {
        "endpoint": cn_service.space_url,
        "hostname": host,
        "dns": {"ok": dns_ok, "details": dns_info},
        "https": {"ok": https_ok, "details": https_info},
        "has_token_configured": bool(cn_service.hf_token)
    }


@router.get("/models")
def list_available_models():
    """List all available model options for inference."""
    models = []

    # Pix2Pix Experiment 3 (Default & Recommended)
    exp3_path = CHECKPOINTS_DIR / "experiment_3" / "generator_best.pth"
    if exp3_path.exists():
        models.append({
            "id": "pix2pix-exp3",
            "name": "Experiment 3 (Compound Loss U-Net)",
            "description": "Local Pix2Pix GAN with edge+SSIM compound loss, 256x256, best edge sharpness, offline CPU inference (~75ms)",
            "type": "local",
            "resolution": "256x256",
            "is_default": True,
            "badge": "Recommended Local",
        })

    # Pix2Pix Experiment 5 (Photographic Interior)
    exp5_path = CHECKPOINTS_EXP5_DIR / "generator_best.pth"
    if exp5_path.exists():
        models.append({
            "id": "pix2pix-exp5",
            "name": "Experiment 5 — Photographic Interior",
            "description": "Fine-tuned on 75-pair balanced photographic dataset. Authentic furniture textures, wood grain, tile sheen & directional lighting, 256x256, offline CPU (~75ms)",
            "type": "local",
            "resolution": "256x256",
            "is_default": False,
            "badge": "Photographic Model",
        })

    # Pix2Pix Experiment 4 (Photographic Pilot)
    exp4_path = CHECKPOINTS_EXP4_DIR / "generator_best.pth"
    if exp4_path.exists():
        models.append({
            "id": "pix2pix-exp4",
            "name": "Experiment 4 (Photographic Pilot)",
            "description": "35-pair pilot fine-tune on authentic room photographs, 256x256, offline CPU (~75ms)",
            "type": "local",
            "resolution": "256x256",
            "is_default": False,
            "badge": "Pilot Model",
        })

    # Pix2Pix Experiment 2
    exp2_path = CHECKPOINTS_EXP2_DIR / "generator_best.pth"
    if exp2_path.exists():
        models.append({
            "id": "pix2pix-exp2",
            "name": "Experiment 2 (Nearest-Neighbor U-Net)",
            "description": "Local Pix2Pix GAN with nearest-neighbor upsampling (smooth planar surfaces, zero checkerboard), 256x256, offline CPU inference (~75ms)",
            "type": "local",
            "resolution": "256x256",
            "is_default": False,
            "badge": "Smooth Baseline",
        })

    # Pix2Pix Experiment 1
    exp1_path = CHECKPOINTS_EXP1_DIR / "generator_best.pth"
    if exp1_path.exists():
        models.append({
            "id": "pix2pix-exp1",
            "name": "Experiment 1 (ConvTranspose2d Baseline)",
            "description": "Local Pix2Pix GAN baseline with transposed convolution (displays Nyquist grid noise), 256x256, offline CPU inference (~50ms)",
            "type": "local",
            "resolution": "256x256",
            "is_default": False,
            "badge": "Ablation Baseline",
        })

    # Local ControlNet + SD 1.5 (Offline GPU)
    local_cn_service = LocalControlNetService.get_instance()
    local_cn_status = local_cn_service.get_status()
    models.append({
        "id": "controlnet-local",
        "name": "Local ControlNet + SD 1.5 (RTX 3050 GPU, Offline)",
        "description": "High-fidelity Stable Diffusion 1.5 + ControlNet Scribble (512x512). 100% offline local inference on NVIDIA RTX 3050 (4GB VRAM with CPU offload). No token or internet required.",
        "type": "local_diffusion",
        "resolution": "512x512",
        "available": local_cn_status["available"],
        "is_default": False,
        "badge": "Local GPU (Offline)",
        "categories": local_cn_status["categories"],
    })

    # ControlNet (optional cloud)
    cn_service = get_controlnet_service()
    cn_status = cn_service.get_status()
    models.append({
        "id": "controlnet",
        "name": "ControlNet Cloud — Optional, Internet & GPU Quota Required",
        "description": "Optional cloud-hosted ControlNet Scribble + Stable Diffusion (512x512). Requires internet connectivity and active Hugging Face GPU quota.",
        "type": "cloud",
        "resolution": "512x512",
        "available": cn_status["available"],
        "is_default": False,
        "badge": "Optional Cloud GPU",
    })

    return {"models": models}


@router.post("/switch-model")
def switch_pix2pix_model(model_id: str = Query(...)):
    """Switch the active Pix2Pix checkpoint (does not affect ControlNet)."""
    norm_id = model_id.strip().lower()
    checkpoint_map = {
        "pix2pix": CHECKPOINTS_DIR / "experiment_3" / "generator_best.pth",
        "pix2pix-exp3": CHECKPOINTS_DIR / "experiment_3" / "generator_best.pth",
        "exp3": CHECKPOINTS_DIR / "experiment_3" / "generator_best.pth",
        "pix2pix-exp5": CHECKPOINTS_EXP5_DIR / "generator_best.pth",
        "exp5": CHECKPOINTS_EXP5_DIR / "generator_best.pth",
        "pix2pix-exp4": CHECKPOINTS_EXP4_DIR / "generator_best.pth",
        "exp4": CHECKPOINTS_EXP4_DIR / "generator_best.pth",
        "pix2pix-exp2": CHECKPOINTS_EXP2_DIR / "generator_best.pth",
        "exp2": CHECKPOINTS_EXP2_DIR / "generator_best.pth",
        "pix2pix-exp1": CHECKPOINTS_EXP1_DIR / "generator_best.pth",
        "exp1": CHECKPOINTS_EXP1_DIR / "generator_best.pth",
    }

    if norm_id not in checkpoint_map:
        raise HTTPException(status_code=400, detail=f"Unknown model_id: {model_id}. Valid: {list(checkpoint_map.keys())}")

    ckpt_path = checkpoint_map[norm_id]
    if not ckpt_path.exists():
        raise HTTPException(status_code=404, detail=f"Checkpoint not found: {ckpt_path}")

    # Reload ModelService with new checkpoint
    service = ModelService.get_instance()
    service.checkpoint_path = ckpt_path
    service.load_model()

    return {
        "success": True,
        "active_model": norm_id,
        "checkpoint": service.checkpoint_info,
    }


@router.get("/examples")
def list_examples():
    """Return available example sketches for user demonstration."""
    examples = SketchService.get_example_sketches()
    return {"examples": examples}


@router.get("/sketches/example/{filename}")
def get_example_sketch(filename: str):
    """Serve pre-rendered example sketch files."""
    examples_dir = PROJECT_ROOT / "examples"
    target = examples_dir / filename
    if target.exists():
        return FileResponse(target, media_type="image/png")
    raise HTTPException(status_code=404, detail="Example sketch not found")


@router.post("/upload")
def upload_sketch(file: UploadFile = File(...)):
    """Upload and validate a room sketch."""
    try:
        content = file.file.read()
        saved_path, pil_img = SketchService.validate_and_save_upload(content, file.filename)
        return {
            "success": True,
            "filename": saved_path.name,
            "dimensions": list(pil_img.size),
            "sketch_url": f"/api/uploads/{saved_path.name}"
        }
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Upload failed: {str(e)}")


@router.post("/generate")
def generate_interior(
    file: UploadFile = File(...),
    model: str = Query("pix2pix-exp3", description="Model to use: 'pix2pix-exp3' (default), 'pix2pix-exp5', 'controlnet-local', or 'controlnet'"),
    hf_token: Optional[str] = Query(None, description="HuggingFace API token for ControlNet cloud inference"),
    category: Optional[str] = Query(None, description="Room category for local ControlNet (bedroom, living_room, office, kitchen, bathroom)"),
    prompt: Optional[str] = Query(None, description="Custom prompt override for local ControlNet"),
    negative_prompt: Optional[str] = Query(None, description="Custom negative prompt override for local ControlNet"),
    steps: int = Query(15, ge=5, le=50, description="Inference steps for local ControlNet (default: 15)")
):
    """Generate realistic interior image from uploaded room sketch.
    
    Default: model='pix2pix-exp3' for local CPU inference (256x256, Compound Loss).
    Local GPU: model='controlnet-local' for offline ControlNet + SD 1.5 (512x512, RTX 3050).
    Optional: model='controlnet' for cloud GPU generation (512x512).
    """
    try:
        content = file.file.read()
        saved_sketch_path, pil_img = SketchService.validate_and_save_upload(content, file.filename)
    except ValueError as ve:
        raise HTTPException(status_code=400, detail=str(ve))

    target_model = (model or "pix2pix-exp3").strip().lower()
    if target_model in ("pix2pix", "default"):
        target_model = "pix2pix-exp3"

    if target_model in ("controlnet-local", "local-controlnet", "diffusion"):
        # Local Offline ControlNet + SD 1.5 GPU inference
        local_cn_service = LocalControlNetService.get_instance()
        try:
            gen_filename, metrics = local_cn_service.generate(
                pil_img,
                category=category,
                custom_prompt=prompt,
                custom_negative_prompt=negative_prompt,
                num_inference_steps=steps,
                input_filename=saved_sketch_path.name
            )
        except LocalControlNetBusyError as be:
            raise HTTPException(status_code=503, detail=be.detail)
        except LocalControlNetError as le:
            raise HTTPException(status_code=le.status_code, detail=le.detail)
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Local ControlNet generation failed: {str(e)}")

        return {
            "success": True,
            "sketch_filename": saved_sketch_path.name,
            "sketch_url": f"/api/uploads/{saved_sketch_path.name}",
            "generated_filename": gen_filename,
            "generated_url": f"/api/image/{gen_filename}",
            "raw_url": f"/api/image/{gen_filename}",
            "model_used": "Local ControlNet + Stable Diffusion 1.5 (RTX 3050)",
            "resolution": "512x512",
            "metrics": metrics,
            "message": "High-quality realistic interior synthesized via local offline ControlNet pipeline."
        }
    elif target_model == "controlnet":
        # Cloud GPU inference via ControlNet
        cn_service = get_controlnet_service()
        active_token = (hf_token or "").strip() or os.environ.get("HF_TOKEN", "") or os.environ.get("HUGGINGFACE_HUB_TOKEN", "")
        if not active_token:
            raise HTTPException(
                status_code=400,
                detail="HuggingFace API token is required for ControlNet cloud GPU inference. Please enter your HuggingFace token (starts with 'hf_') in the token field."
            )

        try:
            fake_uint8, gen_filename = cn_service.generate(pil_img, hf_token=active_token)
        except ControlNetAPIError as cne:
            raise HTTPException(status_code=cne.status_code, detail=cne.detail)
        except Exception as e:
            raise HTTPException(status_code=502, detail=f"ControlNet cloud generation failed: {str(e)}")

        # Copy to web_generated for consistent serving
        gen_dir = OUTPUTS_DIR / "web_generated"
        gen_dir.mkdir(parents=True, exist_ok=True)
        import shutil
        src = cn_service.output_dir / gen_filename
        dst = gen_dir / gen_filename
        if src.exists():
            shutil.copy2(src, dst)

        return {
            "success": True,
            "sketch_filename": saved_sketch_path.name,
            "sketch_url": f"/api/uploads/{saved_sketch_path.name}",
            "generated_filename": gen_filename,
            "generated_url": f"/api/image/{gen_filename}",
            "model_used": "ControlNet + Stable Diffusion (Cloud GPU)",
            "resolution": f"{fake_uint8.shape[1]}x{fake_uint8.shape[0]}",
            "message": "High-quality interior generated via ControlNet cloud inference."
        }
    else:
        # Local Pix2Pix inference
        checkpoint_map = {
            "pix2pix": CHECKPOINTS_DIR / "experiment_3" / "generator_best.pth",
            "pix2pix-exp3": CHECKPOINTS_DIR / "experiment_3" / "generator_best.pth",
            "exp3": CHECKPOINTS_DIR / "experiment_3" / "generator_best.pth",
            "pix2pix-exp5": CHECKPOINTS_EXP5_DIR / "generator_best.pth",
            "exp5": CHECKPOINTS_EXP5_DIR / "generator_best.pth",
            "pix2pix-exp4": CHECKPOINTS_EXP4_DIR / "generator_best.pth",
            "exp4": CHECKPOINTS_EXP4_DIR / "generator_best.pth",
            "pix2pix-exp2": CHECKPOINTS_EXP2_DIR / "generator_best.pth",
            "exp2": CHECKPOINTS_EXP2_DIR / "generator_best.pth",
            "pix2pix-exp1": CHECKPOINTS_EXP1_DIR / "generator_best.pth",
            "exp1": CHECKPOINTS_EXP1_DIR / "generator_best.pth",
        }

        service = ModelService.get_instance()
        target_ckpt = checkpoint_map.get(target_model)
        if target_ckpt and target_ckpt.exists() and service.checkpoint_path != target_ckpt:
            service.checkpoint_path = target_ckpt
            service.load_model()

        if not service.is_loaded:
            raise HTTPException(
                status_code=503,
                detail="Trained Pix2Pix model checkpoint is not loaded. Please train the model before running inference."
            )

        try:
            fake_uint8, gen_filename = service.generate(pil_img)

            # Generate CPU-compatible enhanced variant
            from backend.services.image_enhancement_service import enhance_interior_image
            raw_pil = Image.fromarray(fake_uint8)
            enh_pil = enhance_interior_image(raw_pil, apply_clahe=True, apply_saturation_boost=True, apply_edge_preserve=True)
            enh_filename = gen_filename.replace(".png", "_enhanced.png")
            enh_path = service.generated_dir / enh_filename
            enh_pil.save(enh_path, format="PNG")

            return {
                "success": True,
                "sketch_filename": saved_sketch_path.name,
                "sketch_url": f"/api/uploads/{saved_sketch_path.name}",
                "generated_filename": gen_filename,
                "generated_url": f"/api/image/{gen_filename}",
                "raw_url": f"/api/image/{gen_filename}",
                "enhanced_url": f"/api/image/{enh_filename}",
                "enhanced_filename": enh_filename,
                "has_enhanced": True,
                "model_used": service.checkpoint_info.get("model_version", "Pix2Pix"),
                "resolution": "256x256",
                "message": "Realistic interior generated successfully."
            }
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Generation failed: {str(e)}")


@router.get("/image/{filename}")
def get_generated_image(filename: str):
    """Retrieve generated interior output."""
    gen_dir = OUTPUTS_DIR / "web_generated"
    file_path = gen_dir / filename
    if not file_path.exists():
        raise HTTPException(status_code=404, detail="Generated image not found")
    return FileResponse(file_path, media_type="image/png")


@router.get("/uploads/{filename}")
def get_uploaded_image(filename: str):
    """Retrieve uploaded sketch image."""
    file_path = UPLOAD_DIR / filename
    if not file_path.exists():
        raise HTTPException(status_code=404, detail="Uploaded sketch image not found")
    return FileResponse(file_path, media_type="image/png")

