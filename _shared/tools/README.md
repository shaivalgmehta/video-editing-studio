# Shared tools

Scripts used by every job. Run them from the workspace root with paths to the job's files; keep outputs in the job's `work/`.
Python: **system python 3.11** has faster-whisper 1.2, numpy, soundfile, librosa, scipy, PIL. Two venvs hold the heavy stacks (moved here 2026-11-02; their `pyvenv.cfg` still names the old path, which is harmless — call the venv's `python.exe` directly and use `python.exe -m pip`, not `pip.exe`):

| venv | python | holds |
|---|---|---|
| `venvs/dfn` | `_shared/tools/venvs/dfn/Scripts/python.exe` | DeepFilterNet 0.5.6, torch/torchaudio 2.5.1 CPU, nara_wpe |
| `venvs/pdf` | `_shared/tools/venvs/pdf/Scripts/python.exe` | PyMuPDF (`import pymupdf`), pymupdf4llm, onnxruntime — reading client PDFs/briefs |

Run only ONE whisper / DeepFilterNet job at a time; several at once starve the CPU (and make `hyperframes check` time out).

## Scripts

| Script | What it does | Call | Env |
|---|---|---|---|
| `render_queue.ps1` | Renders HyperFrames projects **one at a time** (`render -q delivery`), two-pass loudnorm to −14 LUFS / TP −1.5 / LRA 11 with the video copied, deletes the `_raw` file, prints duration + LUFS + true peak. Validates every pair before the first render and refuses to overwrite an existing output unless `-Overwrite` (archive or bump the version instead). | `powershell -ExecutionPolicy Bypass -File _shared\tools\render_queue.ps1 [-WhatIf] [-KeepRaw] [-Overwrite] [-Version 0.8.217] [-Quality delivery] <projDir> <out.mp4> [<projDir> <out.mp4> ...]` — always `-WhatIf` first; run the real queue as one background job | PowerShell 5.1, npx, ffmpeg 9 |
| `transcribe_fw.py` | faster-whisper word transcript → `[{"id","text","start","end","prob"}]`, prints the text. Passes the WAV **path** (never a numpy array: arrays are assumed 16 kHz). | `python _shared/tools/transcribe_fw.py in.wav out.json [small.en\|medium.en]` | system |
| `align_words.py` | Snaps ASR word times onto measured speech regions (`silencedetect -45 dB / 0.1 s`): ASR starts run 0.15–0.45 s early. | `python _shared/tools/align_words.py words.json cut.wav out.json` | system |
| `audio_metrics.py` | Compares cleanup candidates against the raw file: speech/pause RMS, SNR, reverb decay, HF/sibilance ratios, pumping, pause flatness. Writes `<ref>_metrics.json`. Meters rank; a transcript decides. | `python _shared/tools/audio_metrics.py raw.wav candA.wav [candB.wav ...]` | system |
| `align_check.py` | Sample lag, length diff and gain between a reference and a processed file (+ drift for files > 25 s). Use before blending wet/dry. | `python _shared/tools/align_check.py ref.wav proc.wav` | system |
| `align_env.py` | Same lag check on 1 ms RMS envelopes, for processors that regenerate phase. | `python _shared/tools/align_env.py ref.wav proc.wav` | system |
| `run_dfn.py` | DeepFilterNet3 speech enhancement, 48 kHz 24-bit mono out. `--pf` = post-filter (house "studio" chain uses it); optional `atten_lim_db` for a lighter touch. | `_shared/tools/venvs/dfn/Scripts/python.exe _shared/tools/run_dfn.py in.wav out.wav [atten_lim_db] [--pf]` | venvs/dfn |
| `run_wpe.py` | WPE late-reverb removal. Measured **worse than raw** on our phone takes; experiments only. | `_shared/tools/venvs/dfn/Scripts/python.exe _shared/tools/run_wpe.py in.wav out.wav [taps] [delay] [iters]` | venvs/dfn |
| `run_resemble.py` | resemble-enhance. **DO NOT USE.** It is generative and rewrote words ("chasing them" → "dating them"), and isn't sample-aligned. Kept only as a record; its venv was not kept. | — | — |

To re-level an already rendered file without rendering (same two-pass loudnorm): set `$env:RENDER_QUEUE_LEVEL_ONLY = "<in.mp4>|<out.mp4>"`, run `render_queue.ps1` with no pairs, then clear the variable.

Full cleanup chains and when to use which: `.claude/skills/video-edit-core/references/audio.md`.

## Related scripts in the L1 skills
| Script | Purpose |
|---|---|
| `.claude/skills/video-edit-core/scripts/cut_aroll.py` | Frame-locked A-roll + voice cut from `segs.json` (30 fps CFR mp4 without audio, exact-length −16 LUFS voice.wav, `segs_snapped.json`); `--audio-src` takes a pre-cleaned WAV |
| `.claude/skills/video-edit-core/scripts/pitch_map.py` | Who is speaking: f0 + level per 50 ms, `--split` tags low/high voice |
| `.claude/skills/video-edit-core/scripts/verify_words.py` | Re-transcribe the final voice and diff against words.json; flags missing words and caption words in silence |
| `.claude/skills/stock-sourcing/scripts/mixkit_check.py` | Mixkit page licence check (free vs Restricted), file URL, LICENSES.md line, optional download |

Client-specific tools live in `<type>/<client>/tools/` (e.g. the ad pipeline's cut/caption/finish scripts).
