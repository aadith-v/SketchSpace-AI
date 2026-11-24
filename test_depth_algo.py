import cv2
import numpy as np
from PIL import Image
from pathlib import Path

def compute_architectural_depth(image_path: Path) -> Image.Image:
    img = Image.open(image_path).convert('RGB')
    w, h = img.size
    img_np = np.array(img)
    gray = cv2.cvtColor(img_np, cv2.COLOR_RGB2GRAY)
    
    # 1. Perspective Vanishing Gradient (Standard architectural single-point perspective)
    # Floor: y from h down to horizon (~0.5*h) -> close (near=255) to far (horizon=60)
    # Back wall: central region -> far (depth 40-70)
    # Ceiling: y from 0 to horizon -> mid-depth (70-120)
    y_coords, x_coords = np.mgrid[0:h, 0:w]
    
    # Center horizon typically at y = 0.52 * h, x = 0.5 * w
    cy = 0.52 * h
    cx = 0.50 * w
    
    # Normalized coordinates
    ny = (y_coords - cy) / (h * 0.5)  # -1 at top, +1 at bottom
    nx = (x_coords - cx) / (w * 0.5)  # -1 at left, +1 at right
    
    # Radial distance from center vanishing line
    r = np.sqrt(nx**2 + (ny * 0.8)**2)
    
    # Base perspective depth: distance from vanishing center
    # Center back wall is furthest (low values ~ 30), floor foreground is nearest (high values ~ 240)
    # Left and right edges are closer than center
    perspective_depth = 50.0 + 130.0 * np.clip(ny, 0, 1.0)**1.2 + 60.0 * (nx**2 * 0.6)
    # Ceiling slope
    ceiling_mask = ny < 0
    perspective_depth[ceiling_mask] = 50.0 + 60.0 * np.abs(ny[ceiling_mask])**1.1 + 40.0 * (nx[ceiling_mask]**2 * 0.5)
    
    # 2. Local photometric & edge cues
    # Blur & bilateral filter to preserve furniture silhouettes
    filtered_gray = cv2.bilateralFilter(gray, d=9, sigmaColor=75, sigmaSpace=75)
    # Contrast normalization
    local_detail = (filtered_gray.astype(np.float32) - np.mean(filtered_gray)) / (np.std(filtered_gray) + 1e-5)
    
    # 3. Furniture prominence: Objects with high local contrast in bottom half pop forward
    furniture_boost = np.zeros_like(perspective_depth)
    furniture_boost[ny > -0.2] = local_detail[ny > -0.2] * 20.0
    
    combined_depth = perspective_depth + furniture_boost
    # Smooth with slight Gaussian to ensure no vertex ripping in Three.js
    combined_depth = cv2.GaussianBlur(combined_depth, (5, 5), 0)
    
    # Normalize to 0..255
    depth_norm = cv2.normalize(combined_depth, None, 0, 255, cv2.NORM_MINMAX)
    depth_uint8 = depth_norm.astype(np.uint8)
    
    return Image.fromarray(depth_uint8, mode='L')

sample = Path("outputs/web_generated/gen_36d642bb82.png")
if sample.exists():
    depth_img = compute_architectural_depth(sample)
    out_path = Path("outputs/web_generated/test_sample_depth.png")
    depth_img.save(out_path)
    print(f"Generated depth map saved to {out_path} ({depth_img.size})")
