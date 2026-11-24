"""Verification script for 3D Spatial Reconstruction & Scene Extraction."""

import json
import requests

BASE_URL = "http://127.0.0.1:8000"

def test_scene_api():
    print("=== Testing Scene Objects Endpoint ===")
    filename = "local_cn_living_room_1795548995653.png"
    r = requests.get(f"{BASE_URL}/api/scene-objects/{filename}", timeout=10)
    print("Scene API Status:", r.status_code)
    assert r.status_code == 200, f"Failed: {r.text}"

    data = r.json()
    print("Scene success:", data.get("success"))
    print("Room dimensions:", data.get("room_dimensions"))
    print("Materials:", data.get("materials"))
    objects = data.get("objects", [])
    print(f"Total detected objects: {len(objects)}")
    for obj in objects:
        print(f" - [{obj['category']}] {obj['label']} at pos: {obj['position']} dims: {obj['dimensions']}")

    categories = [o["category"] for o in objects]
    assert "ceiling_fan" in categories, "Must detect ceiling fan"
    assert "window" in categories, "Must detect windows"
    assert "door" in categories, "Must detect doorway"
    assert "plant" in categories, "Must detect plant clusters"

    print("\n=== Testing Depth Map Endpoint ===")
    r_depth = requests.get(f"{BASE_URL}/api/depth/{filename}", timeout=10)
    print("Depth API Status:", r_depth.status_code)
    assert r_depth.status_code == 200
    assert len(r_depth.content) > 1000

    print("\n=== ALL SCENE RECONSTRUCTION TESTS PASSED! ===")

if __name__ == "__main__":
    test_scene_api()
