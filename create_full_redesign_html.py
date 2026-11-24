# -*- coding: utf-8 -*-
"""Full Redesign Generator for SketchSpace AI.
Creates backend/static/index.html with:
- Rich Petrol Blue, Rich Teal, Warm Ivory, Terracotta, Saffron, Olive palette
- 3 Independent Destinations: Overview, Creative Studio, My Designs (SPA router with hash support)
- Creative Studio with Drawing Workspace FIRST (Dual-Panel Desktop layout)
- Reliable Before/After Comparison (CSS clip-path slider + Side-by-Side view)
- First-Person 3D Room Experience (Mode A: Depth Walkthrough, Mode B: Procedural Room)
- Scroll-Driven Cinematic Walkthrough
- Dedicated My Designs Portfolio
"""

import sys
from pathlib import Path

OUTPUT_PATH = Path("backend/static/index.html")

print("Generating SketchSpace AI Complete Redesign...")

# We will write the file in clear modular sections
with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
    # 1. HTML Header & CSS System
    f.write('''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>SKETCHSPACE AI — From Imagination To Architecture</title>
  
  <!-- Architectural Typography: Cormorant Garamond, Instrument Serif, Manrope, IBM Plex Mono -->
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
      /* Primary Architectural Foundation */
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

    /* Main View Container */
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

    /* ==========================================================================
       VIEW 1: OVERVIEW PAGE STYLES
       ========================================================================== */
    .overview-hero-section {
      min-height: 88vh;
      display: grid;
      grid-template-columns: 1.15fr 1fr;
      align-items: center;
      gap: 56px;
      padding: 48px 64px 64px 64px;
      position: relative;
    }
    .hero-content {
      display: flex;
      flex-direction: column;
      gap: 24px;
      max-width: 680px;
    }
    .hero-pretitle {
      display: inline-flex;
      align-items: center;
      gap: 10px;
      font-family: var(--font-tech);
      font-size: 0.82rem;
      letter-spacing: 0.16em;
      text-transform: uppercase;
      color: var(--terracotta);
    }
    .hero-pretitle-line {
      width: 32px;
      height: 2px;
      background: var(--terracotta);
    }
    
    /* Signature Headline (Floating freely, never in a box) */
    .hero-signature-headline {
      font-family: var(--font-display-serif);
      font-size: clamp(3.2rem, 5.8vw, 5.6rem);
      font-weight: 400;
      line-height: 1.05;
      color: var(--warm-ivory);
      letter-spacing: -0.02em;
    }
    .hero-signature-headline span.italic-highlight {
      font-style: italic;
      color: var(--saffron-yellow);
      font-family: 'Instrument Serif', var(--font-display-serif);
    }

    .hero-subtitle {
      font-size: 1.18rem;
      color: var(--soft-stone);
      line-height: 1.68;
      max-width: 540px;
      font-weight: 300;
    }

    .hero-cta-group {
      display: flex;
      align-items: center;
      gap: 16px;
      margin-top: 12px;
    }
    .btn-hero-primary {
      background: var(--terracotta);
      border: 1px solid var(--terracotta-hover);
      color: var(--warm-ivory);
      font-family: var(--font-body);
      font-size: 1rem;
      font-weight: 600;
      padding: 14px 34px;
      border-radius: var(--radius-pill);
      cursor: pointer;
      display: flex;
      align-items: center;
      gap: 12px;
      transition: all 0.25s ease;
      box-shadow: 0 6px 20px rgba(200, 90, 56, 0.4);
      text-decoration: none;
    }
    .btn-hero-primary:hover {
      background: var(--terracotta-hover);
      transform: translateY(-2px);
      box-shadow: 0 10px 28px rgba(200, 90, 56, 0.5);
    }
    .btn-hero-secondary {
      background: rgba(20, 46, 64, 0.6);
      border: 1px solid var(--border-medium);
      color: var(--warm-ivory);
      font-family: var(--font-body);
      font-size: 1rem;
      font-weight: 600;
      padding: 14px 28px;
      border-radius: var(--radius-pill);
      cursor: pointer;
      display: flex;
      align-items: center;
      gap: 10px;
      transition: all 0.25s ease;
      text-decoration: none;
    }
    .btn-hero-secondary:hover {
      background: var(--bg-petrol-surface);
      border-color: var(--teal-light);
    }

    /* 3D Cutaway Dollhouse Container */
    .hero-3d-stage {
      width: 100%;
      height: 520px;
      position: relative;
      display: flex;
      align-items: center;
      justify-content: center;
      perspective: 1400px;
    }
    .dollhouse-3d-wrapper {
      width: 380px;
      height: 380px;
      position: relative;
      transform-style: preserve-3d;
      transform: rotateX(24deg) rotateY(-36deg);
      transition: transform 0.15s ease-out;
      cursor: grab;
    }
    .dollhouse-3d-wrapper:active {
      cursor: grabbing;
    }
    .dollhouse-3d-wrapper.auto-spin {
      animation: dollhouseSpin 42s infinite linear;
    }
    @keyframes dollhouseSpin {
      from { transform: rotateX(24deg) rotateY(0deg); }
      to { transform: rotateX(24deg) rotateY(360deg); }
    }

    /* Dollhouse Architectural Elements */
    .dollhouse-slab {
      position: absolute;
      width: 340px;
      height: 340px;
      top: 20px; left: 20px;
      background: linear-gradient(135deg, #1b384d 0%, #112837 100%);
      border: 2px solid var(--border-medium);
      border-radius: var(--radius-lg);
      transform: rotateX(90deg) translateZ(-60px);
      box-shadow: 0 40px 80px rgba(0, 0, 0, 0.65);
    }
    .dollhouse-wall-back {
      position: absolute;
      width: 340px;
      height: 180px;
      top: 20px; left: 20px;
      background: linear-gradient(to top, #142e40, #1b3a50);
      border: 1px solid var(--border-subtle);
      transform: translateZ(-170px);
      opacity: 0.95;
    }
    .dollhouse-wall-left {
      position: absolute;
      width: 340px;
      height: 180px;
      top: 20px; left: 20px;
      background: linear-gradient(to top, #112837, #18374d);
      border: 1px solid var(--border-subtle);
      transform: rotateY(90deg) translateZ(-170px);
      opacity: 0.92;
    }

    /* Miniature Architectural Furniture in Dollhouse */
    .mini-sofa {
      position: absolute;
      width: 140px; height: 50px;
      bottom: 60px; left: 40px;
      background: #c85a38;
      border-radius: 6px;
      transform: translateZ(-20px);
      box-shadow: 0 6px 14px rgba(0,0,0,0.5);
    }
    .mini-table {
      position: absolute;
      width: 70px; height: 40px;
      bottom: 80px; left: 110px;
      background: #faf7f2;
      border-radius: 4px;
      transform: translateZ(-10px);
    }
    .mini-bed {
      position: absolute;
      width: 110px; height: 130px;
      top: 40px; right: 40px;
      background: #2689a1;
      border-radius: 6px;
      transform: translateZ(-30px);
    }
    .mini-plant {
      position: absolute;
      width: 24px; height: 24px;
      top: 40px; left: 40px;
      background: #2d5a43;
      border-radius: 50%;
      transform: translateZ(-15px);
    }

    /* Dollhouse Interactive Room Badges */
    .room-badge-node {
      position: absolute;
      background: rgba(14, 34, 48, 0.95);
      border: 1px solid var(--border-medium);
      color: var(--warm-ivory);
      font-family: var(--font-tech);
      font-size: 0.72rem;
      letter-spacing: 0.08em;
      text-transform: uppercase;
      padding: 5px 12px;
      border-radius: var(--radius-pill);
      display: flex;
      align-items: center;
      gap: 6px;
      box-shadow: 0 6px 16px rgba(0,0,0,0.4);
      pointer-events: auto;
      cursor: pointer;
      transition: all 0.2s ease;
    }
    .room-badge-node:hover {
      background: var(--terracotta);
      border-color: var(--terracotta-hover);
      transform: scale(1.08);
    }
    .room-badge-node::before {
      content: '';
      width: 6px; height: 6px;
      border-radius: 50%;
      background: var(--saffron-yellow);
    }
    .badge-living { top: 15%; left: 5%; }
    .badge-bedroom { top: 15%; right: 5%; }
    .badge-kitchen { bottom: 15%; left: 10%; }
    .badge-bathroom { bottom: 15%; right: 10%; }

    .dollhouse-controls-bar {
      position: absolute;
      bottom: 12px;
      display: flex;
      align-items: center;
      gap: 10px;
      background: rgba(14, 34, 48, 0.85);
      backdrop-filter: blur(12px);
      border: 1px solid var(--border-subtle);
      border-radius: var(--radius-pill);
      padding: 6px 16px;
    }
    .btn-dollhouse-control {
      background: transparent;
      border: none;
      color: var(--soft-stone);
      font-family: var(--font-tech);
      font-size: 0.75rem;
      cursor: pointer;
      display: flex;
      align-items: center;
      gap: 6px;
    }
    .btn-dollhouse-control:hover { color: var(--warm-ivory); }

    /* Editorial Showcase Gallery (Section 2) */
    .overview-showcase-section {
      padding: 96px 64px;
      display: flex;
      flex-direction: column;
      gap: 48px;
      border-top: 1px solid var(--border-subtle);
    }
    .section-header-block {
      display: flex;
      flex-direction: column;
      gap: 12px;
      max-width: 650px;
    }
    .section-tag {
      font-family: var(--font-tech);
      font-size: 0.78rem;
      letter-spacing: 0.16em;
      text-transform: uppercase;
      color: var(--rich-teal);
    }
    .section-heading-serif {
      font-family: var(--font-display-serif);
      font-size: clamp(2.2rem, 3.8vw, 3.4rem);
      font-weight: 400;
      line-height: 1.15;
      color: var(--warm-ivory);
    }
    .section-description {
      font-size: 1.05rem;
      color: var(--soft-stone);
      line-height: 1.6;
    }

    .editorial-gallery-grid {
      display: grid;
      grid-template-columns: repeat(12, 1fr);
      gap: 28px;
    }
    .gallery-tile {
      position: relative;
      border-radius: var(--radius-xl);
      overflow: hidden;
      border: 1px solid var(--border-subtle);
      background: var(--bg-petrol-surface);
      box-shadow: var(--shadow-md);
      transition: all 0.35s ease;
      cursor: pointer;
    }
    .gallery-tile:hover {
      transform: translateY(-4px);
      border-color: var(--border-medium);
      box-shadow: var(--shadow-lg);
    }
    .tile-span-7 { grid-column: span 7; aspect-ratio: 16/10; }
    .tile-span-5 { grid-column: span 5; aspect-ratio: 16/10; }
    .tile-span-4 { grid-column: span 4; aspect-ratio: 4/3; }

    .gallery-tile img {
      width: 100%; height: 100%;
      object-fit: cover;
      display: block;
      transition: transform 0.5s ease;
    }
    .gallery-tile:hover img {
      transform: scale(1.03);
    }
    .tile-caption-overlay {
      position: absolute;
      bottom: 0; left: 0; width: 100%;
      padding: 24px;
      background: linear-gradient(to top, rgba(10, 25, 36, 0.95), transparent);
      display: flex;
      justify-content: space-between;
      align-items: flex-end;
    }
    .tile-title {
      font-family: var(--font-display-serif);
      font-size: 1.35rem;
      color: var(--warm-ivory);
    }
    .tile-meta {
      font-family: var(--font-tech);
      font-size: 0.72rem;
      color: var(--soft-stone);
      letter-spacing: 0.1em;
      text-transform: uppercase;
    }

    /* Workflow Storytelling Section (Section 3) */
    .overview-workflow-section {
      padding: 96px 64px;
      display: flex;
      flex-direction: column;
      gap: 48px;
      background: rgba(14, 34, 48, 0.5);
      border-top: 1px solid var(--border-subtle);
    }
    .workflow-steps-grid {
      display: grid;
      grid-template-columns: repeat(4, 1fr);
      gap: 24px;
    }
    .workflow-step-card {
      background: var(--bg-petrol-surface);
      border: 1px solid var(--border-subtle);
      border-radius: var(--radius-xl);
      padding: 32px 24px;
      display: flex;
      flex-direction: column;
      gap: 16px;
      position: relative;
    }
    .step-number {
      font-family: var(--font-tech);
      font-size: 0.82rem;
      letter-spacing: 0.16em;
      color: var(--terracotta);
      font-weight: 600;
    }
    .step-title {
      font-family: var(--font-display-serif);
      font-size: 1.45rem;
      color: var(--warm-ivory);
      line-height: 1.25;
    }
    .step-desc {
      font-size: 0.92rem;
      color: var(--soft-stone);
      line-height: 1.6;
    }

    /* Single Discreet Technology Section (Part 6) */
    .discreet-tech-section {
      padding: 72px 64px;
      border-top: 1px solid var(--border-subtle);
      border-bottom: 1px solid var(--border-subtle);
      display: grid;
      grid-template-columns: 1fr 1.6fr;
      gap: 48px;
      align-items: center;
      background: rgba(10, 25, 36, 0.7);
    }
    .tech-badges-row {
      display: flex;
      flex-wrap: wrap;
      gap: 10px;
      margin-top: 16px;
    }
    .tech-pill {
      background: rgba(20, 46, 64, 0.7);
      border: 1px solid var(--border-subtle);
      color: var(--soft-stone);
      font-family: var(--font-tech);
      font-size: 0.75rem;
      padding: 6px 14px;
      border-radius: var(--radius-pill);
    }

    /* Final CTA Section */
    .overview-cta-section {
      padding: 110px 64px;
      display: flex;
      flex-direction: column;
      align-items: center;
      text-align: center;
      gap: 28px;
    }
    .cta-heading {
      font-family: var(--font-display-serif);
      font-size: clamp(2.8rem, 4.5vw, 4.2rem);
      font-weight: 400;
      color: var(--warm-ivory);
      line-height: 1.15;
    }

    /* ==========================================================================
       VIEW 2: CREATIVE STUDIO (DRAWING WORKSPACE FIRST!)
       ========================================================================== */
    .studio-view-container {
      padding: 24px 48px 64px 48px;
      display: flex;
      flex-direction: column;
      gap: 48px;
    }

    /* Dual-Panel Studio Workspace Grid */
    .studio-dual-panel-grid {
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 32px;
      align-items: start;
      min-height: calc(100vh - 140px);
    }

    /* Left Panel: Architectural Sketch Studio */
    .sketch-studio-panel {
      background: var(--bg-petrol-surface);
      border: 1px solid var(--border-subtle);
      border-radius: var(--radius-2xl);
      padding: 28px;
      display: flex;
      flex-direction: column;
      gap: 20px;
      box-shadow: var(--shadow-md);
    }
    .studio-panel-header {
      display: flex;
      align-items: center;
      justify-content: space-between;
      border-bottom: 1px solid var(--border-subtle);
      padding-bottom: 16px;
    }
    .panel-header-title {
      display: flex;
      align-items: center;
      gap: 12px;
    }
    .panel-icon-badge {
      width: 32px; height: 32px;
      border-radius: var(--radius-md);
      background: rgba(200, 90, 56, 0.2);
      color: var(--terracotta);
      display: flex;
      align-items: center;
      justify-content: center;
    }
    .panel-heading {
      font-family: var(--font-display-serif);
      font-size: 1.45rem;
      color: var(--warm-ivory);
    }

    /* Toolbar Dock */
    .sketch-toolbar-dock {
      display: flex;
      align-items: center;
      justify-content: space-between;
      background: var(--bg-petrol-card);
      border: 1px solid var(--border-subtle);
      border-radius: var(--radius-xl);
      padding: 8px 12px;
      gap: 8px;
      flex-wrap: wrap;
    }
    .tool-btn-group {
      display: flex;
      align-items: center;
      gap: 6px;
    }
    .btn-sketch-tool {
      width: 36px; height: 36px;
      border-radius: var(--radius-md);
      background: transparent;
      border: 1px solid transparent;
      color: var(--soft-stone);
      cursor: pointer;
      display: flex;
      align-items: center;
      justify-content: center;
      transition: all 0.2s ease;
    }
    .btn-sketch-tool:hover {
      background: rgba(255, 255, 255, 0.08);
      color: var(--warm-ivory);
    }
    .btn-sketch-tool.active {
      background: var(--terracotta);
      color: var(--warm-ivory);
      border-color: var(--terracotta-hover);
      box-shadow: 0 2px 8px rgba(200, 90, 56, 0.4);
    }

    /* Stroke Size Slider */
    .brush-size-control {
      display: flex;
      align-items: center;
      gap: 8px;
      font-family: var(--font-tech);
      font-size: 0.75rem;
      color: var(--soft-stone);
    }
    .slider-stroke {
      width: 80px;
      accent-color: var(--terracotta);
      cursor: pointer;
    }

    /* Architectural Ink Swatches */
    .ink-swatches-group {
      display: flex;
      align-items: center;
      gap: 8px;
    }
    .swatch-btn {
      width: 22px; height: 22px;
      border-radius: 50%;
      border: 2px solid transparent;
      cursor: pointer;
      transition: all 0.2s ease;
    }
    .swatch-btn.active {
      border-color: var(--warm-ivory);
      transform: scale(1.15);
      box-shadow: 0 0 8px rgba(255, 255, 255, 0.4);
    }
    .swatch-charcoal { background: #1a1715; }
    .swatch-white { background: #faf7f2; }
    .swatch-terracotta { background: #c85a38; }
    .swatch-teal { background: #1b677a; }
    .swatch-olive { background: #6b7858; }

    /* Canvas Viewport */
    .drawing-canvas-viewport {
      position: relative;
      width: 100%;
      max-width: 512px;
      aspect-ratio: 1/1;
      margin: 0 auto;
      border-radius: var(--radius-xl);
      overflow: hidden;
      border: 1px solid var(--border-medium);
      background: #112636;
      box-shadow: var(--shadow-sm);
    }
    #drawing-canvas {
      position: absolute;
      top: 0; left: 0;
      width: 100%; height: 100%;
      cursor: crosshair;
      z-index: 2;
    }
    #grid-canvas {
      position: absolute;
      top: 0; left: 0;
      width: 100%; height: 100%;
      pointer-events: none;
      z-index: 1;
      opacity: 0.35;
    }

    /* Layout Preset Chips Deck */
    .preset-chips-deck {
      display: flex;
      align-items: center;
      gap: 8px;
      overflow-x: auto;
      padding: 4px 0;
    }
    .preset-chip-btn {
      background: var(--bg-petrol-card);
      border: 1px solid var(--border-subtle);
      color: var(--soft-stone);
      font-family: var(--font-body);
      font-size: 0.8rem;
      font-weight: 500;
      padding: 6px 14px;
      border-radius: var(--radius-pill);
      cursor: pointer;
      white-space: nowrap;
      transition: all 0.2s ease;
      display: flex;
      align-items: center;
      gap: 6px;
    }
    .preset-chip-btn:hover {
      background: var(--bg-petrol-elevated);
      color: var(--warm-ivory);
      border-color: var(--teal-light);
    }

    /* Synthesis Settings Controls */
    .synthesis-params-box {
      display: flex;
      flex-direction: column;
      gap: 14px;
      background: var(--bg-petrol-card);
      border: 1px solid var(--border-subtle);
      border-radius: var(--radius-xl);
      padding: 16px;
    }
    .params-row {
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 12px;
    }
    .param-group {
      display: flex;
      flex-direction: column;
      gap: 6px;
    }
    .param-label {
      font-family: var(--font-tech);
      font-size: 0.72rem;
      letter-spacing: 0.1em;
      text-transform: uppercase;
      color: var(--soft-stone);
    }
    .param-select, .param-input {
      background: var(--bg-petrol-surface);
      border: 1px solid var(--border-subtle);
      color: var(--warm-ivory);
      font-family: var(--font-body);
      font-size: 0.85rem;
      padding: 8px 12px;
      border-radius: var(--radius-md);
      outline: none;
    }
    .param-select:focus, .param-input:focus {
      border-color: var(--terracotta);
    }

    /* Master Action Button */
    .btn-synthesize-master {
      background: linear-gradient(135deg, var(--terracotta), var(--burnt-orange));
      border: 1px solid var(--terracotta-hover);
      color: var(--warm-ivory);
      font-family: var(--font-body);
      font-size: 1.05rem;
      font-weight: 700;
      padding: 16px;
      border-radius: var(--radius-xl);
      cursor: pointer;
      display: flex;
      align-items: center;
      justify-content: center;
      gap: 12px;
      transition: all 0.25s ease;
      box-shadow: 0 8px 24px rgba(200, 90, 56, 0.45);
    }
    .btn-synthesize-master:hover {
      transform: translateY(-2px);
      box-shadow: 0 12px 32px rgba(200, 90, 56, 0.6);
    }
    .btn-synthesize-master:disabled {
      opacity: 0.6;
      cursor: not-allowed;
      transform: none;
    }

    /* Right Panel: Synthesized Interior Viewport */
    .interior-viewport-panel {
      background: var(--bg-petrol-surface);
      border: 1px solid var(--border-subtle);
      border-radius: var(--radius-2xl);
      padding: 28px;
      display: flex;
      flex-direction: column;
      gap: 20px;
      box-shadow: var(--shadow-md);
    }

    /* View Mode Tabs in Viewport */
    .viewport-mode-tabs {
      display: flex;
      align-items: center;
      background: var(--bg-petrol-card);
      border: 1px solid var(--border-subtle);
      border-radius: var(--radius-pill);
      padding: 3px;
      gap: 3px;
    }
    .mode-tab-btn {
      background: transparent;
      border: none;
      color: var(--soft-stone);
      font-family: var(--font-body);
      font-size: 0.82rem;
      font-weight: 600;
      padding: 6px 16px;
      border-radius: var(--radius-pill);
      cursor: pointer;
      transition: all 0.2s ease;
    }
    .mode-tab-btn:hover { color: var(--warm-ivory); }
    .mode-tab-btn.active {
      background: var(--terracotta);
      color: var(--warm-ivory);
    }

    /* Viewport Display Stage */
    .viewport-stage-box {
      position: relative;
      width: 100%;
      max-width: 512px;
      aspect-ratio: 1/1;
      margin: 0 auto;
      border-radius: var(--radius-xl);
      overflow: hidden;
      border: 1px solid var(--border-medium);
      background: #0d202d;
      box-shadow: var(--shadow-sm);
    }
    .stage-layer {
      position: absolute;
      top: 0; left: 0;
      width: 100%; height: 100%;
    }

    /* Empty Placeholder HUD */
    .viewport-empty-hud {
      position: absolute;
      top: 0; left: 0; width: 100%; height: 100%;
      display: flex;
      flex-direction: column;
      align-items: center;
      justify-content: center;
      gap: 16px;
      padding: 32px;
      text-align: center;
      color: var(--soft-stone);
    }
    .empty-hud-icon {
      width: 64px; height: 64px;
      border-radius: 50%;
      background: rgba(27, 103, 122, 0.2);
      color: var(--teal-light);
      display: flex;
      align-items: center;
      justify-content: center;
    }

    /* Single Interior Image */
    #stage-single-image {
      display: none;
      width: 100%; height: 100%;
      object-fit: cover;
    }

    /* ==========================================================================
       PART 5 FIX: RELIABLE BEFORE / AFTER COMPARISON VIEW
       Uses CSS clip-path inset so both images have identical layout & aspect-ratio.
       Zero width math, zero black blanks, flawless mouse & touch dragging!
       ========================================================================== */
    .spatial-compare-wrapper {
      display: none;
      position: relative;
      width: 100%; height: 100%;
      overflow: hidden;
      user-select: none;
      touch-action: none;
    }
    .compare-img-bottom {
      position: absolute;
      top: 0; left: 0;
      width: 100%; height: 100%;
      object-fit: cover;
      display: block;
    }
    .compare-img-top {
      position: absolute;
      top: 0; left: 0;
      width: 100%; height: 100%;
      object-fit: cover;
      display: block;
      /* Default 50% reveal */
      clip-path: inset(0 50% 0 0);
    }
    .compare-divider-handle {
      position: absolute;
      top: 0; left: 50%;
      width: 3px; height: 100%;
      background: var(--terracotta);
      box-shadow: 0 0 12px rgba(200, 90, 56, 0.6);
      cursor: ew-resize;
      transform: translateX(-50%);
    }
    .divider-grip-pill {
      position: absolute;
      top: 50%; left: 50%;
      transform: translate(-50%, -50%);
      width: 32px; height: 32px;
      border-radius: 50%;
      background: var(--terracotta);
      border: 2px solid var(--warm-ivory);
      color: var(--warm-ivory);
      display: flex;
      align-items: center;
      justify-content: center;
      box-shadow: 0 4px 12px rgba(0, 0, 0, 0.5);
    }

    /* Side-by-Side Comparison Container */
    .spatial-side-by-side-wrapper {
      display: none;
      grid-template-columns: 1fr 1fr;
      width: 100%; height: 100%;
      gap: 2px;
      background: var(--border-medium);
    }
    .side-by-side-cell {
      position: relative;
      width: 100%; height: 100%;
      overflow: hidden;
      background: #0d202d;
    }
    .side-by-side-cell img {
      width: 100%; height: 100%;
      object-fit: cover;
      display: block;
    }
    .side-cell-label {
      position: absolute;
      bottom: 8px; left: 8px;
      background: rgba(10, 25, 36, 0.85);
      border: 1px solid var(--border-subtle);
      color: var(--warm-ivory);
      font-family: var(--font-tech);
      font-size: 0.68rem;
      padding: 3px 8px;
      border-radius: 4px;
      text-transform: uppercase;
    }

    /* Loading / Synthesis Overlay */
    .stage-loading-overlay {
      display: none;
      position: absolute;
      top: 0; left: 0; width: 100%; height: 100%;
      background: rgba(10, 25, 36, 0.88);
      backdrop-filter: blur(8px);
      flex-direction: column;
      align-items: center;
      justify-content: center;
      gap: 20px;
      z-index: 10;
    }
    .spinning-gyro-loader {
      width: 56px; height: 56px;
      border: 3px solid rgba(222, 215, 205, 0.15);
      border-top-color: var(--terracotta);
      border-right-color: var(--rich-teal);
      border-radius: 50%;
      animation: spinGyro 1s linear infinite;
    }
    @keyframes spinGyro {
      to { transform: rotate(360deg); }
    }
    .loading-step-msg {
      font-family: var(--font-display-serif);
      font-size: 1.25rem;
      color: var(--warm-ivory);
    }
    .loading-timer-badge {
      font-family: var(--font-tech);
      font-size: 0.78rem;
      color: var(--soft-stone);
      background: rgba(20, 46, 64, 0.7);
      padding: 4px 12px;
      border-radius: var(--radius-pill);
    }

    /* Viewport Action Controls */
    .viewport-actions-bar {
      display: flex;
      align-items: center;
      justify-content: space-between;
      gap: 12px;
      flex-wrap: wrap;
    }
    .btn-viewport-action {
      background: var(--bg-petrol-card);
      border: 1px solid var(--border-subtle);
      color: var(--soft-stone);
      font-family: var(--font-body);
      font-size: 0.82rem;
      font-weight: 600;
      padding: 8px 16px;
      border-radius: var(--radius-pill);
      cursor: pointer;
      display: flex;
      align-items: center;
      gap: 8px;
      transition: all 0.2s ease;
    }
    .btn-viewport-action:hover {
      background: var(--bg-petrol-elevated);
      color: var(--warm-ivory);
      border-color: var(--border-medium);
    }
    .btn-viewport-action.highlight-3d {
      background: rgba(27, 103, 122, 0.25);
      border-color: var(--teal-light);
      color: var(--warm-ivory);
    }
    .btn-viewport-action.highlight-3d:hover {
      background: var(--rich-teal);
    }

    /* ==========================================================================
       PART 8 & 9: FIRST-PERSON 3D ROOM EXPERIENCE & SCROLL WALKTHROUGH
       ========================================================================== */
    .spatial-3d-experience-section {
      background: var(--bg-petrol-surface);
      border: 1px solid var(--border-subtle);
      border-radius: var(--radius-2xl);
      padding: 36px;
      display: flex;
      flex-direction: column;
      gap: 28px;
      box-shadow: var(--shadow-md);
      margin-top: 12px;
    }
    .experience-header-row {
      display: flex;
      align-items: center;
      justify-content: space-between;
      border-bottom: 1px solid var(--border-subtle);
      padding-bottom: 20px;
      flex-wrap: wrap;
      gap: 16px;
    }
    .experience-title-block h3 {
      font-family: var(--font-display-serif);
      font-size: 1.85rem;
      color: var(--warm-ivory);
    }
    .experience-title-block p {
      font-size: 0.92rem;
      color: var(--soft-stone);
    }

    /* 3D Mode Selector: Mode A vs Mode B */
    .spatial-mode-switch-dock {
      display: flex;
      align-items: center;
      background: var(--bg-petrol-card);
      border: 1px solid var(--border-subtle);
      border-radius: var(--radius-pill);
      padding: 4px;
      gap: 4px;
    }
    .spatial-mode-pill {
      background: transparent;
      border: none;
      color: var(--soft-stone);
      font-family: var(--font-body);
      font-size: 0.85rem;
      font-weight: 600;
      padding: 8px 18px;
      border-radius: var(--radius-pill);
      cursor: pointer;
      transition: all 0.2s ease;
      display: flex;
      align-items: center;
      gap: 8px;
    }
    .spatial-mode-pill.active {
      background: var(--terracotta);
      color: var(--warm-ivory);
    }

    /* Three.js 3D Viewport Stage */
    .spatial-canvas-stage {
      position: relative;
      width: 100%;
      height: 580px;
      border-radius: var(--radius-xl);
      overflow: hidden;
      border: 1px solid var(--border-medium);
      background: #07131b;
      box-shadow: inset 0 0 40px rgba(0, 0, 0, 0.6);
    }
    #three-spatial-canvas {
      width: 100%; height: 100%;
      display: block;
    }

    /* In-Canvas 3D HUD & Controls */
    .spatial-hud-overlay {
      position: absolute;
      top: 16px; left: 16px;
      display: flex;
      flex-direction: column;
      gap: 8px;
      pointer-events: none;
    }
    .hud-chip {
      background: rgba(10, 25, 36, 0.85);
      backdrop-filter: blur(8px);
      border: 1px solid var(--border-subtle);
      color: var(--warm-ivory);
      font-family: var(--font-tech);
      font-size: 0.75rem;
      padding: 6px 14px;
      border-radius: var(--radius-pill);
      pointer-events: auto;
    }
    .hud-disclaimer {
      color: var(--saffron-yellow);
      font-size: 0.72rem;
    }

    /* First-Person Navigation Touch D-Pad */
    .dpad-touch-controls {
      position: absolute;
      bottom: 20px; right: 20px;
      display: grid;
      grid-template-columns: repeat(3, 40px);
      grid-template-rows: repeat(3, 40px);
      gap: 4px;
      background: rgba(10, 25, 36, 0.85);
      backdrop-filter: blur(10px);
      border: 1px solid var(--border-subtle);
      border-radius: var(--radius-xl);
      padding: 6px;
    }
    .dpad-btn {
      background: rgba(20, 46, 64, 0.7);
      border: 1px solid var(--border-subtle);
      border-radius: var(--radius-md);
      color: var(--warm-ivory);
      cursor: pointer;
      display: flex;
      align-items: center;
      justify-content: center;
      transition: background 0.15s ease;
    }
    .dpad-btn:active {
      background: var(--terracotta);
    }
    .dpad-up { grid-column: 2; grid-row: 1; }
    .dpad-left { grid-column: 1; grid-row: 2; }
    .dpad-center { grid-column: 2; grid-row: 2; font-size: 0.65rem; color: var(--soft-stone); }
    .dpad-right { grid-column: 3; grid-row: 2; }
    .dpad-down { grid-column: 2; grid-row: 3; }

    /* Floating Camera Presets Bar in 3D Viewport */
    .camera-presets-bar {
      position: absolute;
      bottom: 20px; left: 20px;
      display: flex;
      align-items: center;
      gap: 8px;
      background: rgba(10, 25, 36, 0.85);
      backdrop-filter: blur(10px);
      border: 1px solid var(--border-subtle);
      border-radius: var(--radius-pill);
      padding: 6px 12px;
    }
    .btn-camera-preset {
      background: transparent;
      border: none;
      color: var(--soft-stone);
      font-family: var(--font-tech);
      font-size: 0.72rem;
      padding: 4px 10px;
      border-radius: var(--radius-pill);
      cursor: pointer;
      transition: all 0.2s ease;
    }
    .btn-camera-preset:hover { color: var(--warm-ivory); }
    .btn-camera-preset.active {
      background: var(--terracotta);
      color: var(--warm-ivory);
    }

    /* Scroll-Driven Cinematic Walkthrough Stages */
    .scroll-cinematic-track {
      display: flex;
      flex-direction: column;
      gap: 20px;
      margin-top: 16px;
    }
    .walkthrough-stage-card {
      background: var(--bg-petrol-card);
      border: 1px solid var(--border-subtle);
      border-radius: var(--radius-xl);
      padding: 20px 24px;
      display: flex;
      align-items: center;
      justify-content: space-between;
      gap: 20px;
    }
    .stage-card-info h5 {
      font-family: var(--font-display-serif);
      font-size: 1.25rem;
      color: var(--warm-ivory);
    }
    .stage-card-info p {
      font-size: 0.88rem;
      color: var(--soft-stone);
    }

    /* ==========================================================================
       VIEW 3: MY DESIGNS ARCHITECTURAL PORTFOLIO
       ========================================================================== */
    .designs-view-container {
      padding: 48px 64px 80px 64px;
      display: flex;
      flex-direction: column;
      gap: 40px;
    }
    .designs-header-row {
      display: flex;
      align-items: flex-end;
      justify-content: space-between;
      border-bottom: 1px solid var(--border-subtle);
      padding-bottom: 24px;
      flex-wrap: wrap;
      gap: 20px;
    }
    .designs-title-block h2 {
      font-family: var(--font-display-serif);
      font-size: clamp(2.2rem, 3.8vw, 3.2rem);
      color: var(--warm-ivory);
    }
    .designs-title-block p {
      font-size: 1.05rem;
      color: var(--soft-stone);
    }

    /* Portfolio Search & Filters Bar */
    .portfolio-filters-dock {
      display: flex;
      align-items: center;
      justify-content: space-between;
      gap: 16px;
      flex-wrap: wrap;
    }
    .search-input-wrapper {
      position: relative;
      width: 320px;
    }
    .search-input-wrapper input {
      width: 100%;
      background: var(--bg-petrol-surface);
      border: 1px solid var(--border-subtle);
      color: var(--warm-ivory);
      font-family: var(--font-body);
      font-size: 0.88rem;
      padding: 10px 16px 10px 40px;
      border-radius: var(--radius-pill);
      outline: none;
    }
    .search-input-wrapper input:focus {
      border-color: var(--terracotta);
    }
    .search-icon-svg {
      position: absolute;
      top: 50%; left: 14px;
      transform: translateY(-50%);
      color: var(--soft-stone);
    }

    .portfolio-filter-chips {
      display: flex;
      align-items: center;
      gap: 8px;
    }
    .portfolio-chip {
      background: var(--bg-petrol-surface);
      border: 1px solid var(--border-subtle);
      color: var(--soft-stone);
      font-family: var(--font-body);
      font-size: 0.82rem;
      font-weight: 600;
      padding: 8px 18px;
      border-radius: var(--radius-pill);
      cursor: pointer;
      transition: all 0.2s ease;
    }
    .portfolio-chip:hover { color: var(--warm-ivory); }
    .portfolio-chip.active {
      background: var(--terracotta);
      color: var(--warm-ivory);
      border-color: var(--terracotta-hover);
    }

    /* Saved Designs Portfolio Grid */
    .saved-designs-grid {
      display: grid;
      grid-template-columns: repeat(auto-fill, minmax(320px, 1fr));
      gap: 28px;
    }
    .saved-design-card {
      background: var(--bg-petrol-surface);
      border: 1px solid var(--border-subtle);
      border-radius: var(--radius-xl);
      overflow: hidden;
      display: flex;
      flex-direction: column;
      box-shadow: var(--shadow-sm);
      transition: all 0.3s ease;
    }
    .saved-design-card:hover {
      transform: translateY(-4px);
      box-shadow: var(--shadow-lg);
      border-color: var(--border-medium);
    }
    .card-thumbnail-stage {
      position: relative;
      width: 100%;
      aspect-ratio: 4/3;
      overflow: hidden;
      background: #0d202d;
    }
    .card-thumbnail-stage img {
      width: 100%; height: 100%;
      object-fit: cover;
      display: block;
    }
    .card-sketch-hover-preview {
      position: absolute;
      top: 0; left: 0; width: 100%; height: 100%;
      object-fit: cover;
      opacity: 0;
      transition: opacity 0.35s ease;
      background: rgba(10, 25, 36, 0.9);
    }
    .card-thumbnail-stage:hover .card-sketch-hover-preview {
      opacity: 1;
    }
    .card-body {
      padding: 20px;
      display: flex;
      flex-direction: column;
      gap: 12px;
    }
    .card-title-row {
      display: flex;
      align-items: center;
      justify-content: space-between;
    }
    .card-project-title {
      font-family: var(--font-display-serif);
      font-size: 1.35rem;
      color: var(--warm-ivory);
    }
    .card-room-badge {
      background: rgba(27, 103, 122, 0.25);
      border: 1px solid var(--teal-light);
      color: var(--warm-ivory);
      font-family: var(--font-tech);
      font-size: 0.68rem;
      padding: 3px 10px;
      border-radius: var(--radius-pill);
      text-transform: uppercase;
    }
    .card-date-meta {
      font-family: var(--font-tech);
      font-size: 0.72rem;
      color: var(--soft-stone);
    }
    .card-actions-row {
      display: flex;
      align-items: center;
      gap: 8px;
      margin-top: 8px;
    }
    .btn-card-action {
      flex: 1;
      background: var(--bg-petrol-card);
      border: 1px solid var(--border-subtle);
      color: var(--warm-ivory);
      font-family: var(--font-body);
      font-size: 0.78rem;
      font-weight: 600;
      padding: 8px;
      border-radius: var(--radius-md);
      cursor: pointer;
      display: flex;
      align-items: center;
      justify-content: center;
      gap: 6px;
      transition: all 0.2s ease;
    }
    .btn-card-action:hover {
      background: var(--bg-petrol-elevated);
      border-color: var(--border-medium);
    }
    .btn-card-delete {
      width: 32px;
      background: transparent;
      border: 1px solid var(--border-subtle);
      color: var(--muted-ash);
      border-radius: var(--radius-md);
      cursor: pointer;
      display: flex;
      align-items: center;
      justify-content: center;
    }
    .btn-card-delete:hover {
      color: #ff6b6b;
      border-color: #ff6b6b;
    }

    /* Portfolio Empty State */
    .portfolio-empty-state {
      padding: 80px 20px;
      text-align: center;
      display: flex;
      flex-direction: column;
      align-items: center;
      gap: 16px;
      color: var(--soft-stone);
    }

    /* ==========================================================================
       MODALS, NOTIFICATIONS & RESPONSIVENESS
       ========================================================================== */
    .spatial-modal-overlay {
      display: none;
      position: fixed;
      top: 0; left: 0; width: 100vw; height: 100vh;
      background: rgba(10, 25, 36, 0.88);
      backdrop-filter: blur(14px);
      z-index: 1000;
      align-items: center;
      justify-content: center;
      padding: 24px;
    }
    .spatial-modal-overlay.active {
      display: flex;
    }
    .spatial-modal-box {
      background: var(--bg-petrol-surface);
      border: 1px solid var(--border-medium);
      border-radius: var(--radius-2xl);
      padding: 32px;
      width: 100%;
      max-width: 520px;
      display: flex;
      flex-direction: column;
      gap: 20px;
      box-shadow: var(--shadow-lg);
    }

    /* Fullscreen Presentation Mode Curtain */
    .fullscreen-presentation-curtain {
      display: none;
      position: fixed;
      top: 0; left: 0; width: 100vw; height: 100vh;
      background: #061118;
      z-index: 2000;
      flex-direction: column;
      padding: 32px 54px;
      gap: 24px;
    }
    .fullscreen-presentation-curtain.active {
      display: flex;
    }
    .presentation-head-row {
      display: flex;
      align-items: center;
      justify-content: space-between;
    }
    .presentation-grid-stage {
      flex: 1;
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 32px;
      align-items: center;
    }

    /* Toast Notification */
    .spatial-toast-banner {
      position: fixed;
      bottom: 24px; right: 24px;
      background: var(--bg-petrol-surface);
      border: 1px solid var(--terracotta);
      color: var(--warm-ivory);
      font-family: var(--font-body);
      font-size: 0.88rem;
      padding: 12px 24px;
      border-radius: var(--radius-pill);
      box-shadow: var(--shadow-lg);
      z-index: 3000;
      display: none;
      align-items: center;
      gap: 12px;
    }

    /* Responsive Breakdown */
    @media (max-width: 1024px) {
      .overview-hero-section {
        grid-template-columns: 1fr;
        padding: 32px 24px;
      }
      .studio-dual-panel-grid {
        grid-template-columns: 1fr;
      }
      .editorial-gallery-grid {
        grid-template-columns: 1fr;
      }
      .tile-span-7, .tile-span-5, .tile-span-4 {
        grid-column: span 12;
      }
      .workflow-steps-grid {
        grid-template-columns: 1fr 1fr;
      }
      .discreet-tech-section {
        grid-template-columns: 1fr;
      }
    }
    @media (max-width: 640px) {
      .studio-navbar {
        padding: 12px 18px;
      }
      .workflow-steps-grid {
        grid-template-columns: 1fr;
      }
      .overview-showcase-section,
      .overview-workflow-section,
      .studio-view-container,
      .designs-view-container {
        padding: 24px 16px;
      }
    }
  </style>
</head>
<body>

  <!-- Ambient Warm Lighting Fields -->
  <div class="ambient-light-fields">
    <div class="light-glow glow-teal"></div>
    <div class="light-glow glow-terracotta"></div>
  </div>

  <!-- Architectural Grid Texture -->
  <div class="architectural-grid-texture"></div>

  <!-- ==========================================================================
       TOP NAVIGATION BAR
       3 Distinct Destinations: Overview, Creative Studio, My Designs
       ========================================================================== -->
  <header class="studio-navbar">
    <div class="nav-brand" onclick="switchAppView('overview')">
      <div class="brand-mark">
        <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5">
          <path d="M3 9l9-7 9 7v11a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2z"></path>
          <polyline points="9 22 9 12 15 12 15 22"></polyline>
        </svg>
      </div>
      <div>
        <span class="brand-title">SketchSpace</span>
        <span class="brand-sub">AI ATELIER</span>
      </div>
    </div>

    <nav class="nav-destinations">
      <button class="nav-tab-btn active" id="nav-btn-overview" onclick="switchAppView('overview')">
        <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M3 9l9-7 9 7v11a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2z"></path></svg>
        Overview
      </button>
      <button class="nav-tab-btn" id="nav-btn-studio" onclick="switchAppView('studio')">
        <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M12 20h9"></path><path d="M16.5 3.5a2.121 2.121 0 0 1 3 3L7 19l-4 1 1-4L16.5 3.5z"></path></svg>
        Creative Studio
      </button>
      <button class="nav-tab-btn" id="nav-btn-designs" onclick="switchAppView('designs')">
        <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="3" y="3" width="18" height="18" rx="2" ry="2"></rect><circle cx="8.5" cy="8.5" r="1.5"></circle><polyline points="21 15 16 10 5 21"></polyline></svg>
        My Designs
      </button>
    </nav>

    <div class="nav-quick-actions">
      <button class="btn-nav-action" onclick="openFullscreenPresentation()">
        <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M8 3H5a2 2 0 0 0-2 2v3m18 0V5a2 2 0 0 0-2-2h-3m0 18h3a2 2 0 0 0 2-2v-3M3 16v3a2 2 0 0 0 2 2h3"></path></svg>
        Presentation Mode
      </button>
    </div>
  </header>

  <main>
''')

    # 2. View 1: Overview
    f.write('''
    <!-- ==========================================================================
         VIEW 1: OVERVIEW HOMEPAGE
         ========================================================================== -->
    <div id="view-overview" class="app-view active-view">
      
      <!-- Section 1: Hero -->
      <section class="overview-hero-section">
        <div class="hero-content">
          <div class="hero-pretitle">
            <span class="hero-pretitle-line"></span>
            <span>Architectural Generative AI Studio</span>
          </div>
          
          <h1 class="hero-signature-headline">
            From Imagination<br>
            <span class="italic-highlight">To Architecture.</span>
          </h1>

          <p class="hero-subtitle">
            Where ideas become extraordinary spaces. Transform rough architectural gestures, wall sketches, and furniture outlines into photorealistic residential interiors with offline local generative AI.
          </p>

          <div class="hero-cta-group">
            <button class="btn-hero-primary" onclick="switchAppView('studio')">
              <span>Enter Creative Studio</span>
              <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><line x1="5" y1="12" x2="19" y2="12"></line><polyline points="12 5 19 12 12 19"></polyline></svg>
            </button>
            <button class="btn-hero-secondary" onclick="switchAppView('designs')">
              <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="3" y="3" width="18" height="18" rx="2" ry="2"></rect><circle cx="8.5" cy="8.5" r="1.5"></circle><polyline points="21 15 16 10 5 21"></polyline></svg>
              <span>Explore My Designs</span>
            </button>
          </div>
        </div>

        <!-- 3D Cutaway Dollhouse Stage -->
        <div class="hero-3d-stage">
          <div class="dollhouse-3d-wrapper auto-spin" id="hero-dollhouse-3d">
            <!-- Travertine Floor Slab -->
            <div class="dollhouse-slab"></div>
            <!-- Walnut Back & Left Walls -->
            <div class="dollhouse-wall-back"></div>
            <div class="dollhouse-wall-left"></div>
            <!-- Miniature Furniture -->
            <div class="mini-sofa"></div>
            <div class="mini-table"></div>
            <div class="mini-bed"></div>
            <div class="mini-plant"></div>
            <!-- Interactive Room Badges -->
            <div class="room-badge-node badge-living" onclick="loadRoomPresetInStudio('living_room')">Living Room</div>
            <div class="room-badge-node badge-bedroom" onclick="loadRoomPresetInStudio('bedroom')">Bedroom</div>
            <div class="room-badge-node badge-kitchen" onclick="loadRoomPresetInStudio('kitchen')">Kitchen</div>
            <div class="room-badge-node badge-bathroom" onclick="loadRoomPresetInStudio('bathroom')">Bathroom</div>
          </div>

          <div class="dollhouse-controls-bar">
            <button class="btn-dollhouse-control" id="btn-spin-toggle" onclick="toggleDollhouseSpin()">
              <svg width="13" height="13" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polygon points="5 3 19 12 5 21 5 3"></polygon></svg>
              <span>Pause Spin</span>
            </button>
            <span style="opacity:0.3;">|</span>
            <span style="font-family:var(--font-tech); font-size:0.72rem; color:var(--soft-stone);">Drag to inspect 3D volume</span>
          </div>
        </div>
      </section>

      <!-- Section 2: Architectural Project Showcase -->
      <section class="overview-showcase-section">
        <div class="section-header-block">
          <span class="section-tag">Curated Portfolio</span>
          <h2 class="section-heading-serif">Architectural Interior Spaces</h2>
          <p class="section-description">
            High-CRI architectural photography rendered directly from freehand line blueprints using local diffusion models.
          </p>
        </div>

        <div class="editorial-gallery-grid">
          <div class="gallery-tile tile-span-7" onclick="switchAppView('studio')">
            <img src="/api/image/local_cn_living_room_1795536539194.png" alt="Contemporary Living Room" onerror="this.src='/api/sketches/example/new_living_room_sketch.png'">
            <div class="tile-caption-overlay">
              <div>
                <h4 class="tile-title">Minimalist Travertine Living Room</h4>
                <p class="tile-meta">Natural Light &bull; Warm Linen &bull; Walnut Finishes</p>
              </div>
            </div>
          </div>
          <div class="gallery-tile tile-span-5" onclick="switchAppView('studio')">
            <img src="/api/image/local_cn_bedroom_1795531503385.png" alt="Master Bedroom Sanctuary" onerror="this.src='/api/sketches/example/new_bedroom_sketch.png'">
            <div class="tile-caption-overlay">
              <div>
                <h4 class="tile-title">Master Bedroom Sanctuary</h4>
                <p class="tile-meta">White Oak &bull; Soft Wool &bull; Ambient Glow</p>
              </div>
            </div>
          </div>
          <div class="gallery-tile tile-span-4" onclick="switchAppView('studio')">
            <img src="/api/image/local_cn_bathroom_1795532521076.png" alt="Calacatta Spa Bathroom" onerror="this.src='/api/sketches/example/new_bathroom_sketch.png'">
            <div class="tile-caption-overlay">
              <div>
                <h4 class="tile-title">Calacatta Spa Bathroom</h4>
                <p class="tile-meta">Honed Marble &bull; Brass Fixtures</p>
              </div>
            </div>
          </div>
          <div class="gallery-tile tile-span-4" onclick="switchAppView('studio')">
            <img src="/api/image/local_cn_office_1795531733794.png" alt="Executive Workspace" onerror="this.src='/api/sketches/example/new_office_sketch.png'">
            <div class="tile-caption-overlay">
              <div>
                <h4 class="tile-title">Executive Creative Studio</h4>
                <p class="tile-meta">Bookshelf Architecture &bull; Minimal Desk</p>
              </div>
            </div>
          </div>
          <div class="gallery-tile tile-span-4" onclick="switchAppView('studio')">
            <img src="/api/image/local_cn_living_room_1795541707324.png" alt="Bespoke Residential Salon" onerror="this.src='/api/sketches/example/new_living_room_sketch.png'">
            <div class="tile-caption-overlay">
              <div>
                <h4 class="tile-title">Bespoke Residential Salon</h4>
                <p class="tile-meta">Floor-to-Ceiling Glazing &bull; 8K Photorealism</p>
              </div>
            </div>
          </div>
        </div>
      </section>

      <!-- Section 3: The Design Process (Storytelling) -->
      <section class="overview-workflow-section">
        <div class="section-header-block">
          <span class="section-tag">Generative Methodology</span>
          <h2 class="section-heading-serif">From Hand Gesture to Built Reality</h2>
          <p class="section-description">
            Four disciplined phases bridging conceptual sketch ideation and photographic space realization.
          </p>
        </div>

        <div class="workflow-steps-grid">
          <div class="workflow-step-card">
            <span class="step-number">PHASE 01</span>
            <h4 class="step-title">Concept Gesture</h4>
            <p class="step-desc">Draw walls, windows, and furniture footprints in our 512x512 precision architectural canvas.</p>
          </div>
          <div class="workflow-step-card">
            <span class="step-number">PHASE 02</span>
            <h4 class="step-title">Spatial Conditioning</h4>
            <p class="step-desc">ControlNet Scribble extracts vector contours and locks architectural proportions.</p>
          </div>
          <div class="workflow-step-card">
            <span class="step-number">PHASE 03</span>
            <h4 class="step-title">Material Synthesis</h4>
            <p class="step-desc">Latent diffusion denoises realistic finishes, natural sunlight directions, and high-CRI illumination.</p>
          </div>
          <div class="workflow-step-card">
            <span class="step-number">PHASE 04</span>
            <h4 class="step-title">Spatial 3D Walkthrough</h4>
            <p class="step-desc">Explore depth parallax, camera translation, and perspective movement inside the synthesized room.</p>
          </div>
        </div>
      </section>

      <!-- Section 4: Single Discreet Technology Section (Part 6) -->
      <section class="discreet-tech-section">
        <div>
          <span class="section-tag">Engineering Foundation</span>
          <h3 class="section-heading-serif" style="font-size:2rem; margin-top:8px;">Locally Powered Generative AI</h3>
        </div>
        <div>
          <p class="section-description">
            SketchSpace AI is engineered for complete independence. By pairing Stable Diffusion 1.5 with ControlNet Scribble via sequential CPU offloading and tiled VAE execution, the entire inference process runs 100% offline on your local machine with zero paid APIs, zero subscriptions, and complete data confidentiality.
          </p>
          <div class="tech-badges-row">
            <span class="tech-pill">Stable Diffusion 1.5</span>
            <span class="tech-pill">ControlNet Scribble</span>
            <span class="tech-pill">100% Offline Mode</span>
            <span class="tech-pill">Sequential CPU Offload</span>
            <span class="tech-pill">Zero Cloud Dependencies</span>
          </div>
        </div>
      </section>

      <!-- Section 5: Final Call to Action -->
      <section class="overview-cta-section">
        <h2 class="cta-heading">Ready to draft your architectural vision?</h2>
        <p class="section-description" style="max-width:540px;">
          Open the Creative Studio to draw your room, configure materials, and generate a photorealistic interior in seconds.
        </p>
        <button class="btn-hero-primary" onclick="switchAppView('studio')" style="font-size:1.1rem; padding:16px 40px;">
          <span>Launch Creative Studio</span>
          <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><line x1="5" y1="12" x2="19" y2="12"></line><polyline points="12 5 19 12 12 19"></polyline></svg>
        </button>
      </section>

    </div>
''')

    # 3. View 2: Creative Studio (Drawing Workspace FIRST!)
    f.write('''
    <!-- ==========================================================================
         VIEW 2: CREATIVE STUDIO (DRAWING WORKSPACE FIRST!)
         ========================================================================== -->
    <div id="view-studio" class="app-view">
      <div class="studio-view-container">

        <!-- DUAL-PANEL WORKSPACE: VISIBLE IMMEDIATELY WITHOUT SCROLLING PAST PROMOS -->
        <div class="studio-dual-panel-grid">
          
          <!-- LEFT PANEL: ARCHITECTURAL SKETCH STUDIO -->
          <div class="sketch-studio-panel">
            <div class="studio-panel-header">
              <div class="panel-header-title">
                <div class="panel-icon-badge">
                  <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M12 20h9"></path><path d="M16.5 3.5a2.121 2.121 0 0 1 3 3L7 19l-4 1 1-4L16.5 3.5z"></path></svg>
                </div>
                <div>
                  <h3 class="panel-heading">1. Architectural Sketch Studio</h3>
                  <p style="font-size:0.78rem; color:var(--soft-stone);">Precision blueprint &amp; spatial layout drafting</p>
                </div>
              </div>

              <!-- Canvas Quick Controls -->
              <div style="display:flex; gap:6px;">
                <button class="btn-sketch-tool" id="btn-grid-toggle" title="Toggle Blueprint Grid (G)" onclick="toggleBlueprintGrid()">
                  <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="3" y="3" width="18" height="18" rx="2" ry="2"></rect><line x1="3" y1="9" x2="21" y2="9"></line><line x1="3" y1="15" x2="21" y2="15"></line><line x1="9" y1="3" x2="9" y2="21"></line><line x1="15" y1="3" x2="15" y2="21"></line></svg>
                </button>
                <button class="btn-sketch-tool" title="Upload Custom Sketch" onclick="document.getElementById('file-upload-input').click()">
                  <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4"></path><polyline points="17 8 12 3 7 8"></polyline><line x1="12" y1="3" x2="12" y2="15"></line></svg>
                </button>
                <input type="file" id="file-upload-input" accept="image/*" style="display:none;" onchange="handleCustomSketchUpload(event)">
                <button class="btn-sketch-tool" title="Download Sketch" onclick="downloadCurrentSketch()">
                  <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4"></path><polyline points="7 10 12 15 17 10"></polyline><line x1="12" y1="15" x2="12" y2="3"></line></svg>
                </button>
              </div>
            </div>

            <!-- Toolbar Dock -->
            <div class="sketch-toolbar-dock">
              <div class="tool-btn-group">
                <button class="btn-sketch-tool active" id="tool-pencil" title="Graphite Pencil (P)" onclick="setDraftingTool('pencil')">
                  <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M17 3a2.828 2.828 0 1 1 4 4L7.5 20.5 2 22l1.5-5.5L17 3z"></path></svg>
                </button>
                <button class="btn-sketch-tool" id="tool-line" title="Straight Wall Line (L)" onclick="setDraftingTool('line')">
                  <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><line x1="5" y1="19" x2="19" y2="5"></line></svg>
                </button>
                <button class="btn-sketch-tool" id="tool-rect" title="Furniture Rectangle (R)" onclick="setDraftingTool('rect')">
                  <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="3" y="3" width="18" height="18" rx="2" ry="2"></rect></svg>
                </button>
                <button class="btn-sketch-tool" id="tool-eraser" title="Eraser (E)" onclick="setDraftingTool('eraser')">
                  <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M18 13.5L11.5 20 2 10.5 8.5 4 18 13.5z"></path><path d="M14.5 7L20 12.5"></path></svg>
                </button>
              </div>

              <!-- Stroke Size Slider -->
              <div class="brush-size-control">
                <span>Size:</span>
                <input type="range" class="slider-stroke" id="stroke-slider" min="1" max="28" value="3" oninput="updateStrokeSize(this.value)">
                <span id="stroke-val-badge">3px</span>
              </div>

              <!-- Ink Swatches -->
              <div class="ink-swatches-group">
                <button class="swatch-btn swatch-charcoal active" title="Charcoal" onclick="setInkColor('#1a1715', this)"></button>
                <button class="swatch-btn swatch-white" title="French White" onclick="setInkColor('#faf7f2', this)"></button>
                <button class="swatch-btn swatch-terracotta" title="Terracotta" onclick="setInkColor('#c85a38', this)"></button>
                <button class="swatch-btn swatch-teal" title="Rich Teal" onclick="setInkColor('#1b677a', this)"></button>
                <button class="swatch-btn swatch-olive" title="Muted Olive" onclick="setInkColor('#6b7858', this)"></button>
              </div>

              <div class="tool-btn-group">
                <button class="btn-sketch-tool" title="Undo (Ctrl+Z)" onclick="undoCanvasStroke()">
                  <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="1 4 1 10 7 10"></polyline><path d="M3.51 15a9 9 0 1 0 2.13-9.36L1 10"></path></svg>
                </button>
                <button class="btn-sketch-tool" title="Redo (Ctrl+Y)" onclick="redoCanvasStroke()">
                  <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="23 4 23 10 17 10"></polyline><path d="M20.49 15a9 9 0 1 1-2.12-9.36L23 10"></path></svg>
                </button>
                <button class="btn-sketch-tool" title="Clear Canvas" onclick="clearCanvasAll()">
                  <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="3 6 5 6 21 6"></polyline><path d="M19 6v14a2 2 0 0 1-2 2H7a2 2 0 0 1-2-2V6m3 0V4a2 2 0 0 1 2-2h4a2 2 0 0 1 2 2v2"></path></svg>
                </button>
              </div>
            </div>

            <!-- Drawing Canvas Viewport (512x512) -->
            <div class="drawing-canvas-viewport">
              <canvas id="drawing-canvas" width="512" height="512"></canvas>
              <canvas id="grid-canvas" width="512" height="512"></canvas>
            </div>

            <!-- Layout Presets Deck -->
            <div>
              <div style="font-family:var(--font-tech); font-size:0.72rem; color:var(--soft-stone); margin-bottom:6px; letter-spacing:0.08em; text-transform:uppercase;">
                Architectural Room Presets:
              </div>
              <div class="preset-chips-deck">
                <button class="preset-chip-btn" onclick="loadRoomPresetInStudio('living_room')">Living Room</button>
                <button class="preset-chip-btn" onclick="loadRoomPresetInStudio('bedroom')">Bedroom</button>
                <button class="preset-chip-btn" onclick="loadRoomPresetInStudio('kitchen')">Kitchen</button>
                <button class="preset-chip-btn" onclick="loadRoomPresetInStudio('office')">Office</button>
                <button class="preset-chip-btn" onclick="loadRoomPresetInStudio('bathroom')">Bathroom</button>
              </div>
            </div>

            <!-- Synthesis Parameters Box -->
            <div class="synthesis-params-box">
              <div class="params-row">
                <div class="param-group">
                  <label class="param-label">Room Category</label>
                  <select class="param-select" id="select-category" onchange="handleCategoryChange(this.value)">
                    <option value="living_room" selected>Living Room</option>
                    <option value="bedroom">Master Bedroom</option>
                    <option value="kitchen">Modern Kitchen</option>
                    <option value="office">Executive Office</option>
                    <option value="bathroom">Luxury Bathroom</option>
                    <option value="dining">Dining Room</option>
                  </select>
                </div>
                <div class="param-group">
                  <label class="param-label">Generative Engine</label>
                  <select class="param-select" id="select-model">
                    <option value="controlnet-local" selected>ControlNet SD 1.5 (Local Offline)</option>
                    <option value="pix2pix-exp3">Pix2Pix Exp 3 (Compound Loss)</option>
                    <option value="pix2pix-exp5">Pix2Pix Exp 5 (Perceptual Loss)</option>
                  </select>
                </div>
              </div>

              <div class="param-group">
                <label class="param-label">Architectural Prompt</label>
                <input type="text" class="param-input" id="input-prompt" value="photorealistic modern living room interior, stylish sofa, coffee table, indoor plants, natural morning sunlight from floor-to-ceiling windows, architectural digest photography, high resolution, sharp focus, 8k">
              </div>
            </div>

            <!-- Master Action Button -->
            <button class="btn-synthesize-master" id="btn-synthesize-master" onclick="executeStudioSynthesis()">
              <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2"><path d="M21 16V8a2 2 0 0 0-1-1.73l-7-4a2 2 0 0 0-2 0l-7 4A2 2 0 0 0 3 8v8a2 2 0 0 0 1 1.73l7 4a2 2 0 0 0 2 0l7-4A2 2 0 0 0 21 16z"></path><polyline points="3.27 6.96 12 12.01 20.73 6.96"></polyline><line x1="12" y1="22.08" x2="12" y2="12"></line></svg>
              <span>Synthesize Architecture</span>
            </button>
          </div>

          <!-- RIGHT PANEL: SYNTHESIZED INTERIOR VIEWPORT -->
          <div class="interior-viewport-panel">
            <div class="studio-panel-header">
              <div class="panel-header-title">
                <div class="panel-icon-badge" style="background:rgba(27,103,122,0.2); color:var(--teal-light);">
                  <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="3" y="3" width="18" height="18" rx="2" ry="2"></rect><circle cx="8.5" cy="8.5" r="1.5"></circle><polyline points="21 15 16 10 5 21"></polyline></svg>
                </div>
                <div>
                  <h3 class="panel-heading">2. Synthesized Interior Viewport</h3>
                  <p style="font-size:0.78rem; color:var(--soft-stone);">High-resolution architectural spatial render</p>
                </div>
              </div>

              <!-- Viewport Mode Tabs -->
              <div class="viewport-mode-tabs">
                <button class="mode-tab-btn active" id="tab-mode-render" onclick="switchViewportMode('render')">Render</button>
                <button class="mode-tab-btn" id="tab-mode-compare" onclick="switchViewportMode('compare')">Before / After</button>
                <button class="mode-tab-btn" id="tab-mode-sketch" onclick="switchViewportMode('sketch')">Sketch</button>
              </div>
            </div>

            <!-- Viewport Stage Box (512x512) -->
            <div class="viewport-stage-box" id="viewport-stage-box">
              
              <!-- Empty State HUD -->
              <div class="viewport-empty-hud" id="viewport-empty-hud">
                <div class="empty-hud-icon">
                  <svg width="28" height="28" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8"><rect x="3" y="3" width="18" height="18" rx="2" ry="2"></rect><circle cx="8.5" cy="8.5" r="1.5"></circle><polyline points="21 15 16 10 5 21"></polyline></svg>
                </div>
                <h4 style="font-family:var(--font-display-serif); font-size:1.35rem; color:var(--warm-ivory);">Awaiting Architectural Blueprint</h4>
                <p style="font-size:0.88rem; max-width:320px;">
                  Sketch walls and furniture on the left canvas or select a room preset, then click Synthesize Architecture.
                </p>
              </div>

              <!-- Single Image View (Mode 1) -->
              <img id="stage-single-image" class="stage-layer" alt="Synthesized Interior Render">

              <!-- Before / After Reveal Slider (Mode 2 - Fixed CSS Clip-Path) -->
              <div class="spatial-compare-wrapper" id="stage-compare-slider">
                <!-- Generated Interior Bottom Layer -->
                <img class="compare-img-bottom" id="compare-bottom-img" alt="Generated Interior">
                <!-- Original Sketch Top Layer (Revealed via Clip-Path) -->
                <img class="compare-img-top" id="compare-top-img" alt="Original Sketch">
                <!-- Draggable Divider Line -->
                <div class="compare-divider-handle" id="compare-divider-handle">
                  <div class="divider-grip-pill">
                    <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="15 18 9 12 15 6"></polyline></svg>
                    <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="9 18 15 12 9 6"></polyline></svg>
                  </div>
                </div>
              </div>

              <!-- Side-by-Side Comparison (Mode 2 Alt) -->
              <div class="spatial-side-by-side-wrapper" id="stage-side-by-side">
                <div class="side-by-side-cell">
                  <img id="sbs-sketch-img" alt="Original Sketch">
                  <span class="side-cell-label">Original Sketch</span>
                </div>
                <div class="side-by-side-cell">
                  <img id="sbs-render-img" alt="Generated Interior">
                  <span class="side-cell-label">Synthesized Interior</span>
                </div>
              </div>

              <!-- Original Sketch Inspect View (Mode 3) -->
              <img id="stage-sketch-image" class="stage-layer" style="display:none; width:100%; height:100%; object-fit:cover;" alt="Input Sketch">

              <!-- Synthesis Loading Sequence Overlay -->
              <div class="stage-loading-overlay" id="stage-loading-overlay">
                <div class="spinning-gyro-loader"></div>
                <div class="loading-step-msg" id="loading-step-text">Denoising Latent Architecture...</div>
                <div class="loading-timer-badge" id="loading-timer-badge">0.0 s</div>
              </div>
            </div>

            <!-- Viewport Actions Bar -->
            <div class="viewport-actions-bar">
              <div style="display:flex; gap:8px;">
                <button class="btn-viewport-action" id="btn-toggle-compare-mode" title="Toggle Slider vs Side-by-Side" onclick="toggleCompareModeLayout()" style="display:none;">
                  <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="2" y="3" width="20" height="18" rx="2"></rect><line x1="12" y1="3" x2="12" y2="21"></line></svg>
                  <span id="compare-layout-mode-label">Side-by-Side View</span>
                </button>
                <button class="btn-viewport-action" id="btn-download-render" onclick="downloadGeneratedInterior()">
                  <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4"></path><polyline points="7 10 12 15 17 10"></polyline><line x1="12" y1="15" x2="12" y2="3"></line></svg>
                  <span>Download Interior</span>
                </button>
                <button class="btn-viewport-action" id="btn-save-design" onclick="openSaveDesignModal()">
                  <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M19 21H5a2 2 0 0 1-2-2V5a2 2 0 0 1 2-2h11l5 5v11a2 2 0 0 1-2 2z"></path><polyline points="17 21 17 13 7 13 7 21"></polyline><polyline points="7 3 7 8 15 8"></polyline></svg>
                  <span>Save to My Designs</span>
                </button>
              </div>

              <div>
                <button class="btn-viewport-action highlight-3d" onclick="scrollToSpatial3DExperience()">
                  <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polygon points="12 2 2 7 12 12 22 7 12 2"></polygon><polyline points="2 17 12 22 22 17"></polyline><polyline points="2 12 12 17 22 12"></polyline></svg>
                  <span>Explore in 3D Walkthrough</span>
                </button>
              </div>
            </div>
          </div>
        </div>

        <!-- ==========================================================================
             PART 8: FIRST-PERSON 3D ROOM EXPERIENCE
             ========================================================================== -->
        <section class="spatial-3d-experience-section" id="section-spatial-3d-experience">
          <div class="experience-header-row">
            <div class="experience-title-block">
              <h3>First-Person Spatial 3D Experience</h3>
              <p id="spatial-mode-subtext">AI Spatial Preview — Depth-Based Walkthrough (Look around, WASD to move)</p>
            </div>

            <!-- Mode A vs Mode B Tabs -->
            <div class="spatial-mode-switch-dock">
              <button class="spatial-mode-pill active" id="tab-3d-mode-a" onclick="switch3DExperienceMode('mode-a')">
                <span>Mode A: Depth Walkthrough</span>
              </button>
              <button class="spatial-mode-pill" id="tab-3d-mode-b" onclick="switch3DExperienceMode('mode-b')">
                <span>Mode B: Procedural 3D Room</span>
              </button>
            </div>
          </div>

          <!-- Three.js 3D Viewport Stage -->
          <div class="spatial-canvas-stage" id="spatial-3d-stage-container">
            <div id="three-spatial-container" style="width:100%; height:100%;"></div>

            <!-- HUD & Controls Info Overlay -->
            <div class="spatial-hud-overlay">
              <div class="hud-chip" id="hud-chip-mode">Mode A: AI Spatial Preview</div>
              <div class="hud-chip hud-disclaimer" id="hud-chip-disclaimer">
                Depth-based 2.5D spatial estimation. Visualizes relative depth and perspective parallax from a single viewpoint.
              </div>
            </div>

            <!-- Camera Presets Bar -->
            <div class="camera-presets-bar">
              <button class="btn-camera-preset active" id="cam-preset-firstperson" onclick="setCameraPresetView('firstperson')">First Person</button>
              <button class="btn-camera-preset" id="cam-preset-isometric" onclick="setCameraPresetView('isometric')">Isometric</button>
              <button class="btn-camera-preset" id="cam-preset-top" onclick="setCameraPresetView('top')">Top View (Plan)</button>
              <button class="btn-camera-preset" id="cam-preset-reset" onclick="reset3DCameraPosition()">Reset View</button>
            </div>

            <!-- On-Screen D-Pad for Touch/Tablet Walkthrough -->
            <div class="dpad-touch-controls">
              <button class="dpad-btn dpad-up" title="Move Forward (W)" onmousedown="startKeyMove('w')" onmouseup="stopKeyMove('w')">&uarr;</button>
              <button class="dpad-btn dpad-left" title="Strafe Left (A)" onmousedown="startKeyMove('a')" onmouseup="stopKeyMove('a')">&larr;</button>
              <div class="dpad-center">MOVE</div>
              <button class="dpad-btn dpad-right" title="Strafe Right (D)" onmousedown="startKeyMove('d')" onmouseup="stopKeyMove('d')">&rarr;</button>
              <button class="dpad-btn dpad-down" title="Move Back (S)" onmousedown="startKeyMove('s')" onmouseup="stopKeyMove('s')">&darr;</button>
            </div>
          </div>

          <!-- Part 9: Scroll-Driven Cinematic Walkthrough Stages -->
          <div class="scroll-cinematic-track">
            <div class="walkthrough-stage-card">
              <div class="stage-card-info">
                <h5>Stage 1 &bull; High-Resolution Photographic Framing</h5>
                <p>The synthesized architectural interior is rendered at high resolution with true material illumination.</p>
              </div>
              <span class="tech-pill">Photorealism</span>
            </div>
            <div class="walkthrough-stage-card">
              <div class="stage-card-info">
                <h5>Stage 2 &bull; Relative Depth &amp; Topography Emergence</h5>
                <p>Architectural depth cues calculate vanishing planes, ceiling slopes, and furniture elevations.</p>
              </div>
              <span class="tech-pill">Depth Mapping</span>
            </div>
            <div class="walkthrough-stage-card">
              <div class="stage-card-info">
                <h5>Stage 3 &bull; Perspective Dolly-In Camera Transition</h5>
                <p>Camera translates smoothly forward into the interior volume without edge distortion.</p>
              </div>
              <span class="tech-pill">Spatial Dolly</span>
            </div>
            <div class="walkthrough-stage-card">
              <div class="stage-card-info">
                <h5>Stage 4 &bull; First-Person Room Exploration</h5>
                <p>Full mouse look and WASD translation allow moving through the space in real time.</p>
              </div>
              <span class="tech-pill">Interactive 3D</span>
            </div>
          </div>
        </section>

      </div>
    </div>
''')

    # 4. View 3: My Designs Architectural Portfolio
    f.write('''
    <!-- ==========================================================================
         VIEW 3: MY DESIGNS ARCHITECTURAL PORTFOLIO
         ========================================================================== -->
    <div id="view-designs" class="app-view">
      <div class="designs-view-container">

        <div class="designs-header-row">
          <div class="designs-title-block">
            <span class="section-tag">Personal Portfolio</span>
            <h2>My Architectural Designs</h2>
            <p>Your saved synthesized spaces, original blueprints, and spatial explorations.</p>
          </div>

          <button class="btn-hero-primary" onclick="switchAppView('studio')">
            <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><line x1="12" y1="5" x2="12" y2="19"></line><line x1="5" y1="12" x2="19" y2="12"></line></svg>
            <span>Create New Design</span>
          </button>
        </div>

        <!-- Portfolio Search & Filters -->
        <div class="portfolio-filters-dock">
          <div class="search-input-wrapper">
            <svg class="search-icon-svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="11" cy="11" r="8"></circle><line x1="21" y1="21" x2="16.65" y2="16.65"></line></svg>
            <input type="text" id="portfolio-search-input" placeholder="Search saved designs..." oninput="filterSavedDesignsGallery()">
          </div>

          <div class="portfolio-filter-chips">
            <button class="portfolio-chip active" onclick="setPortfolioCategoryFilter('all', this)">All Spaces</button>
            <button class="portfolio-chip" onclick="setPortfolioCategoryFilter('living_room', this)">Living Room</button>
            <button class="portfolio-chip" onclick="setPortfolioCategoryFilter('bedroom', this)">Bedroom</button>
            <button class="portfolio-chip" onclick="setPortfolioCategoryFilter('kitchen', this)">Kitchen</button>
            <button class="portfolio-chip" onclick="setPortfolioCategoryFilter('office', this)">Office</button>
            <button class="portfolio-chip" onclick="setPortfolioCategoryFilter('bathroom', this)">Bathroom</button>
          </div>
        </div>

        <!-- Saved Designs Grid -->
        <div class="saved-designs-grid" id="saved-designs-grid-container">
          <!-- Populated dynamically via JavaScript -->
        </div>

        <!-- Empty State (Shown when no designs match) -->
        <div class="portfolio-empty-state" id="portfolio-empty-state" style="display:none;">
          <svg width="48" height="48" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5"><rect x="3" y="3" width="18" height="18" rx="2" ry="2"></rect><circle cx="8.5" cy="8.5" r="1.5"></circle><polyline points="21 15 16 10 5 21"></polyline></svg>
          <h4 style="font-family:var(--font-display-serif); font-size:1.45rem; color:var(--warm-ivory);">No Saved Designs Found</h4>
          <p style="font-size:0.92rem; max-width:360px;">
            Synthesize an interior in Creative Studio and click "Save to My Designs" to build your portfolio.
          </p>
          <button class="btn-hero-primary" onclick="switchAppView('studio')" style="margin-top:12px;">
            Enter Creative Studio
          </button>
        </div>

      </div>
    </div>
''')

    # 5. Modals & Notifications
    f.write('''
    <!-- Save Design Modal -->
    <div class="spatial-modal-overlay" id="save-design-modal">
      <div class="spatial-modal-box">
        <h3 style="font-family:var(--font-display-serif); font-size:1.6rem; color:var(--warm-ivory);">Save Project to My Designs</h3>
        <p style="font-size:0.88rem; color:var(--soft-stone);">
          Add an architectural title and optional notes to catalog this interior in your personal design portfolio.
        </p>

        <div class="param-group">
          <label class="param-label">Project Title</label>
          <input type="text" class="param-input" id="save-design-title" value="Bespoke Residential Salon">
        </div>

        <div class="param-group">
          <label class="param-label">Architectural Notes</label>
          <input type="text" class="param-input" id="save-design-notes" placeholder="e.g. Calacatta gold marble, linen upholstery, morning light">
        </div>

        <div style="display:flex; justify-content:flex-end; gap:12px; margin-top:10px;">
          <button class="btn-viewport-action" onclick="closeSaveDesignModal()">Cancel</button>
          <button class="btn-hero-primary" onclick="confirmSaveCurrentDesign()" style="padding:10px 24px; font-size:0.92rem;">Save Design</button>
        </div>
      </div>
    </div>

    <!-- Fullscreen Presentation Mode Curtain -->
    <div class="fullscreen-presentation-curtain" id="fullscreen-presentation-curtain">
      <div class="presentation-head-row">
        <div>
          <h3 style="font-family:var(--font-display-serif); font-size:1.8rem; color:var(--warm-ivory);">SketchSpace AI &bull; Architectural Presentation</h3>
          <p style="font-size:0.85rem; color:var(--soft-stone);">Academic Generative AI Architecture Demonstration</p>
        </div>
        <button class="btn-viewport-action" onclick="closeFullscreenPresentation()">
          <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><line x1="18" y1="6" x2="6" y2="18"></line><line x1="6" y1="6" x2="18" y2="18"></line></svg>
          <span>Exit Presentation</span>
        </button>
      </div>

      <div class="presentation-grid-stage">
        <div style="display:flex; flex-direction:column; gap:10px; height:100%;">
          <span class="tech-pill" style="align-self:flex-start;">Input Architectural Blueprint</span>
          <div style="flex:1; border-radius:var(--radius-xl); overflow:hidden; border:1px solid var(--border-medium); background:#0a1c27;">
            <img id="pres-sketch-img" src="/api/sketches/example/new_living_room_sketch.png" style="width:100%; height:100%; object-fit:contain;" alt="Input Sketch">
          </div>
        </div>
        <div style="display:flex; flex-direction:column; gap:10px; height:100%;">
          <span class="tech-pill" style="align-self:flex-start; background:var(--terracotta); color:var(--warm-ivory);">Synthesized Photorealistic Interior</span>
          <div style="flex:1; border-radius:var(--radius-xl); overflow:hidden; border:1px solid var(--border-medium); background:#0a1c27;">
            <img id="pres-render-img" src="/api/image/local_cn_living_room_1795536539194.png" style="width:100%; height:100%; object-fit:contain;" alt="Synthesized Interior">
          </div>
        </div>
      </div>
    </div>

    <!-- Toast Notification Banner -->
    <div class="spatial-toast-banner" id="spatial-toast">
      <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M22 11.08V12a10 10 0 1 1-5.93-9.14"></path><polyline points="22 4 12 14.01 9 11.01"></polyline></svg>
      <span id="toast-message-text">Notification</span>
    </div>

  </main>
''')

    # 6. JavaScript Core Engine
    f.write('''
  <!-- ==========================================================================
       JAVASCRIPT CORE LOGIC & ENGINE
       ========================================================================== -->
  <script>
    /* Global Application State */
    const AppState = {
      activeView: 'overview',
      currentSketchUrl: '/api/sketches/example/new_living_room_sketch.png',
      currentGeneratedUrl: '/api/image/local_cn_living_room_1795536539194.png',
      currentDepthUrl: '/api/depth/local_cn_living_room_1795536539194.png',
      activeCategory: 'living_room',
      viewportMode: 'render', // 'render', 'compare', 'sketch'
      compareLayout: 'slider', // 'slider', 'side-by-side'
      compareSplitPercent: 50,
      active3DMode: 'mode-a', // 'mode-a' (depth walkthrough), 'mode-b' (procedural room)
      savedDesigns: [],
      cameraKeyMove: { w: false, a: false, s: false, d: false }
    };

    /* ==========================================================================
       ROUTING & VIEW MANAGEMENT (PART 2)
       3 Independent Destinations: Overview, Creative Studio, My Designs
       ========================================================================== */
    function switchAppView(viewKey) {
      if (!['overview', 'studio', 'designs'].includes(viewKey)) viewKey = 'overview';
      AppState.activeView = viewKey;

      // Update Nav Buttons
      document.querySelectorAll('.nav-tab-btn').forEach(b => b.classList.remove('active'));
      const activeNavBtn = document.getElementById(`nav-btn-${viewKey}`);
      if (activeNavBtn) activeNavBtn.classList.add('active');

      // Update Views
      document.querySelectorAll('.app-view').forEach(v => v.classList.remove('active-view'));
      const targetView = document.getElementById(`view-${viewKey}`);
      if (targetView) targetView.classList.add('active-view');

      // Update URL Hash
      if (window.location.hash !== `#${viewKey}`) {
        history.pushState(null, '', `#${viewKey}`);
      }

      // View-specific initializations
      if (viewKey === 'studio') {
        window.scrollTo({ top: 0, behavior: 'instant' });
        initDrawingCanvasIfNeeded();
      } else if (viewKey === 'designs') {
        renderSavedDesignsGallery();
      }
    }

    // Listen to hash changes for browser back/forward buttons
    window.addEventListener('hashchange', () => {
      const hash = window.location.hash.replace('#', '');
      if (hash) switchAppView(hash);
    });

    /* ==========================================================================
       DRAWING CANVAS WORKSPACE (PART 4)
       ========================================================================== */
    let canvas, ctx, gridCanvas, gridCtx;
    let isDrawing = false;
    let currentTool = 'pencil';
    let currentStrokeColor = '#1a1715';
    let currentStrokeWidth = 3;
    let startX = 0, startY = 0;
    let canvasSnapshot = null;
    let undoStack = [];
    let redoStack = [];
    let isCanvasInitialized = false;
    let showGrid = true;

    function initDrawingCanvasIfNeeded() {
      if (isCanvasInitialized) return;
      canvas = document.getElementById('drawing-canvas');
      if (!canvas) return;
      ctx = canvas.getContext('2d');
      gridCanvas = document.getElementById('grid-canvas');
      gridCtx = gridCanvas.getContext('2d');

      // Initialize stone background
      ctx.fillStyle = '#faf7f2';
      ctx.fillRect(0, 0, canvas.width, canvas.height);
      saveCanvasState();

      drawBlueprintGrid();

      // Mouse & Touch Listeners
      canvas.addEventListener('mousedown', startDrawing);
      canvas.addEventListener('mousemove', drawMove);
      canvas.addEventListener('mouseup', stopDrawing);
      canvas.addEventListener('mouseleave', stopDrawing);

      canvas.addEventListener('touchstart', handleTouchStart, { passive: false });
      canvas.addEventListener('touchmove', handleTouchMove, { passive: false });
      canvas.addEventListener('touchend', stopDrawing, { passive: false });

      isCanvasInitialized = true;

      // Load default sketch
      loadRoomPresetInStudio('living_room');
    }

    function getCanvasCoordinates(e) {
      const rect = canvas.getBoundingClientRect();
      const scaleX = canvas.width / rect.width;
      const scaleY = canvas.height / rect.height;
      let clientX = e.clientX;
      let clientY = e.clientY;
      if (e.touches && e.touches.length > 0) {
        clientX = e.touches[0].clientX;
        clientY = e.touches[0].clientY;
      }
      return {
        x: (clientX - rect.left) * scaleX,
        y: (clientY - rect.top) * scaleY
      };
    }

    function startDrawing(e) {
      isDrawing = true;
      const coords = getCanvasCoordinates(e);
      startX = coords.x;
      startY = coords.y;
      canvasSnapshot = ctx.getImageData(0, 0, canvas.width, canvas.height);

      ctx.beginPath();
      ctx.moveTo(startX, startY);
      ctx.strokeStyle = (currentTool === 'eraser') ? '#faf7f2' : currentStrokeColor;
      ctx.lineWidth = currentStrokeWidth;
      ctx.lineCap = 'round';
      ctx.lineJoin = 'round';
    }

    function drawMove(e) {
      if (!isDrawing) return;
      const coords = getCanvasCoordinates(e);

      if (currentTool === 'pencil' || currentTool === 'eraser') {
        ctx.lineTo(coords.x, coords.y);
        ctx.stroke();
      } else if (currentTool === 'line') {
        ctx.putImageData(canvasSnapshot, 0, 0);
        ctx.beginPath();
        ctx.moveTo(startX, startY);
        ctx.lineTo(coords.x, coords.y);
        ctx.stroke();
      } else if (currentTool === 'rect') {
        ctx.putImageData(canvasSnapshot, 0, 0);
        ctx.beginPath();
        ctx.strokeRect(startX, startY, coords.x - startX, coords.y - startY);
      }
    }

    function stopDrawing() {
      if (isDrawing) {
        isDrawing = false;
        saveCanvasState();
      }
    }

    function handleTouchStart(e) {
      e.preventDefault();
      startDrawing(e);
    }
    function handleTouchMove(e) {
      e.preventDefault();
      drawMove(e);
    }

    function setDraftingTool(tool) {
      currentTool = tool;
      document.querySelectorAll('.btn-sketch-tool').forEach(b => b.classList.remove('active'));
      const activeBtn = document.getElementById(`tool-${tool}`);
      if (activeBtn) activeBtn.classList.add('active');
    }

    function setInkColor(hex, btn) {
      currentStrokeColor = hex;
      document.querySelectorAll('.swatch-btn').forEach(b => b.classList.remove('active'));
      if (btn) btn.classList.add('active');
      if (currentTool === 'eraser') setDraftingTool('pencil');
    }

    function updateStrokeSize(val) {
      currentStrokeWidth = parseInt(val, 10);
      document.getElementById('stroke-val-badge').innerText = `${val}px`;
    }

    function saveCanvasState() {
      if (undoStack.length >= 25) undoStack.shift();
      undoStack.push(ctx.getImageData(0, 0, canvas.width, canvas.height));
      redoStack = [];
    }

    function undoCanvasStroke() {
      if (undoStack.length > 1) {
        redoStack.push(undoStack.pop());
        const previousState = undoStack[undoStack.length - 1];
        ctx.putImageData(previousState, 0, 0);
      }
    }

    function redoCanvasStroke() {
      if (redoStack.length > 0) {
        const nextState = redoStack.pop();
        undoStack.push(nextState);
        ctx.putImageData(nextState, 0, 0);
      }
    }

    function clearCanvasAll() {
      if (!confirm('Clear canvas blueprint?')) return;
      ctx.fillStyle = '#faf7f2';
      ctx.fillRect(0, 0, canvas.width, canvas.height);
      saveCanvasState();
    }

    function drawBlueprintGrid() {
      if (!gridCtx) return;
      gridCtx.clearRect(0, 0, gridCanvas.width, gridCanvas.height);
      if (!showGrid) return;
      gridCtx.strokeStyle = 'rgba(27, 103, 122, 0.35)';
      gridCtx.lineWidth = 1;
      const step = 32;
      for (let x = 0; x <= gridCanvas.width; x += step) {
        gridCtx.beginPath();
        gridCtx.moveTo(x, 0);
        gridCtx.lineTo(x, gridCanvas.height);
        gridCtx.stroke();
      }
      for (let y = 0; y <= gridCanvas.height; y += step) {
        gridCtx.beginPath();
        gridCtx.moveTo(0, y);
        gridCtx.lineTo(gridCanvas.width, y);
        gridCtx.stroke();
      }
    }

    function toggleBlueprintGrid() {
      showGrid = !showGrid;
      drawBlueprintGrid();
      document.getElementById('btn-grid-toggle').classList.toggle('active', showGrid);
    }

    function downloadCurrentSketch() {
      const link = document.createElement('a');
      link.download = `sketch_${Date.now()}.png`;
      link.href = canvas.toDataURL('image/png');
      link.click();
      showToast('Sketch blueprint downloaded');
    }

    function handleCustomSketchUpload(e) {
      const file = e.target.files[0];
      if (!file) return;
      const reader = new FileReader();
      reader.onload = (evt) => {
        const img = new Image();
        img.onload = () => {
          ctx.fillStyle = '#faf7f2';
          ctx.fillRect(0, 0, canvas.width, canvas.height);
          ctx.drawImage(img, 0, 0, canvas.width, canvas.height);
          saveCanvasState();
          showToast('Custom sketch blueprint loaded');
        };
        img.src = evt.target.result;
      };
      reader.readAsDataURL(file);
    }

    function loadRoomPresetInStudio(category) {
      switchAppView('studio');
      AppState.activeCategory = category;
      const selectCat = document.getElementById('select-category');
      if (selectCat) selectCat.value = category;

      const presetMap = {
        living_room: {
          file: '/api/sketches/example/new_living_room_sketch.png',
          prompt: 'photorealistic contemporary luxury living room interior, designer sofa, marble coffee table, indoor plants, natural morning sunlight from floor-to-ceiling windows, architectural digest photography, high resolution, sharp focus, 8k'
        },
        bedroom: {
          file: '/api/sketches/example/new_bedroom_sketch.png',
          prompt: 'photorealistic modern master bedroom interior, luxury upholstered bed, bedside lamps, floor-to-ceiling windows, natural daylight, hardwood flooring, serene ambiance, 8k'
        },
        kitchen: {
          file: '/api/sketches/example/new_kitchen_sketch.png',
          prompt: 'photorealistic contemporary kitchen interior, marble waterfall island, brass fixtures, integrated cabinetry, warm recessed ceiling lights, high resolution, 8k'
        },
        office: {
          file: '/api/sketches/example/new_office_sketch.png',
          prompt: 'photorealistic executive workspace, walnut desk, ergonomic chair, architectural bookshelf, natural window illumination, minimalist interior, 8k'
        },
        bathroom: {
          file: '/api/sketches/example/new_bathroom_sketch.png',
          prompt: 'photorealistic luxury spa bathroom interior, freestanding stone tub, Calacatta marble wall tiles, frameless glass shower enclosure, brushed brass fixtures, 8k'
        }
      };

      const preset = presetMap[category] || presetMap.living_room;
      document.getElementById('input-prompt').value = preset.prompt;

      const img = new Image();
      img.crossOrigin = 'anonymous';
      img.onload = () => {
        if (ctx) {
          ctx.fillStyle = '#faf7f2';
          ctx.fillRect(0, 0, canvas.width, canvas.height);
          ctx.drawImage(img, 0, 0, canvas.width, canvas.height);
          saveCanvasState();
        }
        AppState.currentSketchUrl = preset.file;
        showToast(`Loaded ${category.replace('_', ' ')} layout preset`);
      };
      img.src = preset.file;
    }

    function handleCategoryChange(cat) {
      loadRoomPresetInStudio(cat);
    }

    /* ==========================================================================
       SYNTHESIS PIPELINE & GENERATION REQUEST
       ========================================================================== */
    let synthesisTimerInterval = null;
    let synthesisStartTime = 0;

    async function executeStudioSynthesis() {
      const btn = document.getElementById('btn-synthesize-master');
      const overlay = document.getElementById('stage-loading-overlay');
      const timerBadge = document.getElementById('loading-timer-badge');
      const stepText = document.getElementById('loading-step-text');

      btn.disabled = true;
      overlay.style.display = 'flex';
      synthesisStartTime = Date.now();

      synthesisTimerInterval = setInterval(() => {
        const elapsed = ((Date.now() - synthesisStartTime) / 1000).toFixed(1);
        timerBadge.innerText = `${elapsed} s`;
      }, 100);

      stepText.innerText = 'Locking architectural contours...';

      // Export canvas blob
      const blob = await new Promise(resolve => canvas.toBlob(resolve, 'image/png'));
      const formData = new FormData();
      formData.append('file', blob, 'blueprint_sketch.png');

      const model = document.getElementById('select-model').value;
      const category = document.getElementById('select-category').value;
      const prompt = document.getElementById('input-prompt').value;

      const queryParams = new URLSearchParams({
        model: model,
        category: category,
        steps: '15',
        prompt: prompt
      });

      setTimeout(() => { stepText.innerText = 'Synthesizing material illumination...'; }, 1800);
      setTimeout(() => { stepText.innerText = 'Computing relative depth topography...'; }, 5000);

      try {
        const response = await fetch(`/api/generate?${queryParams.toString()}`, {
          method: 'POST',
          body: formData
        });

        if (!response.ok) {
          const errData = await response.json();
          throw new Error(errData.detail || 'Synthesis failed');
        }

        const data = await response.json();
        clearInterval(synthesisTimerInterval);
        overlay.style.display = 'none';
        btn.disabled = false;

        // Update application state
        AppState.currentGeneratedUrl = data.generated_url;
        AppState.currentSketchUrl = data.sketch_url || canvas.toDataURL('image/png');
        AppState.currentDepthUrl = data.depth_url || `/api/depth/${data.generated_filename}`;

        displaySynthesizedResult();
        showToast('Realistic interior synthesized successfully!');

        // Update 3D Walkthrough with new render & depth map
        initOrUpdateThree3DScene(AppState.currentGeneratedUrl, AppState.currentDepthUrl);

      } catch (err) {
        clearInterval(synthesisTimerInterval);
        overlay.style.display = 'none';
        btn.disabled = false;
        alert(`Synthesis error: ${err.message}`);
      }
    }

    function displaySynthesizedResult() {
      document.getElementById('viewport-empty-hud').style.display = 'none';
      const singleImg = document.getElementById('stage-single-image');
      singleImg.src = AppState.currentGeneratedUrl;
      singleImg.style.display = 'block';

      // Setup Before/After sources
      const bottomImg = document.getElementById('compare-bottom-img');
      const topImg = document.getElementById('compare-top-img');
      bottomImg.src = AppState.currentGeneratedUrl;
      topImg.src = canvas.toDataURL('image/png');

      // Setup Side-by-Side sources
      document.getElementById('sbs-render-img').src = AppState.currentGeneratedUrl;
      document.getElementById('sbs-sketch-img').src = canvas.toDataURL('image/png');

      // Setup sketch view
      document.getElementById('stage-sketch-image').src = canvas.toDataURL('image/png');

      // Switch to render view
      switchViewportMode('render');
    }

    /* ==========================================================================
       PART 5: FIXED BEFORE/AFTER VIEW WITH CLIP-PATH & SIDE-BY-SIDE
       ========================================================================== */
    let isCompareDragging = false;

    function switchViewportMode(mode) {
      AppState.viewportMode = mode;
      document.querySelectorAll('.mode-tab-btn').forEach(b => b.classList.remove('active'));
      const activeBtn = document.getElementById(`tab-mode-${mode}`);
      if (activeBtn) activeBtn.classList.add('active');

      const singleImg = document.getElementById('stage-single-image');
      const compareSlider = document.getElementById('stage-compare-slider');
      const sideBySide = document.getElementById('stage-side-by-side');
      const sketchImg = document.getElementById('stage-sketch-image');
      const toggleModeBtn = document.getElementById('btn-toggle-compare-mode');

      singleImg.style.display = 'none';
      compareSlider.style.display = 'none';
      sideBySide.style.display = 'none';
      sketchImg.style.display = 'none';
      toggleModeBtn.style.display = 'none';

      if (mode === 'render') {
        singleImg.style.display = 'block';
      } else if (mode === 'compare') {
        toggleModeBtn.style.display = 'flex';
        if (AppState.compareLayout === 'slider') {
          compareSlider.style.display = 'block';
          initCompareSliderListeners();
        } else {
          sideBySide.style.display = 'grid';
        }
      } else if (mode === 'sketch') {
        sketchImg.style.display = 'block';
      }
    }

    function toggleCompareModeLayout() {
      AppState.compareLayout = (AppState.compareLayout === 'slider') ? 'side-by-side' : 'slider';
      document.getElementById('compare-layout-mode-label').innerText =
        (AppState.compareLayout === 'slider') ? 'Side-by-Side View' : 'Reveal Slider View';
      switchViewportMode('compare');
    }

    function initCompareSliderListeners() {
      const stage = document.getElementById('viewport-stage-box');
      if (!stage) return;

      const handleMove = (clientX) => {
        const rect = stage.getBoundingClientRect();
        let posX = clientX - rect.left;
        posX = Math.max(0, Math.min(rect.width, posX));
        const percent = (posX / rect.width) * 100;
        AppState.compareSplitPercent = percent;

        // Update Clip-Path Inset & Handle Position
        const topImg = document.getElementById('compare-top-img');
        const handle = document.getElementById('compare-divider-handle');
        topImg.style.clipPath = `inset(0 ${100 - percent}% 0 0)`;
        handle.style.left = `${percent}%`;
      };

      stage.onpointerdown = (e) => {
        isCompareDragging = true;
        handleMove(e.clientX);
      };
      window.onpointermove = (e) => {
        if (isCompareDragging) handleMove(e.clientX);
      };
      window.onpointerup = () => {
        isCompareDragging = false;
      };
    }

    function downloadGeneratedInterior() {
      if (!AppState.currentGeneratedUrl) return;
      const a = document.createElement('a');
      a.href = AppState.currentGeneratedUrl;
      a.download = `interior_${Date.now()}.png`;
      a.click();
      showToast('Interior render downloaded');
    }

    /* ==========================================================================
       PART 8 & 9: THREE.JS 3D FIRST-PERSON WALKTHROUGH & PROCEDURAL ROOM
       ========================================================================== */
    let threeScene, threeCamera, threeRenderer;
    let planeMesh = null;
    let proceduralRoomGroup = null;
    let isThreeInitialized = false;
    let threeAnimFrameId = null;

    // First person camera rotation state
    let cameraYaw = 0;
    let cameraPitch = 0;
    let is3DPointerDown = false;
    let prevMouseX = 0, prevMouseY = 0;

    function initOrUpdateThree3DScene(diffuseUrl, depthUrl) {
      const container = document.getElementById('three-spatial-container');
      if (!container) return;

      if (!isThreeInitialized) {
        threeScene = new THREE.Scene();
        threeScene.background = new THREE.Color(0x07131b);

        threeCamera = new THREE.PerspectiveCamera(55, container.clientWidth / container.clientHeight, 0.1, 100);
        threeCamera.position.set(0, 0, 4.5);

        threeRenderer = new THREE.WebGLRenderer({ antialias: true });
        threeRenderer.setSize(container.clientWidth, container.clientHeight);
        threeRenderer.setPixelRatio(Math.min(window.devicePixelRatio, 2));
        container.appendChild(threeRenderer.domElement);

        // Lighting
        const ambLight = new THREE.AmbientLight(0xffffff, 0.85);
        threeScene.add(ambLight);
        const dirLight = new THREE.DirectionalLight(0xfffaed, 0.8);
        dirLight.position.set(5, 8, 5);
        threeScene.add(dirLight);

        // Mouse look / pointer drag listeners
        container.addEventListener('pointerdown', (e) => {
          is3DPointerDown = true;
          prevMouseX = e.clientX;
          prevMouseY = e.clientY;
        });
        window.addEventListener('pointermove', (e) => {
          if (!is3DPointerDown) return;
          const deltaX = e.clientX - prevMouseX;
          const deltaY = e.clientY - prevMouseY;
          prevMouseX = e.clientX;
          prevMouseY = e.clientY;

          cameraYaw -= deltaX * 0.004;
          cameraPitch -= deltaY * 0.003;
          cameraPitch = Math.max(-1.1, Math.min(1.1, cameraPitch));

          threeCamera.rotation.order = 'YXZ';
          threeCamera.rotation.y = cameraYaw;
          threeCamera.rotation.x = cameraPitch;
        });
        window.addEventListener('pointerup', () => { is3DPointerDown = false; });

        // WASD Keyboard Listeners
        window.addEventListener('keydown', (e) => {
          const k = e.key.toLowerCase();
          if (['w', 'a', 's', 'd'].includes(k)) AppState.cameraKeyMove[k] = true;
        });
        window.addEventListener('keyup', (e) => {
          const k = e.key.toLowerCase();
          if (['w', 'a', 's', 'd'].includes(k)) AppState.cameraKeyMove[k] = false;
        });

        // Window resize
        window.addEventListener('resize', () => {
          if (!threeCamera || !threeRenderer) return;
          threeCamera.aspect = container.clientWidth / container.clientHeight;
          threeCamera.updateProjectionMatrix();
          threeRenderer.setSize(container.clientWidth, container.clientHeight);
        });

        isThreeInitialized = true;
        animateThreeScene();
      }

      // Load Texture & Depth Map for Mode A
      const textureLoader = new THREE.TextureLoader();
      textureLoader.load(diffuseUrl, (diffuseTex) => {
        textureLoader.load(depthUrl, (depthTex) => {
          if (planeMesh) threeScene.remove(planeMesh);

          // Subdivided 3D plane with depth displacement
          const geom = new THREE.PlaneGeometry(8, 8, 180, 180);
          const mat = new THREE.MeshStandardMaterial({
            map: diffuseTex,
            displacementMap: depthTex,
            displacementScale: 1.8,
            roughness: 0.45,
            metalness: 0.1
          });

          planeMesh = new THREE.Mesh(geom, mat);
          planeMesh.position.set(0, 0, -1);
          threeScene.add(planeMesh);
        });
      });

      // Build Procedural Room for Mode B
      buildProcedural3DRoom();
    }

    function buildProcedural3DRoom() {
      if (proceduralRoomGroup) threeScene.remove(proceduralRoomGroup);
      proceduralRoomGroup = new THREE.Group();

      // Floor (Warm walnut / travertine)
      const floorGeom = new THREE.PlaneGeometry(10, 10);
      const floorMat = new THREE.MeshStandardMaterial({ color: 0x3d281d, roughness: 0.3 });
      const floor = new THREE.Mesh(floorGeom, floorMat);
      floor.rotation.x = -Math.PI / 2;
      floor.position.y = -2;
      proceduralRoomGroup.add(floor);

      // Back Wall
      const wallGeom = new THREE.PlaneGeometry(10, 5);
      const wallMat = new THREE.MeshStandardMaterial({ color: 0x142e40, roughness: 0.8 });
      const backWall = new THREE.Mesh(wallGeom, wallMat);
      backWall.position.set(0, 0.5, -5);
      proceduralRoomGroup.add(backWall);

      // Left Wall
      const leftWall = new THREE.Mesh(wallGeom, wallMat);
      leftWall.rotation.y = Math.PI / 2;
      leftWall.position.set(-5, 0.5, 0);
      proceduralRoomGroup.add(leftWall);

      // Ceiling
      const ceilingGeom = new THREE.PlaneGeometry(10, 10);
      const ceilingMat = new THREE.MeshStandardMaterial({ color: 0x0e2230, roughness: 0.9 });
      const ceiling = new THREE.Mesh(ceilingGeom, ceilingMat);
      ceiling.rotation.x = Math.PI / 2;
      ceiling.position.y = 3;
      proceduralRoomGroup.add(ceiling);

      // Stylized Furniture Blocks
      // Sofa
      const sofaGeom = new THREE.BoxGeometry(3.2, 0.9, 1.4);
      const sofaMat = new THREE.MeshStandardMaterial({ color: 0xc85a38, roughness: 0.5 });
      const sofa = new THREE.Mesh(sofaGeom, sofaMat);
      sofa.position.set(0, -1.5, -3.2);
      proceduralRoomGroup.add(sofa);

      // Coffee Table
      const tableGeom = new THREE.BoxGeometry(1.8, 0.45, 0.9);
      const tableMat = new THREE.MeshStandardMaterial({ color: 0xfaf7f2, roughness: 0.2 });
      const table = new THREE.Mesh(tableGeom, tableMat);
      table.position.set(0, -1.75, -1.8);
      proceduralRoomGroup.add(table);

      proceduralRoomGroup.visible = (AppState.active3DMode === 'mode-b');
      threeScene.add(proceduralRoomGroup);
    }

    function switch3DExperienceMode(mode) {
      AppState.active3DMode = mode;
      document.querySelectorAll('.spatial-mode-pill').forEach(b => b.classList.remove('active'));
      const activeBtn = document.getElementById(`tab-3d-${mode}`);
      if (activeBtn) activeBtn.classList.add('active');

      if (planeMesh) planeMesh.visible = (mode === 'mode-a');
      if (proceduralRoomGroup) proceduralRoomGroup.visible = (mode === 'mode-b');

      const modeTitle = document.getElementById('spatial-mode-subtext');
      const hudChipMode = document.getElementById('hud-chip-mode');
      const hudDisclaimer = document.getElementById('hud-chip-disclaimer');

      if (mode === 'mode-a') {
        modeTitle.innerText = 'AI Spatial Preview — Depth-Based Walkthrough (Look around, WASD to move)';
        hudChipMode.innerText = 'Mode A: AI Spatial Preview';
        hudDisclaimer.innerText = 'Depth-based 2.5D spatial estimation. Visualizes relative depth and perspective parallax from a single viewpoint.';
      } else {
        modeTitle.innerText = 'Procedural 3D Room — Approximate Geometric Reconstruction (Orbit / Camera view)';
        hudChipMode.innerText = 'Mode B: Procedural 3D Room';
        hudDisclaimer.innerText = 'Reconstructs approximate room bounds, floor plan, and architectural volumes based on category heuristics.';
      }
    }

    function setCameraPresetView(preset) {
      document.querySelectorAll('.btn-camera-preset').forEach(b => b.classList.remove('active'));
      const activeBtn = document.getElementById(`cam-preset-${preset}`);
      if (activeBtn) activeBtn.classList.add('active');

      if (!threeCamera) return;
      if (preset === 'firstperson') {
        threeCamera.position.set(0, 0, 4.2);
        cameraYaw = 0; cameraPitch = 0;
        threeCamera.rotation.set(0, 0, 0);
      } else if (preset === 'isometric') {
        threeCamera.position.set(4, 3, 5);
        threeCamera.lookAt(0, 0, -1);
      } else if (preset === 'top') {
        threeCamera.position.set(0, 7, 0);
        threeCamera.lookAt(0, 0, 0);
      }
    }

    function reset3DCameraPosition() {
      setCameraPresetView('firstperson');
    }

    function startKeyMove(key) { AppState.cameraKeyMove[key] = true; }
    function stopKeyMove(key) { AppState.cameraKeyMove[key] = false; }

    function animateThreeScene() {
      threeAnimFrameId = requestAnimationFrame(animateThreeScene);

      // WASD Camera movement inside the room
      if (threeCamera) {
        const moveSpeed = 0.06;
        if (AppState.cameraKeyMove.w) threeCamera.translateZ(-moveSpeed);
        if (AppState.cameraKeyMove.s) threeCamera.translateZ(moveSpeed);
        if (AppState.cameraKeyMove.a) threeCamera.translateX(-moveSpeed);
        if (AppState.cameraKeyMove.d) threeCamera.translateX(moveSpeed);

        // Clamp camera position to prevent flying outside virtual room bounds
        threeCamera.position.x = Math.max(-4, Math.min(4, threeCamera.position.x));
        threeCamera.position.y = Math.max(-1.5, Math.min(2.5, threeCamera.position.y));
        threeCamera.position.z = Math.max(-2, Math.min(6, threeCamera.position.z));
      }

      threeRenderer.render(threeScene, threeCamera);
    }

    function scrollToSpatial3DExperience() {
      const section = document.getElementById('section-spatial-3d-experience');
      if (section) section.scrollIntoView({ behavior: 'smooth' });
    }

    /* Dollhouse 3D Interactive Controls in Hero */
    let isSpinning = true;
    function toggleDollhouseSpin() {
      const dollhouse = document.getElementById('hero-dollhouse-3d');
      const btn = document.getElementById('btn-spin-toggle');
      isSpinning = !isSpinning;
      dollhouse.classList.toggle('auto-spin', isSpinning);
      btn.querySelector('span').innerText = isSpinning ? 'Pause Spin' : 'Resume Spin';
    }

    /* ==========================================================================
       PART 11: MY DESIGNS ARCHITECTURAL PORTFOLIO
       ========================================================================== */
    function loadSavedDesignsFromStorage() {
      try {
        const data = localStorage.getItem('sketchspace_saved_designs');
        if (data) {
          AppState.savedDesigns = JSON.parse(data);
        } else {
          // Preload initial curated designs if storage empty
          AppState.savedDesigns = [
            {
              id: 'design_1',
              title: 'Minimalist Travertine Salon',
              category: 'living_room',
              renderUrl: '/api/image/local_cn_living_room_1795536539194.png',
              sketchUrl: '/api/sketches/example/new_living_room_sketch.png',
              depthUrl: '/api/depth/local_cn_living_room_1795536539194.png',
              date: 'November 2026',
              notes: 'Natural daylight, travertine slab flooring, warm linen upholstery'
            },
            {
              id: 'design_2',
              title: 'Master Bedroom Sanctuary',
              category: 'bedroom',
              renderUrl: '/api/image/local_cn_bedroom_1795531503385.png',
              sketchUrl: '/api/sketches/example/new_bedroom_sketch.png',
              depthUrl: '/api/depth/local_cn_bedroom_1795531503385.png',
              date: 'November 2026',
              notes: 'White oak accents, wool throws, floor-to-ceiling windows'
            },
            {
              id: 'design_3',
              title: 'Calacatta Gold Spa Bathroom',
              category: 'bathroom',
              renderUrl: '/api/image/local_cn_bathroom_1795532521076.png',
              sketchUrl: '/api/sketches/example/new_bathroom_sketch.png',
              depthUrl: '/api/depth/local_cn_bathroom_1795532521076.png',
              date: 'November 2026',
              notes: 'Freestanding stone tub, brushed brass fixtures'
            }
          ];
          saveDesignsToStorage();
        }
      } catch (e) {
        console.error('Failed to load designs:', e);
      }
    }

    function saveDesignsToStorage() {
      try {
        localStorage.setItem('sketchspace_saved_designs', JSON.stringify(AppState.savedDesigns));
      } catch (e) {
        console.error('Storage error:', e);
      }
    }

    function renderSavedDesignsGallery(filterCategory = 'all', searchQuery = '') {
      const container = document.getElementById('saved-designs-grid-container');
      const emptyState = document.getElementById('portfolio-empty-state');
      if (!container) return;

      container.innerHTML = '';
      let list = AppState.savedDesigns || [];

      if (filterCategory && filterCategory !== 'all') {
        list = list.filter(d => d.category === filterCategory);
      }
      if (searchQuery) {
        const q = searchQuery.toLowerCase();
        list = list.filter(d => d.title.toLowerCase().includes(q) || (d.notes && d.notes.toLowerCase().includes(q)));
      }

      if (list.length === 0) {
        emptyState.style.display = 'flex';
        return;
      }
      emptyState.style.display = 'none';

      list.forEach(item => {
        const card = document.createElement('div');
        card.className = 'saved-design-card';
        card.innerHTML = `
          <div class="card-thumbnail-stage">
            <img src="${item.renderUrl}" alt="${item.title}" onerror="this.src='/api/sketches/example/new_living_room_sketch.png'">
            <img class="card-sketch-hover-preview" src="${item.sketchUrl}" alt="Original Sketch">
          </div>
          <div class="card-body">
            <div class="card-title-row">
              <h4 class="card-project-title">${item.title}</h4>
              <span class="card-room-badge">${item.category.replace('_', ' ')}</span>
            </div>
            <div class="card-date-meta">${item.date || 'Saved Space'}</div>
            <div class="card-actions-row">
              <button class="btn-card-action" onclick="reopenDesignInStudio('${item.id}')">
                <svg width="13" height="13" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M11 4H4a2 2 0 0 0-2 2v14a2 2 0 0 0 2 2h14a2 2 0 0 0 2-2v-7"></path><path d="M18.5 2.5a2.121 2.121 0 0 1 3 3L12 15l-4 1 1-4 9.5-9.5z"></path></svg>
                <span>Edit in Studio</span>
              </button>
              <button class="btn-card-action" onclick="exploreSavedDesignIn3D('${item.id}')">
                <svg width="13" height="13" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polygon points="12 2 2 7 12 12 22 7 12 2"></polygon><polyline points="2 17 12 22 22 17"></polyline><polyline points="2 12 12 17 22 12"></polyline></svg>
                <span>3D</span>
              </button>
              <button class="btn-card-delete" title="Delete Design" onclick="deleteSavedDesign('${item.id}')">
                <svg width="13" height="13" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="3 6 5 6 21 6"></polyline><path d="M19 6v14a2 2 0 0 1-2 2H7a2 2 0 0 1-2-2V6m3 0V4a2 2 0 0 1 2-2h4a2 2 0 0 1 2 2v2"></path></svg>
              </button>
            </div>
          </div>
        `;
        container.appendChild(card);
      });
    }

    function setPortfolioCategoryFilter(cat, btn) {
      document.querySelectorAll('.portfolio-chip').forEach(c => c.classList.remove('active'));
      if (btn) btn.classList.add('active');
      const search = document.getElementById('portfolio-search-input').value;
      renderSavedDesignsGallery(cat, search);
    }

    function filterSavedDesignsGallery() {
      const search = document.getElementById('portfolio-search-input').value;
      const activeChip = document.querySelector('.portfolio-chip.active');
      const cat = activeChip ? activeChip.innerText.toLowerCase().replace(' ', '_') : 'all';
      renderSavedDesignsGallery(cat === 'all_spaces' ? 'all' : cat, search);
    }

    function reopenDesignInStudio(id) {
      const design = AppState.savedDesigns.find(d => d.id === id);
      if (!design) return;
      switchAppView('studio');
      AppState.currentGeneratedUrl = design.renderUrl;
      AppState.currentSketchUrl = design.sketchUrl;
      AppState.currentDepthUrl = design.depthUrl || design.renderUrl;
      displaySynthesizedResult();

      // Load sketch into canvas
      const img = new Image();
      img.onload = () => {
        ctx.fillStyle = '#faf7f2';
        ctx.fillRect(0, 0, canvas.width, canvas.height);
        ctx.drawImage(img, 0, 0, canvas.width, canvas.height);
        saveCanvasState();
      };
      img.src = design.sketchUrl;
      showToast(`Reopened "${design.title}" in Studio`);
    }

    function exploreSavedDesignIn3D(id) {
      const design = AppState.savedDesigns.find(d => d.id === id);
      if (!design) return;
      switchAppView('studio');
      AppState.currentGeneratedUrl = design.renderUrl;
      AppState.currentSketchUrl = design.sketchUrl;
      AppState.currentDepthUrl = design.depthUrl || design.renderUrl;
      displaySynthesizedResult();
      initOrUpdateThree3DScene(design.renderUrl, design.depthUrl || design.renderUrl);
      scrollToSpatial3DExperience();
    }

    function deleteSavedDesign(id) {
      if (!confirm('Are you sure you want to delete this saved design?')) return;
      AppState.savedDesigns = AppState.savedDesigns.filter(d => d.id !== id);
      saveDesignsToStorage();
      renderSavedDesignsGallery();
      showToast('Design deleted from portfolio');
    }

    function openSaveDesignModal() {
      document.getElementById('save-design-modal').classList.add('active');
    }
    function closeSaveDesignModal() {
      document.getElementById('save-design-modal').classList.remove('active');
    }

    function confirmSaveCurrentDesign() {
      const title = document.getElementById('save-design-title').value.trim() || 'Untitled Spatial Design';
      const notes = document.getElementById('save-design-notes').value.trim();

      const newDesign = {
        id: `design_${Date.now()}`,
        title: title,
        category: AppState.activeCategory,
        renderUrl: AppState.currentGeneratedUrl,
        sketchUrl: canvas.toDataURL('image/png'),
        depthUrl: AppState.currentDepthUrl,
        date: new Date().toLocaleDateString('en-US', { month: 'short', year: 'numeric' }),
        notes: notes
      };

      AppState.savedDesigns.unshift(newDesign);
      saveDesignsToStorage();
      closeSaveDesignModal();
      showToast(`Saved "${title}" to My Designs`);
    }

    /* Presentation Mode Curtain */
    function openFullscreenPresentation() {
      document.getElementById('pres-sketch-img').src = AppState.currentSketchUrl;
      document.getElementById('pres-render-img').src = AppState.currentGeneratedUrl;
      document.getElementById('fullscreen-presentation-curtain').classList.add('active');
    }
    function closeFullscreenPresentation() {
      document.getElementById('fullscreen-presentation-curtain').classList.remove('active');
    }

    /* Spatial Toast System */
    function showToast(msg) {
      const toast = document.getElementById('spatial-toast');
      document.getElementById('toast-message-text').innerText = msg;
      toast.style.display = 'flex';
      setTimeout(() => { toast.style.display = 'none'; }, 3200);
    }

    /* Page Initialization */
    window.addEventListener('DOMContentLoaded', () => {
      loadSavedDesignsFromStorage();
      const hash = window.location.hash.replace('#', '') || 'overview';
      switchAppView(hash);
      initDrawingCanvasIfNeeded();

      // Preload Three.js 3D scene with verified living room
      initOrUpdateThree3DScene(AppState.currentGeneratedUrl, AppState.currentDepthUrl);
    });
  </script>
</body>
</html>
''')

print("Successfully generated SketchSpace AI Complete Redesign index.html!")
