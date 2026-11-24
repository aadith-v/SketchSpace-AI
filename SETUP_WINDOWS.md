# SketchSpace AI — Windows Installation & Setup Guide

This guide details how to install, configure, and execute SketchSpace AI on Windows 10/11 with an **Intel i7 processor and an NVIDIA GeForce RTX 3050 Laptop GPU (4 GB VRAM)**.

---

## 1. Hardware & System Requirements

| Component | Minimum Specification | Recommended (Tested Environment) |
| :--- | :--- | :--- |
| **Operating System** | Windows 10/11 64-bit | Windows 11 64-bit |
| **Processor** | Intel Core i5 / AMD Ryzen 5 | Intel Core i7-13620H |
| **System RAM** | 8 GB | 16 GB |
| **GPU** | NVIDIA GTX 1650 (4 GB) or CPU | NVIDIA GeForce RTX 3050 Laptop GPU (4 GB VRAM) |
| **NVIDIA Driver** | Driver version 550.00+ | Driver version 576.52 (CUDA 12.9 compatible) |
| **Free Disk Space** | 10 GB on `Z:` drive | 80 GB free on `Z:` drive |

---

## 2. Directory Layout & Model Weights

Pretrained diffusion models are stored in the local Hugging Face Hub cache on drive `Z:`:

```
Z:\SketchSpace_AI_Models\huggingface\hub\
├── models--stable-diffusion-v1-5--stable-diffusion-v1-5\
│   └── snapshots\451f4fe16113bff5a5d2269ed5ad43b0592e9a14\
└── models--lllyasviel--control_v11p_sd15_scribble\
    └── snapshots\3564ec7b87dd706d5fc760d21c9e90bb160d1e9f\
```

The system environment variable `HF_HOME` is persistently set to:
```powershell
[Environment]::SetEnvironmentVariable("HF_HOME", "Z:\SketchSpace_AI_Models\huggingface", "User")
```

---

## 3. Dedicated Python Environment (`venv_diffusion`)

SketchSpace AI uses an isolated virtual environment located at `.\venv_diffusion` to prevent package conflicts with the system Python installation:

```powershell
# In the project directory:
python -m venv --system-site-packages venv_diffusion

# Activate environment:
.\venv_diffusion\Scripts\Activate.ps1

# Verify packages:
python -c "import torch, diffusers, transformers, accelerate, safetensors, fastapi, uvicorn; print('Environment ready!')"
```

Installed runtime components:
* `torch 2.11.0+cu128` (CUDA acceleration for RTX 3050)
* `torchvision 0.26.0+cu128`
* `diffusers 0.43.0`
* `transformers 5.24.0`
* `accelerate 1.16.0` (Essential for model CPU offloading)
* `safetensors 0.8.0` (Fast zero-copy model loader)
* `fastapi 0.165.0`
* `uvicorn 0.54.0`

---

## 4. Starting the Application

### Option A: Double-Click Launcher (Recommended)
Double-click `start_windows.bat` in File Explorer.

### Option B: PowerShell Launcher
```powershell
.\start_windows.ps1
```

The launcher will verify packages, bind to `http://127.0.0.1:8000`, and automatically open the application in your default web browser.

---

## 5. Verification & Testing

To run the automated verification test suite:

```powershell
.\venv_diffusion\Scripts\python.exe C:\Users\aadit\.gemini\antigravity\brain\83b488cf-1cce-4b53-aaa5-2f8d09a20551\scratch\test_e2e_full.py
```

This validates:
1. Health check endpoint (`GET /api/health`).
2. HTML5 interactive canvas UI serving.
3. Registered model options list.
4. GPU detection and offline status (`GET /api/status`).
5. Invalid image and request rejection (HTTP 422).
6. Synthetic bedroom sketch creation and real offline ControlNet generation on RTX 3050 (HTTP 200).
7. Visual output integrity check (512×512, RGB, non-blank).
8. Independent Pix2Pix generator execution (~75 ms CPU).
9. Concurrency lock and busy protection (HTTP 503).
