"""Canary collector: presents fake sensitive assets and detects access.

Creates fake canary files (including an AWS-credential-shaped file) and canary
environment variables before the target runs, then infers access afterward.
File-access detection here is metadata-based (atime / mtime) and therefore
**low confidence** — the strace collector provides higher-confidence
``open``/``openat`` evidence when enabled. Canary *values* are fake and are
never written to events; only identifiers and paths are reported.
"""
from __future__ import annotations

from pathlib import Path
from typing import Dict, List
import os

from .base import Collector

# Canonical fake canary material. Values are deliberately obvious placeholders.
_CANARY_FILE_NAME = "CANARY_SECRET_DO_NOT_USE.txt"
_CANARY_FILE_BODY = "DTA_CANARY_SECRET=not-a-real-secret\n"
_CANARY_AWS_NAME = "aws_credentials_canary"
_CANARY_AWS_BODY = (
    "[default]\n"
    "aws_access_key_id = AKIAIOSFODNN7EXAMPLE\n"  # AWS's own documentation example key
    "aws_secret_access_key = wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY\n"
)
_CANARY_ENV = {"DTA_CANARY_ENV": "not-a-real-secret"}


class CanaryCollector(Collector):
    name = "canary"

    def __init__(self, sink, workspace) -> None:
        super().__init__(sink, workspace)
        self._files: List[Path] = []
        self._atime_before: Dict[str, int] = {}

    def setup(self) -> None:
        super().setup()
        secret = self.workspace.canary / _CANARY_FILE_NAME
        secret.write_text(_CANARY_FILE_BODY, encoding="utf-8")
        aws_cred = self.workspace.canary / _CANARY_AWS_NAME
        aws_cred.write_text(_CANARY_AWS_BODY, encoding="utf-8")
        self._files = [secret, aws_cred]

        for f in self._files:
            self.sink.record(
                "canary.file_presented", severity="none", source="canary",
                message="Presented a fake canary file",
                canary={"id": f.name, "path": str(f)},
            )
            try:
                self._atime_before[str(f)] = f.stat().st_atime_ns
            except OSError:
                pass

        for key in _CANARY_ENV:
            self.sink.record(
                "canary.env_presented", severity="none", source="canary",
                message="Presented a fake canary environment variable",
                canary={"id": key},
            )

    @property
    def canary_env(self) -> Dict[str, str]:
        """Canary env vars to inject into the target (called by the supervisor)."""
        return dict(_CANARY_ENV)

    def finish(self, launch_result) -> None:
        # The target ran with the canary env in scope.
        for key in _CANARY_ENV:
            self.sink.record(
                "canary.env_exposed_to_target", severity="low", source="canary",
                message="Target ran with a canary environment variable in scope",
                canary={"id": key},
            )

        # High-confidence detection: did strace observe an open of a canary path?
        # (The supervisor orders the strace collector before canary so its
        # syscall events are already in the sink.)
        strace_opened = self._strace_opened_paths()

        for f in self._files:
            fkey = str(f)
            high_confidence = fkey in strace_opened
            if high_confidence:
                event_type = (
                    "canary.aws_credential_path_touched"
                    if f.name == _CANARY_AWS_NAME
                    else "canary.file_read_observed"
                )
                self.sink.record(
                    event_type, severity="high", source="canary",
                    message="Canary file read confirmed by syscall evidence",
                    canary={"id": f.name, "path": fkey, "confidence": "high", "evidence": "strace.open"},
                )
                continue
            # Low-confidence fallback: atime advanced. This is informational only
            # (suspected) and does not by itself constitute a policy violation.
            if self._atime_advanced(f):
                self.sink.record(
                    "canary.file_touched_suspected", severity="low", source="canary",
                    message="Canary file access suspected (low-confidence atime evidence)",
                    canary={"id": f.name, "path": fkey, "confidence": "low", "evidence": "atime"},
                )
        super().finish(launch_result)

    def _atime_advanced(self, f: Path) -> bool:
        try:
            atime = f.stat().st_atime_ns
        except OSError:
            return False
        before = self._atime_before.get(str(f))
        return before is not None and atime > before

    def _strace_opened_paths(self) -> set[str]:
        opened: set[str] = set()
        canary_dir = str(self.workspace.canary.resolve())
        for event in self.sink.events():
            if event.type != "syscall.file_open" or not event.file:
                continue
            path = str(event.file.get("path") or "")
            if not path:
                continue
            resolved = self._resolve_under_canary(path, canary_dir)
            if resolved:
                opened.add(resolved)
        return opened

    def _resolve_under_canary(self, path: str, canary_dir: str) -> str | None:
        # Match canary files by basename to tolerate relative paths in strace output.
        for f in self._files:
            if Path(path).name == f.name:
                return str(f)
        return None
