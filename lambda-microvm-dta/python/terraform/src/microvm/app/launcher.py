"""Target launcher: runs the untrusted target as a child process.

The launcher is the boundary between observation and execution. It starts the
target with a fixed argv (never a shell), enforces a timeout, captures
stdout/stderr to artifact files, and returns structured metadata. Collectors
observe the process *through* this launcher (it exposes the Popen handle) rather
than the target reporting on itself.
"""
from __future__ import annotations

from dataclasses import dataclass, field
from pathlib import Path
from typing import Dict, List, Optional
import os
import signal
import subprocess
import time


@dataclass
class LaunchResult:
    argv: List[str]
    pid: Optional[int]
    exit_code: Optional[int]
    timed_out: bool
    started_at_monotonic: float
    duration_seconds: float
    stdout_path: Path
    stderr_path: Path
    started_at: str
    ended_at: str
    error: Optional[str] = None
    extra: Dict[str, object] = field(default_factory=dict)


def build_child_env(base_environment: Dict[str, str], canary_env: Dict[str, str]) -> Dict[str, str]:
    """Construct the target's environment.

    Starts from a minimal copy of the supervisor environment (PATH, HOME, etc.),
    overlays declared target environment, then canary variables. Real secrets
    must never be placed here by callers.
    """
    safe_keys = ("PATH", "HOME", "LANG", "LC_ALL", "TZ", "TMPDIR")
    env: Dict[str, str] = {k: os.environ[k] for k in safe_keys if k in os.environ}
    env.update(base_environment)
    env.update(canary_env)
    return env


def launch_target(
    argv: List[str],
    *,
    cwd: Path,
    env: Dict[str, str],
    timeout_seconds: float,
    stdout_path: Path,
    stderr_path: Path,
    wrapper: Optional[List[str]] = None,
    on_started=None,
) -> LaunchResult:
    """Run ``argv`` under ``cwd`` with a timeout, capturing output to files.

    ``wrapper`` lets a collector prepend a tracer (e.g. ``["strace", "-ff", ...,
    "--"]``); the wrapper + argv are exec'd together so the tracer is the parent
    and the target is its child. ``on_started(pid)`` is invoked once the child
    is running so a poller-based collector can begin observing immediately.
    """
    from .events import utc_now

    full_argv = list(wrapper or []) + list(argv)
    stdout_path.parent.mkdir(parents=True, exist_ok=True)
    stderr_path.parent.mkdir(parents=True, exist_ok=True)

    started_at = utc_now()
    start_mono = time.monotonic()
    timed_out = False
    error: Optional[str] = None
    exit_code: Optional[int] = None
    pid: Optional[int] = None

    with open(stdout_path, "wb") as out, open(stderr_path, "wb") as err:
        try:
            proc = subprocess.Popen(  # nosec B603 - argv list, no shell
                full_argv,
                cwd=str(cwd),
                env=env,
                stdout=out,
                stderr=err,
                stdin=subprocess.DEVNULL,
                start_new_session=True,  # own process group so we can kill the tree
            )
        except FileNotFoundError as exc:
            ended_at = utc_now()
            return LaunchResult(
                argv=full_argv, pid=None, exit_code=None, timed_out=False,
                started_at_monotonic=start_mono, duration_seconds=0.0,
                stdout_path=stdout_path, stderr_path=stderr_path,
                started_at=started_at, ended_at=ended_at,
                error=f"target executable not found: {exc}",
            )

        pid = proc.pid
        if on_started is not None:
            try:
                on_started(pid)
            except Exception:  # observation must never break execution
                pass

        try:
            exit_code = proc.wait(timeout=timeout_seconds)
        except subprocess.TimeoutExpired:
            timed_out = True
            _terminate_tree(proc)
            try:
                exit_code = proc.wait(timeout=5)
            except subprocess.TimeoutExpired:
                error = "target did not exit after kill"

    duration = time.monotonic() - start_mono
    ended_at = utc_now()
    return LaunchResult(
        argv=full_argv,
        pid=pid,
        exit_code=exit_code,
        timed_out=timed_out,
        started_at_monotonic=start_mono,
        duration_seconds=round(duration, 4),
        stdout_path=stdout_path,
        stderr_path=stderr_path,
        started_at=started_at,
        ended_at=ended_at,
        error=error,
    )


def _terminate_tree(proc: "subprocess.Popen") -> None:
    """Best-effort SIGTERM then SIGKILL of the target's process group."""
    try:
        pgid = os.getpgid(proc.pid)
    except (ProcessLookupError, PermissionError):
        pgid = None
    for sig in (signal.SIGTERM, signal.SIGKILL):
        try:
            if pgid is not None:
                os.killpg(pgid, sig)
            else:
                proc.send_signal(sig)
        except (ProcessLookupError, PermissionError):
            return
        if sig is signal.SIGTERM:
            for _ in range(20):  # up to ~2s grace
                if proc.poll() is not None:
                    return
                time.sleep(0.1)
