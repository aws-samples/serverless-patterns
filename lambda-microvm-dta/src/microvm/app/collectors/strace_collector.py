"""strace syscall collector.

Wraps the target argv with ``strace -ff`` so the tracer is the parent and the
target is its child — user-space syscall tracing via ptrace, no eBPF/Tracee/
Falco required. After the target exits, the per-PID strace logs are parsed into
normalized syscall events and kept as raw artifacts.

Limitations (documented in the support boundary): strace adds runtime overhead,
can miss anti-debugging targets, and is not a high-performance production
sensor. It is appropriate for CI DTA-style analysis where the supervisor
launches the target.
"""
from __future__ import annotations

from pathlib import Path
from typing import Dict, List, Optional
import re
import shutil

from .base import Collector

_STRACE_CLASSES = "process,file,network,signal"

# Syscalls we normalize. Mapping: syscall name -> (event type, severity).
_SYSCALL_EVENTS: Dict[str, tuple[str, str]] = {
    "execve": ("syscall.execve", "low"),
    "execveat": ("syscall.execve", "low"),
    "clone": ("syscall.clone", "low"),
    "clone3": ("syscall.clone", "low"),
    "fork": ("syscall.clone", "low"),
    "vfork": ("syscall.clone", "low"),
    "open": ("syscall.file_open", "none"),
    "openat": ("syscall.file_open", "none"),
    "creat": ("syscall.file_open", "low"),
    "unlink": ("syscall.file_delete", "low"),
    "unlinkat": ("syscall.file_delete", "low"),
    "rename": ("syscall.file_write_path", "low"),
    "renameat": ("syscall.file_write_path", "low"),
    "renameat2": ("syscall.file_write_path", "low"),
    "chmod": ("syscall.file_permission_change", "low"),
    "fchmod": ("syscall.file_permission_change", "low"),
    "fchmodat": ("syscall.file_permission_change", "low"),
    "chown": ("syscall.file_permission_change", "low"),
    "fchown": ("syscall.file_permission_change", "low"),
    "fchownat": ("syscall.file_permission_change", "low"),
    "socket": ("syscall.socket", "low"),
    "connect": ("syscall.connect", "medium"),
    "bind": ("syscall.bind", "low"),
    "listen": ("syscall.bind", "low"),
    "accept": ("syscall.socket", "none"),
    "accept4": ("syscall.socket", "none"),
    "sendto": ("syscall.connect", "low"),
    "recvfrom": ("syscall.socket", "none"),
    "mprotect": ("syscall.mprotect", "low"),
    "setuid": ("syscall.privilege_change_attempt", "high"),
    "setgid": ("syscall.privilege_change_attempt", "high"),
    "setreuid": ("syscall.privilege_change_attempt", "high"),
    "setregid": ("syscall.privilege_change_attempt", "high"),
    "capset": ("syscall.capability_change_attempt", "high"),
}

# strace line: "[pid 1234] 1700000000.123 execve("/bin/sh", ["sh"], ...) = 0"
# With -ff and -o FILE.PID, the [pid N] prefix may be absent; PID comes from the
# filename suffix. We capture optional pid, optional timestamp, syscall, args.
_LINE_RE = re.compile(
    r"^(?:\[pid\s+(?P<pid>\d+)\]\s+)?"
    r"(?P<ts>\d+\.\d+\s+)?"
    r"(?P<call>[a-zA-Z0-9_]+)\((?P<args>.*?)\)\s*=\s*(?P<ret>-?\d+|\?|0x[0-9a-fA-F]+).*$"
)

_CONNECT_ADDR_RE = re.compile(r'sin_addr=inet_addr\("(?P<ip>[0-9.]+)"\)')
_CONNECT_PORT_RE = re.compile(r"sin_port=htons\((?P<port>\d+)\)")
_CONNECT6_ADDR_RE = re.compile(r'inet_pton\([^,]+,\s*"(?P<ip>[0-9a-fA-F:]+)"')
_FIRST_STR_ARG_RE = re.compile(r'"((?:[^"\\]|\\.)*)"')


class StraceCollector(Collector):
    name = "strace"

    def __init__(self, sink, workspace, fail_closed: bool = True) -> None:
        super().__init__(sink, workspace)
        self._fail_closed = fail_closed
        self._trace_dir = workspace.artifacts / "strace"
        self._strace_path: Optional[str] = None

    @staticmethod
    def is_available() -> bool:
        return shutil.which("strace") is not None

    def setup(self) -> None:
        super().setup()
        self._trace_dir.mkdir(parents=True, exist_ok=True)
        self._strace_path = shutil.which("strace")
        if self._strace_path is None:
            self.fail("strace binary not found on PATH")
            self.sink.record(
                "collector.strace_failed", severity="medium", source="strace",
                message="strace is not available; syscall evidence will be missing",
            )
            return
        self.sink.record("collector.strace_started", source="strace", message="strace collector armed")

    @property
    def strace_wrapper(self) -> Optional[List[str]]:
        if self._strace_path is None:
            return None
        trace_prefix = str(self._trace_dir / "trace")
        return [
            self._strace_path,
            "-ff",
            "-ttt",
            "-s", "256",
            "-o", trace_prefix,
            "-e", f"trace={_STRACE_CLASSES}",
            "--",
        ]

    @property
    def available(self) -> bool:
        return self._strace_path is not None

    def finish(self, launch_result) -> None:
        if self._strace_path is None:
            # already recorded failure in setup
            if self.status.status != "failed":
                self.fail("strace unavailable")
            super().finish(launch_result)
            return
        trace_files = sorted(self._trace_dir.glob("trace.*"))
        if not trace_files:
            self.fail("strace produced no trace files")
            self.sink.record(
                "collector.strace_failed", severity="medium", source="strace",
                message="strace produced no output",
            )
            super().finish(launch_result)
            return
        total = 0
        for tf in trace_files:
            pid = self._pid_from_filename(tf)
            total += self._parse_file(tf, pid)
        self.sink.record(
            "collector.strace_completed", source="strace",
            message="strace parsing complete",
            data={"files": len(trace_files), "events": total},
        )
        super().finish(launch_result)

    @staticmethod
    def _pid_from_filename(path: Path) -> Optional[int]:
        suffix = path.name.rsplit(".", 1)[-1]
        return int(suffix) if suffix.isdigit() else None

    def _parse_file(self, path: Path, pid: Optional[int]) -> int:
        count = 0
        try:
            lines = path.read_text(encoding="utf-8", errors="replace").splitlines()
        except OSError as exc:
            self.status.errors.append(f"could not read {path}: {exc}")
            return 0
        for line in lines:
            m = _LINE_RE.match(line)
            if not m:
                continue
            call = m.group("call")
            mapping = _SYSCALL_EVENTS.get(call)
            if mapping is None:
                continue
            event_type, severity = mapping
            args = m.group("args")
            line_pid = int(m.group("pid")) if m.group("pid") else pid
            self._emit(event_type, severity, call, args, line_pid)
            count += 1
        return count

    def _emit(self, event_type: str, severity: str, call: str, args: str, pid: Optional[int]) -> None:
        process: Dict[str, object] = {"syscall": call}
        network: Optional[Dict[str, object]] = None
        file_info: Optional[Dict[str, object]] = None

        if call in ("execve", "execveat"):
            argv = self._parse_execve_argv(args)
            if argv:
                process["argv"] = argv
        elif call in ("open", "openat", "creat", "unlink", "unlinkat", "chmod", "chown"):
            sm = _FIRST_STR_ARG_RE.search(args)
            # openat's first string is often the dirfd symbol; take the last path-looking string
            paths = _FIRST_STR_ARG_RE.findall(args)
            path_val = paths[-1] if paths else (sm.group(1) if sm else None)
            if path_val:
                file_info = {"path": path_val}
        elif call in ("connect", "sendto"):
            network = self._parse_connect(args)

        self.sink.record(
            event_type, severity=severity, source="strace",
            message=f"strace observed {call}()",
            pid=pid, process=process, network=network, file=file_info,
        )

    @staticmethod
    def _parse_execve_argv(args: str) -> Optional[List[str]]:
        # execve("/path", ["a", "b"], 0x...) -> capture the bracketed list
        start = args.find("[")
        end = args.find("]", start)
        if start == -1 or end == -1:
            return None
        inner = args[start + 1 : end]
        return [m.group(1) for m in _FIRST_STR_ARG_RE.finditer(inner)] or None

    @staticmethod
    def _parse_connect(args: str) -> Optional[Dict[str, object]]:
        ip_m = _CONNECT_ADDR_RE.search(args)
        port_m = _CONNECT_PORT_RE.search(args)
        ip6_m = _CONNECT6_ADDR_RE.search(args)
        info: Dict[str, object] = {}
        if ip_m:
            info["destinationIp"] = ip_m.group("ip")
        elif ip6_m:
            info["destinationIp"] = ip6_m.group("ip")
        if port_m:
            info["destinationPort"] = int(port_m.group("port"))
        return info or None
