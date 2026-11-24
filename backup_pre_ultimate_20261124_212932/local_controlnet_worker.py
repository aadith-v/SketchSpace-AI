"""Standalone Local ControlNet Inference Worker for SketchSpace AI.
Executed strictly within venv_diffusion environment.
Loads local offline snapshots of SD 1.5 and ControlNet Scribble in FP16 with CPU offload.
"""

import argparse
import json
import os
import sys
import time
from pathlib import Path

# Enforce strict offline execution
os.environ["HF_HUB_OFFLINE"] = "1"
os.environ["TRANSFORMERS_OFFLINE"] = "1"
os.environ["HF_HOME"] = r"Z:\SketchSpace_AI_Models\huggingface"

import psutil
import torch
from PIL import Image, ImageOps

SD_SNAPSHOT = Path(r"Z:\SketchSpace_AI_Models\huggingface\hub\models--stable-diffusion-v1-5--stable-diffusion-v1-5\snapshots\451f4fe16113bff5a5d2269ed5ad43b0592e9a14")
CN_SNAPSHOT = Path(r"Z:\SketchSpace_AI_Models\huggingface\hub\models--lllyasviel--control_v11p_sd15_scribble\snapshots\3564ec7b87dd706d5fc760d21c9e90bb160d1e9f")

def run_inference(args):
    sketch_path = Path(args.sketch_path)
    output_path = Path(args.output_path)
    output_path.parent.mkdir(parents=True, exist_ok=True)

    if not sketch_path.exists():
        raise FileNotFoundError(f"Input sketch not found at: {sketch_path}")

    # 1. Preprocess Sketch to 512x512 with aspect ratio preservation
    raw_img = Image.open(sketch_path).convert("RGB")
    w, h = raw_img.size
    target_size = 512
    if w == h:
        sketch_512 = raw_img.resize((target_size, target_size), Image.LANCZOS)
    else:
        ratio = min(target_size / w, target_size / h)
        new_w, new_h = int(w * ratio), int(h * ratio)
        resized = raw_img.resize((new_w, new_h), Image.LANCZOS)
        sketch_512 = Image.new("RGB", (target_size, target_size), (255, 255, 255))
        pad_x = (target_size - new_w) // 2
        pad_y = (target_size - new_h) // 2
        sketch_512.paste(resized, (pad_x, pad_y))

    # ControlNet scribble v1.1 expectation: 0 = background (black), 255 = stroke (white)
    gray = sketch_512.convert("L")
    import numpy as np
    arr = np.array(gray)
    if arr.mean() > 127:  # black strokes on white canvas -> invert to white on black
        inverted = ImageOps.invert(gray)
        control_image = inverted.convert("RGB")
    else:  # already white strokes on dark canvas
        control_image = gray.convert("RGB")

    # 2. Load Diffusers Pipeline
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

    # 4GB VRAM & System RAM Optimizations:
    # enable_sequential_cpu_offload offloads each submodule (UNet, ControlNet, VAE) sequentially,
    # ensuring total VRAM allocation stays well under the 4GB boundary without allocation failures.
    pipe.enable_sequential_cpu_offload()
    pipe.enable_attention_slicing(1)
    if hasattr(pipe.vae, "enable_slicing"):
        pipe.vae.enable_slicing()
    if hasattr(pipe.vae, "enable_tiling"):
        pipe.vae.enable_tiling()
    t_load = time.time() - t_load_start

    # 3. Generate Image with torch.inference_mode()
    if torch.cuda.is_available():
        torch.cuda.reset_peak_memory_stats()

    generator = None
    if args.seed is not None and args.seed >= 0:
        generator = torch.Generator(device="cpu").manual_seed(args.seed)

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
            height=target_size,
            width=target_size,
        )
    t_gen = time.time() - t_gen_start

    # 4. Save Output
    generated_image = result.images[0]
    generated_image.save(output_path, format="PNG")

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
        "load_time_sec": round(t_load, 2),
        "gen_time_sec": round(t_gen, 2),
        "vram_peak_allocated_mb": round(vram_peak_mb, 1),
        "vram_peak_reserved_mb": round(vram_res_mb, 1),
        "ram_peak_gb": round(ram_peak_gb, 2)
    }

def main():
    parser = argparse.ArgumentParser(description="SketchSpace Local ControlNet Worker")
    parser.add_argument("--sketch-path", required=True, help="Path to input sketch PNG")
    parser.add_argument("--output-path", required=True, help="Path to write output PNG")
    parser.add_argument("--prompt", required=True, help="Text generation prompt")
    parser.add_argument("--negative-prompt", default="", help="Negative text prompt")
    parser.add_argument("--steps", type=int, default=15, help="Number of inference steps")
    parser.add_argument("--guidance-scale", type=float, default=7.0, help="Guidance scale")
    parser.add_argument("--conditioning-scale", type=float, default=1.0, help="ControlNet conditioning scale")
    parser.add_argument("--seed", type=int, default=42, help="Random seed (-1 for random)")

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
