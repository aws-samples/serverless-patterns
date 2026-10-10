"""Collector interface shared by all v0.2 collectors."""
from __future__ import annotations

from dataclasses import dataclass, field
from typing import List, Optional

from ..events import EventSink
from ..workspace import Workspace


@dataclass
class CollectorStatus:
    name: str
    enabled: bool
    status: str = "pending"  # pending | running | completed | failed | skipped
    errors: List[str] = field(default_factory=list)

    def to_dict(self) -> dict:
        return {
            "name": self.name,
            "enabled": self.enabled,
            "status": self.status,
            "errors": list(self.errors),
        }


class Collector:
    """Lifecycle: ``setup`` (pre-launch) → target runs → ``finish`` (post-exit).

    A collector that needs to observe a live PID implements
    :meth:`on_target_started`, which the supervisor calls from the launcher's
    ``on_started`` hook. Concurrency-heavy collectors (pollers) spawn their own
    thread in ``on_target_started`` and join it in ``finish``.
    """

    name = "collector"

    def __init__(self, sink: EventSink, workspace: Workspace) -> None:
        self.sink = sink
        self.workspace = workspace
        self.status = CollectorStatus(name=self.name, enabled=True)

    # --- lifecycle hooks (override as needed) ---
    def setup(self) -> None:  # before target launch
        self.status.status = "running"

    def on_target_started(self, pid: int) -> None:  # target is live
        pass

    def finish(self, launch_result) -> None:  # after target exit
        if self.status.status == "running":
            self.status.status = "completed"

    # --- helpers ---
    def fail(self, message: str) -> None:
        self.status.status = "failed"
        self.status.errors.append(message)

    @property
    def strace_wrapper(self) -> Optional[List[str]]:
        """Collectors that need to wrap the target argv (strace) return one here."""
        return None
