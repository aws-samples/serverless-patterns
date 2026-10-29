// In-MicroVM hello-world app (Node 22, no dependencies). Every GET on :8080 returns the
// session id the control plane passed in at launch.
//
//   :8080 — the app (what the edge proxies viewer traffic to)
//   :9000 — the lifecycle hooks the Lambda MicroVMs service calls
//
// Both answer /ready and /validate (a precaution in case the service polls the app port),
// and both bind 0.0.0.0 (a bare listen() can bind IPv6-only, which the poller can't reach).
import http from "node:http";

const HOOK_PREFIX = "/aws/lambda-microvms/runtime/v1/";
const startedAt = new Date().toISOString();

// Launch-time identity, populated by the /run hook from its runHookPayload.
const vm = { sessionId: "unknown", microvmId: "unknown", hits: 0 };

// :8080 — the app. Serves any GET (or HEAD) path: the edge forwards the viewer's path as-is.
function appHandler(req, res) {
  if (req.url?.startsWith(HOOK_PREFIX)) {
    const name = req.url.slice(HOOK_PREFIX.length).split("?")[0];
    if (name === "ready" || name === "validate") {
      res.writeHead(200);
      return res.end();
    }
  }
  if (req.method === "GET" || req.method === "HEAD") { // Node omits the body for HEAD
    vm.hits += 1;
    res.writeHead(200, { "content-type": "application/json" });
    return res.end(
      JSON.stringify({
        message: `Hello from session ${vm.sessionId}`,
        sessionId: vm.sessionId,
        microvmId: vm.microvmId,
        path: req.url,
        startedAt,
        hits: vm.hits,
      }),
    );
  }
  res.writeHead(404, { "content-type": "application/json" });
  res.end(JSON.stringify({ error: "not found" }));
}

// :9000 — lifecycle hooks. POST /run carries { microvmId, runHookPayload }, where
// runHookPayload is the JSON string { sessionId }. Always 200: a non-200 /run kills the VM.
async function hookHandler(req, res) {
  const name = req.url?.startsWith(HOOK_PREFIX) ? req.url.slice(HOOK_PREFIX.length).split("?")[0] : "";
  if (name === "run" && req.method === "POST") {
    try {
      let raw = "";
      for await (const chunk of req) raw += chunk;
      const { microvmId, runHookPayload } = JSON.parse(raw);
      vm.microvmId = microvmId ?? vm.microvmId;
      vm.sessionId = JSON.parse(runHookPayload ?? "{}").sessionId ?? vm.sessionId;
    } catch {
      // Ignore a malformed body: /run must still return 200.
    }
  }
  // ready / validate / run / resume / suspend / terminate all just succeed.
  res.writeHead(name ? 200 : 404);
  res.end();
}

http.createServer(appHandler).listen(8080, "0.0.0.0");
http.createServer(hookHandler).listen(9000, "0.0.0.0", () => {
  console.log("microvm-app: app listening on :8080, hooks on :9000");
});
