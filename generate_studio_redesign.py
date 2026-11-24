# Python script to generate complete redesigned index.html
import os
import shutil
from pathlib import Path

BACKUP_PATH = Path("backend/static/index.html.backup_before_complete_redesign")
TARGET_PATH = Path("backend/static/index.html")

if TARGET_PATH.exists() and not BACKUP_PATH.exists():
    shutil.copy2(TARGET_PATH, BACKUP_PATH)
    print(f"Backed up index.html to {BACKUP_PATH}")

part1_head = '''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>SKETCHSPACE AI — From Imagination To Architecture</title>
  
  <!-- Architectural Atelier Typography: Cormorant Garamond, Instrument Serif, Manrope, IBM Plex Mono -->
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,300;0,400;0,500;0,600;0,700;1,400;1,500;1,600;1,700&family=IBM+Plex+Mono:ital,wght@0,400;0,500;0,600;1,400&family=Instrument+Serif:ital@0;1&family=Manrope:wght@300;400;500;600;700;800&display=swap" rel="stylesheet">
  
  <!-- Three.js for 3D Walkthrough & Spatial Exploration -->
  <script src="https://cdnjs.cloudflare.com/ajax/libs/three.js/r128/three.min.js"></script>

  <style>
    /* ==========================================================================
       SKETCHSPACE AI — RICH ARCHITECTURAL DESIGN SYSTEM
       Palette: Deep Petrol Blue, Rich Teal, Warm Ivory, Natural Cream,
                Soft Stone, Terracotta, Burnt Orange, Saffron, Olive, Botanical Green
       ========================================================================== */
    :root {
      /* Primary Foundation */
      --bg-petrol-deep: #0a1924;
      --bg-petrol-main: #0e2230;
      --bg-petrol-surface: #142e40;
      --bg-petrol-card: #18374d;
      --bg-petrol-elevated: #1e425b;

      /* Primary Natural & Architectural Surfaces */
      --warm-ivory: #faf7f2;
      --natural-cream: #f5eee6;
      --soft-stone: #ded7cd;
      --muted-ash: #9c9284;
      --dim-charcoal: #544d44;

      /* Rich Earth & Botanical Accents */
      --rich-teal: #1b677a;
      --teal-light: #2689a1;
      --teal-glow: rgba(27, 103, 122, 0.28);
      --terracotta: #c85a38;
      --terracotta-hover: #db6a46;
      --burnt-orange: #d96b32;
      --saffron-yellow: #e5a93b;
      --botanical-green: #2d5a43;
      --muted-olive: #6b7858;
      --cobalt-accent: #2554c7;
      --deep-burgundy: #5c1d2e;
      --warm-walnut: #3d281d;

      /* Structural Borders & Shadows */
      --border-subtle: rgba(222, 215, 205, 0.12);
      --border-medium: rgba(222, 215, 205, 0.22);
      --border-accent: rgba(200, 90, 56, 0.55);
      --border-teal: rgba(27, 103, 122, 0.45);
      --shadow-sm: 0 4px 12px rgba(0, 0, 0, 0.25);
      --shadow-md: 0 10px 28px rgba(0, 0, 0, 0.35);
      --shadow-lg: 0 20px 50px rgba(0, 0, 0, 0.5);

      /* Typography Stack */
      --font-display-serif: 'Cormorant Garamond', 'Instrument Serif', Georgia, serif;
      --font-body: 'Manrope', -apple-system, BlinkMacSystemFont, sans-serif;
      --font-tech: 'IBM Plex Mono', monospace;

      /* Radii */
      --radius-2xl: 20px;
      --radius-xl: 14px;
      --radius-lg: 10px;
      --radius-md: 6px;
      --radius-sm: 4px;
      --radius-pill: 9999px;
    }

    * { box-sizing: border-box; margin: 0; padding: 0; }

    html {
      scroll-behavior: smooth;
      background-color: var(--bg-petrol-deep);
    }

    body {
      background-color: var(--bg-petrol-deep);
      color: var(--natural-cream);
      font-family: var(--font-body);
      min-height: 100vh;
      display: flex;
      flex-direction: column;
      overflow-x: hidden;
      line-height: 1.6;
      -webkit-font-smoothing: antialiased;
      -moz-osx-font-smoothing: grayscale;
    }

    ::selection {
      background: var(--terracotta);
      color: var(--warm-ivory);
    }

    /* Ambient Warm Architectural Light Fields (No Neon) */
    .ambient-light-fields {
      position: fixed;
      top: 0; left: 0; width: 100vw; height: 100vh;
      pointer-events: none;
      z-index: 0;
      overflow: hidden;
    }
    .light-glow {
      position: absolute;
      border-radius: 50%;
      filter: blur(140px);
      opacity: 0.18;
      will-change: transform;
    }
    .glow-teal {
      top: -10%; left: 15%;
      width: 60vw; height: 55vh;
      background: radial-gradient(circle, #1b677a 0%, #0e2230 70%, transparent 85%);
      animation: floatWarmLight 30s infinite alternate ease-in-out;
    }
    .glow-terracotta {
      bottom: -15%; right: 10%;
      width: 55vw; height: 60vh;
      background: radial-gradient(circle, #c85a38 0%, #3d281d 65%, transparent 85%);
      animation: floatWarmLight 36s infinite alternate ease-in-out;
      animation-delay: -12s;
    }

    @keyframes floatWarmLight {
      0% { transform: translate(0, 0) scale(1); }
      50% { transform: translate(4vw, 3vh) scale(1.06); }
      100% { transform: translate(-3vw, -4vh) scale(0.96); }
    }

    /* Architectural Subtle Grid Overlay */
    .architectural-grid-texture {
      position: fixed;
      top: 0; left: 0; width: 100vw; height: 100vh;
      pointer-events: none;
      z-index: 0;
      opacity: 0.12;
      background-image: 
        linear-gradient(to right, rgba(222, 215, 205, 0.08) 1px, transparent 1px),
        linear-gradient(to bottom, rgba(222, 215, 205, 0.08) 1px, transparent 1px);
      background-size: 60px 60px;
    }

    /* ==========================================================================
       TOP NAVIGATION BAR
       ========================================================================== */
    .studio-navbar {
      position: sticky;
      top: 0;
      z-index: 200;
      backdrop-filter: blur(20px);
      -webkit-backdrop-filter: blur(20px);
      background: rgba(10, 25, 36, 0.92);
      border-bottom: 1px solid var(--border-subtle);
      padding: 14px 48px;
      display: flex;
      align-items: center;
      justify-content: space-between;
    }

    .nav-brand {
      display: flex;
      align-items: center;
      gap: 14px;
      text-decoration: none;
      cursor: pointer;
    }
    .brand-mark {
      width: 36px;
      height: 36px;
      border-radius: var(--radius-md);
      background: linear-gradient(135deg, var(--terracotta), var(--rich-teal));
      display: flex;
      align-items: center;
      justify-content: center;
      color: var(--warm-ivory);
      box-shadow: 0 4px 14px rgba(200, 90, 56, 0.35);
    }
    .brand-title {
      font-family: var(--font-body);
      font-size: 1.05rem;
      font-weight: 700;
      letter-spacing: 0.08em;
      text-transform: uppercase;
      color: var(--warm-ivory);
    }
    .brand-sub {
      font-family: var(--font-tech);
      font-size: 0.72rem;
      letter-spacing: 0.12em;
      text-transform: uppercase;
      color: var(--soft-stone);
      opacity: 0.75;
      margin-left: 6px;
    }

    /* 3 Clean Destinations: Overview, Creative Studio, My Designs */
    .nav-destinations {
      display: flex;
      align-items: center;
      background: rgba(20, 46, 64, 0.75);
      border: 1px solid var(--border-subtle);
      border-radius: var(--radius-pill);
      padding: 4px;
      gap: 4px;
    }
    .nav-tab-btn {
      background: transparent;
      border: none;
      color: var(--soft-stone);
      font-family: var(--font-body);
      font-size: 0.88rem;
      font-weight: 600;
      padding: 8px 22px;
      border-radius: var(--radius-pill);
      cursor: pointer;
      transition: all 0.25s ease;
      display: flex;
      align-items: center;
      gap: 8px;
      text-decoration: none;
    }
    .nav-tab-btn:hover {
      color: var(--warm-ivory);
      background: rgba(255, 255, 255, 0.06);
    }
    .nav-tab-btn.active {
      background: var(--terracotta);
      color: var(--warm-ivory);
      box-shadow: 0 2px 10px rgba(200, 90, 56, 0.4);
    }

    .nav-quick-actions {
      display: flex;
      align-items: center;
      gap: 12px;
    }
    .btn-nav-action {
      background: rgba(27, 103, 122, 0.25);
      border: 1px solid var(--teal-light);
      color: var(--warm-ivory);
      font-family: var(--font-body);
      font-size: 0.82rem;
      font-weight: 600;
      padding: 8px 18px;
      border-radius: var(--radius-pill);
      cursor: pointer;
      transition: all 0.2s ease;
      display: flex;
      align-items: center;
      gap: 8px;
    }
    .btn-nav-action:hover {
      background: var(--rich-teal);
      color: var(--warm-ivory);
    }

    /* Main View Wrapper */
    main {
      position: relative;
      z-index: 10;
      flex: 1;
      width: 100%;
    }

    .app-view {
      display: none;
      width: 100%;
      min-height: calc(100vh - 70px);
    }
    .app-view.active-view {
      display: block;
      animation: fadeInView 0.35s ease forwards;
    }
    @keyframes fadeInView {
      from { opacity: 0; transform: translateY(6px); }
      to { opacity: 1; transform: translateY(0); }
    }
'''

with open("generate_studio_redesign_helper.py", "w", encoding="utf-8") as f:
    f.write(part1_head)

print("Part 1 helper written.")
