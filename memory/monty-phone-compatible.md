---
name: monty-phone-compatible
description: "Monty \"Is My Phone eSIM Compatible [71273]\" 44.5 s how-to: HyperFrames project monty_phone_check, captions top-centre, v1 rendered 2026-11-04"
metadata:
  node_type: memory
  type: project
  originSessionId: 5c817354-7672-4cc3-b538-1f430a863dd3
  modified: 2026-11-04T11:04:20.041Z
---

Job folder `motion-graphics/monty/projects/Is My Phone eSIM Compatible [71273]/`. The pptx storyboard holds the VO script; the client VO `input/vo.mp3` (42.45 s) matches it word for word. The CD drew `input/Scene 1-3.png`; I built Scenes 4-6 frames in `work/frames/` (HTML → PNG via headless Chrome).

Video: `work/hyperframes/monty_phone_check/` (wallets v1 kit), v1 → `output/final/Monty_eSIM_Is_My_Phone_Compatible_16x9_v1.mp4`. Details, slot table, music edit and open questions are in `work/NOTES.md`.

CD decision: **captions top-centre** on this job (phones fill the bottom of the frames).
Gotcha: `_shared/tools/render_queue.ps1` fails on paths with `[...]` (PowerShell wildcard); render with `npx hyperframes render` + the two-pass loudnorm by hand.

**How to apply:** for notes, edit scene files and re-render as v2; 9:16 comes after the CD approves v1. See [[monty-digital-wallets]], [[feedback-build-storyboard-asks]].
