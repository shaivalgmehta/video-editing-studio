# TRRS R2 A-roll: EDL (reel timeline 29.000 s, 1920x1080, 30 fps CFR, 870 frames)

Source: `podcasts/retail-razor/episodes/S6E15_leslie-ann-hall/input/S6E15 Leslie Ann Hall.mp4` (1920x1080, 29.97 fps, 44.1 kHz stereo; episode time 0 = file time 0).
Speaker: Leslie Ann Hall throughout. Script: "I think the biggest difference ... fresh, new, and dynamic content."

## Kept segments
| # | source in | source out | reel in | reel out | dur | words |
|---|---|---|---|---|---|---|
| 1 | 464.240 | 493.240 | 0.000 | 29.000 | 29.000 | "I think the biggest difference" … "fresh, new, and dynamic content." |

- One continuous take, no internal cuts. Her pauses are all at or under 0.34 s (longest: 468.25–468.59 "is | that", 478.42–478.74 "decades, | and", 486.31–486.64 "brands, | and brands"; the 481.28–481.64 gap after "website." is a breath). None crossed the 0.35 s threshold, and at 29.0 s the natural cut already fits the 28–32 s target.
- In point 464.240 = 0.15 s handle before her first onset at 464.39. dropped: "And then in terms of specific tactics," (461.9–463.9).
- Out point 493.240 = about 0.14 s after "content." ends (≈493.11) and about 0.13 s before her next word "So" (onset ≈493.37). Audio has a 30 ms fade-out at the end and a 10 ms fade-in at the start.
- Ricardo makes no separate backchannel inside the range, so there was nothing to remove. Two short low-pitch (≈80–95 Hz) bits overlap her words: 473.8–474.0 ("have been") and 492.1–492.5 (start of "content"). These are probably her own vocal fry. If either is a Ricardo murmur, it sits under her words and can't be removed.

## Video
`ffmpeg -ss 463 -i SRC -ss 1.24 -t 29 -an -vf fps=30,format=yuv420p -fps_mode cfr -c:v libx264 -preset slow -crf 16 -profile:v high -frames:v 870` → `podcasts/retail-razor/episodes/S6E15_leslie-ann-hall/work/hyperframes/r2/assets/video/aroll.mp4` (no audio stream, full frame).

## Audio
Same in/out. Downmixed to mono (L+R)/2 and resampled to 48 kHz (soxr). Then: highpass 80 Hz, then deesser (i=0.25), then acompressor (-24 dB, 2.5:1), then +12.6 dB, then alimiter (0.76), then fades. Padded/trimmed to exactly 1,392,000 samples.
Result: -15.95 LUFS integrated, -2.34 dBTP, 24-bit mono 48 kHz, 29.000 s → `podcasts/retail-razor/episodes/S6E15_leslie-ann-hall/work/hyperframes/r2/assets/audio/voice.wav`.

## Square crops (source px [x, y, size])
- LESLIE_CU  [1100, 113, 460]: face and shoulders, eyes about 38% from top, lead room to the left (she looks toward Ricardo). Her head stays in frame for the whole 29 s.
- LESLIE_MED [950, 110, 720]: waist-up with both hands in frame for all gestures.
- RICARDO_REACT [340, 156, 440]: head and shoulders, starts at y=156 to clear the title box (x<420, y<155).
None of the crops touch the logo box (x>1700, y<185) or the captions (y>990).

## Gesture moments (reel time)
- 0.8–1.2 "biggest difference": both hands open, spreading
- 5.8–6.3 "really rewards": hands together, chopping
- 17.0 "With GEO": hands open
- 18.4–18.7 "much bigger opportunity": strongest hand move
- 22.0–23.0 "and brands that want to compete": sustained two-hand gesture
