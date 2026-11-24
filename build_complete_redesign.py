# Master Builder for SketchSpace AI Complete Redesign
import os
import shutil
from pathlib import Path

BACKUP_PATH = Path("backend/static/index.html.backup_before_complete_redesign")
TARGET_PATH = Path("backend/static/index.html")

if TARGET_PATH.exists() and not BACKUP_PATH.exists():
    shutil.copy2(TARGET_PATH, BACKUP_PATH)
    print("Backed up existing index.html to", BACKUP_PATH)

print("Starting Complete Redesign generation...")
