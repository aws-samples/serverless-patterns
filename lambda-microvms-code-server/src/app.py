"""
app.py — VS Code Server (code-server) service for AWS Lambda MicroVM

Runs on port 9000 handling MicroVM lifecycle hooks (runtime callbacks).
The /ready hook waits for code-server to be healthy on port 8080 before
responding, ensuring the snapshot captures a fully booted IDE.

Copyright 2026 Amazon.com, Inc. or its affiliates. All Rights Reserved.
SPDX-License-Identifier: MIT-0
"""

import json
import logging
import os
import socket
import time
from http.server import HTTPServer, BaseHTTPRequestHandler

logging.basicConfig(
    level=logging.INFO,
    format='{"timestamp": "%(asctime)s", "level": "%(levelname)s", "message": "%(message)s"}'
)
logger = logging.getLogger(__name__)

MICROVM_ID = None  # Set on the /run hook


def wait_for_code_server(host="127.0.0.1", port=8080, timeout=240):
    """Block until code-server is accepting connections on port 8080."""
    deadline = time.time() + timeout
    while time.time() < deadline:
        try:
            with socket.create_connection((host, port), timeout=2):
                logger.info(f"code-server is up on port {port}")
                return True
        except (ConnectionRefusedError, OSError):
            time.sleep(1)
    logger.error(f"code-server did not start within {timeout}s")
    return False


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
            # Wait for code-server to be accepting connections before signaling ready
            if wait_for_code_server():
                logger.info("/ready — code-server is running, snapshot will be taken")
                self.send_json(200, {"status": "ready"})
            else:
                logger.error("/ready — code-server failed to start")
                self.send_json(500, {"status": "error", "message": "code-server not ready"})

        elif self.path.endswith("/run"):
            MICROVM_ID = body.get("microVmId")
            logger.info(f"/run — microVmId={MICROVM_ID}")
            self.send_json(200, {"status": "running"})

        elif self.path.endswith("/suspend"):
            logger.info("/suspend — flushing state before suspend")
            self.send_json(200, {"status": "suspending"})

        elif self.path.endswith("/resume"):
            logger.info("/resume — MicroVM resumed from suspension")
            self.send_json(200, {"status": "resumed"})

        elif self.path.endswith("/terminate"):
            logger.info("/terminate — shutting down gracefully")
            self.send_json(200, {"status": "terminating"})

        else:
            self.send_json(404, {"error": "unknown hook"})


# ── Startup ───────────────────────────────────────────────────────────────────

def main():
    port = int(os.environ.get("HOOKS_PORT", "9000"))
    server = HTTPServer(("0.0.0.0", port), HookHandler)
    logger.info(f"Lifecycle hook server listening on port {port}")
    server.serve_forever()


if __name__ == "__main__":
    main()
