"""
app.py -- Codex CLI agent service for AWS Lambda MicroVMs

The MicroVM bakes in the Codex CLI and is launched with the SHELL_INGRESS network
connector. You connect over an interactive shell and run `codex` inside the VM,
against Amazon Bedrock, authenticated through the execution role.

This process has two jobs:

1. Render the Codex configuration from the MicroVM environment before signalling
   readiness, and again on /run and /resume. Nothing about the Region is baked
   into the image: AWS_REGION is supplied by the platform (it is a reserved
   environment variable and cannot be set on the image), the model comes from
   CODEX_MODEL, and the AWS MCP Server endpoint from AWS_MCP_ENDPOINT. The AWS
   CloudFormation template sets both from its ModelId and McpEndpoint parameters.
   Rendering at runtime is what keeps the image Region-agnostic.

2. Stay alive and answer the runtime callbacks:
     - Port 9000: MicroVM lifecycle hooks
     - Port 8080: health endpoint, which also reports the resolved configuration
"""

import json
import logging
import os
import threading
from http.server import HTTPServer, BaseHTTPRequestHandler
from pathlib import Path

logging.basicConfig(
    level=logging.INFO,
    format='{"timestamp": "%(asctime)s", "level": "%(levelname)s", "message": "%(message)s"}'
)
logger = logging.getLogger(__name__)

TEMPLATE_DIR = Path("/opt/codex-agent")
CODEX_HOME = Path(os.environ.get("CODEX_HOME", "/root/.codex"))

# Placeholders substituted into every template. Order is irrelevant, but
# membership matters: a placeholder missing from this tuple is left verbatim in
# the output.
PLACEHOLDERS = ("__AWS_REGION__", "__CODEX_MODEL__", "__AWS_MCP_ENDPOINT__")

RENDER_TARGETS = (
    (TEMPLATE_DIR / "codex-config.toml.tmpl", CODEX_HOME / "config.toml"),
    (TEMPLATE_DIR / "codex-profile.sh.tmpl", Path("/etc/profile.d/codex-agent.sh")),
)

MICROVM_ID = None
CONFIG_STATE = {}  # Resolved values, surfaced on /health for troubleshooting.


# -- Configuration rendering --------------------------------------------------

def resolve_settings() -> dict:
    """Resolve template placeholders from the MicroVM environment.

    A value that cannot be resolved is left out of the returned mapping, and
    render() drops every line that references it, so an unresolved Region falls
    back to the AWS SDK default chain instead of silently pointing Codex and the
    MCP server at the wrong one.
    """
    settings = {}

    region = os.environ.get("AWS_REGION") or os.environ.get("AWS_DEFAULT_REGION")
    if region:
        settings["__AWS_REGION__"] = region
    else:
        logger.error(
            "AWS_REGION and AWS_DEFAULT_REGION are both unset, so the Region is "
            "omitted from the Codex config and the shell profile. Amazon Bedrock calls "
            "will fail unless the AWS SDK default chain supplies a Region."
        )

    model = os.environ.get("CODEX_MODEL")
    if model:
        settings["__CODEX_MODEL__"] = model
    else:
        logger.error(
            "CODEX_MODEL is unset, so the model is omitted from the Codex config. "
            "Codex will fall back to the amazon-bedrock provider default, which "
            "may not be a model your account has access to. Set the ModelId "
            "AWS CloudFormation parameter and redeploy."
        )

    endpoint = os.environ.get("AWS_MCP_ENDPOINT")
    if endpoint:
        settings["__AWS_MCP_ENDPOINT__"] = endpoint
    else:
        logger.error(
            "AWS_MCP_ENDPOINT is unset, so the endpoint is omitted from the MCP "
            "server config and the AWS MCP Server will fail to start. Codex itself "
            "still works. Set the McpEndpoint AWS CloudFormation parameter and "
            "redeploy."
        )

    return settings


def render(template: Path, settings: dict) -> str:
    """Substitute placeholders, dropping any line whose value is unresolved."""
    lines = []
    for line in template.read_text().splitlines():
        # Comments are kept verbatim in both file types, placeholders and all:
        # they document the template rather than configure anything.
        if line.lstrip().startswith("#"):
            lines.append(line)
            continue

        placeholders = [p for p in PLACEHOLDERS if p in line]
        if any(p not in settings for p in placeholders):
            logger.warning(f"Dropping unresolved line from {template.name}: {line.strip()}")
            continue
        for placeholder in placeholders:
            line = line.replace(placeholder, settings[placeholder])
        lines.append(line)
    return "\n".join(lines) + "\n"


def write_config(reason: str) -> None:
    """Render every template. Never raises: a config failure must not stop the VM."""
    global CONFIG_STATE

    settings = resolve_settings()
    written, failed = [], {}

    for template, target in RENDER_TARGETS:
        try:
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_text(render(template, settings))
            written.append(str(target))
        except OSError as exc:
            logger.error(f"Failed to write {target}: {exc}")
            failed[str(target)] = str(exc)

    CONFIG_STATE = {
        "reason": reason,
        "region": settings.get("__AWS_REGION__"),
        "model": settings.get("__CODEX_MODEL__"),
        "mcp_endpoint": settings.get("__AWS_MCP_ENDPOINT__"),
        "written": written,
        "failed": failed,
    }
    logger.info(f"Rendered Codex config ({reason}): {json.dumps(CONFIG_STATE)}")


# -- Health endpoint (port 8080) ----------------------------------------------

class AppHandler(BaseHTTPRequestHandler):
    """Minimal health endpoint. Interactive work happens over the shell."""

    def log_message(self, format, *args):
        logger.info(f"APP {format % args}")

    def send_json(self, status: int, body: dict):
        payload = json.dumps(body).encode()
        self.send_response(status)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(payload)))
        self.end_headers()
        self.wfile.write(payload)

    def do_GET(self):
        if self.path in ("/", "/health"):
            self.send_json(200, {
                "service": "codex-cli-agent",
                "microvm_id": MICROVM_ID,
                "status": "ready",
                "config": CONFIG_STATE,
            })
        else:
            self.send_json(404, {"error": "not found"})


# -- Lifecycle hook handler (port 9000) ---------------------------------------

class HookHandler(BaseHTTPRequestHandler):
    """Handles MicroVM lifecycle hook callbacks from the runtime."""

    def log_message(self, format, *args):
        logger.info(f"HOOK {format % args}")

    def send_json(self, status: int, body: dict):
        payload = json.dumps(body).encode()
        self.send_response(status)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(payload)))
        self.end_headers()
        self.wfile.write(payload)

    def read_body(self) -> dict:
        length = int(self.headers.get("Content-Length", 0))
        return json.loads(self.rfile.read(length)) if length else {}

    def do_POST(self):
        global MICROVM_ID
        body = self.read_body()

        if self.path.endswith("/ready"):
            logger.info("/ready -- application is up, snapshot will be taken")
            self.send_json(200, {"status": "ready"})

        elif self.path.endswith("/run"):
            MICROVM_ID = body.get("microvmId")
            logger.info(f"/run -- microvmId={MICROVM_ID}")
            # Re-render after the snapshot resumes: this is the first point at
            # which the environment reflects where the VM is actually running.
            write_config("run")
            self.send_json(200, {"status": "running"})

        elif self.path.endswith("/suspend"):
            logger.info("/suspend -- flushing state before suspend")
            self.send_json(200, {"status": "suspending"})

        elif self.path.endswith("/resume"):
            logger.info("/resume -- re-establishing connections")
            write_config("resume")
            self.send_json(200, {"status": "resumed"})

        elif self.path.endswith("/terminate"):
            logger.info("/terminate -- flushing before shutdown")
            self.send_json(200, {"status": "terminating"})

        else:
            self.send_json(404, {"error": "unknown hook"})


# -- Startup ------------------------------------------------------------------

def start_hook_server():
    """Start the lifecycle hook server on port 9000."""
    server = HTTPServer(("0.0.0.0", 9000), HookHandler)
    logger.info("Lifecycle hook server listening on port 9000")
    server.serve_forever()


def main():
    # Render before anything else so the config is in place by the time the
    # runtime calls /ready and snapshots the VM.
    write_config("startup")

    threading.Thread(target=start_hook_server, daemon=True).start()

    # Health server on 8080 runs in the foreground and keeps the VM alive.
    server = HTTPServer(("0.0.0.0", 8080), AppHandler)
    logger.info("Health endpoint listening on port 8080 -- connect via shell to run `codex`")
    server.serve_forever()


if __name__ == "__main__":
    main()
