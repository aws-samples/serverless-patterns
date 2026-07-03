"""Sandbox supervisor HTTP service (runs inside the Lambda MicroVM).

Exposes the analysis lifecycle and result artifacts over the authenticated
MicroVM endpoint. The supervisor receives a target config (via POST body or the
run hook payload), runs the analysis through :mod:`app.supervisor`, and serves
report.json, events.jsonl, and artifacts.
"""
from __future__ import annotations

from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from typing import Any, Dict, Optional
import json
import os
import threading
import traceback

from .supervisor import run_analysis
from .target_config import parse_target_config, load_target_config, TargetConfigError

PORT = int(os.environ.get("PORT", "8080"))
ANALYSIS_ROOT = os.environ.get("DTA_ANALYSIS_ROOT", "/analysis")
RULES_FILE = os.environ.get("DTA_RULES_FILE", "/app/rules/default.yaml")
SOURCE_BASE = os.environ.get("DTA_SOURCE_BASE", "/app")
DEFAULT_TARGET_CONFIG = os.environ.get("DTA_TARGET_CONFIG")  # optional path

_state_lock = threading.RLock()
_state: Dict[str, Any] = {
    "status": "idle",
    "report": None,
    "result": None,
    "last_error": None,
    "microvm_id": os.environ.get("AWS_LAMBDA_MICROVM_ID"),
    "run_hook_payload": None,
}


def _json_response(handler: BaseHTTPRequestHandler, status: int, payload: Dict[str, Any]) -> None:
    body = json.dumps(payload, indent=2, sort_keys=True).encode("utf-8")
    handler.send_response(status)
    handler.send_header("Content-Type", "application/json")
    handler.send_header("Content-Length", str(len(body)))
    handler.end_headers()
    handler.wfile.write(body)


def _bytes_response(handler: BaseHTTPRequestHandler, status: int, body: bytes, content_type: str) -> None:
    handler.send_response(status)
    handler.send_header("Content-Type", content_type)
    handler.send_header("Content-Length", str(len(body)))
    handler.end_headers()
    handler.wfile.write(body)


def _read_json(handler: BaseHTTPRequestHandler) -> Dict[str, Any]:
    length = int(handler.headers.get("Content-Length") or "0")
    if length == 0:
        return {}
    raw = handler.rfile.read(length)
    return json.loads(raw.decode("utf-8")) if raw else {}


def _resolve_target_config(request: Dict[str, Any]):
    """Determine the target config from the request, run hook payload, or env.

    Priority: explicit ``targetConfig`` object in the request → ``targetConfig``
    inside the stored run hook payload → ``DTA_TARGET_CONFIG`` file path.
    """
    allow_shell = os.environ.get("DTA_ALLOW_SHELL_STRINGS", "false").lower() == "true"
    if isinstance(request.get("targetConfig"), dict):
        return parse_target_config(request["targetConfig"], allow_shell_strings=allow_shell)
    with _state_lock:
        payload = _state.get("run_hook_payload")
    if isinstance(payload, str) and payload:
        try:
            payload = json.loads(payload)
        except json.JSONDecodeError:
            payload = None
    if isinstance(payload, dict) and isinstance(payload.get("targetConfig"), dict):
        return parse_target_config(payload["targetConfig"], allow_shell_strings=allow_shell)
    if DEFAULT_TARGET_CONFIG:
        return load_target_config(DEFAULT_TARGET_CONFIG, allow_shell_strings=allow_shell)
    raise TargetConfigError("no target config provided (request.targetConfig, run hook payload, or DTA_TARGET_CONFIG)")


def _run(request: Dict[str, Any]) -> Dict[str, Any]:
    config = _resolve_target_config(request)
    with _state_lock:
        microvm_id = _state.get("microvm_id")
    result = run_analysis(
        config,
        root=request.get("analysisRoot") or ANALYSIS_ROOT,
        rules_file=request.get("rulesFile") or RULES_FILE,
        source_base=SOURCE_BASE,
        correlation_id=request.get("correlationId") or os.environ.get("DTA_CORRELATION_ID"),
        commit_sha=request.get("commitSha") or os.environ.get("GITHUB_SHA"),
        mode="microvm",
        region=os.environ.get("AWS_REGION"),
        microvm_id=microvm_id,
        image_identifier=request.get("imageIdentifier") or os.environ.get("DTA_IMAGE_IDENTIFIER"),
    )
    with _state_lock:
        _state["result"] = result
    return result.report


class Handler(BaseHTTPRequestHandler):
    server_version = "microvm-dta-supervisor/0.2.0"

    def log_message(self, fmt: str, *args: Any) -> None:
        print(json.dumps({"level": "info", "message": fmt % args}))

    # --- GET ---
    def do_GET(self) -> None:  # noqa: N802
        if self.path == "/health":
            _json_response(self, 200, {"status": "ok"})
            return
        if self.path == "/analysis/status":
            with _state_lock:
                payload = {k: v for k, v in _state.items() if k not in ("report", "result")}
            _json_response(self, 200, payload)
            return
        if self.path == "/analysis/report":
            with _state_lock:
                report = _state.get("report")
                status = _state.get("status")
                err = _state.get("last_error")
            if report is None:
                _json_response(self, 404, {"status": status, "error": err or "report not ready"})
                return
            _json_response(self, 200, report)
            return
        if self.path == "/analysis/events":
            self._serve_events()
            return
        if self.path.startswith("/analysis/artifacts/"):
            self._serve_artifact(self.path[len("/analysis/artifacts/"):])
            return
        _json_response(self, 404, {"error": "not found", "path": self.path})

    def _serve_events(self) -> None:
        with _state_lock:
            result = _state.get("result")
        if result is None:
            _json_response(self, 404, {"error": "events not ready"})
            return
        try:
            body = Path(result.events_path).read_bytes()
        except OSError as exc:
            _json_response(self, 500, {"error": str(exc)})
            return
        _bytes_response(self, 200, body, "application/x-ndjson")

    def _serve_artifact(self, name: str) -> None:
        with _state_lock:
            result = _state.get("result")
        if result is None:
            _json_response(self, 404, {"error": "artifacts not ready"})
            return
        root = Path(result.report_path).parent
        # Confine artifact access to the analysis root (no path traversal).
        target = (root / name).resolve()
        try:
            target.relative_to(root.resolve())
        except ValueError:
            _json_response(self, 400, {"error": "invalid artifact path"})
            return
        if not target.is_file():
            _json_response(self, 404, {"error": "artifact not found", "name": name})
            return
        _bytes_response(self, 200, target.read_bytes(), "application/octet-stream")

    # --- POST ---
    def do_POST(self) -> None:  # noqa: N802
        if self.path in {"/aws/lambda-microvms/runtime/v1/ready", "/aws/lambda-microvms/runtime/v1/validate", "/ready", "/validate"}:
            _json_response(self, 200, {"status": "ready"})
            return
        if self.path in {"/aws/lambda-microvms/runtime/v1/run", "/run"}:
            payload = _read_json(self)
            with _state_lock:
                _state["microvm_id"] = payload.get("microvmId") or _state.get("microvm_id")
                _state["run_hook_payload"] = payload.get("runHookPayload")
                _state["status"] = "ready"
            _json_response(self, 200, {"status": "run-hook-ok"})
            return
        if self.path in {
            "/aws/lambda-microvms/runtime/v1/suspend", "/aws/lambda-microvms/runtime/v1/resume",
            "/aws/lambda-microvms/runtime/v1/terminate", "/suspend", "/resume", "/terminate",
        }:
            with _state_lock:
                _state["status"] = self.path.rsplit("/", 1)[-1]
            _json_response(self, 200, {"status": "ok", "hook": self.path})
            return
        if self.path == "/analysis/start":
            self._handle_start()
            return
        _json_response(self, 404, {"error": "not found", "path": self.path})

    def _handle_start(self) -> None:
        try:
            request = _read_json(self)
        except json.JSONDecodeError as exc:
            _json_response(self, 400, {"status": "failed", "error": f"invalid JSON: {exc}"})
            return
        with _state_lock:
            if _state["status"] == "running":
                _json_response(self, 409, {"status": "running", "error": "analysis already in progress"})
                return
            _state["status"] = "running"
            _state["last_error"] = None
        try:
            report = _run(request)
            with _state_lock:
                _state["report"] = report
                _state["status"] = report["summary"]["status"]
            _json_response(self, 200, {"status": report["summary"]["status"], "summary": report["summary"]})
        except Exception as exc:
            error = f"{exc.__class__.__name__}: {exc}"
            print(traceback.format_exc())
            with _state_lock:
                _state["status"] = "failed"
                _state["last_error"] = error
            _json_response(self, 500, {"status": "failed", "error": error})


def main() -> None:
    server = ThreadingHTTPServer(("0.0.0.0", PORT), Handler)
    print(json.dumps({"level": "info", "message": "supervisor listening", "port": PORT}))
    server.serve_forever()


if __name__ == "__main__":
    main()
