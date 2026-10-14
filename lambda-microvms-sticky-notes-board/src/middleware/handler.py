"""
Session middleware Lambda for the Sticky Notes Board.

Exposed via an API Gateway HTTP API (payload format v2.0). The browser UI calls
this instead of talking to the MicroVM control plane directly, so it never needs
AWS credentials — it only ever handles a clientId and the auth token the
middleware returns.

Routes (method + path from the API Gateway v2 event):

  POST   /session           Open the interface for a clientId. Reuses the
                            running MicroVM if it is still alive and its token
                            is valid; otherwise launches a fresh MicroVM (which
                            restores the client's notes+files from S3 via the
                            /run hook), mints a token, and persists the session.
                            -> { endpoint, authToken, microvmId, port, restored }

  POST   /session/token     Mint a fresh auth token for the current MicroVM.
                            -> { authToken, port }

  POST   /session/close     Mark the session closed (keeps the DynamoDB record
                            so the next open restores). Does NOT terminate.

  DELETE /session           Terminate the MicroVM (state flushes to S3 via the
                            /terminate hook) and mark the session closed.

  ANY    /api/{proxy+}      Reverse-proxy to the client's MicroVM. The browser
                            never talks to the MicroVM directly (that endpoint
                            has no browser-usable CORS); it calls the API Gateway
                            origin only. The clientId travels in the X-Client-Id
                            header. Everything after /api is forwarded as-is to
                            the MicroVM app (e.g. /api/notes -> MicroVM /notes),
                            with the auth token injected server-side.

Request body for /session routes (JSON): { "clientId": "<id>" }
Proxy routes carry the clientId in the X-Client-Id header instead.

Environment:
  SESSIONS_TABLE     DynamoDB table name (default "microvm-sessions")
  IMAGE_ARN          MicroVM image ARN to launch
  IMAGE_VERSION      MicroVM image version (default "1.0")
  EXECUTION_ROLE_ARN execution role for launched MicroVMs
  STATE_BUCKET       S3 bucket backing notes + files
  TOKEN_TTL_MINUTES  auth-token lifetime (default "30")
"""

from __future__ import annotations

import base64
import json
import logging
import os
import time
import urllib.error
import urllib.parse
import urllib.request

from middleware import session_store as sessions
from middleware import microvm_control as mvm

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("session-middleware")

IMAGE_ARN = os.environ.get("IMAGE_ARN", "")
IMAGE_VERSION = os.environ.get("IMAGE_VERSION", "1.0")
EXECUTION_ROLE_ARN = os.environ.get("EXECUTION_ROLE_ARN", "")
STATE_BUCKET = os.environ.get("STATE_BUCKET", "")
TOKEN_TTL_MINUTES = int(os.environ.get("TOKEN_TTL_MINUTES", "30"))
APP_PORT = int(os.environ.get("APP_PORT", "8080"))
# Hard cap on concurrently live MicroVMs. Launching is refused once this many
# sessions are "running", so abuse of this (demo-unauthenticated) endpoint can't
# spin up unbounded billable MicroVMs. 0 disables the cap.
MAX_LIVE_MICROVMS = int(os.environ.get("MAX_LIVE_MICROVMS", "10"))

# CORS headers returned on every response. The browser only ever sees this
# API Gateway origin, so these are the only CORS headers that matter.
CORS_HEADERS = {
    "Access-Control-Allow-Origin": "*",
    "Access-Control-Allow-Methods": "GET, POST, PUT, DELETE, OPTIONS",
    "Access-Control-Allow-Headers": "Content-Type, X-Client-Id, X-File-Name",
}

# Max body we are willing to proxy (API Gateway hard-caps payloads at ~10 MB,
# so keep uploads under that when routed through the middleware).
MAX_PROXY_BYTES = 9 * 1024 * 1024


# --------------------------------------------------------------------------
# Lambda entrypoint
# --------------------------------------------------------------------------

def lambda_handler(event, context):
    method, path = _route(event)
    logger.info("Request: %s %s", method, path)

    if method == "OPTIONS":
        return _resp(204, {})

    try:
        # Reverse-proxy everything under /api to the client's MicroVM.
        if "/api" in path:
            return proxy_to_microvm(event, method, path)

        # Session-control routes take the clientId in the JSON body.
        body = _parse_body(event)
        client_id = (body.get("clientId") or "").strip()
        if not client_id:
            return _resp(400, {"error": "clientId is required"})

        if method == "POST" and path.endswith("/session"):
            return open_session(client_id)
        if method == "POST" and path.endswith("/session/token"):
            return refresh_token(client_id)
        if method == "POST" and path.endswith("/session/close"):
            return close_session(client_id)
        if method == "DELETE" and path.endswith("/session"):
            return terminate_session(client_id)

        return _resp(404, {"error": f"No route for {method} {path}"})
    except CapacityExceeded as e:
        # 429 so clients (and any abuse) back off instead of retrying hard.
        return _resp(429, {"error": str(e)})
    except Exception as e:  # pragma: no cover - surface errors as 500 JSON
        logger.exception("Unhandled error")
        return _resp(500, {"error": str(e)})


# --------------------------------------------------------------------------
# Route handlers
# --------------------------------------------------------------------------

# A MicroVM in any of these states can still serve the user: RUNNING directly,
# SUSPENDED/SUSPENDING resumes transparently on ingress (autoResumeEnabled),
# PENDING is still coming up. Only a terminal state means we must relaunch.
REUSABLE_STATES = {"PENDING", "RUNNING", "SUSPENDING", "SUSPENDED"}


class CapacityExceeded(Exception):
    """Raised when launching a new MicroVM would exceed MAX_LIVE_MICROVMS."""


def open_session(client_id: str):
    if not (IMAGE_ARN and EXECUTION_ROLE_ARN and STATE_BUCKET):
        return _resp(500, {"error": "Middleware not configured: IMAGE_ARN / "
                                    "EXECUTION_ROLE_ARN / STATE_BUCKET must be set"})

    resolved, reused = _resolve_microvm(client_id)
    if resolved is None:
        return _resp(503, {"error": "Could not establish a MicroVM session"})

    return _resp(200, {
        "endpoint": resolved["endpoint"],
        "authToken": resolved["authToken"],
        "microvmId": resolved["microvmId"],
        "port": APP_PORT,
        # restored=True means a prior session existed and we relaunched (state
        # pulled from S3 by the /run hook); reused=True means we reconnected to
        # the still-existing MicroVM (running or resumed from suspend).
        "restored": resolved.get("restored", False),
        "reused": reused,
    })


def _resolve_microvm(client_id: str) -> tuple[dict | None, bool]:
    """
    Core reuse-or-relaunch decision, shared by open_session and the proxy.

    Reuses the client's existing MicroVM whenever the control plane reports it
    in a non-terminal state (RUNNING/SUSPENDED/SUSPENDING/PENDING) — a suspended
    MicroVM resumes transparently when ingress traffic arrives. Only launches a
    new MicroVM when there is no prior record or the previous one is terminated.

    Returns (resolved, reused) where resolved is
    {endpoint, authToken, microvmId, restored} or None on failure.
    """
    session = sessions.get_session(client_id)

    if session and session.get("microvmId"):
        microvm_id = session["microvmId"]
        info = mvm.get_microvm(microvm_id)
        state = info["state"] if info else "TERMINATED"
        if info and state in REUSABLE_STATES:
            # Prefer the control-plane endpoint (authoritative), fall back to
            # the stored one.
            endpoint = info.get("endpoint") or session.get("endpoint", "")
            # Ensure a valid token; mint a fresh one if stale/expiring.
            if sessions.token_is_valid(session) and session.get("authToken"):
                auth_token = session["authToken"]
                expires_at = int(session.get("authExpiresAt", 0))
            else:
                token = mvm.create_auth_token(microvm_id, TOKEN_TTL_MINUTES)
                auth_token = token["token"]
                expires_at = int(time.time()) + token["expiresInMinutes"] * 60
            # Persist (and flip status back to "running" if a prior
            # Switch-workspace had closed it), keeping the same MicroVM.
            sessions.put_session(
                client_id=client_id,
                microvm_id=microvm_id,
                endpoint=endpoint,
                auth_token=auth_token,
                auth_expires_at=expires_at,
                image_arn=session.get("imageArn", IMAGE_ARN),
                state_bucket=session.get("stateBucket", STATE_BUCKET),
                status="running",
            )
            logger.info("Reusing MicroVM %s for %s (state=%s)", microvm_id, client_id, state)
            return {
                "endpoint": endpoint,
                "authToken": auth_token,
                "microvmId": microvm_id,
                "restored": False,
            }, True
        # The stored MicroVM is gone/terminal. Mark the session closed now so it
        # stops counting toward MAX_LIVE_MICROVMS (e.g. when the platform's idle
        # policy terminated it without a DELETE /session call).
        sessions.mark_closed(client_id)
        logger.info("MicroVM %s for %s is %s -> relaunching", microvm_id, client_id, state)

    # No reusable MicroVM -> launch a fresh one. State restores from S3 in /run.
    if not (IMAGE_ARN and EXECUTION_ROLE_ARN and STATE_BUCKET):
        return None, False

    # Enforce the hard cap on concurrently live MicroVMs before launching. This
    # bounds billable MicroVMs if the (demo-unauthenticated) endpoint is abused
    # with a flood of fabricated clientIds. A production authorizer is still the
    # primary control; this is the backstop. Set MAX_LIVE_MICROVMS=0 to disable.
    if MAX_LIVE_MICROVMS > 0:
        running = sessions.count_running()
        if running == sessions.COUNT_UNKNOWN:
            # GSI still backfilling (brief, right after stack creation). Can't
            # evaluate the cap; allow the launch rather than 500. Throttling and
            # reserved concurrency still bound the blast radius.
            logger.warning("Running-session count unavailable (GSI backfilling); "
                           "skipping cap check for %s", client_id)
        elif running >= MAX_LIVE_MICROVMS:
            logger.warning(
                "Refusing launch for %s: %d running MicroVMs >= cap %d",
                client_id, running, MAX_LIVE_MICROVMS,
            )
            raise CapacityExceeded(
                f"MicroVM capacity reached ({running}/{MAX_LIVE_MICROVMS} running)"
            )

    logger.info("Launching new MicroVM for %s", client_id)
    launched = mvm.run_microvm(
        image_arn=IMAGE_ARN,
        image_version=IMAGE_VERSION,
        execution_role_arn=EXECUTION_ROLE_ARN,
        client_id=client_id,
        state_bucket=STATE_BUCKET,
    )
    token = mvm.create_auth_token(launched["microvmId"], TOKEN_TTL_MINUTES)
    expires_at = int(time.time()) + token["expiresInMinutes"] * 60
    sessions.put_session(
        client_id=client_id,
        microvm_id=launched["microvmId"],
        endpoint=launched["endpoint"],
        auth_token=token["token"],
        auth_expires_at=expires_at,
        image_arn=IMAGE_ARN,
        state_bucket=STATE_BUCKET,
        status="running",
    )
    return {
        "endpoint": launched["endpoint"],
        "authToken": token["token"],
        "microvmId": launched["microvmId"],
        "restored": bool(session),  # relaunch of a prior session vs. brand new
    }, False


def refresh_token(client_id: str):
    session = sessions.get_session(client_id)
    if not session or session.get("status") != "running":
        return _resp(404, {"error": "No running session for clientId"})
    token = mvm.create_auth_token(session["microvmId"], TOKEN_TTL_MINUTES)
    expires_at = int(time.time()) + token["expiresInMinutes"] * 60
    sessions.update_token(client_id, token["token"], expires_at)
    return _resp(200, {"authToken": token["token"], "port": APP_PORT})


def close_session(client_id: str):
    # Just record that the UI closed. The MicroVM's own idle policy will
    # suspend/terminate it eventually, flushing state to S3. We keep the record
    # so the next open() can relaunch and restore.
    if sessions.get_session(client_id):
        sessions.mark_closed(client_id)
    return _resp(200, {"status": "closed"})


def terminate_session(client_id: str):
    session = sessions.get_session(client_id)
    if session and session.get("microvmId"):
        mvm.terminate_microvm(session["microvmId"])
        sessions.mark_closed(client_id)
    return _resp(200, {"status": "terminated"})


# --------------------------------------------------------------------------
# Reverse proxy to the MicroVM
# --------------------------------------------------------------------------

def _ensure_live_session(client_id: str) -> dict | None:
    """
    Return {endpoint, authToken, microvmId} for the client, reusing an existing
    (running or suspended) MicroVM or launching a fresh one. Thin wrapper over
    _resolve_microvm so the proxy and open_session share one decision path.
    """
    resolved, _ = _resolve_microvm(client_id)
    return resolved


def proxy_to_microvm(event, method: str, path: str):
    """
    Forward a request under /api to the client's MicroVM and relay the response.

    The browser calls, e.g., `POST {api}/api/notes` with header X-Client-Id.
    We strip the `/api` prefix and forward to `https://{endpoint}/notes` with
    the server-held X-aws-proxy-auth token. Binary responses (file downloads)
    are relayed base64-encoded.
    """
    client_id = _header(event, "x-client-id").strip()
    if not client_id:
        return _resp(400, {"error": "X-Client-Id header is required"})

    session = _ensure_live_session(client_id)
    if not session:
        return _resp(503, {"error": "Could not establish a MicroVM session"})

    # Map /api/<rest> (optionally with the stage prefix already stripped) to
    # the MicroVM path /<rest>, preserving the query string.
    idx = path.find("/api")
    sub_path = path[idx + len("/api"):] or "/"
    if not sub_path.startswith("/"):
        sub_path = "/" + sub_path
    # API Gateway delivers the path already URL-decoded, so a filename like
    # "Tag itau.pdf" arrives with a literal space. Re-encode each segment
    # (keeping the "/" separators) before building the target URL, otherwise
    # urllib rejects it: "URL can't contain control characters".
    sub_path = "/".join(urllib.parse.quote(seg, safe="") for seg in sub_path.split("/"))
    qs = event.get("rawQueryString") or ""
    target = f"https://{session['endpoint']}{sub_path}"
    if qs:
        target += "?" + qs

    # Request body (may be base64 for binary uploads).
    raw = event.get("body")
    data = None
    if raw is not None and method in ("POST", "PUT", "PATCH"):
        data = base64.b64decode(raw) if event.get("isBase64Encoded") else raw.encode("utf-8")
        if len(data) > MAX_PROXY_BYTES:
            return _resp(413, {"error": "Payload too large to proxy (limit ~9 MB)"})

    # Forward select headers from the browser; always inject the auth token.
    fwd_headers = {"X-aws-proxy-auth": session["authToken"]}
    for h in ("content-type", "x-file-name"):
        v = _header(event, h)
        if v:
            fwd_headers[h.title() if h != "x-file-name" else "X-File-Name"] = v

    req = urllib.request.Request(target, data=data, method=method, headers=fwd_headers)
    try:
        # Below the function's 29s timeout so a slow MicroVM fails cleanly as a
        # 502 here, rather than the function being killed mid-request.
        with urllib.request.urlopen(req, timeout=25) as r:
            return _passthrough(r.status, r.headers.get("Content-Type", ""), r.read())
    except urllib.error.HTTPError as e:
        # Relay the MicroVM's own error response (e.g. 404 note not found).
        return _passthrough(e.code, e.headers.get("Content-Type", "application/json"), e.read())
    except Exception as e:
        logger.exception("Proxy to MicroVM failed")
        return _resp(502, {"error": f"Bad gateway: {e}"})


# --------------------------------------------------------------------------
# Helpers
# --------------------------------------------------------------------------

def _route(event) -> tuple[str, str]:
    # API Gateway v2 (HTTP API) payload format
    ctx = event.get("requestContext", {})
    http = ctx.get("http", {})
    method = http.get("method") or event.get("httpMethod") or "POST"
    path = http.get("path") or event.get("rawPath") or event.get("path") or "/session"
    return method, path


def _header(event, name: str) -> str:
    """Case-insensitive header lookup (API Gateway lowercases header keys)."""
    headers = event.get("headers") or {}
    name = name.lower()
    for k, v in headers.items():
        if k.lower() == name:
            return v or ""
    return ""


def _passthrough(status: int, content_type: str, body_bytes: bytes):
    """
    Relay a MicroVM response through API Gateway. Text content is returned as
    UTF-8; anything else is base64-encoded (isBase64Encoded) so binary file
    downloads survive the Lambda proxy integration.
    """
    headers = dict(CORS_HEADERS)
    headers["Content-Type"] = content_type or "application/octet-stream"
    is_text = content_type.startswith("text/") or content_type.startswith("application/json")
    if is_text:
        try:
            return {
                "statusCode": status,
                "headers": headers,
                "body": body_bytes.decode("utf-8"),
                "isBase64Encoded": False,
            }
        except UnicodeDecodeError:
            pass
    return {
        "statusCode": status,
        "headers": headers,
        "body": base64.b64encode(body_bytes).decode("ascii"),
        "isBase64Encoded": True,
    }


def _parse_body(event) -> dict:
    raw = event.get("body")
    if not raw:
        return {}
    if event.get("isBase64Encoded"):
        import base64
        raw = base64.b64decode(raw).decode("utf-8")
    try:
        return json.loads(raw)
    except (json.JSONDecodeError, TypeError):
        return {}


def _resp(status: int, body: dict):
    headers = dict(CORS_HEADERS)
    headers["Content-Type"] = "application/json"
    return {
        "statusCode": status,
        "headers": headers,
        "body": json.dumps(body),
    }
