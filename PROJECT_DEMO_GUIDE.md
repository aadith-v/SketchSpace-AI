# SketchSpace AI — Project Demonstration & Viva Guide

This document is a comprehensive demonstration script and technical reference for presenting **SketchSpace AI** during academic reviews, project demonstrations, and evaluations.

---

## 1. Project Pitch & Academic Value

* **Title**: SketchSpace AI: Interactive Sketch-to-Photorealistic Interior Synthesis with Dual-Engine Architecture
* **Core Contribution**: A consumer-hardware, 100% offline interior design studio that bridges the gap between rapid interactive wireframing (sub-100ms CPU GANs) and high-fidelity photorealistic synthesis (diffusion-conditioned ControlNet) within a strict 4 GB GPU VRAM envelope.
* **Key Innovations**:
  1. **Dual-Tier Generative Architecture**: Enables immediate wireframe feedback via custom-trained Pix2Pix U-Nets (Compound Edge+SSIM loss) and final photorealistic rendering via Stable Diffusion 1.5 + ControlNet Scribble.
  2. **Zero-Copy Memory-Staged Inference**: Allows 512×512 diffusion models to run safely on a 4 GB laptop GPU (NVIDIA RTX 3050) without out-of-memory errors by using sequential model CPU offloading and attention slicing.
  3. **Strict Concurrency Protection**: Thread-safe locking guarantees that incoming requests during active generation receive clear HTTP 503 busy responses rather than crashing host memory.
  4. **Fully Offline Interactive Canvas**: Users draw architectural rooms freely, tweak prompts, compare input-to-output alignment, and export high-resolution assets without internet access or paid APIs.

---

## 2. Step-by-Step Live Demonstration Script

Follow this sequential walkthrough during a live project presentation:

### Step 1: Open Application & Highlight Hardware Profile
1. Launch the server via `start_windows.bat` or `.\start_windows.ps1`.
2. Open `http://127.0.0.1:8000`.
3. Point out the top header badges:
   * **"100% Offline Local Engine"** (pulsing green dot).
   * **"NVIDIA RTX 3050 (4GB FP16 Offload)"** hardware detection.
4. Mention that the system requires **zero cloud tokens, zero subscriptions, and zero internet connectivity**.

### Step 2: Demonstrate the Interactive Canvas
1. Explain that the canvas is a native HTML5 drawing surface (not a static preloaded image).
2. Click the **Pencil Tool** and draw a simple room box:
   * Draw four walls.
   * Draw a bed in the center and two bedside rectangles.
   * Draw a window opening on the top wall.
3. Demonstrate editing features:
   * Change brush size using the **Size slider** (e.g. 4px to 10px).
   * Use the **Eraser Tool** to fix a stroke.
   * Press `Ctrl+Z` to show the **Undo** history stack and `Ctrl+Y` for **Redo**.
   * Click **Download Sketch** to show that client-side vector/raster export works.

### Step 3: Showcase Category-Aware Prompts
1. In the **Room Category Preset** dropdown, switch from **Modern Bedroom** to **Contemporary Living Room**.
2. Note that the **Category Positive Prompt** automatically updates:
   * Bedroom prompt prioritizes bed, pillows, nightstand, and ambient lighting.
   * Living room prompt prioritizes sofa, coffee table, indoor plants, and natural daylight.
3. Switch back to **Modern Bedroom** (or click the **"Bedroom Sketch"** preset chip to load a crisp architectural template).

### Step 4: Execute Local ControlNet Generation (Primary Model)
1. Verify **"Local ControlNet + SD 1.5 (RECOMMENDED GPU)"** is selected.
2. Click the glowing **"Generate Photorealistic Interior"** button.
3. Highlight the live feedback:
   * The button disables to prevent double submissions.
   * The live timer badge counts up (`Elapsed: X.Xs`).
   * The status explains that diffusion is running in FP16 on the RTX 3050 GPU.
4. In **~14–16 seconds**, the synthesized 512×512 interior appears!
5. Highlight:
   * The bed, pillows, nightstands, and window in the photo exactly match the sketch strokes!
   * Textures: Natural wood flooring, fabric weave on bedding, sunlight streaming through the window.
   * The metric chips show: Latency (`~15.4s`), VRAM Peak (`2.65 GB`), Resolution (`512x512`).

### Step 5: Compare Input & Output
1. In the output panel, click the view tabs:
   * **"Side-by-Side"**: Shows the original sketch next to the generated interior.
   * **"Input Sketch"**: Shows the raw sketch.
   * **"Interior"**: Full generated photo.
2. Click **"Download High-Res Interior"** to save the synthesized PNG image.

### Step 6: Demonstrate Dual-Engine Comparison (Pix2Pix GAN)
1. Select the **"Pix2Pix Exp 3 (Compound Loss)"** model card.
2. Click **"Generate Photorealistic Interior"**.
3. Note that generation finishes in **under 80 milliseconds on CPU**, displaying a 256×256 wireframe-faithful visualization.
4. Explain the academic comparison: Pix2Pix provides instant layout verification, while ControlNet provides publication-grade photorealism.

---

## 3. Important Screenshots for Your Project Report

Capture and include the following screenshots in your documentation and slide deck:

| # | Screenshot Name | What to Capture | Purpose in Report |
|---|---|---|---|
| 1 | `01_studio_overview.png` | Full application view on 1080p display | Shows modern UI design and dual-panel layout |
| 2 | `02_canvas_drawing.png` | Canvas with active freehand sketching, tools toolbar, and size slider | Demonstrates interactive HTML5 canvas features |
| 3 | `03_room_presets.png` | Category selector open with Bedroom, Living Room, Office, Kitchen chips | Illustrates category-aware prompt tuning |
| 4 | `04_generation_progress.png` | Loading overlay with spinning indicator and elapsed timer | Shows responsive UX and non-blocking state |
| 5 | `05_controlnet_result.png` | Rendered 512×512 bedroom interior with metric chips | Proves photorealistic synthesis and VRAM efficiency |
| 6 | `06_side_by_side_view.png` | Split-view showing sketch on the left and rendered photo on the right | Demonstrates structural geometric adherence |
| 7 | `07_pix2pix_comparison.png` | Pix2Pix Exp 3 result (256×256) | Compares GAN baseline vs. Diffusion pipeline |
| 8 | `08_terminal_logs.png` | FastAPI terminal output showing clean 200 OK responses and VRAM stats | Technical evidence of offline execution |

---

## 4. Key Viva Questions & Technical Answers

### Q1: How did you fit Stable Diffusion 1.5 and ControlNet into a 4 GB Laptop GPU?
> **Answer**: Standard FP32 diffusion pipelines require ~8–12 GB VRAM. We implemented a 3-tier memory optimization strategy:
> 1. **FP16 Precision**: Reduced model weight storage by 50% without perceptual quality loss.
> 2. **Model CPU Offloading (`accelerate`)**: The text encoder, UNet, VAE, and ControlNet reside in host system RAM and are staged sequentially onto the GPU only during their respective forward passes. Peak VRAM allocation drops to **~2.65 GB**.
> 3. **Attention Slicing (`diffusers`)**: Computes multi-head attention in sequential chunks, reducing peak activation memory during the UNet denoising loop.

### Q2: What is the difference between Pix2Pix and ControlNet in your system?
> **Answer**: 
> * **Pix2Pix** is a feed-forward conditional GAN trained end-to-end on paired sketch-interior datasets. It is extremely fast (~75ms on CPU) and excellent for real-time structural guidance, but can produce blurry textures on complex furniture.
> * **ControlNet** is a fine-tuned spatial conditioning adapter connected to a pretrained latent diffusion model (SD 1.5). It conditions the diffusion process using zero-convolutions on the scribble input, producing photorealistic materials and lighting, taking ~15 seconds on consumer GPUs.

### Q3: How do you handle concurrency if multiple users click generate?
> **Answer**: `LocalControlNetService` implements a non-blocking thread lock (`threading.Lock`). If an inference is actively running, subsequent requests immediately receive an **HTTP 503 Service Unavailable** with a descriptive message ("Local GPU ControlNet is currently busy synthesizing an image. Please wait a few seconds and try again."). This prevents VRAM or RAM exhaustion.

### Q4: Did you use any external cloud APIs or paid services?
> **Answer**: None. The weights are hosted in the local Hugging Face Hub cache (`Z:\SketchSpace_AI_Models\huggingface\hub`), and execution is enforced in strict offline mode with `HF_HUB_OFFLINE=1` and `TRANSFORMERS_OFFLINE=1`.
