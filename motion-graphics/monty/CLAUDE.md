# Monty eSIM (L3 client: motion-graphics explainers)

Applies on top of `motion-graphics/CLAUDE.md` (L2) and the root `CLAUDE.md` (L1).

## Client

- **Monty eSIM**: travel eSIM provider selling a white-label / partner solution to the travel industry (airlines, hotels, agencies). Jobs arrive as numbered briefs, e.g. `[71208]` "Monty eSIM for Travel Industry".
- Delivered: `projects/2026-10_travel-industry/` — 19-scene explainer, VO 78.3 s, v1 render `output/final/Monty_eSIM_Travel_Industry_v1.mp4` (1920×1080, 30 fps, 81 s), built 2026-10-29.
- Delivered: `projects/eSIM API Integrations - Digital Wallets [71256]/` — 42.6 s, 16:9 + 9:16, Nov 2026 (section below).
- Media (`input/`, `output/`, renders) is not in Git: it lives on the shared drive in the same folder layout. See `SETUP.md` at the workspace root.
- Style reference: `projects/2026-10_travel-industry/input/reference/Monty eSIM - White Label Solution Video [71109].mp4` (64 s): no hard cuts, light gradient ground, elements blur/pop in, scenes clear with whip/blur/push, VO-led with a music bed.

## Look (house kit in `work/hyperframes/monty_travel/index.html`)

- Ground: linear gradient 118° #ffffff → #edf4f7 → #d3e8ef → #abdae8.
- Colours: ink #0b0b0b, navy #13294b, teal-dark #05658e, teal #0a7ea8, cyan #00a5cd, cyan-light #6cb5cd, purple #7a58de (eSIM accent, lavender #ece7fc), red #e5203d (problems, on #fde4e9), green #1f9a6b, amber #fbb02b, magenta #e266b4.
- Type: **Montserrat**. Headlines 81 px (xl 116, md 72): light 400 ink words + bold 700 words in a cyan gradient (#6cb5cd → #00a5cd, left to right). Sub/eyebrow 32 px.
- Components: cyan gradient pills (60 px), white chips (42 px), gradient icon tiles (52 px, lavender variant), discs with halo, white cards (radius 26), rows with eSIM variant (lavender gradient, purple border), navy→teal buttons, red badges, phone frame 490×1004 (radius 74, cyan gradient bezel).
- Icons: Font Awesome 6 Free **solid**, as CSS masks coloured by `currentColor` (`assets/icons/`, licence file included).
- Motion helpers `window.MS`: `words` (per-word blur 8→0, 85 ms stagger), `pop` (blur + scale 0.88 + y 40, expo.out 0.75 s), `badge` (back.out), `exit` (`blur` / `whip` / `push`), `grad` (gradient-colour bold lines).
- Sound: VO, music bed (`Proximity.wav`, 112 BPM), Pixabay SFX bundle (whoosh on scene changes at 0.18–0.22, pops on badges at ~0.4, one sparkle on the logo).

## Decisions on the travel-industry job (don't re-ask)

- Scene 4 plays **before** scene 3 so both sit on their VO lines.
- Music extended by repeating 4 bars (54.43–63.0 s) so the final hit lands on "montyesim.com"; the drop at 21.4 s lands on "Three ways to partner".
- Storyboard typos kept as drawn and flagged to the CD: S18 second row also says "Today"; S14 hotel column header says "Your airline".
- Lisbon photo (S15) extracted from `Scene15.ai` with PyMuPDF (`work/monty/extract_imgs.py`, venv `_shared/tools/venvs/pdf`).

## Working on notes

Edit the scene files `compositions/sNN.html`; keep the slot timing table in `index.html` (scenes alternate tracks 1/2 and overlap ~0.45 s). One render at a time; version up to `_v2` and move v1 to `output/archive/`.

## Job: eSIM API Integrations - Digital Wallets [71256] (Nov 2026)

`projects/eSIM API Integrations - Digital Wallets [71256]/`. 42.6 s, 8 scenes, VO `input/vo.mp3` (39.7 s, placed at +0.3 s), music Mixkit 729 "Pop Track 03" (intro bar repeated, then a jump to the last 3 bars so the final hit lands at 40.2 s).

- **Base design = `input/Scene 1.png`–`Scene 6.png`** (studio frames the client already saw: Montserrat, white→light-blue ground, black phone, white cards). The pptx storyboard look (Manrope, dot grid, lime, stamps) was dropped. Scenes 7–8 had no frame and were built in the same language.
- **Client colour note:** frames 1–6 were "monochromatic blue" → add secondary colours (purple, yellow, navy…), never lime. Blue stays the lead; headline accent lines run cyan→purple; tiles/rows in purple, amber, navy; orange only for the problem scene (S2). An amber background glow read as muddy olive over blue: use amber in objects, not glows.
- CD decisions: keep $1,227.10 as drawn; no "01 · MONTY eSIM API" / "THE MONTY eSIM LINE" eyebrows; captions in house style (Montserrat 600 white on a navy pill, low centre, verbatim, clause per caption); **end card shows the official Monty eSIM logo** (`assets/img/montyesim_logo.png`, from montyesim.com) above "Travel data, built into your wallet."
- **The CD's preferred version is v1** (over v2 and the v3 camera-pan pass). Delivered: `output/final/Monty_eSIM_API_Digital_Wallets_16x9_v4.mp4` (= v1 + logo end card) and `..._9x16_v1.mp4`.

Where the sources are (all under `work/`):

| Project | What it is |
|---|---|
| `v1_rebuild/hyperframes/monty_wallets` | **16:9 v1, the approved motion.** Rebuilt from the edit history; matches the v1 render. Its end card still has "Monty eSIM" in type: the delivered v4 patches the render with `v1_logo_endcard.py`; for a new 16:9 version, put the logo in `s08.html` instead (as in the 9:16). |
| `hyperframes/monty_wallets_9x16` | **9:16 v1** (YouTube Shorts): v1 motion re-laid for 1080×1920: headline top-left at y 230; phone in a `.phw` wrapper scaled 82%; S6 cards in a 72% group; S7 as a vertical line of alternating cards; logo end card; captions from `make_caps_9x16.py` at y 1450 (above the Shorts UI); exits start 0.3 s earlier than 16:9 because every headline shares one slot. |
| `hyperframes/monty_wallets` | v3 (camera pans, one-at-a-time builds, drift): **not chosen**, kept for reference. |

Captions: `make_caps.py` (16:9) / `make_caps_9x16.py` regenerate `compositions/caps.html` from `transcript.json`.

## Motion: what the CD has liked and not liked

- The CD's rule: **motion should guide the viewer's eye to what you want them to see.** Designer feedback on the travel v1: "hierarchy and sequences are everywhere and tiring to the eyes."
- Rosette's AE style (travel reference video): the film is one canvas and the camera pans/scrolls between scenes; inside a scene one thing builds at a time in reading order on its VO word; holds drift slowly.
- On wallets: v1 (pops, rises, cards with a little overshoot, counters) was preferred; v2 (groups flying in from off-screen, fade-out pushes, dead holds) was "even worse"; v3 (Rosette's camera grammar) was still not preferred over v1. Treat her grammar as a reference, not a rule.
- **Copy the HyperFrames project folder before any restyling pass** (v1's source was once lost by editing it in place). Level delivered audio to −14 LUFS (the travel reference sat at −20.9, too quiet for web).
