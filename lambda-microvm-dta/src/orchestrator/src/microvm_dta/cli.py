from __future__ import annotations

from pathlib import Path
from typing import Any, Dict, List, Optional
import argparse
import json
import os
import sys
import time

from .aws_cli import AwsCli, AwsCliError
from .evaluate import evaluate_report
from .http_client import request_json
from .local import run_local_analysis
from .packaging import package_microvm

DEFAULT_INGRESS = "arn:aws:lambda:{region}:aws:network-connector:aws-network-connector:ALL_INGRESS"
DEFAULT_INTERNET_EGRESS = "arn:aws:lambda:{region}:aws:network-connector:aws-network-connector:INTERNET_EGRESS"


def _print_json(data: Dict[str, Any]) -> None:
    print(json.dumps(data, indent=2, sort_keys=True))


# --------------------------------------------------------------------------- #
# Safety guards
# --------------------------------------------------------------------------- #
def _require_aws_mode(args: argparse.Namespace) -> None:
    """AWS-mode commands must be explicitly opted into.

    Requires DTA_ALLOW_AWS_MODE=true in the environment and --confirm-sandbox-account
    on the command line so a real, billable MicroVM run is never a surprise.
    """
    if getattr(args, "print_only", False):
        return  # print-only never touches AWS
    if os.environ.get("DTA_ALLOW_AWS_MODE", "").lower() != "true":
        raise SystemExit("AWS mode is disabled. Set DTA_ALLOW_AWS_MODE=true to enable real MicroVM operations.")
    if not getattr(args, "confirm_sandbox_account", False):
        raise SystemExit("Refusing to run AWS mode without --confirm-sandbox-account (use a dedicated sandbox account).")


# --------------------------------------------------------------------------- #
# Local commands
# --------------------------------------------------------------------------- #
def cmd_package(args: argparse.Namespace) -> int:
    out = package_microvm(args.source_dir, args.output)
    print(str(out))
    return 0


def cmd_dry_run(args: argparse.Namespace) -> int:
    report = run_local_analysis(
        target_config=args.target_config,
        root=args.workspace,
        rules_file=args.rules_file,
        correlation_id=args.correlation_id,
        commit_sha=args.commit_sha,
        allow_shell_strings=args.allow_shell_strings,
    )
    _print_json(report["summary"])
    return 0 if report["summary"]["status"] == "passed" else 1


def cmd_evaluate(args: argparse.Namespace) -> int:
    report = json.loads(Path(args.report).read_text(encoding="utf-8"))
    ok, reasons = evaluate_report(
        report,
        fail_on_severity=args.fail_on_severity,
        fail_on_policy_violation=args.fail_on_policy_violation,
    )
    if ok:
        print("policy: passed")
        return 0
    print("policy: failed")
    for reason in reasons:
        print(f"- {reason}")
    return 1


# --------------------------------------------------------------------------- #
# AWS helpers
# --------------------------------------------------------------------------- #
def _aws(args: argparse.Namespace) -> AwsCli:
    return AwsCli(profile=args.profile, region=args.region, dry_print=getattr(args, "print_only", False))


def _looks_like_not_found(error: AwsCliError) -> bool:
    text = str(error).lower()
    # "Invalid ARN format" appears when an image name is passed as an identifier
    # to a not-yet-existing image; treat it as "absent → create" too.
    markers = ("resourcenotfound", "notfound", "does not exist", "not found", "invalid arn format")
    return any(marker in text for marker in markers)


def _region_of(args: argparse.Namespace) -> str:
    return args.region or os.environ.get("AWS_REGION") or os.environ.get("AWS_DEFAULT_REGION") or "us-east-1"


def _account_id(aws: AwsCli) -> Optional[str]:
    try:
        resp = aws.run(["sts", "get-caller-identity"])
        if isinstance(resp, dict):
            return str(resp.get("Account")) or None
    except AwsCliError:
        return None
    return None


def _image_arn(aws: AwsCli, args: argparse.Namespace) -> Optional[str]:
    """Build a MicroVM image ARN from name + region + account for get/update.

    The control-plane get/update operations require a full ARN as the
    --image-identifier; create takes a bare --name.
    """
    if args.image_name.startswith("arn:"):
        return args.image_name
    account = _account_id(aws)
    if not account:
        return None
    return f"arn:aws:lambda:{_region_of(args)}:{account}:microvm-image:{args.image_name}"


def cmd_build_image(args: argparse.Namespace) -> int:
    aws = _aws(args)
    image_arn = _image_arn(aws, args)
    image_exists = False
    if image_arn:
        try:
            aws.microvms(["get-microvm-image", "--image-identifier", image_arn])
            image_exists = True
        except AwsCliError as exc:
            if not _looks_like_not_found(exc):
                raise
            image_exists = False
    common = [
        "--code-artifact", f"uri={args.artifact_uri}",
        "--base-image-arn", args.base_image_arn,
        "--build-role-arn", args.build_role_arn,
    ]
    if args.additional_os_capabilities:
        common.extend(["--additional-os-capabilities", json.dumps(args.additional_os_capabilities.split(","))])
    if args.description:
        common.extend(["--description", args.description])
    if image_exists:
        resp = aws.microvms(["update-microvm-image", "--image-identifier", image_arn, *common])
    else:
        resp = aws.microvms(["create-microvm-image", "--name", args.image_name, *common])
    _print_json(resp if isinstance(resp, dict) else {"output": resp})
    return 0


def cmd_wait_image(args: argparse.Namespace) -> int:
    aws = _aws(args)
    deadline = time.monotonic() + args.timeout_seconds
    last: Dict[str, Any] = {}
    while time.monotonic() < deadline:
        resp = aws.microvms(["get-microvm-image", "--image-identifier", args.image_identifier])
        if not isinstance(resp, dict):
            raise RuntimeError("Unexpected non-JSON response")
        last = resp
        state = str(resp.get("state"))
        # The GA control plane reports image readiness via `state`
        # (CREATING -> CREATED, UPDATING -> UPDATED). A versionState field is
        # optional; when present it must also be terminal-success, but its
        # absence on a CREATED/UPDATED/ACTIVE image means ready.
        raw_vs = resp.get("versionState")
        if raw_vs is None:
            raw_vs = resp.get("latestVersionState")
        version_state = "" if raw_vs is None else str(raw_vs)
        print(f"image state={state} versionState={version_state or 'n/a'}", file=sys.stderr)
        terminal_success = {"CREATED", "UPDATED", "ACTIVE"}
        if state in terminal_success and version_state in {"", "SUCCESSFUL", "ACTIVE"}:
            _print_json(resp)
            return 0
        if state in {"CREATION_FAILED", "UPDATE_FAILED", "DELETED", "DELETION_FAILED"} or version_state == "FAILED":
            _print_json(resp)
            return 1
        time.sleep(args.poll_seconds)
    print("Timed out waiting for image readiness", file=sys.stderr)
    _print_json(last)
    return 1


def _wait_microvm_running(aws: AwsCli, microvm_id: str, timeout_seconds: int, poll_seconds: int) -> Dict[str, Any]:
    deadline = time.monotonic() + timeout_seconds
    last: Dict[str, Any] = {}
    while time.monotonic() < deadline:
        resp = aws.microvms(["get-microvm", "--microvm-identifier", microvm_id])
        if not isinstance(resp, dict):
            raise RuntimeError("Unexpected non-JSON response")
        last = resp
        state = str(resp.get("state"))
        print(f"microvm state={state}", file=sys.stderr)
        if state == "RUNNING":
            return resp
        if state in {"FAILED", "TERMINATED"}:
            raise RuntimeError(f"MicroVM entered terminal state {state}: {resp}")
        time.sleep(poll_seconds)
    raise TimeoutError(f"Timed out waiting for MicroVM to RUNNING. Last response: {last}")


def _extract_token(auth_resp: Dict[str, Any]) -> str:
    token_obj = auth_resp.get("authToken")
    if isinstance(token_obj, dict) and "X-aws-proxy-auth" in token_obj:
        return str(token_obj["X-aws-proxy-auth"])
    if isinstance(token_obj, str):
        return token_obj
    raise RuntimeError(
        "Cannot extract auth token from create-microvm-auth-token response "
        f"(top-level keys: {sorted(auth_resp.keys())})"
    )


def _build_run_hook_payload(args: argparse.Namespace) -> Optional[str]:
    payload: Dict[str, Any] = {}
    if args.correlation_id:
        payload["correlationId"] = args.correlation_id
    if args.commit_sha:
        payload["commitSha"] = args.commit_sha
    if getattr(args, "target_config", None):
        payload["targetConfig"] = json.loads(_target_config_as_json(args.target_config))
    return json.dumps(payload) if payload else None


def _target_config_as_json(path: str) -> str:
    """Load a target config (YAML or JSON) into a JSON string for the run hook."""
    text = Path(path).read_text(encoding="utf-8")
    if path.lower().endswith(".json"):
        return text
    import yaml  # type: ignore

    return json.dumps(yaml.safe_load(text))


def cmd_run(args: argparse.Namespace) -> int:
    """Start a MicroVM and leave it running (lifecycle only).

    Prints microvmId/endpoint for a subsequent start-analysis/fetch-results.
    """
    _require_aws_mode(args)
    aws = _aws(args)
    region = _region_of(args)
    ingress = args.ingress_network_connector or DEFAULT_INGRESS.format(region=region)
    egress = args.egress_network_connector or DEFAULT_INTERNET_EGRESS.format(region=region)
    if args.profile_mode == "production" and not args.egress_network_connector:
        raise SystemExit("production profile requires an explicit --egress-network-connector (VPC egress)")
    run_args = [
        "run-microvm",
        "--image-identifier", args.image_identifier,
        "--ingress-network-connectors", ingress,
        "--egress-network-connectors", egress,
        "--maximum-duration-in-seconds", str(args.max_duration_seconds),
        "--idle-policy", json.dumps({
            "autoResumeEnabled": True,
            "maxIdleDurationSeconds": args.idle_seconds,
            "suspendedDurationSeconds": args.suspended_seconds,
        }),
    ]
    if args.image_version:
        run_args.extend(["--image-version", args.image_version])
    if args.execution_role_arn:
        run_args.extend(["--execution-role-arn", args.execution_role_arn])
    payload = _build_run_hook_payload(args)
    if payload:
        run_args.extend(["--run-hook-payload", payload])
    resp = aws.microvms(run_args)
    if aws.dry_print:
        aws.microvms(["get-microvm", "--microvm-identifier", "<microvmId>"])
        print("print-only: skipped live run")
        return 0
    if not isinstance(resp, dict):
        raise RuntimeError("Unexpected non-JSON response from run-microvm")
    microvm_id = str(resp["microvmId"])
    endpoint = str(resp["endpoint"])
    _wait_microvm_running(aws, microvm_id, args.wait_timeout_seconds, args.poll_seconds)
    _print_json({"microvmId": microvm_id, "endpoint": endpoint})
    return 0


def _endpoint_session(aws: AwsCli, microvm_id: str, port: int, token_minutes: int):
    info = aws.microvms(["get-microvm", "--microvm-identifier", microvm_id])
    endpoint = str(info["endpoint"])
    auth = aws.microvms([
        "create-microvm-auth-token",
        "--microvm-identifier", microvm_id,
        "--expiration-in-minutes", str(token_minutes),
        "--allowed-ports", json.dumps([{"port": port}]),
    ])
    token = _extract_token(auth)
    return f"https://{endpoint}", token


def cmd_start_analysis(args: argparse.Namespace) -> int:
    _require_aws_mode(args)
    aws = _aws(args)
    base_url, token = _endpoint_session(aws, args.microvm_identifier, args.port, args.token_expiration_minutes)
    body: Dict[str, Any] = {"correlationId": args.correlation_id, "commitSha": args.commit_sha}
    if getattr(args, "target_config", None):
        body["targetConfig"] = json.loads(_target_config_as_json(args.target_config))
    resp = request_json("POST", f"{base_url}/analysis/start", token=token, port=args.port, payload=body, retries=3)
    _print_json(resp)
    return 0


def cmd_fetch_results(args: argparse.Namespace) -> int:
    _require_aws_mode(args)
    aws = _aws(args)
    base_url, token = _endpoint_session(aws, args.microvm_identifier, args.port, args.token_expiration_minutes)
    out_dir = Path(args.output_dir)
    out_dir.mkdir(parents=True, exist_ok=True)

    report = request_json("GET", f"{base_url}/analysis/report", token=token, port=args.port, retries=5)

    # events.jsonl and named artifacts are best-effort.
    for name, path in (("events.jsonl", "/analysis/events"),):
        try:
            raw = request_json("GET", f"{base_url}{path}", token=token, port=args.port, retries=3, raw=True)
            (out_dir / name).write_bytes(raw)
        except Exception as exc:  # noqa: BLE001
            print(f"WARNING: could not fetch {name}: {exc}", file=sys.stderr)

    # Optional VPC Flow Logs correlation (post-processing metadata, never fatal).
    if getattr(args, "flow_log_group", None):
        from .flow_logs import fetch_flow_logs, attach_flow_logs
        target = report.get("target", {})
        result = fetch_flow_logs(
            aws,
            log_group=args.flow_log_group,
            start_iso=str(target.get("startedAt", "")),
            end_iso=str(target.get("endedAt", "")),
            eni_id=getattr(args, "flow_log_eni", None),
        )
        attach_flow_logs(report, result)
        print(f"flow logs: available={result.available} records={result.recordCount}")

    (out_dir / "report.json").write_text(json.dumps(report, indent=2, sort_keys=True), encoding="utf-8")

    ok, reasons = evaluate_report(report, fail_on_severity=args.fail_on_severity, fail_on_policy_violation=args.fail_on_policy_violation)
    print(f"report written to {out_dir/'report.json'}")
    if ok:
        print("policy: passed")
        return 0
    print("policy: failed")
    for reason in reasons:
        print(f"- {reason}")
    return 1


def cmd_terminate(args: argparse.Namespace) -> int:
    _require_aws_mode(args)
    aws = _aws(args)
    resp = aws.microvms(["terminate-microvm", "--microvm-identifier", args.microvm_identifier])
    _print_json(resp if isinstance(resp, dict) else {"output": resp})
    return 0


def cmd_cleanup_stale(args: argparse.Namespace) -> int:
    """Terminate MicroVMs left running (safety net for failed CI runs)."""
    _require_aws_mode(args)
    aws = _aws(args)
    resp = aws.microvms(["list-microvms"])
    items = resp.get("items", resp.get("microvms", [])) if isinstance(resp, dict) else []
    terminated: List[str] = []
    for item in items:
        state = str(item.get("state", "")).upper()
        mid = item.get("microvmId") or item.get("microVmId")
        if mid and state in {"RUNNING", "SUSPENDED", "PENDING"}:
            try:
                aws.microvms(["terminate-microvm", "--microvm-identifier", str(mid)])
                terminated.append(str(mid))
            except AwsCliError as exc:
                print(f"WARNING: failed to terminate {mid}: {exc}", file=sys.stderr)
    _print_json({"terminated": terminated, "count": len(terminated)})
    return 0


# --------------------------------------------------------------------------- #
# Argument parser
# --------------------------------------------------------------------------- #
def _add_aws_safety_flags(p: argparse.ArgumentParser) -> None:
    p.add_argument("--confirm-sandbox-account", action="store_true", help="Required to run real AWS operations")
    p.add_argument("--print-only", action="store_true", help="Print the planned AWS CLI calls without executing")


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(prog="microvm-dta")
    parser.add_argument("--profile", default=None, help="AWS profile for AWS commands")
    parser.add_argument("--region", default=os.environ.get("AWS_REGION") or os.environ.get("AWS_DEFAULT_REGION"), help="AWS region")
    sub = parser.add_subparsers(dest="command", required=True)

    p = sub.add_parser("package", help="Package microvm/ into a zip artifact")
    p.add_argument("--source-dir", default="microvm")
    p.add_argument("--output", default="out/microvm-dta.zip")
    p.set_defaults(func=cmd_package)

    p = sub.add_parser("dry-run", help="Run a target through the supervisor locally (no AWS)")
    p.add_argument("--target-config", default="examples/targets/benign-command.yaml")
    p.add_argument("--workspace", default="out/analysis")
    p.add_argument("--rules-file", default=None)
    p.add_argument("--correlation-id", default=os.environ.get("GITHUB_RUN_ID"))
    p.add_argument("--commit-sha", default=os.environ.get("GITHUB_SHA"))
    p.add_argument("--allow-shell-strings", action="store_true", help="(unsafe) allow shell metacharacters in argv")
    p.set_defaults(func=cmd_dry_run)

    p = sub.add_parser("evaluate", help="Evaluate a report against CI policy")
    p.add_argument("--report", required=True)
    p.add_argument("--fail-on-severity", default="high")
    p.add_argument("--fail-on-policy-violation", action=argparse.BooleanOptionalAction, default=True)
    p.set_defaults(func=cmd_evaluate)

    p = sub.add_parser("build-image", help="Create or update a Lambda MicroVM image")
    p.add_argument("--image-name", required=True)
    p.add_argument("--artifact-uri", required=True)
    p.add_argument("--base-image-arn", required=True)
    p.add_argument("--build-role-arn", required=True)
    p.add_argument("--additional-os-capabilities", default=None, help="Comma-separated, e.g. ALL")
    p.add_argument("--description", default="aws-lambda-microvm-dta-sample")
    _add_aws_safety_flags(p)
    p.set_defaults(func=cmd_build_image)

    p = sub.add_parser("wait-image", help="Wait for MicroVM image readiness")
    p.add_argument("--image-identifier", required=True)
    p.add_argument("--timeout-seconds", type=int, default=1800)
    p.add_argument("--poll-seconds", type=int, default=15)
    _add_aws_safety_flags(p)
    p.set_defaults(func=cmd_wait_image)

    p = sub.add_parser("run", help="Start a MicroVM (lifecycle only)")
    p.add_argument("--image-identifier", required=True)
    p.add_argument("--image-version", default=None)
    p.add_argument("--execution-role-arn", default=None)
    p.add_argument("--target-config", default=None, help="Embed target config in the run hook payload")
    p.add_argument("--profile-mode", choices=["public", "production"], default="public")
    p.add_argument("--max-duration-seconds", type=int, default=900)
    p.add_argument("--idle-seconds", type=int, default=600)
    p.add_argument("--suspended-seconds", type=int, default=300)
    p.add_argument("--wait-timeout-seconds", type=int, default=300)
    p.add_argument("--poll-seconds", type=int, default=5)
    p.add_argument("--ingress-network-connector", default=None)
    p.add_argument("--egress-network-connector", default=None)
    p.add_argument("--correlation-id", default=os.environ.get("GITHUB_RUN_ID"))
    p.add_argument("--commit-sha", default=os.environ.get("GITHUB_SHA"))
    _add_aws_safety_flags(p)
    p.set_defaults(func=cmd_run)

    p = sub.add_parser("start-analysis", help="Call /analysis/start on a running MicroVM")
    p.add_argument("--microvm-identifier", required=True)
    p.add_argument("--target-config", default=None)
    p.add_argument("--port", type=int, default=8080)
    p.add_argument("--token-expiration-minutes", type=int, default=15)
    p.add_argument("--correlation-id", default=os.environ.get("GITHUB_RUN_ID"))
    p.add_argument("--commit-sha", default=os.environ.get("GITHUB_SHA"))
    _add_aws_safety_flags(p)
    p.set_defaults(func=cmd_start_analysis)

    p = sub.add_parser("fetch-results", help="Download report/events from a MicroVM and evaluate")
    p.add_argument("--microvm-identifier", required=True)
    p.add_argument("--output-dir", default="out")
    p.add_argument("--port", type=int, default=8080)
    p.add_argument("--token-expiration-minutes", type=int, default=15)
    p.add_argument("--fail-on-severity", default="high")
    p.add_argument("--fail-on-policy-violation", action=argparse.BooleanOptionalAction, default=True)
    p.add_argument("--flow-log-group", default=None, help="CloudWatch log group for optional VPC Flow Logs correlation")
    p.add_argument("--flow-log-eni", default=None, help="Restrict flow-log correlation to this ENI id")
    _add_aws_safety_flags(p)
    p.set_defaults(func=cmd_fetch_results)

    p = sub.add_parser("terminate", help="Terminate a MicroVM")
    p.add_argument("--microvm-identifier", required=True)
    _add_aws_safety_flags(p)
    p.set_defaults(func=cmd_terminate)

    p = sub.add_parser("cleanup-stale", help="Terminate any non-terminated MicroVMs (safety net)")
    _add_aws_safety_flags(p)
    p.set_defaults(func=cmd_cleanup_stale)
    return parser


def main(argv: Optional[List[str]] = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)
    try:
        return int(args.func(args))
    except SystemExit:
        raise
    except Exception as exc:  # noqa: BLE001
        print(f"ERROR: {exc}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
