# TRRS R3 A-roll: EDL v2 (reel timeline 59.300 s, 1920x1080, 30 fps CFR, 1779 frames)

**v2 (CD fix):** v1 cut 429.67–430.56 on the belief that the quiet sound at 429.66–430.12 was Ricardo's "Okay". In fact it is Leslie's own drawn-out "that" ("as the foundation that… drives"). Her "foundation" runs to 429.64, and the earlier dip at 429.38 is the stop inside "-tion". So v1 lost "that", which made the line sound clipped at ≈13–14 s. In v2, segments 1 and 2 are one continuous take (415.370–448.627), with her natural 0.5 s pause before "drives" kept. Everything after reel 14.3 moves by +0.900 s.

Source: `podcasts/retail-razor/episodes/S6E15_leslie-ann-hall/input/S6E15 Leslie Ann Hall.mp4` (1920x1080, 29.97 fps, 44.1 kHz stereo; episode time 0 = file time 0).
Speaker: Leslie Ann Hall throughout (Ricardo is never on screen or heard). Built by `podcasts/retail-razor/episodes/S6E15_leslie-ann-hall/work/reels/r3/build_aroll.py` from `segs.json`.
Words: `words_src.json` (episode times; ep_words.json corrected with a 20 ms energy envelope and a small.en re-transcription), then `words.json` (cut-relative).

## Kept segments
Each out point is snapped to a whole frame (moves < 17 ms).

| # | source in | source out | reel in | reel out | dur | words |
|---|---|---|---|---|---|---|
| 1 | 415.370 | 448.627 | 0.000 | 33.267 | 33.267 | "Instead of thinking of AI search" … "as the foundation that drives …" … "is not consistent," |
| 2 | 450.400 | 454.167 | 33.267 | 37.033 | 3.767 | "it's going to be harder to come up as the best answer." |
| 3 | 674.060 | 676.360 | 37.033 | 39.333 | 2.300 | "For large corporations," |
| 4 | 676.660 | 691.393 | 39.333 | 54.067 | 14.733 | "it can be a lot more challenging" … "responsible for Amazon PDPs," |
| 5 | 691.620 | 696.853 | 54.067 | 59.300 | 5.233 | "are all making sure that they're prioritizing the same products and the same messages." |

## What was removed, and why
- Before 415.37: "...creating new pathways, but". The in point sits in the 20 ms dip between "but" and "Instead" (415.34–415.38), so the reel opens on "Instead".
- (v1 only, reverted in v2) 429.67–430.56 was cut as a supposed "Okay". It was her "that"; see the v2 note above.
- 448.63–450.40: "does not continuity," plus the pause. Both the episode transcript and a fresh small.en pass hear "does not continuity" (the show notes' "have" is not audible). Per the rules (no unclear words, no patching), the clause was cut. The sentence now reads "…is not consistent, it's going to be harder to come up as the best answer."
- After 454.17: "for the products brands have the right to win." (the script ends on "best answer"). There is a 0.12 s gap between "answer" and "for".
- 672.88 and earlier: "What I find especially with our clients, that". The in point is in silence before the "f" of "For".
- 676.36–676.66: a 0.3 s breath pause after "corporations,". This jump cut is hidden by a hard punch-in (1.04 → 1.15) at reel 39.333 (v2).
- 691.39–691.62: silence after "PDPs,". The burned captions show Ricardo's "Right" around here. Pitch tracking finds no voiced sound in 691.30–691.76, so if he says it, it is too faint to register. The cut lands on the teams-card → face cut.
- After 696.85: "One, that's why for indie brands…".

## Backchannels that could not be removed (they overlap her words)
- About 434.2–435.0 (reel ≈18.9–19.5 in v2), "tactics and channels across": the burned captions show Ricardo's "I see / Yeah" here. The level stays continuous with no gap, and whisper hears "in channel" for "and channels". Captioned as "and channels" (the show notes and ep_words.json agree).
- About 683.2–683.5 (reel ≈45.8–46.1 in v2), "the paid team, | the PR team": a flat 187 Hz tail that may be Ricardo's "Yeah". It sits under the end of "team".

## Video
Per segment: `ffmpeg -ss (in-2) -i SRC -ss 2 -an -vf fps=30,format=yuv420p -fps_mode cfr -frames:v N -crf 14`, then concat and re-encode with x264 high, crf 16, 30 fps CFR. Output: `podcasts/retail-razor/episodes/S6E15_leslie-ann-hall/work/hyperframes/r3/assets/video/aroll.mp4` (full frame, no audio, 1779 frames).

## Audio
Downmixed to mono (L+R)/2, resampled to 48 kHz with soxr. Segments overlap by 15 ms with equal-power crossfades centred on each video cut, so audio and video stay frame-locked. Processing: 10 ms fade-in, highpass 80 Hz, de-esser (i=0.25), acompressor (−24 dB, 2.5:1), gain to −16 LUFS, alimiter 0.76, and a 30 ms fade-out. Output: `assets/audio/voice.wav`, 24-bit mono 48 kHz, 59.300 s (2,846,400 samples), −16.0 LUFS integrated, −2.3 dBFS peak.

## Verification
A small.en re-transcription of the final voice.wav matches words.json word for word (onsets within ±0.1 s). There are two exceptions:
- At 0.00, whisper adds "But". The in point has no audible "but" (see above). Whisper still hears "But" when the clip starts at 415.40, 415.43 or 415.46, which is already inside "Instead". So this is the model, not leftover audio.
- At reel 19.0 (v2), whisper hears "channel" rather than "channels" (the overlap described above).

- v2: a fresh small.en pass over the changed region (reel 9–22.5) reads "…share of answers as the foundation that drives all of their marketing tactics in channel across the entire ecosystem because really". That matches words.json ("channel" is the known overlap).
