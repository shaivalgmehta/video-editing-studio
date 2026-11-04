# Shared reel build brief (template for `work/reels/BRIEF.md`)

Write this brief once the pilot is approved. Each reel agent receives it as its only context, so it must stand alone. For a filled-in example, see `podcasts/retail-razor/episodes/S6E15_leslie-ann-hall/work/reels/BRIEF.md`.

```
# <SHOW> <SxEyy> reels — shared build brief

Client / show: <name, topic>. Guest <name, title, company>; host <name>. Release <date>.
Source: <input/...mp4> (<WxH>, <fps>). Burned-in boxes: <title box x/y>, <logo box>, <lower-third>, <caption band y≈...>. Seating: <host left/right>.
Word timings: work/episode/ep_words.json — same timebase as the mp4 (verified). Show-notes times run <±N s>; always locate lines by searching words.
Pilot to copy: work/hyperframes/<pilot>. Read index.html, compositions/*.html, build_captions.py, the pilot EDL first.

## Style (approved — do not deviate)
- Canvas, fps, background, fonts, colours (exact values).
- Header: logo only, position, size; hidden over full-screen b-roll/cards (BROLL list).
- Speaker window: position/size; per-speaker source crops [x,y,w,h]; punch-in origin; hard cuts between speakers.
- Name tags: text per speaker, position, duration.
- Captions: font/size/case, line limits, y, active/key colours, KEY set per reel.
- B-roll/cards: FULL SCREEN; literal to the line; card style reference (pilot composition).
- Do-not-show list: <guest's/client's customers and partners — never as negative examples>.
- Stock: <sources that work>, check each clip page licence, log in assets/LICENSES.md.
- Outro: compositions/outro.html unchanged, <dur> s, sfx at outro_start − 0.33 s.
- Sound: voice chain + −16 LUFS; music file, volume under voice / outro; sfx files and when.

## Audio/cut rules
Verbatim; cut at word boundaries/pauses; 10–20 ms crossfades; hard video cuts; backchannels only in gaps; unclear word → cut sentence + open question; never re-synthesise; complete endings (room-tone tail + held picture).
Deliver aroll.mp4 (full frame, CFR, no audio) + voice.wav (48 kHz, same duration) + words.json (cut-relative, verified) + EDL.md.

## Process
1. Copy the pilot project to work/hyperframes/rN WITHOUT .hyperframes/, renders/, the pilot's video/broll/voice. Rename in package.json/meta.json. Copy + repoint build_captions.py.
2. Cut A-roll, words, EDL. 3. Source/build b-roll and cards. 4. Timeline in index.html.
5. check → 0 errors. 6. Snapshot every shot change (avoid first frames, --no-end), look, iterate.
7. DO NOT RENDER. Write work/reels/rN/NOTES.md (duration, EDL, shot list, sources+licences, check status, open questions).
Only touch your own rN folders.

## Gotchas
<copy the current HyperFrames/ffmpeg gotchas from video-edit-core and the client L3>
```
