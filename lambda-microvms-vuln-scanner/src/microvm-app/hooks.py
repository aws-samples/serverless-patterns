"""
Lifecycle hook listener for the vulnerability scanner MicroVM.

Lambda MicroVMs invokes hooks by sending an HTTP POST to
  /aws/lambda-microvms/runtime/v1/<hook-name>
on the hooks port (default 9000).

Build-time hook (during create-microvm-image):
  * ready   - Lambda POSTs this to determine the application has initialized.
              The image build only succeeds once this returns HTTP 200.

Runtime hooks (during the MicroVM lifecycle):
  * run       - initialize per-scan state; traffic begins after this returns 200.
  * resume    - re-establish state after resuming from a suspend.
  * suspend   - flush partial output before the MicroVM is suspended.
  * terminate - final cleanup.

All hooks are POSTs. We answer 200 for every known hook path (both the
fully-qualified runtime path and the bare hook name, to be robust across
readiness/runtime probes).
"""

import os
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer

HOOKS_PORT = int(os.environ.get("HOOKS_PORT", "9000"))
HOOK_PREFIX = "/aws/lambda-microvms/runtime/v1"

# Hook names we acknowledge with 200 (matched against both
# "<prefix>/<name>" and "/<name>").
KNOWN_HOOKS = {"ready", "run", "resume", "suspend", "terminate"}


def _hook_name(path: str) -> str:
    """Return the trailing hook name for a request path, or ''."""
    p = path.rstrip("/")
    if p.startswith(HOOK_PREFIX + "/"):
        return p[len(HOOK_PREFIX) + 1:]
    return p.lstrip("/")


class HookHandler(BaseHTTPRequestHandler):
    def _ok(self, code: int = 200) -> None:
        self.send_response(code)
        self.send_header("Content-Length", "0")
        self.end_headers()

    def _handle(self):
        name = _hook_name(self.path)
        if name in KNOWN_HOOKS:
            print(f"hook: {name} -> 200")
            self._ok(200)
        else:
            self._ok(404)

    # Lambda MicroVMs POSTs all hooks (including the build-time /ready probe).
    def do_POST(self):  # noqa: N802
        self._handle()

    # Answer GET as well, so a health-style probe on the hook path also succeeds.
    def do_GET(self):  # noqa: N802
        self._handle()


def main() -> None:
    # nosec B104 - binding to 0.0.0.0 is required so Lambda MicroVMs can deliver
    # lifecycle hooks to this listener. The isolation boundary is the Firecracker
    # VM, not a loopback bind; 127.0.0.1 would make the hooks unreachable.
    server = ThreadingHTTPServer(("0.0.0.0", HOOKS_PORT), HookHandler)  # nosec B104
    print(f"Lifecycle hook listener on :{HOOKS_PORT}")
    server.serve_forever()


if __name__ == "__main__":
    main()
