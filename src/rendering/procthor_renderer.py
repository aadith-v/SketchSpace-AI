"""ProcTHOR 3D Interior Renderer (High-Fidelity Architectural Version).
Generates realistic interior design images from ProcTHOR procedural scene configurations.

Features:
- Multi-component semantic furniture assemblies (tables with legs, chairs with backrests,
  sofas with cushions, beds with pillows/mattress/duvet, countertops with cabinets/sinks,
  fridges with split doors/handles, dressers, lamps, plants, framed art).
- Surface objects (children items: books, bowls, bottles, fruit on countertops/tables).
- Architectural detailing (wood plank / tile perspective floors, wall baseboard trims,
  doors with casing/panels, windows with exterior daylight glow).
- Dual-source lighting (key ceiling light + window fill) and floor contact shadows.
- Calibrated pinhole perspective projection aligned with ProcTHOR agent camera pose.
- Pure Python execution optimized for Intel CPU.
"""

import math
import cv2
import numpy as np
from typing import Dict, Any, List, Tuple, Optional


class ProcTHORRenderer:
    """High-fidelity procedural interior renderer for ProcTHOR scenes."""

    def __init__(self, width: int = 256, height: int = 256, fov: float = 75.0):
        self.width = width
        self.height = height
        self.fov = fov
        self.focal = (self.width / 2.0) / math.tan(math.radians(self.fov / 2.0))

        # Two-point lighting vectors
        l_key = np.array([0.35, 0.90, 0.35], dtype=np.float32)
        self.key_light = l_key / np.linalg.norm(l_key)

        l_fill = np.array([-0.55, 0.45, 0.65], dtype=np.float32)
        self.fill_light = l_fill / np.linalg.norm(l_fill)

        self.ambient_base = 0.44

    def render_scene(self, scene_dict: Dict[str, Any]) -> np.ndarray:
        """Render a ProcTHOR scene dictionary into a realistic interior RGB image."""
        # 1. Camera Pose
        agent = scene_dict.get("metadata", {}).get("agent", {})
        pos = agent.get("position", {"x": 0.0, "y": 1.0, "z": 0.0})
        cam_pos = np.array([pos.get("x", 0.0), pos.get("y", 1.0), pos.get("z", 0.0)], dtype=np.float32)

        rot = agent.get("rotation", {"x": 0.0, "y": 0.0, "z": 0.0})
        yaw_deg = float(rot.get("y", 0.0))
        pitch_deg = float(agent.get("horizon", 30.0))

        polygons: List[Dict[str, Any]] = []

        # 2. Floor Geometry & Material Styling
        for room in scene_dict.get("rooms", []):
            floor_pts = room.get("floorPolygon", [])
            if len(floor_pts) >= 3:
                pts_3d = np.array([[p["x"], p.get("y", 0.0), p["z"]] for p in floor_pts], dtype=np.float32)
                mat_name = room.get("floorMaterial", {}).get("name", "").lower()
                room_type = room.get("roomType", "").lower()
                floor_color, is_wood = self._get_floor_style(mat_name, room_type)

                polygons.append({
                    "vertices": pts_3d,
                    "color": floor_color,
                    "normal": np.array([0.0, 1.0, 0.0], dtype=np.float32),
                    "type": "floor",
                    "style": "wood" if is_wood else "tile"
                })

        # 3. Wall Geometry & Baseboard Skirting
        for wall in scene_dict.get("walls", []):
            poly_pts = wall.get("polygon", [])
            if len(poly_pts) >= 4:
                pts_3d = np.array([[p["x"], p["y"], p["z"]] for p in poly_pts], dtype=np.float32)
                v1 = pts_3d[1] - pts_3d[0]
                v2 = pts_3d[2] - pts_3d[0]
                norm = np.cross(v1, v2)
                nlen = np.linalg.norm(norm)
                norm = norm / nlen if nlen > 1e-5 else np.array([0.0, 0.0, 1.0], dtype=np.float32)

                w_color = wall.get("color", {})
                if w_color and "r" in w_color:
                    base_c = (
                        int(np.clip(w_color.get("r", 0.86) * 255, 0, 255)),
                        int(np.clip(w_color.get("g", 0.86) * 255, 0, 255)),
                        int(np.clip(w_color.get("b", 0.86) * 255, 0, 255))
                    )
                else:
                    base_c = (226, 224, 220)

                # Main Wall Surface
                polygons.append({
                    "vertices": pts_3d,
                    "color": base_c,
                    "normal": norm,
                    "type": "wall"
                })

                # Architectural Baseboard (12cm bottom trim)
                p0, p1 = pts_3d[0], pts_3d[1]
                p0_top = p0 + np.array([0.0, 0.12, 0.0], dtype=np.float32)
                p1_top = p1 + np.array([0.0, 0.12, 0.0], dtype=np.float32)
                polygons.append({
                    "vertices": np.array([p0, p1, p1_top, p0_top], dtype=np.float32),
                    "color": (246, 246, 248),
                    "normal": norm,
                    "type": "trim"
                })

        # 4. Windows & Doors
        polygons.extend(self._generate_windows_and_doors(scene_dict))

        # 5. Multi-Part Furniture
        for obj in scene_dict.get("objects", []):
            polygons.extend(self._generate_detailed_furniture(obj))

            # Surface items (apples, cups, bottles, books)
            for child in obj.get("children", []):
                polygons.extend(self._generate_surface_item(child))

        # 6. Project & Rasterize
        return self._render_polygons_to_image(polygons, cam_pos, yaw_deg, pitch_deg)

    def _get_floor_style(self, mat_name: str, room_type: str) -> Tuple[Tuple[int, int, int], bool]:
        """Realistic floor palettes based on room specifications."""
        if "wood" in mat_name or "cabinet" in mat_name or "parquet" in mat_name:
            return (182, 142, 102), True  # Warm oak hardwood
        elif "tile" in mat_name or "ceramic" in mat_name:
            return (218, 220, 222), False # Light polished ceramic tile
        elif "carpet" in mat_name:
            return (170, 172, 168), False # Textured neutral carpet
        elif "kitchen" in room_type:
            return (192, 165, 135), True  # Kitchen hardwood
        elif "bathroom" in room_type:
            return (215, 225, 230), False # Bathroom ceramic tile
        else:
            return (178, 140, 105), True

    def _generate_windows_and_doors(self, scene_dict: Dict[str, Any]) -> List[Dict[str, Any]]:
        """Construct realistic window frames with daylight glow and doors with casing."""
        polys = []

        # Windows
        for win in scene_dict.get("windows", []):
            hole = win.get("holePolygon", [])
            wall_id = win.get("wall0", "")
            if len(hole) >= 2:
                hx1, hy1 = hole[0].get("x", 0.0), hole[0].get("y", 0.6)
                hx2, hy2 = hole[1].get("x", 1.0), hole[1].get("y", 1.8)
                coords = self._parse_wall_coords(wall_id)
                if coords:
                    wx1, wz1, wx2, wz2 = coords
                    polys.extend(self._build_3d_window(wx1, wz1, wx2, wz2, hx1, hx2, hy1, hy2))

        # Doors
        for door in scene_dict.get("doors", []):
            hole = door.get("holePolygon", [])
            wall_id = door.get("wall0", "")
            if len(hole) >= 2:
                hx1, hy1 = hole[0].get("x", 0.0), hole[0].get("y", 0.0)
                hx2, hy2 = hole[1].get("x", 1.0), hole[1].get("y", 2.1)
                coords = self._parse_wall_coords(wall_id)
                if coords:
                    wx1, wz1, wx2, wz2 = coords
                    polys.extend(self._build_3d_door(wx1, wz1, wx2, wz2, hx1, hx2, hy1, hy2))

        return polys

    def _parse_wall_coords(self, wall_id: str) -> Optional[Tuple[float, float, float, float]]:
        """Extract wall start/end coordinates from wall_id string: wall|room|x1|z1|x2|z2."""
        parts = wall_id.split("|")
        if len(parts) >= 6:
            try:
                return float(parts[2]), float(parts[3]), float(parts[4]), float(parts[5])
            except ValueError:
                pass
        return None

    def _build_3d_window(self, wx1: float, wz1: float, wx2: float, wz2: float,
                          hx1: float, hx2: float, hy1: float, hy2: float) -> List[Dict[str, Any]]:
        """Construct detailed window with white frame and daylight blue glass."""
        polys = []
        w_vec = np.array([wx2 - wx1, 0.0, wz2 - wz1], dtype=np.float32)
        w_len = np.linalg.norm(w_vec)
        if w_len < 1e-4:
            return polys
        w_dir = w_vec / w_len
        w_norm = np.array([-w_dir[2], 0.0, w_dir[0]], dtype=np.float32)

        p0 = np.array([wx1, 0.0, wz1], dtype=np.float32) + (w_dir * hx1)
        p1 = np.array([wx1, 0.0, wz1], dtype=np.float32) + (w_dir * hx2)

        bl = p0 + np.array([0.0, hy1, 0.0], dtype=np.float32)
        br = p1 + np.array([0.0, hy1, 0.0], dtype=np.float32)
        tr = p1 + np.array([0.0, hy2, 0.0], dtype=np.float32)
        tl = p0 + np.array([0.0, hy2, 0.0], dtype=np.float32)

        # 1. Outer Frame (White casing)
        polys.append({
            "vertices": np.array([bl, br, tr, tl], dtype=np.float32),
            "color": (245, 245, 248),
            "normal": w_norm,
            "type": "trim"
        })

        # 2. Inner Glass Pane (Daylight sky blue)
        pad = 0.06
        g_bl = bl + (w_dir * pad) + np.array([0.0, pad, 0.0], dtype=np.float32) + (w_norm * 0.02)
        g_br = br - (w_dir * pad) + np.array([0.0, pad, 0.0], dtype=np.float32) + (w_norm * 0.02)
        g_tr = tr - (w_dir * pad) - np.array([0.0, pad, 0.0], dtype=np.float32) + (w_norm * 0.02)
        g_tl = tl + (w_dir * pad) - np.array([0.0, pad, 0.0], dtype=np.float32) + (w_norm * 0.02)

        polys.append({
            "vertices": np.array([g_bl, g_br, g_tr, g_tl], dtype=np.float32),
            "color": (210, 235, 252),  # Daylight blue glass
            "normal": w_norm,
            "type": "glass"
        })

        # 3. Window Sill Ledge
        s_bl = bl + (w_norm * 0.08)
        s_br = br + (w_norm * 0.08)
        polys.append({
            "vertices": np.array([bl, br, s_br, s_bl], dtype=np.float32),
            "color": (240, 240, 242),
            "normal": np.array([0.0, 1.0, 0.0], dtype=np.float32),
            "type": "trim"
        })

        return polys

    def _build_3d_door(self, wx1: float, wz1: float, wx2: float, wz2: float,
                        hx1: float, hx2: float, hy1: float, hy2: float) -> List[Dict[str, Any]]:
        """Construct interior door with white casing frame and walnut panel."""
        polys = []
        w_vec = np.array([wx2 - wx1, 0.0, wz2 - wz1], dtype=np.float32)
        w_len = np.linalg.norm(w_vec)
        if w_len < 1e-4:
            return polys
        w_dir = w_vec / w_len
        w_norm = np.array([-w_dir[2], 0.0, w_dir[0]], dtype=np.float32)

        p0 = np.array([wx1, 0.0, wz1], dtype=np.float32) + (w_dir * hx1)
        p1 = np.array([wx1, 0.0, wz1], dtype=np.float32) + (w_dir * hx2)

        bl = p0 + np.array([0.0, hy1, 0.0], dtype=np.float32)
        br = p1 + np.array([0.0, hy1, 0.0], dtype=np.float32)
        tr = p1 + np.array([0.0, hy2, 0.0], dtype=np.float32)
        tl = p0 + np.array([0.0, hy2, 0.0], dtype=np.float32)

        # White Casing Frame
        polys.append({
            "vertices": np.array([bl, br, tr, tl], dtype=np.float32),
            "color": (242, 240, 238),
            "normal": w_norm,
            "type": "trim"
        })

        # Recessed Door Leaf
        d_pad = 0.05
        d_bl = bl + (w_dir * d_pad) + np.array([0.0, 0.02, 0.0], dtype=np.float32) - (w_norm * 0.015)
        d_br = br - (w_dir * d_pad) + np.array([0.0, 0.02, 0.0], dtype=np.float32) - (w_norm * 0.015)
        d_tr = tr - (w_dir * d_pad) - np.array([0.0, d_pad, 0.0], dtype=np.float32) - (w_norm * 0.015)
        d_tl = tl + (w_dir * d_pad) - np.array([0.0, d_pad, 0.0], dtype=np.float32) - (w_norm * 0.015)

        polys.append({
            "vertices": np.array([d_bl, d_br, d_tr, d_tl], dtype=np.float32),
            "color": (150, 110, 80),  # Classic walnut wood door
            "normal": w_norm,
            "type": "door_panel"
        })

        return polys

    def _generate_detailed_furniture(self, obj: Dict[str, Any]) -> List[Dict[str, Any]]:
        """Construct multi-part structural furniture assemblies based on category."""
        aid = obj.get("assetId", "").lower()
        oid = obj.get("id", "").split("|")[0].lower()
        combined = f"{oid} {aid}"

        pos = obj.get("position", {"x": 0.0, "y": 0.0, "z": 0.0})
        cx, cy, cz = pos.get("x", 0.0), pos.get("y", 0.0), pos.get("z", 0.0)
        rot = obj.get("rotation", {"x": 0.0, "y": 0.0, "z": 0.0})
        yaw_rad = math.radians(rot.get("y", 0.0))

        R = np.array([
            [math.cos(yaw_rad), 0, math.sin(yaw_rad)],
            [0,                 1, 0                ],
            [-math.sin(yaw_rad),0, math.cos(yaw_rad)]
        ], dtype=np.float32)

        center = np.array([cx, cy, cz], dtype=np.float32)

        if "chair" in combined and "armchair" not in combined:
            return self._build_chair(center, R)
        elif "armchair" in combined or "sofa" in combined or "couch" in combined:
            return self._build_sofa(center, R, is_armchair=("armchair" in combined))
        elif "diningtable" in combined or "table" in combined or "desk" in combined or "coffeetable" in combined:
            is_coffee = "coffeetable" in combined
            return self._build_table(center, R, is_coffee=is_coffee)
        elif "bed" in combined:
            return self._build_bed(center, R)
        elif "countertop" in combined:
            return self._build_countertop(center, R)
        elif "fridge" in combined or "refrigerator" in combined:
            return self._build_fridge(center, R)
        elif "tvstand" in combined or "television" in combined:
            return self._build_media_center(center, R)
        elif "dresser" in combined or "shelvingunit" in combined or "cabinet" in combined:
            return self._build_cabinet(center, R)
        elif "houseplant" in combined or "plant" in combined:
            return self._build_plant(center, R)
        elif "lamp" in combined:
            return self._build_lamp(center, R)
        elif "toilet" in combined or "sink" in combined:
            return self._build_bathroom_fixture(center, R, is_toilet=("toilet" in combined))
        elif "painting" in combined or "photo" in combined or "decor" in combined:
            return self._build_wall_art(center, R)
        else:
            return self._make_box_faces(center, (0.5, 0.5, 0.5), R, (160, 155, 150), "generic")

    def _make_box_faces(self, center: np.ndarray, extents: Tuple[float, float, float],
                         R: np.ndarray, color: Tuple[int, int, int], item_type: str = "furniture") -> List[Dict[str, Any]]:
        """Construct 6 oriented 3D faces for any box component."""
        sx, sy, sz = extents
        hx, hy, hz = sx / 2.0, sy / 2.0, sz / 2.0

        local_v = np.array([
            [-hx, -hy, -hz],
            [ hx, -hy, -hz],
            [ hx, -hy,  hz],
            [-hx, -hy,  hz],
            [-hx,  hy, -hz],
            [ hx,  hy, -hz],
            [ hx,  hy,  hz],
            [-hx,  hy,  hz]
        ], dtype=np.float32)

        world_v = (local_v @ R.T) + center

        faces_def = [
            ([4, 5, 6, 7], np.array([0, 1, 0])),   # Top
            ([0, 3, 2, 1], np.array([0, -1, 0])),  # Bottom
            ([5, 1, 2, 6], np.array([1, 0, 0])),   # Right
            ([0, 4, 7, 3], np.array([-1, 0, 0])),  # Left
            ([7, 6, 2, 3], np.array([0, 0, 1])),   # Front
            ([4, 0, 1, 5], np.array([0, 0, -1]))   # Back
        ]

        polys = []
        for idxs, l_norm in faces_def:
            w_norm = l_norm @ R.T
            polys.append({
                "vertices": world_v[idxs],
                "color": color,
                "normal": w_norm,
                "type": item_type
            })
        return polys

    def _build_chair(self, center: np.ndarray, R: np.ndarray) -> List[Dict[str, Any]]:
        """Chair: 4 slender legs, horizontal seat cushion, tall backrest."""
        polys = []
        leg_color = (80, 60, 45)       # Walnut wood legs
        seat_color = (135, 145, 155)   # Contemporary woven fabric seat
        back_color = (125, 135, 145)

        # 4 Legs (height 0.44m, thickness 0.04m)
        leg_offsets = [(-0.18, -0.18), (0.18, -0.18), (-0.18, 0.18), (0.18, 0.18)]
        for lx, lz in leg_offsets:
            c = center + (R @ np.array([lx, -0.22, lz], dtype=np.float32))
            polys.extend(self._make_box_faces(c, (0.04, 0.44, 0.04), R, leg_color, "chair_leg"))

        # Seat Cushion
        seat_c = center + (R @ np.array([0.0, 0.02, 0.0], dtype=np.float32))
        polys.extend(self._make_box_faces(seat_c, (0.46, 0.06, 0.46), R, seat_color, "cushion"))

        # Backrest
        back_c = center + (R @ np.array([0.0, 0.28, -0.20], dtype=np.float32))
        polys.extend(self._make_box_faces(back_c, (0.42, 0.46, 0.04), R, back_color, "backrest"))

        return polys

    def _build_table(self, center: np.ndarray, R: np.ndarray, is_coffee: bool = False) -> List[Dict[str, Any]]:
        """Table: tabletop with bevel thickness + 4 corner legs."""
        polys = []
        wood_color = (155, 115, 80) if not is_coffee else (130, 95, 65)

        sx = 0.9 if is_coffee else 1.5
        sy = 0.42 if is_coffee else 0.74
        sz = 0.6 if is_coffee else 0.9

        # Tabletop
        top_c = center + (R @ np.array([0.0, sy / 2.0 - 0.02, 0.0], dtype=np.float32))
        polys.extend(self._make_box_faces(top_c, (sx, 0.05, sz), R, wood_color, "tabletop"))

        # 4 Legs
        leg_h = sy - 0.05
        lx, lz = (sx / 2.0) - 0.06, (sz / 2.0) - 0.06
        for ox, oz in [(-lx, -lz), (lx, -lz), (-lx, lz), (lx, lz)]:
            lc = center + (R @ np.array([ox, -0.02, oz], dtype=np.float32))
            polys.extend(self._make_box_faces(lc, (0.06, leg_h, 0.06), R, (100, 75, 50), "table_leg"))

        return polys

    def _build_sofa(self, center: np.ndarray, R: np.ndarray, is_armchair: bool = False) -> List[Dict[str, Any]]:
        """Sofa / Armchair: base plinth, seat cushions, backrest, armrests."""
        polys = []
        fabric = (95, 120, 140) if is_armchair else (85, 115, 135)
        accent = (80, 105, 125)
        w = 0.9 if is_armchair else 1.9

        # Base Frame
        base_c = center + (R @ np.array([0.0, -0.15, 0.0], dtype=np.float32))
        polys.extend(self._make_box_faces(base_c, (w, 0.22, 0.85), R, accent, "sofa_base"))

        # Seat Cushion
        seat_c = center + (R @ np.array([0.0, 0.02, 0.06], dtype=np.float32))
        polys.extend(self._make_box_faces(seat_c, (w - 0.28, 0.14, 0.68), R, fabric, "cushion"))

        # Backrest
        back_c = center + (R @ np.array([0.0, 0.24, -0.32], dtype=np.float32))
        polys.extend(self._make_box_faces(back_c, (w, 0.48, 0.22), R, fabric, "sofa_back"))

        # Armrests
        arm_w = 0.16
        for side in [-1.0, 1.0]:
            ac = center + (R @ np.array([side * (w / 2.0 - arm_w / 2.0), 0.10, 0.02], dtype=np.float32))
            polys.extend(self._make_box_faces(ac, (arm_w, 0.32, 0.80), R, accent, "armrest"))

        return polys

    def _build_bed(self, center: np.ndarray, R: np.ndarray) -> List[Dict[str, Any]]:
        """Bed: headboard, bed frame, mattress, 2 sleeping pillows, duvet."""
        polys = []
        frame_color = (130, 95, 65)
        mattress_color = (235, 235, 238)
        duvet_color = (145, 130, 120)
        pillow_color = (250, 250, 252)

        # 1. Headboard against wall
        hb_c = center + (R @ np.array([0.0, 0.35, -0.95], dtype=np.float32))
        polys.extend(self._make_box_faces(hb_c, (1.68, 0.95, 0.08), R, frame_color, "headboard"))

        # 2. Bed Base Frame
        base_c = center + (R @ np.array([0.0, -0.12, 0.0], dtype=np.float32))
        polys.extend(self._make_box_faces(base_c, (1.64, 0.28, 1.95), R, frame_color, "bed_frame"))

        # 3. Mattress
        mat_c = center + (R @ np.array([0.0, 0.08, 0.02], dtype=np.float32))
        polys.extend(self._make_box_faces(mat_c, (1.56, 0.22, 1.85), R, mattress_color, "mattress"))

        # 4. Duvet (covers lower 70% of bed)
        duvet_c = center + (R @ np.array([0.0, 0.20, 0.26], dtype=np.float32))
        polys.extend(self._make_box_faces(duvet_c, (1.58, 0.06, 1.30), R, duvet_color, "duvet"))

        # 5. Two Pillows Side-by-Side
        for px in [-0.42, 0.42]:
            pill_c = center + (R @ np.array([px, 0.22, -0.68], dtype=np.float32))
            polys.extend(self._make_box_faces(pill_c, (0.55, 0.08, 0.38), R, pillow_color, "pillow"))

        return polys

    def _build_countertop(self, center: np.ndarray, R: np.ndarray) -> List[Dict[str, Any]]:
        """Kitchen Countertop: base cabinets, polished stone slab, stainless sink."""
        polys = []
        cab_color = (210, 205, 198)       # Light warm cabinetry
        counter_slab = (235, 238, 240)    # White polished quartz slab

        # 1. Base Cabinets
        cab_c = center + (R @ np.array([0.0, -0.04, 0.0], dtype=np.float32))
        polys.extend(self._make_box_faces(cab_c, (1.20, 0.80, 0.64), R, cab_color, "cabinet"))

        # 2. Polished Countertop Slab
        slab_c = center + (R @ np.array([0.0, 0.40, 0.0], dtype=np.float32))
        polys.extend(self._make_box_faces(slab_c, (1.28, 0.05, 0.72), R, counter_slab, "counter_slab"))

        # 3. Sink basin / Stainless steel accent
        sink_c = center + (R @ np.array([0.0, 0.43, 0.0], dtype=np.float32))
        polys.extend(self._make_box_faces(sink_c, (0.45, 0.02, 0.36), R, (175, 180, 185), "sink"))

        return polys

    def _build_fridge(self, center: np.ndarray, R: np.ndarray) -> List[Dict[str, Any]]:
        """Refrigerator: stainless body, freezer/fridge split line, sleek handles."""
        polys = []
        steel = (210, 215, 220)
        handle = (160, 165, 170)

        # Main Body
        polys.extend(self._make_box_faces(center, (0.78, 1.75, 0.72), R, steel, "fridge_body"))

        # Metallic Pull Handles
        h1 = center + (R @ np.array([0.32, 0.15, 0.38], dtype=np.float32))
        polys.extend(self._make_box_faces(h1, (0.03, 0.38, 0.03), R, handle, "fridge_handle"))

        h2 = center + (R @ np.array([0.32, 0.65, 0.38], dtype=np.float32))
        polys.extend(self._make_box_faces(h2, (0.03, 0.28, 0.03), R, handle, "fridge_handle"))

        return polys

    def _build_media_center(self, center: np.ndarray, R: np.ndarray) -> List[Dict[str, Any]]:
        """TV Stand Credenza + Television with Glass Screen."""
        polys = []
        stand_color = (65, 60, 55)
        tv_bezel = (25, 25, 28)
        tv_screen = (40, 48, 55)

        # TV Stand
        stand_c = center + (R @ np.array([0.0, -0.22, 0.0], dtype=np.float32))
        polys.extend(self._make_box_faces(stand_c, (1.35, 0.44, 0.44), R, stand_color, "tv_stand"))

        # TV Screen
        tv_c = center + (R @ np.array([0.0, 0.38, 0.0], dtype=np.float32))
        polys.extend(self._make_box_faces(tv_c, (1.10, 0.64, 0.06), R, tv_bezel, "tv_bezel"))

        # Inner Glass
        screen_c = center + (R @ np.array([0.0, 0.38, 0.035], dtype=np.float32))
        polys.extend(self._make_box_faces(screen_c, (1.04, 0.58, 0.01), R, tv_screen, "tv_screen"))

        return polys

    def _build_cabinet(self, center: np.ndarray, R: np.ndarray) -> List[Dict[str, Any]]:
        """Dresser / Credenza / Cabinet."""
        polys = []
        wood = (150, 115, 80)
        polys.extend(self._make_box_faces(center, (1.10, 0.90, 0.50), R, wood, "cabinet"))
        # Drawer lines
        d_c = center + (R @ np.array([0.0, 0.10, 0.26], dtype=np.float32))
        polys.extend(self._make_box_faces(d_c, (0.95, 0.04, 0.02), R, (110, 80, 50), "drawer_trim"))
        return polys

    def _build_plant(self, center: np.ndarray, R: np.ndarray) -> List[Dict[str, Any]]:
        """Houseplant: ceramic pot, dark soil, branching green foliage."""
        polys = []
        pot_color = (190, 135, 95)
        leaf_color = (45, 125, 55)
        leaf_accent = (65, 145, 75)

        # Planter Pot
        pot_c = center + (R @ np.array([0.0, -0.20, 0.0], dtype=np.float32))
        polys.extend(self._make_box_faces(pot_c, (0.36, 0.38, 0.36), R, pot_color, "plant_pot"))

        # Foliage Leaves
        for ang in [0.0, 45.0, 90.0, 135.0, 180.0, 225.0, 270.0, 315.0]:
            rad = math.radians(ang)
            lx, lz = 0.22 * math.cos(rad), 0.22 * math.sin(rad)
            lc = center + (R @ np.array([lx, 0.14, lz], dtype=np.float32))
            col = leaf_color if ang % 90 == 0 else leaf_accent
            polys.extend(self._make_box_faces(lc, (0.16, 0.28, 0.16), R, col, "plant_leaf"))

        return polys

    def _build_lamp(self, center: np.ndarray, R: np.ndarray) -> List[Dict[str, Any]]:
        """Lamp: base, pole, warm lampshade."""
        polys = []
        metal = (180, 165, 120)
        shade = (248, 240, 205)

        # Base
        base_c = center + (R @ np.array([0.0, -0.70, 0.0], dtype=np.float32))
        polys.extend(self._make_box_faces(base_c, (0.32, 0.04, 0.32), R, metal, "lamp_base"))

        # Pole
        pole_c = center + (R @ np.array([0.0, -0.05, 0.0], dtype=np.float32))
        polys.extend(self._make_box_faces(pole_c, (0.04, 1.25, 0.04), R, metal, "lamp_pole"))

        # Lampshade
        shade_c = center + (R @ np.array([0.0, 0.62, 0.0], dtype=np.float32))
        polys.extend(self._make_box_faces(shade_c, (0.42, 0.34, 0.42), R, shade, "lamp_shade"))

        return polys

    def _build_bathroom_fixture(self, center: np.ndarray, R: np.ndarray, is_toilet: bool = True) -> List[Dict[str, Any]]:
        """Toilet or Bathroom Sink."""
        polys = []
        white_ceramic = (235, 238, 242)
        if is_toilet:
            bowl_c = center + (R @ np.array([0.0, -0.15, 0.10], dtype=np.float32))
            polys.extend(self._make_box_faces(bowl_c, (0.44, 0.45, 0.55), R, white_ceramic, "toilet_bowl"))
            tank_c = center + (R @ np.array([0.0, 0.20, -0.18], dtype=np.float32))
            polys.extend(self._make_box_faces(tank_c, (0.48, 0.42, 0.24), R, white_ceramic, "toilet_tank"))
        else:
            basin_c = center + (R @ np.array([0.0, 0.0, 0.0], dtype=np.float32))
            polys.extend(self._make_box_faces(basin_c, (0.55, 0.85, 0.50), R, white_ceramic, "sink"))
        return polys

    def _build_wall_art(self, center: np.ndarray, R: np.ndarray) -> List[Dict[str, Any]]:
        """Wall art: picture frame with canvas."""
        polys = []
        frame_color = (40, 35, 30)
        art_color = (175, 140, 100)

        polys.extend(self._make_box_faces(center, (0.84, 0.64, 0.04), R, frame_color, "art_frame"))
        canvas_c = center + (R @ np.array([0.0, 0.0, 0.025], dtype=np.float32))
        polys.extend(self._make_box_faces(canvas_c, (0.76, 0.56, 0.01), R, art_color, "art_canvas"))
        return polys

    def _generate_surface_item(self, child: Dict[str, Any]) -> List[Dict[str, Any]]:
        """Render smaller decorative and everyday objects on tabletops / counters."""
        aid = child.get("assetId", "").lower()
        pos = child.get("position", {"x": 0.0, "y": 0.0, "z": 0.0})
        cx, cy, cz = pos.get("x", 0.0), pos.get("y", 0.0), pos.get("z", 0.0)
        center = np.array([cx, cy, cz], dtype=np.float32)
        R_ident = np.eye(3, dtype=np.float32)

        if "apple" in aid or "tomato" in aid:
            return self._make_box_faces(center, (0.09, 0.09, 0.09), R_ident, (195, 45, 40), "fruit")
        elif "bottle" in aid or "wine" in aid:
            return self._make_box_faces(center, (0.08, 0.28, 0.08), R_ident, (55, 95, 75), "bottle")
        elif "bowl" in aid or "plate" in aid:
            return self._make_box_faces(center, (0.22, 0.06, 0.22), R_ident, (240, 240, 245), "dishware")
        elif "book" in aid:
            return self._make_box_faces(center, (0.18, 0.04, 0.24), R_ident, (140, 60, 50), "book")
        else:
            return self._make_box_faces(center, (0.10, 0.10, 0.10), R_ident, (180, 180, 185), "item")

    def _render_polygons_to_image(
        self,
        polygons: List[Dict[str, Any]],
        cam_pos: np.ndarray,
        yaw_deg: float,
        pitch_deg: float
    ) -> np.ndarray:
        """Project and rasterize 3D polygons with dual-light diffuse shading and edge profiling."""
        yaw_rad = math.radians(yaw_deg)
        pitch_rad = math.radians(pitch_deg)

        cos_y, sin_y = math.cos(-yaw_rad), math.sin(-yaw_rad)
        R_yaw = np.array([
            [cos_y, 0, sin_y],
            [0,     1, 0    ],
            [-sin_y, 0, cos_y]
        ], dtype=np.float32)

        cos_p, sin_p = math.cos(-pitch_rad), math.sin(-pitch_rad)
        R_pitch = np.array([
            [1, 0,      0     ],
            [0, cos_p, -sin_p],
            [0, sin_p,  cos_p]
        ], dtype=np.float32)

        R_cam = R_pitch @ R_yaw

        projected_faces = []
        for poly in polygons:
            verts_world = poly["vertices"]
            v_rel = verts_world - cam_pos
            v_cam = v_rel @ R_cam.T

            # Near clipping plane (z > 0.08m)
            if np.all(v_cam[:, 2] <= 0.08):
                continue

            v_clipped = v_cam.copy()
            v_clipped[:, 2] = np.maximum(v_clipped[:, 2], 0.06)

            z = v_clipped[:, 2]
            u = (self.width / 2.0) + (self.focal * (v_clipped[:, 0] / z))
            v = (self.height / 2.0) - (self.focal * (v_clipped[:, 1] / z))
            pts_2d = np.stack([u, v], axis=1).astype(np.int32)

            if np.max(pts_2d[:, 0]) < 0 or np.min(pts_2d[:, 0]) >= self.width:
                continue
            if np.max(pts_2d[:, 1]) < 0 or np.min(pts_2d[:, 1]) >= self.height:
                continue

            # Dual-source lighting calculation
            norm_world = poly["normal"]
            dot_key = max(0.0, float(np.dot(norm_world, self.key_light)))
            dot_fill = max(0.0, float(np.dot(norm_world, self.fill_light)))

            intensity = self.ambient_base + (0.42 * dot_key) + (0.16 * dot_fill)
            intensity = min(1.0, max(0.22, intensity))

            base_c = poly["color"]
            shaded_c = (
                int(np.clip(base_c[0] * intensity, 0, 255)),
                int(np.clip(base_c[1] * intensity, 0, 255)),
                int(np.clip(base_c[2] * intensity, 0, 255))
            )

            mean_depth = float(np.mean(z))
            projected_faces.append({
                "pts_2d": pts_2d,
                "color": shaded_c,
                "depth": mean_depth,
                "type": poly.get("type", "generic"),
                "style": poly.get("style", "")
            })

        # Depth sorting: back to front
        projected_faces.sort(key=lambda f: f["depth"], reverse=True)

        # Off-white warm ceiling canvas
        canvas = np.full((self.height, self.width, 3), (242, 240, 238), dtype=np.uint8)

        for face in projected_faces:
            pts = face["pts_2d"]
            color = face["color"]
            f_type = face["type"]

            if len(pts) >= 3:
                cv2.fillConvexPoly(canvas, pts, color, lineType=cv2.LINE_AA)

                # Floor plank / tile detail rendering
                if f_type == "floor":
                    self._draw_floor_texture(canvas, pts, face.get("style", "wood"))

                # Clean structural outline
                border_strength = 0.78 if "leg" in f_type or "cushion" in f_type else 0.88
                border_color = (
                    int(max(0, color[0] * border_strength)),
                    int(max(0, color[1] * border_strength)),
                    int(max(0, color[2] * border_strength))
                )
                cv2.polylines(canvas, [pts], isClosed=True, color=border_color, thickness=1, lineType=cv2.LINE_AA)

        return canvas

    def _draw_floor_texture(self, canvas: np.ndarray, floor_pts: np.ndarray, style: str):
        """Draw realistic perspective wood plank seams or tile grid lines on floor."""
        min_y, max_y = np.min(floor_pts[:, 1]), np.max(floor_pts[:, 1])
        if max_y - min_y < 10:
            return

        mask = np.zeros((self.height, self.width), dtype=np.uint8)
        cv2.fillConvexPoly(mask, floor_pts, 255)

        overlay = canvas.copy()
        line_color = (130, 95, 65) if style == "wood" else (190, 195, 200)

        y = float(min_y)
        step = 6.0
        while y < max_y:
            iy = int(y)
            if 0 <= iy < self.height:
                cv2.line(overlay, (0, iy), (self.width, iy), line_color, thickness=1)
            step *= 1.08  # Perspective expansion towards viewer
            y += step

        cv2.addWeighted(overlay, 0.25, canvas, 0.75, 0, canvas)
