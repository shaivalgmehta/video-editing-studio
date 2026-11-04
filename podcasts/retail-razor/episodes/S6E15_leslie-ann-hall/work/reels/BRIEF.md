# Retail Razor S6E15 reels — shared build brief

Client: The Retail Razor Show (retail / retail-tech podcast). Guest Leslie Ann Hall (Founder & CEO, Iced Media); host Ricardo Belmar. Episode release Tue Nov 3 2026.
Source: `podcasts/retail-razor/episodes/S6E15_leslie-ann-hall/input/S6E15 Leslie Ann Hall.mp4` (1920x1080 finished episode; burned-in title box top-left down to y≈155, logo box top-right x>1700 y<185, "Recorded live at Shoptalk" box bottom-left, burned captions y≈990–1080). Ricardo sits left, Leslie right.
Whole-episode word timings: `podcasts/retail-razor/episodes/S6E15_leslie-ann-hall/work/episode/ep_words.json` — same timebase as the mp4 (verified). Show-notes transcript timestamps run ~4 s EARLY vs the mp4 (e.g. show-notes 07:40 = mp4 464.4 s); always locate lines by searching the words.
Approved pilot to copy: **`podcasts/retail-razor/episodes/S6E15_leslie-ann-hall/work/hyperframes/r2`** (reel R2). Read its `index.html`, `compositions/*.html`, `podcasts/retail-razor/episodes/S6E15_leslie-ann-hall/work/reels/r2/build_captions.py`, `podcasts/retail-razor/episodes/S6E15_leslie-ann-hall/work/reels/r2/EDL.md` first. Renders of it: `out/TRRS_S6E15_R2_9x16_v3.mp4`.

## Style (approved by the creative director — do not deviate)
- 1080x1920, 30 fps. Warm brand ground: `radial-gradient(ellipse 90% 60% at 30% 22%, #4a2a1d 0%, #2a1610 45%, #120a07 100%)`. Montserrat 900 cream #fbeee6, red #e3262b (#ff4a55 highlight), peach labels #f2b48c, Caveat for name tags. Fonts in `assets/fonts/`.
- NO headline/title text. Only the Retail Razor logo (`assets/img/rr_logo.png`, height 112) top-left at left 60 / top 132 (`compositions/header.html`), and it is HIDDEN whenever full-screen b-roll or a full-screen card is on (update its BROLL list).
- Speaker window FULL WIDTH: `#win` left 0, top 325, 1080x1270, thin red top/bottom line. Leslie base crop = source [x950,y113,w744,h875] (video at left -1379, top -164, 2787x1568; punch-in origin "552px 417px"). Ricardo needs his own 744x875-aspect crop (keep y ≥ 156 to avoid the title box; check frames). Cut between speakers with hard cuts (switch which crop/video is shown); GSAP punch-ins (scale 1.0→~1.18, expo.out) on key words, slow drifts otherwise — never a static shot.
- Name tag (Caveat 84px name + 28px peach uppercase role) lower-left of the window (left 60, top 1146) the first time each speaker appears, ~3 s. Ricardo = "Ricardo Belmar / HOST, THE RETAIL RAZOR SHOW"; Leslie = "Leslie Ann Hall / FOUNDER & CEO, ICED MEDIA".
- Captions: uppercase Montserrat 900 76px, word-synced, ≤16 chars & ≤3 words per line, top 1290, active word peach, key words red (`build_captions.py`, edit KEY set per reel). Verbatim to the audio.
- B-roll and explainer cards play FULL SCREEN (1080x1920, object-fit cover). Nothing may cover her face (no chips/labels over the speaker).
- B-roll must literally show what the line says. The CD rejected a library shelf for "legacy brands" and an abstract typewriter for "signals for decades" — generic mood footage is not acceptable. Prefer REAL things: real UIs (Reddit, TikTok, Amazon PDP, search/AI answer screens) recreated faithfully as HyperFrames HTML or captured, real brand logos/products, real data shown as cards. Real brand logos/imagery are fine as illustration, BUT never show Iced Media's clients (L'Oréal and its brands e.g. Maybelline/Garnier/Lancôme/Kiehl's, Walmart, LVMH and its brands e.g. Sephora/Dior/Fenty, Moroccanoil) as negative examples.
- Stock footage: Mixkit only works reliably (tag pages list `free-stock-video/<slug>-<id>/`; files `https://assets.mixkit.co/videos/<id>/<id>-1080.mp4`, newer clips via the page's download route). CHECK EACH CLIP PAGE: some are "Restricted License" (personal only) — reject those. Pexels/Unsplash block scripts. Log every source in the project's `assets/LICENSES.md`. No AI video generation is available.
- Explainer cards: brand style like `compositions/rank.html` (dark scrim, peach tracked labels, cream/red rows, motion that explains the argument, timed to the words).
- Outro: reuse `compositions/outro.html` unchanged (3 s, host id `outro`, z-index 20), at the end. Shing sfx `assets/sfx/shing.wav` at outro_start − 0.33 s. Outro title stays "AI Search Is a Mirror for Your Brand".
- Sound: voice.wav (−16 LUFS, cleaned like R2: highpass 80, gentle de-ess, light comp, limiter), music `assets/audio/music.wav` ("Close Up", groove at media 18.3 s, bar 2.286 s) at volume 0.2 under voice and a second clip at 0.55 for the outro; whoosh on b-roll cuts, click on card beats (`assets/sfx/`), sparse.

## Audio/cut rules
- Quotes verbatim. Cut only at word boundaries / pauses; 10–20 ms crossfades on internal audio cuts; hard video cuts. Remove Ricardo backchannels only where they sit in a gap. A word that isn't said clearly → cut its sentence rather than patch. Never re-synthesise voice.
- Deliver `assets/video/aroll.mp4` (full 1920x1080 frame, 30 fps CFR, crf 16, no audio) + `assets/audio/voice.wav` (48 kHz, exact same duration) + `work/trrs_rN/words.json` ([{"w","s","e","spk"}], cut-relative, verified against the final audio) + `work/trrs_rN/EDL.md`.

## Process
1. Copy `podcasts/retail-razor/episodes/S6E15_leslie-ann-hall/work/hyperframes/r2` → `work/hyperframes/trrs_rN` WITHOUT `.hyperframes/`, `renders/`, `assets/video/`, `assets/broll/`, `assets/audio/voice.wav`. Update `package.json`/`meta.json` names. Copy `podcasts/retail-razor/episodes/S6E15_leslie-ann-hall/work/reels/r2/build_captions.py` → `work/trrs_rN/` and repoint paths.
2. Cut A-roll, words, EDL. 3. Source/build b-roll and cards. 4. Write index.html timeline. 5. `npx --yes hyperframes@0.8.217 check --json` from the project dir — fix every error. 6. `npx --yes hyperframes@0.8.217 snapshot --at <t,...> --no-end -o <dir>` covering every shot change, and LOOK at the frames; iterate until clean.
7. DO NOT RENDER (renders are queued centrally). Write `work/trrs_rN/NOTES.md`: final duration, EDL, shot list with times, b-roll sources + licences, open questions for the CD.
Only touch your own `trrs_rN` folders.

## Gotchas
- A scene mounted under a host id different from its `data-composition-id` renders black. One scene per sub-composition file.
- Never tween top/left/width/height (use transforms/clip-path). Every timed element: class="clip", data-start, data-duration. Every <audio> needs id + data-duration. Never tween opacity/visibility on a `.clip` itself — animate a child.
- ffmpeg 9: `-filter_complex_script` gone (use `-/filter_complex file`), `-vsync` gone (use `-fps_mode`). ffmpeg can't decode SVG (render SVG logos to PNG another way, e.g. headless Chrome via a tiny HTML page + `npx hyperframes snapshot`, or python cairosvg if installed).
- `rm -rf` and some `Remove-Item` chains get denied; leave temp files in `work/trrs_rN/tmp`.
- Snapshot times must avoid the first frame of a clip for fair judgement; use `--no-end`.
