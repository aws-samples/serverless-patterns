// Edge router (Lambda@Edge, origin-request). Pure over the injected session lookup so it
// unit-tests without AWS; lambda.ts supplies the DynamoDB lookup.
import type { CloudFrontRequest, CloudFrontRequestResult } from "aws-lambda";

const MARGIN_MS = 60_000; // a token within 60s of expiry counts as a miss -> re-mint via control

// Session ids: URL-safe, 1-64 chars. Anything else is a 400 and never reaches DynamoDB.
const SESSION_RE = /^[A-Za-z0-9_-]{1,64}$/;
// Path form: /s/{sessionId}/rest -> session = {sessionId}, forward = /rest (or "/").
const PATH_RE = /^\/s\/([^/]+)(\/.*)?$/;

export interface Session {
  endpoint: string;
  token?: string;
  tokenExpiresAt?: number;
}

const noStore = { "cache-control": [{ key: "Cache-Control", value: "no-store" }] };
export const reply = (status: string, statusDescription: string, body: string): CloudFrontRequestResult => ({
  status,
  statusDescription,
  headers: { ...noStore, "content-type": [{ key: "Content-Type", value: "text/plain" }] },
  body,
});

// Session id from the `/s/{id}/...` path prefix first, else the `?session=` query param,
// plus the path to forward to the VM (prefix stripped in the path form).
function parseSession(uri: string, params: URLSearchParams): { sessionId: string; forwardUri: string } {
  const m = PATH_RE.exec(uri);
  if (m) return { sessionId: m[1], forwardUri: m[2] ?? "/" };
  return { sessionId: params.get("session") ?? "", forwardUri: uri };
}

export async function handleRequest(
  request: CloudFrontRequest,
  lookup: (sessionId: string) => Promise<Session | undefined>,
  now: number = Date.now(),
): Promise<CloudFrontRequestResult> {
  const params = new URLSearchParams(request.querystring);
  const { sessionId, forwardUri } = parseSession(request.uri, params);
  if (!SESSION_RE.test(sessionId)) return reply("400", "Bad Request", "missing or invalid session id");

  let session: Session | undefined;
  try {
    session = await lookup(sessionId);
  } catch (err) {
    console.error("session lookup failed", { sessionId, err });
    return reply("503", "Service Unavailable", "session lookup failed");
  }

  const retried = params.has("_attempt"); // any value: a crafted _attempt=0 can't bypass the guard
  params.delete("_attempt"); // loop-guard marker, never forwarded to the VM

  if (session?.token && (session.tokenExpiresAt ?? 0) - now > MARGIN_MS) {
    request.uri = forwardUri;
    request.querystring = params.toString();
    // Point the request at the MicroVM. Host does NOT follow an origin override, and the
    // MicroVM endpoint is virtual-hosted: a mismatched Host fails token auth. Drop the
    // config headers (see lambda.ts) so they aren't forwarded to the VM.
    request.origin!.custom!.domainName = session.endpoint;
    request.origin!.custom!.customHeaders = {};
    request.headers["host"] = [{ key: "Host", value: session.endpoint }];
    request.headers["x-aws-proxy-auth"] = [{ key: "X-aws-proxy-auth", value: session.token }];
    request.headers["x-aws-proxy-port"] = [{ key: "X-aws-proxy-port", value: "8080" }];
    return request;
  }

  // Not usable. Control already ran once (it added _attempt=1) and it's STILL not usable
  // -> stop redirecting rather than loop forever.
  if (retried) return reply("503", "Service Unavailable", "provisioning did not converge");

  // Bounce to the control plane, which launches the VM and redirects back here.
  const original = request.querystring ? `${request.uri}?${request.querystring}` : request.uri;
  const location = `/_control?session=${encodeURIComponent(sessionId)}&return=${encodeURIComponent(original)}`;
  return {
    status: "307",
    statusDescription: "Temporary Redirect",
    headers: { location: [{ key: "Location", value: location }], ...noStore },
  };
}
