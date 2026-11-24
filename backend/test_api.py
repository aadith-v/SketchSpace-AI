"""Unit and Integration Tests for SketchSpace AI FastAPI Backend."""

import io
import sys
from pathlib import Path
from PIL import Image

PROJECT_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(PROJECT_ROOT))

from fastapi.testclient import TestClient
from backend.main import app

client = TestClient(app)


def test_api_endpoints():
    print("=" * 60)
    print("TESTING FASTAPI BACKEND ENDPOINTS")
    print("=" * 60)

    # 1. Health check
    res = client.get("/api/health")
    assert res.status_code == 200, f"Health check failed: {res.text}"
    print("[PASS] GET /api/health ->", res.json())

    # 2. Model status
    res = client.get("/api/status")
    assert res.status_code == 200, f"Status check failed: {res.text}"
    print("[PASS] GET /api/status ->", res.json())
    assert res.json()["model_loaded"] is True, "Model should be loaded!"

    # 3. Example sketches
    res = client.get("/api/examples")
    assert res.status_code == 200, f"Examples check failed: {res.text}"
    examples = res.json()["examples"]
    print(f"[PASS] GET /api/examples -> Found {len(examples)} example sketches")
    assert len(examples) > 0, "Should have at least 1 example sketch"

    # 4. Generate with sample sketch
    test_sketch_img = Image.new("RGB", (256, 256), color=(255, 255, 255))
    buf = io.BytesIO()
    test_sketch_img.save(buf, format="PNG")
    buf.seek(0)

    res = client.post(
        "/api/generate",
        files={"file": ("test_sketch.png", buf, "image/png")}
    )
    assert res.status_code == 200, f"Generate failed: {res.text}"
    gen_data = res.json()
    print("[PASS] POST /api/generate ->", gen_data)
    assert "generated_filename" in gen_data

    # 5. Retrieve generated image
    res = client.get(f"/api/image/{gen_data['generated_filename']}")
    assert res.status_code == 200, f"Image retrieval failed: {res.status_code}"
    print(f"[PASS] GET /api/image/{gen_data['generated_filename']} -> Received {len(res.content)} bytes")

    print("\nALL BACKEND API TESTS PASSED SUCCESSFULLY!")


if __name__ == "__main__":
    test_api_endpoints()

