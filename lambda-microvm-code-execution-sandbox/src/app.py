"""
app.py — Sandboxed Code Execution Service for Lambda MicroVM

Runs two HTTP servers:
- Port 8080: Code execution API (application traffic)
- Port 9000: Lifecycle hooks (MicroVM runtime callbacks)
"""

import os
import json
import logging
import subprocess
import tempfile
import threading
from http.server import HTTPServer, BaseHTTPRequestHandler

logging.basicConfig(
    level=logging.INFO,
    format='{"timestamp": "%(asctime)s", "level": "%(levelname)s", "message": "%(message)s"}'
)
logger = logging.getLogger(__name__)

MICROVM_ID = None  # Set on /launch hook


# ── Application handler (port 8080) ──────────────────────────────────────────

class AppHandler(BaseHTTPRequestHandler):
    """Handles code execution requests from AI agents."""

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
        if self.path == "/":
            self.send_json(200, {
                "service": "code-execution-sandbox",
                "microvm_id": MICROVM_ID,
                "status": "ready"
            })
        else:
            self.send_json(404, {"error": "not found"})

    def do_POST(self):
        if self.path == "/execute":
            length = int(self.headers.get("Content-Length", 0))
            body = json.loads(self.rfile.read(length)) if length else {}
            code = body.get("code", "")
            if not code.strip():
                self.send_json(400, {"error": "code field is required"})
                return
            self.send_json(200, execute_code(code))
        else:
            self.send_json(404, {"error": "not found"})


def execute_code(code: str) -> dict:
    """Execute Python code in an isolated subprocess with a 30-second timeout."""
    with tempfile.NamedTemporaryFile(mode="w", suffix=".py", delete=False) as f:
        f.write(code)
        script_path = f.name
    try:
        result = subprocess.run(
            ["python3", script_path],
            capture_output=True, text=True, timeout=30,
            cwd=tempfile.gettempdir()
        )
        return {
            "stdout": result.stdout,
            "stderr": result.stderr,
            "exit_code": result.returncode,
            "success": result.returncode == 0
        }
    except subprocess.TimeoutExpired:
        return {"stdout": "", "stderr": "Execution timed out after 30 seconds",
                "exit_code": -1, "success": False}
    except Exception as e:
        return {"stdout": "", "stderr": str(e), "exit_code": -1, "success": False}
    finally:
        os.unlink(script_path)


# ── Lifecycle hook handler (port 9000) ───────────────────────────────────────

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

    # Start application server on port 8080
    server = HTTPServer(("0.0.0.0", 8080), AppHandler)
    logger.info("Code execution API listening on port 8080")
    server.serve_forever()


if __name__ == "__main__":
    main()
