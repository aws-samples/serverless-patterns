"""Process collector: observes the target process tree from outside.

Polls ``/proc/<pid>`` for the root PID and any observed children while the
target runs, then records terminal events (exit / timeout / nonzero) from the
launch result. Environment values are never recorded (only variable names), so
canary or injected values cannot leak into the report.
"""
from __future__ import annotations

from pathlib import Path
from typing import Dict, Optional, Set
import threading
import time

from .base import Collector


def _read_proc_text(pid: int, name: str) -> Optional[str]:
    try:
        return Path(f"/proc/{pid}/{name}").read_text(encoding="utf-8", errors="replace")
    except (FileNotFoundError, ProcessLookupError, PermissionError, OSError):
        return None


def _read_cmdline(pid: int) -> Optional[list[str]]:
    raw = _read_proc_text(pid, "cmdline")
    if raw is None:
        return None
    parts = [p for p in raw.split("\x00") if p]
    return parts or None


def _read_exe(pid: int) -> Optional[str]:
    try:
        return str(Path(f"/proc/{pid}/exe").resolve())
    except (FileNotFoundError, ProcessLookupError, PermissionError, OSError):
        return None


def _read_children(pid: int) -> Set[int]:
    """Best-effort child discovery via /proc/<pid>/task/*/children."""
    children: Set[int] = set()
    task_dir = Path(f"/proc/{pid}/task")
    try:
        for task in task_dir.iterdir():
            raw = _read_proc_text_path(task / "children")
            if raw:
                children.update(int(x) for x in raw.split())
    except (FileNotFoundError, ProcessLookupError, PermissionError, OSError):
        pass
    return children


def _read_proc_text_path(path: Path) -> Optional[str]:
    try:
        return path.read_text(encoding="utf-8", errors="replace")
    except (FileNotFoundError, ProcessLookupError, PermissionError, OSError):
        return None


class ProcessCollector(Collector):
    name = "process"

    def __init__(self, sink, workspace, poll_interval: float = 0.2) -> None:
        super().__init__(sink, workspace)
        self._poll_interval = poll_interval
        self._stop = threading.Event()
        self._thread: Optional[threading.Thread] = None
        self._root_pid: Optional[int] = None
        self._seen_children: Set[int] = set()

    def on_target_started(self, pid: int) -> None:
        self._root_pid = pid
        argv = _read_cmdline(pid)
        self.sink.record(
            "process.start",
            severity="none",
            source="process",
            message="Target process started",
            pid=pid,
            process={"argv": argv, "exe": _read_exe(pid)},
        )
        self._thread = threading.Thread(target=self._poll_loop, args=(pid,), daemon=True)
        self._thread.start()

    def _poll_loop(self, root_pid: int) -> None:
        # /proc is Linux-only; on other platforms this simply observes nothing.
        proc_available = Path("/proc").is_dir()
        while not self._stop.is_set():
            if proc_available:
                for child in _read_children(root_pid):
                    if child not in self._seen_children:
                        self._seen_children.add(child)
                        self.sink.record(
                            "process.child_observed",
                            severity="low",
                            source="process",
                            message="Observed a child process spawned by the target",
                            pid=child,
                            process={"argv": _read_cmdline(child), "exe": _read_exe(child)},
                        )
            time.sleep(self._poll_interval)

    def finish(self, launch_result) -> None:
        self._stop.set()
        if self._thread is not None:
            self._thread.join(timeout=2)

        lr = launch_result
        self.sink.record(
            "process.stdout_captured", source="process",
            message="Captured target stdout", data={"path": str(lr.stdout_path)},
        )
        self.sink.record(
            "process.stderr_captured", source="process",
            message="Captured target stderr", data={"path": str(lr.stderr_path)},
        )
        if lr.timed_out:
            self.sink.record(
                "process.timeout", severity="medium", source="process",
                message="Target exceeded its timeout and was terminated",
                pid=lr.pid, data={"durationSeconds": lr.duration_seconds},
            )
        self.sink.record(
            "process.exit", severity="none", source="process",
            message="Target process exited",
            pid=lr.pid,
            data={"exitCode": lr.exit_code, "durationSeconds": lr.duration_seconds, "timedOut": lr.timed_out},
        )
        if not lr.timed_out and lr.exit_code not in (0, None):
            self.sink.record(
                "process.nonzero_exit", severity="low", source="process",
                message="Target exited with a non-zero status",
                pid=lr.pid, data={"exitCode": lr.exit_code},
            )
        super().finish(launch_result)
