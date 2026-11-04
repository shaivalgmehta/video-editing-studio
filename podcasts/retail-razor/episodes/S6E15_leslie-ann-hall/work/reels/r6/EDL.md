# TRRS R6 A-roll: EDL (reel timeline 55.533 s, 1920x1080, 30 fps CFR, 1666 frames)

Source: `podcasts/retail-razor/episodes/S6E15_leslie-ann-hall/input/S6E15 Leslie Ann Hall.mp4` (1920x1080, 29.97 fps, 44.1 kHz stereo; episode time 0 = file time 0).
Speaker: Leslie Ann Hall throughout (no Ricardo shots, no backchannels inside the kept ranges).
Script: R6 "Shoppers added a new step before they buy" (vibes to validation). Cut built by `podcasts/retail-razor/episodes/S6E15_leslie-ann-hall/work/reels/r6/tmp/cut.py` from `tmp/segs.json`; each segment snapped to whole frames.

## Kept segments
| # | source in | source out | reel in | reel out | frames | words |
|---|---|---|---|---|---|---|
| S1 | 855.300 | 860.367 | 0.000 | 5.067 | 152 | "What we call this new customer journey at Iced Media is from vibes to validation." |
| S2a | 863.360 | 867.493 | 5.067 | 9.200 | 124 | "brand marketing, those vibes are more important than ever, especially" |
| S2b | 868.550 | 873.750 | 9.200 | 14.400 | 156 | "in a category like beauty where people are very emotionally connected to their products." |
| S3 | 888.660 | 899.460 | 14.400 | 25.200 | 324 | "I think where the AI search of it all comes in is then you need to make sure that you're giving them that validation to feel like they have the confidence to choose you." |
| S4a | 927.080 | 938.113 | 25.200 | 36.233 | 331 | "We used to see where consumers were much more likely to see something from their favorite creator, or see something unexpected, add to cart." |
| S4b | 939.200 | 941.933 | 36.233 | 38.967 | 82 | "And now there's this kind of extra step," |
| S6 | 943.620 | 951.720 | 38.967 | 47.067 | 243 | "this validation stage of saying, 'But is this the best product for me? Is it worth the price? Are there competitors I'm not aware of?'" |
| S7 | 971.840 | 980.307 | 47.067 | 55.533 | 254 | "consumers are finding out about new things, but that extra step is going to Reddit, it's going to the LLMs, and it's wanting to make sure something's right for them." |

## What was removed, and why
- Before S1: "So, absolutely, and" (the "and" ends 855.23; cut sits in the 855.23–855.33 gap).
- Between S1 and S2a: "And what we mean by that is that" (cut in the closure before "brand", 863.36).
- Between S2a and S2b: "for me working in a," — she says "in a, in a category"; the cut keeps the second "in a" (868.55, after a 70 ms silence). Verified by transcribing the join: "especially in a category like".
- Between S2b and S3: "sometimes the brand helps define them … more important than ever." (873.75–888.66).
- Start of S4a: "I think" dropped; "We" starts at 927.11 after a 60 ms gap.
- **"transact" dropped** (938.12–939.20). Both transcribers heard it as "transound"/"trans out": it isn't said clearly, so per the standing rule it was cut rather than kept. The line now reads "…add to cart. And now there's this kind of extra step". The journey card still shows the order-confirmed step on the pause after "cart."
- Between S4b and S6: "which is exactly what you're talking about," (941.93–943.62).
- After S6: "Is there something that meets my needs more specifically that I'm not aware of yet? And I think that's the biggest opportunity … validate those claims. So I think" (951.72–971.84).
- Out point 980.307: after "them." (ends ≈980.18), before Ricardo's "Yeah." (980.74).

## Video
Per segment: accurate seek, `trim` + `fps=30` + `trim=end_frame=N`, concatenated, `libx264 -preset slow -crf 16 -profile:v high`, `-an`, chapters and metadata stripped → `podcasts/retail-razor/episodes/S6E15_leslie-ann-hall/work/hyperframes/r6/assets/video/aroll.mp4` (1666 frames, 55.533 s, video stream only).

## Audio
Mono (L+R)/2 at 48 kHz, cut at the same frame-snapped points with 12 ms fade-out/fade-in at every join (no overlap, so length is exact). Then highpass 80 Hz → deesser (i=0.25) → acompressor (−24 dB, 2.5:1, 8/120 ms) → +12.4 dB → alimiter (0.79) → 10 ms fade-in / 30 ms fade-out.
Result: −16.1 LUFS integrated, −2.0 dBTP, 24-bit mono 48 kHz, 2,665,600 samples = 55.533 s → `podcasts/retail-razor/episodes/S6E15_leslie-ann-hall/work/hyperframes/r6/assets/audio/voice.wav`.

## Words
`podcasts/retail-razor/episodes/S6E15_leslie-ann-hall/work/reels/r6/words.json` (160 words, cut-relative): faster-whisper small.en on the cut voice, retimed past the dropped "transact", spelled to the script ("Iced Media", "creator,", "But is this…"), segment-initial words snapped to the first loud frame after each cut, "consumers" (S7 head) set by hand from the energy (47.08–47.67). The transcript of the cut matches the script word for word, apart from the deliberate "transact" removal. That transcript was made just before "transact" was dropped; the new "cart. | And now" join was transcribed separately ("Add to cart, and now there's this kind of extra…").
