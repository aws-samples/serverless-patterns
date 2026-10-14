import express from "express";
import path from "node:path";
import { timingSafeEqual } from "node:crypto";
import { BedrockAgentCoreClient, InvokeAgentRuntimeCommand } from "@aws-sdk/client-bedrock-agentcore";

const AGENT_RUNTIME_ARN = process.env.AGENT_RUNTIME_ARN;
// Set by Terraform. CloudFront sends the same value in the X-Origin-Verify header.
const ORIGIN_VERIFY_SECRET = process.env.ORIGIN_VERIFY_SECRET;

if (!AGENT_RUNTIME_ARN) {
  console.error("AGENT_RUNTIME_ARN env var is required");
  process.exit(1);
}

// arn:aws:bedrock-agentcore:<region>:<account>:runtime/<id>
const agentRegion = AGENT_RUNTIME_ARN.split(":")[3];
const agentcore = new BedrockAgentCoreClient({ region: agentRegion });

// The browser creates one session ID per tab. AgentCore Runtime keeps each session in its own
// isolated microVM, so two users never share one. Session IDs must be at least 33 characters.
const SESSION_ID = /^[0-9a-f]{8}-[0-9a-f]{4}-4[0-9a-f]{3}-[89ab][0-9a-f]{3}-[0-9a-f]{12}$/;

const app = express();
app.disable("x-powered-by");

// Only accept requests that came through CloudFront. Without this check, anyone who finds the
// Web Function endpoint could skip CloudFront and any AWS WAF rules attached to it.
const expected = ORIGIN_VERIFY_SECRET ? Buffer.from(ORIGIN_VERIFY_SECRET) : null;
app.use((req, res, next) => {
  if (!expected) return next(); // local development
  const received = Buffer.from(req.get("x-origin-verify") ?? "");
  if (received.length === expected.length && timingSafeEqual(received, expected)) return next();
  res.status(403).json({ error: "Forbidden. Use the CloudFront URL." });
});

app.use(express.json({ limit: "32kb" }));
app.use(express.static(path.join(import.meta.dirname, "static")));

// Invoke the agent and stream its SSE response back to the browser as it arrives.
app.post("/api/chat", async (req, res) => {
  const { prompt, sessionId } = req.body ?? {};
  if (typeof prompt !== "string" || !prompt.trim()) {
    return res.status(400).json({ error: "Missing required field: 'prompt'" });
  }
  if (typeof sessionId !== "string" || !SESSION_ID.test(sessionId)) {
    return res.status(400).json({ error: "Missing or invalid field: 'sessionId'" });
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
