# Video Editing Studio

A ready-to-use workspace for editing videos with [Claude Code](https://claude.com/claude-code) and
[HyperFrames](https://github.com/heygen-com/hyperframes) (HTML-to-video). Claude works as the editor, you as the
creative director. The repo carries the folder structure, the layered rules (`CLAUDE.md` files), the skills, the
helper agents, the shared scripts, reusable templates and a seed memory. It carries no client media.

## What's inside

```
CLAUDE.md                 level 1: global editing rules (verbatim captions, no invented numbers, QA gate, loudness, naming)
.claude/skills/           level 1 skills: video-edit-core, video-qa-delivery, stock-sourcing
.claude/agents/           helper agents (verifier, docs-writer, codex-reviewer, automation/integration builders)
.claude/settings.json     shared permissions (safe allow-list; deletes denied)
_shared/tools/            transcription, alignment, audio metrics, DeepFilterNet cleanup, render queue (+ README)
_shared/music|references/ empty: your licensed beds and style-reference videos go here (not committed)
ads/                      level 2: paid social ads (CLAUDE.md + ad-edit skill)
podcasts/                 level 2: podcast repurposing (reels, teasers, covers, carousels) + 4 skills
  retail-razor/           level 3 WORKED EXAMPLE: a real show's brand rules, CD decisions, skills
                          (trrs-style/-reel/-teaser/-cover/-carousel) and HyperFrames templates (reel, teaser, cover)
  retail-razor/episodes/S6E15_…/  the process record of one full episode job (briefs, EDLs, review notes, captions,
                          posting calendar) with the media removed
motion-graphics/          level 2: VO-led explainers from storyboards
_templates/new-client/    empty client skeletons per type of work
_templates/new-job/       empty input/ work/ output/ job skeleton
memory/                   seed memory for Claude (lessons learned); see "Memory" below
setup.ps1                 one-time setup (skills, tool checks, Python packages)
```

Rules load by folder: start Claude at the repo root and work inside a job folder; the `CLAUDE.md` and
`.claude/skills/` of that folder and every parent apply automatically.

## Setup (once)

1. Install **Claude Code** (CLI or the VS Code extension), **Git**, **Node.js LTS**, **ffmpeg** (`winget install Gyan.FFmpeg`)
   and **Python 3.11**.
2. Clone this repo and run from its root:
   ```
   powershell -ExecutionPolicy Bypass -File setup.ps1
   ```
   It installs the HyperFrames skills (`npx skills add heygen-com/hyperframes`, pinned by `skills-lock.json`),
   installs the Python packages in `requirements.txt` and reports anything missing. HyperFrames itself runs through
   `npx --yes hyperframes@0.8.217`.
3. Optional: DeepFilterNet audio cleanup needs its own venv. See `_shared/tools/README.md`.

## Memory

Claude Code keeps per-project memory outside the repo, in `~/.claude/projects/<project-path>/memory/`. To start
with the lessons in `memory/`, open the repo once in Claude Code, then copy the files from `memory/` into that folder
(`MEMORY.md` is the index Claude reads). Or ask Claude: "copy the seed memory from memory/ into your memory folder".

## Starting a job

1. New client: copy `_templates/new-client/<type>-client/` to `<type>/<client-slug>/`.
2. New job: copy `_templates/new-job/` to `<type>/<client>/projects/<YYYY-MM_slug>/` (or `episodes/<SxEyy_guest>/`)
   and drop the client's files into `input/`.
3. Open Claude at the repo root and say what you need, e.g. "Podcast job for <client>, episode in
   podcasts/<client>/episodes/S1E01_guest/input. Use the podcast-repurposing skill and propose 6 reels."
4. After the first approved pilot, have Claude write the client's level-3 `CLAUDE.md` and skills, the way
   `podcasts/retail-razor/` was built.

## Not included

- Client media, transcripts, client logos and photos.
- Stock music and SFX: their licences (e.g. Mixkit) don't allow redistribution. Templates list the track IDs to
  download in their `assets/LICENSES.md` / README; place them at the paths the template expects.
- Fonts in the templates are open-licence Google Fonts (OFL).
