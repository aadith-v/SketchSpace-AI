"""Direct Verification of all FastAPI endpoints and router functions."""

import asyncio
import io
import sys
from pathlib import Path
from PIL import Image
from fastapi import UploadFile

PROJECT_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(PROJECT_ROOT))

from backend.api import routes


async def test_all_routes():
    print("=" * 60)
    print("FASTAPI ROUTE FUNCTIONS VERIFICATION")
    print("=" * 60)

    # 1. Health check
    h = routes.health_check()
    print("  1. GET /api/health ->", h)
    assert h["status"] == "healthy"

    # 2. Model status
    s = routes.model_status()
    print("  2. GET /api/status ->", s)
    assert s["model_loaded"] is True

    # 3. Examples
    ex = routes.list_examples()
    print(f"  3. GET /api/examples -> {len(ex['examples'])} examples returned")
    assert len(ex["examples"]) > 0

    # 4. Get specific example sketch
    first_ex_name = ex["examples"][0]["filename"]
    res_ex = routes.get_example_sketch(first_ex_name)
    print(f"  4. GET /api/sketches/example/{first_ex_name} -> FileResponse path={res_ex.path}")
    assert Path(res_ex.path).exists()

    # 5. Upload sketch
    test_img = Image.new("RGB", (256, 256), color=(255, 255, 255))
    buf = io.BytesIO()
    test_img.save(buf, format="PNG")
    buf.seek(0)
    upload_file = UploadFile(filename="unit_test_sketch.png", file=buf)

    up_res = await routes.upload_sketch(upload_file)
    print("  5. POST /api/upload ->", up_res)
    assert up_res["success"] is True

    # 6. Generate interior
    buf.seek(0)
    gen_file = UploadFile(filename="unit_test_sketch.png", file=buf)
    gen_res = await routes.generate_interior(gen_file)
    print("  6. POST /api/generate ->", gen_res)
    assert gen_res["success"] is True
    assert "generated_filename" in gen_res

    # 7. Get generated image
    gen_fn = gen_res["generated_filename"]
    res_img = routes.get_generated_image(gen_fn)
    print(f"  7. GET /api/image/{gen_fn} -> FileResponse path={res_img.path}")
    assert Path(res_img.path).exists()

    # 8. Get uploaded image
    up_fn = up_res["filename"]
    res_up = routes.get_uploaded_image(up_fn)
    print(f"  8. GET /api/uploads/{up_fn} -> FileResponse path={res_up.path}")
    assert Path(res_up.path).exists()

    print("\nALL 8 FASTAPI ENDPOINTS VERIFIED & WORKING!")


if __name__ == "__main__":
    asyncio.run(test_all_routes())

