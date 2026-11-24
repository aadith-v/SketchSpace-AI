"""SketchSpace AI - FastAPI Application Entry Point.
Launches the REST API server with CORS support and mounts endpoints.
"""

import sys
from pathlib import Path
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles

PROJECT_ROOT = Path(__file__).resolve().parent.parent
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from configs.config import API_HOST, API_PORT, OUTPUTS_DIR
from backend.api.routes import router
from fastapi.responses import FileResponse

STATIC_DIR = Path(__file__).resolve().parent / "static"
STATIC_DIR.mkdir(parents=True, exist_ok=True)

app = FastAPI(
    title="SketchSpace AI API",
    description="Sketch-to-Realistic Interior Generation powered by Pix2Pix Conditional GAN",
    version="1.0.0"
)

# Enable CORS for frontend clients (dev ports 3000, 5173, etc.)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Root endpoint serves interactive demonstration web UI
@app.get("/")
def serve_frontend():
    index_file = STATIC_DIR / "index.html"
    if index_file.exists():
        return FileResponse(index_file)
    return {"message": "SketchSpace AI API running. Visit /docs for Swagger UI."}

# Include API Router
app.include_router(router, prefix="/api")

# Mount static directories
app.mount("/static/web", StaticFiles(directory=str(STATIC_DIR)), name="web_static")
app.mount("/static/outputs", StaticFiles(directory=str(OUTPUTS_DIR)), name="outputs")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("backend.main:app", host=API_HOST, port=API_PORT, reload=False)

