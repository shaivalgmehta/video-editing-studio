---
name: audio-cleanup-lessons
description: "What worked and what failed for cleaning the presenter's echoey phone audio (DeepFilterNet studio chain yes, resemble-enhance no)"
metadata:
  node_type: memory
  type: feedback
  originSessionId: 3ea7e804-e64c-439c-9aa4-df9ff89d47c1
  modified: 2026-10-23T15:36:46.128Z
---

For this room and mic, the chain that keeps every word is DeepFilterNet (with `--pf` post-filter since 2B) → expander → EQ (de-mud at 280 Hz, presence at 3.5 kHz, air above 9 kHz) → de-esser → 4:1 compressor; exact filters in the project skill. The CD asked for "crisp, studio" on 2B and approved this stronger chain: tail between phrases 16.5 dB under raw, 7.6 dB brighter. resemble-enhance (any strength) rewrote words ("chasing them" → "dating them") and isn't sample-aligned, so it is out; WPE dereverb measured worse than raw. The honest ceiling: the room is reduced, not erased; a lav re-record is the real fix for a booth sound, and I say so each delivery.

Timing (found on 2C/2D, Oct 2026): Parakeet word *starts* run 0.15–0.45 s early against the audio envelope and its word *ends* are inflated; whisper is early too. For cut boundaries use a `silencedetect=n=-50dB:d=0.12` map of the clean WAV (speech regions = between silences), not the word timestamps; soft first words ("The", "I") show up as 20 ms blips, so start the run early. Since 2C, `new_ad.py` runs the studio chain with `--pf` by default.

**Why:** generative enhancement looked best on the meters but failed the transcript check, the only intelligibility test I have since I can't listen.
**How to apply:** always verify cleanup with a Parakeet transcript (all words must survive) before picking; report measurements as measured, not heard. Install notes: DeepFilterNet needs torch/torchaudio 2.5.1; Parakeet via `npx hyperframes models install parakeet`.
