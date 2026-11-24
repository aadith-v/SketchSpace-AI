import urllib.request
import json
import sys

BASE_URL = "http://127.0.0.1:8000"

def run_tests():
    print("=== SKETCHSPACE AI: LUXURY ARCHITECTURAL ATELIER AUDIT ===")
    
    # 1. Fetch Root HTML
    print("\n[1] Testing Root HTML (GET /)...")
    req = urllib.request.Request(f"{BASE_URL}/")
    with urllib.request.urlopen(req) as resp:
        assert resp.status == 200, f"Expected 200, got {resp.status}"
        html = resp.read().decode('utf-8')
        print(f"  -> HTTP 200 OK | Size: {len(html):,} characters")
        
    # 2. Verify Visual, Typography & Architectural DOM Elements
    print("\n[2] Verifying Architectural Atelier Design & DOM Elements...")
    checks = {
        "Atelier Serif Display (Cormorant Garamond)": "Cormorant+Garamond",
        "Editorial Serif (Playfair Display)": "Playfair+Display",
        "Atelier Body Typography (Manrope)": "Manrope",
        "Atelier Monospace Tech (IBM Plex Mono)": "IBM+Plex+Mono",
        "Warm Palette: Travertine": "--travertine",
        "Warm Palette: Sandstone": "--sandstone",
        "Warm Palette: Antique Brass": "--antique-brass",
        "Warm Palette: Walnut": "--walnut-rich",
        "Ambient Warm Lighting Fields": "atelier-light-fields",
        "Ambient Spatial Particles Canvas": "ambient-particles-canvas",
        "Minimal Premium Nav Bar": "spatial-nav",
        "RTX 3050 Hardware Status Beacon": "engine-status-tag",
        "Primary Headline Part 1 (From Imagination)": "From Imagination",
        "Primary Headline Part 2 (To Architecture.)": "To Architecture.",
        "Secondary Tagline": "Where ideas become extraordinary spaces.",
        "3D Cutaway Dollhouse": "hero-dollhouse-3d",
        "Dollhouse Floor Slab": "dollhouse-slab",
        "Dollhouse Living Room Badge": "badge-living",
        "Dollhouse Bedroom Badge": "badge-bedroom",
        "Dollhouse Kitchen Badge": "badge-kitchen",
        "Dollhouse Bathroom Badge": "badge-bathroom",
        "Dollhouse Spin Pause/Resume Button": "btn-house-spin-toggle",
        "Section 2: Architectural Showcase Gallery": "section-gallery-showcase",
        "Section 3: The Design Process (Storytelling)": "section-storytelling",
        "Interactive Comparison Slider": "homepage-compare-slider",
        "Section 4: Spatial 3D Experience": "spatial-3d-intro-section",
        "Section 5: Creative Studio Workspace": "studio-spatial-section",
        "Section 6: Engineered for Local AI": "ENGINEERED FOR LOCAL AI",
        "Measured 649.8 MB Peak VRAM Badge": "649.8 MB",
        "Section 7: Final Call to Action": "final-cta-section",
        "Architectural Drafting Dock": "spatial-toolbar",
        "512x512 Drawing Canvas": "drawing-canvas",
        "Toggleable Blueprint Grid": "grid-canvas",
        "Preset Layout Chips Deck": "layout-presets-deck",
        "Prompt Matrix Synthesizer": "spatial-params-matrix",
        "Engine Stack (ControlNet + Pix2Pix)": "engine-stack",
        "Synthesize Action Button": "btn-synthesize-master",
        "Spatial Visualizer Viewport": "spatial-visualizer-stage",
        "Interactive Comparison Curtain": "spatial-compare-box",
        "Multi-Stage Loading Sequence": "spatial-synthesis-overlay",
        "Spinning Gyro Loader": "spatial-gyro-spinner",
        "Live Millisecond Telemetry Timer": "live-timer-badge",
        "Real-Time Telemetry HUD": "spatial-telemetry-hud",
        "My Designs Portfolio Section": "gallery-spatial-section",
        "Save Project Modal Window": "spatial-modal-window",
        "Fullscreen Presentation Mode Curtain": "presentation-fullscreen-curtain",
        "Spatial Toast Notification": "spatial-toast"
    }

    all_passed = True
    for name, tag in checks.items():
        present = tag in html
        status = "PASSED" if present else "FAILED"
        if not present:
            all_passed = False
        print(f"  [{status}] {name}")

    # 3. Verify Backend API Endpoints
    print("\n[3] Testing Backend API Endpoints...")
    endpoints = [
        ("/api/models", "Available Models"),
        ("/api/examples", "Example Sketches List"),
        ("/api/sketches/example/new_bedroom_sketch.png", "Bedroom Sketch Static Asset"),
        ("/api/image/local_cn_living_room_1795536539194.png", "Verified Generated Interior Image")
    ]
    for path, desc in endpoints:
        url = f"{BASE_URL}{path}"
        try:
            with urllib.request.urlopen(url) as r:
                print(f"  [PASSED] {desc} ({path}) -> HTTP {r.status} (Type: {r.headers.get('Content-Type')})")
        except Exception as e:
            print(f"  [FAILED] {desc} ({path}) -> Error: {e}")
            all_passed = False

    print("\n" + "="*50)
    if all_passed:
        print("ALL LUXURY ARCHITECTURAL ATELIER AUDITS PASSED 100%!")
    else:
        print("SOME CHECKS FAILED - REVIEW LOGS ABOVE.")
        sys.exit(1)

if __name__ == "__main__":
    run_tests()
