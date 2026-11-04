---
name: workspace-structure
description: How this video workspace is organised - 3 levels of CLAUDE.md + skills, and input/work/output per job
metadata:
  type: project
---

The workspace is organised by type of work and client: `_shared/` (tools + venvs, music, references), then `<type>/` (ads, podcasts, motion-graphics) and `<type>/<client>/`. Each job is `projects/<YYYY-MM_slug>/` or `episodes/<SxEyy_guest>/` with `input/` (read-only client files), `work/` (incl. `work/hyperframes/`), `output/final/` + `output/archive/`. Rules and skills are layered: root `CLAUDE.md` + `.claude/skills` = L1 general editing; `<type>/` = L2; `<type>/<client>/` = L3 (brand, templates, per-deliverable skills). `podcasts/retail-razor/` is the worked example of a full L3 client. New clients start from `_templates/new-client/`, new jobs from `_templates/new-job/`.

**Why:** a repeatable process per client and per type of project, with general rules applying across all.
**How to apply:** put new jobs in the matching `<type>/<client>/` folder; add learnings to the right level's CLAUDE.md or skill, not only to memory. Related: [[trrs-reels]], [[hyperframes-gotchas]].
