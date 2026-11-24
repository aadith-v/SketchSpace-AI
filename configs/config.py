"""SketchSpace AI - Central Configuration Module (Standalone Distribution)."""
from pathlib import Path

# Base Paths (Self-Contained)
PROJECT_ROOT = Path(__file__).resolve().parent.parent
EXAMPLES_DIR = PROJECT_ROOT / "examples"
CHECKPOINTS_DIR = PROJECT_ROOT / "checkpoints"
CHECKPOINTS_EXP1_DIR = CHECKPOINTS_DIR / "experiment_15epochs"
CHECKPOINTS_EXP2_DIR = CHECKPOINTS_DIR / "experiment_2"
CHECKPOINTS_EXP3_DIR = CHECKPOINTS_DIR / "experiment_3"
CHECKPOINTS_EXP4_DIR = CHECKPOINTS_DIR / "phase2_pilot" / "experiment_4"
CHECKPOINTS_EXP5_DIR = CHECKPOINTS_DIR / "phase2_experiment_5"
OUTPUTS_DIR = PROJECT_ROOT / "outputs"

# Dataset & Examples Fallback
FILTERED_EXP2_TEST_SKETCHES_DIR = EXAMPLES_DIR
FILTERED_TEST_SKETCHES_DIR = EXAMPLES_DIR
TEST_SKETCHES_DIR = EXAMPLES_DIR
TRAIN_SKETCHES_DIR = EXAMPLES_DIR

# Server Settings
API_HOST = "127.0.0.1"
API_PORT = 8000
LATEST_CHECKPOINT_NAME = "experiment_3/generator_best.pth"
