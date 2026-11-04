# Audio: cleanup, levels, what failed

## Pick the chain by source
**Clean source (podcast mics, finished episode, decent camera audio)** — light touch, what `cut_aroll.py` does by default:
mono `(L+R)/2` at 48 kHz → `highpass=f=80` → `deesser=i=0.25` → `acompressor=threshold=-24dB:ratio=2.5:attack=8:release=120` → gain to −16 LUFS → `alimiter=limit=0.79:level=false` → 10 ms fade-in / 30 ms fade-out. Lands −16.0 LUFS, −2.0 to −2.3 dBTP.
If two speakers were recorded at different levels, gain-match segments first (measure each with ebur128; e.g. host −24.9 vs guest −23.9 → host +1.0 dB).

**Noisy / echoey phone or room audio** — "studio" chain, approved by the CD, keeps every word:
1. DeepFilterNet with post-filter (venv python, see `_shared/tools/README.md`):
   `_shared/tools/venvs/dfn/Scripts/python.exe _shared/tools/run_dfn.py in.wav out_dfn.wav --pf` (optional 3rd arg `atten_lim_db`, e.g. 20, for a lighter touch).
2. `agate=threshold=0.01:ratio=2.5:attack=10:release=220:knee=6,highpass=f=90,equalizer=f=280:t=q:w=1.2:g=-4,equalizer=f=3500:t=q:w=1:g=3,highshelf=f=9000:g=2,deesser=i=0.55:m=0.5:f=0.5,acompressor=threshold=-20dB:ratio=4:attack=8:release=120:makeup=2.5`
   Measured on that room: tail between phrases 16.5 dB under raw, 7.6 dB brighter.
   Gentler variant: `agate=threshold=0.006:ratio=2:attack=15:release=300:knee=8,highpass=f=80,equalizer=f=300:t=q:w=1:g=-2,equalizer=f=4000:t=q:w=1:g=2,deesser=i=0.5:m=0.5:f=0.5,acompressor=threshold=-18dB:ratio=3:attack=10:release=150:makeup=2`.
3. Clean BEFORE cutting (on the whole region), then cut with `cut_aroll.py ... --audio-src clean.wav --audio-offset <region start> --chain anull`, so the denoiser never sees a join.
Honest ceiling: the room is reduced, not erased. A lav re-record is the real fix; say so in the delivery note.

## What not to use
- **resemble-enhance (`_shared/tools/run_resemble.py`) — never.** It is generative: at every strength it rewrote words ("chasing them" → "dating them") and isn't sample-aligned. It looked best on the meters and failed the transcript check. Its venv isn't kept; don't reinstall it. Same rule for any AI "enhance"/voice-regeneration service.
- **WPE dereverb (`run_wpe.py`)** measured worse than raw on our phone takes. Kept only for experiments.
- Never judge a cleanup by meters alone: `audio_metrics.py` ranks candidates, a transcript decides (every word must survive).

## Comparing candidates
`python _shared/tools/audio_metrics.py raw.wav candA.wav candB.wav` → speech/pause RMS, SNR, decay (reverb proxy), HF ratio (dull vs harsh), sibilance, pumping, pause flatness (warble). Then transcribe each candidate and diff against the raw transcript. Blending wet/dry? Check lag first: `align_check.py ref.wav proc.wav` (sample-level) or `align_env.py` (envelope, for vocoder output).

## Measuring
- Integrated + true peak: `ffmpeg -hide_banner -nostats -i f -af ebur128=peak=true -f null -` → last `I:` (LUFS) and `Peak:` (dBFS true peak).
- Single-pass `loudnorm` lands ~0.5 LU off and can overshoot TP (a deliverable measured âˆ’13.6 LUFS / âˆ’1.1 dBTP). For deliverables use two-pass (measure with `print_format=json`, then `measured_*` + `linear=true`); `_shared/tools/render_queue.ps1` does this.
- Targets: voice stem −16 LUFS integrated, ≈ −2 dBTP. Delivered mix −14 LUFS, TP ≤ −1.5 dB, LRA 11.

## Room tone
Build it from the SAME speaker's own pauses with zero voiced frames (pitch_map shows all 0) — another speaker's pause often hides faint 70–85 Hz voicing. Join two pauses with a 50 ms crossfade if one is too short; fade the last 0.3 s. Use it to give a soft final word air (≈0.5–1.2 s; confirm per client — Retail Razor approved ~0.6 s) or to fill a muted backchannel.

## Music and SFX under voice (starting points, tune per client)
- Bed under speech ≈ 0.2 linear volume (≈ −14 dB) of a −14 LUFS music file; lift to ≈ 0.55 for an outro/end card. Start the bed at a media offset so a bar line lands on the outro cut (bar = 60/BPM × 4).
- SFX sparse: whoosh on full-screen cuts (start ~0.15 s before the cut), soft click on card beats, one impact on the key word. Bundled SFX: `.claude/skills/media-use/audio/assets/sfx/`.
- Check the mix by measurement: integrated LUFS of the final, and that speech segments stay ≥ 10 dB above the bed (ebur128 momentary in a pause vs in speech).
