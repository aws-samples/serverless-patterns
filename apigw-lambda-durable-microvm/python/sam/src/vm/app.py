"""MicroVM application: lifecycle hooks plus one job per VM.

The platform POSTs hooks to /aws/lambda-microvms/runtime/v1/<hook>:
  ready, validate   during the image build, before the snapshot is taken
  run               after RunMicrovm; the body carries runHookPayload
  suspend, resume, terminate

On /run we parse {"command", "callbackId", "callbackUrl"} from runHookPayload,
run the command in a background thread, and POST the result to callbackUrl.
Standard library only.
"""
import json
import subprocess
import threading
import time
import urllib.error
import urllib.request
from http.server import BaseHTTPRequestHandler, HTTPServer

HOOK_PREFIX = "/aws/lambda-microvms/runtime/v1"
PORT = 8080
COMMAND_TIMEOUT = 600


def run_job(job: dict) -> None:
    try:
        proc = subprocess.run(
            job["command"], shell=True, capture_output=True, text=True, timeout=COMMAND_TIMEOUT
        )
        body = {
            "callbackId": job["callbackId"],
            "status": "success" if proc.returncode == 0 else "failure",
            "result": {"exitCode": proc.returncode, "stdout": proc.stdout[-4000:], "stderr": proc.stderr[-4000:]},
        }
        if proc.returncode != 0:
            body["error"] = {"type": "NonZeroExit", "message": f"exit code {proc.returncode}"}
    except subprocess.TimeoutExpired:
        body = {"callbackId": job["callbackId"], "status": "failure",
                "error": {"type": "Timeout", "message": f"command exceeded {COMMAND_TIMEOUT}s"}}
    post_callback(job["callbackUrl"], body)


def post_callback(url: str, body: dict) -> None:
    """POST the result; retry briefly so a transient API error does not leave
    the orchestrator waiting for the full timeout."""
    data = json.dumps(body).encode()
    for attempt in range(5):
        try:
            req = urllib.request.Request(url, data=data, method="POST", headers={"Content-Type": "application/json"})
            with urllib.request.urlopen(req, timeout=30) as resp:
                print(f"callback -> HTTP {resp.status} apigw-id={resp.headers.get('x-amz-apigw-id')}", flush=True)
                return
        except urllib.error.HTTPError as err:
            # Log what the server said. API Gateway stamps x-amzn-RequestId and
            # x-amz-apigw-id; a response without them came from somewhere else.
            hdrs = {k: err.headers.get(k) for k in ("x-amzn-RequestId", "x-amz-apigw-id", "x-amzn-ErrorType", "Server", "Via", "Date") if err.headers.get(k)}
            print(f"callback attempt {attempt + 1}: HTTP {err.code} headers={json.dumps(hdrs)} "
                  f"body={err.read()[:300]!r} local_time={time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())}", flush=True)
            if err.code in (400, 404, 409):
                return  # bad body, wrong URL, or already answered; retrying will not help
            # Anything else (a transient 403 or 5xx from the proxy or the API) is retried.
        except (urllib.error.URLError, TimeoutError) as err:
            print(f"callback attempt {attempt + 1}: {err}", flush=True)
        time.sleep(2 ** attempt)


class Handler(BaseHTTPRequestHandler):
    def _reply(self, status: int = 200, body: bytes = b"{}") -> None:
        self.send_response(status)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def _json_body(self) -> dict:
        length = int(self.headers.get("Content-Length") or 0)
        return json.loads(self.rfile.read(length) or b"{}")

    def do_GET(self):  # noqa: N802
        self._reply(200, b'{"status":"ok"}')

    def do_POST(self):  # noqa: N802
        hook = self.path.removeprefix(HOOK_PREFIX).strip("/")
        if hook == "run":
            payload = self._json_body().get("runHookPayload")
            if not payload:
                return self._reply(400, b'{"error":"no runHookPayload"}')
            job = json.loads(payload)
            threading.Thread(target=run_job, args=(job,), daemon=True).start()
            return self._reply()
        if hook in ("ready", "validate", "suspend", "resume", "terminate"):
            return self._reply()
        self._reply(404, b'{"error":"not found"}')

    def log_message(self, fmt, *args):  # keep the VM log to hook names
        print(f"{getattr(self, 'command', '-')} {getattr(self, 'path', '-')}", flush=True)


if __name__ == "__main__":
    print(f"listening on {PORT}", flush=True)
    HTTPServer(("0.0.0.0", PORT), Handler).serve_forever()
