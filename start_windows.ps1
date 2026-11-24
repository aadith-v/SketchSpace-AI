# SketchSpace AI - Windows PowerShell Startup Script
Write-Host "===============================================================================" -ForegroundColor Cyan
Write-Host "           SketchSpace AI - Interactive Interior Generation" -ForegroundColor Cyan
Write-Host "===============================================================================" -ForegroundColor Cyan
Write-Host ""

# Verify Python Environment
if (Test-Path ".\venv_diffusion\Scripts\python.exe") {
    $pyExe = ".\venv_diffusion\Scripts\python.exe"
    Write-Host "Using dedicated venv_diffusion environment: $pyExe" -ForegroundColor Green
} else {
    $pyExe = "python"
    Write-Host "Using system Python: $pyExe" -ForegroundColor Yellow
}

# Verify Dependencies
Write-Host "Checking runtime packages..." -ForegroundColor Yellow
& $pyExe -c "import torch, fastapi, uvicorn, PIL, numpy; print('Core dependencies OK!')"
if ($LASTEXITCODE -ne 0) {
    Write-Host "[WARNING] Missing packages! Installing requirements from requirements.txt..." -ForegroundColor Yellow
    pip install -r requirements.txt
}

Write-Host "`nStarting server at http://127.0.0.1:8000 ..." -ForegroundColor Green
Start-Process "http://127.0.0.1:8000"
& $pyExe -m uvicorn backend.main:app --host 127.0.0.1 --port 8000
