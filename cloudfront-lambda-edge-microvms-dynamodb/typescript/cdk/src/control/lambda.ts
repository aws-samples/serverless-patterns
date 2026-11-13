// Control-plane Lambda: regional (not edge), fronted by CloudFront on /_control* over
// an IAM-auth Function URL with Origin Access Control. Routes:
//   GET  /_control?session=ID[&return=/path]  launch-or-attach, then 307 back (or 200 JSON)
//   POST /_control/terminate?session=ID       terminate the session's MicroVM
// No authentication — this is a demo; the session id is the only key (README "Limitations").
import {
  LambdaMicrovmsClient,
  RunMicrovmCommand,
  GetMicrovmCommand,
  CreateMicrovmAuthTokenCommand,
  ResourceNotFoundException,
  TerminateMicrovmCommand,
} from "@aws-sdk/client-lambda-microvms";
import { ConditionalCheckFailedException, DynamoDBClient } from "@aws-sdk/client-dynamodb";
import { DeleteCommand, DynamoDBDocumentClient, GetCommand, PutCommand } from "@aws-sdk/lib-dynamodb";
import type { APIGatewayProxyEventV2 } from "aws-lambda";
import { ensureSession, LaunchInProgress, type EnsureDeps, type SessionRecord } from "./microvm.js";

const { SESSION_TABLE, IMAGE_ARN, EXECUTION_ROLE_ARN, RUNTIME_LOG_GROUP } = process.env as Record<string, string>;
const TTL_MS = 24 * 60 * 60_000; // records self-expire (table TTL) 24h after their last write

const microvms = new LambdaMicrovmsClient({});
const ddb = DynamoDBDocumentClient.from(new DynamoDBClient({}));

const item = (rec: SessionRecord) => ({ ...rec, expiresAt: Math.floor((Date.now() + TTL_MS) / 1000) });

const deps: EnsureDeps = {
  imageArn: IMAGE_ARN,
  now: Date.now,
  sleep: (ms) => new Promise((r) => setTimeout(r, ms)),
  ddb: {
    // ConsistentRead: a retry must see the microvmId the winner just wrote.
    get: async (sessionId) =>
      (await ddb.send(new GetCommand({ TableName: SESSION_TABLE, Key: { sessionId }, ConsistentRead: true })))
        .Item as SessionRecord | undefined,
    put: async (rec) => {
      await ddb.send(new PutCommand({ TableName: SESSION_TABLE, Item: item(rec) }));
    },
    // The launch mutex: succeeds only if no live launch holds the record.
    claim: async (rec, staleBefore, deadMicrovmId) => {
      try {
        await ddb.send(
          new PutCommand({
            TableName: SESSION_TABLE,
            Item: item(rec),
            ConditionExpression:
              "attribute_not_exists(launchedAt) OR launchedAt < :stale" + (deadMicrovmId ? " OR microvmId = :dead" : ""),
            ExpressionAttributeValues: { ":stale": staleBefore, ...(deadMicrovmId && { ":dead": deadMicrovmId }) },
          }),
        );
        return true;
      } catch (err) {
        if (err instanceof ConditionalCheckFailedException) return false;
        throw err;
      }
    },
  },
  mvm: {
    // The session id travels in runHookPayload (RunMicrovm has no per-run env vars).
    // executionRoleArn + logging send the VM's stdout/stderr to CloudWatch.
    runMicrovm: async (args) => {
      const out = await microvms.send(
        new RunMicrovmCommand({
          ...args,
          executionRoleArn: EXECUTION_ROLE_ARN,
          logging: { cloudWatch: { logGroup: RUNTIME_LOG_GROUP } },
        }),
      );
      return { microvmId: out.microvmId! };
    },
    getMicrovm: async (id) => {
      try {
        const out = await microvms.send(new GetMicrovmCommand({ microvmIdentifier: id }));
        return { state: out.state!, endpoint: out.endpoint! };
      } catch (err) {
        if (err instanceof ResourceNotFoundException) return undefined;
        throw err;
      }
    },
    createAuthToken: async (id) => {
      const out = await microvms.send(
        new CreateMicrovmAuthTokenCommand({ microvmIdentifier: id, expirationInMinutes: 30, allowedPorts: [{ port: 8080 }] }),
      );
      return out.authToken!["X-aws-proxy-auth"];
    },
  },
};

export type Controls = {
  ensure: (sessionId: string) => Promise<void>;
  terminate: (sessionId: string) => Promise<void>;
};

const controls: Controls = {
  ensure: (sessionId) => ensureSession(deps, sessionId),
  // Best effort: the record is deleted even if TerminateMicrovm fails; a VM left
  // running is reclaimed by its idle policy.
  terminate: async (sessionId) => {
    const rec = await deps.ddb.get(sessionId);
    if (rec?.microvmId) {
      await microvms
        .send(new TerminateMicrovmCommand({ microvmIdentifier: rec.microvmId }))
        .catch((err) => console.error("TerminateMicrovm failed", { sessionId, err }));
    }
    await ddb.send(new DeleteCommand({ TableName: SESSION_TABLE, Key: { sessionId } }));
  },
};

type ControlEvent = { rawPath: string; rawQueryString: string; method: string };

const SESSION_RE = /^[A-Za-z0-9_-]{1,64}$/;

// Only same-origin relative paths are valid `return` targets. Browsers treat "//host" and
// "/\host" as protocol-relative, and strip tabs/newlines first ("/\t/host" -> "//host"),
// so any of those would make this an open redirect.
const isSafeReturn = (ret: string) =>
  ret.startsWith("/") && !ret.startsWith("//") && !ret.startsWith("/\\") && !/[\x00-\x1f\x7f]/.test(ret);

const json = (statusCode: number, body: unknown) => ({
  statusCode,
  headers: { "content-type": "application/json", "cache-control": "no-store" },
  body: JSON.stringify(body),
});

export async function handle(controls: Controls, event: ControlEvent) {
  const route = event.rawPath.replace(/^\/_control/, "").replace(/\/$/, "");
  const params = new URLSearchParams(event.rawQueryString);
  const sessionId = params.get("session") ?? "";
  if (!SESSION_RE.test(sessionId)) return json(400, { error: "missing or invalid session" });

  try {
    if (route === "") {
      await controls.ensure(sessionId);
      // Bounce the viewer back with _attempt=1 (the edge's loop guard).
      const ret = params.get("return");
      if (ret && isSafeReturn(ret)) {
        return {
          statusCode: 307,
          headers: { location: `${ret}${ret.includes("?") ? "&" : "?"}_attempt=1`, "cache-control": "no-store" },
          body: "",
        };
      }
      return json(200, { sessionId, state: "RUNNING" });
    }
    if (route === "/terminate") {
      if (event.method !== "POST") return json(405, { error: "use POST" });
      await controls.terminate(sessionId);
      return json(200, { sessionId, state: "TERMINATED" });
    }
    return json(404, { error: "unknown control route" });
  } catch (err) {
    if (err instanceof LaunchInProgress) return json(503, { error: "launch in progress, retry shortly" });
    console.error("control operation failed", { sessionId, route, err });
    return json(500, { error: "control operation failed" });
  }
}

export const handler = (event: APIGatewayProxyEventV2) =>
  handle(controls, {
    rawPath: event.rawPath,
    rawQueryString: event.rawQueryString,
    method: event.requestContext.http.method,
  });
