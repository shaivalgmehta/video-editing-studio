# Ad 2A "The fourth way": QA report and delivery note

Date: 2026-10-23. Editor's report for the creative director. Stages 5, 6 and 7 complete on cut v2, graphics v3.

## v4 (your second note)

- "Requests stay organized" now plays the Go request-list scroll recording full-bleed under the picture-in-picture and captions (no circle, no highlight).
- The ground behind the whole middle section is a light dot pattern (#D7DEE8 dots on #F8FAFC, 30px grid) instead of plain off-white. The end card stays pure white per the brief.
- The brand board uses your "Branding Example (2)" image. It is 532px wide, so it's upscaled about 1.8x in its 950px card and reads soft; a larger file would sharpen it.
- Export re-measured: -14.0 LUFS, -1.0 dBTP, 46.80s, 11.1 Mbps. End card last second: max pixel change 5/255 (encoder noise, visually still).

## v3 layout change (your first note after delivery)

- **Face time cut to the hook and the close.** Shaival is full-frame only for the sit-down and "Did you know…" (0–2.5s), "Agency design work is the same" (7.4–8.9s), and the closing lines from "So does your client work" to the end card (38.3–43.8s). From the chips (8.9s) to the bridge B-roll (35.5s) he is a rounded picture-in-picture, bottom-left inside the safe zone, and the graphics own the frame on an off-white ground.
- **Middle graphics enlarged:** chips at 64px, counter at 56px, option cards 665px wide and 260px tall stacked to just above the caption band, portfolio flashes 665×790, Go screens as before.
- **Request list:** the hand-drawn circle is gone. The list is now a still of three request rows with a clean Sunset Orange selection outline that lands on row 1 on "requests" and steps to row 2 on "organized".
- Measured on the final export: -14.0 LUFS, -1.0 dBTP, 46.80s, 10.9 Mbps video (the encoder lands under the 14 Mbps target because the long off-white sections are cheap to encode; raise `-b:v` if a flat 12–16 is required by a platform check). Last second of the end card is pixel-still.

## Deliverables (in `/out`)

| File | Measured |
|---|---|
| `2A_9x16.mp4` | 1080×1920, H.264 High 4.1, yuv420p, 30fps, 12.4 Mbps video, AAC-LC 48 kHz (320k target, 255k measured average), 46.80s |
| `2A_4x5.mp4` | 1080×1350, same encode, re-framed by cropping 120px off the top and 450px off the bottom of the 9:16 (not squashed). Hook bar, captions, cards, Go screens and end card all inside the frame (checked at 7 moments) |
| `2A.srt` | 48 cues, US spelling, "Delesign" twice and correct, follows what he said |
| `2A_thumb.jpg` | The hook frame at 1.93s: Shaival mid-word with the hook bar |

Working masters: `work/render/2A_v2_mixed.mp4` (render + final mix), `ads/delesign/projects/2026-10_meta-campaign/work/mix/2A_mix_final.wav` (mix), `work/cut/2A_aroll_v2.mov` (locked A-roll), HyperFrames project `ads/delesign/projects/2026-10_meta-campaign/work/hyperframes/2A/`.

## Final duration

46.80s total: 43.77s of A-roll (1.83s sit-down pre-roll, first word at 1.90s, last word ends 43.04s) plus a 3.03s end card.

## Changes made after Checkpoint 3 (your notes)

1. **"Uncertainty" sentence removed.** "and have the uncertainty of their availability" is cut (raw 28.21–30.67s). Freelancers card now carries one item, "Chasing deadlines", plus the "…again?" note. Couldn't be made clearer honestly: the audio is his delivery and the brief rules out re-synthesis.
2. **Sit-down opens the ad.** Cut now starts at raw 3.9s: he walks in from the right and drops into the chair, hook bar on screen from frame 1.
3. **"× 6 clients" tag removed** (and its click).
4. **Portfolio flashes are the real pieces** you supplied: Landing pages, Ads, Social graphics (0.6s each with a slow drift).

Everything after the removed sentence was re-timed to the new word timestamps; everything before it moved later by the pre-roll.

## Audio (Stage 5)

- Voice: the Stage 2 chain (DeepFilterNet, expander, polish) on the one take; voice-plus-clicks stem taken from the HyperFrames render.
- Music bed: Mixkit track 749 ("ambient / calm / piano" tags; Mixkit license, free for commercial use, no credit). Entered 8s into the track, sits 22.8 dB under the voice before ducking, sidechain-ducked a further ~5:1 under speech, +6 dB swell from the end card, 1.4s fade on the last bar. Alternate downloaded: `_shared/music/mixkit/mixkit_139.mp3`.
- Loudness: two-pass loudnorm. Export measures **-14.0 LUFS integrated, -1.0 dBTP, LRA 2.8 LU**.
- Chosen by measurement, not by ear: I can't listen. If the bed reads wrong, every other candidate is in `_shared/music/mixkit/` with its numbers in this session's notes, and swapping is a one-line change.

## QA checklist (Stage 7)

- [x] **Frame 1 shows a face plus hook text.** *Deviation, your call:* frame 1 is now Shaival entering the frame (hook bar present, face partly out of frame for the first ~0.9s). The sit-down was your request. The thumbnail uses 1.93s, where the face and hook bar are both in.
- [x] **No silence longer than 0.4s except the deliberate beat.** In the voice stem: the pre-roll (0–1.90s, by design), the deliberate beat before "Agency design work" (0.48s), and the end-card tail. Under music the only gap is the first 0.44s of the fade-in. Nothing else over 0.4s.
- [x] **Captions match the audio word for word, US spelling, "Delesign" correct.** 48 groups from the Parakeet transcript of the cut, brand name normalized, "and there's a process" pinned (the ASR wobbled on it), "all year long" per the audio (two passes), "coat" and "graphics" corrected. No "organised"/"colour". 2–4 words per group, two lines max.
- [x] **Voice sounds close and clean, echo clearly reduced, no artifacts.** Measured, not heard: tail 4 dB drier and floor 19 dB lower than raw, every word intact on transcription. The residual room is the honest ceiling noted at Checkpoint 1.
- [x] **Nothing important in the top 14% or bottom 35%.** Hook bar top at 300px (15.6%); caption pills end at 1248px (65%); card stack ends at 1154px; picture-in-picture ends at 1142px. Verified by HyperFrames' layout audit (0 errors) and frame grabs.
- [x] **Go screenshots redacted / labeled.** Not redacted, per your instruction (names, brand names, project names visible). Every Go screen carries the grey "Illustrative workflow" label at 14px bottom-right.
- [ ] **$85,000 card has its source footnote.** Removed per your instruction. Brief rule overridden.
- [x] **No turnaround, SLA or "unlimited" claims.** On-screen text is exactly the brief's wording: chips, card titles, items, "Requests: 18 → 27 / 27 → 36 (illustrative)", "$85,000 / year", annotations, end card.
- [x] **Electric Blue only in the logo.** #334EAC appears once, as the logo fill on the end card.
- [x] **Loudness -14 LUFS ±1, peaks ≤ -1 dBTP.** -14.0 LUFS, -1.0 dBTP.
- [ ] **Watched muted and at phone size.** I can't watch; I checked 40+ frame grabs at full size and a 540p proxy, and the 4:5 at 7 moments. This one needs your eyes.
- [x] **End card holds ≥ 2.5s.** 3.03s, and the last 30 frames are pixel-identical (measured frame difference 0.000).

## Deviations from the brief, all logged

| Item | Why |
|---|---|
| No $85,000 footnote | Your instruction |
| No blurring of names/logos/clients | Your instruction |
| Cold open on the sit-down instead of on "Did" | Your instruction; frame 1 no longer shows the face |
| "Uncertainty" sentence removed | Your instruction (audio not clear) |
| Hook bar reads "round", captions read "long." | Bar keeps the brief's wording; captions follow the audio |
| "Illustrative workflow" at 14px | Brief spec; under HyperFrames' 28px phone floor |
| Active caption word 2.89:1 contrast on the pill | Brand orange on brand charcoal, as specified |
| Go screens upscaled 2x | 1x captures supplied; 2x captures would sharpen them |
| resemble-enhance not used | It rewrote words (Checkpoint 1); DeepFilterNet chain used instead |
| Music from Mixkit, chosen by measurement | No track supplied; I can't audition |

## What I'd test next

1. **Two hooks:** this sit-down open against a version starting on "Did" with the face in frame 1 (the brief's original). Same everything else; it's a one-number change in `build_rough_cut.py`.
2. **Music bed A/B:** track 749 (piano) against 139 (ambient pad).
3. **A no-chips variant** of the "Landing pages, ads, social" beat, since the chips sit over his chin; captions already carry the words.
4. **The "You can hire" line** as a pickup with "could", to restore the three-part "You could…" pattern.
5. **2x Go captures** and a real handover view for the continuity beat.
