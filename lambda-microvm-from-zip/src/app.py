"""Minimal Lambda MicroVM application — lifecycle hooks + health endpoint."""

import json
import threading
from http.server import HTTPServer, BaseHTTPRequestHandler

MICROVM_ID = None


class AppHandler(BaseHTTPRequestHandler):
    """Health endpoint on port 8080."""

    def log_message(self, *a):
        pass

    def do_GET(self):
        body = json.dumps({"status": "ok", "microvm_id": MICROVM_ID}).encode()
        self.send_response(200)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)


class HookHandler(BaseHTTPRequestHandler):
    """Lifecycle hooks on port 9000."""

    def log_message(self, *a):
        pass

    def do_POST(self):
        global MICROVM_ID
        length = int(self.headers.get("Content-Length", 0))
        body = json.loads(self.rfile.read(length)) if length else {}
        if self.path.endswith("/run"):
            MICROVM_ID = body.get("microvmId")
        self.send_response(200)
        self.send_header("Content-Type", "application/json")
        self.end_headers()
        self.wfile.write(b'{"status":"ok"}')


if __name__ == "__main__":
    threading.Thread(
        target=lambda: HTTPServer(("0.0.0.0", 9000), HookHandler).serve_forever(),
        daemon=True,
    ).start()
    HTTPServer(("0.0.0.0", 8080), AppHandler).serve_forever()
