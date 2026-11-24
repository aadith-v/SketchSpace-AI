"""Sketch Generator Module.
Generates synthetic sketch representations from realistic rendered interior images
using multiple configurable computer vision methods:
1. Canny edge detection
2. Grayscale edge extraction
3. Contour-based sketch generation
4. Line-based structural sketch generation

Note: Edge maps derived from rendered images are synthetic sketch representations,
not genuine human hand-drawn sketches.
"""

import cv2
import numpy as np
from PIL import Image
from typing import Union, Tuple


class SketchGenerator:
    """Multi-method sketch generator for paired image-to-image dataset synthesis."""

    def __init__(
        self,
        method: str = "canny",
        line_thickness: int = 1,
        bilateral_d: int = 3,
        bilateral_sigma_color: float = 15.0,
        bilateral_sigma_space: float = 15.0,
        canny_thresh1: int = 40,
        canny_thresh2: int = 120
    ):
        self.method = method.lower()
        self.line_thickness = line_thickness
        self.bilateral_d = bilateral_d
        self.bilateral_sigma_color = bilateral_sigma_color
        self.bilateral_sigma_space = bilateral_sigma_space
        self.canny_thresh1 = canny_thresh1
        self.canny_thresh2 = canny_thresh2

    def generate(self, image: Union[np.ndarray, Image.Image], method: str = None) -> np.ndarray:
        """Generate a sketch from an RGB image using the specified or default method.

        Returns an RGB image (H, W, 3) where background is white (255) and sketch lines are dark.
        """
        if method is None:
            method = self.method
        method = method.lower()

        # Convert PIL to numpy if needed
        if isinstance(image, Image.Image):
            img_np = np.array(image.convert("RGB"))
        else:
            img_np = image.copy()
            if img_np.ndim == 2:
                img_np = cv2.cvtColor(img_np, cv2.COLOR_GRAY2RGB)

        if method == "canny":
            return self._canny_sketch(img_np)
        elif method == "grayscale":
            return self._grayscale_edge_sketch(img_np)
        elif method == "contour":
            return self._contour_sketch(img_np)
        elif method == "structural_lines":
            return self._structural_line_sketch(img_np)
        else:
            raise ValueError(f"Unknown sketch generation method: {method}. "
                             f"Supported methods: ['canny', 'grayscale', 'contour', 'structural_lines']")

    def _canny_sketch(self, rgb_img: np.ndarray) -> np.ndarray:
        """Canny edge detection with bilateral filtering for clean structural edges.
        Uses less aggressive filtering (d=3, sigma=15) to preserve fine furniture edges.
        """
        gray = cv2.cvtColor(rgb_img, cv2.COLOR_RGB2GRAY)
        # Moderate bilateral filter preserves subtle furniture boundaries and thin legs
        filtered = cv2.bilateralFilter(
            gray,
            d=self.bilateral_d,
            sigmaColor=self.bilateral_sigma_color,
            sigmaSpace=self.bilateral_sigma_space
        )
        edges = cv2.Canny(filtered, threshold1=self.canny_thresh1, threshold2=self.canny_thresh2)
        
        # Invert edges so background is white (255) and strokes are black (0)
        sketch = cv2.bitwise_not(edges)
        if self.line_thickness > 1:
            kernel = np.ones((self.line_thickness, self.line_thickness), np.uint8)
            sketch = cv2.erode(sketch, kernel)
        return cv2.cvtColor(sketch, cv2.COLOR_GRAY2RGB)

    def _grayscale_edge_sketch(self, rgb_img: np.ndarray) -> np.ndarray:
        """Grayscale edge extraction using Sobel gradients and thresholding."""
        gray = cv2.cvtColor(rgb_img, cv2.COLOR_RGB2GRAY)
        # Gaussian blur to smooth out fine texture noise
        blurred = cv2.GaussianBlur(gray, (3, 3), 0)
        grad_x = cv2.Sobel(blurred, cv2.CV_32F, 1, 0, ksize=3)
        grad_y = cv2.Sobel(blurred, cv2.CV_32F, 0, 1, ksize=3)
        magnitude = cv2.magnitude(grad_x, grad_y)
        
        # Normalize magnitude to 0-255
        norm_mag = cv2.normalize(magnitude, None, 0, 255, cv2.NORM_MINMAX, dtype=cv2.CV_8U)
        # Invert and threshold to create clean pencil-style strokes
        sketch = 255 - norm_mag
        # Apply slight contrast boost
        sketch = np.clip((sketch.astype(np.float32) - 30) * 1.3, 0, 255).astype(np.uint8)
        return cv2.cvtColor(sketch, cv2.COLOR_GRAY2RGB)

    def _contour_sketch(self, rgb_img: np.ndarray) -> np.ndarray:
        """Contour-based sketch extraction using morphological gradients and adaptive thresholding."""
        gray = cv2.cvtColor(rgb_img, cv2.COLOR_RGB2GRAY)
        kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))
        # Morphological gradient highlights structural boundaries
        gradient = cv2.morphologyEx(gray, cv2.MORPH_GRADIENT, kernel)
        # Adaptive thresholding to extract distinct room contours
        adaptive = cv2.adaptiveThreshold(
            gradient, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2
        )
        sketch = cv2.bitwise_not(adaptive)
        return cv2.cvtColor(sketch, cv2.COLOR_GRAY2RGB)

    def _structural_line_sketch(self, rgb_img: np.ndarray) -> np.ndarray:
        """Line-based structural sketch using Probabilistic Hough Line Transform."""
        gray = cv2.cvtColor(rgb_img, cv2.COLOR_RGB2GRAY)
        edges = cv2.Canny(gray, 50, 150, apertureSize=3)
        
        # Create blank white canvas
        h, w = gray.shape
        sketch = np.ones((h, w), dtype=np.uint8) * 255

        # Detect structural lines (walls, furniture borders)
        lines = cv2.HoughLinesP(edges, rho=1, theta=np.pi / 180, threshold=40,
                                minLineLength=20, maxLineGap=10)
        if lines is not None:
            for line in lines:
                l = np.asarray(line).ravel()
                if len(l) >= 4:
                    x1, y1, x2, y2 = int(l[0]), int(l[1]), int(l[2]), int(l[3])
                    cv2.line(sketch, (x1, y1), (x2, y2), (0, 0, 0), thickness=self.line_thickness, lineType=cv2.LINE_AA)
        
        # Combine with light Canny edge outline to preserve non-linear details (e.g. lamps, plants)
        soft_edges = cv2.bitwise_not(edges)
        combined = cv2.min(sketch, soft_edges)
        return cv2.cvtColor(combined, cv2.COLOR_GRAY2RGB)
