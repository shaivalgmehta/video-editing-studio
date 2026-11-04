# Delesign ad template (HyperFrames)

Clean copy of ad 2B "Co-pilot" (Oct 2026), the build that set the house layout: walk-in open with the hook bar, B-roll under the metaphor, Shaival in a bottom-right picture-in-picture over a dot-pattern ground for the middle, B-roll callback, face for the close, end card. Checked with `npx --yes hyperframes@0.8.217 check` (0 errors, 1 known warning on `go2b`'s nested video start).

**Never edit in place.** Copy the folder to `<job>/work/hyperframes/<ad>/` and work there. Full procedure: skill `delesign-ad`.

## What is a placeholder (replace per ad)

| File | Placeholder | Replace with |
|---|---|---|
| `assets/aroll.mp4` | 45.167 s charcoal frame, silent | the ad's cut (`work/cut/<name>.mov`), re-encoded with `-g 15` |
| `assets/broll/broll_a.mp4`, `broll_b.mp4` | solid colour clips | licensed B-roll that shows the line (sets in `ads/delesign/brand/broll/`) |
| `compositions/captions.html`, `assets/captions_groups.json` | dummy captions | `python ads/delesign/tools/build_captions.py <aligned.json> <this folder> <aroll_seconds>` |
| Scene copy in `hook`, `stack`, `questions`, `go2b`, `asks`, `endcard` | 2B's words and timings | the new script's lines, timed to the aligned words |
| `index.html` | 2B timings (clip starts, PiP in at 11.1 s / out at 37.87 s, SFX clicks, end card at 45.167 s) | new beat map; keep `data-duration` of root = A-roll + 3 s end card |

## What is reusable as is

- `assets/fonts/` (Hanken Grotesk, Architects Daughter), `assets/brand/logo.svg` (Electric Blue), `assets/sfx/click-soft.mp3`.
- `assets/go/` — the 2B Go screens (team panel, request list scroll, brand list, branding examples), reused by default on 2C/2D.
- Scene files: `hook` (hook bar), `stack` (numbered card stack), `questions` (checklist card), `go2b` (Go screens + full-bleed request list), `asks` (chips), `endcard`. More scenes in the reference builds `ads/delesign/projects/2026-10_meta-campaign/work/hyperframes/2A`–`2D`.

## Notes

- `compositions/components/` (`hw-callout-circle`, `hw-arrow`, `caption-pill-karaoke`) came from the registry and are **not used**; hand-drawn circles are banned by the CD. Captions come from `build_captions.py`, not the karaoke component.
- Scene file id = host id = timeline key, or the scene renders black.
- `.hyperframes/` is a cache made by `check`; don't copy it into a new ad.
