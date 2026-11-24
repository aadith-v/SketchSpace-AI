"""End-to-End Test for Sketch Conditioning Fix and Architectural Preservation."""

import json
import os
import sys
import time
from pathlib import Path

import requests

BASE_URL = "http://127.0.0.1:8000"
USER_SKETCH_PATH = Path(r"C:\Users\aadit\.gemini\antigravity\brain\83b488cf-1cce-4b53-aaa5-2f8d09a20551\.user_uploaded\media_1795548307116_c663ae59.jpg")

def test_pipeline():
    print("=== Step 1: Health & ControlNet Status Check ===")
    r_health = requests.get(f"{BASE_URL}/api/health", timeout=10)
    print("Health response:", r_health.status_code, r_health.json())
    assert r_health.status_code == 200

    r_status = requests.get(f"{BASE_URL}/api/status", timeout=10)
    print("ControlNet status:", r_status.status_code, r_status.json())
    assert r_status.status_code == 200

    print("\n=== Step 2: Preprocess Sketch Endpoint Test ===")
    assert USER_SKETCH_PATH.exists(), f"User sketch not found at {USER_SKETCH_PATH}"

    with open(USER_SKETCH_PATH, "rb") as f:
        files = {"file": ("user_sketch_fan.jpg", f, "image/jpeg")}
        r_prep = requests.post(f"{BASE_URL}/api/preprocess-sketch", files=files, timeout=15)

    print("Preprocess response:", r_prep.status_code)
    prep_data = r_prep.json()
    print("Preprocess JSON:", json.dumps(prep_data, indent=2))
    assert r_prep.status_code == 200
    assert prep_data["success"] is True
    assert "conditioning_url" in prep_data
    assert "input_sha256" in prep_data
    assert "conditioning_sha256" in prep_data

    # Fetch conditioning image from server
    r_cond = requests.get(f"{BASE_URL}{prep_data['conditioning_url']}", timeout=10)
    assert r_cond.status_code == 200
    cond_save_path = Path("examples/verified_conditioning_fan.png")
    cond_save_path.write_bytes(r_cond.content)
    print(f"Verified conditioning image retrieved ({len(r_cond.content)} bytes), saved to {cond_save_path}")

    print("\n=== Step 3: End-to-End Generation Test (Model: controlnet-local) ===")
    with open(USER_SKETCH_PATH, "rb") as f:
        files = {"file": ("user_sketch_fan.jpg", f, "image/jpeg")}
        params = {
            "model": "controlnet-local",
            "category": "living_room",
            "prompt": "photorealistic modern interior room, architectural precision, natural daylight through windows on left wall, open central doorway, ceiling fan on wooden ceiling, potted indoor plants, hardwood flooring, architectural digest photography, 8k resolution, sharp focus",
            "negative_prompt": "outdoor, exterior, patio, garden, yard, hedge, bushes on walls, altered architectural layout, missing windows, missing doors, shifted walls, cartoon, 3d render, blurry, distorted architecture, low quality",
            "steps": 18,
            "conditioning_scale": 1.15,
            "seed": 4242
        }
        t0 = time.time()
        print("Submitting /api/generate request with seed=4242, conditioning_scale=1.15...")
        r_gen = requests.post(f"{BASE_URL}/api/generate", files=files, params=params, timeout=180)
        dt = time.time() - t0

    print(f"Generation finished in {dt:.1f}s, HTTP status: {r_gen.status_code}")
    assert r_gen.status_code == 200, f"Generate failed: {r_gen.text}"
    gen_data = r_gen.json()
    print("Generation response JSON:", json.dumps(gen_data, indent=2))

    # Retrieve generated image
    r_img = requests.get(f"{BASE_URL}{gen_data['generated_url']}", timeout=10)
    assert r_img.status_code == 200
    out_save_path = Path("examples/verified_generated_fan.png")
    out_save_path.write_bytes(r_img.content)
    print(f"Verified generated interior saved to {out_save_path} ({len(r_img.content)} bytes)")

    # Copy to artifact directory for inspection
    artifact_dir = Path(r"C:\Users\aadit\.gemini\antigravity\brain\83b488cf-1cce-4b53-aaa5-2f8d09a20551")
    (artifact_dir / "verified_conditioning_fan.png").write_bytes(r_cond.content)
    (artifact_dir / "verified_generated_fan.png").write_bytes(r_img.content)

    print("\n=== ALL TESTS PASSED SUCCESSFULLY! ===")
    print(f"Input SHA-256:        {gen_data.get('input_sha256')}")
    print(f"Conditioning SHA-256: {gen_data.get('conditioning_sha256')}")
    print(f"Output SHA-256:       {gen_data.get('output_sha256')}")
    print(f"Seed Used:            {gen_data.get('seed_used')}")
    print(f"Conditioning URL:     {gen_data.get('conditioning_url')}")

if __name__ == "__main__":
    test_pipeline()
