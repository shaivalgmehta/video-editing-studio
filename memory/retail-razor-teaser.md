---
name: retail-razor-teaser
description: "Retail Razor Show S6E15 (Leslie Ann Hall) podcast teaser — sources, project, style decisions, state"
metadata:
  node_type: memory
  type: project
  originSessionId: 71b52c47-16d0-49e6-9b8b-6322b322e454
  modified: 2026-11-02T14:25:28.088Z
---

Started 2026-10-29: 60 s 16:9 teaser for The Retail Razor Show S6E15 (guest Leslie Ann Hall, Iced Media; hosts Ricardo Belmar & Casey Golden). Release Tue Nov 3 2026 (no time given). The CD had no raw camera files, so footage is cropped out of the finished episode (`podcasts/retail-razor/episodes/S6E15_leslie-ann-hall/input/S6E15 Leslie Ann Hall.mp4`, which has a burned-in show frame + captions); crops/EDL in `podcasts/retail-razor/episodes/S6E15_leslie-ann-hall/work/episode/EDL.md` and `aroll_work/crops.json`.

HyperFrames project `podcasts/retail-razor/episodes/S6E15_leslie-ann-hall/work/hyperframes/teaser` (scenes hook, ricardo, title, seo, products, bloat, vibes, search, reddit, endcard, glitch); output `out/TRRS_S6E15_teaser_16x9.mp4`. Style: "Anatomy of a dream" reference mapped to the cover's brown/peach glow + Retail Razor red #e3262b, Montserrat 900 slams, Caveat handwriting. Music Mixkit 370 "Sparta" 120 BPM, drop at 9.5 s; ducked via `podcasts/retail-razor/episodes/S6E15_leslie-ann-hall/work/episode/duck.sh`. The teaser ends on Leslie cut off mid-sentence ("So the number one thing that we encourage is…") so the 3 rules stay hidden.

v2 (2026-10-30, `out/TRRS_S6E15_teaser_16x9_v2.mp4`) applied CD notes: brand system from the media kit pptx (bg #16171B, red #D81F26/#FF4A55, Archivo Black headlines ending in a red ".", Space Mono tracked labels, red corner glow), always show the logo caption "Cutting through the clutter", both hosts named, client/platform logos instead of text (assets/img/logos), continuous spoken captions (build_captions.py), animations that explain the argument rather than decorate, lighter grade, more eased zooms, dramatic music with hits in a separate un-ducked hits.wav. Platforms per show notes: Apple Podcasts, Spotify, YouTube, Goodpods.

v3–v5 (2026-10-30): CD reverted to the v1 look (brown/peach glow, Montserrat) but kept v2's features; title card = the supplied `S6E15 ... Video Cover.png` used exactly; handwritten graphics (name tags with drawn arrows, vibes→validation) in **Caveat Brush** (CD picked it from an 11-font sheet, rejected Mr Dafoe); whip-pans + B&W flash between sections; one "Legacy brand" row; search cards say "Competitor". Latest: `out/TRRS_S6E15_teaser_16x9_v5.mp4`. Pending: CD asked for "a 16:9 version" while v5 rendered; I asked if they meant 9:16.

v6 music (2026-10-30): client rejected the Sparta trap bed. New "mystery unfolding" bed from Mixkit 548 "A Voice from the Past" (C# minor, 108.03 BPM). Its layer entries were re-ordered onto the drama map, with synth C# pulse, pad and clock ticks, and the hits were re-tuned to C#. Files `music_v6/hits_v6/music_ducked_v6.wav`, built by `podcasts/retail-razor/episodes/S6E15_leslie-ann-hall/work/episode/music3_work/build_music3.py` + `duck_v6.sh`, checked with `verify3.py`. index.html still points at v5. The summed mix needs a final limiter (+0.3 dBTP raw).

v7 music (2026-10-30, `out/TRRS_S6E15_teaser_16x9_v7.mp4`): CD asked to replicate the reference's music grammar itself. Analysis in `podcasts/retail-razor/episodes/S6E15_leslie-ann-hall/work/episode/music4_work/REFERENCE_MUSIC.md`: 136 BPM cinematic-electronic pulse, sections switch on dialogue beats about every 4.9 s, bass-only drop-outs then a boom on the key word, host interjections surge rather than stop, one full stop under a host reaction, music about 10.7 LU under voice with little ducking, dead cut at the end. Built from Mixkit 550 "Falling Inversus" stems (`build_music4.py`, `duck_v7.sh`); index.html now plays the v7 files.

Final teaser = **v5** (CD confirmed 2026-11-02): the CD had saved it as `TRRS S6E15 Teaser.mp4`; now `output/final/teaser/TRRS_S6E15_teaser_16x9_v5.mp4`. v6/v7 were later explorations, archived.

**Why:** the CD left beat choices to me and asked for agents to speed things up. **How to apply:** for the next TRRS episode teaser, copy this project and the EDL approach. Related: [[hyperframes-gotchas]].
