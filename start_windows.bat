@echo off
title SketchSpace AI - Offline Generator
echo ===============================================================================
echo            SketchSpace AI - Interactive Interior Generation
echo ===============================================================================
echo.
echo Starting FastAPI Web Server at http://127.0.0.1:8000 ...
echo Press CTRL+C to stop the server anytime.
echo.

if exist "venv_diffusion\Scripts\python.exe" (
    echo Using dedicated venv_diffusion environment...
    venv_diffusion\Scripts\python.exe -m uvicorn backend.main:app --host 127.0.0.1 --port 8000
) else (
    python -m uvicorn backend.main:app --host 127.0.0.1 --port 8000
)
pause
