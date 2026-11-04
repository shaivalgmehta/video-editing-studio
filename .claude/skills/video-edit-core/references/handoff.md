# words.json, captions, EDL and notes

## words.json
Cut-relative seconds, one entry per spoken word, speaker tagged:
```json
[{"w": "How", "s": 0.11, "e": 0.47, "spk": "host"}, ...]
```
- Text: verbatim and spelled as said; punctuation on the word it follows ("now?"). Fix ASR tokens (brand names, "Iced Media", hyphens, dropped short words) against a second model or the source's burned-in captions.
- Times: ASR times shifted by (reel_in − src_in) per segment, onsets snapped to the voice envelope (≈ −36 dB) or `align_words.py`; first word of each segment = first loud frame after the cut. Clamp the last word's end before any muted tail.
- Gate: `verify_words.py` → 0 missing/changed words (or each one explained) and 0 words in silence.

## Captions (craft rules; the look is client L3)
- Verbatim to the audio. Only the main lines are captioned; murmurs under someone else's words are not.
- Word-synced: a word appears at its `s`, never before it is said; a caption word never sits in silence.
- Short lines: ≤16 characters and ≤3 words per line on 9:16 (≈76 px heavy sans); break at phrase boundaries, not mid-name.
- Hold the final caption a little past the last word (≈0.8 s into the tail) so it doesn't vanish on the word.
- Key-word highlight sparingly (one or two per line at most), on the word that carries the idea.
- Keep captions in the safe zone (see video-qa-delivery) and clear of b-roll text and card content.
- SRT for platforms: generate from words.json, ≤2 lines, ≤42 chars/line, 1–6 s per cue.

## Pacing (talking-head ads/reels; tested on house ads)
- Gaps between phrases 0.15–0.25 s (≈60% kept after the word, 40% before the next); one deliberate ≈0.45 s beat at the turn of the argument; ≤0.15 s before each list item; ≈0.3 s + punch-in before the reveal.
- A jump cut inside one speaker needs cover: punch-in/out (100% ↔ 115%), a reframe, or a cutaway. Check cut frames for blinks and half-open mouths; nudge the in point a frame or two.
- Never a static shot for long: slow drift (1.00 → 1.04 over the shot) plus punch-ins on key words.
- Breaths/pauses ≥0.35 s are candidates for tightening; under that, leave the natural rhythm.

## EDL.md (one per deliverable, in work/)
```
# <job> A-roll EDL vN (timeline X.XXX s, WxH, 30 fps CFR, N frames)
**vN change (CD note: "..."):** what changed, why, what moved by how much.
Source: <path> (WxH, fps, audio rate/ch; time base notes)
| # | spk | source in | source out | reel in | reel out | frames | words |
What was removed and why (each cut: what sits in the gap, measured silence/voicing).
Backchannels that could not be removed (time, overlap, captioned or not).
Video: exact ffmpeg / script used.  Audio: chain, measured LUFS / dBTP, sample count.
Crops: source px [x, y, w, h] per speaker, and what they clear (burned-in titles, logos).
Verification: model(s), diffs and the call on each.
```
Keep older versions' notes; mark which is current and keep alternates (e.g. `tmp/voice_ALT.wav`) as drop-ins the CD can pick.

## NOTES.md (what the CD reads)
Final duration; one-paragraph change log per version; script as cut (verbatim); shot list with reel times and what moves on which word; b-roll sources + licences; check/snapshot status with accepted warnings; **open questions** as a short numbered list, each with the default you chose and the one-line alternative.
