import json
import urllib.request
import uuid
from pathlib import Path

# 1. Health check
req = urllib.request.Request("http://127.0.0.1:8000/api/health")
with urllib.request.urlopen(req) as resp:
    health = json.loads(resp.read().decode())
    print("HEALTH:", health)

# 2. System Status (includes local_controlnet)
req2 = urllib.request.Request("http://127.0.0.1:8000/api/status")
with urllib.request.urlopen(req2) as resp2:
    status = json.loads(resp2.read().decode())
    print("STATUS local_controlnet:", status.get("local_controlnet"))

# 3. Test ControlNet generation via API
sketch_path = Path(r"Z:\SketchSpace-AI-Share\SketchSpace-AI-Share\examples\new_bedroom_sketch.png")
with open(sketch_path, "rb") as f:
    img_data = f.read()

boundary = f"----Boundary{uuid.uuid4().hex}"
parts = []
parts.append(f"--{boundary}\r\nContent-Disposition: form-data; name=\"file\"; filename=\"sketch.png\"\r\nContent-Type: image/png\r\n\r\n".encode("latin-1"))
parts.append(img_data)
parts.append(f"\r\n--{boundary}\r\nContent-Disposition: form-data; name=\"model\"\r\n\r\ncontrolnet-local\r\n--{boundary}--\r\n".encode("latin-1"))

payload = b"".join(parts)

req3 = urllib.request.Request(
    "http://127.0.0.1:8000/api/generate?model=controlnet-local&category=bedroom&steps=15",
    data=payload,
    headers={"Content-Type": f"multipart/form-data; boundary={boundary}"}
)

print("Sending generation request to http://127.0.0.1:8000/api/generate ...")
with urllib.request.urlopen(req3, timeout=180) as resp3:
    gen_res = json.loads(resp3.read().decode())
    print("API GENERATION RESULT:", json.dumps(gen_res, indent=2))
