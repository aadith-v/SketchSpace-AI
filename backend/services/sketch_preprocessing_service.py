"""Sketch Preprocessing Service for SketchSpace AI.
Transforms hand-drawn paper sketches, digital sketches, and photographs
into clean, high-contrast white-on-black scribble representations expected
by ControlNet Scribble v1.1 (0 = pitch black background, 255 = white linework).

Handles:
- Uneven room lighting, paper shadows, camera vignette.
- Blue marker, black ink, and graphite pencil strokes.
- Canvas drawings with pure white backgrounds.
- Screenshots or photos with outer borders/desks (auto-crop to drawing bounds).
- Pre-inverted or dark-mode drawings.
- Aspect ratio letterboxing to 512x512 with black padding.
- SHA-256 hash calculation for lineage and integrity verification.
"""

import hashlib
import io
import logging
from typing import Tuple, Dict, Any, Optional

import cv2
import numpy as np
from PIL import Image

logger = logging.getLogger("SketchPreprocessingService")


def compute_sha256(data: bytes) -> str:
    """Compute SHA-256 hex digest for byte array."""
    h = hashlib.sha256()
    h.update(data)
    return h.hexdigest()


def compute_image_sha256(pil_image: Image.Image) -> str:
    """Compute SHA-256 hex digest of a PIL Image saved as PNG."""
    buf = io.BytesIO()
    pil_image.save(buf, format="PNG")
    return compute_sha256(buf.getvalue())


class SketchPreprocessor:
    """Robust architectural sketch normalization for ControlNet Scribble."""

    @staticmethod
    def auto_crop_canvas(bgr_img: np.ndarray) -> np.ndarray:
        """Detect and crop if image contains a framed canvas or paper surrounded by dark borders.
        
        If a user takes a screenshot of the app or photographed paper on a dark desk,
        this extracts the central active paper region.
        """
        h, w = bgr_img.shape[:2]
        gray = cv2.cvtColor(bgr_img, cv2.COLOR_BGR2GRAY)

        # Threshold to locate bright paper / canvas region
        _, thresh = cv2.threshold(gray, 60, 255, cv2.THRESH_BINARY)
        contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        best_box = None
        max_area = 0
        min_canvas_area = w * h * 0.15  # At least 15% of total image

        for cnt in contours:
            area = cv2.contourArea(cnt)
            if area > min_canvas_area and area > max_area:
                bx, by, bw, bh = cv2.boundingRect(cnt)
                # Aspect ratio check: architectural sketches are generally not razor thin slivers
                aspect = bw / float(bh)
                if 0.35 <= aspect <= 2.8:
                    max_area = area
                    best_box = (bx, by, bw, bh)

        # Only crop if there is a clearly bounded inner region taking less than 85% of total image
        if best_box and (max_area < w * h * 0.88):
            bx, by, bw, bh = best_box
            # Slightly inset (2px) to remove the border stroke itself if framing
            bx = min(w - 1, max(0, bx + 2))
            by = min(h - 1, max(0, by + 2))
            bw = max(10, bw - 4)
            bh = max(10, bh - 4)
            logger.info(f"Auto-cropped outer border: box=({bx}, {by}, {bw}, {bh})")
            return bgr_img[by:by + bh, bx:bx + bw]

        return bgr_img

    @classmethod
    def extract_strokes(cls, bgr_img: np.ndarray) -> np.ndarray:
        """Extract line art as binary white strokes (255) on pitch black background (0)."""
        gray = cv2.cvtColor(bgr_img, cv2.COLOR_BGR2GRAY)
        h, w = gray.shape

        # Check if image is already a white-on-black sketch
        mean_val = gray.mean()
        if mean_val < 35:
            # Already predominantly dark with bright lines
            _, binary = cv2.threshold(gray, 40, 255, cv2.THRESH_BINARY)
            kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (2, 2))
            cleaned = cv2.morphologyEx(binary, cv2.MORPH_OPEN, kernel)
            return cv2.dilate(cleaned, kernel, iterations=1)

        # Check if image is a pure digital canvas (e.g. HTML5 white canvas with black strokes)
        white_pixel_ratio = (gray > 240).mean()
        if white_pixel_ratio > 0.80:
            # Digital canvas: simple crisp threshold + inversion
            _, binary = cv2.threshold(gray, 220, 255, cv2.THRESH_BINARY_INV)
            kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (2, 2))
            dilated = cv2.dilate(binary, kernel, iterations=1)
            return dilated

        # Photographed paper sketch: Handle lighting gradients, shadows, and marker color
        # 1. Bilateral filter / Gaussian blur to suppress paper grain while keeping stroke edges
        blurred = cv2.GaussianBlur(gray, (5, 5), 0)

        # 2. Adaptive Gaussian thresholding: detects strokes locally regardless of lighting
        # Block size 31, C=12 provides crisp extraction without background paper noise
        adaptive = cv2.adaptiveThreshold(
            blurred, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 31, 12
        )

        # 3. Specific blue/colored marker enhancement
        # Blue markers often have strong contrast in (B - R) or LAB space
        b, _, r = cv2.split(bgr_img.astype(np.int16))
        color_diff = np.clip(b - r, 0, 255).astype(np.uint8)
        _, color_contrast = cv2.threshold(color_diff, 45, 255, cv2.THRESH_BINARY)

        # Merge adaptive threshold with high-confidence color strokes
        combined = cv2.bitwise_or(adaptive, color_contrast)

        # 4. Morphological noise cleanup (remove stray 1-2px noise specks)
        kernel_open = cv2.getStructuringElement(cv2.MORPH_RECT, (2, 2))
        cleaned = cv2.morphologyEx(combined, cv2.MORPH_OPEN, kernel_open)

        # 5. Border cleanup: zero out extreme 3px border to remove camera edge artifacts
        cleaned[0:3, :] = 0
        cleaned[-3:, :] = 0
        cleaned[:, 0:3] = 0
        cleaned[:, -3:] = 0

        # 6. Gentle dilation so strokes are ~2-3px solid white lines for ControlNet's downsampling
        kernel_dilate = cv2.getStructuringElement(cv2.MORPH_RECT, (2, 2))
        final_strokes = cv2.dilate(cleaned, kernel_dilate, iterations=1)

        # Safety check: if strokes cover more than 40% of image, it's over-activated
        stroke_ratio = (final_strokes > 0).mean()
        if stroke_ratio > 0.40:
            logger.warning(f"High stroke activation ({stroke_ratio:.2f}), applying higher threshold")
            _, fallback = cv2.threshold(gray, int(gray.mean() - 30), 255, cv2.THRESH_BINARY_INV)
            final_strokes = cv2.morphologyEx(fallback, cv2.MORPH_OPEN, kernel_open)

        return final_strokes

    @classmethod
    def letterbox_pad(cls, stroke_img: np.ndarray, target_size: int = 512) -> np.ndarray:
        """Pad image to target_size x target_size with black background (0), preserving aspect ratio."""
        h, w = stroke_img.shape[:2]
        if w == target_size and h == target_size:
            return stroke_img

        ratio = min(target_size / w, target_size / h)
        new_w = max(1, int(w * ratio))
        new_h = max(1, int(h * ratio))

        resized = cv2.resize(stroke_img, (new_w, new_h), interpolation=cv2.INTER_NEAREST)

        # Black background for ControlNet Scribble
        padded = np.zeros((target_size, target_size), dtype=np.uint8)
        pad_x = (target_size - new_w) // 2
        pad_y = (target_size - new_h) // 2

        padded[pad_y:pad_y + new_h, pad_x:pad_x + new_w] = resized
        return padded

    @classmethod
    def process_sketch(
        cls,
        image_input: Image.Image | np.ndarray,
        target_size: int = 512
    ) -> Tuple[Image.Image, Dict[str, Any]]:
        """Main entry point: processes input sketch to 512x512 ControlNet scribble image.
        
        Returns:
            (pil_control_image, metadata)
        """
        # Convert PIL to BGR numpy array
        if isinstance(image_input, Image.Image):
            rgb = np.array(image_input.convert("RGB"))
            bgr = cv2.cvtColor(rgb, cv2.COLOR_RGB2BGR)
        else:
            bgr = image_input

        orig_h, orig_w = bgr.shape[:2]

        # 1. Auto-crop canvas if bounded by outer frame/desk
        cropped = cls.auto_crop_canvas(bgr)

        # 2. Extract clean binary strokes (white lines on black background)
        strokes = cls.extract_strokes(cropped)

        # 3. Letterbox pad to target 512x512
        final_scribble = cls.letterbox_pad(strokes, target_size=target_size)

        # Convert back to 3-channel RGB PIL Image
        scribble_rgb = cv2.cvtColor(final_scribble, cv2.COLOR_GRAY2RGB)
        pil_scribble = Image.fromarray(scribble_rgb)

        stroke_pixels = int((final_scribble > 0).sum())
        stroke_density = float(stroke_pixels / (target_size * target_size))

        metadata = {
            "original_width": orig_w,
            "original_height": orig_h,
            "target_resolution": f"{target_size}x{target_size}",
            "stroke_pixels": stroke_pixels,
            "stroke_density": round(stroke_density, 4),
            "background_convention": "ControlNet Scribble v1.1 (0=Black, 255=White)",
        }

        return pil_scribble, metadata
