---
name: monty-esim-travel
description: "Monty eSIM \"for Travel Industry\" [71208] motion-graphics explainer: project location, how it was built, open questions sent to the CD"
metadata:
  node_type: memory
  type: project
  originSessionId: 754dc864-b6e5-4c8c-8201-37b5a00f825f
  modified: 2026-10-29T10:54:18.042Z
---

Client job (not a Delesign ad): a 19-scene storyboard in `motion-graphics/monty/projects/2026-10_travel-industry/input/Monty eSIM for Travel Industry [71208]/Storyboard`, VO `vo.mp3` (78.3 s) and music `Proximity.wav`, styled after `motion-graphics/monty/projects/2026-10_travel-industry/input/Monty eSIM - White Label Solution Video [71109].mp4` (64 s, no hard cuts: light gradient ground, elements blur/pop in, scenes clear with whip/blur/push, VO-led with music bed).

Built 2026-10-29 as HyperFrames project `motion-graphics/monty/projects/2026-10_travel-industry/work/hyperframes/monty_travel/` (shared kit + helpers `window.MS` in index.html, one scene per `compositions/sNN.html`, scenes rebuilt as HTML in Montserrat, icons = Font Awesome 6 Free solid via CSS masks, Lisbon photo extracted from Scene15.ai with PyMuPDF in `_shared/tools/venvs/pdf`). v1 render: `out/Monty_eSIM_Travel_Industry_v1.mp4`, 81 s.

Decisions made: S4 plays before S3 so they sit on the VO; music extended by repeating 4 bars (112 BPM, 54.43–63.0 s) so its final hit lands on montyesim.com; drop at 21.4 s lands on "Three ways to partner". Flagged storyboard typos kept as drawn: S18 second row also says "Today"; S14 hotel column header says "Your airline".

**Why:** the CD may come back with notes. **How to apply:** edit scene files, keep slot timing table in index.html; see [[hyperframes-gotchas]].
