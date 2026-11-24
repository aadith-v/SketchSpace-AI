import json
import urllib.parse
import urllib.request
import uuid

# 1. Test sketch serving
req_sketch = urllib.request.Request("http://127.0.0.1:8000/api/sketches/example/new_bathroom_sketch.png")
with urllib.request.urlopen(req_sketch) as resp:
    data = resp.read()
    print("PRESET SKETCH SERVING: OK (bytes:", len(data), ")")

# 2. Test showcase images
for img_name in ["local_cn_bedroom_1795531503385.png", "local_cn_office_1795531733794.png", "gen_36d642bb82.png", "gen_872659fba5.png"]:
    req_img = urllib.request.Request(f"http://127.0.0.1:8000/api/image/{img_name}")
    with urllib.request.urlopen(req_img) as resp:
        print(f"SHOWCASE {img_name}: OK (HTTP {resp.status})")

# 3. Test generate endpoint with custom style & lighting prompt
boundary = f"----Boundary{uuid.uuid4().hex}"
with open(r"Z:\SketchSpace-AI-Share\SketchSpace-AI-Share\examples\new_bathroom_sketch.png", "rb") as f:
    sketch_bytes = f.read()

parts = [
    f"--{boundary}\r\nContent-Disposition: form-data; name=\"file\"; filename=\"bath.png\"\r\nContent-Type: image/png\r\n\r\n".encode("latin-1"),
    sketch_bytes,
    f"\r\n--{boundary}\r\nContent-Disposition: form-data; name=\"model\"\r\n\r\ncontrolnet-local\r\n--{boundary}--\r\n".encode("latin-1")
]
payload = b"".join(parts)

custom_p = "photorealistic luxury spa bathroom interior, porcelain sink, vanity mirror, glass shower enclosure, ceramic wall tiles, Calacatta gold marble surfaces, warm ambient recessed lighting, high resolution, sharp focus, 8k"
query_str = urllib.parse.urlencode({
    "model": "controlnet-local",
    "category": "bathroom",
    "steps": 15,
    "prompt": custom_p
})

req_gen = urllib.request.Request(
    f"http://127.0.0.1:8000/api/generate?{query_str}",
    data=payload,
    headers={"Content-Type": f"multipart/form-data; boundary={boundary}"}
)
print("Dispatching generation for bathroom sketch with compound prompt...")
with urllib.request.urlopen(req_gen, timeout=180) as resp:
    res = json.loads(resp.read().decode())
    print("GENERATION RESULT:", json.dumps(res, indent=2))
