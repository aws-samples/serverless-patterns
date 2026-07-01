"""report.json v0.2.0 builder.

Assembles the deterministic CI report from the launch result, collected events,
collector statuses, rule evaluation, and policy result.
"""
from __future__ import annotations

from typing import Any, Dict, List, Optional
import os
import platform
import uuid

from .events import Event
from .rules import Evaluation, PolicyResult

SCHEMA_VERSION = "0.2.0"


def build_report(
    *,
    correlation_id: Optional[str],
    commit_sha: Optional[str],
    mode: str,
    region: Optional[str],
    microvm_id: Optional[str],
    image_identifier: Optional[str],
    target: Dict[str, Any],
    events: List[Event],
    collector_statuses: List[Dict[str, Any]],
    evaluation: Evaluation,
    policy_result: PolicyResult,
    policy_config: Dict[str, Any],
    include_evidence: bool = True,
) -> Dict[str, Any]:
    collector_error_count = sum(1 for c in collector_statuses if c.get("status") == "failed")
    summary = {
        "status": policy_result.status,
        "verdict": evaluation.verdict,
        "maxSeverity": evaluation.max_severity,
        "eventCount": len(events),
        "matchedRuleCount": len(evaluation.matches),
        "collectorErrorCount": collector_error_count,
    }
    report: Dict[str, Any] = {
        "schemaVersion": SCHEMA_VERSION,
        "project": "aws-lambda-microvm-dta-sample",
        "correlationId": correlation_id or f"local-{uuid.uuid4()}",
        "commitSha": commit_sha or os.environ.get("GITHUB_SHA") or "unknown",
        "target": target,
        "environment": {
            "mode": mode,
            "region": region or "",
            "microvmId": microvm_id or "local",
            "imageIdentifier": image_identifier or "local",
            "python": platform.python_version(),
            "platform": platform.platform(),
        },
        "summary": summary,
        "collectors": collector_statuses,
        "matchedRules": [m.to_dict() for m in evaluation.matches],
        "evidence": [e.to_dict() for e in events] if include_evidence else [],
        "policy": {
            "failOnSeverity": policy_config.get("failOnSeverity", "high"),
            "failOnPolicyViolation": policy_config.get("failOnPolicyViolation", True),
            "failClosed": policy_config.get("failClosed", True),
            "reasons": policy_result.reasons,
        },
    }
    return report
