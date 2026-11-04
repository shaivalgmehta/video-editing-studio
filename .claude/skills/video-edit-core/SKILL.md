---
name: video-edit-core
description: Level-1 editing craft for any video in this workspace that cuts real speech. Use whenever you transcribe, pick cut points, cut A-roll + voice, tell speakers apart in one mixed track, clean or level dialogue, build words.json / captions, or verify that a cut kept every word (ads, podcast reels, teasers, VO-led motion work). Holds the tested scripts (cut_aroll, pitch_map, verify_words), the audio chain, ffmpeg 9 traps and the EDL hand-off.
---

# Video edit core (cutting, speech, audio, captions)

You can't listen or watch. Every claim about audio or picture comes from a measurement (transcript, pitch, level, spectrogram, frame snapshot). Report what was measured, not "it sounds fine", and say which calls the CD should check by ear.

## Non-negotiables
- Quotes and captions are verbatim to the audio, spelled as said ("wanna" if they say wanna). Never invent words, figures or quotes.
- A word that isn't said clearly gets its sentence or clause cut. Never patch, splice syllables, or re-synthesise a voice (no TTS, no voice cloning, no generative enhancement).
- Cut only in silences or stop-closures, never mid-word. Hard video cuts; 10–20 ms audio fades/crossfades at every join.
- Verify every cut by re-transcribing the FINAL voice track (step 7). Not done until that passes.
- Client style (caption look, crops, music) lives in the L2/L3 skills; this skill is the craft underneath.

## Workflow
1. **Ingest.** `ffprobe` the source (fps, audio rate/channels, data/chapter streams, burned-in text). Read-only `input/`; everything else under `work/`.
   Region to WAV: `ffmpeg -ss <a> -t <dur> -i SRC -vn -ac 1 -ar 48000 -c:a pcm_s24le work/.../region.wav`.
2. **Transcribe** (one job at a time; several whisper jobs starve the CPU and make `hyperframes check` time out):
   `python _shared/tools/transcribe_fw.py <wav> <out.json> [small.en|medium.en]` (system python). Pass the WAV PATH to faster-whisper, never a numpy array: an array is assumed 16 kHz, so 48 kHz samples come out as garbage and the run takes an hour. small.en for speed, medium.en to settle disputes.
   Show notes / third-party transcript timestamps drift by seconds (one episode ran ~4 s early): locate lines by searching the word list, never by the notes' clock.
3. **Map the speech.** ASR timestamps are biased (Parakeet starts 0.15–0.45 s early and ends inflated; whisper also early). Take cut boundaries from the audio, not the words:
   `ffmpeg -i clean.wav -af silencedetect=n=-50dB:d=0.12 -f null -` (speech = between silences; soft first words like "The"/"I" show as ~20 ms blips, start the run early). `_shared/tools/align_words.py` snaps ASR words onto measured speech regions.
4. **Pick cuts.** In points 0.10–0.15 s before the first onset; out points inside the silence after the last sound and before anyone else's onset. Who is talking: pitch map (below). Where a word really ends: spectrogram (below).
5. **Cut** picture + voice frame-locked: write `segs.json` `[[src_in, src_out, "label"], ...]` and run
   `python .claude/skills/video-edit-core/scripts/cut_aroll.py <source.mp4> segs.json <out_dir> [--fade-ms 12] [--lufs -16]`
   → `aroll.mp4` (30 fps CFR, crf 16, no audio, no chapter stream), `voice.wav` (48 kHz 24-bit mono, exactly frames/30 s, cleaned, −16 LUFS, ≈ −2 dBTP), `segs_snapped.json`. Tested: 2 segments → 276 frames, 441,600 samples, −16.0 LUFS / −2.0 dBTP.
   Backchannel in a gap you can't cut around: mute it (âˆ’30 dB, 15 ms ramps) so length doesn't change; keep the pre-mute copy.
6. **Clean** (if the source is noisy/echoey) — see `references/audio.md`. Voice stems −16 LUFS; delivered mix −14 LUFS / TP ≤ −1.5 dB (render_queue does that).
7. **Verify** the final voice: `python .claude/skills/video-edit-core/scripts/verify_words.py <voice.wav> <words.json> [--model medium.en]`. Exit 1 = a word is missing/changed or a caption word sits in silence. Judge each diff: known ASR mishears (names, "wanna"→"want to", unstressed "and", a soft final syllable) are fine once a second model or the source's burned captions agree; anything else means the cut lost audio. Write the call into EDL.md.
8. **Hand off**: `words.json` + `EDL.md` + `NOTES.md` (format in `references/handoff.md`), then video-qa-delivery.

## Telling speakers apart in one mixed track
Panned/mixed podcast audio can't be separated; identify by pitch, confirm by picture.
- `python .claude/skills/video-edit-core/scripts/pitch_map.py <media> <start> <end> --step 0.05 --split 150` prints `t:f0/dB[L|H]` cells (fast autocorrelation, ~20 s; `--pyin` for librosa pYIN, slower). Measure each voice on a clean stretch first. Reference case: male host ≈ 90–100 Hz (range 70–130), female guest ≈ 200–240 Hz (180–260); split at 150.
- **A quiet sound is not automatically the other speaker.** Check its pitch. We once cut a guest's drawn-out "that" (voiced at her pitch, just quieter) believing it was the host's "Okay"; the line lost a word and the caption still showed it. Before removing any "backchannel", require: pitch in the other speaker's band, AND their mouth moving / the source's burned captions attributing it.
- Murmurs that overlap the main speaker's words can't be removed: leave them uncaptioned and list them as an open question. Ones in a gap can be cut or muted.
- Vocal fry drops a female voice to 80–95 Hz at phrase ends; don't mistake it for the host.

## Where a word truly ends
Unvoiced finals (/s/, /t/, /f/, /k/, breath) carry no pitch, so a pitch map or loudness envelope ends the word too early. Zoom a spectrogram on a 0.8 s window:
```
ffmpeg -ss <t-0.4> -t 0.8 -i voice.wav -lavfi "showspectrumpic=s=1600x500:scale=log:stop=12000:legend=1" spec.png
```
Then read the PNG. Voicing = stacked horizontal harmonic stripes below ~4 kHz; /s/ = a noise block at 4–10 kHz with no stripes; silence = dark. Cut after the noise block and before the next speaker's first stripes. A next speaker's breathy onset looks like a weak 0.3–4 kHz smear with no 4–10 kHz energy: that is not your speaker's /s/.
A word that ends softly in the source can't be made crisper. Give it air instead of cutting into the next speaker: keep the source to the end of the hiss, crossfade (10 ms) into ≈0.5–1.2 s (confirm per client; Retail Razor approved ~0.6 s) of the same speaker's own room tone (two of their pauses with zero voiced frames, joined with a 50 ms crossfade) and hold the picture on a listening frame before an outro. Whisper may still mishear a soft final syllable: transcribe the UNEDITED source cut at the same point; if it mishears that too, the cut has kept everything there is.

## ffmpeg 9 / environment traps
- `-filter_complex_script` is gone: `-/filter_complex <file>`. `-vsync` is gone: `-fps_mode cfr|passthrough`. One filter output label can't be mapped to two outputs.
- Frame-accurate segment: `-ss <in-2> -i SRC` then `trim=start=2:...,setpts=PTS-STARTPTS,fps=30,trim=end_frame=N`. 29.97 sources become 30 CFR through `fps=30`.
- Podcast mp4s carry chapter/data streams: add `-map_chapters -1 -dn` or HyperFrames/concat can choke.
- `drawtext` has no fontconfig: always `fontfile=`. ffmpeg can't decode SVG (see stock-sourcing).
- `rm -rf` is denied in Bash; leave temp files in `work/<job>/tmp/` or the scratchpad, or `Remove-Item` single paths in PowerShell.
- System python has faster-whisper 1.2, numpy, soundfile, librosa, scipy. DeepFilterNet/WPE live in `_shared/tools/venvs/dfn` (see `_shared/tools/README.md`).

## References
- `references/audio.md` — cleanup chains (podcast vs phone/echo), DeepFilterNet, what failed (resemble-enhance, WPE), measuring LUFS/TP, room tone, music/SFX levels.
- `references/handoff.md` — words.json format, caption rules, EDL.md / NOTES.md templates, pacing numbers for talking-head cuts.
