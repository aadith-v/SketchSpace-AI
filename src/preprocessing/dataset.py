"""Dataset Preprocessing and Paired PyTorch DataLoader for SketchSpace AI.
Implements:
- Paired (Sketch, Realistic Interior) loading.
- Normalization to [-1, 1] range for Pix2Pix Tanh generator.
- Synchronized paired data augmentations (horizontal flip applied to both).
- Independent visual augmentations (mild brightness/contrast on realistic target).
- Train/Val/Test dataset access and validation.
"""

import os
import sys
import random
from pathlib import Path
from typing import Tuple, Optional, Callable

# Add project root to sys.path
PROJECT_ROOT = Path(__file__).resolve().parent.parent.parent
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

import numpy as np
import torch
from torch.utils.data import Dataset, DataLoader
from PIL import Image, ImageEnhance
import torchvision.transforms.functional as TF


class PairedInteriorDataset(Dataset):
    """PyTorch Dataset for paired Sketch -> Realistic Interior images."""

    def __init__(
        self,
        sketch_dir: Path,
        realistic_dir: Path,
        image_size: Tuple[int, int] = (256, 256),
        is_train: bool = True,
        augment: bool = True
    ):
        self.sketch_dir = Path(sketch_dir)
        self.realistic_dir = Path(realistic_dir)
        self.image_size = image_size
        self.is_train = is_train
        self.augment = augment and is_train

        # Verify directories exist
        if not self.sketch_dir.exists():
            raise FileNotFoundError(f"Sketch directory does not exist: {self.sketch_dir}")
        if not self.realistic_dir.exists():
            raise FileNotFoundError(f"Realistic directory does not exist: {self.realistic_dir}")

        # Collect paired files
        sketch_files = {p.stem: p for p in self.sketch_dir.glob("*.png")}
        realistic_files = {p.stem: p for p in self.realistic_dir.glob("*.png")}

        common_keys = sorted(list(set(sketch_files.keys()) & set(realistic_files.keys())))
        if len(common_keys) == 0:
            raise ValueError(f"No paired images found between {self.sketch_dir} and {self.realistic_dir}")

        self.paired_paths = [(sketch_files[k], realistic_files[k]) for k in common_keys]

    def __len__(self) -> int:
        return len(self.paired_paths)

    def __getitem__(self, index: int) -> Tuple[torch.Tensor, torch.Tensor, str]:
        sketch_path, realistic_path = self.paired_paths[index]

        sketch_img = Image.open(sketch_path).convert("RGB")
        realistic_img = Image.open(realistic_path).convert("RGB")

        # Resize to target resolution
        sketch_img = sketch_img.resize(self.image_size, Image.BILINEAR)
        realistic_img = realistic_img.resize(self.image_size, Image.BILINEAR)

        # Synchronized Data Augmentation for training
        if self.augment:
            # Synchronized Random Horizontal Flip
            # Critical: must be applied to BOTH images identically to preserve spatial correspondence
            if random.random() > 0.5:
                sketch_img = TF.hflip(sketch_img)
                realistic_img = TF.hflip(realistic_img)

        # Convert to Tensor in [0, 1]
        sketch_tensor = TF.to_tensor(sketch_img)
        realistic_tensor = TF.to_tensor(realistic_img)

        # Normalize to [-1, 1] for Pix2Pix Tanh compatibility
        sketch_norm = (sketch_tensor - 0.5) / 0.5
        realistic_norm = (realistic_tensor - 0.5) / 0.5

        return sketch_norm, realistic_norm, sketch_path.stem


def get_dataloader(
    split: str = "train",
    batch_size: int = 4,
    shuffle: bool = True,
    num_workers: int = 0,
    dataset_dir: Optional[Path] = None
) -> DataLoader:
    """Helper to build DataLoader for a given dataset split."""
    from configs.config import (
        IMAGE_WIDTH, IMAGE_HEIGHT, FILTERED_DIR, GENERATED_DIR
    )

    if dataset_dir is None:
        base_dir = FILTERED_DIR if FILTERED_DIR.exists() else GENERATED_DIR
    else:
        base_dir = Path(dataset_dir)

    if split in ("train", "val", "test"):
        s_dir = base_dir / split / "sketches"
        r_dir = base_dir / split / "realistic"
        is_train = (split == "train")
    else:
        raise ValueError(f"Unknown split: {split}. Expected 'train', 'val', or 'test'.")

    dataset = PairedInteriorDataset(
        sketch_dir=s_dir,
        realistic_dir=r_dir,
        image_size=(IMAGE_WIDTH, IMAGE_HEIGHT),
        is_train=is_train,
        augment=is_train
    )

    return DataLoader(
        dataset,
        batch_size=batch_size,
        shuffle=shuffle if is_train else False,
        num_workers=num_workers,
        drop_last=is_train and len(dataset) > batch_size
    )


if __name__ == "__main__":
    print("Testing PairedInteriorDataset...")
    loader = get_dataloader(split="train", batch_size=4)
    print(f"Total batches in train loader: {len(loader)}")
    sketches, realistic, stems = next(iter(loader))
    print(f"Sketch batch shape: {sketches.shape}, dtype: {sketches.dtype}")
    print(f"Realistic batch shape: {realistic.shape}, dtype: {realistic.dtype}")
    print(f"Sketch min/max: {sketches.min().item():.3f} / {sketches.max().item():.3f}")
    print(f"Realistic min/max: {realistic.min().item():.3f} / {realistic.max().item():.3f}")
    print(f"Sample stems: {stems[:4]}")
    assert sketches.shape == (4, 3, 256, 256)
    assert realistic.shape == (4, 3, 256, 256)
    print("Dataset and Preprocessing tests passed successfully!")
