import express from "express";
import path from "node:path";
import { createHmac, randomUUID, timingSafeEqual } from "node:crypto";
import { BedrockAgentCoreClient, InvokeAgentRuntimeCommand } from "@aws-sdk/client-bedrock-agentcore";
import { SecretsManagerClient, GetSecretValueCommand } from "@aws-sdk/client-secrets-manager";

const { AGENT_RUNTIME_ARN, LOGIN_SECRET_ARN, SESSION_SIGNING_KEY_ARN } = process.env;
// Set by Terraform. CloudFront sends the same value in the X-Origin-Verify header.
const ORIGIN_VERIFY_SECRET = process.env.ORIGIN_VERIFY_SECRET;

for (const [name, value] of Object.entries({ AGENT_RUNTIME_ARN, LOGIN_SECRET_ARN, SESSION_SIGNING_KEY_ARN })) {
  if (!value) {
    console.error(`${name} env var is required`);
    process.exit(1);
  }
}

// Prompts longer than this are rejected, to cap the input tokens a single request can spend.
// The agent caps the output tokens.
const MAX_PROMPT_LENGTH = 100;

// arn:aws:bedrock-agentcore:<region>:<account>:runtime/<id>
const agentRegion = AGENT_RUNTIME_ARN.split(":")[3];
const agentcore = new BedrockAgentCoreClient({ region: agentRegion });

// Read both secrets once, when the execution environment starts.
const secretsManager = new SecretsManagerClient({ region: agentRegion });
async function loadSecret(arn) {
  const { SecretString } = await secretsManager.send(new GetSecretValueCommand({ SecretId: arn }));
  if (!SecretString) throw new Error(`Secret ${arn} has no string value`);
  return SecretString;
}
const [LOGIN_SECRET, SESSION_SIGNING_KEY] = await Promise.all([
  loadSecret(LOGIN_SECRET_ARN),
  loadSecret(SESSION_SIGNING_KEY_ARN),
]);

function safeEqual(a, b) {
  const x = Buffer.from(a);
  const y = Buffer.from(b);
  return x.length === y.length && timingSafeEqual(x, y);
}

// A session token is "<sessionId>.<HMAC of sessionId>". The server picks the session ID, so a
// browser cannot choose or guess another user's AgentCore session. The session ID is a UUID,
// which contains no ".", so splitting on the last "." is unambiguous.
function sign(sessionId) {
  return createHmac("sha256", SESSION_SIGNING_KEY).update(sessionId).digest("base64url");
}
function issueSessionToken() {
  const sessionId = randomUUID();
  return `${sessionId}.${sign(sessionId)}`;
}
function verifySessionToken(token) {
  const dot = token.lastIndexOf(".");
  if (dot < 0) return null;
  const sessionId = token.slice(0, dot);
  return safeEqual(token.slice(dot + 1), sign(sessionId)) ? sessionId : null;
}

const app = express();
app.disable("x-powered-by");

// Only accept requests that came through CloudFront. Without this check, anyone who finds the
// Web Function endpoint could skip CloudFront and any AWS WAF rules attached to it.
app.use((req, res, next) => {
  if (!ORIGIN_VERIFY_SECRET) return next(); // local development
  if (safeEqual(req.get("x-origin-verify") ?? "", ORIGIN_VERIFY_SECRET)) return next();
  res.status(403).json({ error: "Forbidden. Use the CloudFront URL." });
});

app.use(express.json({ limit: "32kb" }));
app.use(express.static(path.join(import.meta.dirname, "static")));

// Exchange the login secret for a session token. The login secret is sent only here; every chat
// request then carries the token. Each call starts a new conversation.
app.post("/connect", (req, res) => {
  const secret = req.body?.secret;
  if (typeof secret !== "string" || !safeEqual(secret, LOGIN_SECRET)) {
    return res.status(401).json({ error: "Invalid or missing login secret" });
  }
  res.json({ sessionToken: issueSessionToken() });
});

// Invoke the agent and stream its SSE response back to the browser as it arrives.
app.post("/api/chat", async (req, res) => {
  const sessionId = verifySessionToken(req.get("x-session-token") ?? "");
  if (!sessionId) {
    return res.status(401).json({ error: "Invalid or missing session token" });
  }
  const { prompt } = req.body ?? {};
  if (typeof prompt !== "string" || !prompt.trim()) {
    return res.status(400).json({ error: "Missing required field: 'prompt'" });
  }
  if (prompt.length > MAX_PROMPT_LENGTH) {
    return res.status(400).json({ error: `'prompt' must be at most ${MAX_PROMPT_LENGTH} characters` });
  }

  // Stop the agent invocation if the browser goes away mid-stream.
  const abortController = new AbortController();
  res.on("close", () => {
    if (!res.writableEnded) abortController.abort();
  });

  res.writeHead(200, {
    "Content-Type": "text/event-stream",
    "Cache-Control": "no-cache",
    Connection: "keep-alive",
    "X-Accel-Buffering": "no",
  });
  res.flushHeaders();

  try {
    const command = new InvokeAgentRuntimeCommand({
      agentRuntimeArn: AGENT_RUNTIME_ARN,
      runtimeSessionId: sessionId,
      contentType: "application/json",
      accept: "text/event-stream",
      payload: new TextEncoder().encode(JSON.stringify({ prompt })),
    });
    const agentResponse = await agentcore.send(command, { abortSignal: abortController.signal });

    // The agent already emits SSE frames ("data: {...}\n\n"), so pass the bytes through as-is.
    for await (const chunk of agentResponse.response) {
      res.write(chunk);
    }
  } catch (err) {
    if (abortController.signal.aborted) return;
    console.error("Agent invocation failed:", err);
    res.write(`data: ${JSON.stringify({ type: "error", error: "The agent could not answer. Check the Web Function logs." })}\n\n`);
  }
  res.end();
});

const [HOSTNAME, PORT] = (process.env.AWS_LAMBDA_HTTP_ENDPOINT || "localhost:3000").split(":");
app.listen(PORT, HOSTNAME, () => {
  console.log(`webapp listening on http://${HOSTNAME}:${PORT}`);
  console.log(`agent runtime: ${AGENT_RUNTIME_ARN}`);
});
