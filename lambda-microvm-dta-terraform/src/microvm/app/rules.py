"""Simple, explainable rule engine for v0.2.

The engine matches normalized events against declarative rules and aggregates a
verdict + max severity. It deliberately makes no high-confidence malware
classification: the verdict vocabulary is clean / suspicious / policy_violation
/ unknown / error — never ``malware``.
"""
from __future__ import annotations

from dataclasses import dataclass, field
from pathlib import Path
from typing import Any, Dict, List, Optional
import json

from .events import Event, SEVERITY_ORDER, max_severity, severity_gte

VERDICTS = ("clean", "suspicious", "policy_violation", "unknown", "error")
# Ranking for aggregating the overall verdict (higher wins).
_VERDICT_RANK = {"clean": 0, "unknown": 1, "suspicious": 2, "policy_violation": 3, "error": 4}


class RuleError(ValueError):
    pass


@dataclass(frozen=True)
class Rule:
    id: str
    name: str
    severity: str
    verdict: str
    event_types: List[str]
    argv_contains_any: List[str] = field(default_factory=list)

    def matches(self, event: Event) -> bool:
        if event.type not in self.event_types:
            return False
        if self.argv_contains_any:
            argv = (event.process or {}).get("argv") or []
            if not isinstance(argv, list):
                return False
            joined = [str(a) for a in argv]
            if not any(tok in joined for tok in self.argv_contains_any):
                return False
        return True


@dataclass
class RuleMatch:
    rule_id: str
    name: str
    severity: str
    verdict: str
    event_type: str
    event_timestamp: str
    message: str

    def to_dict(self) -> Dict[str, Any]:
        return {
            "ruleId": self.rule_id,
            "name": self.name,
            "severity": self.severity,
            "verdict": self.verdict,
            "eventType": self.event_type,
            "eventTimestamp": self.event_timestamp,
            "message": self.message,
        }


@dataclass
class Evaluation:
    matches: List[RuleMatch]
    verdict: str
    max_severity: str

    @property
    def has_policy_violation(self) -> bool:
        return any(m.verdict == "policy_violation" for m in self.matches)


def parse_rules(data: Any) -> List[Rule]:
    raw_rules = data.get("rules") if isinstance(data, dict) else data
    if not isinstance(raw_rules, list):
        raise RuleError("rules file must contain a 'rules' list")
    rules: List[Rule] = []
    for item in raw_rules:
        if not isinstance(item, dict):
            raise RuleError("each rule must be a mapping")
        when = item.get("when") or {}
        event_types: List[str] = []
        if "eventType" in when:
            event_types = [str(when["eventType"])]
        elif "eventTypeAny" in when:
            any_list = when["eventTypeAny"]
            if not isinstance(any_list, list):
                raise RuleError(f"rule {item.get('id')}: eventTypeAny must be a list")
            event_types = [str(x) for x in any_list]
        else:
            raise RuleError(f"rule {item.get('id')}: 'when' needs eventType or eventTypeAny")

        verdict = str(item.get("verdict", "unknown"))
        if verdict not in VERDICTS:
            raise RuleError(f"rule {item.get('id')}: invalid verdict {verdict!r}")
        severity = str(item.get("severity", "low"))
        if severity not in SEVERITY_ORDER:
            raise RuleError(f"rule {item.get('id')}: invalid severity {severity!r}")

        argv_contains = when.get("argvContainsAny") or []
        if not isinstance(argv_contains, list):
            raise RuleError(f"rule {item.get('id')}: argvContainsAny must be a list")

        rules.append(
            Rule(
                id=str(item.get("id", f"R{len(rules)+1:03d}")),
                name=str(item.get("name", "")),
                severity=severity,
                verdict=verdict,
                event_types=event_types,
                argv_contains_any=[str(x) for x in argv_contains],
            )
        )
    return rules


def load_rules(path: str | Path) -> List[Rule]:
    p = Path(path)
    text = p.read_text(encoding="utf-8")
    if p.suffix.lower() == ".json":
        data = json.loads(text)
    else:
        try:
            import yaml  # type: ignore

            data = yaml.safe_load(text)
        except ModuleNotFoundError:
            from .target_config import _parse_limited_yaml

            data = _parse_limited_yaml(text)
    return parse_rules(data)


def evaluate_events(events: List[Event], rules: List[Rule]) -> Evaluation:
    matches: List[RuleMatch] = []
    for event in events:
        for rule in rules:
            if rule.matches(event):
                matches.append(
                    RuleMatch(
                        rule_id=rule.id,
                        name=rule.name,
                        severity=rule.severity,
                        verdict=rule.verdict,
                        event_type=event.type,
                        event_timestamp=event.timestamp,
                        message=event.message,
                    )
                )
    if matches:
        verdict = max((m.verdict for m in matches), key=lambda v: _VERDICT_RANK.get(v, 0))
        sev = max_severity(m.severity for m in matches)
    else:
        verdict = "clean"
        sev = "none"
    return Evaluation(matches=matches, verdict=verdict, max_severity=sev)


@dataclass
class PolicyResult:
    status: str  # passed | failed | error
    reasons: List[str] = field(default_factory=list)


def apply_policy(
    evaluation: Evaluation,
    *,
    fail_on_severity: str,
    fail_on_policy_violation: bool,
    fail_closed: bool,
    collector_errors: int,
    target_error: bool = False,
) -> PolicyResult:
    reasons: List[str] = []
    status = "passed"

    if target_error:
        return PolicyResult(status="error", reasons=["target failed to execute"])

    if fail_on_policy_violation and evaluation.has_policy_violation:
        reasons.append("policy_violation rule matched")
    if severity_gte(evaluation.max_severity, fail_on_severity):
        reasons.append(f"max severity {evaluation.max_severity!r} >= threshold {fail_on_severity!r}")
    if fail_closed and collector_errors > 0:
        reasons.append(f"{collector_errors} collector(s) failed and failClosed is true")

    if reasons:
        status = "failed"
    return PolicyResult(status=status, reasons=reasons)
