---
name: podcast-reel
description: End-to-end process for cutting 4–6 vertical Reels/Shorts (1080x1920) from a finished podcast episode. It runs from clip picks and verbatim scripts for the CD, through A-roll cut from a branded episode file, speaker-window layout, word-synced captions, literal full-screen b-roll and cards, and a reusable outro, to one agent per reel, central renders and posting order. Use when the CD asks for reels, shorts or clips from a podcast episode, or for a new reel in an existing show's style.
---

# Podcast reel (Reels / Shorts)

Before you start, read the following:
- the `podcast-repurposing` skill (section 2 and the packaging workflow)
- the client's level-3 skills (brand, approved pilot template, outro, show-frame crop map)
- the level-1 skills `video-edit-core`, `video-qa-delivery` and `stock-sourcing`

This skill is the podcast-specific process. Retail Razor S6E15 proved it: 6 reels, R1–R6. The worked example is in `podcasts/retail-razor/episodes/S6E15_leslie-ann-hall/work/reels/` (`BRIEF.md`, `rN/NOTES.md`, `rN/EDL.md`).

## 1. Pick the clips (editorial, before any cutting)
1. Transcribe the whole episode once to `work/episode/ep_words.json` (`[{"w","s","e"}]`) and confirm it shares the mp4's timebase. With faster-whisper, pass the wav **path**, not a numpy array; an array is assumed to be 16 kHz. Run one whisper job at a time.
2. Build an insight inventory, following the `podcast-repurposing` packaging workflow. Pick **4–6 distinct clips with one idea each**, each giving a different reason to care. Keep 1–2 alternates.
3. Give the CD a short list. For each clip include:
   - a working title
   - the angle (one sentence)
   - a **verbatim script** with speaker labels
   - **source timecodes in mp4 seconds**
   - the planned internal cuts
   - the estimated length (30–60 s)
   - the suggested posting slot

   Use `references/clip-pick-template.md`.
4. Find every line by **searching the word timings**. Show-notes timestamps drift (about 4 s early on S6E15), and show-notes transcripts mislabel speakers. Check who is speaking on the video. Speakers can be told apart by pitch, for example host ≈95 Hz and guest ≈220 Hz.
5. Keep the host: open on the host's question when it frames the idea, and keep his short reactions ("Oh, interesting.") as natural beats. The CD accepted host backchannels that overlap the guest and can't be removed. List them as open questions and don't caption them.

## 2. Pilot first, then a shared brief
- For a new show, build **one pilot reel** and iterate it with the CD until the look is approved. That pilot becomes the template.
- Then write `work/reels/BRIEF.md` from `references/build-brief-template.md`. It covers the source and its burned-in boxes, the timebase note, the pilot to copy, the exact style values, the b-roll rules, the do-not-show list, the cut rules, the deliverables, the process and the gotchas.
- Launch **one agent per reel** in parallel, each pointed at the brief. Each agent owns only its own `rN` folders. Agents build up to a passing `check` plus snapshots and a `NOTES.md`. **They do not render.**

## 3. Cut the A-roll from a finished episode
- The source is usually the published episode, with a branded frame, logo boxes and burned-in captions. Measure those boxes in pixel coordinates (title box, logo box, lower-third box, caption band) and record them in the brief or in L3.
- Give each speaker their own crop at the window's aspect ratio, inside the clean area. Check it on frames from each segment. A crop that has to clear a title box can cost headroom; flag it to the CD rather than showing the box.
- Cut at word boundaries and pauses, with 10–20 ms crossfades on internal audio joins and hard video cuts. Hide a jump cut with a punch-in or a reframe.
- Remove host backchannels only where they sit in a gap. If a word isn't said clearly, cut its sentence and list it as an open question (example: R6's "transact").
- **Endings:** let the last word decay. The CD rejected an abrupt end three times on R1. If the next speaker starts at once, crossfade into 0.5–1.2 s of room tone from the same recording and hold the picture on the speaker with the camera drift continuing, then cut to the outro.
- Before you remove a "backchannel", re-transcribe the cut and listen to it. On R3 the guest's own drawn-out "that" was taken for the host's "Okay" and cut out of the line.
- Deliverables per reel:
  - `assets/video/aroll.mp4` (full source frame, 30 fps CFR, no audio)
  - `assets/audio/voice.wav` (48 kHz, cleaned, −16 LUFS, the same length)
  - `words.json` (`[{"w","s","e","spk"}]`, cut-relative, checked against the final audio with a fresh transcription)
  - `EDL.md`

## 4. Layout (defaults proven on S6E15; confirm per client)
- 1080x1920, 30 fps, on the client's brand background.
- **No headline or title text** on the reel. The hook is in the spoken line and on the cover.
- **Header = the show logo only, top-left**, **hidden whenever full-screen b-roll or a full-screen card is on**. Keep one BROLL/hide list per reel.
- **Full-width speaker window**, like the Sharkpreneur reference: x 0, y ≈325, 1080x1270, with thin brand lines top and bottom. Cut between speakers with hard cuts.
- **The camera never sits static.** Use slow drifts, plus GSAP punch-ins (scale 1.0→~1.18, expo.out) on key words.
- **Name tag** at the lower-left of the window when each speaker first appears, for about 3 s: name, plus a role line such as "HOST, <SHOW>" or "<TITLE>, <COMPANY>".
- **Captions:** word-synced, uppercase, heavy sans, ≤3 words and ≤16 characters per line, placed below the window. The active word is highlighted and key words get the accent colour (a KEY set per reel). Captions stay on over cards; keep the cards' content clear of the caption band. For the caption build itself, see `video-edit-core`.
- **Nothing covers the speaker's face.** No chips, labels or definitions over the speaker.

## 5. B-roll and explainer cards
- They run **FULL SCREEN** (1080x1920, cover), never as a picture in a box.
- They must **literally show what the line says**: real brands, real logos, real UIs and real data. The CD rejected a library shelf for "legacy brands" and an abstract typewriter for "signals for decades". A heritage storefront and real legacy brand logos were accepted.
- When a real UI can't be captured, **rebuild it faithfully in HTML**. Reddit blocks automated capture, so R1 rebuilt Reddit's mobile thread in dark mode, with invented generic usernames, and scrolled it. AI-answer screens, Amazon-style PDPs, search results and phone notifications were done the same way. Products, brands and handles are invented. Ask the CD whether a manual screen recording is wanted instead.
- **Don't invent numbers on cards.** Spend bars, meters and counters stay without figures. A stat appears only in the speaker's own words, or attributed to them.
- Cards **explain the argument and are timed to the words**: each beat lands on its word, with a click sfx where it helps. Don't decorate.
- Never show the guest's or client's own customers or partners as negative examples. Real third-party logos are fine as neutral illustration, for example partner logos named in the line.
- For sourcing and licences, see `stock-sourcing`. Check every stock clip's own page, because some are "Restricted License". Log every source in `assets/LICENSES.md`.

## 6. Outro and sound
- Use **one reusable outro of about 3 s per show** (an L3 template), placed unchanged at the end. Its sound cue starts about 0.33 s before it.
- Mix the music bed at about 0.2 under the voice, lifting to about 0.55 for the outro. Start the bed at a media offset that puts the outro on a bar line. Add whooshes on full-screen cuts and clicks on card beats, sparingly. For levels, see `video-qa-delivery`.

## 7. QA, render, review
1. Each agent runs `check` (0 errors) and takes a snapshot at every shot change, then looks at the frames and fixes issues (`video-qa-delivery`). Accepted warnings: caption-track density, and small UI text on mock screens.
2. Each agent writes `NOTES.md` from `references/reel-notes-template.md`.
3. **Render centrally, one at a time**, from a queue (parallel renders and parallel whisper runs starve the machine). Level each render after it finishes, then put it in `output/final/reels/`.
4. Collect the CD's notes. Each fix is a new `v<N>`; the old version moves to `output/archive/`. Record what changed and why at the top of the reel's `NOTES.md`.

## 8. Posting cadence (suggestion for the CD)
- **Pre-release** (1–2 days before): the most accessible reel, alongside the teaser.
- **Launch day:** the strongest, most on-message reel, usually the one that carries the episode title.
- **Days +2 to +14:** the rest, spaced 2–3 days apart, alternating angles.
- S6E15 example order: R2 pre-release, R3 at launch, then R6, R1, R5, R4.

## CD preferences that shaped this (confirm for each new client)
- No headline on the reel.
- Full width, like the Sharkpreneur reference.
- Logo only, top-left, with no show-name text.
- No chips over the face.
- Real legacy brands, not mood b-roll.
- Real Reddit scrolling.
- Fill gaps with faces rather than filler b-roll.
- Endings complete and not clipped.
- No invented statistics.
- Invented brand mock screens are OK.
- Rebuilt dark-mode Reddit is OK.
- Licensed stock music is OK when the show theme's licence is unknown.

## Post captions
Deliver a `CAPTIONS.md` next to the finals: per reel a YouTube Shorts title and one caption used for both the Instagram caption and the YouTube description. Hook first line with searchable keywords; verbatim quotes in quotation marks; guest stats attributed to the guest; release info; "link in bio" on Instagram and the episode link on YouTube. Exactly 2 specific hashtags per post (no broad tags like #Retail or #Ecommerce); no #Shorts in titles (YouTube detects Shorts on its own). CD decision 2026-11-02.
