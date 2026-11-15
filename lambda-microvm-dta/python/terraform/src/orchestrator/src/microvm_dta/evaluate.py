from __future__ import annotations

from typing import Any, Dict, List, Tuple

SEVERITY_ORDER = {
    "none": 0,
    "informational": 0,
    "low": 1,
    "medium": 2,
    "high": 3,
    "critical": 4,
}


def severity_gte(left: str, right: str) -> bool:
    return SEVERITY_ORDER.get(left, -1) >= SEVERITY_ORDER.get(right, -1)


def evaluate_report(
    report: Dict[str, Any],
    *,
    fail_on_severity: str = "high",
    fail_on_policy_violation: bool = True,
) -> Tuple[bool, List[str]]:
    """Re-apply CI policy to a v0.2 report. Returns (ok, reasons).

    The supervisor already computed ``summary.status``; this lets CI re-evaluate
    independently (e.g. with a stricter threshold) and surface human-readable
    reasons. An ``error`` status always fails.
    """
    reasons: List[str] = []
    summary = report.get("summary") or {}

    status = str(summary.get("status", "failed"))
    if status == "error":
        reasons.append("analysis status is 'error'")
        return (False, reasons)

    verdict = str(summary.get("verdict", "unknown"))
    max_severity = str(summary.get("maxSeverity", "none"))

    if severity_gte(max_severity, fail_on_severity):
        reasons.append(f"max severity {max_severity!r} is >= threshold {fail_on_severity!r}")

    if fail_on_policy_violation and verdict == "policy_violation":
        reasons.append("verdict is 'policy_violation'")

    if status == "failed":
        # Honor the supervisor's own decision (e.g. fail-closed on collector error)
        # even if the threshold check above didn't trip.
        for reason in (report.get("policy") or {}).get("reasons", []):
            if reason not in reasons:
                reasons.append(str(reason))
        if not reasons:
            reasons.append("report summary status is 'failed'")

    return (len(reasons) == 0, reasons)
