# TRRS teaser template (16:9 HyperFrames, ~60 s)

Clean copy of the S6E15 teaser project (`episodes/S6E15_leslie-ann-hall/work/hyperframes/teaser`) with all episode
media and episode-specific beat scenes removed.

**Approved look = v5** (`output/final/teaser/TRRS_S6E15_teaser_16x9_v5.mp4`). The project folder was left at its v7
state. From the notes (memory `retail-razor-teaser`, `work/episode/duck_v6.sh`, `duck_v7.sh`, `music3_work`, `music4_work`),
**v6 and v7 changed only the music**. Both were unapproved explorations and are not part of this recipe:
- v6: a "mystery" bed from Mixkit 548 "A Voice from the Past", with hits re-tuned to C#.
- v7: Mixkit 550 "Falling Inversus" stems arranged to copy the reference's music grammar, with a gentle duck (ratio 1.5)
  and the files `music_v7` / `hits_v7` / `music_ducked_v7`.

The v5 audio is `music.wav` + `hits.wav` + `music_ducked.wav`, made by `duck.sh` (ratio 4, threshold 0.05, volume 0.62).
`tools/duck.sh` defaults to those settings, and `index.html` points at the v5 file names.
Caveat: I can't confirm from file history that nothing visual changed after v5. The scene files are dated 10-30, before
the v6/v7 music passes, but `captions.html` was modified later that afternoon and there is no git history. Compare a
snapshot against the v5 mp4 before reusing a beat.
Procedure: skill **trrs-teaser**. Tokens: skill **trrs-style**.

## Use
1. Copy the folder to `episodes/<SxEyy_guest>/work/hyperframes/teaser`; rename `package.json` / `meta.json`.
2. Drop in: `assets/video/aroll.mp4` (pre-cut 1920x1080 30 fps, crops baked in, black in the title/end gaps),
   `assets/audio/voice.wav`, `assets/audio/music_ducked.wav` (via `tools/duck.sh`), `assets/audio/hits.wav`,
   `assets/img/video_cover.png` (client's cover, as supplied), `assets/img/guest_cutout.png`.
3. Captions: `python tools/build_captions.py --words <voice_words.json> --out compositions/captions.html --cuts "<EDL cuts>" --fix fixes.json --cutoff-end <t>`.
4. Write one scene per body beat (start from `hook.html` / `handwrite.html`), set `glitch.html` seams, the endcard
   variables, the camera and pan/whip lists in `index.html`.
5. `npx --yes hyperframes@0.8.217 check --json` -> 0 errors; snapshot every beat and look.

## Contents
| Path | What |
|---|---|
| `index.html` | commented 60 s skeleton: hook / host / title / body example / end card, pan + whip + B&W flash system, camera zoom helper, audio layout |
| `compositions/hook.html` | cold open: tracked label + huge slammed key word, then handwritten guest name + arrow |
| `compositions/host.html` | host question: handwritten host name + arrow, words appear as spoken, key word slam |
| `compositions/title.html` | the client's video cover slammed in on the music drop, slow push |
| `compositions/handwrite.html` | Caveat Brush "from X -> Y" write-on beat |
| `compositions/endcard.html` | logo, 3-line question, sub, red date, Watch on + 4 platforms, guest cutout; variables h1/h2/h3/sub/date |
| `compositions/glitch.html` | red/cream bar glitch bursts on section seams |
| `compositions/captions.html` | GENERATED placeholder from `tools/words.sample.json` |
| `tools/build_captions.py` | teaser caption builder (segment-aware, ASR fixes, cut-off ellipsis), paths as arguments |
| `tools/duck.sh` | sidechain duck of the music bed under voice.wav, args `music voice out [dur]` |

Removed on purpose: S6E15 beat scenes `seo`, `products`, `bloat`, `search`, `reddit`, `vibes` (their ideas are listed in
the skill as patterns), all audio beds and stems, the A-roll, the cover, the cutout, guest-client logos.

## Check status
As shipped, `check` reports only missing-media lint errors: aroll.mp4, the voice/music_ducked/hits wavs, video_cover.png
and guest_cutout.png. With placeholder media (scratch test, 2026-11-02) it returns ok: true with 0 errors. The warnings
left are inherited from v5: the 26 px host role (`text_below_floor`), the 22 px platform labels on the end card, and the
peach endcard label contrast.
