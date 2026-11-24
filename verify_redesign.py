import urllib.request
import urllib.parse
import json
import sys
import uuid
from pathlib import Path

BASE_URL = "http://127.0.0.1:8000"

def run_tests():
    print("=" * 60)
    print("SKETCHSPACE AI: COMPLETE REDESIGN VERIFICATION SUITE")
    print("=" * 60)

    # 1. Health & Status
    print("\n[1] Testing Health & Engine Status...")
    with urllib.request.urlopen(f"{BASE_URL}/api/health") as r:
        assert r.status == 200
        data = json.loads(r.read())
        assert data["status"] == "healthy"
        print("  -> Health Check: PASSED")

    with urllib.request.urlopen(f"{BASE_URL}/api/status") as r:
        assert r.status == 200
        status_data = json.loads(r.read())
        assert status_data["local_controlnet"]["available"] is True
        print("  -> Engine Status: PASSED (Local ControlNet SD 1.5 Ready)")

    # 2. Root HTML Structure & Hierarchy
    print("\n[2] Testing HTML Structure & 3 Independent Destinations...")
    with urllib.request.urlopen(f"{BASE_URL}/") as r:
        assert r.status == 200
        html = r.read().decode("utf-8")
        print(f"  -> Root HTML: HTTP 200 OK ({len(html):,} characters)")

    checks = {
        "Brand Signature Headline": "From Imagination",
        "Brand Signature Headline Part 2": "To Architecture.",
        "Palette: Deep Petrol Blue": "--bg-petrol-deep: #0a1924;",
        "Palette: Rich Teal": "--rich-teal: #1b677a;",
        "Palette: Terracotta": "--terracotta: #c85a38;",
        "Palette: Warm Ivory": "--warm-ivory: #faf7f2;",
        "Destination 1: Overview View": 'id="view-overview"',
        "Destination 2: Creative Studio View": 'id="view-studio"',
        "Destination 3: My Designs View": 'id="view-designs"',
        "Navigation Tabs (3 Distinct Destinations)": 'id="nav-btn-overview"',
        "Navigation Tab Creative Studio": 'id="nav-btn-studio"',
        "Navigation Tab My Designs": 'id="nav-btn-designs"',
        "Creative Studio: Left Panel Sketch Studio": 'class="sketch-studio-panel"',
        "Creative Studio: Drawing Canvas 512x512": 'id="drawing-canvas"',
        "Creative Studio: Blueprint Grid Canvas": 'id="grid-canvas"',
        "Creative Studio: Toolbar Dock": 'class="sketch-toolbar-dock"',
        "Creative Studio: Tool Pencil": 'id="tool-pencil"',
        "Creative Studio: Tool Straight Line": 'id="tool-line"',
        "Creative Studio: Tool Rectangle": 'id="tool-rect"',
        "Creative Studio: Tool Eraser": 'id="tool-eraser"',
        "Creative Studio: Brush Size Slider": 'id="stroke-slider"',
        "Creative Studio: Ink Swatches": 'class="ink-swatches-group"',
        "Creative Studio: Room Presets Deck": 'class="preset-chips-deck"',
        "Creative Studio: Right Panel Interior Viewport": 'class="interior-viewport-panel"',
        "Creative Studio: Master Action Button": 'id="btn-synthesize-master"',
        "Fixed Before/After: Reveal Slider": 'id="stage-compare-slider"',
        "Fixed Before/After: Bottom Layer": 'id="compare-bottom-img"',
        "Fixed Before/After: Top Layer Clip-Path": 'id="compare-top-img"',
        "Fixed Before/After: Divider Handle": 'id="compare-divider-handle"',
        "Fixed Before/After: Side-by-Side Alternative": 'id="stage-side-by-side"',
        "First-Person 3D Room Experience Section": 'id="section-spatial-3d-experience"',
        "Three.js 3D Canvas Stage Container": 'id="spatial-3d-stage-container"',
        "3D Mode A: Depth Walkthrough Tab": 'id="tab-3d-mode-a"',
        "3D Mode B: Procedural 3D Room Tab": 'id="tab-3d-mode-b"',
        "3D Camera Presets Bar": 'class="camera-presets-bar"',
        "3D Touch/Mobile D-Pad Controls": 'class="dpad-touch-controls"',
        "My Designs: Portfolio Header": 'My Architectural Designs',
        "My Designs: Search Input": 'id="portfolio-search-input"',
        "My Designs: Category Filter Chips": 'class="portfolio-filter-chips"',
        "My Designs: Saved Designs Grid": 'id="saved-designs-grid-container"',
        "Discreet Technology Section": 'class="discreet-tech-section"',
        "Fullscreen Presentation Curtain": 'id="fullscreen-presentation-curtain"'
    }

    all_passed = True
    for name, snippet in checks.items():
        present = snippet in html
        status = "PASSED" if present else "FAILED"
        if not present:
            all_passed = False
        print(f"  [{status}] {name}")

    assert all_passed, "Some DOM structural checks failed!"

    # 3. Verify Depth Map API Endpoint
    print("\n[3] Testing On-Demand Depth Estimation Endpoint...")
    sample_img = "local_cn_living_room_1795536539194.png"
    depth_url = f"{BASE_URL}/api/depth/{sample_img}"
    with urllib.request.urlopen(depth_url) as r:
        assert r.status == 200
        content_type = r.headers.get("Content-Type")
        depth_data = r.read()
        assert content_type == "image/png"
        assert len(depth_data) > 1000
        print(f"  -> Depth Map Endpoint: HTTP 200 OK (PNG, {len(depth_data):,} bytes)")

    # 4. Live Offline ControlNet Generation Test
    print("\n[4] Dispatching Live Local ControlNet Generation...")
    boundary = f"----Boundary{uuid.uuid4().hex}"
    sketch_path = Path("examples/new_living_room_sketch.png")
    with open(sketch_path, "rb") as f:
        sketch_bytes = f.read()

    parts = [
        f"--{boundary}\r\nContent-Disposition: form-data; name=\"file\"; filename=\"living_sketch.png\"\r\nContent-Type: image/png\r\n\r\n".encode("latin-1"),
        sketch_bytes,
        f"\r\n--{boundary}\r\nContent-Disposition: form-data; name=\"model\"\r\n\r\ncontrolnet-local\r\n--{boundary}--\r\n".encode("latin-1")
    ]
    payload = b"".join(parts)

    query = urllib.parse.urlencode({
        "model": "controlnet-local",
        "category": "living_room",
        "steps": 15,
        "prompt": "photorealistic luxury contemporary living room interior, designer sofa, travertine coffee table, natural sunlight, architectural digest, 8k"
    })

    req = urllib.request.Request(
        f"{BASE_URL}/api/generate?{query}",
        data=payload,
        headers={"Content-Type": f"multipart/form-data; boundary={boundary}"}
    )

    with urllib.request.urlopen(req, timeout=120) as resp:
        gen_data = json.loads(resp.read().decode())
        assert gen_data["success"] is True
        assert gen_data["generated_url"].startswith("/api/image/")
        assert "depth_url" in gen_data
        print(f"  -> Live ControlNet Pipeline: PASSED!")
        print(f"     Generated Image: {gen_data['generated_filename']}")
        print(f"     Depth URL: {gen_data['depth_url']}")
        print(f"     Gen Time: {gen_data['metrics']['gen_time_sec']}s")
        print(f"     Peak VRAM: {gen_data['metrics']['vram_peak_allocated_mb']} MB")

    # Verify generated depth url works
    with urllib.request.urlopen(f"{BASE_URL}{gen_data['depth_url']}") as r:
        assert r.status == 200
        print("  -> Generated Image Depth Map Retrieval: PASSED (HTTP 200 OK)")

    print("\n" + "=" * 60)
    print("ALL VERIFICATION SUITE TESTS PASSED 100%!")
    print("=" * 60)

if __name__ == "__main__":
    run_tests()
