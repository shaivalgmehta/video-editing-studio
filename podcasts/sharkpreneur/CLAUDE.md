# Sharkpreneur (L3 client: podcast reels)

Applies on top of `podcasts/CLAUDE.md` (L2) and the root `CLAUDE.md` (L1). Procedure for a reel: skill `sharkpreneur-reel` (`.claude/skills/sharkpreneur-reel/`), which builds on the L2 skills `podcast-repurposing`, `podcast-reel` and `podcast-cover`.

## Client

- **Sharkpreneur** podcast, host **Seth Greene**. Episodes are Zoom interviews (host + guest webcams); a separate client from Delesign.
- Started 2026-10-27. The CD asked for reels that **copy the style of the reference reel exactly**: `reference/Sharkpreneur Reel #1.mp4` (1080×1920, 30 fps, 32.1 s).
- Delivered so far: one reel from Episode 1331 with Troy Broussard ("The Low-Stress Revenue Stream for Business Owners"), "Low Stress Options", 24.3 s: `episodes/reel-02_low-stress-options/output/final/Sharkpreneur_Reel_2_Low_Stress_Options.mp4`. HyperFrames project `.../work/hyperframes/SP1`, cut in `.../work/reel_lso/`.

## Look (measured from the reference; SP1 is the approved build)

| Element | Spec |
|---|---|
| Ground | #07080b with a #2f2e32 dot grid, 54 px pitch (dots ~4 px) |
| Speaker windows | full-width (1080) webcam windows: host at y=472, 976 px tall; guest at y=325, 1270 px tall. One speaker on screen at a time |
| Hook | the host's question. Red #c30a0a words build above the window, white words below it, synced to speech (Inter 600, ~124–150 px, −0.07 em) |
| Captions | Inter 600, ~74 px, −0.06 em tracking, white with drop shadow, no pill, centred at y≈1512, 1–3 words per group |
| Cutaways | full-bleed B-roll with scanlines, channel split and vignette (HyperFrames media treatment: scanlines 0.45, chromatic aberration 0.12, vignette 0.3, contrast +0.12, saturation −0.12). Huge red/white words (175–215 px) sit **behind** the subject via a `remove-background` cutout layered above them |
| Slate | black, red header ending in "...", white words appearing as spoken |
| Diagram card | red title, white pills joined by red arrows, last pill green #429b46 |
| Outro | the reference reel's outro (27.43 s to end, shark + logo, with its own sound) reused as is: SP1 `assets/video/outro.mp4`, 4.7 s |
| Sound | music bed ~18 dB under the voice, master −14 LUFS per the root rule (CD confirmed 2026-11-02; the reference reel measured ~−16), whooshes sparse (one into each slate/diagram) |
| Font | Inter (OFL), `SP1/assets/fonts/Inter.ttf` |

## Standing notes

- Episode source: the YouTube upload is 480p at best; download the full stream with `yt-dlp` (section downloads re-encode at a low bitrate). Ask the client for the original recording if quality matters.
- B-roll that worked: Mixkit (free licence, commercial, no credit). Tag pages list `free-stock-video/<slug>-<id>/`; files at `assets.mixkit.co/videos/<id>/<id>-720.mp4`. Pexels/Unsplash block scripts; Openverse times out. Log every clip in the project's `assets/LICENSES.md`.
- Music used: Mixkit 139 (`_shared/music/mixkit/mixkit_139.mp3`).
- Naming: the first reel was delivered as `Sharkpreneur_Reel_2_Low_Stress_Options.mp4` (before the naming rule). For new reels use `SHARK_E<episode>_R<n>_9x16_v<N>.mp4` (CD-approved 2026-11-02) and episode folders `episodes/E<episode>_<guest-slug>/`.
- No L3 template folder yet: copy SP1 (see the skill).
