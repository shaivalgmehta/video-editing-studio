# TRRS R4 A-roll: EDL (reel timeline 48.867 s, 1920x1080, 30 fps CFR, 1466 frames) - v2

Source: `podcasts/retail-razor/episodes/S6E15_leslie-ann-hall/input/S6E15 Leslie Ann Hall.mp4` (1920x1080, 29.97 fps, 44.1 kHz stereo; episode time 0 = file time 0).
Speakers: Leslie Ann Hall, plus Ricardo Belmar's "For all of them, yeah." (reel 7.56-8.47).
Script (verbatim, bracketed clause KEPT): "Oftentimes brands will come to us, and they'll have 200 products in their portfolio, and they wanna rank for everything." / R: "For all of them, yeah." / "But the truth is, they might not deserve to rank for everything. So the number one thing ... The third thing we recommend is making sure their content is understood by both humans and machines."
Show-notes said ~08:15-09:06; mp4 is 502.09-548.96 (about 4 s later, as expected).

## Kept segments
| # | source in | source out | reel in | reel out | dur | words |
|---|---|---|---|---|---|---|
| 1 | 502.090 | 548.957 | 0.000 | 46.867 | 46.867 | "Oftentimes brands will come to us" ... "both humans and machines." |

- One continuous take, no internal audio cuts. Every pause in the range is under 0.4 s (longest: 504.13-504.52 after "us,", 523.66-524.05 after "rank for.", 541.86-542.46 area after "ecosystem." measures 0.30 s of true silence), so nothing was tightened.
- In point 502.090 sits in the 40 ms silence between "succeed." (previous sentence, ends ~502.05) and "Oftentimes" (onset ~502.17). 10 ms fade-in.
- Out point 548.957 = ~0.2 s after "machines." ends and before a new sound at ~549.04 (her next phrase "So both,"). 30 ms fade-out.
- Bracketed clause "to a diverse group of customers across the entire ecosystem" is KEPT: "message" runs straight into "to" with no gap, so dropping it would need a mid-phrase cut on a rising pitch. Keeping it costs 4.6 s (reel 35.17-39.77).
- Ricardo's "For all of them, yeah." (509.65-510.56) follows "everything." with a ~30 ms gap and runs into Leslie's "But"; it's kept (it is in the script) and shown as a reaction cut.
- Transcript notes: ep_words has "want to"; the audio and the burned captions say "wanna" (used). ep_words drops the "and" before "getting" (burned captions show "and getting"); it is a short, unstressed "and" at reel 28.80-28.90, kept in words.json.

## v2 change (CD review of v1, 2026-11-02)
A final checklist card (all three rules ticked) now runs from "machines" (46.10) to 48.867. To give it a ~2.4 s hold, the A-roll is extended past her last word: the video clones its last frame (frames 1406-1465, hidden under the card) and voice.wav is padded with 2.0 s of digital silence. No new dialogue. The outro moves to 48.867.

## Video
`ffmpeg -ss 501 -i SRC -ss 1.09 -t 46.8667 -an -vf fps=30,format=yuv420p -fps_mode cfr -c:v libx264 -preset slow -crf 16 -profile:v high -frames:v 1406` (v1). v2 = the v1 file (first generation, kept as `tmp/aroll_v1.mp4`) + a 60-frame clip of its last frame (same x264 settings), joined with the concat demuxer `-c copy` (no re-encode of the speech part) -> `podcasts/retail-razor/episodes/S6E15_leslie-ann-hall/work/hyperframes/r4/assets/video/aroll.mp4` (no audio, full frame, 1466 frames = 48.867 s).

## Audio
Same in/out. Mono (L+R)/2, 48 kHz (soxr), highpass 80 Hz, deesser (i=0.25), acompressor (-24 dB, 2.5:1, 10/150 ms), +12.9 dB, alimiter (0.76), 10 ms fade-in / 30 ms fade-out, padded/trimmed to exactly 2,249,600 samples (v1). Ricardo "Okay" muted at 18.50-18.97 (-30 dB, 15 ms ramps). v2: padded with silence to 2,345,600 samples.
Result: -16.1 LUFS integrated (speech), -2.3 dBTP, 24-bit mono 48 kHz, 48.867 s -> `podcasts/retail-razor/episodes/S6E15_leslie-ann-hall/work/hyperframes/r4/assets/audio/voice.wav`.

## Crops (source px)
- Leslie base (R2): [x950, y113, w744, h875] -> `#aroll` left -1379, top -164, 2787x1568; punch origin "552px 417px".
- Ricardo: [x250, y156, w680, h799] -> `#arollR` left -397, top -248, 3049x1715 (scale 1.588). Starts at y156 (title box ends y~155) and ends at y955 (the "Recorded live at Shoptalk" box starts y~957 at x<445; burned captions y>=990).

## Words
`podcasts/retail-razor/episodes/S6E15_leslie-ann-hall/work/reels/r4/words.json`: 119 words, {"w","s","e","spk"}, reel-relative. Timed from ep_words.json (shifted by -502.09), onsets snapped to the final voice.wav envelope (-36 dB), and checked against a fresh faster-whisper medium.en pass on the final voice.wav (see NOTES.md).
