// Persistent gateway bridge: holds ONE WebSocket to the warm OpenClaw gateway and
// runs agent turns over it — eliminating the ~20s per-message CLI spawn cost.
// Exposes a tiny local HTTP API on 127.0.0.1:8090 that the sidecar calls.
//
//   GET /agent?m=<msg>&s=<sessionKey>  -> {"reply": "..."}          (sync)
//   POST /agent {m,s,attachments}      -> {"reply": "..."}          (sync, images)
//   POST /agent-async {m,s,attachments}-> {"turnId": "..."}         (returns at once)
//   GET /progress?id=<turnId>          -> {"text","done","reply"?}  (poll for stream)
//   GET /ready                         -> {"connected": true}
//
// Frame protocol (reverse-engineered + verified against gateway 2026.6.11):
//   server sends event connect.challenge{nonce}
//   client sends req connect{minProtocol,maxProtocol,role,scopes,caps,client{mode:backend},auth{token}}
//   server res ok -> hello-ok
//   client sends req agent{message,sessionKey,idempotencyKey}
//   server res ok -> result.payloads[].text   (async; deltas stream as events meanwhile)
const http = require("http");
const crypto = require("node:crypto");
const WebSocket = require("/app/node_modules/ws");

// DEMO FALLBACK ONLY: the template injects OPENCLAW_GATEWAY_TOKEN into every MicroVM
// (deploy.sh mints a random one), so this literal is never used in a real deploy. It
// stays as a last-resort so the bridge still starts if the var is somehow unset. For a
// hardened build, drop the default and fail fast on a missing token.
const TOKEN = process.env.OPENCLAW_GATEWAY_TOKEN || "poc-microvm-token-42";
const GW = "ws://127.0.0.1:18789";
const PORT = 8090;

let ws = null;
let connected = false;
const pending = new Map(); // requestId -> {resolve, reject, timer}
// Async turns for the poll-based streaming path: turnId -> {text, done, reply, error, at}
const turns = new Map();
// Gateway assigns its own runId per run (returned on the ack frame); delta
// events are keyed by that runId, so map it back to our turnId.
const runToTurn = new Map();
const TURN_TTL_MS = 10 * 60 * 1000;
// Async turns may legitimately run for hours (the Lambda pollers chain across
// invocations); the VM's 8h max lifetime is the real bound, not a poll timeout.
const ASYNC_TURN_TIMEOUT_MS = 8 * 60 * 60 * 1000;

// GC: drop turns 10 min after their last activity (progress poll or completion).
// An in-flight turn being polled keeps refreshing its timestamp, so only turns
// abandoned by every poller age out.
function gcTurns() {
  const cutoff = Date.now() - TURN_TTL_MS;
  for (const [id, t] of turns) if (t.at < cutoff) turns.delete(id);
  for (const [rid, tid] of runToTurn) if (!turns.has(tid)) runToTurn.delete(rid);
}

function connect() {
  connected = false;
  ws = new WebSocket(GW);
  ws.on("open", () => {});
  ws.on("message", (buf) => {
    let m;
    try { m = JSON.parse(buf.toString()); } catch { return; }
    if (m.event === "connect.challenge") {
      ws.send(JSON.stringify({
        type: "req", id: "connect", method: "connect",
        params: {
          minProtocol: 4, maxProtocol: 4, role: "operator",
          scopes: ["operator.admin"], caps: [],
          client: { id: "gateway-client", displayName: "gw-bridge",
                    version: "2026.6.11", platform: "linux", mode: "backend" },
          auth: { token: TOKEN },
        },
      }));
      return;
    }
    if (m.type === "res" && m.id === "connect") {
      connected = !!m.ok;
      if (!m.ok) { console.error("[bridge] connect failed", JSON.stringify(m.error)); ws.close(); }
      else console.error("[bridge] connected to gateway");
      return;
    }
    // Streaming deltas: the gateway broadcasts "agent" events to operator
    // clients while a run executes. Assistant-stream events carry accumulated
    // text and/or the raw delta in payload.data. Events are keyed by the
    // gateway-assigned runId, which the ack frame maps to our turnId.
    if (m.type === "event" && m.event === "agent") {
      const pl = m.payload || {};
      const tid = pl.runId ? runToTurn.get(pl.runId) : null;
      const t = tid ? turns.get(tid) : null;
      if (t && pl.stream === "assistant" && pl.data) {
        if (typeof pl.data.text === "string" && pl.data.text.length >= t.text.length) {
          t.text = pl.data.text;
        } else if (typeof pl.data.delta === "string") {
          t.text += pl.data.delta;
        }
      }
      return;
    }
    if (m.type === "res" && pending.has(m.id)) {
      // The agent method emits TWO res frames with the same id, BOTH ok:true:
      //   1) ack:   payload.status === "accepted" (+ runId of the spawned run)
      //   2) final: payload.status === "ok" + payload.result.payloads[]
      // Everything of interest is nested under m.payload (not m.result).
      const pl = m.payload || {};
      const result = pl.result;
      const isError = m.ok === false || m.error || pl.status === "error";
      const isFinal = (result && Array.isArray(result.payloads)) || isError;
      if (!isFinal) {
        // ack — capture the gateway runId so delta events route to this turn
        if (pl.runId && turns.has(m.id)) runToTurn.set(pl.runId, m.id);
        return;
      }
      const p = pending.get(m.id);
      pending.delete(m.id);
      clearTimeout(p.timer);
      if (isError) {
        p.reject(new Error(JSON.stringify(m.error || pl.error || m)));
      } else {
        p.resolve(result.payloads.map((x) => x.text).filter(Boolean).join(" ") || "(no reply)");
      }
    }
  });
  ws.on("close", () => { connected = false; setTimeout(connect, 1000); });
  ws.on("error", (e) => { console.error("[bridge] ws error", e.message); });
}

function runAgent(message, sessionKey, attachments, turnId, timeoutMs) {
  return new Promise((resolve, reject) => {
    if (!connected) return reject(new Error("gateway not connected"));
    const id = turnId || crypto.randomUUID();
    const timer = setTimeout(() => {
      pending.delete(id); reject(new Error("agent turn timeout"));
    }, timeoutMs || 280000);
    pending.set(id, { resolve, reject, timer });
    // Attachment wire format matches the gateway's own subagent-spawn caller:
    // [{type:"image", source:{type:"base64", media_type, data}}]
    const gwAttachments = (attachments || [])
      .filter((a) => a && a.data && a.media_type)
      .map((a) => ({
        type: "image",
        source: { type: "base64", media_type: a.media_type, data: a.data },
      }));
    ws.send(JSON.stringify({
      type: "req", id, method: "agent",
      params: {
        message, sessionKey, idempotencyKey: id,
        ...(gwAttachments.length ? { attachments: gwAttachments } : {}),
      },
    }));
  });
}

async function readJsonBody(req) {
  const chunks = [];
  for await (const c of req) chunks.push(c);
  return JSON.parse(Buffer.concat(chunks).toString() || "{}");
}

http.createServer(async (req, res) => {
  const u = new URL(req.url, "http://x");
  if (u.pathname === "/ready") {
    res.writeHead(200, { "Content-Type": "application/json" });
    return res.end(JSON.stringify({ connected }));
  }
  if (u.pathname === "/agent-async" && req.method === "POST") {
    // Fire an agent turn and return immediately; poll /progress for text.
    let body;
    try { body = await readJsonBody(req); } catch {
      res.writeHead(400, { "Content-Type": "application/json" });
      return res.end(JSON.stringify({ error: "bad json body" }));
    }
    gcTurns();
    const turnId = crypto.randomUUID();
    turns.set(turnId, { text: "", done: false, reply: null, error: null, at: Date.now() });
    runAgent(body.m || "", body.s || "default", body.attachments || null, turnId,
             ASYNC_TURN_TIMEOUT_MS)
      .then((reply) => {
        const t = turns.get(turnId);
        if (t) { t.done = true; t.reply = reply; t.at = Date.now(); }
      })
      .catch((e) => {
        console.error("[bridge] async agent turn failed:", e);
        const t = turns.get(turnId);
        if (t) { t.done = true; t.error = "agent turn failed"; t.at = Date.now(); }
      });
    res.writeHead(200, { "Content-Type": "application/json" });
    return res.end(JSON.stringify({ turnId }));
  }
  if (u.pathname === "/progress") {
    const t = turns.get(u.searchParams.get("id") || "");
    if (!t) {
      res.writeHead(404, { "Content-Type": "application/json" });
      return res.end(JSON.stringify({ error: "unknown turn" }));
    }
    t.at = Date.now(); // being polled = alive; see gcTurns

    res.writeHead(200, { "Content-Type": "application/json" });
    return res.end(JSON.stringify({
      text: t.text, done: t.done,
      ...(t.reply !== null ? { reply: t.reply } : {}),
      ...(t.error ? { error: t.error } : {}),
    }));
  }
  if (u.pathname === "/agent") {
    let msg = u.searchParams.get("m") || "";
    let sess = u.searchParams.get("s") || "default";
    let attachments = null;
    if (req.method === "POST") {
      // JSON body variant for image turns (base64 too big for a query string).
      try {
        const chunks = [];
        for await (const c of req) chunks.push(c);
        const body = JSON.parse(Buffer.concat(chunks).toString() || "{}");
        msg = body.m || msg;
        sess = body.s || sess;
        attachments = body.attachments || null;
      } catch {
        res.writeHead(400, { "Content-Type": "application/json" });
        return res.end(JSON.stringify({ error: "bad json body" }));
      }
    }
    try {
      const reply = await runAgent(msg, sess, attachments);
      res.writeHead(200, { "Content-Type": "application/json" });
      res.end(JSON.stringify({ reply }));
    } catch (e) {
      // Log the detail server-side only; never echo exception text to the client
      // (CodeQL js/stack-trace-exposure).
      console.error("[bridge] agent turn failed:", e);
      res.writeHead(500, { "Content-Type": "application/json" });
      res.end(JSON.stringify({ error: "agent turn failed" }));
    }
    return;
  }
  res.writeHead(404); res.end();
}).listen(PORT, "127.0.0.1", () => console.error(`[bridge] http on :${PORT}`));

connect();
