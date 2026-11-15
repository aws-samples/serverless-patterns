"""Optional VPC Flow Logs importer (AWS-side network-flow metadata).

This is post-processing evidence, not a primary detector. It queries a
CloudWatch Logs group for VPC Flow Log records within the analysis time window
and attaches a metadata-only summary to a v0.2 report under
``report['flowLogs']``. Flow Logs carry 5-tuple + bytes/packets metadata only —
no payload and no DNS hostname attribution.

It shells out to the AWS CLI (like the rest of the orchestrator) and degrades
gracefully: any failure leaves the report untouched and returns an empty result,
so local mode is never affected.
"""
from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime, timezone
from typing import Any, Dict, List, Optional
import json

from .aws_cli import AwsCli, AwsCliError


@dataclass
class FlowLogResult:
    available: bool
    recordCount: int = 0
    flows: List[Dict[str, Any]] = field(default_factory=list)
    note: str = ""

    def to_dict(self) -> Dict[str, Any]:
        return {
            "available": self.available,
            "recordCount": self.recordCount,
            "flows": self.flows,
            "note": self.note,
            "limitation": "metadata only (5-tuple + bytes/packets); no payload; no DNS hostname attribution",
        }


def _to_epoch_ms(iso_ts: str) -> Optional[int]:
    if not iso_ts:
        return None
    try:
        cleaned = iso_ts.replace("Z", "+00:00")
        dt = datetime.fromisoformat(cleaned)
        if dt.tzinfo is None:
            dt = dt.replace(tzinfo=timezone.utc)
        return int(dt.timestamp() * 1000)
    except ValueError:
        return None


def fetch_flow_logs(
    aws: AwsCli,
    *,
    log_group: str,
    start_iso: str,
    end_iso: str,
    eni_id: Optional[str] = None,
    limit: int = 200,
) -> FlowLogResult:
    """Best-effort fetch of flow-log records in [start, end]. Never raises."""
    start_ms = _to_epoch_ms(start_iso)
    end_ms = _to_epoch_ms(end_iso)
    if start_ms is None or end_ms is None:
        return FlowLogResult(available=False, note="missing/invalid analysis time window")

    args = [
        "logs", "filter-log-events",
        "--log-group-name", log_group,
        "--start-time", str(start_ms),
        "--end-time", str(end_ms + 60_000),  # flow logs lag; widen the tail
        "--limit", str(limit),
    ]
    if eni_id:
        args.extend(["--filter-pattern", eni_id])
    try:
        resp = aws.run(args)
    except AwsCliError as exc:
        return FlowLogResult(available=False, note=f"flow log query failed: {exc}")
    if not isinstance(resp, dict):
        return FlowLogResult(available=False, note="unexpected flow log response")

    flows: List[Dict[str, Any]] = []
    for event in resp.get("events", []):
        parsed = _parse_flow_record(str(event.get("message", "")))
        if parsed:
            flows.append(parsed)
    return FlowLogResult(available=True, recordCount=len(flows), flows=flows,
                         note="flow log metadata correlated by time window" + (f" and ENI {eni_id}" if eni_id else ""))


def _parse_flow_record(message: str) -> Optional[Dict[str, Any]]:
    """Parse the default VPC Flow Logs v2 format.

    version account-id interface-id srcaddr dstaddr srcport dstport protocol
    packets bytes start end action log-status
    """
    cols = message.split()
    if len(cols) < 14:
        return None
    try:
        return {
            "interfaceId": cols[2],
            "srcAddr": cols[3],
            "dstAddr": cols[4],
            "srcPort": int(cols[5]) if cols[5].isdigit() else None,
            "dstPort": int(cols[6]) if cols[6].isdigit() else None,
            "protocol": cols[7],
            "packets": int(cols[8]) if cols[8].isdigit() else None,
            "bytes": int(cols[9]) if cols[9].isdigit() else None,
            "action": cols[12],
        }
    except (ValueError, IndexError):
        return None


def attach_flow_logs(report: Dict[str, Any], result: FlowLogResult) -> Dict[str, Any]:
    """Attach flow-log metadata to a report (returns the same dict)."""
    report["flowLogs"] = result.to_dict()
    return report
