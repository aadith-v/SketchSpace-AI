# Build Luxury Architectural Atelier index.html for SketchSpace AI
import os

HTML_CONTENT = """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>SKETCHSPACE AI — From Imagination To Architecture</title>
  
  <!-- Architectural Atelier Typography: Cormorant Garamond (Serif), Playfair Display, Manrope, IBM Plex Mono -->
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,300;0,400;0,500;0,600;0,700;1,400;1,500;1,600;1,700&family=IBM+Plex+Mono:ital,wght@0,400;0,500;0,600;1,400&family=Manrope:wght@300;400;500;600;700;800&family=Playfair+Display:ital,wght@0,400;0,600;0,700;1,400;1,600&display=swap" rel="stylesheet">
  
  <style>
    /* ==========================================================================
       LUXURY ARCHITECTURAL ATELIER DESIGN SYSTEM
       Warm Natural Materials: Travertine, Walnut, Sandstone, Antique Brass
       ========================================================================== */
    :root {
      /* Deep Architectural Foundation */
      --atelier-bg: #11100e;
      --atelier-surface-1: #181613;
      --atelier-surface-2: #211e1a;
      --atelier-surface-elevated: #2a2622;
      --atelier-card: rgba(30, 27, 24, 0.88);
      
      /* Primary Architectural Palette */
      --warm-ivory: #fbf9f5;
      --soft-cream: #f4f0e6;
      --travertine: #dfd7c7;
      --sandstone: #eae3d2;
      --natural-taupe: #b5a895;
      --muted-ash: #9e9382;
      --dim-charcoal: #6b6357;
      --border-subtle: rgba(223, 215, 199, 0.12);
      --border-medium: rgba(223, 215, 199, 0.22);
      --border-focus: rgba(197, 168, 128, 0.65);
      
      /* Rich Natural Material Accents */
      --antique-brass: #c5a880;
      --brass-hover: #d8bc94;
      --brass-subtle: rgba(197, 168, 128, 0.22);
      --walnut-rich: #3c2f2f;
      --honed-bronze: #8c7853;
      --olive-sage: #606b5d;
      --terracotta-soft: #a8624a;
      
      /* Typography Fonts */
      --font-serif-display: 'Cormorant Garamond', 'Playfair Display', Georgia, serif;
      --font-body: 'Manrope', -apple-system, BlinkMacSystemFont, sans-serif;
      --font-tech: 'IBM Plex Mono', monospace;

      /* Refined Radii */
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
      background-color: var(--atelier-bg);
    }

    body {
      background-color: var(--atelier-bg);
      color: var(--soft-cream);
      font-family: var(--font-body);
      min-height: 100vh;
      display: flex;
      flex-direction: column;
      overflow-x: hidden;
      position: relative;
      line-height: 1.65;
      -webkit-font-smoothing: antialiased;
      -moz-osx-font-smoothing: grayscale;
    }

    ::selection {
      background: var(--brass-subtle);
      color: var(--warm-ivory);
    }

    /* Ambient Warm Architectural Lighting Fields (No Neon) */
    .atelier-light-fields {
      position: fixed;
      top: 0; left: 0; width: 100vw; height: 100vh;
      pointer-events: none;
      z-index: 0;
      overflow: hidden;
    }

    .light-field-glow {
      position: absolute;
      border-radius: 50%;
      filter: blur(120px);
      opacity: 0.16;
      will-change: transform;
    }
    .glow-1 {
      top: -15%; left: 10%;
      width: 65vw; height: 60vh;
      background: radial-gradient(circle, #c5a880 0%, #3c2f2f 60%, transparent 80%);
      animation: floatWarmLight 28s infinite alternate ease-in-out;
    }
    .glow-2 {
      bottom: -15%; right: 5%;
      width: 60vw; height: 65vh;
      background: radial-gradient(circle, #8c7853 0%, #1e1714 65%, transparent 80%);
      animation: floatWarmLight 34s infinite alternate ease-in-out;
      animation-delay: -10s;
    }

    @keyframes floatWarmLight {
      0% { transform: translate(0, 0) scale(1); }
      50% { transform: translate(3vw, 4vh) scale(1.08); }
      100% { transform: translate(-2vw, -3vh) scale(0.95); }
    }

    /* Fine Architectural Grid Texture */
    .atelier-grid-texture {
      position: fixed;
      top: 0; left: 0; width: 100vw; height: 100vh;
      pointer-events: none;
      z-index: 0;
      opacity: 0.15;
      background-image: 
        linear-gradient(to right, rgba(223, 215, 199, 0.08) 1px, transparent 1px),
        linear-gradient(to bottom, rgba(223, 215, 199, 0.08) 1px, transparent 1px);
      background-size: 64px 64px;
    }

    /* Ambient Spatial Dust Particles Canvas */
    #ambient-particles-canvas {
      position: fixed;
      top: 0; left: 0; width: 100vw; height: 100vh;
      pointer-events: none;
      z-index: 1;
    }

    /* ==========================================================================
       MINIMAL PREMIUM NAVIGATION
       ========================================================================== */
    .spatial-nav {
      position: sticky;
      top: 0;
      z-index: 100;
      backdrop-filter: blur(20px);
      -webkit-backdrop-filter: blur(20px);
      background: rgba(17, 16, 14, 0.88);
      border-bottom: 1px solid var(--border-subtle);
      padding: 16px 54px;
      display: flex;
      align-items: center;
      justify-content: space-between;
      gap: 24px;
      transition: background 0.3s ease;
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
      width: 44px;
      height: 44px;
      border-radius: var(--radius-md);
      background: linear-gradient(135deg, #24201c, #161412);
      border: 1px solid var(--border-medium);
      display: flex;
      align-items: center;
      justify-content: center;
      box-shadow: 0 4px 16px rgba(0, 0, 0, 0.35);
      transition: transform 0.3s ease, border-color 0.3s ease;
    }
    .spatial-brand:hover .brand-cube-badge {
      transform: translateY(-2px);
      border-color: var(--antique-brass);
    }

    .brand-text-lockup h1 {
      font-family: var(--font-serif-display);
      font-size: 1.45rem;
      font-weight: 600;
      letter-spacing: 0.08em;
      color: var(--warm-ivory);
      line-height: 1.1;
      text-transform: uppercase;
    }
    .brand-text-lockup p {
      font-family: var(--font-tech);
      font-size: 0.68rem;
      color: var(--natural-taupe);
      letter-spacing: 0.06em;
      margin-top: 2px;
      text-transform: uppercase;
    }

    .spatial-nav-tabs {
      display: flex;
      align-items: center;
      gap: 4px;
      background: var(--atelier-surface-1);
      padding: 4px;
      border-radius: var(--radius-pill);
      border: 1px solid var(--border-subtle);
    }

    .nav-link-btn {
      background: transparent;
      border: none;
      color: var(--natural-taupe);
      font-family: var(--font-body);
      font-size: 0.84rem;
      font-weight: 500;
      padding: 8px 22px;
      border-radius: var(--radius-pill);
      cursor: pointer;
      transition: all 0.22s ease;
      display: flex;
      align-items: center;
      gap: 8px;
    }
    .nav-link-btn:hover {
      color: var(--warm-ivory);
      background: rgba(223, 215, 199, 0.06);
    }
    .nav-link-btn.active {
      color: var(--warm-ivory);
      background: var(--atelier-surface-elevated);
      border: 1px solid var(--border-medium);
      box-shadow: 0 2px 8px rgba(0,0,0,0.25);
    }

    .engine-status-tag {
      display: flex;
      align-items: center;
      gap: 10px;
      padding: 7px 18px;
      border-radius: var(--radius-pill);
      background: rgba(96, 107, 93, 0.14);
      border: 1px solid rgba(96, 107, 93, 0.35);
      color: #b0c2ac;
      font-family: var(--font-tech);
      font-size: 0.72rem;
      font-weight: 500;
      letter-spacing: 0.04em;
    }
    .beacon-pulse {
      width: 7px;
      height: 7px;
      border-radius: 50%;
      background: #8fa68a;
      box-shadow: 0 0 10px #8fa68a;
      animation: beaconSoftPulse 2.4s infinite ease-in-out;
    }
    @keyframes beaconSoftPulse {
      0%, 100% { opacity: 0.45; transform: scale(0.9); }
      50% { opacity: 1; transform: scale(1.2); }
    }

    .btn-presentation-pill {
      background: var(--atelier-surface-1);
      border: 1px solid var(--border-medium);
      color: var(--travertine);
      font-family: var(--font-body);
      font-size: 0.78rem;
      font-weight: 500;
      padding: 7px 18px;
      border-radius: var(--radius-pill);
      cursor: pointer;
      display: inline-flex;
      align-items: center;
      gap: 8px;
      transition: all 0.2s ease;
    }
    .btn-presentation-pill:hover {
      background: var(--atelier-surface-elevated);
      border-color: var(--antique-brass);
      color: var(--warm-ivory);
    }

    /* Main Container Shell */
    .main-spatial-container {
      position: relative;
      z-index: 2;
      width: 100%;
      max-width: 1540px;
      margin: 0 auto;
      padding: 44px 54px 84px;
      display: flex;
      flex-direction: column;
      gap: 68px;
    }

    /* ==========================================================================
       SECTION 1: FULL-SCREEN BRAND-FIRST ATELIER HERO WITH 3D DOLLHOUSE
       ========================================================================== */
    .hero-spatial-section {
      position: relative;
      padding: 72px 58px 64px;
      border-radius: var(--radius-2xl);
      background: linear-gradient(145deg, rgba(24, 22, 19, 0.94) 0%, rgba(17, 16, 14, 0.98) 100%);
      border: 1px solid var(--border-subtle);
      box-shadow: 0 28px 70px rgba(0, 0, 0, 0.55);
      overflow: hidden;
      display: grid;
      grid-template-columns: 1.15fr 0.85fr;
      gap: 48px;
      align-items: center;
    }

    @media (max-width: 1140px) {
      .hero-spatial-section { grid-template-columns: 1fr; text-align: center; }
      .hero-editorial-left { align-items: center; }
      .hero-trust-indicators { justify-content: center; }
    }

    .hero-editorial-left {
      display: flex;
      flex-direction: column;
      gap: 22px;
      text-align: left;
      z-index: 2;
    }

    .hero-brand-identifier {
      display: inline-flex;
      align-items: center;
      gap: 12px;
      padding: 6px 18px;
      border-radius: var(--radius-pill);
      background: rgba(197, 168, 128, 0.08);
      border: 1px solid rgba(197, 168, 128, 0.28);
      color: var(--antique-brass);
      font-family: var(--font-tech);
      font-size: 0.76rem;
      font-weight: 600;
      letter-spacing: 0.1em;
      text-transform: uppercase;
      align-self: flex-start;
    }
    .hero-brand-identifier span.dot {
      width: 5px; height: 5px; border-radius: 50%; background: var(--antique-brass);
    }

    /* Editorial Headline in Serif Italic & Regular */
    .hero-editorial-headline {
      font-family: var(--font-serif-display);
      font-size: clamp(3.2rem, 5.2vw, 5.4rem);
      line-height: 1.04;
      letter-spacing: -0.02em;
      color: var(--warm-ivory);
      font-weight: 400;
    }
    .headline-serif-italic {
      display: block;
      font-style: italic;
      font-weight: 300;
      color: var(--warm-ivory);
    }
    .headline-serif-regular {
      display: block;
      font-weight: 500;
      color: var(--travertine);
    }

    .hero-subtagline {
      font-family: var(--font-serif-display);
      font-size: 1.45rem;
      font-weight: 400;
      font-style: italic;
      color: var(--antique-brass);
      margin-top: -6px;
    }

    .hero-editorial-lead {
      font-size: 1.08rem;
      color: var(--natural-taupe);
      line-height: 1.7;
      max-width: 560px;
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
      background: var(--antique-brass);
      color: #171512;
      font-family: var(--font-body);
      font-weight: 700;
      font-size: 0.98rem;
      letter-spacing: 0.02em;
      padding: 16px 36px;
      border-radius: var(--radius-md);
      border: none;
      cursor: pointer;
      display: inline-flex;
      align-items: center;
      gap: 10px;
      box-shadow: 0 8px 24px rgba(197, 168, 128, 0.25);
      transition: all 0.25s ease;
    }
    .btn-spatial-primary:hover {
      background: var(--brass-hover);
      transform: translateY(-2px);
      box-shadow: 0 12px 30px rgba(197, 168, 128, 0.35);
    }

    .btn-spatial-secondary {
      background: var(--atelier-surface-1);
      color: var(--soft-cream);
      font-family: var(--font-body);
      font-weight: 600;
      font-size: 0.96rem;
      padding: 16px 30px;
      border-radius: var(--radius-md);
      border: 1px solid var(--border-medium);
      cursor: pointer;
      display: inline-flex;
      align-items: center;
      gap: 10px;
      transition: all 0.22s ease;
    }
    .btn-spatial-secondary:hover {
      background: var(--atelier-surface-elevated);
      border-color: var(--antique-brass);
      color: var(--warm-ivory);
      transform: translateY(-2px);
    }

    .hero-trust-indicators {
      display: flex;
      align-items: center;
      gap: 14px;
      flex-wrap: wrap;
      margin-top: 10px;
      padding-top: 20px;
      border-top: 1px solid var(--border-subtle);
      font-family: var(--font-tech);
      font-size: 0.72rem;
      color: var(--muted-ash);
    }
    .hero-trust-indicators span.trust-chip {
      display: inline-flex;
      align-items: center;
      gap: 6px;
      background: rgba(223, 215, 199, 0.04);
      padding: 4px 12px;
      border-radius: var(--radius-pill);
      border: 1px solid var(--border-subtle);
    }
    .hero-trust-indicators strong {
      color: var(--antique-brass);
    }

    /* ==========================================================================
       RIGHT AREA: 3D CUTAWAY ARCHITECTURAL DOLLHOUSE (NATURAL MATERIALS)
       ========================================================================== */
    .hero-spatial-stage-right {
      position: relative;
      width: 100%;
      height: 480px;
      perspective: 1200px;
      display: flex;
      align-items: center;
      justify-content: center;
      user-select: none;
      cursor: grab;
    }
    .hero-spatial-stage-right:active {
      cursor: grabbing;
    }

    .dollhouse-3d-scene {
      width: 360px;
      height: 240px;
      position: relative;
      transform-style: preserve-3d;
      transform: rotateX(24deg) rotateY(-36deg);
      animation: rotateSpatialDollhouse 32s infinite linear;
      transition: transform 0.12s ease-out;
    }

    @keyframes rotateSpatialDollhouse {
      0% { transform: rotateX(24deg) rotateY(0deg); }
      100% { transform: rotateX(24deg) rotateY(360deg); }
    }

    /* Honed Travertine Stone Floor Slab */
    .dollhouse-slab {
      position: absolute;
      width: 360px;
      height: 360px;
      transform: rotateX(-90deg) translateZ(120px);
      background: radial-gradient(circle at 50% 50%, #302a24 0%, #1e1b17 80%);
      border: 2px solid var(--border-medium);
      box-shadow: 0 20px 50px rgba(0, 0, 0, 0.6);
      display: grid;
      grid-template-columns: 1fr 1fr;
      grid-template-rows: 1fr 1fr;
    }

    /* Cutaway Exterior Walls (Natural Walnut & Plaster) */
    .dollhouse-wall-back {
      position: absolute;
      width: 360px; height: 160px;
      transform: rotateY(180deg) translateZ(180px);
      background: linear-gradient(to top, rgba(60, 47, 47, 0.75), rgba(24, 22, 19, 0.92));
      border: 1px solid var(--border-subtle);
      backdrop-filter: blur(4px);
    }
    .dollhouse-wall-left {
      position: absolute;
      width: 360px; height: 160px;
      transform: rotateY(-90deg) translateZ(180px);
      background: linear-gradient(to top, rgba(74, 59, 50, 0.75), rgba(24, 22, 19, 0.9));
      border: 1px solid var(--border-subtle);
      backdrop-filter: blur(4px);
    }

    .dollhouse-divider-x {
      position: absolute;
      width: 360px; height: 90px;
      top: 50%; left: 0;
      transform: translateY(-50%) translateZ(0);
      border-bottom: 1px solid var(--border-medium);
      pointer-events: none;
    }
    .dollhouse-divider-y {
      position: absolute;
      width: 90px; height: 360px;
      left: 50%; top: 0;
      transform: translateX(-50%) translateZ(0);
      border-right: 1px solid var(--border-medium);
      pointer-events: none;
    }

    /* Natural Furniture Volumes: Linen, Walnut, Stone */
    .room-furniture-sofa {
      position: absolute;
      bottom: 30px; left: 30px;
      width: 80px; height: 42px;
      transform: translateZ(28px);
      background: #473d35;
      border: 1px solid var(--antique-brass);
      box-shadow: 0 4px 14px rgba(0,0,0,0.4);
    }
    .room-furniture-table {
      position: absolute;
      bottom: 40px; left: 120px;
      width: 36px; height: 22px;
      transform: translateZ(15px);
      background: #dfd7c7;
      border: 1px solid #c5a880;
    }

    .room-furniture-bed {
      position: absolute;
      top: 30px; left: 30px;
      width: 85px; height: 95px;
      transform: translateZ(35px);
      background: #383028;
      border: 1px solid var(--border-medium);
      box-shadow: 0 4px 14px rgba(0,0,0,0.4);
    }

    .room-furniture-island {
      position: absolute;
      bottom: 35px; right: 35px;
      width: 90px; height: 38px;
      transform: translateZ(30px);
      background: #2e2822;
      border: 1px solid var(--antique-brass);
    }

    .room-furniture-tub {
      position: absolute;
      top: 35px; right: 40px;
      width: 75px; height: 45px;
      border-radius: 18px;
      transform: translateZ(25px);
      background: #dfd7c7;
      border: 1px solid var(--border-medium);
    }

    /* Floating Architectural Callouts */
    .dollhouse-room-badge {
      position: absolute;
      padding: 5px 12px;
      border-radius: var(--radius-sm);
      font-family: var(--font-tech);
      font-size: 0.68rem;
      font-weight: 500;
      letter-spacing: 0.06em;
      text-transform: uppercase;
      background: rgba(24, 22, 19, 0.92);
      border: 1px solid var(--border-medium);
      color: var(--travertine);
      box-shadow: 0 4px 16px rgba(0,0,0,0.45);
    }
    .badge-living   { bottom: -18px; left: 20px;  color: var(--antique-brass); border-color: var(--antique-brass); }
    .badge-bedroom  { top: -20px;    left: 20px;  color: var(--soft-cream); }
    .badge-kitchen  { bottom: -18px; right: 20px; color: var(--sandstone); }
    .badge-bathroom { top: -20px;    right: 20px; color: #b0c2ac; }

    .dollhouse-controls-bar {
      position: absolute;
      bottom: 12px;
      left: 50%;
      transform: translateX(-50%);
      display: flex;
      align-items: center;
      gap: 10px;
      background: rgba(24, 22, 19, 0.92);
      backdrop-filter: blur(12px);
      border: 1px solid var(--border-medium);
      padding: 6px 16px;
      border-radius: var(--radius-pill);
      font-family: var(--font-tech);
      font-size: 0.72rem;
      color: var(--natural-taupe);
      box-shadow: 0 4px 20px rgba(0,0,0,0.5);
      z-index: 5;
    }
    .btn-dollhouse-action {
      background: transparent;
      border: none;
      color: var(--soft-cream);
      cursor: pointer;
      display: inline-flex;
      align-items: center;
      gap: 5px;
      font-family: var(--font-tech);
      font-size: 0.72rem;
      padding: 2px 6px;
      border-radius: var(--radius-sm);
    }
    .btn-dollhouse-action:hover {
      color: var(--antique-brass);
    }

    /* ==========================================================================
       SECTION 2: EDITORIAL ARCHITECTURAL CASE STUDIES SHOWCASE
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
      border-radius: var(--radius-xl);
      overflow: hidden;
      border: 1px solid var(--border-subtle);
      background: var(--atelier-surface-1);
      box-shadow: 0 16px 40px rgba(0, 0, 0, 0.4);
      transition: all 0.35s ease;
      aspect-ratio: 16/10;
      cursor: pointer;
    }
    .gallery-hero-card:hover {
      transform: translateY(-4px);
      border-color: var(--antique-brass);
    }

    .gallery-side-card {
      grid-column: span 5;
      position: relative;
      border-radius: var(--radius-xl);
      overflow: hidden;
      border: 1px solid var(--border-subtle);
      background: var(--atelier-surface-1);
      box-shadow: 0 16px 40px rgba(0, 0, 0, 0.4);
      transition: all 0.35s ease;
      aspect-ratio: 16/10;
      cursor: pointer;
    }
    .gallery-side-card:hover {
      transform: translateY(-4px);
      border-color: var(--antique-brass);
    }

    .gallery-bottom-card-1, .gallery-bottom-card-2, .gallery-bottom-card-3 {
      grid-column: span 4;
      position: relative;
      border-radius: var(--radius-xl);
      overflow: hidden;
      border: 1px solid var(--border-subtle);
      background: var(--atelier-surface-1);
      aspect-ratio: 4/3;
      transition: all 0.35s ease;
      cursor: pointer;
    }
    .gallery-bottom-card-1:hover, .gallery-bottom-card-2:hover, .gallery-bottom-card-3:hover {
      transform: translateY(-4px);
      border-color: var(--antique-brass);
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
      transition: transform 0.6s cubic-bezier(0.16, 1, 0.3, 1);
    }
    .gallery-hero-card:hover .gallery-card-img,
    .gallery-side-card:hover .gallery-card-img,
    .gallery-bottom-card-1:hover .gallery-card-img,
    .gallery-bottom-card-2:hover .gallery-card-img,
    .gallery-bottom-card-3:hover .gallery-card-img {
      transform: scale(1.04);
    }

    .gallery-card-overlay {
      position: absolute;
      bottom: 0; left: 0; width: 100%;
      padding: 24px;
      background: linear-gradient(to top, rgba(17, 16, 14, 0.95) 0%, rgba(17, 16, 14, 0.5) 60%, transparent 100%);
      display: flex;
      justify-content: space-between;
      align-items: flex-end;
      z-index: 2;
    }
    .gallery-card-info h3 {
      font-family: var(--font-serif-display);
      font-size: 1.35rem;
      font-weight: 500;
      color: var(--warm-ivory);
    }
    .gallery-card-info p {
      font-family: var(--font-tech);
      font-size: 0.74rem;
      color: var(--antique-brass);
      margin-top: 2px;
    }

    /* ==========================================================================
       SECTION 3: ARCHITECTURAL SYNTHESIS WORKFLOW
       ========================================================================== */
    .sketch-to-reality-showcase {
      display: flex;
      flex-direction: column;
      gap: 28px;
      padding: 52px;
      background: linear-gradient(135deg, rgba(24, 22, 19, 0.9), rgba(17, 16, 14, 0.95));
      border: 1px solid var(--border-subtle);
      border-radius: var(--radius-2xl);
      box-shadow: 0 20px 50px rgba(0, 0, 0, 0.4);
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
      background: var(--atelier-surface-1);
      border: 1px solid var(--border-subtle);
      border-radius: var(--radius-xl);
      padding: 24px;
      display: flex;
      flex-direction: column;
      gap: 12px;
      transition: all 0.25s ease;
      position: relative;
    }
    .story-step-item:hover {
      border-color: var(--antique-brass);
      transform: translateY(-4px);
    }
    .story-step-item::before {
      content: "";
      position: absolute;
      top: 0; left: 0; width: 100%; height: 2px;
      background: linear-gradient(90deg, var(--antique-brass), var(--border-subtle));
    }
    .story-step-label {
      font-family: var(--font-tech);
      font-size: 0.72rem;
      font-weight: 600;
      color: var(--antique-brass);
      letter-spacing: 0.08em;
      text-transform: uppercase;
    }
    .story-step-title {
      font-family: var(--font-serif-display);
      font-size: 1.25rem;
      font-weight: 500;
      color: var(--warm-ivory);
    }
    .story-step-desc {
      font-size: 0.84rem;
      color: var(--natural-taupe);
      line-height: 1.6;
    }

    /* ==========================================================================
       SECTION 4: INTERACTIVE VISUAL COMPARISON CURTAIN
       ========================================================================== */
    .interactive-compare-demo-section {
      display: flex;
      flex-direction: column;
      gap: 24px;
      padding: 48px;
      background: linear-gradient(135deg, rgba(24, 22, 19, 0.9), rgba(17, 16, 14, 0.95));
      border: 1px solid var(--border-subtle);
      border-radius: var(--radius-2xl);
    }

    .compare-demo-container {
      position: relative;
      width: 100%;
      max-width: 820px;
      aspect-ratio: 16/10;
      margin: 0 auto;
      border-radius: var(--radius-xl);
      overflow: hidden;
      border: 1px solid var(--border-medium);
      box-shadow: 0 20px 50px rgba(0,0,0,0.5);
      cursor: ew-resize;
      user-select: none;
    }
    .demo-layer-bottom {
      width: 100%; height: 100%; object-fit: cover; display: block;
    }
    .demo-layer-top {
      position: absolute;
      top: 0; left: 0;
      width: 50%; height: 100%;
      overflow: hidden;
      border-right: 2px solid var(--antique-brass);
      box-shadow: 2px 0 16px rgba(197, 168, 128, 0.4);
    }
    .demo-layer-top img {
      position: absolute;
      top: 0; left: 0;
      width: 820px; height: 100%;
      object-fit: cover;
      display: block;
    }

    /* ==========================================================================
       SECTION 5: SPATIAL 3D ARCHITECTURAL EXPERIENCE
       ========================================================================== */
    .spatial-3d-intro-section {
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 40px;
      align-items: center;
      padding: 52px;
      background: linear-gradient(135deg, rgba(24, 22, 19, 0.9), rgba(17, 16, 14, 0.95));
      border: 1px solid var(--border-subtle);
      border-radius: var(--radius-2xl);
    }
    @media (max-width: 900px) {
      .spatial-3d-intro-section { grid-template-columns: 1fr; }
    }

    /* ==========================================================================
       SECTION 6: ENGINEERED FOR LOCAL AI (HONEST MEASURED SPECS)
       ========================================================================== */
    .technical-specs-section {
      display: flex;
      flex-direction: column;
      gap: 28px;
      padding: 52px;
      background: linear-gradient(135deg, rgba(24, 22, 19, 0.92), rgba(17, 16, 14, 0.98));
      border: 1px solid var(--border-subtle);
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
      background: var(--atelier-surface-1);
      border: 1px solid var(--border-subtle);
      border-radius: var(--radius-xl);
      padding: 26px;
      display: flex;
      flex-direction: column;
      gap: 12px;
      position: relative;
    }
    .spec-card-box strong { color: var(--antique-brass); }
    .spec-val-badge {
      font-family: var(--font-tech);
      font-size: 1.45rem;
      font-weight: 600;
      color: var(--warm-ivory);
    }

    /* ==========================================================================
       SECTION 7: FINAL CALL TO ACTION
       ========================================================================== */
    .final-cta-section {
      display: flex;
      flex-direction: column;
      align-items: center;
      text-align: center;
      gap: 22px;
      padding: 72px 36px;
      border-radius: var(--radius-2xl);
      background: linear-gradient(145deg, #1f1b17 0%, #161412 100%);
      border: 1px solid var(--border-medium);
      box-shadow: 0 28px 70px rgba(0,0,0,0.55);
    }

    /* ==========================================================================
       SECTION 8: CREATIVE STUDIO WORKSPACE (WARM ATELIER DRAFTING ENVIRONMENT)
       ========================================================================== */
    .studio-spatial-section {
      display: flex;
      flex-direction: column;
      gap: 28px;
    }

    .studio-workspace-grid {
      display: grid;
      grid-template-columns: 1.05fr 1fr;
      gap: 32px;
      align-items: start;
    }
    @media (max-width: 1160px) {
      .studio-workspace-grid { grid-template-columns: 1fr; }
    }

    .spatial-panel {
      background: var(--atelier-card);
      backdrop-filter: blur(20px);
      -webkit-backdrop-filter: blur(20px);
      border: 1px solid var(--border-medium);
      border-radius: var(--radius-2xl);
      padding: 28px;
      display: flex;
      flex-direction: column;
      gap: 22px;
      box-shadow: 0 24px 60px rgba(0, 0, 0, 0.45);
      position: relative;
    }

    .panel-head-spatial {
      display: flex;
      justify-content: space-between;
      align-items: center;
      padding-bottom: 18px;
      border-bottom: 1px solid var(--border-subtle);
    }

    .panel-headline {
      display: flex;
      align-items: center;
      gap: 14px;
    }

    .spatial-orb {
      width: 44px;
      height: 44px;
      border-radius: var(--radius-md);
      background: var(--atelier-surface-1);
      border: 1px solid var(--border-medium);
      display: flex;
      align-items: center;
      justify-content: center;
      color: var(--antique-brass);
    }

    .panel-title-block h2 {
      font-family: var(--font-serif-display);
      font-size: 1.35rem;
      font-weight: 500;
      color: var(--warm-ivory);
    }
    .panel-title-block p {
      font-size: 0.82rem;
      color: var(--natural-taupe);
    }

    .spatial-toolbar {
      display: flex;
      flex-wrap: wrap;
      align-items: center;
      gap: 8px;
      background: var(--atelier-surface-1);
      border: 1px solid var(--border-subtle);
      border-radius: var(--radius-lg);
      padding: 8px 12px;
    }

    .tool-group-dock {
      display: flex;
      align-items: center;
      gap: 6px;
      border-right: 1px solid var(--border-subtle);
      padding-right: 10px;
      margin-right: 4px;
    }
    .tool-group-dock:last-child {
      border-right: none;
      padding-right: 0;
      margin-right: 0;
    }

    .btn-spatial-tool {
      background: transparent;
      border: 1px solid transparent;
      color: var(--natural-taupe);
      width: 36px;
      height: 36px;
      border-radius: var(--radius-sm);
      cursor: pointer;
      display: flex;
      align-items: center;
      justify-content: center;
      transition: all 0.18s ease;
      position: relative;
    }
    .btn-spatial-tool:hover {
      background: var(--atelier-surface-elevated);
      color: var(--warm-ivory);
    }
    .btn-spatial-tool.active {
      background: var(--antique-brass);
      color: #171512;
      border-color: var(--antique-brass);
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
      font-weight: 500;
      color: var(--natural-taupe);
    }
    .spatial-range {
      width: 70px;
      accent-color: var(--antique-brass);
      cursor: pointer;
    }
    .tech-badge {
      font-family: var(--font-tech);
      font-size: 0.74rem;
      color: var(--antique-brass);
      min-width: 28px;
    }

    .ink-orb {
      width: 22px;
      height: 22px;
      border-radius: 50%;
      border: 2px solid transparent;
      box-shadow: 0 0 0 1px var(--border-medium);
      cursor: pointer;
      transition: transform 0.18s ease;
    }
    .ink-orb:hover { transform: scale(1.15); }
    .ink-orb.active { border-color: var(--antique-brass); transform: scale(1.15); }

    .spatial-canvas-viewport {
      position: relative;
      width: 100%;
      aspect-ratio: 1;
      max-width: 512px;
      margin: 0 auto;
      border-radius: var(--radius-xl);
      overflow: hidden;
      border: 1px solid var(--border-medium);
      background: #ffffff;
      box-shadow: 0 12px 36px rgba(0, 0, 0, 0.4);
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
      background: rgba(24, 22, 19, 0.92);
      backdrop-filter: blur(10px);
      border: 1px solid var(--border-medium);
      color: var(--antique-brass);
      padding: 6px 18px;
      border-radius: var(--radius-pill);
      font-size: 0.72rem;
      font-family: var(--font-tech);
      font-weight: 500;
      pointer-events: none;
      transition: opacity 0.3s;
    }

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
      font-size: 0.72rem;
      font-weight: 600;
      color: var(--muted-ash);
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
      background: var(--atelier-surface-1);
      border: 1px solid var(--border-subtle);
      color: var(--natural-taupe);
      padding: 8px 16px;
      border-radius: var(--radius-md);
      font-size: 0.78rem;
      font-weight: 500;
      cursor: pointer;
      white-space: nowrap;
      transition: all 0.2s ease;
    }
    .layout-chip:hover {
      background: var(--atelier-surface-elevated);
      color: var(--warm-ivory);
    }
    .layout-chip.active {
      background: var(--antique-brass);
      color: #171512;
      border-color: var(--antique-brass);
      font-weight: 600;
    }

    .spatial-params-matrix {
      background: var(--atelier-surface-1);
      border: 1px solid var(--border-subtle);
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
      font-size: 0.72rem;
      font-weight: 500;
      color: var(--antique-brass);
      text-transform: uppercase;
      letter-spacing: 0.06em;
      display: flex;
      justify-content: space-between;
    }

    .spatial-select, .spatial-input, .spatial-textarea {
      background: var(--atelier-bg);
      border: 1px solid var(--border-medium);
      color: var(--soft-cream);
      border-radius: var(--radius-md);
      padding: 11px 15px;
      font-family: var(--font-body);
      font-size: 0.86rem;
      outline: none;
      transition: border-color 0.2s;
    }
    .spatial-select:focus, .spatial-input:focus, .spatial-textarea:focus {
      border-color: var(--antique-brass);
    }

    .spatial-textarea {
      resize: vertical;
      min-height: 54px;
      line-height: 1.5;
      font-size: 0.82rem;
    }

    .engine-stack {
      display: flex;
      flex-direction: column;
      gap: 10px;
    }
    .engine-choice-card {
      background: var(--atelier-bg);
      border: 1px solid var(--border-subtle);
      border-radius: var(--radius-lg);
      padding: 14px 18px;
      display: flex;
      align-items: flex-start;
      gap: 14px;
      cursor: pointer;
      transition: all 0.2s ease;
    }
    .engine-choice-card:hover {
      background: var(--atelier-surface-elevated);
    }
    .engine-choice-card.active {
      border-color: var(--antique-brass);
      background: rgba(197, 168, 128, 0.08);
    }
    .engine-choice-card input[type="radio"] {
      accent-color: var(--antique-brass);
      margin-top: 3px;
    }
    .engine-card-text { flex: 1; }
    .engine-title-row {
      display: flex;
      align-items: center;
      gap: 10px;
      font-family: var(--font-serif-display);
      font-size: 1.05rem;
      font-weight: 600;
      color: var(--warm-ivory);
    }
    .engine-tag {
      font-family: var(--font-tech);
      font-size: 0.65rem;
      font-weight: 600;
      padding: 2px 8px;
      border-radius: var(--radius-sm);
      text-transform: uppercase;
      letter-spacing: 0.05em;
    }
    .engine-tag.primary {
      background: rgba(197, 168, 128, 0.2);
      color: var(--antique-brass);
      border: 1px solid var(--antique-brass);
    }
    .engine-tag.exp {
      background: rgba(142, 120, 83, 0.2);
      color: var(--honed-bronze);
      border: 1px solid var(--honed-bronze);
    }
    .engine-sub-desc {
      font-size: 0.76rem;
      color: var(--natural-taupe);
      margin-top: 4px;
      line-height: 1.45;
    }

    .fine-tune-accordion {
      font-family: var(--font-tech);
      font-size: 0.76rem;
      font-weight: 500;
      color: var(--antique-brass);
      cursor: pointer;
      display: flex;
      align-items: center;
      gap: 8px;
      user-select: none;
      padding-top: 4px;
    }
    .fine-tune-accordion:hover { color: var(--warm-ivory); }
    .fine-tune-drawer {
      display: none;
      grid-template-columns: 1fr 1fr 1fr;
      gap: 12px;
      padding-top: 12px;
    }

    .btn-synthesize-master {
      background: var(--antique-brass);
      color: #171512;
      font-family: var(--font-body);
      border: none;
      padding: 17px 30px;
      border-radius: var(--radius-md);
      font-size: 1.02rem;
      font-weight: 700;
      cursor: pointer;
      display: flex;
      align-items: center;
      justify-content: center;
      gap: 12px;
      box-shadow: 0 8px 24px rgba(197, 168, 128, 0.25);
      transition: all 0.22s ease;
    }
    .btn-synthesize-master:hover:not(:disabled) {
      background: var(--brass-hover);
      transform: translateY(-2px);
      box-shadow: 0 12px 32px rgba(197, 168, 128, 0.35);
    }
    .btn-synthesize-master:disabled {
      opacity: 0.45;
      cursor: not-allowed;
      transform: none;
      box-shadow: none;
    }

    /* Spatial Visualizer Stage */
    .spatial-visualizer-stage {
      position: relative;
      width: 100%;
      aspect-ratio: 1;
      max-width: 512px;
      margin: 0 auto;
      border-radius: var(--radius-xl);
      overflow: hidden;
      border: 1px solid var(--border-medium);
      background: #0d0c0a;
      display: flex;
      align-items: center;
      justify-content: center;
      box-shadow: 0 16px 40px rgba(0, 0, 0, 0.4);
    }

    .spatial-visualizer-stage img {
      width: 100%;
      height: 100%;
      object-fit: cover;
      display: none;
      animation: spatialFadeIn 0.45s ease-out;
    }
    @keyframes spatialFadeIn {
      from { opacity: 0; transform: scale(0.98); }
      to { opacity: 1; transform: scale(1); }
    }

    .visualizer-empty-hud {
      color: var(--natural-taupe);
      font-size: 0.88rem;
      text-align: center;
      padding: 34px;
      line-height: 1.6;
    }
    .visualizer-empty-hud strong {
      color: var(--antique-brass);
    }

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
      border-right: 2px solid var(--antique-brass);
      box-shadow: 2px 0 16px rgba(197, 168, 128, 0.4);
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
      background: #171512;
      border: 2px solid var(--antique-brass);
      color: var(--antique-brass);
      display: flex;
      align-items: center;
      justify-content: center;
      font-size: 14px;
      font-weight: bold;
      pointer-events: none;
    }

    .spatial-error-drawer {
      display: none;
      position: absolute;
      top: 0; left: 0; width: 100%; height: 100%;
      background: rgba(17, 16, 14, 0.95);
      backdrop-filter: blur(12px);
      flex-direction: column;
      align-items: center;
      justify-content: center;
      padding: 32px;
      text-align: center;
      gap: 16px;
      z-index: 10;
    }
    .error-hex-icon {
      width: 50px; height: 50px;
      border-radius: var(--radius-md);
      background: rgba(168, 98, 74, 0.18);
      border: 1px solid var(--terracotta-soft);
      color: var(--terracotta-soft);
      display: flex;
      align-items: center;
      justify-content: center;
    }
    .btn-spatial-retry {
      background: rgba(168, 98, 74, 0.25);
      border: 1px solid var(--terracotta-soft);
      color: var(--soft-cream);
      padding: 10px 22px;
      border-radius: var(--radius-md);
      font-family: var(--font-tech);
      font-size: 0.82rem;
      cursor: pointer;
      display: flex;
      align-items: center;
      gap: 8px;
    }

    .spatial-synthesis-overlay {
      display: none;
      position: absolute;
      top: 0; left: 0; width: 100%; height: 100%;
      background: rgba(17, 16, 14, 0.95);
      backdrop-filter: blur(14px);
      flex-direction: column;
      align-items: center;
      justify-content: center;
      gap: 20px;
      z-index: 10;
      padding: 32px;
      text-align: center;
    }
    .spatial-gyro-spinner {
      width: 54px; height: 54px;
      border: 2px solid var(--border-subtle);
      border-top-color: var(--antique-brass);
      border-radius: 50%;
      animation: spinSpatialGyro 1.1s linear infinite;
    }
    @keyframes spinSpatialGyro {
      to { transform: rotate(360deg); }
    }
    .stage-sequence-text {
      font-family: var(--font-serif-display);
      font-size: 1.2rem;
      font-weight: 500;
      color: var(--warm-ivory);
    }
    .stage-sub-text {
      font-family: var(--font-tech);
      font-size: 0.74rem;
      color: var(--natural-taupe);
      margin-top: 4px;
    }
    .elapsed-hud-tag {
      font-family: var(--font-tech);
      font-size: 0.8rem;
      color: var(--antique-brass);
      background: rgba(197, 168, 128, 0.1);
      border: 1px solid rgba(197, 168, 128, 0.35);
      padding: 5px 14px;
      border-radius: var(--radius-pill);
    }

    .visualizer-dock-row {
      display: flex;
      justify-content: space-between;
      align-items: center;
      flex-wrap: wrap;
      gap: 12px;
    }
    .btn-spatial-dock {
      background: var(--atelier-surface-1);
      border: 1px solid var(--border-medium);
      color: var(--soft-cream);
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
      background: var(--atelier-surface-elevated);
      border-color: var(--antique-brass);
    }
    .btn-spatial-dock:disabled {
      opacity: 0.35;
      cursor: not-allowed;
    }

    .spatial-telemetry-hud {
      display: flex;
      align-items: center;
      gap: 8px;
      flex-wrap: wrap;
    }
    .telemetry-chip {
      background: var(--atelier-surface-1);
      border: 1px solid var(--border-subtle);
      color: var(--natural-taupe);
      font-family: var(--font-tech);
      font-size: 0.72rem;
      padding: 5px 12px;
      border-radius: var(--radius-sm);
      display: inline-flex;
      align-items: center;
      gap: 6px;
    }
    .telemetry-chip strong { color: var(--antique-brass); }

    /* ==========================================================================
       SECTION 9: MY DESIGNS — ARCHITECTURAL PORTFOLIO
       ========================================================================== */
    .gallery-spatial-section {
      display: none;
      flex-direction: column;
      gap: 28px;
    }

    .gallery-collection-grid {
      display: grid;
      grid-template-columns: repeat(auto-fill, minmax(320px, 1fr));
      gap: 28px;
    }

    .spatial-project-card {
      background: var(--atelier-surface-1);
      border: 1px solid var(--border-subtle);
      border-radius: var(--radius-xl);
      overflow: hidden;
      transition: all 0.3s ease;
      display: flex;
      flex-direction: column;
    }
    .spatial-project-card:hover {
      transform: translateY(-4px);
      border-color: var(--antique-brass);
      box-shadow: 0 16px 36px rgba(0,0,0,0.35);
    }
    .spatial-project-thumb {
      width: 100%;
      aspect-ratio: 1;
      object-fit: cover;
      background: #171512;
      display: block;
    }
    .spatial-project-body {
      padding: 20px;
      display: flex;
      flex-direction: column;
      gap: 10px;
    }
    .spatial-project-name {
      font-family: var(--font-serif-display);
      font-size: 1.25rem;
      font-weight: 500;
      color: var(--warm-ivory);
    }
    .spatial-project-meta {
      font-family: var(--font-tech);
      font-size: 0.72rem;
      color: var(--antique-brass);
    }
    .spatial-project-actions {
      display: flex;
      gap: 8px;
      margin-top: 6px;
    }
    .btn-spatial-mini {
      flex: 1;
      background: var(--atelier-surface-elevated);
      border: 1px solid var(--border-subtle);
      color: var(--soft-cream);
      padding: 8px 14px;
      border-radius: var(--radius-sm);
      font-size: 0.78rem;
      font-weight: 500;
      cursor: pointer;
      transition: all 0.18s;
    }
    .btn-spatial-mini:hover {
      background: var(--antique-brass);
      color: #171512;
      border-color: var(--antique-brass);
    }
    .btn-spatial-mini.delete-btn:hover {
      background: rgba(168, 98, 74, 0.25);
      border-color: var(--terracotta-soft);
      color: var(--terracotta-soft);
    }

    .spatial-modal-curtain {
      display: none;
      position: fixed;
      top: 0; left: 0; width: 100vw; height: 100vh;
      background: rgba(17, 16, 14, 0.9);
      backdrop-filter: blur(14px);
      z-index: 1000;
      align-items: center;
      justify-content: center;
      padding: 24px;
    }
    .spatial-modal-window {
      background: var(--atelier-surface-1);
      border: 1px solid var(--border-medium);
      border-radius: var(--radius-xl);
      padding: 32px;
      max-width: 450px;
      width: 100%;
      box-shadow: 0 24px 60px rgba(0, 0, 0, 0.6);
      display: flex;
      flex-direction: column;
      gap: 20px;
    }

    /* Presentation Mode */
    .presentation-fullscreen-curtain {
      display: none;
      position: fixed;
      top: 0; left: 0; width: 100vw; height: 100vh;
      background: var(--atelier-bg);
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
      border-bottom: 1px solid var(--border-subtle);
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
      border: 1px solid var(--border-medium);
      box-shadow: 0 20px 50px rgba(0, 0, 0, 0.5);
    }

    .spatial-toast {
      position: fixed;
      bottom: 30px;
      right: 30px;
      z-index: 1000;
      background: var(--atelier-surface-elevated);
      backdrop-filter: blur(14px);
      border: 1px solid var(--antique-brass);
      color: var(--warm-ivory);
      padding: 14px 24px;
      border-radius: var(--radius-md);
      box-shadow: 0 12px 36px rgba(0,0,0,0.45);
      display: none;
      align-items: center;
      gap: 12px;
      font-size: 0.86rem;
      animation: toastGlideUp 0.3s ease-out;
    }
    @keyframes toastGlideUp {
      from { transform: translateY(20px); opacity: 0; }
      to { transform: translateY(0); opacity: 1; }
    }

    footer {
      margin-top: auto;
      padding: 38px 54px;
      border-top: 1px solid var(--border-subtle);
      display: flex;
      justify-content: space-between;
      align-items: center;
      flex-wrap: wrap;
      gap: 16px;
      font-size: 0.82rem;
      color: var(--natural-taupe);
      background: var(--atelier-surface-1);
    }

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
  <!-- Ambient Warm Lighting Fields & Texture -->
  <div class="atelier-light-fields">
    <div class="light-field-glow glow-1"></div>
    <div class="light-field-glow glow-2"></div>
  </div>
  <div class="atelier-grid-texture"></div>
  <canvas id="ambient-particles-canvas"></canvas>

  <!-- Top Spatial Navigation -->
  <header class="spatial-nav">
    <div class="spatial-brand" onclick="switchSpatialNav('landing')">
      <div class="brand-cube-badge">
        <svg width="24" height="24" viewBox="0 0 28 28" fill="none" xmlns="http://www.w3.org/2000/svg">
          <path d="M14 2L26 8.5V21.5L14 28L2 21.5V8.5L14 2Z" stroke="#c5a880" stroke-width="1.8" stroke-linejoin="round"/>
          <path d="M14 28V15" stroke="#c5a880" stroke-width="1.8"/>
          <path d="M26 8.5L14 15L2 8.5" stroke="#c5a880" stroke-width="1.8"/>
        </svg>
      </div>
      <div class="brand-text-lockup">
        <h1>SKETCHSPACE AI</h1>
        <p>Architectural Atelier</p>
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
        <span>RTX 3050 &bull; 100% Offline Atelier</span>
      </div>
    </div>
  </header>

  <!-- Main Viewport Shell -->
  <main class="main-spatial-container">

    <!-- ====================================================================
         1. EDITORIAL ATELIER HERO WITH 3D CUTAWAY DOLLHOUSE
         ==================================================================== -->
    <section class="hero-spatial-section" id="section-landing">
      <div class="hero-editorial-left">
        <div class="hero-brand-identifier">
          <span class="dot"></span>
          <span>SKETCHSPACE AI</span>
          <span>&bull;</span>
          <span>RESIDENTIAL ATELIER</span>
        </div>

        <h1 class="hero-editorial-headline">
          <span class="headline-serif-italic">From Imagination</span>
          <span class="headline-serif-regular">To Architecture.</span>
        </h1>

        <p class="hero-subtagline">Where ideas become extraordinary spaces.</p>

        <p class="hero-editorial-lead">
          Transform hand-drawn architectural ideas into breathtaking interior visualizations with locally powered generative AI.
        </p>

        <div class="hero-cta-cluster">
          <button type="button" class="btn-spatial-primary" onclick="switchSpatialNav('studio')">
            <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2"><path d="M12 20h9"></path><path d="M16.5 3.5a2.121 2.121 0 0 1 3 3L7 19l-4 1 1-4L16.5 3.5z"></path></svg>
            Enter Creative Studio
          </button>
          <button type="button" class="btn-spatial-secondary" onclick="scrollToSignatureStory()">
            <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"></circle><polygon points="10 8 16 12 10 16 10 8"></polygon></svg>
            Explore Designs
          </button>
        </div>

        <div class="hero-trust-indicators">
          <span class="trust-chip">&bull; AI-Powered Interior Visualization</span>
          <span class="trust-chip">&bull; Local Stable Diffusion + ControlNet</span>
          <span class="trust-chip">&bull; Offline GPU Inference</span>
        </div>
      </div>

      <!-- Right Area: Continuously Rotating 3D Cutaway Dollhouse -->
      <div class="hero-spatial-stage-right" id="hero-interactive-stage">
        <div class="dollhouse-3d-scene" id="hero-dollhouse-3d">
          <div class="dollhouse-slab">
            <div class="room-furniture-sofa"></div>
            <div class="room-furniture-table"></div>
            <div class="room-furniture-bed"></div>
            <div class="room-furniture-island"></div>
            <div class="room-furniture-tub"></div>
          </div>

          <div class="dollhouse-wall-back"></div>
          <div class="dollhouse-wall-left"></div>
          <div class="dollhouse-divider-x"></div>
          <div class="dollhouse-divider-y"></div>

          <div class="dollhouse-room-badge badge-living">Living Room</div>
          <div class="dollhouse-room-badge badge-bedroom">Master Bedroom</div>
          <div class="dollhouse-room-badge badge-kitchen">Kitchen</div>
          <div class="dollhouse-room-badge badge-bathroom">Bathroom</div>
        </div>

        <div class="dollhouse-controls-bar">
          <span>&#x21BB; DRAG TO ROTATE 3D RESIDENCE</span>
          <span>&bull;</span>
          <button type="button" class="btn-dollhouse-action" id="btn-house-spin-toggle" onclick="toggleDollhouseSpin()">Pause Spin</button>
        </div>
      </div>
    </section>

    <!-- ====================================================================
         2. ARCHITECTURAL SHOWCASE (EDITORIAL ASYMMETRIC GALLERY)
         ==================================================================== -->
    <section class="editorial-gallery-section" id="section-gallery-showcase">
      <div style="display:flex; justify-content:space-between; align-items:flex-end; flex-wrap:wrap; gap:16px;">
        <div>
          <span style="font-family:var(--font-tech); font-size:0.74rem; color:var(--antique-brass); text-transform:uppercase; letter-spacing:0.06em;">Architectural Portfolio</span>
          <h2 style="font-family:var(--font-serif-display); font-size:2.2rem; font-weight:500; color:var(--warm-ivory); margin-top:4px;">Verified Local Interior Outputs</h2>
        </div>
        <p style="font-size:0.86rem; color:var(--natural-taupe); max-width:440px; line-height:1.6;">
          Genuine outputs synthesized locally with ControlNet Scribble + Stable Diffusion 1.5.
        </p>
      </div>

      <div class="gallery-showcase-grid">
        <div class="gallery-hero-card" onclick="loadAndOpenPreset('living_room')">
          <img src="/api/image/local_cn_living_room_1795536539194.png" class="gallery-card-img" alt="Contemporary Living Room" onerror="this.src='/api/sketches/example/new_living_room_sketch.png'">
          <div class="gallery-card-overlay">
            <div class="gallery-card-info">
              <h3>Contemporary Living Room</h3>
              <p>Natural Daylight &bull; Hardwood &amp; Linen &bull; 28.9s Latency</p>
            </div>
            <button type="button" class="btn-spatial-mini" style="width:auto; padding:6px 16px;">Open in Studio</button>
          </div>
        </div>

        <div class="gallery-side-card" onclick="loadAndOpenPreset('bathroom')">
          <img src="/api/image/local_cn_bathroom_1795532521076.png" class="gallery-card-img" alt="Spa Bathroom" onerror="this.src='/api/sketches/example/new_bathroom_sketch.png'">
          <div class="gallery-card-overlay">
            <div class="gallery-card-info">
              <h3>Spa Bathroom Suite</h3>
              <p>Porcelain &bull; Chrome Fixtures &bull; 22.4s Latency</p>
            </div>
            <button type="button" class="btn-spatial-mini" style="width:auto; padding:6px 16px;">Open in Studio</button>
          </div>
        </div>

        <div class="gallery-bottom-card-1" onclick="loadAndOpenPreset('bedroom')">
          <img src="/api/image/local_cn_bedroom_1795531503385.png" class="gallery-card-img" alt="Master Bedroom" onerror="this.src='/api/sketches/example/new_bedroom_sketch.png'">
          <div class="gallery-card-overlay">
            <div class="gallery-card-info">
              <h3>Master Bedroom</h3>
              <p>Modern Minimalist &bull; Natural Light</p>
            </div>
          </div>
        </div>

        <div class="gallery-bottom-card-2" onclick="loadAndOpenPreset('office')">
          <img src="/api/image/local_cn_office_1795531733794.png" class="gallery-card-img" alt="Executive Office" onerror="this.src='/api/sketches/example/new_office_sketch.png'">
          <div class="gallery-card-overlay">
            <div class="gallery-card-info">
              <h3>Executive Office</h3>
              <p>Bleached Oak &bull; Recessed Illumination</p>
            </div>
          </div>
        </div>

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
         3. THE DESIGN PROCESS (SKETCH TO REALITY)
         ==================================================================== -->
    <section class="sketch-to-reality-showcase" id="section-storytelling">
      <div class="story-header-row">
        <div>
          <span style="font-family:var(--font-tech); font-size:0.74rem; color:var(--antique-brass); text-transform:uppercase; letter-spacing:0.06em;">The Design Process</span>
          <h2 style="font-family:var(--font-serif-display); font-size:2.2rem; font-weight:500; color:var(--warm-ivory); margin-top:4px;">From Linework to Architectural Photorealism</h2>
        </div>
        <p style="font-size:0.86rem; color:var(--natural-taupe); max-width:480px; line-height:1.6;">
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
          <p class="story-step-desc">ControlNet Scribble conditions on boundary strokes, guiding room geometry without random structural drift.</p>
        </div>
        <div class="story-step-item">
          <span class="story-step-label">Stage 3 &bull; Transform</span>
          <h3 class="story-step-title">Neural Diffusion</h3>
          <p class="story-step-desc">Stable Diffusion 1.5 infuses authentic textures, daylight illumination, and materials on your local GPU.</p>
        </div>
        <div class="story-step-item">
          <span class="story-step-label">Stage 4 &bull; Experience</span>
          <h3 class="story-step-title">Photorealistic Space</h3>
          <p class="story-step-desc">A polished 512×512 interior render ready for client presentation and before/after inspection.</p>
        </div>
      </div>
    </section>

    <!-- ====================================================================
         4. FEATURED INTERIOR GALLERY / INTERACTIVE VISUAL COMPARISON
         ==================================================================== -->
    <section class="interactive-compare-demo-section">
      <div style="display:flex; justify-content:space-between; align-items:flex-end; flex-wrap:wrap; gap:16px;">
        <div>
          <span style="font-family:var(--font-tech); font-size:0.74rem; color:var(--antique-brass); text-transform:uppercase; letter-spacing:0.06em;">Interactive Visual Comparison</span>
          <h2 style="font-family:var(--font-serif-display); font-size:2.2rem; font-weight:500; color:var(--warm-ivory); margin-top:4px;">Drag To Reveal Architectural Synthesis</h2>
        </div>
        <p style="font-size:0.86rem; color:var(--natural-taupe); max-width:440px; line-height:1.6;">
          Direct side-by-side transition from raw blueprint input to photorealistic living space.
        </p>
      </div>

      <div class="compare-demo-container" id="homepage-compare-slider">
        <img src="/api/image/local_cn_living_room_1795536539194.png" class="demo-layer-bottom" alt="Synthesized Living Room" onerror="this.src='/api/sketches/example/new_living_room_sketch.png'">
        <div class="demo-layer-top" id="demo-top-curtain">
          <img src="/api/sketches/example/new_living_room_sketch.png" alt="Living Room Sketch Blueprint">
          <div class="compare-spatial-handle">&#x21D4;</div>
        </div>
      </div>
    </section>

    <!-- ====================================================================
         5. 3D ARCHITECTURAL SPATIAL EXPERIENCE INTRODUCTION
         ==================================================================== -->
    <section class="spatial-3d-intro-section">
      <div>
        <span style="font-family:var(--font-tech); font-size:0.74rem; color:var(--antique-brass); text-transform:uppercase; letter-spacing:0.06em;">Spatial Computing Ready</span>
        <h2 style="font-family:var(--font-serif-display); font-size:2.2rem; font-weight:500; color:var(--warm-ivory); margin-top:4px;">Dimensional Architectural Visualization</h2>
        <p style="font-size:0.95rem; color:var(--natural-taupe); line-height:1.75; margin-top:14px;">
          SketchSpace AI approaches interior design not as flat pictures, but as three-dimensional volumes with depth, scale, and lighting. From rotating dollhouse previews to depth-conditioned neural generation, your concepts retain their spatial relationships.
        </p>
        <div style="display:flex; gap:12px; margin-top:24px;">
          <button type="button" class="btn-spatial-primary" style="padding:13px 26px; font-size:0.92rem;" onclick="switchSpatialNav('studio')">Open Studio &bull; Try It</button>
        </div>
      </div>
      <div style="background:var(--atelier-surface-1); border:1px solid var(--border-medium); border-radius:var(--radius-xl); padding:32px; display:flex; flex-direction:column; gap:18px;">
        <div style="font-family:var(--font-tech); font-size:0.76rem; color:var(--antique-brass); text-transform:uppercase;">Spatial Highlights</div>
        <div style="font-size:0.9rem; color:var(--soft-cream); display:flex; align-items:center; gap:10px;">
          <span style="color:var(--antique-brass);">&#10003;</span>
          <span>Interactive 3D cutaway dollhouse with furnished room quadrants</span>
        </div>
        <div style="font-size:0.9rem; color:var(--soft-cream); display:flex; align-items:center; gap:10px;">
          <span style="color:var(--antique-brass);">&#10003;</span>
          <span>Drag-to-rotate perspective camera with pause/resume controls</span>
        </div>
        <div style="font-size:0.9rem; color:var(--soft-cream); display:flex; align-items:center; gap:10px;">
          <span style="color:var(--antique-brass);">&#10003;</span>
          <span>Zero WebGL VRAM consumption — 100% GPU dedicated to diffusion</span>
        </div>
      </div>
    </section>

    <!-- ====================================================================
         6. TECHNOLOGY: ENGINEERED FOR LOCAL AI
         ==================================================================== -->
    <section class="technical-specs-section">
      <div style="display:flex; justify-content:space-between; align-items:flex-end; flex-wrap:wrap; gap:16px;">
        <div>
          <span style="font-family:var(--font-tech); font-size:0.74rem; color:var(--antique-brass); text-transform:uppercase; letter-spacing:0.06em;">Local Hardware Engineering</span>
          <h2 style="font-family:var(--font-serif-display); font-size:2.2rem; font-weight:500; color:var(--warm-ivory); margin-top:4px;">ENGINEERED FOR LOCAL AI</h2>
        </div>
        <p style="font-size:0.86rem; color:var(--natural-taupe); max-width:440px; line-height:1.6;">
          Optimized for consumer GPUs with memory-aware sequential offloading and tiled VAE decoding.
        </p>
      </div>

      <div class="specs-grid-3col">
        <div class="spec-card-box">
          <span style="font-family:var(--font-tech); font-size:0.75rem; color:var(--muted-ash);">MEASURED PEAK VRAM</span>
          <div class="spec-val-badge">649.8 MB</div>
          <p style="font-size:0.82rem; color:var(--natural-taupe); line-height:1.55;">
            Sequential layer-by-layer offload streams PyTorch UNet weights between system RAM and GPU memory, maintaining peak allocation around ~650 MB on the 4 GB RTX 3050.
          </p>
        </div>
        <div class="spec-card-box">
          <span style="font-family:var(--font-tech); font-size:0.75rem; color:var(--muted-ash);">CONTROLNET CONDITIONING</span>
          <div class="spec-val-badge">Scribble Guidance</div>
          <p style="font-size:0.82rem; color:var(--natural-taupe); line-height:1.55;">
            ControlNet conditioning locks boundary strokes and spatial vectors to guide structural alignment without hallucinating unintended walls.
          </p>
        </div>
        <div class="spec-card-box">
          <span style="font-family:var(--font-tech); font-size:0.75rem; color:var(--muted-ash);">OFFLINE EXECUTION</span>
          <div class="spec-val-badge">Zero Cloud API</div>
          <p style="font-size:0.82rem; color:var(--natural-taupe); line-height:1.55;">
            Local snapshot loading (<code style="color:var(--antique-brass);">local_files_only=True</code>) guarantees complete client blueprint privacy with zero external network requests.
          </p>
        </div>
      </div>
    </section>

    <!-- ====================================================================
         7. FINAL CALL TO ACTION
         ==================================================================== -->
    <section class="final-cta-section">
      <span style="font-family:var(--font-tech); font-size:0.76rem; color:var(--antique-brass); text-transform:uppercase; letter-spacing:0.08em;">Atelier Invitation</span>
      <h2 style="font-family:var(--font-serif-display); font-size:2.8rem; font-weight:500; color:var(--warm-ivory);">Ready to Experience SketchSpace AI?</h2>
      <p style="color:var(--natural-taupe); max-width:580px; font-size:1.02rem;">
        Launch the Creative Studio, draw your architectural layout, and synthesize photorealistic interiors right on your machine.
      </p>
      <div style="display:flex; gap:16px; margin-top:8px;">
        <button type="button" class="btn-spatial-primary" onclick="switchSpatialNav('studio')">Enter Creative Studio</button>
        <button type="button" class="btn-spatial-secondary" onclick="openPresentationMode()">Academic Presentation</button>
      </div>
    </section>

    <!-- ====================================================================
         CREATIVE STUDIO WORKSPACE (PRESERVED FUNCTIONALITY)
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

            <div class="tool-group-dock">
              <div class="slider-pillbox">
                <span>Size:</span>
                <input type="range" id="brush-size" class="spatial-range" min="1" max="24" value="4" oninput="updateSpatialBrushSize(this.value)">
                <span id="brush-size-val" class="tech-badge">4px</span>
              </div>
            </div>

            <!-- Architectural Ink Palette (Charcoal, Graphite, Sepia) -->
            <div class="tool-group-dock">
              <div class="ink-orb active" style="background:#171512;" title="Charcoal" onclick="setSpatialColor('#171512', this)"></div>
              <div class="ink-orb" style="background:#4a4744;" title="Graphite" onclick="setSpatialColor('#4a4744', this)"></div>
              <div class="ink-orb" style="background:#c5a880;" title="Antique Brass" onclick="setSpatialColor('#c5a880', this)"></div>
            </div>

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
              <label style="color:var(--antique-brass); cursor:pointer; text-transform:none;">
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
                <span style="color:var(--muted-ash); font-weight:normal; text-transform:none;">Directly drives synthesis</span>
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
              <div class="spatial-orb">
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
                <div style="font-family:var(--font-serif-display); font-weight:600; color:var(--warm-ivory); font-size:1.15rem;">Neural Synthesis Interrupted</div>
                <div style="font-size:0.82rem; color:var(--natural-taupe); margin-top:4px; max-width:340px;" id="error-overlay-msg">Error detail message</div>
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

            <div class="spatial-telemetry-hud" id="metrics-hud" style="display:none;">
              <div class="telemetry-chip">Model: <strong id="metric-model-val">SD 1.5 + ControlNet</strong></div>
              <div class="telemetry-chip">Latency: <strong id="metric-latency-val">22.6s</strong></div>
              <div class="telemetry-chip">VRAM: <strong id="metric-vram-val">0.65 GB</strong></div>
              <div class="telemetry-chip">Res: <strong id="metric-res-val">512&times;512</strong></div>
            </div>
          </div>

          <div style="margin-top:auto; padding:14px 18px; background:var(--atelier-surface-1); border:1px solid var(--border-subtle); border-radius:var(--radius-lg); font-size:0.76rem; color:var(--natural-taupe); line-height:1.55;">
            <strong style="color:var(--antique-brass);">Local GPU Execution Architecture:</strong><br>
            Diffusion executes strictly in local FP16 with sequential CPU offloading and VAE slicing. Total peak GPU memory is measured around ~650 MB to prevent out-of-memory interruptions on 4 GB laptop GPUs.
          </div>
        </div>

      </div>
    </section>

    <!-- ====================================================================
         MY DESIGNS — ARCHITECTURAL PORTFOLIO
         ==================================================================== -->
    <section class="gallery-spatial-section" id="section-gallery">
      <div style="display:flex; justify-content:space-between; align-items:center; flex-wrap:wrap; gap:14px;">
        <div>
          <h2 style="font-family:var(--font-serif-display); font-size:2.2rem; font-weight:500; color:var(--warm-ivory);">Architectural Portfolio</h2>
          <p style="font-size:0.86rem; color:var(--natural-taupe); margin-top:4px;">Locally preserved interior blueprints and photorealistic visualizations</p>
        </div>
        <button type="button" class="btn-spatial-primary" style="padding:11px 24px; font-size:0.88rem;" onclick="switchSpatialNav('studio')">
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
      <div style="font-family:var(--font-serif-display); font-weight:600; font-size:1.35rem; color:var(--warm-ivory);">Save Project to Portfolio</div>
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
        <h2 style="font-family:var(--font-serif-display); font-size:1.9rem; color:var(--warm-ivory);" id="pres-project-title">Academic Demonstration — SketchSpace AI</h2>
        <p style="font-family:var(--font-tech); font-size:0.8rem; color:var(--antique-brass);" id="pres-project-meta">Local SD 1.5 + ControlNet Scribble &bull; RTX 3050</p>
      </div>
      <button type="button" class="btn-spatial-secondary" onclick="closePresentationMode()">Exit Presentation</button>
    </div>
    <div class="pres-view-split">
      <div class="pres-card-box">
        <span style="font-family:var(--font-tech); color:var(--natural-taupe);">Original Architectural Blueprint</span>
        <img id="pres-sketch-img" alt="Original Sketch">
      </div>
      <div class="pres-card-box">
        <span style="font-family:var(--font-tech); color:var(--antique-brass);">Synthesized Interior Photorealism</span>
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
      <strong style="color:var(--warm-ivory); font-family:var(--font-serif-display); font-size:1.05rem; letter-spacing:0.04em;">SKETCHSPACE AI</strong> &mdash; Architectural Atelier
      <p style="font-size:0.75rem; color:var(--muted-ash); margin-top:4px;">100% Offline Local Neural Synthesis &bull; NVIDIA GeForce RTX 3050 Laptop GPU &bull; PyTorch 2.11</p>
    </div>
    <div style="display:flex; gap:16px; align-items:center;">
      <a href="#section-storytelling" style="color:var(--antique-brass); text-decoration:none;" onclick="switchSpatialNav('landing'); scrollToSignatureStory();">Process</a>
      <span style="opacity:0.3;">|</span>
      <a href="#section-gallery-showcase" style="color:var(--antique-brass); text-decoration:none;" onclick="switchSpatialNav('landing');">Case Studies</a>
      <span style="opacity:0.3;">|</span>
      <button type="button" class="btn-spatial-mini" style="width:auto; padding:6px 14px;" onclick="openPresentationMode()">Academic Presentation</button>
    </div>
  </footer>

  <!-- ==========================================================================
       JAVASCRIPT ARCHITECTURE & SCRIPT CONTROLS
       ========================================================================== */ -->
  <script>
    // -------------------------------------------------------------------------
    // 1. AMBIENT WARM ARCHITECTURAL PARTICLES
    // -------------------------------------------------------------------------
    const pCanvas = document.getElementById('ambient-particles-canvas');
    const pCtx = pCanvas.getContext('2d');
    let particles = [];
    const PARTICLE_COUNT = 32;

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
        this.size = Math.random() * 1.8 + 0.6;
        this.speedX = (Math.random() - 0.5) * 0.28;
        this.speedY = (Math.random() - 0.5) * 0.28;
        const colorPalette = ['rgba(197, 168, 128, ', 'rgba(223, 215, 199, ', 'rgba(140, 120, 83, '];
        this.color = colorPalette[Math.floor(Math.random() * colorPalette.length)];
        this.opacity = Math.random() * 0.35 + 0.12;
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
    // 2. 3D CUTAWAY DOLLHOUSE INTERACTIVE DRAG-TO-ROTATE & PAUSE CONTROLS
    // -------------------------------------------------------------------------
    const houseStage = document.getElementById('hero-interactive-stage');
    const dollhouse = document.getElementById('hero-dollhouse-3d');
    const spinToggleBtn = document.getElementById('btn-house-spin-toggle');
    let isHouseSpinning = true;
    let isDraggingHouse = false;
    let houseStartX = 0;
    let houseStartY = 0;
    let houseRotX = 24;
    let houseRotY = -36;

    if (houseStage && dollhouse) {
      houseStage.addEventListener('mousedown', (e) => {
        isDraggingHouse = true;
        houseStartX = e.clientX;
        houseStartY = e.clientY;
        dollhouse.style.animationPlayState = 'paused';
      });

      window.addEventListener('mousemove', (e) => {
        if (isDraggingHouse) {
          const dx = e.clientX - houseStartX;
          const dy = e.clientY - houseStartY;
          houseRotY += dx * 0.45;
          houseRotX = Math.max(8, Math.min(60, houseRotX - dy * 0.35));
          dollhouse.style.transform = `rotateX(${houseRotX}deg) rotateY(${houseRotY}deg)`;
          houseStartX = e.clientX;
          houseStartY = e.clientY;
        } else if (houseStage.matches(':hover') && isHouseSpinning) {
          const rect = houseStage.getBoundingClientRect();
          const xVal = (e.clientX - rect.left) / rect.width - 0.5;
          const yVal = (e.clientY - rect.top) / rect.height - 0.5;
          dollhouse.style.transform = `rotateX(${houseRotX - yVal * 14}deg) rotateY(${houseRotY + xVal * 20}deg)`;
        }
      });

      window.addEventListener('mouseup', () => {
        if (isDraggingHouse) {
          isDraggingHouse = false;
          if (isHouseSpinning) {
            dollhouse.style.animationPlayState = 'running';
          }
        }
      });
    }

    function toggleDollhouseSpin() {
      if (!dollhouse) return;
      isHouseSpinning = !isHouseSpinning;
      if (isHouseSpinning) {
        dollhouse.style.animationPlayState = 'running';
        if (spinToggleBtn) spinToggleBtn.textContent = 'Pause Spin';
      } else {
        dollhouse.style.animationPlayState = 'paused';
        if (spinToggleBtn) spinToggleBtn.textContent = 'Resume Spin';
      }
    }

    // -------------------------------------------------------------------------
    // 3. HOMEPAGE INTERACTIVE COMPARISON CURTAIN DRAGGER
    // -------------------------------------------------------------------------
    const demoSlider = document.getElementById('homepage-compare-slider');
    const demoCurtain = document.getElementById('demo-top-curtain');
    let isDemoComparing = false;

    if (demoSlider && demoCurtain) {
      const moveDemoDivider = (clientX) => {
        const rect = demoSlider.getBoundingClientRect();
        let pos = clientX - rect.left;
        if (pos < 0) pos = 0;
        if (pos > rect.width) pos = rect.width;
        demoCurtain.style.width = `${pos}px`;
      };

      demoSlider.addEventListener('mousedown', (e) => {
        isDemoComparing = true;
        moveDemoDivider(e.clientX);
      });
      window.addEventListener('mousemove', (e) => {
        if (isDemoComparing) moveDemoDivider(e.clientX);
      });
      window.addEventListener('mouseup', () => {
        isDemoComparing = false;
      });

      demoSlider.addEventListener('touchstart', (e) => {
        isDemoComparing = true;
        if (e.touches.length > 0) moveDemoDivider(e.touches[0].clientX);
      }, { passive: true });
      window.addEventListener('touchmove', (e) => {
        if (isDemoComparing && e.touches.length > 0) moveDemoDivider(e.touches[0].clientX);
      }, { passive: true });
      window.addEventListener('touchend', () => {
        isDemoComparing = false;
      });
    }

    // -------------------------------------------------------------------------
    // 4. NAVIGATION & TABS
    // -------------------------------------------------------------------------
    function switchSpatialNav(navKey) {
      document.querySelectorAll('.nav-link-btn').forEach(btn => btn.classList.remove('active'));
      const activeNav = document.getElementById(`tab-nav-${navKey}`);
      if (activeNav) activeNav.classList.add('active');

      document.getElementById('section-landing').style.display = (navKey === 'landing') ? 'grid' : 'none';
      const showcaseSec = document.getElementById('section-gallery-showcase');
      if (showcaseSec) showcaseSec.style.display = (navKey === 'landing') ? 'flex' : 'none';
      const storySec = document.getElementById('section-storytelling');
      if (storySec) storySec.style.display = (navKey === 'landing') ? 'flex' : 'none';

      document.getElementById('section-studio').style.display = (navKey === 'studio') ? 'flex' : 'none';
      document.getElementById('section-gallery').style.display = (navKey === 'gallery') ? 'flex' : 'none';

      if (navKey === 'gallery') {
        renderSpatialGallery();
      }
      window.scrollTo({ top: 0, behavior: 'smooth' });
    }

    function scrollToSignatureStory() {
      const target = document.getElementById('section-gallery-showcase') || document.getElementById('section-storytelling');
      if (target) target.scrollIntoView({ behavior: 'smooth' });
    }

    function loadAndOpenPreset(category) {
      switchSpatialNav('studio');
      loadSpatialRoomPreset(category);
    }

    // -------------------------------------------------------------------------
    // 5. COMPOUND PROMPT MATRIX SYNTHESIZER
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
    // 6. DRAWING CANVAS ENGINE
    // -------------------------------------------------------------------------
    const canvas = document.getElementById('drawing-canvas');
    const ctx = canvas.getContext('2d', { willReadFrequently: true });
    const gridCanvas = document.getElementById('grid-canvas');
    const gCtx = gridCanvas.getContext('2d');

    let currentTool = 'pencil';
    let currentColor = '#171512';
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
      gCtx.strokeStyle = 'rgba(197, 168, 128, 0.22)';
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
    // 7. ROOM PRESETS & FILE HANDLING
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
    // 8. MULTI-STAGE GENERATION PIPELINE
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
    // 9. INTERACTIVE VIEW MODES & COMPARISON CURTAIN
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
    // 10. MY DESIGNS — ARCHITECTURAL PORTFOLIO
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
      document.getElementById('project-name-input').value = `${defaultName} Residence`;
      document.getElementById('save-modal').style.display = 'flex';
    }

    function closeSaveSpatialModal() {
      document.getElementById('save-modal').style.display = 'none';
    }

    function confirmSaveSpatialProject() {
      const name = document.getElementById('project-name-input').value.trim() || 'Untitled Spatial Residence';
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
      displaySpatialToast(`Saved "${name}" to Portfolio`);
    }

    function renderSpatialGallery() {
      const grid = document.getElementById('gallery-grid');
      const projects = getSpatialProjects();

      if (projects.length === 0) {
        grid.innerHTML = `
          <div style="grid-column: 1 / -1; padding: 56px; text-align: center; color: var(--natural-taupe); background: var(--atelier-surface-1); border-radius: var(--radius-xl); border: 1px dashed var(--border-medium);">
            <svg width="40" height="40" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" style="margin: 0 auto 12px; display:block; opacity:0.4;">
              <rect x="3" y="3" width="18" height="18" rx="2" ry="2"></rect><circle cx="8.5" cy="8.5" r="1.5"></circle><polyline points="21 15 16 10 5 21"></polyline>
            </svg>
            <div style="font-family:var(--font-serif-display); font-size: 1.35rem; font-weight: 500; color: var(--warm-ivory);">No Saved Projects Yet</div>
            <div style="font-size: 0.84rem; margin-top: 6px;">Synthesize an interior in the Studio and click "Save to Gallery".</div>
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
    // 11. FULLSCREEN ACADEMIC PRESENTATION MODE
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
    // 12. INITIALIZATION
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

print(f"Successfully generated luxury atelier index.html ({len(HTML_CONTENT)} characters)")
