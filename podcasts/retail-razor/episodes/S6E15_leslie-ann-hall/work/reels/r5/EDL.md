# TRRS R5 A-roll: EDL (reel timeline 48.100 s, 1920x1080, 30 fps CFR, 1443 frames)

Source: `podcasts/retail-razor/episodes/S6E15_leslie-ann-hall/input/S6E15 Leslie Ann Hall.mp4` (1920x1080, 29.97 fps, 44.1 kHz stereo; episode time 0 = file time 0).
Idea: "Bottom funnel bloat". Ricardo sets it up, then Leslie explains it.

## Kept segments
| # | spk | source in | source out | reel in | reel out | dur | frames | words |
|---|---|---|---|---|---|---|---|---|
| 1 | Ricardo | 775.760 | 784.427 | 0.000 | 8.667 | 8.667 | 260 | "we've spent so much time in recent years" … "driving more dollars into performance marketing." |
| 2 | Leslie | 813.860 | 853.293 | 8.667 | 48.100 | 39.433 | 1183 | "ironically, because Iced Media's roots" … "looking and prospecting for new customers." |

- Cut 1 in: 775.76 sits in the short dip (−45 to −51 dB, 775.74–775.80) between "that" and "we've". Dropped words before it: "And I know I personally feel that". The setup starts on "we've" (as scripted).
- Cut 1 out: 784.43, in the silence (784.25–784.57) after "marketing." Ricardo continues "There's been less conversation around brand marketing", which is dropped.
- Cut 2 in: 813.86, in the silence (813.73–813.98) after "And we," (dropped). Leslie's onset on "ironically" is at 813.98.
- Cut 2 out: 853.29, in the dip after "customers." and before Ricardo's "So, absolutely" (853.47).
- Leslie's segment is one continuous take with no internal cuts. Her pauses are 0.38 s at most ("that. | We call it", "sales, | and").
- Ricardo backchannels: three sit UNDER her words in the mixed track (the mics are panned, not isolated), so they can't be removed: "Yeah" around 822.2–822.5 ("go on and on"), "Okay" around 827.2 ("bloat, | where"), and "Right, right" around 836.4–837.0 ("media, | where"). They are quiet, and the show's own burned captions list them.
- The burned show captions confirm the ASR on two words: "we're a Meta business partner" (the ASR missed "we're") and "focusing on bottom of the funnel" (medium.en heard "on the bottom").

## Video
`ffmpeg -ss 770 -i SRC -ss 810 -i SRC -filter_complex "[0:v]trim=start=5.76:duration=8.666667,setpts=PTS-STARTPTS,fps=30[a];[1:v]trim=start=3.86:duration=39.433333,setpts=PTS-STARTPTS,fps=30[b];[a][b]concat=n=2:v=1:a=0,format=yuv420p" -fps_mode cfr -c:v libx264 -preset slow -crf 16 -profile:v high -frames:v 1443`, then remuxed with `-map 0:v -dn -map_chapters -1` to drop the episode's chapter data stream → `podcasts/retail-razor/episodes/S6E15_leslie-ann-hall/work/hyperframes/r5/assets/video/aroll.mp4` (full frame, no audio). The hard cut between speakers is at frame 260 (8.667 s).

## Audio
Same in/out points. Downmixed to mono (L+R)/2 and resampled to 48 kHz (soxr). Ricardo +1.0 dB to match Leslie (segments measured −24.9 / −23.9 LUFS). Fades: 10 ms in / 15 ms out on segment 1, 15 ms in / 30 ms out on segment 2. The join is silence to silence. Then highpass 80 Hz, deesser (i=0.25), acompressor (−24 dB, 2.5:1, 5/80 ms), +12.4 dB, alimiter (0.76).
Tail: a short burst at reel 47.90–48.06 (source 853.09–853.25), after "customers." ends at about 47.80, is Ricardo starting his reply (the small.en verification pass heard "Yeah"). It is muted with a 30 ms fade at 47.86–47.89, and the rest is digital silence (pre-fix copy: `tmp/voice_pre_tailfix.wav`).
Result: −16.0 LUFS integrated, −2.3 dBFS peak, 24-bit mono 48 kHz, 2,308,800 samples = 48.100 s → `podcasts/retail-razor/episodes/S6E15_leslie-ann-hall/work/hyperframes/r5/assets/audio/voice.wav`.

## Crops (source px [x, y, w, h])
- RICARDO [230, 156, 680, 800]: 1080/680 = 1.588 into the 1080x1270 window (`#aroll-r` left −365, top −248, 3049x1715). Starts at y=156 to clear the title box (x<420, y<155) and stops at y=956, above the "Recorded live at Shoptalk" box and the burned captions. Punch-in origin "480px 120px" (near the top of his head, so zooming never reveals more of the top edge).
- LESLIE [950, 113, 744, 875]: R2's base crop, unchanged (`#aroll-l` left −1379, top −164, 2787x1568; origin "552px 417px").

## words.json
`podcasts/retail-razor/episodes/S6E15_leslie-ann-hall/work/reels/r5/words.json` (91 words, spk ricardo/leslie). Times come from faster-whisper medium.en word timestamps on the source regions, shifted to reel time (Ricardo: src − 775.76; Leslie: src − 805.1933), with the text taken verbatim from the script and the show captions. `build_words.py` rebuilds it (the last word's end was then clamped to 47.86). Verified against the final voice.wav with a faster-whisper small.en pass at 16 kHz (`tmp/verify.py`). Every word lands within about 0.1 s of words.json. small.en mishears "we're a Meta" as "I met a", "bloat" as "blow", and "funnel and" as garbage. The show's burned captions and medium.en confirm the words as captioned.
