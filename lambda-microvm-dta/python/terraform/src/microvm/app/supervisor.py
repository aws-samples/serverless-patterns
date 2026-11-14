"""Sandbox supervisor: orchestrates a single DTA analysis run.

Flow:
  1. prepare workspace, materialize the (untrusted) target
  2. construct enabled collectors; canary presents fake assets
  3. start collectors (pre-launch snapshots / arming)
  4. launch the target as a child, optionally wrapped by strace; collectors
     observe via the on_started hook
  5. stop collectors, normalize events to events.jsonl
  6. evaluate rules + policy, build report.json and run-metadata.json

The target never reports on itself — all evidence comes from the collectors.
"""
from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import Any, Dict, List, Optional
import json

from .events import EventSink, utc_now
from .launcher import build_child_env, launch_target
from .report import build_report
from .rules import apply_policy, evaluate_events, load_rules
from .target_config import AnalysisConfig
from .workspace import materialize_target, prepare_workspace

from .collectors.process import ProcessCollector
from .collectors.filesystem import FilesystemCollector
from .collectors.canary import CanaryCollector
from .collectors.network import NetworkCollector
from .collectors.strace_collector import StraceCollector


@dataclass
class AnalysisResult:
    report: Dict[str, Any]
    events_path: Path
    report_path: Path
    metadata_path: Path


def run_analysis(
    config: AnalysisConfig,
    *,
    root: str | Path,
    rules_file: str | Path,
    source_base: str | Path,
    correlation_id: Optional[str] = None,
    commit_sha: Optional[str] = None,
    mode: str = "local",
    region: Optional[str] = None,
    microvm_id: Optional[str] = None,
    image_identifier: Optional[str] = None,
) -> AnalysisResult:
    ws = prepare_workspace(root)
    sink = EventSink()

    # Build collectors per config. Canary is constructed first so its env can be
    # merged into the target environment.
    canary: Optional[CanaryCollector] = CanaryCollector(sink, ws) if config.collectors.canary else None
    collectors: List[Any] = []
    if config.collectors.process:
        collectors.append(ProcessCollector(sink, ws))
    if config.collectors.filesystem:
        collectors.append(FilesystemCollector(sink, ws))
    if canary is not None:
        collectors.append(canary)
    if config.collectors.network_procnet:
        collectors.append(NetworkCollector(sink, ws))
    strace: Optional[StraceCollector] = None
    if config.collectors.strace:
        strace = StraceCollector(sink, ws, fail_closed=config.policy.fail_closed)
        collectors.append(strace)

    target_error = False
    target_meta: Dict[str, Any] = {
        "type": config.target.type,
        "argv": config.target.argv,
    }

    try:
        materialize_target(config.target, ws, source_base=Path(source_base))
    except Exception as exc:  # materialization failure is a target error
        target_error = True
        sink.record("target.materialization_failed", severity="medium", source="supervisor",
                    message=f"Could not materialize target: {exc}")

    # Pre-launch setup for all collectors.
    for c in collectors:
        try:
            c.setup()
        except Exception as exc:  # a collector setup failure must not crash the run
            c.fail(f"setup error: {exc}")

    launch_result = None
    if not target_error:
        canary_env = canary.canary_env if canary is not None else {}
        env = build_child_env(config.target.environment, canary_env)
        cwd = ws.workspace
        if config.target.working_directory:
            wd = Path(config.target.working_directory)
            cwd = wd if wd.is_absolute() else (ws.root / config.target.working_directory)
            cwd.mkdir(parents=True, exist_ok=True)

        wrapper = strace.strace_wrapper if (strace is not None and strace.available) else None

        def on_started(pid: int) -> None:
            for c in collectors:
                try:
                    c.on_target_started(pid)
                except Exception as exc:
                    c.fail(f"on_target_started error: {exc}")

        launch_result = launch_target(
            config.target.argv,
            cwd=cwd,
            env=env,
            timeout_seconds=config.target.timeout_seconds,
            stdout_path=ws.artifacts / "stdout.log",
            stderr_path=ws.artifacts / "stderr.log",
            wrapper=wrapper,
            on_started=on_started,
        )
        target_meta.update({
            "startedAt": launch_result.started_at,
            "endedAt": launch_result.ended_at,
            "exitCode": launch_result.exit_code,
            "timedOut": launch_result.timed_out,
            "durationSeconds": launch_result.duration_seconds,
        })
        if launch_result.error:
            target_error = True
            sink.record("target.launch_failed", severity="medium", source="supervisor",
                        message=launch_result.error)

    # Post-execution finish. strace must finish first so its syscall events are
    # in the sink before the canary collector cross-references them for
    # high-confidence read detection.
    finish_order = sorted(
        collectors,
        key=lambda c: 0 if isinstance(c, StraceCollector) else (2 if isinstance(c, CanaryCollector) else 1),
    )
    for c in finish_order:
        try:
            c.finish(launch_result)
        except Exception as exc:
            c.fail(f"finish error: {exc}")

    events = sink.sorted_events()
    events_path = sink.write_jsonl(ws.root / "events.jsonl")

    rules = load_rules(rules_file)
    evaluation = evaluate_events(events, rules)
    collector_statuses = [c.status.to_dict() for c in collectors]
    collector_errors = sum(1 for s in collector_statuses if s["status"] == "failed")

    policy_result = apply_policy(
        evaluation,
        fail_on_severity=config.policy.fail_on_severity,
        fail_on_policy_violation=config.policy.fail_on_policy_violation,
        fail_closed=config.policy.fail_closed,
        collector_errors=collector_errors,
        target_error=target_error,
    )

    report = build_report(
        correlation_id=correlation_id,
        commit_sha=commit_sha,
        mode=mode,
        region=region,
        microvm_id=microvm_id,
        image_identifier=image_identifier,
        target=target_meta,
        events=events,
        collector_statuses=collector_statuses,
        evaluation=evaluation,
        policy_result=policy_result,
        policy_config={
            "failOnSeverity": config.policy.fail_on_severity,
            "failOnPolicyViolation": config.policy.fail_on_policy_violation,
            "failClosed": config.policy.fail_closed,
        },
    )

    report_path = ws.root / "report.json"
    report_path.write_text(json.dumps(report, indent=2, sort_keys=True), encoding="utf-8")

    metadata = {
        "correlationId": report["correlationId"],
        "commitSha": report["commitSha"],
        "mode": mode,
        "region": region or "",
        "microvmId": microvm_id or "local",
        "imageIdentifier": image_identifier or "local",
        "generatedAt": utc_now(),
        "artifacts": {
            "report": "report.json",
            "events": "events.jsonl",
            "stdout": "artifacts/stdout.log",
            "stderr": "artifacts/stderr.log",
            "straceDir": "artifacts/strace",
        },
        "cloudwatch": {},
    }
    metadata_path = ws.root / "run-metadata.json"
    metadata_path.write_text(json.dumps(metadata, indent=2, sort_keys=True), encoding="utf-8")

    return AnalysisResult(
        report=report,
        events_path=events_path,
        report_path=report_path,
        metadata_path=metadata_path,
    )
