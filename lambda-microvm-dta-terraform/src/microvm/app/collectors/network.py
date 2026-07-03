"""Basic network collector using ``/proc/net`` snapshots.

Polls ``/proc/net/{tcp,tcp6,udp,udp6}`` while the target runs and reports
observed connections. This is host-metadata evidence — it sees sockets owned by
the network namespace, not just the target — so it is corroborating rather than
authoritative. The strace collector provides per-process ``connect``/``socket``
evidence, and (in AWS mode) VPC Flow Logs add the AWS-side view.
"""
from __future__ import annotations

from pathlib import Path
from typing import Optional, Set, Tuple
import threading
import time

from .base import Collector

_PROC_NET_FILES = {
    "tcp": Path("/proc/net/tcp"),
    "tcp6": Path("/proc/net/tcp6"),
    "udp": Path("/proc/net/udp"),
    "udp6": Path("/proc/net/udp6"),
}

# TCP state 01 == ESTABLISHED in /proc/net/tcp.
_TCP_ESTABLISHED = "01"


def _parse_hex_ipv4(hexip: str) -> str:
    # /proc stores the address little-endian.
    b = bytes.fromhex(hexip)
    return ".".join(str(x) for x in reversed(b))


def _parse_addr(field: str, ipv6: bool) -> Tuple[str, int]:
    addr, _, port = field.partition(":")
    port_num = int(port, 16) if port else 0
    if ipv6:
        return (addr.lower(), port_num)  # keep raw hex for v6 to stay dependency-light
    return (_parse_hex_ipv4(addr), port_num)


class NetworkCollector(Collector):
    name = "network"

    def __init__(self, sink, workspace, poll_interval: float = 0.25) -> None:
        super().__init__(sink, workspace)
        self._poll_interval = poll_interval
        self._stop = threading.Event()
        self._thread: Optional[threading.Thread] = None
        self._seen: Set[Tuple[str, str, int]] = set()
        self._observed_any = False

    def on_target_started(self, pid: int) -> None:
        if not any(p.exists() for p in _PROC_NET_FILES.values()):
            return  # not Linux / no procfs: stay silent, finish() notes no egress
        self._thread = threading.Thread(target=self._poll_loop, daemon=True)
        self._thread.start()

    def _poll_loop(self) -> None:
        while not self._stop.is_set():
            for proto, path in _PROC_NET_FILES.items():
                self._scan(proto, path)
            time.sleep(self._poll_interval)

    def _scan(self, proto: str, path: Path) -> None:
        try:
            lines = path.read_text(encoding="utf-8", errors="replace").splitlines()[1:]
        except (FileNotFoundError, PermissionError, OSError):
            return
        ipv6 = proto.endswith("6")
        for line in lines:
            cols = line.split()
            if len(cols) < 4:
                continue
            rem_ip, rem_port = _parse_addr(cols[2], ipv6)
            state = cols[3]
            if rem_port == 0:
                continue  # listening / unconnected
            if proto.startswith("tcp") and state != _TCP_ESTABLISHED:
                continue
            key = (proto, rem_ip, rem_port)
            if key in self._seen:
                continue
            self._seen.add(key)
            self._observed_any = True
            self.sink.record(
                "network.procnet_connection_observed", severity="low", source="network",
                message="Observed an active connection via /proc/net",
                network={"protocol": proto, "destinationIp": rem_ip, "destinationPort": rem_port},
            )

    def finish(self, launch_result) -> None:
        self._stop.set()
        if self._thread is not None:
            self._thread.join(timeout=2)
        if not self._observed_any:
            self.sink.record(
                "network.no_egress_observed", severity="none", source="network",
                message="No outbound connections observed via /proc/net",
            )
        super().finish(launch_result)
