"""Analysis workspace management for the v0.2 supervisor.

Each analysis runs in a dedicated workspace tree so collectors have a bounded
area to observe and cleanup is simple:

    <root>/
      workspace/   # target cwd; materialized script/archive lands here
      canary/      # fake canary files
      tmp/         # temp-like dir watched by the filesystem collector
      artifacts/   # strace logs, stdout/stderr, etc.
"""
from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
import shutil
import tarfile
import zipfile

from .target_config import TargetSpec, TargetConfigError


@dataclass(frozen=True)
class Workspace:
    root: Path
    workspace: Path
    canary: Path
    tmp: Path
    artifacts: Path

    @property
    def monitored_dirs(self) -> list[Path]:
        return [self.workspace, self.canary, self.tmp]


def prepare_workspace(root: str | Path) -> Workspace:
    root_path = Path(root).resolve()
    ws = Workspace(
        root=root_path,
        workspace=root_path / "workspace",
        canary=root_path / "canary",
        tmp=root_path / "tmp",
        artifacts=root_path / "artifacts",
    )
    for d in (ws.workspace, ws.canary, ws.tmp, ws.artifacts):
        d.mkdir(parents=True, exist_ok=True)
    return ws


def _is_within(child: Path, parent: Path) -> bool:
    try:
        child.resolve().relative_to(parent.resolve())
        return True
    except ValueError:
        return False


def materialize_target(target: TargetSpec, ws: Workspace, *, source_base: Path) -> None:
    """Place script/archive targets into the workspace before execution.

    ``command`` targets need nothing materialized — argv runs as-is in the
    workspace cwd. ``source_base`` is the directory that relative source/archive
    paths in the config are resolved against (the supervisor's app dir locally,
    or the materialized config dir in MicroVM mode).
    """
    if target.type == "command":
        return
    if target.type == "script":
        src = (source_base / target.source).resolve() if not Path(target.source).is_absolute() else Path(target.source)
        if not src.is_file():
            raise TargetConfigError(f"script source not found: {src}")
        dest = ws.workspace / src.name
        shutil.copy2(src, dest)
        dest.chmod(dest.stat().st_mode | 0o100)  # u+x
        return
    if target.type == "archive":
        arc = (source_base / target.archive).resolve() if not Path(target.archive).is_absolute() else Path(target.archive)
        if not arc.is_file():
            raise TargetConfigError(f"archive not found: {arc}")
        _safe_extract(arc, ws.workspace)
        return
    raise TargetConfigError(f"Unsupported target type for materialization: {target.type}")


def _safe_extract(archive: Path, dest: Path) -> None:
    """Extract zip/tar, refusing path-traversal entries (Zip-Slip)."""
    dest = dest.resolve()
    if zipfile.is_zipfile(archive):
        with zipfile.ZipFile(archive) as zf:
            for name in zf.namelist():
                target_path = (dest / name).resolve()
                if not _is_within(target_path, dest):
                    raise TargetConfigError(f"archive entry escapes workspace: {name}")
            zf.extractall(dest)
        return
    if tarfile.is_tarfile(archive):
        with tarfile.open(archive) as tf:
            for member in tf.getmembers():
                target_path = (dest / member.name).resolve()
                if not _is_within(target_path, dest):
                    raise TargetConfigError(f"archive entry escapes workspace: {member.name}")
            tf.extractall(dest)
        return
    raise TargetConfigError(f"archive is neither zip nor tar: {archive}")


def cleanup_workspace(ws: Workspace, *, keep_artifacts: bool = True) -> None:
    """Remove the workspace, optionally preserving collected artifacts."""
    for d in (ws.workspace, ws.canary, ws.tmp):
        shutil.rmtree(d, ignore_errors=True)
    if not keep_artifacts:
        shutil.rmtree(ws.artifacts, ignore_errors=True)
