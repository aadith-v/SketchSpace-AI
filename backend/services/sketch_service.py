"""Sketch Service for SketchSpace AI Backend.
Handles sketch file validation, uploads, and example sketch catalog.
"""

import io
import shutil
import uuid
from pathlib import Path
from typing import List, Dict, Any, Tuple
from PIL import Image

PROJECT_ROOT = Path(__file__).resolve().parent.parent.parent
from configs.config import (
    OUTPUTS_DIR,
    FILTERED_EXP2_TEST_SKETCHES_DIR,
    FILTERED_TEST_SKETCHES_DIR,
    TEST_SKETCHES_DIR,
    TRAIN_SKETCHES_DIR
)

UPLOAD_DIR = OUTPUTS_DIR / "web_uploads"
UPLOAD_DIR.mkdir(parents=True, exist_ok=True)


class SketchService:
    """Manages sketch uploads and example queries."""

    ALLOWED_EXTENSIONS = {".png", ".jpg", ".jpeg"}
    MAX_FILE_SIZE = 10 * 1024 * 1024  # 10 MB

    @classmethod
    def validate_and_save_upload(cls, file_bytes: bytes, filename: str) -> Tuple[Path, Image.Image]:
        """Validate format, dimensions, corruption and save to upload directory."""
        ext = Path(filename).suffix.lower()
        if ext not in cls.ALLOWED_EXTENSIONS:
            raise ValueError(f"Unsupported file format '{ext}'. Allowed: PNG, JPG, JPEG")

        if len(file_bytes) > cls.MAX_FILE_SIZE:
            raise ValueError(f"File size exceeds 10MB limit ({len(file_bytes)} bytes).")

        try:
            image = Image.open(io.BytesIO(file_bytes))
            image.verify()  # Verify integrity
            # Reopen after verify
            image = Image.open(io.BytesIO(file_bytes))
        except Exception as e:
            raise ValueError(f"Corrupted or invalid image file: {e}")

        # Check resolution
        w, h = image.size
        if w < 64 or h < 64:
            raise ValueError(f"Image too small ({w}x{h}). Minimum required resolution is 64x64.")

        unique_name = f"sketch_{uuid.uuid4().hex[:10]}{ext}"
        saved_path = UPLOAD_DIR / unique_name
        image.save(saved_path)

        return saved_path, image

    PRIORITY_EXAMPLES = [
        "scene_00024.png",
        "scene_00023.png",
        "scene_00004.png",
        "scene_00010.png",
        "scene_00002.png",
        "scene_00031.png"
    ]

    @classmethod
    def get_example_sketches(cls) -> List[Dict[str, Any]]:
        """Retrieve pre-rendered example sketches from test/train datasets with prioritized furniture-rich scenes."""
        examples = []
        source_dirs = [
            PROJECT_ROOT / "examples"
        ]

        seen_names = set()

        # 1. First add verified priority examples in requested order
        for target_name in cls.PRIORITY_EXAMPLES:
            for s_dir in source_dirs:
                if s_dir.exists():
                    p = s_dir / target_name
                    if p.exists() and target_name not in seen_names:
                        examples.append({
                            "id": p.stem,
                            "filename": p.name,
                            "path": str(p),
                            "url": f"/api/sketches/example/{p.name}"
                        })
                        seen_names.add(target_name)
                        break

        # 2. If fewer than 6, fallback to additional available scenes
        if len(examples) < 6:
            for s_dir in source_dirs:
                if s_dir.exists():
                    for p in sorted(list(s_dir.glob("*.png"))):
                        if p.name not in seen_names:
                            examples.append({
                                "id": p.stem,
                                "filename": p.name,
                                "path": str(p),
                                "url": f"/api/sketches/example/{p.name}"
                            })
                            seen_names.add(p.name)
                        if len(examples) >= 6:
                            break
                if len(examples) >= 6:
                    break

        return examples

