---
name: trrs-reel
description: Build The Retail Razor Show 9:16 reels (Instagram/Shorts) for a new episode from templates/reel. Covers the cut, words.json, crops, cards and b-roll, captions, outro, sound, check/snapshot, and the one-agent-per-reel brief pattern used on S6E15. Use when the CD asks for TRRS reels, clips or shorts.
---

# TRRS reels

The editorial side (picking 4–6 one-idea moments, hooks, posting order around the release) is in the L2 skill
`podcast-repurposing`, and generic reel craft is in `podcast-reel`. This skill is the TRRS build. Read the
`trrs-style` skill and `podcasts/retail-razor/CLAUDE.md` (standing CD decisions) first. The reference build is
S6E15: projects `episodes/S6E15_leslie-ann-hall/work/hyperframes/r1..r6` with notes and EDLs in
`work/reels/rN/NOTES.md` and `EDL.md`. R2 is the approved pilot.

## 0. Episode prep (once per episode, by the coordinator)
1. Put the client files in `episodes/<SxEyy_guest>/input/` (finished episode mp4, show notes, video cover).
2. Transcribe the whole episode with word timings (`_shared/tools/transcribe_fw.py`; pass the wav **path** to
   faster-whisper, not a numpy array) → `work/episode/ep_words.json` on the mp4 timebase. Check the offset against the
   show-notes timestamps (S6E15 notes were about 4 s early). Always find lines by searching the words.
3. Map the burned-in boxes in the source frame (title box, logo box, "Recorded live" box, caption band) and measure
   **one crop per speaker** with the window's 1080:1270 aspect (w x 1.176 = h):
   - S6E15 guest crop: [950, 113, 744, 875]
   - S6E15 host crop: [230, 156, 680, 800], with y ≥ 156 to clear the title box

   Snapshot real frames from each reel's range to check them.
4. Pick the reels (L2 `podcast-repurposing`): one idea each, 28–62 s, verbatim. Propose them to the CD as a short list
   (working title, in/out, why, the visual idea for each beat) and wait for the picks.
5. Pilot one reel (as R2 was), get the CD's notes on it, then fan out the rest.
6. Find out who the guest's company works with (its client roster). Those brands must never appear as negative examples.

## 1. Shared brief → one agent per reel
On S6E15 the coordinator wrote `work/reels/BRIEF.md` once and gave each reel to its own agent with a short prompt.
Do the same:
- **BRIEF.md** (one per episode, in `work/reels/`) contains:
  - client and guest line
  - source path, burned-box map and word-timing file with its offset note
  - path of the approved pilot to copy
  - the style rules (point to `trrs-style` and the CLAUDE.md decisions, plus any episode-specific ones such as the
    guest's client list)
  - the stock rules (Mixkit, check each clip's licence page)
  - the sound recipe and the outro values (`ep_title`, `ep_show`)
  - the audio/cut rules, the deliverables (step 2 below), the process steps 3–7 below, and the gotchas
- **Per-reel prompt:** reel id; the verbatim script with episode in/out times; the speakers; the idea for each beat
  ("on 'X' show Y"); the caption KEY words; the folders the agent owns (`work/hyperframes/rN`, `work/reels/rN` only);
  and "build to check + snapshots, DO NOT RENDER, write NOTES.md".
- Renders run **centrally, one at a time** after review (workspace rule), followed by loudness levelling.
- Several agents running whisper or `check` at once starve the CPU. If `check` or `snapshot` times out
  ("no progress for 120 s"), re-run it on its own.

## 2. Cut (per reel)
Generic cutting, speaker separation, the audio chain and word verification come from the L1 skill `video-edit-core`
(its `cut_aroll`, `pitch_map` and `verify_words` scripts). The TRRS specifics:
- Make a cut list at word boundaries in `work/reels/rN/EDL.md`, with a table of source in/out → reel in/out, dur and
  first…last words.
- Leave a 0.10–0.15 s handle before the first onset. Use hard video cuts and 10–20 ms audio crossfades centred on the
  cut.
- Remove a host backchannel only when it sits in a clean gap. Pitch tells the speakers apart (S6E15: Ricardo about
  95 Hz, Leslie about 220 Hz). Muting 30 dB with 15 ms ramps keeps the length unchanged.
- A word that isn't said clearly gets its sentence or clause cut, and you note it for the CD.
- **Ending:** keep the final word's whole tail, then about **0.5–0.6 s** of air (room tone from the same recording, with the
  picture holding on the speaker and the drift continuing) before the outro. The CD approved R1 v2 (~0.57 s tail); the
  longer 1.2 s hold of v4 was not chosen.
- Deliverables:
  - `assets/video/aroll.mp4`: the full 1920x1080 frame, 30 fps CFR, crf 16, no audio, e.g.
    `ffmpeg -ss <in-1> -i SRC -ss 1 -t D -an -vf fps=30,format=yuv420p -fps_mode cfr -c:v libx264 -preset slow -crf 16`.
    Concat the segments.
  - `assets/audio/voice.wav`: mono 48 kHz, clean chain (highpass 80, deesser, acompressor -24 dB 2.5:1, gain,
    alimiter, fades), -16 LUFS, padded or trimmed to exactly the A-roll sample count.
  - `work/reels/rN/words.json`: `[{"w","s","e","spk"}]`, cut-relative, verbatim. Verify it by re-transcribing the final
    voice.wav; no caption word should sit in silence.

## 3. Project
1. Copy `podcasts/retail-razor/templates/reel` → `episodes/<ep>/work/hyperframes/rN`. Rename `package.json` /
   `meta.json`, delete `tools/words.sample.json`, and copy `assets/LICENSES.md` along with the rest.
2. Captions: `python tools/build_captions.py --words ../../reels/rN/words.json --out compositions/captions.html --end <A-roll end> --key "w1,w2"`.
3. `index.html`:
   - **Shots:** one timed `<video>` of `aroll.mp4` per speaker stretch, each inside its own untimed `.cam` wrapper,
     with `data-media-start` = `data-start`. Use host and guest crops from step 0; framing math is in the template
     comment.
   - **Camera:** never static. Slow drifts (ease `none`) plus punch-ins on key words (scale to about 1.14–1.18,
     0.3 s `expo.out`), and a `power2.inOut` ease back out to reset. The transform origin is the speaker's face.
     A punch-in also hides a jump cut.
   - **B-roll:** full screen, slow push from 1.1, `whoosh` on the cut. Must be literal and real (see CLAUDE.md).
   - **Cards:** one composition file per card. Copy `card.html`, give it a new file name and `data-composition-id`,
     and use the same host id in index. Cues are word times minus the card start.
   - Root duration is A-roll end + 3. header, tags, captions and voice run 0 → A-roll end, then the outro.
   - Sound per `trrs-style`: bed 0.2 from a media start that puts the outro on a bar line, music-out 0.55, shing at
     outro âˆ’ 0.33.
4. `header.html`: set the duration and the `BROLL` hide list (every full-screen b-roll/card window).
   `tags.html`: names and first-appearance times.
   `outro.html`: only `ep_title` and `ep_show`, changing both the variable defaults and the element text.

## 4. B-roll and cards
- Literal and real. Approved on S6E15:
  - real legacy-brand wordmarks from Wikimedia Commons with a sourced founding year
  - real platform logos (Meta, TikTok, Google)
  - a real shopper scrolling a real Amazon PDP (Mixkit 42136)
  - Mixkit creator / ring-light footage for "creators"
- Rejected: a library shelf for "legacy", a typewriter for "decades", a building facade.
- When a real capture is blocked (Reddit blocks `hyperframes capture` and its JSON), build a faithful HTML rebuild of
  the current app UI (dark-mode Reddit was approved) with invented usernames, brands, products and prices.
  "r/SkincareAddiction" was fine because it is a real public subreddit name.
- No invented numbers on cards (R5 had its percentages removed). List/checklist cards finish with the **last item
  ticked** and hold about 2 s (R4 v2).
- Stock: Mixkit only works from scripts. Open every clip page, reject "Restricted License", and log every source in
  `assets/LICENSES.md` (L1 `stock-sourcing`). No AI video generation was available on S6E15.
- ffmpeg can't decode SVG. Use Wikimedia's PNG renders or a headless-Chrome snapshot.

## 5. QA before handing over (per reel)
1. `npx --yes hyperframes@0.8.217 check --json` must show 0 errors. Accepted warnings:
   - `timeline_track_too_dense` (captions)
   - `container_overflow` on the cams (punch-ins)
   - outro `line_unread`
   - small UI text in rebuilt screens (`text_below_floor` / `line_unread`)
   - peach role contrast on name tags
2. `npx --yes hyperframes@0.8.217 snapshot --at <every shot change + 0.2 s> --no-end -o work/reels/rN/snapsK`, then look
   at every frame:
   - faces clear
   - logo hidden on every full-screen shot
   - nothing in the caption band
   - no burned-in box edges in the crops
   - the last list item ticked
   - about 0.5–0.6 s of air before the outro
3. Write `work/reels/rN/NOTES.md`:
   - duration
   - verbatim script
   - EDL summary
   - shot list with times
   - logo-hide windows
   - KEY words
   - SFX times
   - b-roll sources and licences
   - check warnings accepted
   - open questions for the CD, as a short list
4. Central render → level to -14 LUFS / ≤ -1.5 dBTP → `output/final/reels/TRRS_<SxEyy>_R<N>_9x16_v<N>.mp4`. Older
   versions go to `output/archive/`.

## Gotchas (cost a cycle on S6E15)
- A scene mounted under a host id different from its `data-composition-id` renders black.
- A hidden full-screen scene with an opaque background blanks the shots under it (R1). Keep the ground inside the
  timed clip.
- Never tween top/left/width/height, or opacity on a `.clip` itself. Animate a child.
- ffmpeg 9: use `-/filter_complex file` (not `-filter_complex_script`) and `-fps_mode` (not `-vsync`).
- `rm -rf` is denied in this environment. Leave temp files in `work/reels/rN/tmp`.
- faster-whisper given a numpy array assumes 16 kHz, so pass the path.
