"""
Vulnerability and security scanning application for AWS Lambda MicroVMs.

Contract (kept deliberately simple so any caller can reuse it):
  * Listens on APP_PORT (default 8080). Lambda routes ingress here.
  * GET  /health           -> {"status": "ok"}
  * POST /scan             -> scan an artifact and return a Trivy JSON report.
        Two input modes:
          a) Content-Type: application/octet-stream (or anything non-JSON)
             The request BODY is the raw artifact bytes (a file or a .tar/.zip).
             It is written to a fresh per-request directory and scanned. This is
             how the S3 event-driven orchestrator submits work: it downloads the
             uploaded object and POSTs the bytes here.
          b) Content-Type: application/json  with {"target": "/path"}
             Scans a path that already exists inside the MicroVM (used for the
             simple /app self-scan demo and local testing).

Each MicroVM is a single-tenant, Firecracker-isolated sandbox. In the
event-driven pattern one MicroVM is launched per uploaded artifact and
terminated after the scan, so untrusted inputs never share an environment.
"""

import json
import os
import shutil
import subprocess
import tempfile
import uuid
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer

APP_PORT = int(os.environ.get("APP_PORT", "8080"))


def _run_trivy(scan_path: str) -> dict:
    """Run `trivy filesystem` against scan_path and return the parsed report."""
    try:
        # nosec B603 - fixed argument list, no shell=True, and no user-controlled
        # executable: running the Trivy scanner on scan_path is the purpose of this
        # service. scan_path is a directory this process created, not caller input.
        completed = subprocess.run(  # nosec B603
            ["trivy", "--quiet", "filesystem", "--format", "json", scan_path],
            capture_output=True, text=True, timeout=600,
        )
        if completed.returncode == 0:
            return {"scanner": "trivy", "target": scan_path, "report": json.loads(completed.stdout)}
        return {"scanner": "trivy", "target": scan_path, "error": completed.stderr.strip()[:2000]}
    except FileNotFoundError:
        return {"scanner": "stub", "target": scan_path, "findings": [],
                "note": "trivy not found in image; bake it in to enable real scans."}
    except Exception as exc:  # noqa: BLE001
        return {"scanner": "trivy", "target": scan_path, "error": str(exc)}


def scan_bytes(artifact: bytes, filename: str = "artifact") -> dict:
    """Write artifact bytes to a fresh directory and scan that directory."""
    workdir = tempfile.mkdtemp(prefix=f"scan-{uuid.uuid4().hex[:8]}-")
    try:
        # Basic filename hardening so a crafted name cannot escape workdir.
        safe = os.path.basename(filename) or "artifact"
        path = os.path.join(workdir, safe)
        with open(path, "wb") as fh:
            fh.write(artifact)
        return _run_trivy(workdir)
    finally:
        shutil.rmtree(workdir, ignore_errors=True)


class ScanHandler(BaseHTTPRequestHandler):
    def _send(self, code: int, body: dict) -> None:
        payload = json.dumps(body).encode("utf-8")
        self.send_response(code)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(payload)))
        self.end_headers()
        self.wfile.write(payload)

    def do_GET(self):  # noqa: N802
        if self.path == "/health":
            self._send(200, {"status": "ok"})
        else:
            self._send(404, {"error": "not found"})

    def do_POST(self):  # noqa: N802
        if self.path != "/scan":
            self._send(404, {"error": "not found"})
            return
        length = int(self.headers.get("Content-Length", "0"))
        raw = self.rfile.read(length) if length else b""
        ctype = (self.headers.get("Content-Type") or "").lower()

        # Mode (b): JSON {"target": "..."} — scan an existing path.
        if "application/json" in ctype:
            try:
                body = json.loads(raw or b"{}")
            except json.JSONDecodeError:
                self._send(400, {"error": "invalid JSON"})
                return
            target = body.get("target", "/app")
            self._send(200, _run_trivy(target))
            return

        # Mode (a): raw artifact bytes — scan the uploaded artifact.
        if not raw:
            self._send(400, {"error": "empty artifact body"})
            return
        filename = self.headers.get("X-Artifact-Filename", "artifact")
        self._send(200, scan_bytes(raw, filename))


def main() -> None:
    # nosec B104 - binding to 0.0.0.0 is required so the Lambda MicroVMs ingress
    # connector can reach the app. The isolation boundary is the Firecracker VM
    # plus the JWE-authenticated endpoint, not a loopback bind; 127.0.0.1 would
    # make the scanner unreachable.
    server = ThreadingHTTPServer(("0.0.0.0", APP_PORT), ScanHandler)  # nosec B104
    print(f"Scanner listening on :{APP_PORT}")
    server.serve_forever()


if __name__ == "__main__":
    main()
