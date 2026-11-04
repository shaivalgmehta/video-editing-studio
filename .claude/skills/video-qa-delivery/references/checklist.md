# Pre-delivery checklist (copy into NOTES.md / QA report and tick with measured values)

## Edit and words
- [ ] Script as cut is verbatim; every removed clause has a reason in EDL.md
- [ ] `verify_words.py` on the final voice: 0 unexplained diffs, 0 caption words in silence (model + date noted)
- [ ] No sentence kept with an unclear word; no patched or synthesised audio
- [ ] Every "other speaker" removal confirmed by pitch + picture/burned captions
- [ ] Final word has its full tail (spectrogram checked); no clipped onset of the next speaker

## Picture
- [ ] `hyperframes check --json`: ok, 0 errors; accepted warnings listed with reasons
- [ ] Snapshots of every shot change + beats looked at (sheet paths listed); fixes re-snapshotted
- [ ] Safe zones: top 168 px, right rail x > 940, captions above y ≈ 1500 (ads: 300–1248)
- [ ] Nothing covers the speaker's face; burned-in source graphics cropped out
- [ ] Text contrast fixed where flagged; caption line legible on every background
- [ ] B-roll literally matches each line; no generic mood stock; no invented statistics on screen
- [ ] Logos/brands: none of the client's own clients/partners shown as negative examples (L3 list)

## Audio
- [ ] Voice stem −16 LUFS (±0.3), ≈ −2 dBTP
- [ ] Delivered mix −14.0 LUFS (±0.5), true peak ≤ −1.5 dB (render_queue printout)
- [ ] Music bed under speech, outro lift on a bar line; SFX sparse
- [ ] Every stock/music/SFX/logo source logged in `assets/LICENSES.md` with page URL, file URL, licence, check date

## File
- [ ] ffprobe: H.264 High, yuv420p, correct WxH, 30/1, AAC 48 kHz; duration = timeline
- [ ] blackdetect/freezedetect clean (or intended holds noted)
- [ ] Contact sheet of the final mp4 looked at
- [ ] Name `<CLIENT>_<project>_<deliverable>_<aspect>_v<N>.mp4`; previous version moved to `output/archive/`; no `_raw` left
- [ ] Covers: 9:16 + 3:4 grid crop checked; SRT if the platform needs it
- [ ] CD summary: paths, duration, LUFS/TP, changes, open questions (with defaults)
