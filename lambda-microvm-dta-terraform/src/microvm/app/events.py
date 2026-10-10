"""Normalized event model for the v0.2 DTA supervisor.

Collectors observe the target from *outside* the target process and emit
normalized events. Events are written to ``events.jsonl`` (one JSON object per
line) and consumed by the rule engine. This module deliberately uses only the
standard library.
"""
from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Dict, Iterable, List, Optional
import json
import threading

SEVERITY_ORDER = {
    "none": 0,
    "informational": 0,
    "low": 1,
    "medium": 2,
    "high": 3,
    "critical": 4,
}


def utc_now() -> str:
    return datetime.now(timezone.utc).isoformat().replace("+00:00", "Z")


def severity_gte(left: str, right: str) -> bool:
    return SEVERITY_ORDER.get(left, -1) >= SEVERITY_ORDER.get(right, -1)


def max_severity(severities: Iterable[str]) -> str:
    best = "none"
    for item in severities:
        if severity_gte(item, best):
            best = item
    return best


@dataclass
class Event:
    """A single normalized observation about the target.

    Only non-empty optional sections are serialized so ``events.jsonl`` stays
    compact and stable.
    """

    type: str
    severity: str = "none"
    source: str = "supervisor"
    message: str = ""
    timestamp: str = field(default_factory=utc_now)
    pid: Optional[int] = None
    process: Optional[Dict[str, Any]] = None
    file: Optional[Dict[str, Any]] = None
    network: Optional[Dict[str, Any]] = None
    canary: Optional[Dict[str, Any]] = None
    data: Dict[str, Any] = field(default_factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        out: Dict[str, Any] = {
            "timestamp": self.timestamp,
            "type": self.type,
            "severity": self.severity,
            "source": self.source,
        }
        if self.pid is not None:
            out["pid"] = self.pid
        if self.process:
            out["process"] = self.process
        if self.file:
            out["file"] = self.file
        if self.network:
            out["network"] = self.network
        if self.canary:
            out["canary"] = self.canary
        if self.data:
            out["data"] = self.data
        if self.message:
            out["message"] = self.message
        return out


class EventSink:
    """Thread-safe collector for normalized events.

    Collectors may run concurrently (e.g. the process poller while strace
    writes), so appends are guarded by a lock. Events are buffered in memory and
    flushed to ``events.jsonl`` once via :meth:`write_jsonl`.
    """

    def __init__(self) -> None:
        self._lock = threading.Lock()
        self._events: List[Event] = []

    def emit(self, event: Event) -> None:
        with self._lock:
            self._events.append(event)

    def record(self, type: str, severity: str = "none", source: str = "supervisor", message: str = "", **sections: Any) -> Event:
        """Convenience for building and emitting an event.

        Known section kwargs (``pid``, ``process``, ``file``, ``network``,
        ``canary``) map onto the event; anything else lands in ``data``.
        """
        known = {k: sections.pop(k) for k in ("pid", "process", "file", "network", "canary") if k in sections}
        event = Event(type=type, severity=severity, source=source, message=message, data=dict(sections), **known)
        self.emit(event)
        return event

    def events(self) -> List[Event]:
        with self._lock:
            return list(self._events)

    def sorted_events(self) -> List[Event]:
        return sorted(self.events(), key=lambda e: e.timestamp)

    def write_jsonl(self, path: str | Path) -> Path:
        out = Path(path)
        out.parent.mkdir(parents=True, exist_ok=True)
        lines = [json.dumps(e.to_dict(), sort_keys=True) for e in self.sorted_events()]
        out.write_text("\n".join(lines) + ("\n" if lines else ""), encoding="utf-8")
        return out
