---
name: delesign-ad
description: Turn a raw talking-head clip of Shaival into a finished Delesign Meta ad (9:16 + 4:5 + SRT + thumb) in the house style built on ads 2A–2D. Use when the creative director drops new Delesign footage in a project's input/ and asks for an ad, a cut, captions or graphics. Covers the full pipeline (clean audio, transcribe, cut, HyperFrames graphics, mix, export, QA), the style kit, and the director's standing decisions.
---

# Delesign ad pipeline (house style from ads 2A–2D)

Read `ads/delesign/CLAUDE.md` first (brand, CD decisions). General steps live in the L2 skill `ad-edit` and the L1 skills `video-edit-core`, `video-qa-delivery`, `stock-sourcing`; this skill is the Delesign-specific recipe.

You are the editor; the user is the CD. Work stage by stage and stop at the checkpoints below unless told "no stops", "make it quick" or "complete the next steps". Reuse, don't rebuild.

## Paths

Run every command **from the job folder** (e.g. `ads/delesign/projects/2026-10_meta-campaign/`); the scripts take `--project <dir>` and default to the current folder. `<ws>` = workspace root.

| What | Where |
|---|---|
| Pipeline scripts | `ads/delesign/tools/` (= `../../tools/` from a job folder) |
| Shared tools | `<ws>/_shared/tools/` (`run_dfn.py`, `align_words.py`, `transcribe_fw.py`, `audio_metrics.py`); DeepFilterNet venv `<ws>/_shared/tools/venvs/dfn/Scripts/python.exe` |
| HyperFrames template | `ads/delesign/templates/ad/` (clean copy of 2B; see its README). Copy to `work/hyperframes/<ad>/`, never edit in place |
| Reference builds | `ads/delesign/projects/2026-10_meta-campaign/work/hyperframes/2A`–`2D` (read-only reference) |
| Brief | `ads/delesign/projects/2026-10_meta-campaign/input/EDIT_BRIEF_2A.md`; new ads inherit it unless a new brief says otherwise. Its folder table (`/raw`, `/out`…) is the old layout |
| Camera files | `<job>/input/` (read-only) |
| Intermediates | `<job>/work/` — `audio_raw/ audio_clean/ transcripts/ edl/ cut/ hyperframes/<ad>/ mix/ render/ reports/` |
| Deliverables | `<job>/output/final/` (older versions to `output/archive/`) |

## Inputs to ask for (once)

| Need | Folder | Notes |
|---|---|---|
| Raw camera file(s) | `<job>/input/` | Phone, 4K portrait (rotation flag), VFR; always conform to 30fps |
| Script (reference only) | the brief | Captions follow what is actually said, never the script |
| Go screens / recordings | `ads/delesign/brand/go/` | Ask for 2x captures; 1x captures need 2x upscale (`PIL LANCZOS + UnsharpMask`). The 2B set is in the template's `assets/go/` |
| Portfolio pieces | `ads/delesign/brand/go/` or `ads/delesign/brand/broll/portfolio/` | Real deliverables only; placeholders flagged |
| Logo | `ads/delesign/brand/brand/` | Web SVG `ads/delesign/brand/brand/logo_web/delesign_logo-electric-blue.svg` is the fallback |
| B-roll | `ads/delesign/brand/broll/` | Golden Gate, cockpit and phone sets already sourced, each with `LICENSES.md` |
| Fonts | `ads/delesign/brand/brand/fonts/` | Hanken Grotesk (variable) + Architects Daughter |
| Music | `<ws>/_shared/music/mixkit/` | Mixkit (free, commercial, no credit): 749 is the house bed, 139 the alternate |

## Fast path (built after ad 2B)

From the job folder, with `T=../../tools` and `S=<ws>/_shared/tools`:

1. `python $T/new_ad.py <ad> input/<file>.mp4` → probe, DFN + studio chain clean audio, Parakeet + faster-whisper transcripts, silence map and a draft runs table in `work/edl/<ad>_ingest.md`. Look at a 0.25s frame strip of the first 6s to pick the walk-in pre-roll.
2. Write `work/edl/<ad>_cut.json` (`name`, `video: "input/<file>.mp4"`, `audio: "work/audio_clean/<ad>_CLEAN_A3.wav"`, `preroll_in`, `runs`: label, onset, offset, gap or null, note) from that table, then `python $T/build_cut.py work/edl/<ad>_cut.json --dry`, review, run without `--dry`. Cut boundaries come from a `silencedetect=n=-50dB:d=0.12` map, not from word timestamps. Transcribe the cut WAV (`work/cut/<name>.wav`) with Parakeet and fix tokens (brand name, hyphens, dropped words) into `work/transcripts/<ad>_cut_v1_words_fixed.json`.
3. Copy `ads/delesign/templates/ad/` to `work/hyperframes/<ad>/` (or a reference build whose scenes fit better), encode the A-roll to `assets/aroll.mp4` (`-g 15`), then `python $S/align_words.py <fixed.json> work/cut/<name>.wav <aligned.json>` (Parakeet word starts run 0.15–0.45 s early; this snaps groups onto measured speech), then `python $T/build_captions.py <aligned.json> work/hyperframes/<ad> <aroll_seconds>`. Rewrite `index.html` times and the scene copy/timings; `npx --yes hyperframes@0.8.217 check --json` at 0 errors; `npx --yes hyperframes@0.8.217 snapshot --at <beats> --no-end -o ../../render/snap<ad>` and look at the contact sheets.
4. Render to `work/render/<ad>.mp4`, then `python $T/finish.py work/render/<ad>.mp4 --name <ad> --thumb-at <t>` (music defaults to Mixkit 749; HyperFrames project defaults to `work/hyperframes/<ad>`; add `--version N` for `_vN` names) as **one background job**. Write `work/reports/QA_REPORT_<ad>.md`.

Scene kit (template + reference builds): hook bar (`hook`), numbered card stack (`stack`, 2A `options`), checklist card (`questions`), chips/asks (`asks`, 2A `chips1/2`), Go screens with note + full-bleed request list (`go2b`, 2A `goscreens`), portfolio flashes (2A `portfolio`), proof chips + guarantee (2C `proof`, `guarantee`), memory/context (2D `memory`, `context`), end card (`endcard`).

## Pipeline (in full)

1. **Ingest.** `ffprobe` every file in `input/`; 540p proxy to `work/proxies/`; 48k 24-bit mono WAV to `work/audio_raw/`.
2. **Clean audio**, house "studio" chain (approved on 2B v2, keeps every word; `new_ad.py` runs it): `run_dfn.py <in> <out> --pf` (DeepFilterNet with post-filter, run with the dfn venv python), then `agate=threshold=0.01:ratio=2.5:attack=10:release=220:knee=6,highpass=f=90,equalizer=f=280:t=q:w=1.2:g=-4,equalizer=f=3500:t=q:w=1:g=3,highshelf=f=9000:g=2,deesser=i=0.55:m=0.5:f=0.5,acompressor=threshold=-20dB:ratio=4:attack=8:release=120:makeup=2.5`. Gentler 2A chain, if the CD asks for softer: `agate=threshold=0.006:ratio=2:attack=15:release=300:knee=8,highpass=f=80,equalizer=f=300:t=q:w=1:g=-2,equalizer=f=4000:t=q:w=1:g=2,deesser=i=0.5:m=0.5:f=0.5,acompressor=threshold=-18dB:ratio=3:attack=10:release=150:makeup=2` (edit `POLISH` in `new_ad.py`). **Never resemble-enhance / generative enhancement**: it rewrote words (Checkpoint 1 of 2A). Verify with a transcript: every word must survive.
3. **Transcribe** with `npx --yes hyperframes@0.8.217 transcribe <wav> --engine parakeet --json` (writes `transcript.json` beside the input; copy to `work/transcripts/`). `transcribe_fw.py` (faster-whisper) is the cross-check. Speech onsets from `silencedetect=n=-40dB:d=0.2`.
4. **Cut** with `build_cut.py` + a cut config (`build_rough_cut.py` / `build_cut_2B.py` are the legacy hard-coded 2A/2B cuts, kept for reference). Pacing: gaps 0.15–0.25s (60% after the word / 40% before the next), one deliberate 0.45s beat at the turn, ≤0.15s before each list item, ~0.3s + punch-in before the reveal, 10ms audio crossfades, punch-ins alternate 100%/115% anchored to the top of frame. Check cut frames for blinks and nudge in-points (`split X after / Y before` in the note). Verify with a transcript of the cut WAV (no clipped words) and `silencedetect` (nothing >0.4s but the beat). **Checkpoint: 540p proxy + EDL.**
5. **Graphics** in HyperFrames (copy the template, new `assets/aroll.mp4` with `-g 15`, captions via `build_captions.py`, re-time `index.html` and scenes to the new words). Gotchas: scene file id = host id = timeline key (a mismatch renders the scene as an opaque black capture); ffmpeg 9 wants `-/filter_complex file`; time the `<video>` and leave its wrapper untimed; never tween `top/height` (use transforms or `clipPath`); every `<audio>` gets `data-duration`; check the hook bar against the face before rendering (on 2C/2D he sat close and the bar moved from y=300 to y=880). Gate: check at 0 errors, snapshot every beat and look. **Checkpoint: full-res review render.**
6. **Finish** with `finish.py`: ducked bed, end-card swell, two-pass loudnorm to −14 LUFS / −1.5 dBTP (the root rule), `output/final/<name>_9x16.mp4` (H.264 High, 30fps, 14 Mbps), `<name>_4x5.mp4` (crop y=120, 1080×1350), `<name>.srt`, `<name>_thumb.jpg`, QA numbers printed; confirm the printed TP is ≤ −1.5. Move superseded versions to `output/archive/`.
7. **QA report** `work/reports/QA_REPORT_<ad>.md`: the brief's checklist, measured numbers, every deviation with its reason (always log the CD's standing overrides from `ads/delesign/CLAUDE.md`), and what to test next. Say plainly what was measured vs. what you couldn't hear/see.

## Style kit (approved on 2A, refined on 2B–2D)

- **Canvas** 1080×1920, 30fps. Text safe band 300–1248px (top 14% and bottom 35% are app UI). 4:5 is a centre crop at y=120, so keep key text inside 120–1470 too.
- **Fonts:** Hanken Grotesk for everything (Bold 700/800); Architects Daughter only for short hand-written notes.
- **Colors:** Sunset Orange #FF5532 (highlights, CTA, active caption word), Charcoal #1E293B (text, caption pill at 85%), Deep Green #33473B (support), French Lavender #C7B0FF (soft accents), White / Off-white #F8FAFC (panels), Electric Blue #334EAC **logo only**.
- **Captions:** 2–4 words, ≤2 lines, 54–66px Bold, white on charcoal pill, active word orange, pill bottom at 1248 (65%). Hard cut between groups. Brand normalized to "Delesign" (`build_captions.py` fixes the ASR variants). US spelling.
- **Hook:** hook bar on from frame 1 (white pill, orange first words, 68px) at y=300 (or below the chin if it covers the face); open on real motion (Shaival walking in and sitting down), not on the first word.
- **Structure:** hook bar → B-roll under the metaphor (two cuts, slow push) → face line → **middle in picture-in-picture**: Shaival in a rounded 260×462 window at **(755, 680), bottom-right**, z above graphics and below captions; ground = light dot pattern (#D7DEE8 1.6px dots on #F8FAFC, 30px grid); graphics full-width (950px at x=65), left-aligned: card stack 950×230 from y=260 with 50px heads, checklist 950 wide with 44px rows (text max-width 600), chips/asks 54–64px stacked left, Go screens 950 wide with one Architects Daughter note each (notes left), request list full-bleed → B-roll callback → face for the close → **end card** (white, logo Electric Blue 420px, headline 84px, orange pill button 48px, sub-line 34px; ≥3s, dead still for the last second).
- **Motion:** ease-out 180–250ms entrances (`power3.out`), no bounce, exits 40–50% shorter, list items 40–80ms apart. One soft click (`assets/sfx/click-soft.mp3`, 0.4–0.55) per card entrance, nothing else.
- **Labels:** any Go screen gets "Illustrative workflow" 14px grey (#6C7786) bottom-right (bottom-left when the PiP covers bottom-right); counters get "illustrative". No turnaround / SLA / "unlimited" / results claims ever.
- **Music:** Mixkit 749 entered 8s in, −26 dB, sidechain-ducked 5:1 under the voice, +6 dB on the end card, 1.4s fade.

## Checkpoints and what to send

1. After audio: 20s samples (raw / clean / polished), take table from the clean transcript, pickups, honest ceiling note.
2. After the cut: 540p proxy + EDL (`work/edl/`), with the judgment calls listed.
3. After graphics: full-res render + 540p proxy + frame sheet + beat map, decisions needed, deviations logged.
4. After finish: `output/final/` files + `work/reports/QA_REPORT_<ad>.md`.
