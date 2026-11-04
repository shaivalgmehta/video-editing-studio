# TRRS R1 A-roll: EDL v2 (reel timeline 30.667 s, 1920x1080, 30 fps CFR, 920 frames)

**v2 (CD note on v1: "the last line gets cut off too quickly")**: segment C picture extended by 15 frames (to source 1091.33). Ricardo's "Oh, okay" starts at 1090.84, only 80 ms after the final "s" of "confidence." (1090.76), so the voice still cuts at 1090.83. A 40 ms crossfade then runs into 0.5 s of room tone from the same recording (Ricardo's silent pause 984.70-985.30, -52 dB), with a 0.3 s fade-out. "confidence." now decays for about 0.57 s before the outro instead of 0.07 s plus a 30 ms fade. On screen she finishes the word and closes her mouth; her next line "So Reddit" starts after the cut (1091.58).

Source: `podcasts/retail-razor/episodes/S6E15_leslie-ann-hall/input/S6E15 Leslie Ann Hall.mp4` (1920x1080, 29.97 fps, 44.1 kHz stereo; episode time 0 = file time 0).
Text checked against the show's own burned-in captions (read off the mp4 every 0.5 s) and the video: the question is Ricardo's (mouth moving, his voice ~75-130 Hz), not Leslie's as the show-notes transcript says.

## Kept segments
| # | spk | source in | source out | reel in | reel out | frames | words |
|---|---|---|---|---|---|---|---|
| A | Ricardo | 981.390 | 984.623 | 0.000 | 3.233 | 97 | "How important has Reddit become in all of this now?" |
| B | Leslie (+Ricardo) | 1062.930 | 1074.263 | 3.233 | 14.567 | 340 | "On the Reddit thing specifically, we know that over half of Redditors do what they call a final check on Reddit before they make a purchase." + Ricardo "Oh, interesting." |
| C | Leslie (+Ricardo) | 1075.230 | 1091.330 (audio 1090.83 + 0.5 s room tone) | 14.567 | 30.667 | 483 | "And by the way, guilty, right? Before I book a hotel, before I buy a new running shoe—" Ricardo "Checking Reddit." Leslie "I do wanna go to Reddit and get that extra stamp of approval. So that's super important. And Reddit is the number one most trusted source to build consumer confidence." |

Cuts:
- A in 981.39: 0.1 s handle before "How" (981.50); dropped Ricardo's "Yeah." (980.5-981.2) and Leslie's previous answer. A out 984.62: in the silence after "now?" (984.60; next sound 985.4 "It's funny, right?").
- A→B: jumps over Leslie's first answer (LLM citation sources, 985-1062). B in 1062.93 sits in a 100 ms silence between "...across channels" and "On the Reddit thing".
- B→C: removes her false start "So that's a s- and," (1074.30-1075.10). B out 1074.26 is in the dip after Ricardo's "interesting." (ends 1074.22); C in 1075.23 is in the 120 ms silence before the second "and" (1075.26).
- C out 1090.83: after "confidence." (sentence-final vocal fry 1090.18-1090.42, final "s" to 1090.76) and before Ricardo's "Oh, okay." (1090.92).
- Audio: 15 ms equal-gain crossfades centred on both internal cuts; 10 ms fade-in, 30 ms fade-out.

Ricardo kept for host presence: "Oh, interesting." (reel 14.02-14.55, in her pause, clean) and "Checking Reddit." (19.57-20.09, in the gap between "shoe" and "I do"). Not removable: his short "Oh" under "Reddit- before" (≈1072.1-1072.4, reel 12.4) and under "by the way" (≈reel 15.0), and his "Yeah" under "I buy- a new" (≈reel 18.4) and under "get- that extra" (≈reel 21.5). They sit under her words; the show's own captions transcribe them as "Oh ..." / "Yeah ...". Not captioned.

## Video
`ffmpeg` three inputs (-ss 979 / 976 / 1073), `trim=start=2.39 / 86.93 / 2.23, fps=30, trim=end_frame=97 / 340 / 483`, concat → libx264 slow crf 16 high, yuv420p, `-fps_mode cfr -r 30`, no audio → `podcasts/retail-razor/episodes/S6E15_leslie-ann-hall/work/hyperframes/r1/assets/video/aroll.mp4` (920 frames).

## Audio
Region 978-1094 s downmixed to mono (L+R)/2 at 48 kHz, cut as above (`tmp/cut_audio.py`), then highpass 80 Hz → deesser (i=0.25) → acompressor (-24 dB, 2.5:1, 10/150 ms) → +12.4 dB → alimiter 0.76 → fades. Exactly 1,472,000 samples (30.6667 s) (`tmp/cut_audio_v2.py`).
Result: -16.0 LUFS integrated, -2.3 dBTP, 24-bit mono 48 kHz → `podcasts/retail-razor/episodes/S6E15_leslie-ann-hall/work/hyperframes/r1/assets/audio/voice.wav`.

## Crops (source px)
- LESLIE [950, 113, 744, 875] (as R2).
- RICARDO [200, 156, 709, 834] (same 0.85 aspect): clears the burned title box (y < 156) and the burned captions (y ≥ 990). Implemented as a GSAP `set` on `#feed` (x 1142, y -66, scale 1.0493, origin 0 0) at each Ricardo cut.

## words.json
`podcasts/retail-razor/episodes/S6E15_leslie-ann-hall/work/reels/r1/words.json` (88 words, spk leslie/ricardo, cut-relative), built by `build_words.py` from ep_words.json timings corrected against the loudness/pitch envelope; checked against the delivered voice.wav (no word starts or sits in silence: 0 flagged).


## v3 (CD: v2 "still ends abruptly", per the coordinator's spec)
- Audio only (`tmp/cut_audio_v3.py`): the source runs continuously to 1090.930 (reel 30.267), then a 25 ms crossfade (src 1090.905-1090.930) into the same room tone, then a 0.3 s fade-out. Total 920 frames, picture and all timings unchanged. Voice -16.0 LUFS / -2.3 dBTP.
- Verification: no voicing (pyin 60-400 Hz) anywhere in the last 0.8 s, so no ~90 Hz Ricardo voicing. BUT the spectra say the added 1090.84-1090.93 stretch is NOT her /s/ hiss: -30 dB, spectral centroid ~0.8 kHz, energy at 300 Hz-4 kHz, almost none at 4-10 kHz. That is the same band profile as Ricardo's voiced "Oh" (1090.95+), only quieter, so it is most likely his breathy onset. Her word ends ~1090.75: 1090.77-1090.83 is -52 dB with no sibilant energy. "confidence." here ends on a soft voiced "-dence" (centroid ~1.1 kHz) without a strong /s/.
- v2 audio is kept as `tmp/proc2v2.wav` if the CD prefers it.


## v4 (current; supersedes v2/v3 tails). Reel A-roll 31.367 s, 941 frames; total 34.367 s
- Audio (`tmp/cut_audio_v4.py`): source continuous to 1090.845 (keeps her faint final /s/ 1090.77-1090.845; Ricardo's "Oh" voices from ~1090.85), 10 ms crossfade (1090.835-1090.845) into room tone, 1.185 s tail, last 0.3 s faded. Room tone = two of her own pauses with no voicing at all, 1007.06-1007.88 and 1065.17-1065.85, joined with a 50 ms crossfade. (Ricardo's pause 984.66-985.36 and 1009.92-1010.96 were rejected: faint 70-85 Hz voiced frames.) Same chain, -15.9 LUFS / -2.3 dBTP.
- Picture: segment C runs 476 source frames (to source 1091.063: she has finished the word, eyes down, mouth closed), then that frame is held for 28 frames (0.93 s). By source 1091.20 she turns to camera and opens her mouth ahead of "So Reddit" (1091.58), so 1091.50 was not usable. The slow camera drift (1.24 -> 1.28) runs on through the hold.
- Timeline: word ends 30.18; caption "CONFIDENCE." holds to 30.97; music bed continuous at 0.2 to 31.367; outro 31.367 (music-out media 40.567), shing 31.037; header/captions/voice/aroll end 31.367; root 34.367.
- Verified: /s/ hiss present at reel 30.10-30.18 (4-10 kHz / 60-1000 Hz ratio 1.0-1.4); zero voiced frames (pyin 60-400 Hz) after 30.19; tail peak -39 dB.
- Transcript check: Whisper reads the v4 ending as "...consumer cause." (small.en) / "...Consumer Conf." (medium.en). The UNEDITED source cut at the same point (1086.10-1090.845) also reads "...Consumer Con./Conf." in medium.en, and only reads "confidence." when run on to 1091.0, i.e. including Ricardo's breathy onset. So v4 contains all of Leslie's audio; her "-dence" is soft/swallowed in the source.
- Alternate ready, NOT swapped in: `tmp/voice_v4b_ALT.wav` (`tmp/cut_audio_v4b.py`): identical to v4 but the source runs to 1090.93 (keeps the ~80 ms unvoiced onset of Ricardo's "Oh") with a 25 ms crossfade. 0 voiced frames, -15.9 LUFS, same length (drop-in for assets/audio/voice.wav). Whisper heard this ending as "confidence." in v3.
