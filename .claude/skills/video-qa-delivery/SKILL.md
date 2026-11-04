---
name: video-qa-delivery
description: Level-1 quality gate and delivery for every video in this workspace. Use before any render (HyperFrames check + snapshot + look at the frames), when queueing renders, when checking a finished mp4 (specs, loudness, black/frozen frames, contact sheet), for safe zones on 9:16 / 4:5 / covers, contrast fixes, and when naming, filing (output/final vs output/archive) and reporting a deliverable to the CD.
---

# Video QA and delivery

Rule zero: **look at the frames.** A clean `check` proves the composition is valid, not that it looks right. No render is queued and nothing is delivered until you have opened and read the snapshot PNGs / contact sheets of every shot and fixed what they show.

## 1. Pre-render gate (HyperFrames)
Run from the project dir, one project at a time:
```
npx --yes hyperframes@0.8.217 check --json
npx --yes hyperframes@0.8.217 snapshot --at <t1,t2,...> --no-end -o <dir>
```
- `check` must report 0 errors (lint, runtime, layout, motion, contrast, audio). Each remaining warning is either fixed or listed as accepted in NOTES.md with a reason. Usually acceptable: `timeline_track_too_dense` on a generated word-caption track; `container_overflow` on an intended punch-in crop; `line_unread` / `text_below_floor` on phone-UI texture inside mock screens (not meant to be read) and on a reused unchanged outro.
- Under machine load `check`/`snapshot` can time out ("no progress for 120 s"): stop other heavy jobs (whisper, renders), re-run, or raise `--timeout`. Never treat a timeout as a pass.
- Snapshot times: every shot change + ~0.3 s (never the first frame of a clip), every card/text beat, the hook (first 3 s), the last word, the outro. `--no-end`. `--quiet` is not a snapshot flag (it fails silently). Output: `frame-NN-at-Ts.png` + `contact-sheet-N.jpg`. Read the contact sheets, then the single frames where something looks off.
- What snapshots caught that `check` didn't: a hidden scene with an opaque background blanking 6 s of video; an element showing before its cue; an overlay sitting on the captions; a post title half under an app nav bar; a b-roll push so tight the subject was cropped; a hook bar over the speaker's eyes; a scene mounted under a host id that differs from its `data-composition-id` rendering as a black frame. After each fix, re-snapshot the changed region into a new folder (`snaps2/`, `snaps3/`) so before/after stay comparable.
- HyperFrames authoring rules that cause most failures (details in the `hyperframes` skill): one scene per sub-composition file, ids matching; time the `<video>`, leave its wrapper untimed; every `<audio>` has `id` + `data-duration`; never tween `top/left/width/height` (transforms or `clip-path`); never tween opacity/visibility on a `.clip` itself (animate a child).

## 2. Frame checks to make on every snapshot
- **Safe zones, 1080×1920** (organic Reels/TikTok/Shorts): nothing important in the top 168 px (status/top bar) or the right rail (x > 940: like/comment/share icons); captions and key text end above y ≈ 1500 (the bottom ≈ 420 px is username, caption and audio UI). Paid placements are stricter (Meta ads): keep text in the band y 300–1248. Left margin ≥ 60 px.
- **Profile grid is 3:4 (1080×1440) on Instagram since 2025**: the grid shows the centre 1080×1440 of a 9:16 cover (y 240–1680). Covers and the first frame keep face + title inside it; export a `_cover_grid.jpg` crop to show the CD. 4:5 feed (1080×1350) is a crop too: choose the y offset per video so faces and captions survive, and snapshot it.
- **Faces:** nothing covers the speaker's eyes/mouth (bars, chips, labels). Check the hook beats first; framing changes between shoots.
- **Contrast:** text on footage needs ≥ 4.5:1 (small) / 3:1 (large, ≥ 48 px bold). Fixes in order: move the text to a darker area or punch in so dark clothing sits behind it; a scrim gradient behind the caption band (black 0 → 55 %); a solid pill/plate; `text-shadow: 0 2px 12px rgba(0,0,0,.6)`. Don't lighten the brand colour to pass; change the ground.
- **Burned-in source graphics** (show titles, logos, old captions) must be cropped out unless intended.
- **B-roll** literally matches the line it sits under (see stock-sourcing); captions don't collide with text inside cards or b-roll.

## 3. Render (one at a time)
Queue every render through `_shared/tools/render_queue.ps1` as ONE background job; parallel renders starve the machine (~10 min per minute of 1080p here). Dry-run first:
```
powershell -ExecutionPolicy Bypass -File _shared\tools\render_queue.ps1 -WhatIf <projDir> <output\final\NAME_v2.mp4> [<projDir> <out.mp4> ...]
```
Without `-WhatIf` it renders (`render -q delivery`), two-pass loudnorms to −14 LUFS / TP −1.5 / LRA 11 (video copied), deletes the `_raw` file and prints duration + LUFS + true peak. Move the previous version to `output/archive/` before writing a new one into `output/final/`.

## 4. Post-render checks (on the delivered mp4)
```
ffprobe -v error -show_entries stream=codec_name,profile,width,height,r_frame_rate,pix_fmt,sample_rate:format=duration -of compact F.mp4
ffmpeg -hide_banner -nostats -i F.mp4 -af ebur128=peak=true -f null -          # I ≈ -14.0, Peak ≤ -1.5
ffmpeg -hide_banner -nostats -i F.mp4 -vf "blackdetect=d=0.1:pix_th=0.10,freezedetect=n=0.003:d=1.5" -an -f null -   # expect no lines
ffmpeg -hide_banner -loglevel error -y -i F.mp4 -vf "fps=1/2,scale=216:-1,tile=6x3" -frames:v 1 sheet.jpg    # look at it
```
Expect H.264 High, yuv420p, 1080×1920 (or the aspect's size), 30/1, AAC 48 kHz ≈ 192 kb/s, duration = timeline length (±1 frame). An intended hold (e.g. a final frame held under a card) can trip freezedetect; note it. A final mp4 opened in the contact sheet must show the same shots as the snapshots.

## 5. Naming, filing, reporting
- Name: `<CLIENT>_<project>_<deliverable>_<aspect>_v<N>.mp4` (aspect `9x16`, `4x5`, `1x1`, `16x9`); covers `..._cover.png`, `..._cover_grid.jpg`; captions `.srt` with the same stem.
- `output/final/` holds only the current version of each deliverable; every superseded file moves to `output/archive/` (never overwritten, never deleted). Any change the CD will see bumps `v<N>`. No `_raw` files left anywhere.
- Report to the CD in a short list: file path(s), duration, measured LUFS/TP, what changed since the last version, accepted warnings, and open questions (each with the default you chose). Say plainly what was measured vs what needs their ear/eye.
- Record the state (version delivered, open questions) in the job's NOTES.md so the next session can pick it up.

See `references/checklist.md` for the full pre-delivery checklist to paste into NOTES/QA reports.
