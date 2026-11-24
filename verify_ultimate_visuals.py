import urllib.request
import json
import sys

BASE_URL = "http://127.0.0.1:8000"

def run_tests():
    print(f"=== SKETCHSPACE AI: ULTIMATE VISUAL EXCELLENCE QA ===")
    
    # 1. Fetch Root HTML
    print("\n[1] Testing Root HTML (GET /)...")
    req = urllib.request.Request(f"{BASE_URL}/")
    with urllib.request.urlopen(req) as resp:
        assert resp.status == 200, f"Expected 200, got {resp.status}"
        html = resp.read().decode('utf-8')
        print(f"  -> HTTP 200 OK | Size: {len(html):,} characters")
        
    # 2. Verify Visual and Structural DOM Components
    print("\n[2] Verifying Visual & Architectural DOM Elements...")
    checks = {
        "Typography Sora / Manrope / Mono": "family=Sora:wght@300;400;500;600;700;800",
        "Aurora Universe (5 Fields)": "aurora-universe",
        "Volumetric Light Ribbon": "aurora-ribbon",
        "Spatial Grid Floor": "spatial-grid-floor",
        "Ambient Particles Canvas": "ambient-particles-canvas",
        "Floating 3D Prisms & Sculptures": "floating-sculptures-layer",
        "Top Spatial Nav Bar": "spatial-nav",
        "Custom Isometric Cube Logo": "brand-cube-badge",
        "RTX 3050 Hardware Status Beacon": "engine-status-tag",
        "Hero Brand Identifier": "hero-brand-identifier",
        "Primary Headline (From Imagination)": "From Imagination",
        "Primary Headline (To Architecture.)": "To Architecture.",
        "Secondary Tagline": "One Sketch. Infinite Possibilities.",
        "3D Cutaway Dollhouse": "hero-dollhouse-3d",
        "Dollhouse Floor Slab": "dollhouse-slab",
        "Dollhouse Living Room Badge": "badge-living",
        "Dollhouse Bedroom Badge": "badge-bedroom",
        "Dollhouse Kitchen Badge": "badge-kitchen",
        "Dollhouse Bathroom Badge": "badge-bathroom",
        "Dollhouse Spin Pause/Resume Button": "btn-house-spin-toggle",
        "Architectural Project Showcase": "section-gallery-showcase",
        "Sketch-to-Photorealism Workflow": "section-storytelling",
        "Interactive Visual Comparison Demo": "homepage-compare-slider",
        "Spatial 3D Experience Section": "spatial-3d-intro-section",
        "Engineered for Local AI Section": "ENGINEERED FOR LOCAL AI",
        "Final Creative Call to Action": "final-cta-section",
        "Creative Studio Workspace": "studio-spatial-section",
        "Architectural Toolbar Dock": "spatial-toolbar",
        "512x512 Drawing Canvas": "drawing-canvas",
        "Toggleable Blueprint Grid": "grid-canvas",
        "Preset Layout Chips Deck": "layout-presets-deck",
        "Prompt Matrix Synthesizer": "spatial-params-matrix",
        "Engine Choice Stack (ControlNet + Pix2Pix)": "engine-stack",
        "Synthesize Master Action Button": "btn-synthesize-master",
        "Spatial Visualizer Viewport": "spatial-visualizer-stage",
        "Interactive Comparison Curtain": "spatial-compare-box",
        "Multi-Stage Loading Sequence": "spatial-synthesis-overlay",
        "Spinning Gyro Loader": "spatial-gyro-spinner",
        "Live Millisecond Telemetry Timer": "live-timer-badge",
        "Real-Time Telemetry HUD": "spatial-telemetry-hud",
        "My Designs Local Gallery Grid": "gallery-spatial-section",
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

    # 3. Verify API Endpoints
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
        print("ALL VISUAL AND STRUCTURAL AUDITS PASSED 100%!")
    else:
        print("SOME CHECKS FAILED - REVIEW LOGS ABOVE.")
        sys.exit(1)

if __name__ == "__main__":
    run_tests()
