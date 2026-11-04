---
name: monty-designer-repo
description: Workspace root is a local Git repo (2026-11-03) with a whitelist .gitignore that shares only the Monty motion-graphics work with a designer; Monty knowledge now lives in the CLAUDE.md files
metadata:
  node_type: memory
  type: project
  originSessionId: b37f3e4a-811c-4c51-8845-c08e2650d805
  modified: 2026-11-03T17:59:54.082Z
---

On 2026-11-03 the CD asked to get a designer onto the Monty motion-graphics work in her own Claude Code. To do that, the workspace root `DelesignAds/` was `git init`-ed (branch `main`). Nothing has been committed or pushed yet; the CD decides on the GitHub repo.

- **`.gitignore` is a whitelist.** It includes only:
  - the root `CLAUDE.md`, `SETUP.md`, `setup.ps1` and `skills-lock.json`
  - `.agents/skills` and our own `.claude/skills`
  - `_shared/tools` (without the venvs)
  - `motion-graphics/CLAUDE.md` and `motion-graphics/monty/`

  It excludes `.env`, `settings.local.json`, other clients, `input/` and `output/`, renders, snapshots and caches. About 625 files, 68 MB.
- **The HyperFrames skill links in `.claude/skills` are excluded.** They are absolute symlinks to `.agents/skills`, and `setup.ps1` recreates them as junctions on each machine.
- **Media goes through the shared drive,** in the same folder layout.
- **Monty knowledge was moved from memory into the rules files:**
  - `motion-graphics/monty/CLAUDE.md`: the wallets job, the source-folder table, the motion likes and dislikes
  - `motion-graphics/CLAUDE.md`: the 9:16 recipe and the gotchas

  **Why:** memory doesn't travel to her machine. **How to apply:** put new Monty decisions in `monty/CLAUDE.md`, not only in memory. When adding a new client or job folder to the repo, re-include it in `.gitignore`.

Related: [[monty-digital-wallets]], [[monty-esim-travel]].
