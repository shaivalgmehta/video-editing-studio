# Video editing workspace

This folder holds every video job the studio edits. The user is the creative director (CD); Claude is the editor.
Rules and skills are layered. Work inside a project folder and the `CLAUDE.md` + `.claude/skills/` of that folder and of every parent folder apply:

| Level | Where | Holds |
|---|---|---|
| 1 General video editing | `./CLAUDE.md`, `./.claude/skills/` | rules and procedures for any edit (cutting, audio, captions, HyperFrames, QA, delivery, sourcing) |
| 2 Type of work | `ads/`, `podcasts/`, `motion-graphics/` | what is specific to that kind of video (e.g. repurposing a podcast into reels) |
| 3 Client | `<type>/<client>/` (worked example: `podcasts/retail-razor/`) | the client's brand, standing CD decisions, templates, and per-deliverable skills (reel, teaser, cover…) |

## Layout

```
_shared/            tools/ (scripts + tools/venvs/), music/, references/ (style reference videos)
<type>/
  CLAUDE.md, .claude/skills/          level 2
  <client>/
    CLAUDE.md, .claude/skills/        level 3
    brand/       logos, fonts, media kits, client-supplied b-roll
    reference/   style references for this client (optional)
    templates/   reusable HyperFrames projects (copy, never edit in place)
    tools/       client-specific scripts (optional)
    projects/<YYYY-MM_slug>/  or  episodes/<SxEyy_guest-slug>/
      input/     exactly what the client supplied — read-only
      work/      everything intermediate (transcripts, EDLs, audio, HyperFrames projects under work/hyperframes/)
      output/final/    current deliverables only
      output/archive/  superseded versions
```

Start a new client by copying `_templates/new-client/<type>-client/` to `<type>/<client-slug>/` and writing its `CLAUDE.md` (brand, standing CD decisions) after the first approved pilot.
Start a new job by copying `_templates/new-job/` into the client's `projects/` or `episodes/`, putting the client's files in `input/`, and copying from the client's `templates/`.
Media never goes into Git: `input/`, `output/`, renders and footage stay on local disk or a shared drive (see `.gitignore`).

## Global rules (all work)
- Quotes and captions are verbatim to the audio. A word that isn't said clearly gets its sentence cut; never patch or re-synthesise a voice.
- Never invent statistics, quotes, claims or numbers on screen. Illustrative motion graphics carry no made-up figures.
- B-roll must literally show what the line says (real brands, real UIs, real places); generic mood stock is not acceptable.
- Every stock/logo source is licence-checked on its own page and logged in the project's `assets/LICENSES.md`.
- Before a render: `npx --yes hyperframes@0.8.217 check` with 0 errors, then snapshot every shot change and look at the frames.
- Render one video at a time (parallel renders starve the machine). Level delivered audio to −14 LUFS integrated, true peak ≤ −1.5 dB (voice stems −16 LUFS). Delete `_raw` pre-levelling renders after levelling.
- Deliverable names: `<CLIENT>_<project>_<deliverable>_<aspect>_v<N>.mp4`; only the current version in `output/final/`, older ones in `output/archive/`.
- Present proposals and open questions to the CD in short, plain lists; the CD gives short review notes.
