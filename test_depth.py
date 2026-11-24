import sys
from pathlib import Path
from PIL import Image
import numpy as np

# Test depth generation for existing generated image
output_dir = Path("outputs/web_generated")
images = list(output_dir.glob("*.png"))
print(f"Found {len(images)} generated images in {output_dir}")
if images:
    sample = images[0]
    print(f"Testing on sample: {sample.name}")
    img = Image.open(sample).convert("RGB")
    w, h = img.size
    print(f"Image size: {w}x{h}")
