# Build Ultimate Visual Excellence index.html for SketchSpace AI
import os

HTML_CONTENT = """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>SketchSpace AI — Spatial Architectural Synthesis Studio</title>
  
  <!-- Architectural Typography System: Sora (Display), Manrope (Body), IBM Plex Mono (Technical) -->
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=IBM+Plex+Mono:ital,wght@0,400;0,500;0,600;0,700;1,400&family=Manrope:wght@300;400;500;600;700;800&family=Sora:wght@300;400;500;600;700;800&display=swap" rel="stylesheet">
  
  <style>
    /* ==========================================================================
       ULTIMATE CINEMATIC MULTICOLOUR & SPATIAL COMPUTING DESIGN SYSTEM
       ========================================================================== */
    :root {
      /* Deep Spatial Midnight & Obsidian Foundation */
      --obsidian: #04060d;
      --midnight: #080c1b;
      --deep-indigo: #0f152d;
      --night-surface: #141b36;
      
      /* Vibrant Multicolour Spectrum (Cyan, Violet, Magenta, Teal, Amber) */
      --electric-cyan: #0fe3ff;
      --cyan-glow: rgba(15, 227, 255, 0.45);
      --electric-violet: #8e44ff;
      --violet-glow: rgba(142, 68, 255, 0.45);
      --magenta-vivid: #ff2a8d;
      --magenta-glow: rgba(255, 42, 141, 0.45);
      --teal-luminous: #00f5c4;
      --teal-glow: rgba(0, 245, 196, 0.4);
      --sapphire-blue: #146eff;
      --rose-pink: #ff6584;
      --amber-warm: #ffb52e;
      --amber-glow: rgba(255, 181, 46, 0.35);
      
      /* Neutral & High-Legibility Typography Shades */
      --soft-white: #f8fafc;
      --pure-white: #ffffff;
      --muted-grey: #94a3b8;
      --dim-grey: #64748b;
      --dark-edge: rgba(255, 255, 255, 0.09);
      --dark-edge-strong: rgba(255, 255, 255, 0.16);
      
      /* Iridescent Glass & Acrylic Materials */
      --glass-surface-1: rgba(12, 18, 38, 0.78);
      --glass-surface-2: rgba(18, 26, 56, 0.7);
      --glass-surface-elevated: rgba(24, 34, 72, 0.88);
      --glass-surface-translucent: rgba(10, 15, 32, 0.6);
      --iridescent-gradient: linear-gradient(135deg, rgba(15, 227, 255, 0.4), rgba(142, 68, 255, 0.45), rgba(255, 42, 141, 0.4));
      --iridescent-border: linear-gradient(135deg, rgba(15, 227, 255, 0.6) 0%, rgba(142, 68, 255, 0.5) 50%, rgba(255, 42, 141, 0.55) 100%);
      
      /* Typography System */
      --font-display: 'Sora', sans-serif;
      --font-body: 'Manrope', -apple-system, BlinkMacSystemFont, sans-serif;
      --font-tech: 'IBM Plex Mono', monospace;

      /* Radii & Elevation */
      --radius-2xl: 28px;
      --radius-xl: 20px;
      --radius-lg: 14px;
      --radius-md: 10px;
      --radius-sm: 6px;
      --radius-pill: 9999px;
    }

    * { box-sizing: border-box; margin: 0; padding: 0; }

    html {
      scroll-behavior: smooth;
      background-color: var(--obsidian);
    }

    body {
      background-color: var(--obsidian);
      color: var(--soft-white);
      font-family: var(--font-body);
      min-height: 100vh;
      display: flex;
      flex-direction: column;
      overflow-x: hidden;
      position: relative;
      line-height: 1.6;
      -webkit-font-smoothing: antialiased;
      -moz-osx-font-smoothing: grayscale;
    }

    /* Selection Styling */
    ::selection {
      background: rgba(15, 227, 255, 0.35);
      color: #ffffff;
    }

    /* ==========================================================================
       LAYER 1: MULTI-LAYERED ANIMATED AURORA LIGHTFIELDS & LIGHT RIBBONS
       ========================================================================== */
    .aurora-universe {
      position: fixed;
      top: 0; left: 0; width: 100vw; height: 100vh;
      pointer-events: none;
      z-index: 0;
      overflow: hidden;
    }

    .aurora-sphere {
      position: absolute;
      border-radius: 50%;
      filter: blur(90px);
      opacity: 0.42;
      mix-blend-mode: screen;
      will-change: transform;
      animation: floatAuroraUniverse 26s infinite alternate ease-in-out;
    }

    .aurora-1 {
      top: -12%; left: -8%;
      width: 70vw; height: 65vh;
      background: radial-gradient(circle, rgba(142, 68, 255, 0.65) 0%, rgba(20, 110, 255, 0.35) 55%, transparent 75%);
      animation-duration: 22s;
    }

    .aurora-2 {
      top: 10%; right: -12%;
      width: 65vw; height: 70vh;
      background: radial-gradient(circle, rgba(15, 227, 255, 0.55) 0%, rgba(0, 245, 196, 0.35) 50%, transparent 75%);
      animation-duration: 28s;
      animation-delay: -6s;
    }

    .aurora-3 {
      bottom: -15%; left: 15%;
      width: 75vw; height: 65vh;
      background: radial-gradient(circle, rgba(255, 42, 141, 0.48) 0%, rgba(255, 101, 132, 0.28) 50%, transparent 75%);
      animation-duration: 30s;
      animation-delay: -12s;
    }

    .aurora-4 {
      top: 40%; left: 30%;
      width: 50vw; height: 50vh;
      background: radial-gradient(circle, rgba(255, 181, 46, 0.25) 0%, rgba(255, 42, 141, 0.2) 55%, transparent 75%);
      animation-duration: 34s;
      animation-delay: -18s;
    }

    .aurora-5 {
      bottom: 25%; right: 10%;
      width: 45vw; height: 45vh;
      background: radial-gradient(circle, rgba(0, 245, 196, 0.3) 0%, rgba(20, 110, 255, 0.22) 50%, transparent 75%);
      animation-duration: 32s;
      animation-delay: -8s;
    }

    /* Diagonal Atmospheric Volumetric Light Ribbon */
    .aurora-ribbon {
      position: absolute;
      top: -20%; left: -10%;
      width: 140vw; height: 40vh;
      background: linear-gradient(115deg, transparent 20%, rgba(15, 227, 255, 0.08) 45%, rgba(142, 68, 255, 0.09) 60%, rgba(255, 42, 141, 0.07) 75%, transparent 90%);
      transform: rotate(-18deg);
      filter: blur(45px);
      mix-blend-mode: screen;
      animation: ribbonSway 36s infinite ease-in-out alternate;
    }

    @keyframes ribbonSway {
      0% { transform: rotate(-18deg) translateY(0); }
      50% { transform: rotate(-14deg) translateY(40px); }
      100% { transform: rotate(-22deg) translateY(-30px); }
    }

    @keyframes floatAuroraUniverse {
      0% { transform: translate(0, 0) scale(1) rotate(0deg); }
      50% { transform: translate(4vw, 5vh) scale(1.1) rotate(10deg); }
      100% { transform: translate(-3vw, -4vh) scale(0.94) rotate(-8deg); }
    }

    /* Dual Perspective Spatial Architectural Grid Floor */
    .spatial-grid-floor {
      position: fixed;
      top: 0; left: 0; width: 100vw; height: 100vh;
      pointer-events: none;
      z-index: 0;
      opacity: 0.32;
      background-image: 
        linear-gradient(to right, rgba(15, 227, 255, 0.1) 1px, transparent 1px),
        linear-gradient(to bottom, rgba(142, 68, 255, 0.1) 1px, transparent 1px);
      background-size: 52px 52px;
      mask-image: radial-gradient(ellipse at 50% 50%, black 30%, transparent 85%);
      -webkit-mask-image: radial-gradient(ellipse at 50% 50%, black 30%, transparent 85%);
    }

    /* Ambient Spatial Dust Particles */
    #ambient-particles-canvas {
      position: fixed;
      top: 0; left: 0; width: 100vw; height: 100vh;
      pointer-events: none;
      z-index: 1;
    }

    /* ==========================================================================
       LAYER 2: FLOATING 3D ARCHITECTURAL BACKGROUND SCULPTURES & PRISMS
       ========================================================================== */
    .floating-sculptures-layer {
      position: fixed;
      top: 0; left: 0; width: 100vw; height: 100vh;
      pointer-events: none;
      z-index: 1;
      overflow: hidden;
    }

    .sculpture-prism {
      position: absolute;
      transform-style: preserve-3d;
      will-change: transform;
      animation: floatSculptureMotion 22s infinite ease-in-out;
    }

    .sculpture-1 {
      top: 16%; left: 3%;
      width: 150px; height: 150px;
      animation-duration: 24s;
    }
    .sculpture-2 {
      bottom: 20%; right: 4%;
      width: 180px; height: 180px;
      animation-duration: 28s;
      animation-delay: -7s;
    }
    .sculpture-3 {
      top: 50%; left: 90%;
      width: 120px; height: 120px;
      animation-duration: 20s;
      animation-delay: -14s;
    }
    .sculpture-4 {
      top: 80%; left: 8%;
      width: 110px; height: 110px;
      animation-duration: 26s;
      animation-delay: -10s;
    }

    @keyframes floatSculptureMotion {
      0% { transform: translateY(0) rotateX(15deg) rotateY(20deg); }
      50% { transform: translateY(-28px) rotateX(32deg) rotateY(60deg); }
      100% { transform: translateY(0) rotateX(15deg) rotateY(20deg); }
    }

    .glass-plane {
      position: absolute;
      width: 100%; height: 100%;
      border: 1px solid rgba(15, 227, 255, 0.42);
      background: linear-gradient(135deg, rgba(15, 227, 255, 0.08), rgba(255, 42, 141, 0.06));
      backdrop-filter: blur(5px);
      box-shadow: 0 0 24px rgba(15, 227, 255, 0.16);
    }

    /* ==========================================================================
       SECTION 3: TOP SPATIAL NAVIGATION & BRAND LOCKUP
       ========================================================================== */
    .spatial-nav {
      position: sticky;
      top: 0;
      z-index: 100;
      backdrop-filter: blur(28px);
      -webkit-backdrop-filter: blur(28px);
      background: rgba(8, 12, 27, 0.78);
      border-bottom: 1px solid rgba(255, 255, 255, 0.1);
      box-shadow: 0 10px 36px rgba(0, 0, 0, 0.45), inset 0 -1px 0 rgba(255, 255, 255, 0.05);
      padding: 14px 44px;
      display: flex;
      align-items: center;
      justify-content: space-between;
      gap: 20px;
      transition: all 0.3s ease;
    }

    .spatial-brand {
      display: flex;
      align-items: center;
      gap: 16px;
      text-decoration: none;
      color: inherit;
      cursor: pointer;
      user-select: none;
    }

    .brand-cube-badge {
      width: 48px;
      height: 48px;
      border-radius: 14px;
      background: linear-gradient(135deg, rgba(15, 227, 255, 0.22), rgba(142, 68, 255, 0.38), rgba(255, 42, 141, 0.28));
      border: 1px solid rgba(15, 227, 255, 0.6);
      display: flex;
      align-items: center;
      justify-content: center;
      box-shadow: 0 0 28px rgba(15, 227, 255, 0.4), inset 0 1px 0 rgba(255, 255, 255, 0.4);
      position: relative;
      transition: transform 0.35s cubic-bezier(0.16, 1, 0.3, 1), box-shadow 0.35s ease;
    }
    .spatial-brand:hover .brand-cube-badge {
      transform: scale(1.08) rotate(4deg);
      box-shadow: 0 0 38px rgba(255, 42, 141, 0.6);
    }

    .brand-text-lockup h1 {
      font-family: var(--font-display);
      font-size: 1.48rem;
      font-weight: 800;
      letter-spacing: -0.04em;
      line-height: 1.1;
      background: linear-gradient(135deg, #ffffff 35%, var(--electric-cyan) 75%, var(--magenta-vivid) 100%);
      -webkit-background-clip: text;
      -webkit-text-fill-color: transparent;
      display: flex;
      align-items: center;
      gap: 8px;
    }

    .brand-text-lockup p {
      font-family: var(--font-tech);
      font-size: 0.72rem;
      color: var(--muted-grey);
      letter-spacing: 0.04em;
      margin-top: 2px;
    }

    .spatial-nav-tabs {
      display: flex;
      align-items: center;
      gap: 6px;
      background: rgba(12, 18, 38, 0.85);
      padding: 5px;
      border-radius: var(--radius-lg);
      border: 1px solid var(--dark-edge);
      box-shadow: inset 0 1px 3px rgba(0, 0, 0, 0.4);
    }

    .nav-link-btn {
      background: transparent;
      border: none;
      color: var(--muted-grey);
      font-family: var(--font-body);
      font-size: 0.86rem;
      font-weight: 600;
      padding: 8px 20px;
      border-radius: var(--radius-md);
      cursor: pointer;
      transition: all 0.22s cubic-bezier(0.16, 1, 0.3, 1);
      display: flex;
      align-items: center;
      gap: 8px;
    }
    .nav-link-btn:hover {
      color: var(--soft-white);
      background: rgba(255, 255, 255, 0.07);
    }
    .nav-link-btn.active {
      color: var(--pure-white);
      background: linear-gradient(135deg, rgba(15, 227, 255, 0.26), rgba(142, 68, 255, 0.32));
      border: 1px solid rgba(15, 227, 255, 0.5);
      box-shadow: 0 0 22px rgba(15, 227, 255, 0.3);
    }

    .engine-status-tag {
      display: flex;
      align-items: center;
      gap: 10px;
      padding: 7px 18px;
      border-radius: var(--radius-pill);
      background: rgba(0, 245, 196, 0.1);
      border: 1px solid rgba(0, 245, 196, 0.38);
      color: var(--teal-luminous);
      font-family: var(--font-tech);
      font-size: 0.74rem;
      font-weight: 600;
      letter-spacing: 0.03em;
      box-shadow: 0 0 16px rgba(0, 245, 196, 0.15);
    }
    .beacon-pulse {
      width: 8px;
      height: 8px;
      border-radius: 50%;
      background: var(--teal-luminous);
      box-shadow: 0 0 14px var(--teal-luminous);
      animation: beaconPulseAnim 2s infinite ease-in-out;
    }
    @keyframes beaconPulseAnim {
      0%, 100% { opacity: 0.4; transform: scale(0.85); }
      50% { opacity: 1; transform: scale(1.35); }
    }

    .btn-presentation-pill {
      background: rgba(142, 68, 255, 0.18);
      border: 1px solid rgba(142, 68, 255, 0.45);
      color: #d8c2ff;
      font-family: var(--font-tech);
      font-size: 0.75rem;
      font-weight: 600;
      padding: 7px 16px;
      border-radius: var(--radius-pill);
      cursor: pointer;
      display: inline-flex;
      align-items: center;
      gap: 7px;
      transition: all 0.22s ease;
      box-shadow: 0 0 15px rgba(142, 68, 255, 0.15);
    }
    .btn-presentation-pill:hover {
      background: rgba(142, 68, 255, 0.35);
      border-color: var(--electric-violet);
      color: #ffffff;
      transform: translateY(-1px);
      box-shadow: 0 0 24px rgba(142, 68, 255, 0.4);
    }

    /* Main Container Shell */
    .main-spatial-container {
      position: relative;
      z-index: 2;
      width: 100%;
      max-width: 1540px;
      margin: 0 auto;
      padding: 38px 44px 72px;
      display: flex;
      flex-direction: column;
      gap: 44px;
    }

    /* ==========================================================================
       SECTION 4: CINEMATIC MULTICOLOUR HERO WITH LARGE 3D SPATIAL ROOM
       ========================================================================== */
    .hero-spatial-section {
      position: relative;
      padding: 76px 54px 68px;
      border-radius: var(--radius-2xl);
      background: linear-gradient(145deg, rgba(12, 18, 38, 0.9) 0%, rgba(8, 12, 27, 0.97) 100%);
      border: 1px solid rgba(255, 255, 255, 0.13);
      box-shadow: 0 32px 80px rgba(0, 0, 0, 0.55), inset 0 1px 0 rgba(255, 255, 255, 0.15);
      overflow: hidden;
      display: grid;
      grid-template-columns: 1.15fr 0.85fr;
      gap: 48px;
      align-items: center;
    }

    @media (max-width: 1100px) {
      .hero-spatial-section { grid-template-columns: 1fr; text-align: center; }
      .hero-editorial-left { align-items: center; }
      .hero-micro-metrics { justify-content: center; }
    }

    .hero-editorial-left {
      display: flex;
      flex-direction: column;
      gap: 24px;
      text-align: left;
      z-index: 2;
    }

    .hero-tagline-badge {
      display: inline-flex;
      align-items: center;
      gap: 10px;
      padding: 7px 20px;
      border-radius: var(--radius-pill);
      background: rgba(15, 227, 255, 0.12);
      border: 1px solid rgba(15, 227, 255, 0.45);
      color: var(--electric-cyan);
      font-family: var(--font-tech);
      font-size: 0.76rem;
      font-weight: 600;
      letter-spacing: 0.08em;
      text-transform: uppercase;
      align-self: flex-start;
      box-shadow: 0 0 20px rgba(15, 227, 255, 0.22);
    }

    .hero-editorial-headline {
      font-family: var(--font-display);
      font-size: clamp(2.8rem, 4.5vw, 4.6rem);
      font-weight: 800;
      line-height: 1.06;
      letter-spacing: -0.04em;
      background: linear-gradient(135deg, #ffffff 20%, var(--electric-cyan) 55%, var(--magenta-vivid) 85%, var(--amber-warm) 100%);
      -webkit-background-clip: text;
      -webkit-text-fill-color: transparent;
      text-shadow: 0 0 55px rgba(15, 227, 255, 0.35);
    }

    .hero-editorial-lead {
      font-size: 1.14rem;
      color: var(--muted-grey);
      line-height: 1.68;
      max-width: 590px;
      font-weight: 400;
    }

    .hero-cta-cluster {
      display: flex;
      align-items: center;
      gap: 18px;
      flex-wrap: wrap;
      margin-top: 6px;
    }

    .btn-spatial-primary {
      background: linear-gradient(135deg, var(--electric-cyan) 0%, var(--electric-violet) 50%, var(--magenta-vivid) 100%);
      color: var(--obsidian);
      font-family: var(--font-display);
      font-weight: 700;
      font-size: 1.02rem;
      padding: 16px 36px;
      border-radius: var(--radius-lg);
      border: none;
      cursor: pointer;
      display: inline-flex;
      align-items: center;
      gap: 10px;
      box-shadow: 0 0 34px rgba(15, 227, 255, 0.45);
      transition: all 0.25s cubic-bezier(0.16, 1, 0.3, 1);
    }
    .btn-spatial-primary:hover {
      transform: translateY(-3px) scale(1.02);
      box-shadow: 0 0 54px rgba(255, 42, 141, 0.65);
    }

    .btn-spatial-secondary {
      background: rgba(18, 26, 56, 0.8);
      color: var(--soft-white);
      font-family: var(--font-display);
      font-weight: 600;
      font-size: 0.98rem;
      padding: 16px 28px;
      border-radius: var(--radius-lg);
      border: 1px solid rgba(255, 255, 255, 0.16);
      cursor: pointer;
      display: inline-flex;
      align-items: center;
      gap: 10px;
      transition: all 0.22s ease;
    }
    .btn-spatial-secondary:hover {
      background: rgba(26, 38, 80, 0.95);
      border-color: rgba(15, 227, 255, 0.55);
      transform: translateY(-2px);
      box-shadow: 0 0 25px rgba(15, 227, 255, 0.2);
    }

    /* Micro-Metrics Badge Row */
    .hero-micro-metrics {
      display: flex;
      align-items: center;
      gap: 20px;
      flex-wrap: wrap;
      margin-top: 8px;
      padding-top: 18px;
      border-top: 1px solid var(--dark-edge);
      font-family: var(--font-tech);
      font-size: 0.74rem;
      color: var(--muted-grey);
    }
    .hero-micro-metrics span {
      display: inline-flex;
      align-items: center;
      gap: 6px;
    }
    .hero-micro-metrics strong {
      color: var(--electric-cyan);
    }

    /* ==========================================================================
       SECTION 5: LARGE INTERACTIVE 3D ARCHITECTURAL ROOM STAGE
       ========================================================================== */
    .hero-spatial-stage-right {
      position: relative;
      width: 100%;
      height: 440px;
      perspective: 1200px;
      display: flex;
      align-items: center;
      justify-content: center;
      user-select: none;
    }

    .large-room-3d {
      width: 300px;
      height: 200px;
      position: relative;
      transform-style: preserve-3d;
      transform: rotateX(24deg) rotateY(-36deg);
      animation: rotateSpatialRoom 24s infinite linear;
      transition: transform 0.25s ease-out;
    }
    @keyframes rotateSpatialRoom {
      0% { transform: rotateX(24deg) rotateY(0deg); }
      100% { transform: rotateX(24deg) rotateY(360deg); }
    }

    .room-wall-panel {
      position: absolute;
      width: 300px;
      height: 200px;
      border: 1px solid rgba(15, 227, 255, 0.52);
      background: linear-gradient(135deg, rgba(15, 227, 255, 0.09), rgba(142, 68, 255, 0.07));
      backdrop-filter: blur(8px);
      box-shadow: inset 0 0 28px rgba(142, 68, 255, 0.25);
    }
    .room-wall-panel.front  { transform: translateZ(150px); }
    .room-wall-panel.back   { transform: rotateY(180deg) translateZ(150px); }
    .room-wall-panel.right  { width: 300px; transform: rotateY(90deg) translateZ(150px); }
    .room-wall-panel.left   { width: 300px; transform: rotateY(-90deg) translateZ(150px); }
    .room-wall-panel.ceiling { height: 300px; transform: rotateX(90deg) translateZ(100px); border-color: rgba(255, 42, 141, 0.48); }
    .room-wall-panel.floor   { height: 300px; transform: rotateX(-90deg) translateZ(100px); background: rgba(15, 227, 255, 0.18); }

    /* Window Aperture Cutout Silhouette */
    .wall-window-frame {
      position: absolute;
      top: 32px; left: 48px;
      width: 104px; height: 116px;
      border: 2px solid var(--electric-cyan);
      box-shadow: 0 0 18px var(--electric-cyan);
      background: rgba(15, 227, 255, 0.14);
    }

    /* Abstract Floating Furniture Block Inside 3D Room */
    .furniture-cube {
      position: absolute;
      width: 115px; height: 48px;
      bottom: 22px; left: 48px;
      transform: translateZ(24px);
      border: 1px solid var(--magenta-vivid);
      background: rgba(255, 42, 141, 0.22);
      box-shadow: 0 0 18px rgba(255, 42, 141, 0.4);
    }

    /* Floating Material Tiles */
    .floating-material-sample {
      position: absolute;
      padding: 6px 15px;
      border-radius: var(--radius-sm);
      font-family: var(--font-tech);
      font-size: 0.72rem;
      font-weight: 600;
      backdrop-filter: blur(10px);
      box-shadow: 0 6px 24px rgba(0, 0, 0, 0.5);
    }
    .sample-1 {
      top: -22px; left: -14px;
      background: rgba(15, 227, 255, 0.22);
      border: 1px solid var(--electric-cyan);
      color: var(--electric-cyan);
    }
    .sample-2 {
      bottom: -18px; right: -18px;
      background: rgba(255, 42, 141, 0.22);
      border: 1px solid var(--magenta-vivid);
      color: var(--magenta-vivid);
    }

    /* Spatial Dimension HUD Overlay Annotations */
    .spatial-dim-badge {
      position: absolute;
      top: 16px; right: 16px;
      background: rgba(8, 12, 27, 0.88);
      border: 1px solid rgba(15, 227, 255, 0.48);
      padding: 7px 16px;
      border-radius: var(--radius-md);
      font-family: var(--font-tech);
      font-size: 0.74rem;
      font-weight: 600;
      color: var(--electric-cyan);
      box-shadow: 0 0 18px rgba(15, 227, 255, 0.25);
    }

    /* ==========================================================================
       SECTION 6: SIGNATURE SKETCH-TO-REALITY STORYTELLING SECTION
       ========================================================================== */
    .sketch-to-reality-showcase {
      display: flex;
      flex-direction: column;
      gap: 28px;
      padding: 48px;
      background: linear-gradient(135deg, rgba(12, 18, 38, 0.86), rgba(18, 26, 56, 0.76));
      border: 1px solid rgba(255, 255, 255, 0.13);
      border-radius: var(--radius-2xl);
      box-shadow: 0 24px 60px rgba(0, 0, 0, 0.4);
      position: relative;
    }

    .story-header-row {
      display: flex;
      justify-content: space-between;
      align-items: flex-end;
      flex-wrap: wrap;
      gap: 18px;
    }

    .story-stage-cards {
      display: grid;
      grid-template-columns: repeat(4, 1fr);
      gap: 22px;
      margin-top: 14px;
    }
    @media (max-width: 960px) {
      .story-stage-cards { grid-template-columns: 1fr 1fr; }
    }
    @media (max-width: 600px) {
      .story-stage-cards { grid-template-columns: 1fr; }
    }

    .story-step-item {
      background: rgba(18, 26, 56, 0.8);
      border: 1px solid rgba(255, 255, 255, 0.09);
      border-radius: var(--radius-xl);
      padding: 22px;
      display: flex;
      flex-direction: column;
      gap: 12px;
      transition: all 0.25s cubic-bezier(0.16, 1, 0.3, 1);
      position: relative;
      overflow: hidden;
    }
    .story-step-item:hover {
      border-color: rgba(15, 227, 255, 0.58);
      transform: translateY(-6px);
      box-shadow: 0 16px 36px rgba(15, 227, 255, 0.18);
    }
    .story-step-item::before {
      content: "";
      position: absolute;
      top: 0; left: 0; width: 100%; height: 3px;
      background: linear-gradient(90deg, var(--electric-cyan), var(--electric-violet), var(--magenta-vivid));
    }
    .story-step-label {
      font-family: var(--font-tech);
      font-size: 0.74rem;
      font-weight: 700;
      color: var(--electric-cyan);
      letter-spacing: 0.08em;
      text-transform: uppercase;
    }
    .story-step-title {
      font-family: var(--font-display);
      font-size: 1.12rem;
      font-weight: 700;
      color: var(--soft-white);
    }
    .story-step-desc {
      font-size: 0.84rem;
      color: var(--muted-grey);
      line-height: 1.55;
    }

    /* ==========================================================================
       SECTION 7: ARCHITECTURAL GALLERY SHOWCASE (EDITORIAL ASYMMETRIC GRID)
       ========================================================================== */
    .editorial-gallery-section {
      display: flex;
      flex-direction: column;
      gap: 28px;
    }

    .gallery-showcase-grid {
      display: grid;
      grid-template-columns: repeat(12, 1fr);
      gap: 24px;
    }

    .gallery-hero-card {
      grid-column: span 7;
      position: relative;
      border-radius: var(--radius-2xl);
      overflow: hidden;
      border: 1px solid rgba(255, 255, 255, 0.14);
      background: var(--glass-surface-1);
      box-shadow: 0 20px 50px rgba(0, 0, 0, 0.45);
      transition: all 0.35s cubic-bezier(0.16, 1, 0.3, 1);
      aspect-ratio: 16/10;
      cursor: pointer;
    }
    .gallery-hero-card:hover {
      transform: translateY(-6px);
      border-color: rgba(15, 227, 255, 0.6);
      box-shadow: 0 28px 65px rgba(15, 227, 255, 0.25);
    }

    .gallery-side-card {
      grid-column: span 5;
      position: relative;
      border-radius: var(--radius-2xl);
      overflow: hidden;
      border: 1px solid rgba(255, 255, 255, 0.14);
      background: var(--glass-surface-1);
      box-shadow: 0 20px 50px rgba(0, 0, 0, 0.45);
      transition: all 0.35s cubic-bezier(0.16, 1, 0.3, 1);
      aspect-ratio: 16/10;
      cursor: pointer;
    }
    .gallery-side-card:hover {
      transform: translateY(-6px);
      border-color: rgba(255, 42, 141, 0.6);
      box-shadow: 0 28px 65px rgba(255, 42, 141, 0.25);
    }

    .gallery-bottom-card-1 {
      grid-column: span 4;
      position: relative;
      border-radius: var(--radius-2xl);
      overflow: hidden;
      border: 1px solid rgba(255, 255, 255, 0.14);
      background: var(--glass-surface-1);
      aspect-ratio: 4/3;
      transition: all 0.35s cubic-bezier(0.16, 1, 0.3, 1);
      cursor: pointer;
    }
    .gallery-bottom-card-2 {
      grid-column: span 4;
      position: relative;
      border-radius: var(--radius-2xl);
      overflow: hidden;
      border: 1px solid rgba(255, 255, 255, 0.14);
      background: var(--glass-surface-1);
      aspect-ratio: 4/3;
      transition: all 0.35s cubic-bezier(0.16, 1, 0.3, 1);
      cursor: pointer;
    }
    .gallery-bottom-card-3 {
      grid-column: span 4;
      position: relative;
      border-radius: var(--radius-2xl);
      overflow: hidden;
      border: 1px solid rgba(255, 255, 255, 0.14);
      background: var(--glass-surface-1);
      aspect-ratio: 4/3;
      transition: all 0.35s cubic-bezier(0.16, 1, 0.3, 1);
      cursor: pointer;
    }
    .gallery-bottom-card-1:hover, .gallery-bottom-card-2:hover, .gallery-bottom-card-3:hover {
      transform: translateY(-6px);
      border-color: rgba(142, 68, 255, 0.6);
      box-shadow: 0 24px 55px rgba(142, 68, 255, 0.25);
    }

    @media (max-width: 960px) {
      .gallery-hero-card, .gallery-side-card, .gallery-bottom-card-1, .gallery-bottom-card-2, .gallery-bottom-card-3 {
        grid-column: span 12;
        aspect-ratio: 16/10;
      }
    }

    .gallery-card-img {
      width: 100%;
      height: 100%;
      object-fit: cover;
      display: block;
      transition: transform 0.5s cubic-bezier(0.16, 1, 0.3, 1);
    }
    .gallery-hero-card:hover .gallery-card-img,
    .gallery-side-card:hover .gallery-card-img,
    .gallery-bottom-card-1:hover .gallery-card-img,
    .gallery-bottom-card-2:hover .gallery-card-img,
    .gallery-bottom-card-3:hover .gallery-card-img {
      transform: scale(1.05);
    }

    .gallery-card-overlay {
      position: absolute;
      bottom: 0; left: 0; width: 100%;
      padding: 24px;
      background: linear-gradient(to top, rgba(4, 6, 13, 0.95) 0%, rgba(4, 6, 13, 0.6) 65%, transparent 100%);
      display: flex;
      justify-content: space-between;
      align-items: flex-end;
      z-index: 2;
    }
    .gallery-card-info h3 {
      font-family: var(--font-display);
      font-size: 1.18rem;
      font-weight: 700;
      color: #ffffff;
    }
    .gallery-card-info p {
      font-family: var(--font-tech);
      font-size: 0.74rem;
      color: var(--electric-cyan);
      margin-top: 3px;
    }

    /* ==========================================================================
       SECTION 8: TECHNICAL ARCHITECTURE & LOCAL OFFLINE HARDWARE PIPELINE
       ========================================================================== */
    .technical-specs-section {
      display: flex;
      flex-direction: column;
      gap: 28px;
      padding: 48px;
      background: linear-gradient(135deg, rgba(12, 18, 38, 0.88), rgba(18, 26, 56, 0.78));
      border: 1px solid rgba(255, 255, 255, 0.13);
      border-radius: var(--radius-2xl);
      box-shadow: 0 24px 60px rgba(0, 0, 0, 0.4);
    }

    .specs-grid-3col {
      display: grid;
      grid-template-columns: repeat(3, 1fr);
      gap: 22px;
      margin-top: 14px;
    }
    @media (max-width: 900px) {
      .specs-grid-3col { grid-template-columns: 1fr; }
    }

    .spec-card-box {
      background: rgba(18, 26, 56, 0.8);
      border: 1px solid rgba(255, 255, 255, 0.09);
      border-radius: var(--radius-xl);
      padding: 24px;
      display: flex;
      flex-direction: column;
      gap: 12px;
      position: relative;
    }
    .spec-card-box strong { color: var(--electric-cyan); }
    .spec-val-badge {
      font-family: var(--font-tech);
      font-size: 1.4rem;
      font-weight: 700;
      color: #ffffff;
      background: linear-gradient(135deg, #ffffff, var(--electric-cyan));
      -webkit-background-clip: text;
      -webkit-text-fill-color: transparent;
    }

    /* ==========================================================================
       SECTION 9: CREATIVE STUDIO WORKSPACE
       ========================================================================== */
    .studio-spatial-section {
      display: flex;
      flex-direction: column;
      gap: 26px;
    }

    .studio-workspace-grid {
      display: grid;
      grid-template-columns: 1.05fr 1fr;
      gap: 28px;
      align-items: start;
    }
    @media (max-width: 1160px) {
      .studio-workspace-grid { grid-template-columns: 1fr; }
    }

    /* Spatial Glass Panels */
    .spatial-panel {
      background: var(--glass-surface-1);
      backdrop-filter: blur(24px);
      -webkit-backdrop-filter: blur(24px);
      border: 1px solid rgba(255, 255, 255, 0.12);
      border-radius: var(--radius-2xl);
      padding: 26px;
      display: flex;
      flex-direction: column;
      gap: 22px;
      box-shadow: 0 24px 60px rgba(0, 0, 0, 0.5);
      position: relative;
    }

    .panel-head-spatial {
      display: flex;
      justify-content: space-between;
      align-items: center;
      padding-bottom: 18px;
      border-bottom: 1px solid var(--dark-edge);
    }

    .panel-headline {
      display: flex;
      align-items: center;
      gap: 14px;
    }

    .spatial-orb {
      width: 44px;
      height: 44px;
      border-radius: 14px;
      background: rgba(15, 227, 255, 0.14);
      border: 1px solid rgba(15, 227, 255, 0.45);
      display: flex;
      align-items: center;
      justify-content: center;
      color: var(--electric-cyan);
      box-shadow: 0 0 18px rgba(15, 227, 255, 0.25);
    }

    .panel-title-block h2 {
      font-family: var(--font-display);
      font-size: 1.22rem;
      font-weight: 700;
      color: var(--soft-white);
    }
    .panel-title-block p {
      font-size: 0.82rem;
      color: var(--muted-grey);
    }

    /* Architectural Toolbar */
    .spatial-toolbar {
      display: flex;
      flex-wrap: wrap;
      align-items: center;
      gap: 8px;
      background: var(--glass-surface-2);
      border: 1px solid var(--dark-edge);
      border-radius: var(--radius-lg);
      padding: 8px 12px;
    }

    .tool-group-dock {
      display: flex;
      align-items: center;
      gap: 6px;
      border-right: 1px solid var(--dark-edge);
      padding-right: 10px;
      margin-right: 4px;
    }
    .tool-group-dock:last-child {
      border-right: none;
      padding-right: 0;
      margin-right: 0;
    }

    .btn-spatial-tool {
      background: rgba(255, 255, 255, 0.05);
      border: 1px solid var(--dark-edge);
      color: var(--muted-grey);
      width: 36px;
      height: 36px;
      border-radius: 9px;
      cursor: pointer;
      display: flex;
      align-items: center;
      justify-content: center;
      transition: all 0.18s ease;
      position: relative;
    }
    .btn-spatial-tool:hover {
      background: rgba(255, 255, 255, 0.12);
      color: #fff;
      border-color: rgba(15, 227, 255, 0.5);
    }
    .btn-spatial-tool.active {
      background: linear-gradient(135deg, rgba(15, 227, 255, 0.35), rgba(142, 68, 255, 0.4));
      color: #fff;
      border-color: var(--electric-cyan);
      box-shadow: 0 0 16px rgba(15, 227, 255, 0.4);
    }
    .btn-spatial-tool:disabled {
      opacity: 0.25;
      cursor: not-allowed;
    }

    .slider-pillbox {
      display: flex;
      align-items: center;
      gap: 8px;
      font-size: 0.76rem;
      font-weight: 600;
      color: var(--muted-grey);
    }
    .spatial-range {
      width: 70px;
      accent-color: var(--electric-cyan);
      cursor: pointer;
    }
    .tech-badge {
      font-family: var(--font-tech);
      font-size: 0.74rem;
      color: var(--electric-cyan);
      min-width: 28px;
    }

    .ink-orb {
      width: 22px;
      height: 22px;
      border-radius: 50%;
      border: 2px solid transparent;
      box-shadow: 0 0 0 1px var(--dark-edge);
      cursor: pointer;
      transition: transform 0.18s ease;
    }
    .ink-orb:hover { transform: scale(1.2); }
    .ink-orb.active { border-color: var(--electric-cyan); box-shadow: 0 0 14px var(--electric-cyan); transform: scale(1.2); }

    /* Interactive HTML5 Canvas Viewport */
    .spatial-canvas-viewport {
      position: relative;
      width: 100%;
      aspect-ratio: 1;
      max-width: 512px;
      margin: 0 auto;
      border-radius: var(--radius-xl);
      overflow: hidden;
      border: 1px solid rgba(15, 227, 255, 0.48);
      background: #ffffff;
      box-shadow: 0 0 45px rgba(15, 227, 255, 0.25);
      user-select: none;
    }

    #drawing-canvas {
      width: 100%;
      height: 100%;
      display: block;
      cursor: crosshair;
      touch-action: none;
      transform-origin: 0 0;
      transition: transform 0.05s ease-out;
    }

    #grid-canvas {
      position: absolute;
      top: 0; left: 0;
      width: 100%; height: 100%;
      pointer-events: none;
      display: none;
    }

    .hud-spatial-hint {
      position: absolute;
      bottom: 14px;
      left: 50%;
      transform: translateX(-50%);
      background: rgba(8, 12, 27, 0.9);
      backdrop-filter: blur(10px);
      border: 1px solid rgba(15, 227, 255, 0.45);
      color: var(--electric-cyan);
      padding: 6px 18px;
      border-radius: var(--radius-pill);
      font-size: 0.72rem;
      font-family: var(--font-tech);
      font-weight: 600;
      pointer-events: none;
      transition: opacity 0.3s;
    }

    /* Architectural Layout Presets */
    .layout-presets-deck {
      display: flex;
      flex-direction: column;
      gap: 10px;
    }
    .deck-header {
      display: flex;
      justify-content: space-between;
      align-items: center;
      font-family: var(--font-tech);
      font-size: 0.74rem;
      font-weight: 700;
      color: var(--muted-grey);
      text-transform: uppercase;
      letter-spacing: 0.05em;
    }
    .deck-scroll-row {
      display: flex;
      gap: 8px;
      overflow-x: auto;
      padding-bottom: 3px;
    }
    .layout-chip {
      background: var(--glass-surface-2);
      border: 1px solid var(--dark-edge);
      color: var(--muted-grey);
      padding: 8px 16px;
      border-radius: var(--radius-md);
      font-size: 0.78rem;
      font-weight: 600;
      cursor: pointer;
      white-space: nowrap;
      transition: all 0.2s ease;
    }
    .layout-chip:hover {
      background: rgba(28, 38, 76, 0.9);
      color: #fff;
      border-color: rgba(15, 227, 255, 0.5);
    }
    .layout-chip.active {
      background: linear-gradient(135deg, rgba(15, 227, 255, 0.3), rgba(142, 68, 255, 0.35));
      color: #fff;
      border-color: var(--electric-cyan);
      box-shadow: 0 0 16px rgba(15, 227, 255, 0.3);
    }

    /* Spatial Parameter Matrix */
    .spatial-params-matrix {
      background: var(--glass-surface-2);
      border: 1px solid var(--dark-edge);
      border-radius: var(--radius-xl);
      padding: 22px;
      display: flex;
      flex-direction: column;
      gap: 18px;
    }

    .matrix-2col {
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 16px;
    }
    @media (max-width: 640px) {
      .matrix-2col { grid-template-columns: 1fr; }
    }

    .spatial-field {
      display: flex;
      flex-direction: column;
      gap: 6px;
    }
    .field-caption {
      font-family: var(--font-tech);
      font-size: 0.74rem;
      font-weight: 600;
      color: var(--electric-cyan);
      text-transform: uppercase;
      letter-spacing: 0.05em;
      display: flex;
      justify-content: space-between;
    }

    .spatial-select, .spatial-input, .spatial-textarea {
      background: rgba(11, 16, 36, 0.94);
      border: 1px solid var(--dark-edge);
      color: var(--soft-white);
      border-radius: var(--radius-md);
      padding: 11px 15px;
      font-family: var(--font-body);
      font-size: 0.86rem;
      outline: none;
      transition: border-color 0.2s, box-shadow 0.2s;
    }
    .spatial-select:focus, .spatial-input:focus, .spatial-textarea:focus {
      border-color: var(--electric-cyan);
      box-shadow: 0 0 16px rgba(15, 227, 255, 0.35);
    }

    .spatial-textarea {
      resize: vertical;
      min-height: 54px;
      line-height: 1.5;
      font-size: 0.82rem;
    }

    /* Engine Stack */
    .engine-stack {
      display: flex;
      flex-direction: column;
      gap: 10px;
    }
    .engine-choice-card {
      background: rgba(11, 16, 36, 0.8);
      border: 1px solid var(--dark-edge);
      border-radius: var(--radius-lg);
      padding: 14px 18px;
      display: flex;
      align-items: flex-start;
      gap: 14px;
      cursor: pointer;
      transition: all 0.2s ease;
    }
    .engine-choice-card:hover {
      background: rgba(22, 32, 68, 0.9);
      border-color: rgba(15, 227, 255, 0.48);
    }
    .engine-choice-card.active {
      background: linear-gradient(135deg, rgba(15, 227, 255, 0.18), rgba(142, 68, 255, 0.25));
      border-color: var(--electric-cyan);
      box-shadow: 0 0 20px rgba(15, 227, 255, 0.28);
    }
    .engine-choice-card input[type="radio"] {
      accent-color: var(--electric-cyan);
      margin-top: 3px;
    }
    .engine-card-text { flex: 1; }
    .engine-title-row {
      display: flex;
      align-items: center;
      gap: 10px;
      font-family: var(--font-display);
      font-size: 0.94rem;
      font-weight: 700;
      color: #fff;
    }
    .engine-tag {
      font-family: var(--font-tech);
      font-size: 0.65rem;
      font-weight: 700;
      padding: 2px 8px;
      border-radius: 6px;
      text-transform: uppercase;
      letter-spacing: 0.05em;
    }
    .engine-tag.primary {
      background: rgba(15, 227, 255, 0.2);
      color: var(--electric-cyan);
      border: 1px solid rgba(15, 227, 255, 0.45);
    }
    .engine-tag.exp {
      background: rgba(255, 181, 46, 0.16);
      color: var(--amber-warm);
      border: 1px solid rgba(255, 181, 46, 0.38);
    }
    .engine-sub-desc {
      font-size: 0.76rem;
      color: var(--muted-grey);
      margin-top: 4px;
      line-height: 1.45;
    }

    /* Fine Tuning Drawer */
    .fine-tune-accordion {
      font-family: var(--font-tech);
      font-size: 0.78rem;
      font-weight: 600;
      color: var(--electric-cyan);
      cursor: pointer;
      display: flex;
      align-items: center;
      gap: 8px;
      user-select: none;
      padding-top: 4px;
    }
    .fine-tune-accordion:hover { color: #fff; }
    .fine-tune-drawer {
      display: none;
      grid-template-columns: 1fr 1fr 1fr;
      gap: 12px;
      padding-top: 12px;
    }

    /* Primary Generate Button */
    .btn-synthesize-master {
      background: linear-gradient(135deg, var(--electric-cyan) 0%, var(--electric-violet) 50%, var(--magenta-vivid) 100%);
      color: var(--obsidian);
      font-family: var(--font-display);
      border: none;
      padding: 17px 30px;
      border-radius: var(--radius-lg);
      font-size: 1.04rem;
      font-weight: 700;
      cursor: pointer;
      display: flex;
      align-items: center;
      justify-content: center;
      gap: 12px;
      box-shadow: 0 0 34px rgba(15, 227, 255, 0.48);
      transition: all 0.22s cubic-bezier(0.16, 1, 0.3, 1);
    }
    .btn-synthesize-master:hover:not(:disabled) {
      transform: translateY(-2px);
      box-shadow: 0 0 48px rgba(255, 42, 141, 0.65);
    }
    .btn-synthesize-master:disabled {
      opacity: 0.45;
      cursor: not-allowed;
      transform: none;
      box-shadow: none;
    }

    /* ==========================================================================
       SECTION 10: RIGHT VIEWPORT: VISUALIZER & COMPARISON CURTAIN
       ========================================================================== */
    .spatial-visualizer-stage {
      position: relative;
      width: 100%;
      aspect-ratio: 1;
      max-width: 512px;
      margin: 0 auto;
      border-radius: var(--radius-xl);
      overflow: hidden;
      border: 1px solid rgba(142, 68, 255, 0.48);
      background: #060914;
      display: flex;
      align-items: center;
      justify-content: center;
      box-shadow: 0 0 44px rgba(142, 68, 255, 0.24);
    }

    .spatial-visualizer-stage img {
      width: 100%;
      height: 100%;
      object-fit: cover;
      display: none;
      animation: spatialFadeIn 0.45s ease-out;
    }
    @keyframes spatialFadeIn {
      from { opacity: 0; transform: scale(0.97); }
      to { opacity: 1; transform: scale(1); }
    }

    .visualizer-empty-hud {
      color: var(--muted-grey);
      font-size: 0.88rem;
      text-align: center;
      padding: 34px;
      line-height: 1.6;
    }
    .visualizer-empty-hud strong {
      color: var(--electric-cyan);
    }

    /* Draggable Before/After Comparison Curtain */
    .spatial-compare-box {
      display: none;
      position: relative;
      width: 100%;
      height: 100%;
      overflow: hidden;
      cursor: ew-resize;
      user-select: none;
    }
    .compare-bottom-layer {
      position: absolute;
      top: 0; left: 0;
      width: 100%; height: 100%;
      object-fit: cover;
    }
    .compare-top-curtain {
      position: absolute;
      top: 0; left: 0;
      width: 50%; height: 100%;
      overflow: hidden;
      border-right: 2px solid var(--electric-cyan);
      box-shadow: 2px 0 16px var(--electric-cyan);
    }
    .compare-top-curtain img {
      position: absolute;
      top: 0; left: 0;
      width: 512px; height: 512px;
      object-fit: cover;
      display: block;
    }
    .compare-spatial-handle {
      position: absolute;
      top: 50%; right: -16px;
      transform: translateY(-50%);
      width: 32px; height: 32px;
      border-radius: 50%;
      background: var(--obsidian);
      border: 2px solid var(--electric-cyan);
      color: var(--electric-cyan);
      display: flex;
      align-items: center;
      justify-content: center;
      font-size: 14px;
      font-weight: bold;
      box-shadow: 0 0 16px var(--electric-cyan);
      pointer-events: none;
    }

    /* Error Overlay */
    .spatial-error-drawer {
      display: none;
      position: absolute;
      top: 0; left: 0; width: 100%; height: 100%;
      background: rgba(8, 12, 27, 0.94);
      backdrop-filter: blur(14px);
      flex-direction: column;
      align-items: center;
      justify-content: center;
      padding: 32px;
      text-align: center;
      gap: 16px;
      z-index: 10;
    }
    .error-hex-icon {
      width: 52px; height: 52px;
      border-radius: 14px;
      background: rgba(239, 68, 68, 0.16);
      border: 1px solid rgba(239, 68, 68, 0.5);
      color: #f87171;
      display: flex;
      align-items: center;
      justify-content: center;
      box-shadow: 0 0 20px rgba(239, 68, 68, 0.3);
    }
    .btn-spatial-retry {
      background: rgba(239, 68, 68, 0.22);
      border: 1px solid #f87171;
      color: #ffffff;
      padding: 10px 22px;
      border-radius: var(--radius-md);
      font-family: var(--font-tech);
      font-size: 0.82rem;
      cursor: pointer;
      display: flex;
      align-items: center;
      gap: 8px;
      transition: all 0.2s;
    }
    .btn-spatial-retry:hover {
      background: rgba(239, 68, 68, 0.4);
    }

    /* Multi-Stage Generation Sequence Overlay */
    .spatial-synthesis-overlay {
      display: none;
      position: absolute;
      top: 0; left: 0; width: 100%; height: 100%;
      background: rgba(8, 12, 27, 0.94);
      backdrop-filter: blur(16px);
      flex-direction: column;
      align-items: center;
      justify-content: center;
      gap: 20px;
      z-index: 10;
      padding: 32px;
      text-align: center;
    }
    .spatial-gyro-spinner {
      width: 60px; height: 60px;
      border: 3px solid rgba(15, 227, 255, 0.18);
      border-top-color: var(--electric-cyan);
      border-right-color: var(--magenta-vivid);
      border-radius: 50%;
      animation: spinSpatialGyro 1s linear infinite;
      box-shadow: 0 0 30px rgba(15, 227, 255, 0.4);
    }
    @keyframes spinSpatialGyro {
      to { transform: rotate(360deg); }
    }
    .stage-sequence-text {
      font-family: var(--font-display);
      font-size: 1.05rem;
      font-weight: 700;
      color: #ffffff;
    }
    .stage-sub-text {
      font-family: var(--font-tech);
      font-size: 0.74rem;
      color: var(--muted-grey);
      margin-top: 4px;
    }
    .elapsed-hud-tag {
      font-family: var(--font-tech);
      font-size: 0.8rem;
      color: var(--electric-cyan);
      background: rgba(15, 227, 255, 0.12);
      border: 1px solid rgba(15, 227, 255, 0.4);
      padding: 5px 14px;
      border-radius: var(--radius-pill);
    }

    /* Viewport Dock Actions */
    .visualizer-dock-row {
      display: flex;
      justify-content: space-between;
      align-items: center;
      flex-wrap: wrap;
      gap: 12px;
    }
    .btn-spatial-dock {
      background: rgba(18, 26, 56, 0.85);
      border: 1px solid var(--dark-edge);
      color: var(--soft-white);
      padding: 10px 18px;
      border-radius: var(--radius-md);
      font-family: var(--font-body);
      font-size: 0.84rem;
      font-weight: 600;
      cursor: pointer;
      display: flex;
      align-items: center;
      gap: 8px;
      transition: all 0.2s ease;
    }
    .btn-spatial-dock:hover:not(:disabled) {
      background: rgba(28, 40, 84, 0.95);
      border-color: rgba(15, 227, 255, 0.5);
      box-shadow: 0 0 16px rgba(15, 227, 255, 0.2);
    }
    .btn-spatial-dock:disabled {
      opacity: 0.35;
      cursor: not-allowed;
    }

    /* Telemetry HUD */
    .spatial-telemetry-hud {
      display: flex;
      align-items: center;
      gap: 8px;
      flex-wrap: wrap;
    }
    .telemetry-chip {
      background: rgba(8, 12, 27, 0.85);
      border: 1px solid var(--dark-edge);
      color: var(--muted-grey);
      font-family: var(--font-tech);
      font-size: 0.72rem;
      padding: 5px 12px;
      border-radius: var(--radius-sm);
      display: inline-flex;
      align-items: center;
      gap: 6px;
    }
    .telemetry-chip strong { color: var(--electric-cyan); }

    /* ==========================================================================
       SECTION 11: MY DESIGNS & PRESENTATION MODE
       ========================================================================== */
    .gallery-spatial-section {
      display: none;
      flex-direction: column;
      gap: 26px;
    }

    .gallery-collection-grid {
      display: grid;
      grid-template-columns: repeat(auto-fill, minmax(300px, 1fr));
      gap: 26px;
    }

    .spatial-project-card {
      background: var(--glass-surface-2);
      border: 1px solid var(--dark-edge);
      border-radius: var(--radius-xl);
      overflow: hidden;
      backdrop-filter: blur(16px);
      transition: all 0.3s cubic-bezier(0.16, 1, 0.3, 1);
      display: flex;
      flex-direction: column;
    }
    .spatial-project-card:hover {
      transform: translateY(-6px);
      border-color: rgba(15, 227, 255, 0.55);
      box-shadow: 0 18px 40px rgba(15, 227, 255, 0.2);
    }
    .spatial-project-thumb {
      width: 100%;
      aspect-ratio: 1;
      object-fit: cover;
      background: #090e20;
      display: block;
    }
    .spatial-project-body {
      padding: 18px;
      display: flex;
      flex-direction: column;
      gap: 10px;
    }
    .spatial-project-name {
      font-family: var(--font-display);
      font-size: 1rem;
      font-weight: 700;
      color: #fff;
    }
    .spatial-project-meta {
      font-family: var(--font-tech);
      font-size: 0.74rem;
      color: var(--muted-grey);
    }
    .spatial-project-actions {
      display: flex;
      gap: 8px;
      margin-top: 6px;
    }
    .btn-spatial-mini {
      flex: 1;
      background: rgba(255, 255, 255, 0.05);
      border: 1px solid var(--dark-edge);
      color: #fff;
      padding: 8px 14px;
      border-radius: var(--radius-sm);
      font-size: 0.78rem;
      font-weight: 600;
      cursor: pointer;
      transition: all 0.18s;
    }
    .btn-spatial-mini:hover {
      background: rgba(15, 227, 255, 0.22);
      border-color: var(--electric-cyan);
    }
    .btn-spatial-mini.delete-btn:hover {
      background: rgba(239, 68, 68, 0.2);
      border-color: #f87171;
      color: #f87171;
    }

    /* Modal Backdrop */
    .spatial-modal-curtain {
      display: none;
      position: fixed;
      top: 0; left: 0; width: 100vw; height: 100vh;
      background: rgba(6, 9, 22, 0.9);
      backdrop-filter: blur(16px);
      z-index: 1000;
      align-items: center;
      justify-content: center;
      padding: 24px;
    }
    .spatial-modal-window {
      background: var(--glass-surface-1);
      border: 1px solid rgba(15, 227, 255, 0.45);
      border-radius: var(--radius-2xl);
      padding: 30px;
      max-width: 450px;
      width: 100%;
      box-shadow: 0 28px 70px rgba(0, 0, 0, 0.65);
      display: flex;
      flex-direction: column;
      gap: 20px;
    }

    /* Fullscreen Academic Presentation Mode */
    .presentation-fullscreen-curtain {
      display: none;
      position: fixed;
      top: 0; left: 0; width: 100vw; height: 100vh;
      background: var(--obsidian);
      z-index: 9999;
      padding: 44px;
      flex-direction: column;
      gap: 24px;
      overflow-y: auto;
    }
    .pres-header-bar {
      display: flex;
      justify-content: space-between;
      align-items: center;
      border-bottom: 1px solid var(--dark-edge);
      padding-bottom: 18px;
    }
    .pres-view-split {
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 36px;
      flex: 1;
      align-items: center;
    }
    @media (max-width: 900px) {
      .pres-view-split { grid-template-columns: 1fr; }
    }
    .pres-card-box {
      display: flex;
      flex-direction: column;
      gap: 14px;
      text-align: center;
    }
    .pres-card-box img {
      width: 100%;
      max-width: 580px;
      aspect-ratio: 1;
      object-fit: cover;
      border-radius: var(--radius-xl);
      margin: 0 auto;
      border: 1px solid var(--dark-edge);
      box-shadow: 0 20px 50px rgba(0, 0, 0, 0.5);
    }

    /* Toast Notification */
    .spatial-toast {
      position: fixed;
      bottom: 30px;
      right: 30px;
      z-index: 1000;
      background: rgba(12, 18, 42, 0.96);
      backdrop-filter: blur(16px);
      border: 1px solid rgba(15, 227, 255, 0.55);
      color: #fff;
      padding: 15px 26px;
      border-radius: var(--radius-md);
      box-shadow: 0 16px 40px rgba(0,0,0,0.5);
      display: none;
      align-items: center;
      gap: 12px;
      font-size: 0.88rem;
      animation: toastGlideUp 0.3s ease-out;
    }
    @keyframes toastGlideUp {
      from { transform: translateY(20px); opacity: 0; }
      to { transform: translateY(0); opacity: 1; }
    }

    footer {
      margin-top: auto;
      padding: 32px 44px;
      border-top: 1px solid var(--dark-edge);
      display: flex;
      justify-content: space-between;
      align-items: center;
      flex-wrap: wrap;
      gap: 16px;
      font-size: 0.82rem;
      color: var(--muted-grey);
      background: rgba(6, 9, 20, 0.6);
      backdrop-filter: blur(12px);
    }

    /* Respect User Reduced Motion Preferences */
    @media (prefers-reduced-motion: reduce) {
      *, ::before, ::after {
        animation-duration: 0.01ms !important;
        animation-iteration-count: 1 !important;
        transition-duration: 0.01ms !important;
        scroll-behavior: auto !important;
      }
    }
  </style>
</head>
<body>
  <!-- ========================================================================
       MULTICOLOUR AURORA LIGHTFIELDS, VOLUMETRIC RIBBONS & 3D SCULPTURES
       ======================================================================== -->
  <div class="aurora-universe">
    <div class="aurora-sphere aurora-1"></div>
    <div class="aurora-sphere aurora-2"></div>
    <div class="aurora-sphere aurora-3"></div>
    <div class="aurora-sphere aurora-4"></div>
    <div class="aurora-sphere aurora-5"></div>
    <div class="aurora-ribbon"></div>
  </div>

  <div class="spatial-grid-floor"></div>
  <canvas id="ambient-particles-canvas"></canvas>

  <div class="floating-sculptures-layer">
    <!-- Sculpture 1: Left Wireframe Prism -->
    <div class="sculpture-prism sculpture-1">
      <div class="glass-plane" style="transform: rotateX(45deg);"></div>
      <div class="glass-plane" style="transform: rotateY(45deg);"></div>
    </div>
    <!-- Sculpture 2: Right Glass Room Structure -->
    <div class="sculpture-prism sculpture-2">
      <div class="glass-plane" style="transform: rotateX(30deg) rotateZ(15deg);"></div>
      <div class="glass-plane" style="transform: rotateY(60deg);"></div>
    </div>
    <!-- Sculpture 3: Upper Floating Coordinate Cube -->
    <div class="sculpture-prism sculpture-3">
      <div class="glass-plane" style="transform: rotateX(60deg);"></div>
    </div>
    <!-- Sculpture 4: Lower Floating Isometric Prism -->
    <div class="sculpture-prism sculpture-4">
      <div class="glass-plane" style="transform: rotateY(45deg) rotateZ(30deg);"></div>
    </div>
  </div>

  <!-- Top Spatial Navigation -->
  <header class="spatial-nav">
    <div class="spatial-brand" onclick="switchSpatialNav('landing')">
      <!-- Original Custom Geometric Architectural Isometric Logo -->
      <div class="brand-cube-badge">
        <svg width="28" height="28" viewBox="0 0 28 28" fill="none" xmlns="http://www.w3.org/2000/svg">
          <path d="M14 2L26 8.5V21.5L14 28L2 21.5V8.5L14 2Z" stroke="#0FE3FF" stroke-width="2" stroke-linejoin="round"/>
          <path d="M14 28V15" stroke="#0FE3FF" stroke-width="2"/>
          <path d="M26 8.5L14 15L2 8.5" stroke="#0FE3FF" stroke-width="2"/>
          <path d="M8 5L20 11.5" stroke="#8E44FF" stroke-width="2" stroke-linecap="round"/>
          <path d="M20 18L14 21.5" stroke="#FF2A8D" stroke-width="2" stroke-linecap="round"/>
        </svg>
      </div>
      <div class="brand-text-lockup">
        <h1>SketchSpace AI</h1>
        <p>Spatial Architectural Synthesis</p>
      </div>
    </div>

    <!-- Navigation Tabs -->
    <div class="spatial-nav-tabs">
      <button type="button" class="nav-link-btn active" id="tab-nav-landing" onclick="switchSpatialNav('landing')">
        <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="m3 9 9-7 9 7v11a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2z"></path></svg>
        Overview
      </button>
      <button type="button" class="nav-link-btn" id="tab-nav-studio" onclick="switchSpatialNav('studio')">
        <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polygon points="12 2 15.09 8.26 22 9.27 17 14.14 18.18 21.02 12 17.77 5.82 21.02 7 14.14 2 9.27 8.91 8.26 12 2"></polygon></svg>
        Creative Studio
      </button>
      <button type="button" class="nav-link-btn" id="tab-nav-gallery" onclick="switchSpatialNav('gallery')">
        <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="3" y="3" width="18" height="18" rx="2" ry="2"></rect><circle cx="8.5" cy="8.5" r="1.5"></circle><polyline points="21 15 16 10 5 21"></polyline></svg>
        My Designs
      </button>
    </div>

    <div style="display:flex; align-items:center; gap:14px;">
      <button type="button" class="btn-presentation-pill" onclick="openPresentationMode()">
        <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polygon points="5 3 19 12 5 21 5 3"></polygon></svg>
        Presentation Mode
      </button>
      <div class="engine-status-tag">
        <div class="beacon-pulse"></div>
        <span>RTX 3050 &bull; 100% Offline</span>
      </div>
    </div>
  </header>

  <!-- Main Viewport Shell -->
  <main class="main-spatial-container">

    <!-- ====================================================================
         SECTION 1: CINEMATIC MULTICOLOUR HERO WITH LARGE 3D SPATIAL ROOM
         ==================================================================== -->
    <section class="hero-spatial-section" id="section-landing">
      <div class="hero-editorial-left">
        <div class="hero-tagline-badge">Spatial Neural Studio</div>
        <h2 class="hero-editorial-headline">From Freehand Line<br>To Spatial Reality.</h2>
        <p class="hero-editorial-lead">
          Transform architectural line sketches into photorealistic interior realities using 100% offline local generative AI.
          Powered by Stable Diffusion 1.5 + ControlNet Scribble running securely on your NVIDIA GeForce RTX 3050.
        </p>

        <div class="hero-cta-cluster">
          <button type="button" class="btn-spatial-primary" onclick="switchSpatialNav('studio')">
            <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2"><path d="M12 20h9"></path><path d="M16.5 3.5a2.121 2.121 0 0 1 3 3L7 19l-4 1 1-4L16.5 3.5z"></path></svg>
            Launch Creative Studio
          </button>
          <button type="button" class="btn-spatial-secondary" onclick="scrollToSignatureStory()">
            <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"></circle><polygon points="10 8 16 12 10 16 10 8"></polygon></svg>
            Explore Pipeline
          </button>
        </div>

        <div class="hero-micro-metrics">
          <span><strong>0%</strong> Cloud Latency</span>
          <span>&bull;</span>
          <span><strong>&lt; 1 GB</strong> VRAM Footprint</span>
          <span>&bull;</span>
          <span><strong>FP16</strong> Precision</span>
          <span>&bull;</span>
          <span><strong>512&times;512</strong> High Resolution</span>
        </div>
      </div>

      <!-- Large Interactive 3D Architectural Room Environment with Cursor Parallax -->
      <div class="hero-spatial-stage-right" id="hero-interactive-stage">
        <div class="spatial-dim-badge">DIM: 512 &times; 512 FP16</div>
        <div class="large-room-3d" id="hero-room-3d">
          <div class="room-wall-panel front">
            <div class="wall-window-frame"></div>
          </div>
          <div class="room-wall-panel back"></div>
          <div class="room-wall-panel right"></div>
          <div class="room-wall-panel left"></div>
          <div class="room-wall-panel ceiling"></div>
          <div class="room-wall-panel floor">
            <div class="furniture-cube"></div>
          </div>

          <!-- Floating Material Palette Annotations -->
          <div class="floating-material-sample sample-1">MAT: Oak &amp; Glass</div>
          <div class="floating-material-sample sample-2">LIGHT: Natural Daylight</div>
        </div>
      </div>
    </section>

    <!-- ====================================================================
         SIGNATURE SKETCH-TO-REALITY STORYTELLING
         ==================================================================== -->
    <section class="sketch-to-reality-showcase" id="section-storytelling">
      <div class="story-header-row">
        <div>
          <span style="font-family:var(--font-tech); font-size:0.76rem; color:var(--electric-cyan); text-transform:uppercase; letter-spacing:0.06em;">Signature Spatial Pipeline</span>
          <h2 style="font-family:var(--font-display); font-size:1.85rem; font-weight:700; color:#fff; margin-top:4px;">From Linework to Architectural Photorealism</h2>
        </div>
        <p style="font-size:0.86rem; color:var(--muted-grey); max-width:480px; line-height:1.5;">
          SketchSpace AI bridges the gap between hand-drawn spatial ideation and photorealistic visualization through zero-cloud diffusion.
        </p>
      </div>

      <div class="story-stage-cards">
        <div class="story-step-item">
          <span class="story-step-label">Stage 1 &bull; Draw</span>
          <h3 class="story-step-title">Hand-Drawn Sketch</h3>
          <p class="story-step-desc">Freehand drafting of walls, window apertures, and furniture bounding wireframes on the HTML5 canvas.</p>
        </div>
        <div class="story-step-item">
          <span class="story-step-label">Stage 2 &bull; Interpret</span>
          <h3 class="story-step-title">Spatial Linework</h3>
          <p class="story-step-desc">ControlNet Scribble conditions on boundary strokes, locking room geometry without hallucinated shifts.</p>
        </div>
        <div class="story-step-item">
          <span class="story-step-label">Stage 3 &bull; Transform</span>
          <h3 class="story-step-title">Neural Diffusion</h3>
          <p class="story-step-desc">Stable Diffusion 1.5 infuses authentic textures, daylight illumination, and materials on the RTX 3050.</p>
        </div>
        <div class="story-step-item">
          <span class="story-step-label">Stage 4 &bull; Experience</span>
          <h3 class="story-step-title">Photorealistic Space</h3>
          <p class="story-step-desc">A polished 512×512 interior render ready for client presentation and before/after inspection.</p>
        </div>
      </div>
    </section>

    <!-- ====================================================================
         EDITORIAL ARCHITECTURAL GALLERY SHOWCASE
         ==================================================================== -->
    <section class="editorial-gallery-section" id="section-gallery-showcase">
      <div style="display:flex; justify-content:space-between; align-items:flex-end; flex-wrap:wrap; gap:16px;">
        <div>
          <span style="font-family:var(--font-tech); font-size:0.76rem; color:var(--magenta-vivid); text-transform:uppercase; letter-spacing:0.06em;">Synthesized Case Studies</span>
          <h2 style="font-family:var(--font-display); font-size:1.85rem; font-weight:700; color:#fff; margin-top:4px;">Verified Local Interior Outputs</h2>
        </div>
        <p style="font-size:0.86rem; color:var(--muted-grey); max-width:440px; line-height:1.5;">
          Genuine outputs synthesized locally with ControlNet Scribble + Stable Diffusion 1.5 under 1 GB VRAM.
        </p>
      </div>

      <div class="gallery-showcase-grid">
        <!-- Hero Showcase Card: Living Room -->
        <div class="gallery-hero-card" onclick="loadAndOpenPreset('living_room')">
          <img src="/api/image/local_cn_living_room_1795536539194.png" class="gallery-card-img" alt="Contemporary Living Room" onerror="this.src='/api/sketches/example/new_living_room_sketch.png'">
          <div class="gallery-card-overlay">
            <div class="gallery-card-info">
              <h3>Contemporary Living Room</h3>
              <p>Natural Daylight &bull; Hardwood &amp; Linen &bull; 28.9s Latency</p>
            </div>
            <button type="button" class="btn-spatial-mini" style="width:auto; padding:6px 16px; background:rgba(15, 227, 255, 0.25); border-color:var(--electric-cyan);">Open in Studio</button>
          </div>
        </div>

        <!-- Side Showcase Card: Luxury Spa Bathroom -->
        <div class="gallery-side-card" onclick="loadAndOpenPreset('bathroom')">
          <img src="/api/image/local_cn_bathroom_1795532521076.png" class="gallery-card-img" alt="Spa Bathroom" onerror="this.src='/api/sketches/example/new_bathroom_sketch.png'">
          <div class="gallery-card-overlay">
            <div class="gallery-card-info">
              <h3>Spa Bathroom Suite</h3>
              <p>Porcelain &bull; Chrome Fixtures &bull; 22.4s Latency</p>
            </div>
            <button type="button" class="btn-spatial-mini" style="width:auto; padding:6px 16px; background:rgba(255, 42, 141, 0.25); border-color:var(--magenta-vivid);">Open in Studio</button>
          </div>
        </div>

        <!-- Bottom Trio Card 1: Master Bedroom Suite -->
        <div class="gallery-bottom-card-1" onclick="loadAndOpenPreset('bedroom')">
          <img src="/api/image/local_cn_bedroom_1795531503385.png" class="gallery-card-img" alt="Master Bedroom" onerror="this.src='/api/sketches/example/new_bedroom_sketch.png'">
          <div class="gallery-card-overlay">
            <div class="gallery-card-info">
              <h3>Master Bedroom</h3>
              <p>Modern Minimalist &bull; Natural Light</p>
            </div>
          </div>
        </div>

        <!-- Bottom Trio Card 2: Executive Home Office -->
        <div class="gallery-bottom-card-2" onclick="loadAndOpenPreset('office')">
          <img src="/api/image/local_cn_office_1795531733794.png" class="gallery-card-img" alt="Executive Office" onerror="this.src='/api/sketches/example/new_office_sketch.png'">
          <div class="gallery-card-overlay">
            <div class="gallery-card-info">
              <h3>Executive Office</h3>
              <p>Bleached Oak &bull; Recessed Illumination</p>
            </div>
          </div>
        </div>

        <!-- Bottom Trio Card 3: Gourmet Kitchen -->
        <div class="gallery-bottom-card-3" onclick="loadAndOpenPreset('kitchen')">
          <img src="/api/sketches/example/new_kitchen_sketch.png" class="gallery-card-img" alt="Gourmet Kitchen Blueprint">
          <div class="gallery-card-overlay">
            <div class="gallery-card-info">
              <h3>Gourmet Kitchen Blueprint</h3>
              <p>Calacatta Marble &bull; Draft Line Matrix</p>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- ====================================================================
         SECTION: TECHNICAL ENGINE ARCHITECTURE & HARDWARE TELEMETRY
         ==================================================================== -->
    <section class="technical-specs-section">
      <div style="display:flex; justify-content:space-between; align-items:flex-end; flex-wrap:wrap; gap:16px;">
        <div>
          <span style="font-family:var(--font-tech); font-size:0.76rem; color:var(--teal-luminous); text-transform:uppercase; letter-spacing:0.06em;">Local Hardware Engineering</span>
          <h2 style="font-family:var(--font-display); font-size:1.85rem; font-weight:700; color:#fff; margin-top:4px;">NVIDIA RTX 3050 Architecture Protection</h2>
        </div>
        <p style="font-size:0.86rem; color:var(--muted-grey); max-width:440px; line-height:1.5;">
          Custom sequential CPU offloading and VAE tiling keep local inference strictly capped below 1 GB VRAM.
        </p>
      </div>

      <div class="specs-grid-3col">
        <div class="spec-card-box">
          <span style="font-family:var(--font-tech); font-size:0.75rem; color:var(--muted-grey);">PEAK VRAM ALLOCATION</span>
          <div class="spec-val-badge">649.8 MB</div>
          <p style="font-size:0.82rem; color:var(--muted-grey); line-height:1.5;">
            Sequential layer-by-layer offload streams PyTorch UNet weights between host RAM and GPU VRAM, preventing OOM crashes on 4 GB laptop GPUs.
          </p>
        </div>
        <div class="spec-card-box">
          <span style="font-family:var(--font-tech); font-size:0.75rem; color:var(--muted-grey);">CONTROLNET CONDITIONING</span>
          <div class="spec-val-badge">100% Scribble</div>
          <p style="font-size:0.82rem; color:var(--muted-grey); line-height:1.5;">
            Conditioning tensors lock architectural wall boundaries, window positions, and perspective vectors to eliminate hallucinated layout distortions.
          </p>
        </div>
        <div class="spec-card-box">
          <span style="font-family:var(--font-tech); font-size:0.75rem; color:var(--muted-grey);">OFFLINE SECURITY</span>
          <div class="spec-val-badge">Zero Cloud API</div>
          <p style="font-size:0.82rem; color:var(--muted-grey); line-height:1.5;">
            Local snapshot loading (<code style="color:var(--electric-cyan);">local_files_only=True</code>) guarantees complete client blueprint privacy with zero third-party data transmission.
          </p>
        </div>
      </div>
    </section>

    <!-- ====================================================================
         CREATIVE STUDIO WORKSPACE
         ==================================================================== -->
    <section class="studio-spatial-section" id="section-studio" style="display:none;">
      <div class="studio-workspace-grid">

        <!-- LEFT WORKSPACE: ADVANCED SKETCH EDITOR & CONTROLS -->
        <div class="spatial-panel">
          <div class="panel-head-spatial">
            <div class="panel-headline">
              <div class="spatial-orb">
                <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M12 20h9"></path><path d="M16.5 3.5a2.121 2.121 0 0 1 3 3L7 19l-4 1 1-4L16.5 3.5z"></path></svg>
              </div>
              <div class="panel-title-block">
                <h2>1. Architectural Sketch Studio</h2>
                <p>Interactive vector &amp; freehand blueprint drafting</p>
              </div>
            </div>

            <!-- Canvas View Options -->
            <div style="display:flex; gap:6px;">
              <button class="btn-spatial-tool" id="btn-grid-toggle" title="Toggle Grid (G)" onclick="toggleSpatialGrid()">
                <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="3" y="3" width="18" height="18" rx="2" ry="2"></rect><line x1="3" y1="9" x2="21" y2="9"></line><line x1="3" y1="15" x2="21" y2="15"></line><line x1="9" y1="3" x2="9" y2="21"></line><line x1="15" y1="3" x2="15" y2="21"></line></svg>
              </button>
              <button class="btn-spatial-tool" title="Zoom In (+)" onclick="zoomSpatialCanvas(1.2)">
                <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="11" cy="11" r="8"></circle><line x1="21" y1="21" x2="16.65" y2="16.65"></line><line x1="11" y1="8" x2="11" y2="14"></line><line x1="8" y1="11" x2="14" y2="11"></line></svg>
              </button>
              <button class="btn-spatial-tool" title="Reset Zoom" onclick="resetSpatialZoom()">
                <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M3 12a9 9 0 1 0 9-9 9.75 9.75 0 0 0-6.74 2.74L3 8"></path><polyline points="3 3 3 8 8 8"></polyline></svg>
              </button>
            </div>
          </div>

          <!-- Professional Architectural Toolbar -->
          <div class="spatial-toolbar">
            <div class="tool-group-dock">
              <button class="btn-spatial-tool active" id="tool-pencil" title="Pencil (P)" onclick="setSpatialTool('pencil')">
                <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M17 3a2.828 2.828 0 1 1 4 4L7.5 20.5 2 22l1.5-5.5L17 3z"></path></svg>
              </button>
              <button class="btn-spatial-tool" id="tool-line" title="Straight Wall Line (L)" onclick="setSpatialTool('line')">
                <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><line x1="5" y1="19" x2="19" y2="5"></line></svg>
              </button>
              <button class="btn-spatial-tool" id="tool-rect" title="Furniture Rectangle (R)" onclick="setSpatialTool('rect')">
                <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="3" y="3" width="18" height="18" rx="2" ry="2"></rect></svg>
              </button>
              <button class="btn-spatial-tool" id="tool-eraser" title="Eraser (E)" onclick="setSpatialTool('eraser')">
                <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="m7 21-4.3-4.3c-1-1-1-2.5 0-3.4l9.6-9.6c1-1 2.5-1 3.4 0l5.6 5.6c1 1 1 2.5 0 3.4L13 21"></path><path d="M22 21H7"></path><path d="m5 11 9 9"></path></svg>
              </button>
            </div>

            <!-- Brush Size Slider -->
            <div class="tool-group-dock">
              <div class="slider-pillbox">
                <span>Size:</span>
                <input type="range" id="brush-size" class="spatial-range" min="1" max="24" value="4" oninput="updateSpatialBrushSize(this.value)">
                <span id="brush-size-val" class="tech-badge">4px</span>
              </div>
            </div>

            <!-- Ink Selection Chips -->
            <div class="tool-group-dock">
              <div class="ink-orb active" style="background:#000000;" title="Deep Ink" onclick="setSpatialColor('#000000', this)"></div>
              <div class="ink-orb" style="background:#4b5563;" title="Graphite" onclick="setSpatialColor('#4b5563', this)"></div>
              <div class="ink-orb" style="background:#0fe3ff;" title="Cyan Blueprint" onclick="setSpatialColor('#0fe3ff', this)"></div>
            </div>

            <!-- History Controls -->
            <div class="tool-group-dock" style="margin-left:auto;">
              <button class="btn-spatial-tool" id="btn-undo" title="Undo (Ctrl+Z)" onclick="undoSpatialStroke()" disabled>
                <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="9 14 4 9 9 4"></polyline><path d="M20 20v-7a4 4 0 0 0-4-4H4"></path></svg>
              </button>
              <button class="btn-spatial-tool" id="btn-redo" title="Redo (Ctrl+Y)" onclick="redoSpatialStroke()" disabled>
                <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="15 14 20 9 15 4"></polyline><path d="M4 20v-7a4 4 0 0 1 4-4h12"></path></svg>
              </button>
              <button class="btn-spatial-tool" title="Clear Canvas" onclick="clearSpatialCanvas()">
                <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="3 6 5 6 21 6"></polyline><path d="M19 6v14a2 2 0 0 1-2 2H7a2 2 0 0 1-2-2V6m3 0V4a2 2 0 0 1 2-2h4a2 2 0 0 1 2 2v2"></path></svg>
              </button>
              <button class="btn-spatial-tool" title="Download Sketch PNG" onclick="downloadSpatialSketch()">
                <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4"></path><polyline points="7 10 12 15 17 10"></polyline><line x1="12" y1="15" x2="12" y2="3"></line></svg>
              </button>
            </div>
          </div>

          <!-- HTML5 Canvas Viewport -->
          <div class="spatial-canvas-viewport" id="canvas-stage-wrapper">
            <canvas id="drawing-canvas" width="512" height="512"></canvas>
            <canvas id="grid-canvas" width="512" height="512"></canvas>
            <div class="hud-spatial-hint" id="canvas-hud-hint">HOLD SHIFT TO PAN &bull; SCROLL TO ZOOM</div>
          </div>

          <!-- Presets Tray (Editable Genuine Templates) -->
          <div class="layout-presets-deck">
            <div class="deck-header">
              <span>Architectural Blueprint Templates:</span>
              <label style="color:var(--electric-cyan); cursor:pointer; text-transform:none;">
                Upload Custom Sketch <input type="file" id="file-upload-input" accept="image/png,image/jpeg" style="display:none;" onchange="handleSpatialFileUpload(event)">
              </label>
            </div>
            <div class="deck-scroll-row" id="preset-chips">
              <button type="button" class="layout-chip active" onclick="loadSpatialRoomPreset('bedroom')">&#128716; Master Bedroom</button>
              <button type="button" class="layout-chip" onclick="loadSpatialRoomPreset('living_room')">&#128715; Living Room</button>
              <button type="button" class="layout-chip" onclick="loadSpatialRoomPreset('office')">&#128187; Home Office</button>
              <button type="button" class="layout-chip" onclick="loadSpatialRoomPreset('kitchen')">&#127859; Gourmet Kitchen</button>
              <button type="button" class="layout-chip" onclick="loadSpatialRoomPreset('bathroom')">&#128705; Spa Bathroom</button>
            </div>
          </div>

          <!-- Customization Matrix (Styles, Lighting, Materials) -->
          <div class="spatial-params-matrix">
            <div class="matrix-2col">
              <div class="spatial-field">
                <label class="field-caption" for="category-select">Room Category</label>
                <select id="category-select" class="spatial-select" onchange="compileSpatialPrompt()">
                  <option value="bedroom" selected>Modern Bedroom</option>
                  <option value="living_room">Contemporary Living Room</option>
                  <option value="office">Executive Home Office</option>
                  <option value="kitchen">Gourmet Modern Kitchen</option>
                  <option value="bathroom">Luxury Spa Bathroom</option>
                  <option value="dining">Designer Dining Room</option>
                </select>
              </div>

              <div class="spatial-field">
                <label class="field-caption" for="style-select">Interior Style</label>
                <select id="style-select" class="spatial-select" onchange="compileSpatialPrompt()">
                  <option value="modern" selected>Modern</option>
                  <option value="minimalist">Minimalist</option>
                  <option value="luxury">Luxury Penthouse</option>
                  <option value="scandinavian">Scandinavian</option>
                  <option value="industrial">Industrial Loft</option>
                  <option value="japandi">Japandi Organic</option>
                </select>
              </div>
            </div>

            <div class="matrix-2col">
              <div class="spatial-field">
                <label class="field-caption" for="lighting-select">Lighting Atmosphere</label>
                <select id="lighting-select" class="spatial-select" onchange="compileSpatialPrompt()">
                  <option value="natural" selected>Natural Daylight from Window</option>
                  <option value="warm">Warm Ambient Recessed</option>
                  <option value="cool">Cool Architectural Daylight</option>
                  <option value="dramatic">Dramatic Chiaroscuro Evening</option>
                  <option value="golden">Golden Hour Sunlight</option>
                </select>
              </div>

              <div class="spatial-field">
                <label class="field-caption" for="materials-select">Material Palette</label>
                <select id="materials-select" class="spatial-select" onchange="compileSpatialPrompt()">
                  <option value="hardwood_linen" selected>Hardwood &amp; Natural Linen</option>
                  <option value="marble_brass">Calacatta Marble &amp; Brushed Brass</option>
                  <option value="concrete_leather">Polished Concrete &amp; Leather</option>
                  <option value="oak_white">Light White Oak &amp; Matte Plaster</option>
                </select>
              </div>
            </div>

            <!-- Engine Selection Stack -->
            <div class="spatial-field">
              <label class="field-caption">Generative Neural Engine</label>
              <div class="engine-stack">
                <div class="engine-choice-card active" onclick="selectSpatialEngine('controlnet-local', this)">
                  <input type="radio" name="ai_model" value="controlnet-local" checked>
                  <div class="engine-card-text">
                    <div class="engine-title-row">
                      <span>Local ControlNet + SD 1.5</span>
                      <span class="engine-tag primary">PRIMARY &bull; GPU</span>
                    </div>
                    <div class="engine-sub-desc">100% offline Stable Diffusion 1.5 + Scribble. High photorealism on RTX 3050 (~22s).</div>
                  </div>
                </div>

                <div class="engine-choice-card" onclick="selectSpatialEngine('pix2pix-exp5', this)">
                  <input type="radio" name="ai_model" value="pix2pix-exp5">
                  <div class="engine-card-text">
                    <div class="engine-title-row">
                      <span>Pix2Pix Exp 5 (Photographic GAN)</span>
                      <span class="engine-tag exp">EXPERIMENTAL CPU</span>
                    </div>
                    <div class="engine-sub-desc">Lightweight feedforward GAN (256x256). Fast CPU baseline with experimental artifacts.</div>
                  </div>
                </div>

                <div class="engine-choice-card" onclick="selectSpatialEngine('pix2pix-exp3', this)">
                  <input type="radio" name="ai_model" value="pix2pix-exp3">
                  <div class="engine-card-text">
                    <div class="engine-title-row">
                      <span>Pix2Pix Exp 3 (Compound Loss GAN)</span>
                      <span class="engine-tag exp">EXPERIMENTAL CPU</span>
                    </div>
                    <div class="engine-sub-desc">Edge+SSIM compound loss GAN (256x256). Demonstrates early milestone training.</div>
                  </div>
                </div>
              </div>
            </div>

            <!-- Computed Positive Prompt -->
            <div class="spatial-field">
              <label class="field-caption" for="prompt-input">
                <span>Computed Synthesis Prompt</span>
                <span style="color:var(--muted-grey); font-weight:normal; text-transform:none;">Directly drives synthesis</span>
              </label>
              <textarea id="prompt-input" class="spatial-textarea"></textarea>
            </div>

            <!-- Negative Prompt -->
            <div class="spatial-field">
              <label class="field-caption" for="neg-prompt-input">Negative Prompt</label>
              <textarea id="neg-prompt-input" class="spatial-textarea" style="min-height:46px;">sketch, drawing, line art, cartoon, 3d render, blurry, deformed, distorted architecture, duplicate furniture, noisy textures, oversaturated, low quality, watermark, text</textarea>
            </div>

            <!-- Fine-Tuning Drawer -->
            <div>
              <div class="fine-tune-accordion" onclick="toggleSpatialAccordion()">
                <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" id="accordion-arrow"><polyline points="6 9 12 15 18 9"></polyline></svg>
                <span>Fine-Tuning Parameters (Steps, Guidance, Seed)</span>
              </div>
              <div class="fine-tune-drawer" id="fine-tune-drawer">
                <div class="spatial-field">
                  <label class="field-caption">Steps</label>
                  <input type="number" id="steps-input" class="spatial-input" min="5" max="30" value="15">
                </div>
                <div class="spatial-field">
                  <label class="field-caption">Guidance</label>
                  <input type="number" id="guidance-input" class="spatial-input" min="1.0" max="15.0" step="0.5" value="7.0">
                </div>
                <div class="spatial-field">
                  <label class="field-caption">Seed</label>
                  <input type="number" id="seed-input" class="spatial-input" value="42">
                </div>
              </div>
            </div>

            <!-- Primary Generate Action Button -->
            <button type="button" class="btn-synthesize-master" id="btn-generate" onclick="generateSpatialInterior()">
              <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5">
                <polygon points="12 2 15.09 8.26 22 9.27 17 14.14 18.18 21.02 12 17.77 5.82 21.02 7 14.14 2 9.27 8.91 8.26 12 2"></polygon>
              </svg>
              <span id="btn-generate-text">Synthesize Photorealistic Interior</span>
            </button>
          </div>
        </div>

        <!-- RIGHT WORKSPACE: SPATIAL VIEWPORT & VISUALIZER -->
        <div class="spatial-panel">
          <div class="panel-head-spatial">
            <div class="panel-headline">
              <div class="spatial-orb" style="border-color:rgba(142, 68, 255, 0.45); color:#d8c2ff;">
                <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="3" y="3" width="18" height="18" rx="2" ry="2"></rect><circle cx="8.5" cy="8.5" r="1.5"></circle><polyline points="21 15 16 10 5 21"></polyline></svg>
              </div>
              <div class="panel-title-block">
                <h2>2. Synthesized Interior Viewport</h2>
                <p id="viewport-status-text">Awaiting architectural sketch</p>
              </div>
            </div>

            <!-- Visualizer View Switcher -->
            <div class="spatial-nav-tabs" id="view-mode-tabs" style="display:none;">
              <button type="button" class="nav-link-btn active" id="tab-view-gen" onclick="switchVisualizerMode('generated')">Interior</button>
              <button type="button" class="nav-link-btn" id="tab-view-compare" onclick="switchVisualizerMode('compare')">Before / After</button>
              <button type="button" class="nav-link-btn" id="tab-view-sketch" onclick="switchVisualizerMode('sketch')">Sketch</button>
            </div>
          </div>

          <!-- Viewport Stage -->
          <div class="spatial-visualizer-stage" id="result-stage">
            <div class="visualizer-empty-hud" id="result-empty-hint">
              <svg width="48" height="48" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.3" style="margin: 0 auto 12px; display:block; opacity:0.35;">
                <path d="M21 16V8a2 2 0 0 0-1-1.73l-7-4a2 2 0 0 0-2 0l-7 4A2 2 0 0 0 3 8v8a2 2 0 0 0 1 1.73l7 4a2 2 0 0 0 2 0l7-4A2 2 0 0 0 21 16z"></path>
                <polyline points="3.27 6.96 12 12.01 20.73 6.96"></polyline>
                <line x1="12" y1="22.08" x2="12" y2="12"></line>
              </svg>
              <strong>Spatial Neural Viewport</strong><br>
              Draft your layout on the left and select your design styles,<br>
              then click <strong>Synthesize Photorealistic Interior</strong>.
            </div>

            <!-- Single Image Output -->
            <img id="result-img" alt="Synthesized Interior">

            <!-- Draggable Interactive Comparison Curtain -->
            <div class="spatial-compare-box" id="compare-slider-box">
              <img id="compare-bottom-img" class="compare-bottom-layer" alt="Generated Interior">
              <div class="compare-top-curtain" id="compare-curtain">
                <img id="compare-top-img" alt="Original Blueprint">
                <div class="compare-spatial-handle">&#x21D4;</div>
              </div>
            </div>

            <!-- Error State Overlay -->
            <div class="spatial-error-drawer" id="error-overlay">
              <div class="error-hex-icon">
                <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"></circle><line x1="12" y1="8" x2="12" y2="12"></line><line x1="12" y1="16" x2="12.01" y2="16"></line></svg>
              </div>
              <div>
                <div style="font-family:var(--font-display); font-weight:700; color:#fff; font-size:1.05rem;">Neural Synthesis Interrupted</div>
                <div style="font-size:0.82rem; color:var(--muted-grey); margin-top:4px; max-width:340px;" id="error-overlay-msg">Error detail message</div>
              </div>
              <button type="button" class="btn-spatial-retry" onclick="generateSpatialInterior()">
                <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="23 4 23 10 17 10"></polyline><path d="M20.49 15a9 9 0 1 1-2.12-9.36L23 10"></path></svg>
                <span>Retry Synthesis</span>
              </button>
            </div>

            <!-- Multi-Stage Generation Sequence Overlay -->
            <div class="spatial-synthesis-overlay" id="loading-overlay">
              <div class="spatial-gyro-spinner"></div>
              <div>
                <div class="stage-sequence-text" id="loading-stage-title">Preparing architectural blueprint...</div>
                <div class="stage-sub-text" id="loading-stage-sub">Local Stable Diffusion 1.5 + ControlNet Scribble on RTX 3050</div>
              </div>
              <div class="elapsed-hud-tag" id="live-timer-badge">Elapsed: 0.0s</div>
            </div>
          </div>

          <!-- Viewport Dock Actions -->
          <div class="visualizer-dock-row">
            <div style="display:flex; gap:8px;">
              <button type="button" class="btn-spatial-dock" id="btn-download-result" onclick="downloadSpatialResult()" disabled>
                <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4"></path><polyline points="7 10 12 15 17 10"></polyline><line x1="12" y1="15" x2="12" y2="3"></line></svg>
                <span>Download PNG</span>
              </button>
              <button type="button" class="btn-spatial-dock" id="btn-save-project" onclick="openSaveSpatialModal()" disabled>
                <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M19 21H5a2 2 0 0 1-2-2V5a2 2 0 0 1 2-2h11l5 5v11a2 2 0 0 1-2 2z"></path><polyline points="17 21 17 13 7 13 7 21"></polyline><polyline points="7 3 7 8 15 8"></polyline></svg>
                <span>Save to Gallery</span>
              </button>
            </div>

            <!-- Live Telemetry HUD -->
            <div class="spatial-telemetry-hud" id="metrics-hud" style="display:none;">
              <div class="telemetry-chip">Model: <strong id="metric-model-val">SD 1.5 + ControlNet</strong></div>
              <div class="telemetry-chip">Latency: <strong id="metric-latency-val">22.6s</strong></div>
              <div class="telemetry-chip">VRAM: <strong id="metric-vram-val">0.65 GB</strong></div>
              <div class="telemetry-chip">Res: <strong id="metric-res-val">512&times;512</strong></div>
            </div>
          </div>

          <div style="margin-top:auto; padding:12px 16px; background:var(--glass-surface-2); border:1px solid var(--dark-edge); border-radius:var(--radius-lg); font-size:0.75rem; color:var(--muted-grey); line-height:1.5;">
            <strong style="color:var(--electric-cyan);">NVIDIA RTX 3050 Sequential Offload Architecture:</strong><br>
            All diffusion operations execute strictly in local FP16 with sequential CPU offloading and VAE slicing. Total peak GPU memory is capped under 1 GB VRAM to guarantee zero out-of-memory interruptions.
          </div>
        </div>

      </div>
    </section>

    <!-- ====================================================================
         MY DESIGNS — LOCAL PERSISTENT GALLERY
         ==================================================================== -->
    <section class="gallery-spatial-section" id="section-gallery">
      <div style="display:flex; justify-content:space-between; align-items:center; flex-wrap:wrap; gap:14px;">
        <div>
          <h2 style="font-family:var(--font-display); font-size:1.55rem; font-weight:700; color:#fff;">My Saved Spatial Projects</h2>
          <p style="font-size:0.84rem; color:var(--muted-grey); margin-top:4px;">Locally preserved interior blueprints and photorealistic visualizations</p>
        </div>
        <button type="button" class="btn-spatial-primary" style="padding:10px 22px; font-size:0.88rem;" onclick="switchSpatialNav('studio')">
          + New Design
        </button>
      </div>

      <div class="gallery-collection-grid" id="gallery-grid">
        <!-- Rendered dynamically -->
      </div>
    </section>

  </main>

  <!-- Save Design Modal -->
  <div class="spatial-modal-curtain" id="save-modal">
    <div class="spatial-modal-window">
      <div style="font-family:var(--font-display); font-weight:700; font-size:1.15rem; color:#fff;">Save Project to Gallery</div>
      <div class="spatial-field">
        <label class="field-caption" for="project-name-input">Project Name</label>
        <input type="text" id="project-name-input" class="spatial-input" placeholder="e.g. Skyline Master Suite">
      </div>
      <div style="display:flex; justify-content:flex-end; gap:10px; margin-top:8px;">
        <button type="button" class="btn-spatial-tool" style="width:auto; padding:0 16px; height:38px;" onclick="closeSaveSpatialModal()">Cancel</button>
        <button type="button" class="btn-spatial-primary" style="padding:10px 22px; font-size:0.88rem;" onclick="confirmSaveSpatialProject()">Save Project</button>
      </div>
    </div>
  </div>

  <!-- FULLSCREEN ACADEMIC PRESENTATION MODE -->
  <div class="presentation-fullscreen-curtain" id="presentation-fullscreen">
    <div class="pres-header-bar">
      <div>
        <h2 style="font-family:var(--font-display); font-size:1.6rem; color:#fff;" id="pres-project-title">Academic Demonstration — SketchSpace AI</h2>
        <p style="font-family:var(--font-tech); font-size:0.8rem; color:var(--electric-cyan);" id="pres-project-meta">Local SD 1.5 + ControlNet Scribble &bull; RTX 3050</p>
      </div>
      <button type="button" class="btn-spatial-secondary" onclick="closePresentationMode()">Exit Presentation</button>
    </div>
    <div class="pres-view-split">
      <div class="pres-card-box">
        <span style="font-family:var(--font-tech); color:var(--muted-grey);">Original Architectural Blueprint</span>
        <img id="pres-sketch-img" alt="Original Sketch">
      </div>
      <div class="pres-card-box">
        <span style="font-family:var(--font-tech); color:var(--electric-cyan);">Synthesized Interior Photorealism</span>
        <img id="pres-gen-img" alt="Synthesized Interior">
      </div>
    </div>
  </div>

  <!-- Toast Notification -->
  <div class="spatial-toast" id="toast-alert">
    <span id="toast-text">Notification</span>
  </div>

  <!-- Footer -->
  <footer>
    <div>
      <strong style="color:#ffffff;">SketchSpace AI</strong> &mdash; Intelligent Spatial Architecture Studio
      <p style="font-size:0.75rem; color:var(--muted-grey); margin-top:4px;">100% Offline Local Neural Synthesis &bull; NVIDIA GeForce RTX 3050 Laptop GPU &bull; PyTorch 2.11</p>
    </div>
    <div style="display:flex; gap:16px; align-items:center;">
      <a href="#section-storytelling" style="color:var(--electric-cyan); text-decoration:none;" onclick="switchSpatialNav('landing'); scrollToSignatureStory();">Pipeline</a>
      <span style="opacity:0.3;">|</span>
      <a href="#section-gallery-showcase" style="color:var(--electric-cyan); text-decoration:none;" onclick="switchSpatialNav('landing');">Case Studies</a>
      <span style="opacity:0.3;">|</span>
      <button type="button" class="btn-spatial-mini" style="width:auto; padding:6px 14px;" onclick="openPresentationMode()">Academic Presentation</button>
    </div>
  </footer>

  <!-- ==========================================================================
       JAVASCRIPT ARCHITECTURE & SCRIPT CONTROLS
       ========================================================================== */ -->
  <script>
    // -------------------------------------------------------------------------
    // 1. AMBIENT SPATIAL DUST SIMULATION
    // -------------------------------------------------------------------------
    const pCanvas = document.getElementById('ambient-particles-canvas');
    const pCtx = pCanvas.getContext('2d');
    let particles = [];
    const PARTICLE_COUNT = 38;

    function resizeSpatialCanvas() {
      pCanvas.width = window.innerWidth;
      pCanvas.height = window.innerHeight;
    }
    window.addEventListener('resize', resizeSpatialCanvas);
    resizeSpatialCanvas();

    class SpatialDust {
      constructor() { this.reset(); }
      reset() {
        this.x = Math.random() * pCanvas.width;
        this.y = Math.random() * pCanvas.height;
        this.size = Math.random() * 2 + 0.8;
        this.speedX = (Math.random() - 0.5) * 0.35;
        this.speedY = (Math.random() - 0.5) * 0.35;
        const colorPalette = ['rgba(15, 227, 255, ', 'rgba(142, 68, 255, ', 'rgba(255, 42, 141, ', 'rgba(0, 245, 196, '];
        this.color = colorPalette[Math.floor(Math.random() * colorPalette.length)];
        this.opacity = Math.random() * 0.45 + 0.14;
      }
      update() {
        this.x += this.speedX;
        this.y += this.speedY;
        if (this.x < 0 || this.x > pCanvas.width || this.y < 0 || this.y > pCanvas.height) {
          this.reset();
        }
      }
      draw() {
        pCtx.fillStyle = this.color + this.opacity + ')';
        pCtx.beginPath();
        pCtx.arc(this.x, this.y, this.size, 0, Math.PI * 2);
        pCtx.fill();
      }
    }

    for (let i = 0; i < PARTICLE_COUNT; i++) {
      particles.push(new SpatialDust());
    }

    function animateSpatialDust() {
      pCtx.clearRect(0, 0, pCanvas.width, pCanvas.height);
      for (let p of particles) {
        p.update();
        p.draw();
      }
      requestAnimationFrame(animateSpatialDust);
    }
    animateSpatialDust();

    // -------------------------------------------------------------------------
    // 2. CURSOR RESPONSIVE 3D PARALLAX FOR HERO ROOM
    // -------------------------------------------------------------------------
    const heroStage = document.getElementById('hero-interactive-stage');
    const heroRoom = document.getElementById('hero-room-3d');
    if (heroStage && heroRoom) {
      heroStage.addEventListener('mousemove', (e) => {
        const rect = heroStage.getBoundingClientRect();
        const xVal = (e.clientX - rect.left) / rect.width - 0.5;
        const yVal = (e.clientY - rect.top) / rect.height - 0.5;
        heroRoom.style.animationPlayState = 'paused';
        heroRoom.style.transform = `rotateX(${24 - yVal * 35}deg) rotateY(${-36 + xVal * 55}deg)`;
      });
      heroStage.addEventListener('mouseleave', () => {
        heroRoom.style.animationPlayState = 'running';
      });
    }

    // -------------------------------------------------------------------------
    // 3. NAVIGATION & TABS
    // -------------------------------------------------------------------------
    function switchSpatialNav(navKey) {
      document.querySelectorAll('.nav-link-btn').forEach(btn => btn.classList.remove('active'));
      const activeNav = document.getElementById(`tab-nav-${navKey}`);
      if (activeNav) activeNav.classList.add('active');

      document.getElementById('section-landing').style.display = (navKey === 'landing') ? 'grid' : 'none';
      document.getElementById('section-storytelling').style.display = (navKey === 'landing') ? 'flex' : 'none';
      const showcaseSection = document.getElementById('section-gallery-showcase');
      if (showcaseSection) showcaseSection.style.display = (navKey === 'landing') ? 'flex' : 'none';
      document.getElementById('section-studio').style.display = (navKey === 'studio') ? 'flex' : 'none';
      document.getElementById('section-gallery').style.display = (navKey === 'gallery') ? 'flex' : 'none';

      if (navKey === 'gallery') {
        renderSpatialGallery();
      }
      window.scrollTo({ top: 0, behavior: 'smooth' });
    }

    function scrollToSignatureStory() {
      const target = document.getElementById('section-storytelling');
      if (target) target.scrollIntoView({ behavior: 'smooth' });
    }

    function loadAndOpenPreset(category) {
      switchSpatialNav('studio');
      loadSpatialRoomPreset(category);
    }

    // -------------------------------------------------------------------------
    // 4. COMPOUND PROMPT MATRIX SYNTHESIZER
    // -------------------------------------------------------------------------
    const ROOM_BASE_PROMPTS = {
      bedroom: "photorealistic modern bedroom interior, comfortable bed, luxury pillows, bedside lamp, natural daylight from window, hardwood floor, architectural digest quality, high resolution, sharp focus, 8k",
      living_room: "photorealistic modern living room interior, stylish sofa, coffee table, indoor plants, natural daylight, hardwood flooring, elegant decor, architectural digest quality, high resolution, sharp focus, 8k",
      office: "photorealistic modern office workspace, executive desk, ergonomic chair, computer monitors and bookshelf, clean minimalist design, natural window lighting, high resolution, sharp focus, 8k",
      kitchen: "photorealistic modern kitchen interior, marble countertops, modern cabinets, stainless steel appliances, warm recessed lighting, clean minimalist surfaces, high resolution, sharp focus, 8k",
      bathroom: "photorealistic modern bathroom interior, porcelain sink, vanity mirror, glass shower enclosure, ceramic wall tiles, clean chrome fixtures, bright sanitary illumination, high resolution, sharp focus, 8k",
      dining: "photorealistic modern dining room, elegant dining table, designer chairs, pendant lighting, hardwood floor, architectural digest photography, high resolution, sharp focus, 8k"
    };

    const STYLE_MODIFIERS = {
      modern: "contemporary sleek modern design, clean geometric forms, subtle luxury",
      minimalist: "minimalist zen aesthetics, negative space, clutter-free elegance, organic simplicity",
      luxury: "high-end luxury penthouse suite, bespoke finishes, premium architectural details",
      scandinavian: "nordic scandinavian design, light woods, hygge warm aesthetic, functional beauty",
      industrial: "industrial loft aesthetics, exposed brick and metal accents, high ceilings, raw textures",
      japandi: "japandi fusion aesthetic, wabi-sabi organic textures, low-profile wooden craftsmanship"
    };

    const LIGHTING_MODIFIERS = {
      natural: "illuminated by soft natural morning daylight pouring from floor-to-ceiling windows",
      warm: "cozy warm ambient illumination, soft golden cove lighting and diffused warm spots",
      cool: "crisp cool architectural daylight, high-CRI clean illumination, vivid natural contrast",
      dramatic: "dramatic chiaroscuro lighting, deep shadows, cinematic atmospheric mood",
      golden: "golden hour late afternoon sunbeams casting elongated warm shadows"
    };

    const MATERIAL_MODIFIERS = {
      hardwood_linen: "natural white oak hardwood flooring, tactile linen drapery, matte wall textures",
      marble_brass: "bookmatched Calacatta gold marble surfaces, brushed satin brass fixtures, rich textures",
      concrete_leather: "poured architectural concrete accents, rich top-grain leather upholstery",
      oak_white: "light Scandinavian bleached oak woodwork, crisp matte plaster walls"
    };

    function compileSpatialPrompt() {
      const room = document.getElementById('category-select').value;
      const style = document.getElementById('style-select').value;
      const light = document.getElementById('lighting-select').value;
      const mat = document.getElementById('materials-select').value;

      const base = ROOM_BASE_PROMPTS[room] || ROOM_BASE_PROMPTS.bedroom;
      const styleText = STYLE_MODIFIERS[style] || "";
      const lightText = LIGHTING_MODIFIERS[light] || "";
      const matText = MATERIAL_MODIFIERS[mat] || "";

      const compound = `${base}, ${styleText}, ${lightText}, ${matText}`;
      document.getElementById('prompt-input').value = compound;
    }

    // -------------------------------------------------------------------------
    // 5. DRAWING CANVAS ENGINE
    // -------------------------------------------------------------------------
    const canvas = document.getElementById('drawing-canvas');
    const ctx = canvas.getContext('2d', { willReadFrequently: true });
    const gridCanvas = document.getElementById('grid-canvas');
    const gCtx = gridCanvas.getContext('2d');

    let currentTool = 'pencil';
    let currentColor = '#000000';
    let currentBrushSize = 4;
    let isDrawing = false;
    let startX = 0;
    let startY = 0;
    let snapshotBeforeShape = null;

    let zoomScale = 1.0;
    let isGridActive = false;

    const MAX_HISTORY = 25;
    let undoStack = [];
    let redoStack = [];

    function initSpatialCanvas() {
      ctx.fillStyle = '#ffffff';
      ctx.fillRect(0, 0, canvas.width, canvas.height);
      saveSpatialState();
      setupSpatialCanvasEvents();
      renderSpatialGrid();
    }

    function saveSpatialState() {
      const imgData = ctx.getImageData(0, 0, canvas.width, canvas.height);
      undoStack.push(imgData);
      if (undoStack.length > MAX_HISTORY) undoStack.shift();
      redoStack = [];
      updateSpatialHistoryButtons();
      document.getElementById('canvas-hud-hint').style.opacity = '0';
    }

    function updateSpatialHistoryButtons() {
      document.getElementById('btn-undo').disabled = (undoStack.length <= 1);
      document.getElementById('btn-redo').disabled = (redoStack.length === 0);
    }

    function undoSpatialStroke() {
      if (undoStack.length > 1) {
        const current = undoStack.pop();
        redoStack.push(current);
        const previous = undoStack[undoStack.length - 1];
        ctx.putImageData(previous, 0, 0);
        updateSpatialHistoryButtons();
      }
    }

    function redoSpatialStroke() {
      if (redoStack.length > 0) {
        const next = redoStack.pop();
        undoStack.push(next);
        ctx.putImageData(next, 0, 0);
        updateSpatialHistoryButtons();
      }
    }

    function clearSpatialCanvas() {
      if (confirm('Clear the architectural canvas?')) {
        ctx.fillStyle = '#ffffff';
        ctx.fillRect(0, 0, canvas.width, canvas.height);
        saveSpatialState();
      }
    }

    function setSpatialTool(tool) {
      currentTool = tool;
      document.querySelectorAll('.btn-spatial-tool').forEach(b => {
        if (b.id && b.id.startsWith('tool-')) b.classList.remove('active');
      });
      const targetBtn = document.getElementById(`tool-${tool}`);
      if (targetBtn) targetBtn.classList.add('active');
      canvas.style.cursor = (tool === 'eraser') ? 'cell' : 'crosshair';
    }

    function setSpatialColor(color, orbElement) {
      currentColor = color;
      if (orbElement) {
        document.querySelectorAll('.ink-orb').forEach(c => c.classList.remove('active'));
        orbElement.classList.add('active');
      }
      if (currentTool === 'eraser') setSpatialTool('pencil');
    }

    function updateSpatialBrushSize(val) {
      currentBrushSize = parseInt(val, 10);
      document.getElementById('brush-size-val').textContent = `${val}px`;
    }

    function zoomSpatialCanvas(factor) {
      zoomScale = Math.min(Math.max(zoomScale * factor, 0.5), 3.0);
      canvas.style.transform = `scale(${zoomScale})`;
      gridCanvas.style.transform = `scale(${zoomScale})`;
    }

    function resetSpatialZoom() {
      zoomScale = 1.0;
      canvas.style.transform = `scale(1)`;
      gridCanvas.style.transform = `scale(1)`;
    }

    function toggleSpatialGrid() {
      isGridActive = !isGridActive;
      gridCanvas.style.display = isGridActive ? 'block' : 'none';
      document.getElementById('btn-grid-toggle').classList.toggle('active', isGridActive);
    }

    function renderSpatialGrid() {
      gCtx.clearRect(0, 0, gridCanvas.width, gridCanvas.height);
      gCtx.strokeStyle = 'rgba(15, 227, 255, 0.22)';
      gCtx.lineWidth = 1;
      const step = 32;
      for (let x = step; x < gridCanvas.width; x += step) {
        gCtx.beginPath();
        gCtx.moveTo(x, 0);
        gCtx.lineTo(x, gridCanvas.height);
        gCtx.stroke();
      }
      for (let y = step; y < gridCanvas.height; y += step) {
        gCtx.beginPath();
        gCtx.moveTo(0, y);
        gCtx.lineTo(gridCanvas.width, y);
        gCtx.stroke();
      }
    }

    function getSpatialCoords(e) {
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

    function setupSpatialCanvasEvents() {
      const onPointerDown = (e) => {
        e.preventDefault();
        isDrawing = true;
        const coords = getSpatialCoords(e);
        startX = coords.x;
        startY = coords.y;

        ctx.lineCap = 'round';
        ctx.lineJoin = 'round';

        if (currentTool === 'pencil') {
          ctx.strokeStyle = currentColor;
          ctx.lineWidth = currentBrushSize;
          ctx.beginPath();
          ctx.moveTo(startX, startY);
          ctx.lineTo(startX, startY);
          ctx.stroke();
        } else if (currentTool === 'eraser') {
          ctx.strokeStyle = '#ffffff';
          ctx.lineWidth = currentBrushSize * 2.5;
          ctx.beginPath();
          ctx.moveTo(startX, startY);
          ctx.lineTo(startX, startY);
          ctx.stroke();
        } else if (currentTool === 'line' || currentTool === 'rect') {
          snapshotBeforeShape = ctx.getImageData(0, 0, canvas.width, canvas.height);
          ctx.strokeStyle = currentColor;
          ctx.lineWidth = currentBrushSize;
        }
      };

      const onPointerMove = (e) => {
        if (!isDrawing) return;
        e.preventDefault();
        const coords = getSpatialCoords(e);

        if (currentTool === 'pencil' || currentTool === 'eraser') {
          ctx.lineTo(coords.x, coords.y);
          ctx.stroke();
        } else if (currentTool === 'line' && snapshotBeforeShape) {
          ctx.putImageData(snapshotBeforeShape, 0, 0);
          ctx.beginPath();
          ctx.moveTo(startX, startY);
          ctx.lineTo(coords.x, coords.y);
          ctx.stroke();
        } else if (currentTool === 'rect' && snapshotBeforeShape) {
          ctx.putImageData(snapshotBeforeShape, 0, 0);
          ctx.strokeRect(startX, startY, coords.x - startX, coords.y - startY);
        }
      };

      const onPointerUp = (e) => {
        if (!isDrawing) return;
        isDrawing = false;
        ctx.closePath();
        snapshotBeforeShape = null;
        saveSpatialState();
      };

      canvas.addEventListener('mousedown', onPointerDown);
      canvas.addEventListener('mousemove', onPointerMove);
      window.addEventListener('mouseup', onPointerUp);

      canvas.addEventListener('touchstart', onPointerDown, { passive: false });
      canvas.addEventListener('touchmove', onPointerMove, { passive: false });
      window.addEventListener('touchend', onPointerUp);

      window.addEventListener('keydown', (e) => {
        if ((e.ctrlKey || e.metaKey) && e.key === 'z') { e.preventDefault(); undoSpatialStroke(); }
        if ((e.ctrlKey || e.metaKey) && e.key === 'y') { e.preventDefault(); redoSpatialStroke(); }
        if (e.key === 'p' || e.key === 'P') setSpatialTool('pencil');
        if (e.key === 'e' || e.key === 'E') setSpatialTool('eraser');
        if (e.key === 'l' || e.key === 'L') setSpatialTool('line');
        if (e.key === 'r' || e.key === 'R') setSpatialTool('rect');
        if (e.key === 'g' || e.key === 'G') toggleSpatialGrid();
      });
    }

    function downloadSpatialSketch() {
      const link = document.createElement('a');
      link.download = `sketchspace_blueprint_${Date.now()}.png`;
      link.href = canvas.toDataURL('image/png');
      link.click();
    }

    // -------------------------------------------------------------------------
    // 6. ROOM PRESETS & FILE HANDLING
    // -------------------------------------------------------------------------
    async function loadSpatialRoomPreset(category) {
      document.querySelectorAll('.layout-chip').forEach(c => c.classList.remove('active'));
      const activeBtn = Array.from(document.querySelectorAll('.layout-chip')).find(b => b.textContent.toLowerCase().includes(category.replace('_', ' ')));
      if (activeBtn) activeBtn.classList.add('active');

      const select = document.getElementById('category-select');
      if (select) {
        select.value = category;
        compileSpatialPrompt();
      }

      const filenameMap = {
        bedroom: 'new_bedroom_sketch.png',
        living_room: 'new_living_room_sketch.png',
        office: 'new_office_sketch.png',
        kitchen: 'new_kitchen_sketch.png',
        bathroom: 'new_bathroom_sketch.png'
      };

      const targetFile = filenameMap[category] || 'new_bedroom_sketch.png';
      try {
        const img = new Image();
        img.crossOrigin = 'anonymous';
        img.onload = () => {
          ctx.fillStyle = '#ffffff';
          ctx.fillRect(0, 0, canvas.width, canvas.height);
          ctx.drawImage(img, 0, 0, canvas.width, canvas.height);
          saveSpatialState();
          displaySpatialToast(`Loaded ${category.replace('_', ' ')} layout preset`);
        };
        img.src = `/api/sketches/example/${targetFile}`;
      } catch (e) {
        displaySpatialToast('Could not load preset sketch: ' + e.message);
      }
    }

    function handleSpatialFileUpload(e) {
      const file = e.target.files[0];
      if (!file) return;
      const reader = new FileReader();
      reader.onload = (event) => {
        const img = new Image();
        img.onload = () => {
          ctx.fillStyle = '#ffffff';
          ctx.fillRect(0, 0, canvas.width, canvas.height);
          const scale = Math.min(canvas.width / img.width, canvas.height / img.height);
          const nw = img.width * scale;
          const nh = img.height * scale;
          const ox = (canvas.width - nw) / 2;
          const oy = (canvas.height - nh) / 2;
          ctx.drawImage(img, ox, oy, nw, nh);
          saveSpatialState();
          displaySpatialToast('Custom sketch uploaded successfully');
        };
        img.src = event.target.result;
      };
      reader.readAsDataURL(file);
    }

    // -------------------------------------------------------------------------
    // 7. MULTI-STAGE GENERATION PIPELINE
    // -------------------------------------------------------------------------
    let selectedModel = 'controlnet-local';
    let currentGeneratedUrl = null;
    let currentSketchUrl = null;
    let timerInterval = null;
    let stageInterval = null;

    function selectSpatialEngine(model, element) {
      selectedModel = model;
      document.querySelectorAll('.engine-choice-card').forEach(c => c.classList.remove('active'));
      if (element) {
        element.classList.add('active');
        element.querySelector('input[type="radio"]').checked = true;
      }

      const btnText = document.getElementById('btn-generate-text');
      if (model === 'controlnet-local') {
        btnText.textContent = 'Synthesize Photorealistic Interior';
      } else if (model === 'pix2pix-exp5') {
        btnText.textContent = 'Synthesize with Pix2Pix Exp 5 (GAN)';
      } else if (model === 'pix2pix-exp3') {
        btnText.textContent = 'Synthesize with Pix2Pix Exp 3 (GAN)';
      }
    }

    function toggleSpatialAccordion() {
      const drawer = document.getElementById('fine-tune-drawer');
      const arrow = document.getElementById('accordion-arrow');
      if (drawer.style.display === 'grid') {
        drawer.style.display = 'none';
        arrow.style.transform = 'rotate(0deg)';
      } else {
        drawer.style.display = 'grid';
        arrow.style.transform = 'rotate(180deg)';
      }
    }

    const STAGES = [
      { t: "Preparing architectural blueprint...", s: "Normalizing 512x512 aspect ratio & sketch geometry" },
      { t: "Interpreting spatial structure...", s: "ControlNet conditioning on RTX 3050 Tensor Cores" },
      { t: "Synthesizing interior environment...", s: "Denoising latents via sequential CPU offload" },
      { t: "Refining lighting and materials...", s: "Decoding FP16 latents via tiled VAE" },
      { t: "Finalizing interior render...", s: "Assembling high-resolution spatial output" }
    ];

    async function generateSpatialInterior() {
      const btn = document.getElementById('btn-generate');
      const loadingOverlay = document.getElementById('loading-overlay');
      const stageTitle = document.getElementById('loading-stage-title');
      const stageSub = document.getElementById('loading-stage-sub');
      const timerBadge = document.getElementById('live-timer-badge');
      const resultImg = document.getElementById('result-img');
      const resultEmpty = document.getElementById('result-empty-hint');
      const compareSlider = document.getElementById('compare-slider-box');
      const errorOverlay = document.getElementById('error-overlay');
      const errorMsg = document.getElementById('error-overlay-msg');
      const statusText = document.getElementById('viewport-status-text');
      const downloadBtn = document.getElementById('btn-download-result');
      const saveBtn = document.getElementById('btn-save-project');
      const metricsHud = document.getElementById('metrics-hud');

      currentGeneratedUrl = null;
      resultImg.src = '';
      resultImg.style.display = 'none';
      compareSlider.style.display = 'none';
      resultEmpty.style.display = 'none';
      errorOverlay.style.display = 'none';
      downloadBtn.disabled = true;
      saveBtn.disabled = true;
      metricsHud.style.display = 'none';
      document.getElementById('view-mode-tabs').style.display = 'none';

      btn.disabled = true;
      loadingOverlay.style.display = 'flex';

      let stageIndex = 0;
      stageTitle.textContent = STAGES[0].t;
      stageSub.textContent = STAGES[0].s;
      stageInterval = setInterval(() => {
        stageIndex = (stageIndex + 1) % STAGES.length;
        stageTitle.textContent = STAGES[stageIndex].t;
        stageSub.textContent = STAGES[stageIndex].s;
      }, 5500);

      const startTime = performance.now();
      timerBadge.textContent = 'Elapsed: 0.0s';
      timerInterval = setInterval(() => {
        const sec = ((performance.now() - startTime) / 1000).toFixed(1);
        timerBadge.textContent = `Elapsed: ${sec}s`;
      }, 100);

      try {
        const blob = await new Promise((resolve) => canvas.toBlob(resolve, 'image/png'));
        currentSketchUrl = canvas.toDataURL('image/png');

        const formData = new FormData();
        formData.append('file', blob, 'sketch.png');
        formData.append('model', selectedModel);

        const category = document.getElementById('category-select').value;
        const prompt = document.getElementById('prompt-input').value;
        const negPrompt = document.getElementById('neg-prompt-input').value;
        const steps = document.getElementById('steps-input').value || 15;

        let apiUrl = `/api/generate?model=${encodeURIComponent(selectedModel)}&category=${encodeURIComponent(category)}&steps=${steps}`;
        if (prompt) apiUrl += `&prompt=${encodeURIComponent(prompt)}`;
        if (negPrompt) apiUrl += `&negative_prompt=${encodeURIComponent(negPrompt)}`;

        const response = await fetch(apiUrl, {
          method: 'POST',
          body: formData
        });

        clearInterval(timerInterval);
        clearInterval(stageInterval);

        if (!response.ok) {
          let errDetail = `HTTP ${response.status}`;
          try {
            const errData = await response.json();
            errDetail = errData.detail || errDetail;
          } catch (_) {
            errDetail = await response.text();
          }
          throw new Error(errDetail);
        }

        const data = await response.json();
        const durationSec = ((performance.now() - startTime) / 1000).toFixed(1);

        if (!data.success || !data.generated_url) {
          throw new Error(data.message || 'Server did not return a valid generated image URL.');
        }

        currentGeneratedUrl = data.generated_url;

        resultImg.src = `${currentGeneratedUrl}?t=${Date.now()}`;
        resultImg.style.display = 'block';
        loadingOverlay.style.display = 'none';
        document.getElementById('view-mode-tabs').style.display = 'flex';
        downloadBtn.disabled = false;
        saveBtn.disabled = false;
        metricsHud.style.display = 'flex';

        const isLocalCN = (selectedModel === 'controlnet-local');
        document.getElementById('metric-model-val').textContent = data.model_used || (isLocalCN ? 'Local SD 1.5 + ControlNet' : selectedModel);
        document.getElementById('metric-latency-val').textContent = `${durationSec}s`;
        document.getElementById('metric-res-val').textContent = data.resolution || (isLocalCN ? '512×512' : '256×256');

        if (data.metrics && data.metrics.vram_peak_allocated_mb) {
          document.getElementById('metric-vram-val').textContent = `${(data.metrics.vram_peak_allocated_mb / 1024).toFixed(2)} GB`;
        } else {
          document.getElementById('metric-vram-val').textContent = isLocalCN ? '0.65 GB' : 'CPU';
        }

        statusText.textContent = `Completed in ${durationSec}s &bull; ${data.resolution || '512x512'}`;
        switchVisualizerMode('generated');
        displaySpatialToast('Photorealistic interior synthesized successfully!');

      } catch (err) {
        clearInterval(timerInterval);
        clearInterval(stageInterval);
        loadingOverlay.style.display = 'none';
        resultImg.style.display = 'none';
        compareSlider.style.display = 'none';
        errorOverlay.style.display = 'flex';
        errorMsg.textContent = err.message;
        statusText.textContent = 'Neural Synthesis Interrupted';
        displaySpatialToast('Synthesis Error: ' + err.message);
      } finally {
        btn.disabled = false;
      }
    }

    // -------------------------------------------------------------------------
    // 8. INTERACTIVE VIEW MODES & COMPARISON CURTAIN
    // -------------------------------------------------------------------------
    function switchVisualizerMode(mode) {
      document.querySelectorAll('#view-mode-tabs .nav-link-btn').forEach(t => t.classList.remove('active'));
      const activeTab = document.getElementById(`tab-view-${mode}`);
      if (activeTab) activeTab.classList.add('active');

      const resultImg = document.getElementById('result-img');
      const compareSlider = document.getElementById('compare-slider-box');

      if (!currentGeneratedUrl) return;

      if (mode === 'generated') {
        compareSlider.style.display = 'none';
        resultImg.src = `${currentGeneratedUrl}?t=${Date.now()}`;
        resultImg.style.display = 'block';
      } else if (mode === 'sketch') {
        compareSlider.style.display = 'none';
        resultImg.src = currentSketchUrl;
        resultImg.style.display = 'block';
      } else if (mode === 'compare') {
        resultImg.style.display = 'none';
        document.getElementById('compare-bottom-img').src = `${currentGeneratedUrl}?t=${Date.now()}`;
        document.getElementById('compare-top-img').src = currentSketchUrl;
        compareSlider.style.display = 'block';
        initSpatialCompareEvents();
      }
    }

    let isComparingSpatial = false;
    function initSpatialCompareEvents() {
      const container = document.getElementById('compare-slider-box');
      const curtain = document.getElementById('compare-curtain');

      const moveDivider = (clientX) => {
        const rect = container.getBoundingClientRect();
        let pos = clientX - rect.left;
        if (pos < 0) pos = 0;
        if (pos > rect.width) pos = rect.width;
        curtain.style.width = `${pos}px`;
      };

      container.onmousedown = (e) => { isComparingSpatial = true; moveDivider(e.clientX); };
      window.onmousemove = (e) => { if (isComparingSpatial) moveDivider(e.clientX); };
      window.onmouseup = () => { isComparingSpatial = false; };

      container.ontouchstart = (e) => { isComparingSpatial = true; moveDivider(e.touches[0].clientX); };
      window.ontouchmove = (e) => { if (isComparingSpatial && e.touches.length > 0) moveDivider(e.touches[0].clientX); };
      window.ontouchend = () => { isComparingSpatial = false; };
    }

    function downloadSpatialResult() {
      if (!currentGeneratedUrl) return;
      const link = document.createElement('a');
      link.download = `sketchspace_interior_${Date.now()}.png`;
      link.href = currentGeneratedUrl;
      link.click();
    }

    // -------------------------------------------------------------------------
    // 9. MY DESIGNS — LOCAL PERSISTENT GALLERY
    // -------------------------------------------------------------------------
    const SPATIAL_STORAGE_KEY = 'sketchspace_spatial_projects';

    function getSpatialProjects() {
      try {
        return JSON.parse(localStorage.getItem(SPATIAL_STORAGE_KEY)) || [];
      } catch (_) {
        return [];
      }
    }

    function saveSpatialProjects(projs) {
      localStorage.setItem(SPATIAL_STORAGE_KEY, JSON.stringify(projs));
    }

    function openSaveSpatialModal() {
      if (!currentGeneratedUrl) return;
      const defaultName = document.getElementById('category-select').selectedOptions[0].text;
      document.getElementById('project-name-input').value = `${defaultName} Project`;
      document.getElementById('save-modal').style.display = 'flex';
    }

    function closeSaveSpatialModal() {
      document.getElementById('save-modal').style.display = 'none';
    }

    function confirmSaveSpatialProject() {
      const name = document.getElementById('project-name-input').value.trim() || 'Untitled Spatial Project';
      const projects = getSpatialProjects();
      const newProj = {
        id: 'proj_' + Date.now(),
        name: name,
        category: document.getElementById('category-select').value,
        style: document.getElementById('style-select').value,
        model: selectedModel,
        imageUrl: currentGeneratedUrl,
        sketchUrl: currentSketchUrl,
        prompt: document.getElementById('prompt-input').value,
        createdAt: new Date().toLocaleDateString(undefined, { month: 'short', day: 'numeric', year: 'numeric' })
      };
      projects.unshift(newProj);
      saveSpatialProjects(projects);
      closeSaveSpatialModal();
      displaySpatialToast(`Saved "${name}" to My Designs`);
    }

    function renderSpatialGallery() {
      const grid = document.getElementById('gallery-grid');
      const projects = getSpatialProjects();

      if (projects.length === 0) {
        grid.innerHTML = `
          <div style="grid-column: 1 / -1; padding: 48px; text-align: center; color: var(--muted-grey); background: var(--glass-surface-2); border-radius: var(--radius-xl); border: 1px dashed var(--dark-edge);">
            <svg width="40" height="40" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" style="margin: 0 auto 12px; display:block; opacity:0.4;">
              <rect x="3" y="3" width="18" height="18" rx="2" ry="2"></rect><circle cx="8.5" cy="8.5" r="1.5"></circle><polyline points="21 15 16 10 5 21"></polyline>
            </svg>
            <div style="font-family:var(--font-display); font-size: 1.1rem; font-weight: 700; color: #fff;">No Saved Projects Yet</div>
            <div style="font-size: 0.82rem; margin-top: 4px;">Synthesize an interior in the Studio and click "Save to Gallery".</div>
          </div>
        `;
        return;
      }

      grid.innerHTML = projects.map(p => `
        <div class="spatial-project-card">
          <img src="${p.imageUrl}" class="spatial-project-thumb" alt="${p.name}">
          <div class="spatial-project-body">
            <div class="spatial-project-name">${p.name}</div>
            <div class="spatial-project-meta">${p.category.toUpperCase()} &bull; ${p.createdAt}</div>
            <div class="spatial-project-actions">
              <button class="btn-spatial-mini" onclick="reopenSpatialProject('${p.id}')">Open</button>
              <button class="btn-spatial-mini delete-btn" onclick="deleteSpatialProject('${p.id}')">Delete</button>
            </div>
          </div>
        </div>
      `).join('');
    }

    function reopenSpatialProject(id) {
      const projects = getSpatialProjects();
      const proj = projects.find(p => p.id === id);
      if (!proj) return;

      switchSpatialNav('studio');
      document.getElementById('category-select').value = proj.category || 'bedroom';
      document.getElementById('style-select').value = proj.style || 'modern';
      document.getElementById('prompt-input').value = proj.prompt || '';
      selectSpatialEngine(proj.model || 'controlnet-local');

      currentGeneratedUrl = proj.imageUrl;
      currentSketchUrl = proj.sketchUrl;

      const resultImg = document.getElementById('result-img');
      resultImg.src = currentGeneratedUrl;
      resultImg.style.display = 'block';
      document.getElementById('result-empty-hint').style.display = 'none';
      document.getElementById('view-mode-tabs').style.display = 'flex';
      document.getElementById('btn-download-result').disabled = false;
      document.getElementById('btn-save-project').disabled = false;
      document.getElementById('viewport-status-text').textContent = `Opened: ${proj.name}`;
      displaySpatialToast(`Reopened "${proj.name}"`);
    }

    function deleteSpatialProject(id) {
      if (!confirm('Delete this saved project?')) return;
      let projects = getSpatialProjects();
      projects = projects.filter(p => p.id !== id);
      saveSpatialProjects(projects);
      renderSpatialGallery();
      displaySpatialToast('Project deleted');
    }

    // -------------------------------------------------------------------------
    // 10. FULLSCREEN ACADEMIC PRESENTATION MODE
    // -------------------------------------------------------------------------
    function openPresentationMode() {
      const presModal = document.getElementById('presentation-fullscreen');
      const presSketch = document.getElementById('pres-sketch-img');
      const presGen = document.getElementById('pres-gen-img');
      const presTitle = document.getElementById('pres-project-title');

      if (!currentGeneratedUrl) {
        presSketch.src = '/api/sketches/example/new_bedroom_sketch.png';
        presGen.src = '/api/image/local_cn_bedroom_1795531503385.png';
        presTitle.textContent = 'Master Bedroom Suite — Academic Demonstration';
      } else {
        presSketch.src = currentSketchUrl;
        presGen.src = currentGeneratedUrl;
        const catName = document.getElementById('category-select').selectedOptions[0].text;
        presTitle.textContent = `${catName} — Academic Demonstration`;
      }

      presModal.style.display = 'flex';
    }

    function closePresentationMode() {
      document.getElementById('presentation-fullscreen').style.display = 'none';
    }

    function displaySpatialToast(msg) {
      const toast = document.getElementById('toast-alert');
      document.getElementById('toast-text').textContent = msg;
      toast.style.display = 'flex';
      setTimeout(() => {
        toast.style.display = 'none';
      }, 3500);
    }

    // -------------------------------------------------------------------------
    // 11. INITIALIZATION
    // -------------------------------------------------------------------------
    window.addEventListener('DOMContentLoaded', () => {
      initSpatialCanvas();
      compileSpatialPrompt();
    });
  </script>
</body>
</html>
"""

with open('backend/static/index.html', 'w', encoding='utf-8') as f:
    f.write(HTML_CONTENT)

print(f"Successfully generated backend/static/index.html ({len(HTML_CONTENT)} characters)")
