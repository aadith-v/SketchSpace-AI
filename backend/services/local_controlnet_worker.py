"""Standalone Local ControlNet Inference Worker for SketchSpace AI.
Executed strictly within venv_diffusion environment.
Loads local offline snapshots of SD 1.5 and ControlNet Scribble in FP16 with CPU offload.
"""

import argparse
import hashlib
import json
import os
import sys
import time
from pathlib import Path

# Enforce strict offline execution and prevent CUDA memory fragmentation
os.environ["HF_HUB_OFFLINE"] = "1"
os.environ["TRANSFORMERS_OFFLINE"] = "1"
os.environ["HF_HOME"] = r"Z:\SketchSpace_AI_Models\huggingface"
os.environ["PYTORCH_CUDA_ALLOC_CONF"] = "expandable_segments:True"

import psutil
import torch
from PIL import Image

PROJECT_ROOT = Path(__file__).resolve().parent.parent.parent
sys.path.insert(0, str(PROJECT_ROOT))
from backend.services.sketch_preprocessing_service import SketchPreprocessor, compute_image_sha256

SD_SNAPSHOT = Path(r"Z:\SketchSpace_AI_Models\huggingface\hub\models--stable-diffusion-v1-5--stable-diffusion-v1-5\snapshots\451f4fe16113bff5a5d2269ed5ad43b0592e9a14")
CN_SNAPSHOT = Path(r"Z:\SketchSpace_AI_Models\huggingface\hub\models--lllyasviel--control_v11p_sd15_scribble\snapshots\3564ec7b87dd706d5fc760d21c9e90bb160d1e9f")


def run_inference(args):
    sketch_path = Path(args.sketch_path)
    output_path = Path(args.output_path)
    output_path.parent.mkdir(parents=True, exist_ok=True)

    if not sketch_path.exists():
        raise FileNotFoundError(f"Input sketch not found at: {sketch_path}")

    # 1. Load raw sketch and compute input hash
    raw_img = Image.open(sketch_path).convert("RGB")
    input_sha256 = compute_image_sha256(raw_img)

    # 2. Intelligent Preprocessing: auto-crop borders, extract crisp linework, pad to 512x512
    # Generates white-on-black scribble strictly conforming to ControlNet Scribble v1.1
    control_image, prep_metadata = SketchPreprocessor.process_sketch(raw_img, target_size=512)
    conditioning_sha256 = compute_image_sha256(control_image)

    # Save conditioning image for audit and UI preview
    conditioning_path = output_path.parent / f"{output_path.stem}_conditioning.png"
    control_image.save(conditioning_path, format="PNG")

    # 3. Load Diffusers Pipeline
    from diffusers import ControlNetModel, StableDiffusionControlNetPipeline

    t_load_start = time.time()
    controlnet = ControlNetModel.from_pretrained(
        str(CN_SNAPSHOT),
        torch_dtype=torch.float16,
        variant="fp16",
        use_safetensors=True,
        local_files_only=True
    )

    pipe = StableDiffusionControlNetPipeline.from_pretrained(
        str(SD_SNAPSHOT),
        controlnet=controlnet,
        torch_dtype=torch.float16,
        variant="fp16",
        use_safetensors=True,
        safety_checker=None,
        local_files_only=True
    )

    # Sequential CPU offload ensures peak allocated VRAM stays ~600-900 MB on 4GB RTX 3050
    pipe.enable_sequential_cpu_offload()
    pipe.enable_attention_slicing(1)
    if hasattr(pipe, "enable_vae_slicing"):
        pipe.enable_vae_slicing()
    elif hasattr(pipe.vae, "enable_slicing"):
        pipe.vae.enable_slicing()
    if hasattr(pipe, "enable_vae_tiling"):
        pipe.enable_vae_tiling()
    elif hasattr(pipe.vae, "enable_tiling"):
        pipe.vae.enable_tiling()
    t_load = time.time() - t_load_start

    # 4. Generate Image with torch.inference_mode()
    if torch.cuda.is_available():
        torch.cuda.reset_peak_memory_stats()

    generator = None
    seed_used = args.seed
    if args.seed is not None and args.seed >= 0:
        generator = torch.Generator(device="cpu").manual_seed(args.seed)
    else:
        import random
        seed_used = random.randint(1, 2147483647)
        generator = torch.Generator(device="cpu").manual_seed(seed_used)

    t_gen_start = time.time()
    with torch.inference_mode():
        result = pipe(
            prompt=args.prompt,
            negative_prompt=args.negative_prompt,
            image=control_image,
            num_inference_steps=args.steps,
            guidance_scale=args.guidance_scale,
            controlnet_conditioning_scale=args.conditioning_scale,
            generator=generator,
            height=512,
            width=512,
        )
    t_gen = time.time() - t_gen_start

    # 5. Save Output & Compute Output Hash
    generated_image = result.images[0]
    generated_image.save(output_path, format="PNG")
    output_sha256 = compute_image_sha256(generated_image)

    vram_peak_mb = (torch.cuda.max_memory_allocated() / (1024**2)) if torch.cuda.is_available() else 0
    vram_res_mb = (torch.cuda.max_memory_reserved() / (1024**2)) if torch.cuda.is_available() else 0
    ram_peak_gb = psutil.virtual_memory().used / (1024**3)

    # Cleanup memory
    del result
    del pipe
    del controlnet
    if torch.cuda.is_available():
        torch.cuda.empty_cache()
    import gc
    gc.collect()

    return {
        "success": True,
        "output_path": str(output_path),
        "conditioning_path": str(conditioning_path),
        "conditioning_filename": conditioning_path.name,
        "input_sha256": input_sha256,
        "conditioning_sha256": conditioning_sha256,
        "output_sha256": output_sha256,
        "seed_used": seed_used,
        "conditioning_scale": args.conditioning_scale,
        "guidance_scale": args.guidance_scale,
        "steps": args.steps,
        "load_time_sec": round(t_load, 2),
        "gen_time_sec": round(t_gen, 2),
        "vram_peak_allocated_mb": round(vram_peak_mb, 1),
        "vram_peak_reserved_mb": round(vram_res_mb, 1),
        "ram_peak_gb": round(ram_peak_gb, 2),
        "stroke_density": prep_metadata.get("stroke_density", 0.0),
        "stroke_pixels": prep_metadata.get("stroke_pixels", 0)
    }


def main():
    parser = argparse.ArgumentParser(description="SketchSpace Local ControlNet Worker")
    parser.add_argument("--sketch-path", required=True, help="Path to input sketch PNG")
    parser.add_argument("--output-path", required=True, help="Path to write output PNG")
    parser.add_argument("--prompt", required=True, help="Text generation prompt")
    parser.add_argument("--negative-prompt", default="", help="Negative text prompt")
    parser.add_argument("--steps", type=int, default=18, help="Number of inference steps")
    parser.add_argument("--guidance-scale", type=float, default=7.5, help="Guidance scale")
    parser.add_argument("--conditioning-scale", type=float, default=1.15, help="ControlNet conditioning scale")
    parser.add_argument("--seed", type=int, default=-1, help="Random seed (-1 for random)")

    args = parser.parse_args()

    try:
        metrics = run_inference(args)
        print("__RESULT_JSON__" + json.dumps(metrics))
    except Exception as e:
        import traceback
        err_info = {
            "success": False,
            "error_type": type(e).__name__,
            "error_detail": str(e),
            "traceback": traceback.format_exc()
        }
        print("__ERROR_JSON__" + json.dumps(err_info), file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
