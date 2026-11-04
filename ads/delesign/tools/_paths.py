"""Path helpers shared by the Delesign pipeline scripts.

PROJECT  = a job folder (e.g. ads/delesign/projects/2026-10_meta-campaign) holding input/ work/ output/final/.
           Given with --project <dir>; defaults to the current working directory.
WS       = the workspace root, i.e. the first parent of this file that contains `_shared/`.
"""
import sys
from pathlib import Path


def workspace_root() -> Path:
    for p in Path(__file__).resolve().parents:
        if (p / "_shared").is_dir():
            return p
    raise SystemExit("workspace root not found (no parent folder of this script contains _shared/)")


WS = workspace_root()
DFN_PY = WS / "_shared" / "tools" / "venvs" / "dfn" / ("Scripts/python.exe" if sys.platform == "win32" else "bin/python")
RUN_DFN = WS / "_shared" / "tools" / "run_dfn.py"
TRANSCRIBE_FW = WS / "_shared" / "tools" / "transcribe_fw.py"
MUSIC_749 = WS / "_shared" / "music" / "mixkit" / "mixkit_749.mp3"


def project_dir(arg=None) -> Path:
    p = Path(arg).resolve() if arg else Path.cwd().resolve()
    if not p.is_dir():
        raise SystemExit(f"project folder not found: {p}")
    return p


def resolve_in_project(project: Path, rel: str) -> Path:
    """Resolve a path from a cut config. Tries, in order: absolute; relative to the project;
    legacy `raw/<f>` -> `input/<f>`; legacy `out/<f>` -> `output/final/<f>`; relative to the workspace root."""
    p = Path(rel)
    if p.is_absolute():
        return p
    cands = [project / p]
    parts = p.parts
    if parts and parts[0] == "raw":
        cands.append(project / "input" / Path(*parts[1:]))
    if parts and parts[0] == "out":
        cands.append(project / "output" / "final" / Path(*parts[1:]))
    cands.append(WS / p)
    for c in cands:
        if c.exists():
            return c
    return cands[1] if len(cands) > 2 else cands[0]
