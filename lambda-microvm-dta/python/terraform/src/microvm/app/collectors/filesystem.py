"""Filesystem diff collector.

Snapshots the monitored workspace directories before and after target execution
and reports created / modified / deleted files and executable-permission
changes. Scope is intentionally limited to the analysis workspace, canary, and
tmp dirs — it never scans the whole MicroVM filesystem in v0.2.
"""
from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import Dict, Optional
import hashlib
import stat

from .base import Collector

# Only hash files at or below this size to keep snapshots cheap.
_HASH_SIZE_LIMIT = 1_048_576  # 1 MiB


@dataclass(frozen=True)
class _FileState:
    size: int
    mtime_ns: int
    mode: int
    sha256: Optional[str]

    @property
    def is_executable(self) -> bool:
        return bool(self.mode & (stat.S_IXUSR | stat.S_IXGRP | stat.S_IXOTH))


def _sha256(path: Path) -> Optional[str]:
    try:
        if path.stat().st_size > _HASH_SIZE_LIMIT:
            return None
        h = hashlib.sha256()
        with open(path, "rb") as f:
            for chunk in iter(lambda: f.read(65536), b""):
                h.update(chunk)
        return h.hexdigest()
    except (OSError, ValueError):
        return None


def _snapshot(roots, *, no_hash_roots=()) -> Dict[str, _FileState]:
    """Snapshot files under ``roots``.

    Files under any directory in ``no_hash_roots`` are stat-only (no content
    read), so snapshotting does not advance their access time. This matters for
    the canary directory, whose atime is used as a (low-confidence) read signal.
    """
    no_hash = [Path(r).resolve() for r in no_hash_roots]
    snap: Dict[str, _FileState] = {}
    for root in roots:
        root = Path(root)
        if not root.exists():
            continue
        for path in root.rglob("*"):
            if not path.is_file() or path.is_symlink():
                continue
            try:
                st = path.stat()
            except OSError:
                continue
            skip_hash = any(_under(path, nh) for nh in no_hash)
            snap[str(path)] = _FileState(
                size=st.st_size,
                mtime_ns=st.st_mtime_ns,
                mode=st.st_mode,
                sha256=None if skip_hash else _sha256(path),
            )
    return snap


def _under(child: Path, parent: Path) -> bool:
    try:
        child.resolve().relative_to(parent)
        return True
    except ValueError:
        return False


def _is_temp_like(path: str, tmp_root: Path) -> bool:
    try:
        Path(path).resolve().relative_to(tmp_root.resolve())
        return True
    except ValueError:
        return False


class FilesystemCollector(Collector):
    name = "filesystem"

    def __init__(self, sink, workspace) -> None:
        super().__init__(sink, workspace)
        self._before: Dict[str, _FileState] = {}

    def setup(self) -> None:
        super().setup()
        self._before = _snapshot(self.workspace.monitored_dirs, no_hash_roots=[self.workspace.canary])

    def finish(self, launch_result) -> None:
        after = _snapshot(self.workspace.monitored_dirs, no_hash_roots=[self.workspace.canary])
        before = self._before
        tmp_root = self.workspace.tmp

        for path, state in after.items():
            if path not in before:
                self.sink.record(
                    "file.created", severity="low", source="filesystem",
                    message="File created by target",
                    file={"path": path, "size": state.size, "sha256": state.sha256},
                )
                if state.is_executable:
                    self.sink.record(
                        "file.executable_created", severity="medium", source="filesystem",
                        message="Executable file created by target",
                        file={"path": path, "sha256": state.sha256},
                    )
                if _is_temp_like(path, tmp_root) and state.is_executable:
                    self.sink.record(
                        "file.temp_executable", severity="medium", source="filesystem",
                        message="Executable created in a temp-like directory",
                        file={"path": path},
                    )
            else:
                prev = before[path]
                if prev.sha256 != state.sha256 or prev.size != state.size or prev.mtime_ns != state.mtime_ns:
                    self.sink.record(
                        "file.modified", severity="low", source="filesystem",
                        message="File modified by target",
                        file={"path": path, "size": state.size, "sha256": state.sha256},
                    )
                if (not prev.is_executable) and state.is_executable:
                    self.sink.record(
                        "file.executable_permission_added", severity="medium", source="filesystem",
                        message="Executable permission added to a file",
                        file={"path": path},
                    )

        for path in before:
            if path not in after:
                self.sink.record(
                    "file.deleted", severity="low", source="filesystem",
                    message="File deleted by target",
                    file={"path": path},
                )
        super().finish(launch_result)
