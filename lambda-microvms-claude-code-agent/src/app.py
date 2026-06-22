"""
app.py — Claude Code Agent service for AWS Lambda MicroVMs

The MicroVM bakes in the Claude Code CLI and is launched with the
SHELL_INGRESS network connector. You connect via an interactive shell
and run `claude` directly inside the VM (Bedrock + Haiku, authenticated
through the execution role).

This process keeps the MicroVM alive and answers the runtime callbacks:
- Port 9000: MicroVM lifecycle hooks
- Port 8080: minimal health endpoint (handy for verifying the VM over HTTP)
"""

import json
import logging
import threading
from http.server import HTTPServer, BaseHTTPRequestHandler

logging.basicConfig(
    level=logging.INFO,
    format='{"timestamp": "%(asctime)s", "level": "%(levelname)s", "message": "%(message)s"}'
)
logger = logging.getLogger(__name__)

MICROVM_ID = None  # Set on the /run hook


# ── Health endpoint (port 8080) ───────────────────────────────────────────────

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
                "service": "claude-code-agent",
                "microvm_id": MICROVM_ID,
                "status": "ready"
            })
        else:
            self.send_json(404, {"error": "not found"})


# ── Lifecycle hook handler (port 9000) ────────────────────────────────────────

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
            logger.info("/ready — application is up, snapshot will be taken")
            self.send_json(200, {"status": "ready"})

        elif self.path.endswith("/run"):
            MICROVM_ID = body.get("microvmId")
            logger.info(f"/run — microvmId={MICROVM_ID}")
            self.send_json(200, {"status": "running"})

        elif self.path.endswith("/suspend"):
            logger.info("/suspend — flushing state before suspend")
            self.send_json(200, {"status": "suspending"})

        elif self.path.endswith("/resume"):
            logger.info("/resume — re-establishing connections")
            self.send_json(200, {"status": "resumed"})

        elif self.path.endswith("/terminate"):
            logger.info("/terminate — flushing before shutdown")
            self.send_json(200, {"status": "terminating"})

        else:
            self.send_json(404, {"error": "unknown hook"})


# ── Startup ───────────────────────────────────────────────────────────────────

def start_hook_server():
    """Start the lifecycle hook server on port 9000."""
    server = HTTPServer(("0.0.0.0", 9000), HookHandler)
    logger.info("Lifecycle hook server listening on port 9000")
    server.serve_forever()


def main():
    # Start lifecycle hook server in background thread
    threading.Thread(target=start_hook_server, daemon=True).start()

    # Start health server on port 8080 (foreground — keeps the VM alive)
    server = HTTPServer(("0.0.0.0", 8080), AppHandler)
    logger.info("Health endpoint listening on port 8080 — connect via shell to run `claude`")
    server.serve_forever()


if __name__ == "__main__":
    main()
