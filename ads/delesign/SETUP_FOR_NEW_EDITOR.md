# Set up the Delesign ad editor in Claude Code

Written for whoever sets this up on a new machine. After setup, a new ad is: drop the raw footage in the job's `input/` (e.g. `ads/delesign/projects/<YYYY-MM_slug>/input/`), paste the transcript, run `/delesign-ad`.

## 1. Install on the machine

| Tool | Version that works | How |
|---|---|---|
| Claude Code | current | CLI, VS Code extension or desktop app. Open it inside the project folder. |
| Node.js | 22+ (24 in use) | nodejs.org; gives `npx` for HyperFrames |
| Python | 3.11 | python.org, on PATH. 3.11 specifically: DeepFilterNet's wheels are pinned to it |
| ffmpeg + ffprobe | 7+ (9 in use) | Windows `winget install Gyan.FFmpeg`; Mac `brew install ffmpeg` |
| Git Bash | any (Windows only) | Claude Code's Bash tool runs through it |
| Chrome/Chromium | any | HyperFrames renders through a headless browser; its CLI can fetch one |

Disk: ~5 GB. No GPU needed; a laptop CPU renders a 48 s ad in about 10 minutes.

## 2. Copy the project folder

Send the `DelesignAds` folder. Keep: every `CLAUDE.md` and `.claude/skills/` + `skills-lock.json`, `_shared/tools/*.py`, `_shared/music/mixkit/`, `ads/delesign/` (`brand/`, `templates/ad/`, `tools/`), and from `ads/delesign/projects/2026-10_meta-campaign/`: `input/EDIT_BRIEF_2A.md`, `work/hyperframes/2A`–`2D`, `work/reports/`, `output/final/` as examples. Leave out: `_shared/tools/venvs/` (rebuilt by the setup prompt), `work/render/`, `work/cut/`, `work/audio_*/`, the camera files in `input/`, and the `.hyperframes/` caches inside each HyperFrames project.

Claude's memory of the director's preferences is per person and not in the folder; the skill file carries the same decisions, so a fresh machine behaves the same. Optional: copy `memory/` from `~/.claude/projects/<this project>/` to the same place on the new machine.

## 3. One-time setup prompt (paste once, in Claude Code opened in the project folder)

```
You are the editor for Delesign's Meta ads. Read CLAUDE.md, ads/CLAUDE.md, ads/delesign/CLAUDE.md and ads/delesign/.claude/skills/delesign-ad/SKILL.md in full before doing anything else; they hold the house pipeline, the style kit and the creative director's standing decisions that you never re-ask.

Set this machine up to run that pipeline, in this order, and stop only if something fails:

1. Check tools: node --version (22+), python --version (3.11), ffmpeg -version, ffprobe. Report any that are missing with the install command for this OS, then continue with the rest.
2. Install the HyperFrames skills and CLI: run `npx skills add heygen-com/hyperframes -y`, then `npx -y hyperframes browser ensure`, then `npx -y hyperframes models install parakeet`, then `npx -y hyperframes doctor --json` and confirm it reports ok.
3. Rebuild the audio environment: create a Python venv at _shared/tools/venvs/dfn, install torch==2.5.1 and torchaudio==2.5.1 from https://download.pytorch.org/whl/cpu, then deepfilternet, soundfile and scipy. Also `pip install faster-whisper` into the system Python (it's the cross-check transcriber). Verify with `_shared/tools/venvs/dfn/Scripts/python.exe -c "from df.enhance import init_df; init_df(post_filter=True)"` (on Mac/Linux the path is _shared/tools/venvs/dfn/bin/python). Do not install resemble-enhance; it was rejected because it rewrites words.
4. Smoke test: generate a 5-second 48 kHz test tone with ffmpeg, run _shared/tools/run_dfn.py on it with --pf, then `npx -y hyperframes transcribe` on ads/delesign/projects/2026-10_meta-campaign/output/final/2A_9x16.mp4 with --engine parakeet, then `npx --yes hyperframes@0.8.217 check --json` inside ads/delesign/templates/ad. All three must succeed.
5. Report in one short message: what's installed with versions, what failed, and the exact command to run the next ad (it's in the skill under "Fast path"; scripts are run from the job folder).
```

## 4. Per-ad prompt (paste for each new ad)

Create the job folder (`ads/delesign/projects/<YYYY-MM_slug>/` with `input/ work/ output/`) or reuse the current campaign's, put the camera file in its `input/`, any Go screens or portfolio pieces in `ads/delesign/brand/go/`, then:

```
/delesign-ad

New ad: <AD NAME, e.g. 2E "Working title">.
Job folder: ads/delesign/projects/<YYYY-MM_slug>/
Raw footage: input/<FILENAME>.mp4
Go screens / portfolio pieces I've added: <list, or "none, reuse 2B's">

Transcript (reference only; captions follow what he actually says):
<PASTE TRANSCRIPT>

Run without checkpoints. Propose the direction and beat map in your delivery note. Reuse the house style and the 2A/2B scene kit; apply the director's standing decisions from the skill. Deliver output/final/<AD>_9x16.mp4, <AD>_4x5.mp4, <AD>.srt, <AD>_thumb.jpg and work/reports/QA_REPORT_<AD>.md, with measured loudness, the deviations you logged, and anything you need from me.
```

To review in stages, replace "Run without checkpoints" with "Stop at every checkpoint" (four: after audio, after the cut, after the graphics render, after exports).

## 5. What the editor needs from the director

- Raw footage: phone, portrait, one take is fine. A lav mic is the upgrade that matters most; post reduces the room, it can't remove it.
- Transcript of what was meant to be said (captions still follow the audio).
- Go screens at 2x if possible. The 2B set is reused by default.
- Portfolio pieces only if the script calls for them.
- Nothing else: B-roll from licensed free libraries, music from Mixkit, fonts and logo in the folder.

## 6. Already decided (in the skill, so nobody re-asks)

No $85,000 footnote; no blurring; face full-frame only for hook and close with Shaival in a bottom-right window for the middle; open on motion with the hook bar from frame 1; no hand-drawn circles; no representative numbers on screen; unclear words get their sentence cut, never AI voice; the studio audio chain verified by transcript.
