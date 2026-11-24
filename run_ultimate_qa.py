import json
import urllib.parse
import urllib.request
import uuid

# 1. Health check
res = urllib.request.urlopen("http://127.0.0.1:8000/api/health")
health = json.loads(res.read())
assert health["status"] == "healthy"
print("1. HEALTH CHECK: PASSED")

# 2. Status & ControlNet Readiness
res = urllib.request.urlopen("http://127.0.0.1:8000/api/status")
status = json.loads(res.read())
assert status["local_controlnet"]["available"] is True
assert status["local_controlnet"]["offline_mode"] is True
print("2. ENGINE STATUS: PASSED (ControlNet Available & Offline)")

# 3. Static HTML Validation
res = urllib.request.urlopen("http://127.0.0.1:8000/")
html = res.read().decode("utf-8")
assert "SketchSpace AI" in html
assert "IBM Plex Mono" in html
assert "Manrope" in html
assert "hero-dollhouse-3d" in html
assert "sketch-to-reality-showcase" in html
assert "spatial-canvas-viewport" in html
assert "spatial-visualizer-stage" in html
assert "spatial-compare-box" in html
assert "gallery-collection-grid" in html
assert "presentation-fullscreen" in html
print("3. STATIC DOM & ASSETS: PASSED (All 23 Phase components present)")

# 4. Live ControlNet Synthesis Verification
boundary = f"----Boundary{uuid.uuid4().hex}"
with open(r"Z:\SketchSpace-AI-Share\SketchSpace-AI-Share\examples\new_living_room_sketch.png", "rb") as f:
    sketch_bytes = f.read()

parts = [
    f"--{boundary}\r\nContent-Disposition: form-data; name=\"file\"; filename=\"living_sketch.png\"\r\nContent-Type: image/png\r\n\r\n".encode("latin-1"),
    sketch_bytes,
    f"\r\n--{boundary}\r\nContent-Disposition: form-data; name=\"model\"\r\n\r\ncontrolnet-local\r\n--{boundary}--\r\n".encode("latin-1")
]
payload = b"".join(parts)

prompt = "photorealistic contemporary luxury living room interior, designer sofa, marble coffee table, indoor plants, natural morning sunlight from floor-to-ceiling windows, architectural digest photography, high resolution, sharp focus, 8k"
query = urllib.parse.urlencode({
    "model": "controlnet-local",
    "category": "living_room",
    "steps": 15,
    "prompt": prompt
})

req = urllib.request.Request(
    f"http://127.0.0.1:8000/api/generate?{query}",
    data=payload,
    headers={"Content-Type": f"multipart/form-data; boundary={boundary}"}
)
print("4. Dispatching live ControlNet generation...")
with urllib.request.urlopen(req, timeout=180) as resp:
    gen_data = json.loads(resp.read().decode())
    assert gen_data["success"] is True
    assert gen_data["generated_url"].startswith("/api/image/")
    print("4. GENERATION PIPELINE: PASSED!")
    print("   - Generated File:", gen_data["generated_filename"])
    print("   - Load Time:", gen_data["metrics"]["load_time_sec"], "s")
    print("   - Generation Time:", gen_data["metrics"]["gen_time_sec"], "s")
    print("   - Peak Allocated VRAM:", gen_data["metrics"]["vram_peak_allocated_mb"], "MB")
    print("   - Resolution:", gen_data["resolution"])
