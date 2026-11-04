# Motion graphics (L2: VO-led explainers built from a storyboard)

Applies to every client under `motion-graphics/`, on top of the root `CLAUDE.md`. Mechanics (HyperFrames, audio, QA, naming) are in the L1 skills `video-edit-core`, `video-qa-delivery`, `stock-sourcing`; client looks live in `motion-graphics/<client>/CLAUDE.md`.

## Typical job

The client supplies a **storyboard** (one PNG per scene, often with the source `.ai`/AE files), a finished **VO**, a **music** track and a **style reference** video. We rebuild every scene as live HTML in HyperFrames (not as flattened images) and animate it to the VO. Output is usually 1920×1080, 30 fps, 60–90 s.

## How to build

1. **Inventory**: list scenes, VO length, music length/BPM, reference duration and transition style. Transcribe the VO with word times (`work/<slug>/vo_words.json`) and map each scene to the VO line it illustrates; flag any scene whose order or text doesn't match the VO.
2. **Kit first**: sample colours, type sizes, radii, gradients from the storyboard frames into CSS variables and shared classes in `index.html`; put shared motion helpers in one `window.<KIT>` object (word blur-in, pop, badge, exit variants) so every scene moves the same way.
3. **One scene per file** `compositions/sNN.html`, mounted in `index.html` with a **slot timing table** (start/duration per scene, alternating tracks so neighbours overlap ~0.4–0.5 s for the transition). Scene id = host id = timeline key.
4. **Assets**: rebuild icons from a licensed set (e.g. Font Awesome Free via CSS masks) rather than screenshots; extract embedded photos from the `.ai` files (PDF-compatible, PyMuPDF in `_shared/tools/venvs/pdf`) instead of re-sourcing. Fonts from Google Fonts. Log licences.
5. **Motion**: match the reference — if it has no hard cuts, every scene clears with a whip/blur/push and the next builds in; elements blur/pop in on long ease-out tails; one idea on screen per VO line.
6. **Sound**: VO on top, music bed under it, sparse SFX (whoosh on scene changes, pops on badges). Fit the music to the picture by repeating whole bars (measure BPM) so the final hit lands on the end frame / logo; land drops on section starts.
7. **Review**: `check` at 0 errors, snapshot each scene at its build-complete moment and at every seam; compare against the storyboard frame side by side.

## Rules

- Storyboard text is the client's copy: build it **as drawn**; flag apparent typos/inconsistencies to the CD instead of fixing them silently.
- Illustrative UI and charts carry no invented numbers beyond what the storyboard shows.
- Reordering scenes to sit on the VO is allowed when the VO demands it; report it as a decision.
- Deliverable `<CLIENT>_<project>_<aspect>_v<N>.mp4` in `output/final/`; the HyperFrames project in `work/hyperframes/<slug>/`.
- A 9:16 cut of a 16:9 film: copy the project, re-lay each scene (headline top, hero object centre, captions above the Shorts/Reels UI at ~y 1450), wrap long lines, and start exits earlier when every scene's headline shares the same slot, or outgoing and incoming copy overlap.

## Gotchas (cost us a cycle before)

- A scene mounted under a host id that differs from its `data-composition-id` / timeline key renders as an opaque black frame. Ids must match.
- Don't put a CSS `transform` on an element GSAP animates: to scale a phone or a card group, wrap it in an untimed, never-animated wrapper and scale the wrapper.
- Never tween `top`/`left`/`width`/`height`; use transforms. Every `<audio>` needs an `id` and `data-duration`.
- `hyperframes snapshot --at <t,...> --no-end -o <dir>` writes contact sheets; snapshot every seam (the moments scenes overlap), not just the holds.
- ffmpeg 9: use `-/filter_complex <file>` (not `-filter_complex_script`) and `-fps_mode passthrough` (not `-vsync`).
- On Windows, never rewrite UTF-8 files with PowerShell 5.1 `Get-Content`/`Set-Content` (it double-encodes characters like €, ’, ·). Edit with Claude's Edit tool or Python `encoding="utf8"`.
- A full render takes ~4–10 min; render one video at a time.
