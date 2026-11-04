---
name: delesign-ad-pipeline
description: "Where the reusable Delesign ad pipeline lives (project skill, scripts, template HyperFrames project) and the state of ad 2A"
metadata:
  node_type: memory
  type: project
  originSessionId: 3ea7e804-e64c-439c-9aa4-df9ff89d47c1
  modified: 2026-10-24T12:37:49.557Z
---

The full house workflow and style kit are in the project skill `.claude/skills/delesign-ad/SKILL.md` (invoke `/delesign-ad` when new footage arrives). Reusable pieces: `work/scripts/` (run_dfn.py, build_rough_cut.py, build_captions.py, finish.py, audio_metrics.py, align_check.py, transcribe_fw.py), the reference HyperFrames project `ads/delesign/projects/2026-10_meta-campaign/work/hyperframes/2A/` (copy it per ad), venvs `_shared/tools/venvs/dfn` (DeepFilterNet, torch 2.5.1) and `work/.venv_re` (resemble-enhance, rejected), Golden Gate B-roll with licenses in `assets/broll/golden_gate/`, fonts in `assets/brand/fonts/`, Mixkit music in `_shared/music/mixkit/`.

Ads 2C ("The one that shows up", guarantee script, VID20261022174728, 25.8 s) and 2D ("Some things just stick", brands script, VID20261022175328, 40.3 s) were delivered 2026-10-23 (2C v1) and 2026-10-24 (2D v2: full first line, "Feedback after" brief with the callout outlined, brand guidelines image; 41.0 s): `out/2C_*`, `out/2D_*`, reports `work/QA_REPORT_2C.md` / `_2D.md`, directions `work/DIRECTION_2C_2D.md`. CD decisions on them: guarantee is real and has no terms text (card shows no terms line); 2D hook sentence trimmed after "number"; 2B Go screens reused. New reusable pieces: `_shared/tools/align_words.py` (snaps ASR words to measured speech), phone B-roll in `assets/broll/phone/` with licenses, 2C `proof.html` (chips + proof slot) and `guarantee.html`, 2D `memory.html`, `context.html`.

Ad 2A "The fourth way" was delivered 2026-10-23 as v4 (46.8s): `out/2A_9x16.mp4`, `out/2A_4x5.mp4`, `out/2A.srt`, `out/2A_thumb.jpg`, report `work/QA_REPORT.md`, checkpoints in `work/CHECKPOINT_1..3.md`. Open follow-ups: 2x Go captures and a larger branding image would sharpen the screens; tests proposed in the QA report (hook A/B, music A/B, no-chips variant).

**Why:** the CD wants to drop raw footage and get a finished ad in the same style. **How to apply:** start from the skill, don't rebuild; see [[cd-standing-decisions]] and [[hyperframes-gotchas]].
