"""Sidecar (multi-tenant EFS variant): lifecycle hooks + health + /tenant + /chat + /tg + /files."""
import json
import os
import subprocess
import urllib.error
import urllib.parse
import urllib.request
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer

HOOK = "/aws/lambda-microvms/runtime/v1/"
OPENCLAW = "http://127.0.0.1:18789"
# DEMO FALLBACK ONLY: the template injects OPENCLAW_GATEWAY_TOKEN into every MicroVM
# (deploy.sh mints a random one), so this literal is never used in a real deploy. It
# stays as a last-resort so the VM still boots if the var is somehow unset. For a
# hardened build, drop the default and fail fast: os.environ["OPENCLAW_GATEWAY_TOKEN"].
GATEWAY_TOKEN = os.environ.get("OPENCLAW_GATEWAY_TOKEN", "poc-microvm-token-42")
TENANT_FILE = "/var/run/tenant-id"
MARKER = "/var/run/efs-mounted"


def agent_turn(message: str, session: str, attachments=None) -> bytes:
    """Run one agent turn via the PERSISTENT gateway bridge (no per-message CLI spawn).

    The bridge holds a warm WebSocket to the gateway; a turn is ~2s instead of ~22s.
    Image attachments (base64) POST to the bridge; text-only turns keep the GET path.
    Returns the same JSON shape callers expect: {"result":{"payloads":[{"text":...}]}}.
    """
    if attachments:
        req = urllib.request.Request(
            "http://127.0.0.1:8090/agent",
            data=json.dumps({"m": message, "s": session,
                             "attachments": attachments}).encode(),
            headers={"Content-Type": "application/json"}, method="POST")
        with urllib.request.urlopen(req, timeout=290) as r:
            d = json.loads(r.read())
    else:
        url = ("http://127.0.0.1:8090/agent?m=" + urllib.parse.quote(message)
               + "&s=" + urllib.parse.quote(session))
        with urllib.request.urlopen(url, timeout=290) as r:
            d = json.loads(r.read())
    if "error" in d:
        return json.dumps({"error": d["error"]}).encode()
    return json.dumps({"result": {"payloads": [{"text": d.get("reply", "")}]}}).encode()


def check(path: str):
    try:
        with urllib.request.urlopen(OPENCLAW + path, timeout=3) as r:
            return r.status, None
    except Exception as e:
        return getattr(e, "code", None), f"{type(e).__name__}: {e}"


def state_report() -> bytes:
    r = subprocess.run(
        ["sh", "-c",
         "echo '--- tenant ---'; cat /var/run/tenant-id 2>&1; "
         "echo; echo '--- mounts ---'; grep -E 'efs|openclaw|nfs' /proc/mounts; "
         "echo '--- marker ---'; ls -la /var/run/efs-mounted 2>&1; "
         "echo '--- state dir ---'; ls -la /home/node/.openclaw/ 2>&1 | head -14; "
         "echo '--- sessions ---'; ls -la /home/node/.openclaw/agents/main/sessions/ 2>&1 | head -8; "
         "echo '--- efs err ---'; tail -3 /tmp/efs-mount.err 2>&1"],
        capture_output=True, text=True, timeout=10,
    )
    return (r.stdout + r.stderr).encode()


class H(BaseHTTPRequestHandler):
    def _send(self, code, body=b""):
        self.send_response(code)
        self.send_header("Content-Type", "application/json")
        self.end_headers()
        self.wfile.write(body)

    def do_GET(self):
        if self.path == "/health":
            hz, herr = check("/healthz")
            rz, rerr = check("/readyz")
            self._send(200 if hz == 200 else 503, json.dumps(
                {"healthz": hz, "readyz": rz, "efsReady": os.path.exists(MARKER),
                 "tenant": open(TENANT_FILE).read().strip() if os.path.exists(TENANT_FILE) else None,
                 "healthzErr": herr, "readyzErr": rerr}).encode())
        elif self.path == "/files":
            self._send(200, state_report())
        elif self.path.startswith("/progress"):
            # Proxy to the bridge: poll accumulated stream text for an async turn.
            try:
                with urllib.request.urlopen(
                        "http://127.0.0.1:8090" + self.path, timeout=10) as r:
                    self._send(200, r.read())
            except urllib.error.HTTPError as e:
                self._send(e.code, e.read())
            except Exception as e:
                self._send(500, json.dumps({"error": str(e)}).encode())
        elif self.path.startswith("/chat"):
            q = urllib.parse.parse_qs(urllib.parse.urlparse(self.path).query)
            msg = (q.get("m") or ["Say pong"])[0]
            sess = (q.get("s") or ["poc-demo"])[0]
            try:
                self._send(200, agent_turn(msg, sess, None))
            except Exception as e:
                self._send(500, json.dumps({"error": str(e)}).encode())
        else:
            self._send(404)

    def do_POST(self):
        if self.path == "/chat":
            # JSON body variant of GET /chat — used for turns with image attachments
            # (base64 payloads don't fit in a query string).
            n = int(self.headers.get("Content-Length") or 0)
            try:
                d = json.loads(self.rfile.read(n) or b"{}")
                msg = d.get("m") or "Say pong"
                sess = d.get("s") or "poc-demo"
                atts = d.get("attachments") or None
                self._send(200, agent_turn(msg, sess, atts))
            except Exception as e:
                self._send(500, json.dumps({"error": str(e)}).encode())
        elif self.path == "/chat-async":
            # Start a turn without blocking; returns {"turnId"} for /progress polling.
            n = int(self.headers.get("Content-Length") or 0)
            try:
                body = self.rfile.read(n) or b"{}"
                json.loads(body)  # validate before proxying
                req = urllib.request.Request(
                    "http://127.0.0.1:8090/agent-async", data=body,
                    headers={"Content-Type": "application/json"}, method="POST")
                with urllib.request.urlopen(req, timeout=15) as r:
                    self._send(200, r.read())
            except Exception as e:
                self._send(500, json.dumps({"error": str(e)}).encode())
        elif self.path == "/tenant":
            # Orchestrator assigns the tenant; unblocks efs-monitor.
            n = int(self.headers.get("Content-Length") or 0)
            tid = json.loads(self.rfile.read(n) or b"{}").get("tenantId", "")
            tid = "".join(c for c in tid if c.isalnum() or c in "-_")[:64]
            if not tid:
                self._send(400, b'{"error":"tenantId required"}')
                return
            with open(TENANT_FILE, "w") as f:
                f.write(tid)
            print(f"[hooks] tenant assigned: {tid}", flush=True)
            self._send(200, json.dumps({"tenant": tid}).encode())
        elif self.path.startswith(HOOK):
            print(f"[hooks] POST {self.path} -> 200", flush=True)
            self._send(200)
        else:
            self._send(200)

    def log_message(self, *a):
        pass


if __name__ == "__main__":
    print("[hooks] sidecar listening on :8080", flush=True)
    ThreadingHTTPServer(("0.0.0.0", 8080), H).serve_forever()
