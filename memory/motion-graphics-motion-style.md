---
name: motion-graphics-motion-style
description: "How Rosette (designer) moves motion graphics and what the CD wants: guide the eye — camera-canvas pans, one-at-a-time builds, slow drift"
metadata:
  node_type: memory
  type: feedback
  originSessionId: b37f3e4a-811c-4c51-8845-c08e2650d805
  modified: 2026-11-03T13:55:52.938Z
---

CD's rule: **motion graphics should guide the viewer's eye to what you want them to see.** Rosette's verdict on our travel v1: "hierarchy and sequences are everywhere and tiring to the eyes."

What Rosette's AE work actually does (studied frame by frame in `2026-10_travel-industry/input/reference/Monty eSIM for Travel Industry (1).mp4`):
- The film is one canvas and the **camera moves**: scene changes are whole-frame pans (left through the story) or scrolls (up), both scenes moving together, the next section's text already sitting there. Nothing fades out and re-enters.
- Inside a scene she builds **one thing at a time in reading order, each next to the last**, on its VO word, with short travel (fade + small slide). UI builds row by row inside the phone; cards 01→02→03 left to right.
- Holds never go dead: the whole layout **drifts slowly**.

What failed for us:
- v1 (wallets and travel): many small simultaneous animations (word-by-word, bounces, counters, floats) → no path for the eye.
- v2 (wallets, 2026-11-03): whole groups flying in from off-screen at once + dead holds + fade-out pushes → CD: "even worse than v1".

Outcome on wallets: the CD still preferred **v1** over the v3 camera-pan pass. So Rosette's grammar is a reference, not a proven win. Before re-styling motion, keep a copy of the version the CD liked (v1's source was lost by overwriting it in place).
**How to apply:** version the compositions folder before any motion pass. The v3 kit is available if pans are wanted: in `motion-graphics/monty/projects/eSIM API Integrations - Digital Wallets [71256]/work/hyperframes/monty_wallets/index.html` (`KIT.panIn/panOut/build/drift`, slots overlapping 0.8 s, `.cam` wrapper per scene for drift). Keep −14 LUFS (hers was −20.9, too quiet for web). Related: [[monty-digital-wallets]].
