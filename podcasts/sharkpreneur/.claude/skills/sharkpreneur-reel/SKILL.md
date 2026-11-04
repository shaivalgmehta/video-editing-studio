---
name: sharkpreneur-reel
description: Build a Sharkpreneur podcast reel (9:16, ~20–35 s) in the exact style of "Sharkpreneur Reel #1" - dark dot-grid ground, full-width Zoom windows, red/white hook words around the window, shadowed Inter captions, scanline B-roll with words behind a cutout, slate, diagram card and the reused shark outro. Use when the CD asks for a Sharkpreneur reel, clip or short; start from the approved SP1 project.
---

# Sharkpreneur reel

Read `podcasts/sharkpreneur/CLAUDE.md` (look table, sourcing, naming). The general process (picks, verbatim scripts, CD approval, cut, captions, renders) is the L2 skill **`podcast-reel`**; editorial rules are **`podcast-repurposing`**; covers are **`podcast-cover`**. Don't repeat them here, follow them, and apply the Sharkpreneur specifics below.

Reference build: `podcasts/sharkpreneur/episodes/reel-02_low-stress-options/` (SP1 = HyperFrames project, `work/reel_lso/` = cut). Style reference: `podcasts/sharkpreneur/reference/Sharkpreneur Reel #1.mp4`.

## 1. Source and pick

- Episode folder `podcasts/sharkpreneur/episodes/E<episode>_<guest-slug>/` with `input/ work/ output/`. Get the episode with `yt-dlp` (full stream; it's 640×360–480p on YouTube) unless the client sends the original.
- Whole-episode word timings once (`podcast-reel`), then pick per `podcast-repurposing`. Shape that worked: **host's question as the hook (~2–3 s) → guest's answer (~15–17 s) ending on a list or framework → outro (4.7 s)**. Total ~20–25 s of speech.

## 2. Cut

- Pull segment in/outs from the word timings, then snap each edge to the quietest 10 ms frame nearby on the source audio (SP1's `work/reel_lso/cut.py`: RMS envelope, search −0.05/+0.03 s at the start, −0.03/+0.10 s at the end). Write `segs.json`, cut host and guest as separate clips (`assets/video/seth.mp4` = host, `<guest>.mp4`), plus the levelled dialogue `assets/audio/voice.wav`.
- Hard punch-in (×1.14, origin 50% 35%) on one emphasis line, back out on the next.

## 3. Build (copy SP1)

1. Copy `.../reel-02_low-stress-options/work/hyperframes/SP1/` to the new episode's `work/hyperframes/R<n>/`, leaving out `.hyperframes/`, `.transcode-cache/`, `renders/`, `snaps*/`, `*.jpg` check images and the per-reel media (`assets/video/seth.mp4`, `troy.mp4`, `assets/broll/*`, `assets/audio/voice.wav`, `bed.wav`). Keep `assets/video/outro.mp4`, `assets/fonts/Inter.ttf`, `assets/sfx/`, `assets/audio/music.mp3` (Mixkit 139).
2. Re-time `index.html`: host window (`#sethwin`, y472 h976) for the question, guest window (`#troywin`, y325 h1270) for the answer, outro at the end of speech with `data-has-audio="true"`.
3. Scenes (rewrite the words, keep the styling): `hook.html` (host question: red words above the window, white below, word-synced), `captions.html` (1–3 words, y≈1512, shadow, no pill), `bigwords.html` (huge red/white keyword behind the subject during a cutaway), `slate.html` (black, red header ending "...", white words as spoken), `diagram.html` (red title, white pills with red arrows, last pill green). Use only the guest's words on cards; no invented figures.
4. Cutaways: literal Mixkit B-roll for the line (see CLAUDE.md sourcing), 1–2 s each, slow push 1.00→1.06. For each, make a subject cutout with `remove-background` (`media-use` skill) as `<clip>_fg.webm` on the layer above the big words; give both the same `data-color-grading` (copy SP1's).
5. Sound: voice on its own track, bed ~18 dB under it (`bed.wav` trimmed to speech + 0.7 s), a short whoosh (0.3–0.35) into the slate and the diagram, nothing else. The outro carries its own audio.
6. Layering: grid 0 / windows 1 / B-roll plate 2 / big words 3 / cutout 4 / hook, slate, diagram 5 / captions 6 / outro 9. Scene ids = host ids.
7. `npx --yes hyperframes@0.8.217 check` at 0 errors; snapshot the hook, every cutaway, slate, diagram and the outro join; compare side by side with frames from the reference reel.

## 4. Deliver

- Render, level (master −14 LUFS, true peak ≤ −1.5 dB, per the root rule), write `NOTES.md` with open questions, update `assets/LICENSES.md` (episode, outro source, each Mixkit id, music, font).
- Output to `output/final/` as `SHARK_E<episode>_R<n>_9x16_v<N>.mp4`; cover via `podcast-cover` if asked.
