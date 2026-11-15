"""Multi-tenant OpenClaw orchestrator on Lambda MicroVMs — Router + Worker + Sweeper.

One Lambda, three roles selected by event shape:
  - Function URL HTTP event      -> ROUTER (fast: ACK Telegram in <1s, hand off to worker)
  - {"_worker": {...}}           -> WORKER (async self-invoke: ensure VM, run turn, reply;
                                    turns outliving one invocation relay to a successor
                                    via {"_worker": {"resume": ...}} — see stream_turn_to_telegram)
  - {"_sweeper": true} (EventBridge) -> SWEEPER (reap idle, reconcile)

Registry (DynamoDB): tenantId -> microvmId, endpoint, generation, state, launchedAt,
lastActiveAt, botToken(optional), webhookSecret(optional).

State lifecycle: a tenant's VM is disposable; state lives on per-tenant EFS subdir.
Router NEVER proactively renews (see design-orchestrator.md). Two branches only:
alive -> forward; dead -> cold-start.
"""
import json
import os
import time
import urllib.error
import urllib.parse
import urllib.request

import boto3
from boto3.dynamodb.conditions import Attr

REGION = os.environ["AWS_REGION"]
TABLE = os.environ["TENANTS_TABLE"]
FN_NAME = os.environ["AWS_LAMBDA_FUNCTION_NAME"]
IMAGE_ARN = os.environ["IMAGE_ARN"]
IMAGE_VERSION = os.environ["IMAGE_VERSION"]
EXEC_ROLE_ARN = os.environ["EXEC_ROLE_ARN"]
INGRESS = os.environ["INGRESS_CONNECTOR"]
EGRESS = os.environ["EGRESS_CONNECTOR"]
IDLE_REAP_SECONDS = int(os.environ.get("IDLE_REAP_SECONDS", "3600"))
# A turn that outlives one worker invocation is handed to a fresh one (chained
# self-invoke). 120 hops x ~4.5min (300s timeout) covers the VM's full 8h life.
MAX_TURN_HOPS = int(os.environ.get("MAX_TURN_HOPS", "120"))

mv = boto3.client("lambda-microvms", region_name=REGION)
lam = boto3.client("lambda", region_name=REGION)
ddb = boto3.resource("dynamodb", region_name=REGION).Table(TABLE)


# ---------- helpers ----------
def now() -> int:
    return int(time.time())


def get_tenant(tid):
    return ddb.get_item(Key={"tenantId": tid}).get("Item")


def mv_state(microvm_id):
    try:
        return mv.get_microvm(microvmIdentifier=microvm_id).get("state")
    except Exception:
        return None


def call_vm(endpoint, path, token, method="GET", body=None, port=8080, timeout=280):
    url = f"https://{endpoint}{path}"
    data = json.dumps(body).encode() if body is not None else None
    headers = {"X-aws-proxy-auth": token,
               "X-aws-proxy-port": str(port),
               "Content-Type": "application/json"}
    req = urllib.request.Request(url, data=data, method=method, headers=headers)
    with urllib.request.urlopen(req, timeout=timeout) as r:
        return r.status, r.read()


def run_turn(endpoint, token, text, session, attachments=None):
    """One agent turn via the sidecar. Images go as a POST body (too big for a URL)."""
    if attachments:
        st, body = call_vm(endpoint, "/chat", token, "POST",
                           {"m": text, "s": session, "attachments": attachments},
                           timeout=280)
    else:
        qs = urllib.parse.urlencode({"m": text, "s": session})
        st, body = call_vm(endpoint, f"/chat?{qs}", token, timeout=280)
    return st, body


def mint_token(microvm_id):
    # Only the sidecar (8080) is reachable through the proxy; the OpenClaw gateway
    # (18789) stays loopback-only inside the VM.
    r = mv.create_microvm_auth_token(
        microvmIdentifier=microvm_id, expirationInMinutes=55,
        allowedPorts=[{"port": 8080}])
    return r["authToken"]["X-aws-proxy-auth"]


def tg_send(bot_token, chat_id, text):
    data = urllib.parse.urlencode({"chat_id": chat_id, "text": text[:4000]}).encode()
    with urllib.request.urlopen(
            f"https://api.telegram.org/bot{bot_token}/sendMessage", data, timeout=20) as r:
        body = json.loads(r.read())
        print(f"[worker] tg_send ok={body.get('ok')} "
              f"message_id={body.get('result', {}).get('message_id')} chat={chat_id}", flush=True)
        return body


def tg_typing(bot_token, chat_id):
    try:
        data = urllib.parse.urlencode({"chat_id": chat_id, "action": "typing"}).encode()
        urllib.request.urlopen(
            f"https://api.telegram.org/bot{bot_token}/sendChatAction", data, timeout=10)
    except Exception:
        pass


def tg_send_placeholder(bot_token, chat_id):
    """Send the placeholder that streaming edits will grow. Returns message_id or None."""
    try:
        data = urllib.parse.urlencode({"chat_id": chat_id, "text": "…"}).encode()
        with urllib.request.urlopen(
                f"https://api.telegram.org/bot{bot_token}/sendMessage", data, timeout=20) as r:
            return json.loads(r.read()).get("result", {}).get("message_id")
    except Exception as e:
        print(f"[worker] placeholder send failed: {e}", flush=True)
        return None


def tg_edit(bot_token, chat_id, message_id, text):
    """Edit a message in place. Telegram rejects edits with unchanged text — skip those."""
    try:
        data = urllib.parse.urlencode({
            "chat_id": chat_id, "message_id": message_id, "text": text[:4000]}).encode()
        urllib.request.urlopen(
            f"https://api.telegram.org/bot{bot_token}/editMessageText", data, timeout=20)
        return True
    except urllib.error.HTTPError as e:
        print(f"[worker] edit failed: {e} body={e.read()[:200]}", flush=True)
        return False
    except Exception as e:
        print(f"[worker] edit failed: {e}", flush=True)
        return False


def stream_turn_to_telegram(endpoint, token, text, session, attachments,
                            bot, chat_id, tid, ctx, resume=None):
    """Pseudo-streaming: async turn + poll /progress, growing one Telegram message.

    Telegram has no true streaming — the standard technique is a placeholder
    message repeatedly edited via editMessageText (~1 edit/sec/chat allowed;
    we edit every ~2s). Falls back to the sync path if the async start fails.

    A turn that outlives this Lambda invocation is NOT lost: just before the
    invocation times out, polling is handed to a fresh async self-invoke
    (carrying turnId + message state), the same chaining the router uses for
    the webhook handoff. Returns None on handoff — the successor owns delivery.
    A single turn is thus bounded by the VM's 8h lifetime, not Lambda's 15 min.
    """
    if resume:
        turn_id = resume["turnId"]
        msg_id = resume.get("msgId")
        last_len = int(resume.get("lastLen", 0))
        hops = int(resume.get("hops", 0))
    else:
        st, body = call_vm(endpoint, "/chat-async", token, "POST",
                           {"m": text, "s": session, "attachments": attachments or []},
                           timeout=30)
        turn_id = json.loads(body).get("turnId")
        if not turn_id:
            raise RuntimeError("no turnId from /chat-async")
        msg_id = tg_send_placeholder(bot, chat_id)
        last_len, hops = 0, 0

    reply = None
    # 1.2s ≈ Telegram's per-chat edit ceiling (~1/s) with headroom; a failed
    # edit (e.g. 429) leaves last_len unchanged so the next cycle retries.
    while True:
        # Hand off before this invocation's timeout would silently kill polling.
        # 20s leaves room for one in-flight poll + the invoke round-trip.
        if ctx.get_remaining_time_in_millis() < 20_000:
            if hops + 1 >= MAX_TURN_HOPS:
                reply = "(turn exceeded the relay budget — increase MAX_TURN_HOPS)"
                break
            lam.invoke(FunctionName=FN_NAME, InvocationType="Event",
                       Payload=json.dumps({"_worker": {"tenantId": tid, "resume": {
                           "turnId": turn_id, "chatId": chat_id, "msgId": msg_id,
                           "lastLen": last_len, "hops": hops + 1}}}).encode())
            print(f"[worker] turn {turn_id} handed off (hop {hops + 1})", flush=True)
            return None
        time.sleep(1.2)
        try:
            st, body = call_vm(endpoint, f"/progress?id={turn_id}", token, timeout=15)
            prog = json.loads(body)
        except urllib.error.HTTPError as e:
            if e.code == 404:
                # Bridge no longer knows the turn (VM replaced / bridge restarted
                # mid-turn) — retrying or relaying can never recover it.
                reply = "(turn lost — the VM was replaced mid-turn, please retry)"
                break
            continue
        except Exception:
            continue
        if prog.get("done"):
            reply = prog.get("reply") or prog.get("text") or "(no reply)"
            if prog.get("error"):
                reply = "(agent error — try again)"
            break
        cur = prog.get("text") or ""
        # Grow the placeholder with partial text; "▌" cursor marks in-progress.
        # Stop editing once past Telegram's 4096-char message cap: tg_edit
        # truncates, so further edits would be byte-identical -> 400 spam.
        if msg_id and len(cur) > last_len and last_len < 3990:
            if tg_edit(bot, chat_id, msg_id, cur + " ▌"):
                last_len = len(cur)
    if msg_id:
        tg_edit(bot, chat_id, msg_id, reply)
    else:
        tg_send(bot, chat_id, reply)
    return reply


def tg_fetch_image(bot_token, file_id, max_bytes=4_500_000):
    """Download a Telegram file and return (base64, media_type), or (None, None).

    Caps at ~4.5MB — Bedrock's per-image limit is 5MB and Telegram photos
    (recompressed JPEG) are far smaller; the cap only bites on image documents.
    """
    import base64
    import mimetypes
    try:
        with urllib.request.urlopen(
                f"https://api.telegram.org/bot{bot_token}/getFile?file_id="
                + urllib.parse.quote(file_id), timeout=20) as r:
            path = json.loads(r.read())["result"]["file_path"]
        with urllib.request.urlopen(
                f"https://api.telegram.org/file/bot{bot_token}/{path}", timeout=60) as r:
            data = r.read(max_bytes + 1)
        if len(data) > max_bytes:
            print(f"[worker] image too large ({len(data)}B), skipped", flush=True)
            return None, None
        media_type = mimetypes.guess_type(path)[0] or "image/jpeg"
        return base64.b64encode(data).decode(), media_type
    except Exception as e:
        print(f"[worker] tg_fetch_image failed: {e}", flush=True)
        return None, None


def extract_content(msg, bot):
    """Pull text + image attachments out of a Telegram message.

    Photos live in msg.photo[] (sizes ascending; last is largest) with the
    user's text in msg.caption — there is NO msg.text on media messages.
    Image documents (sent as files) come via msg.document with an image/* mime.
    """
    text = msg.get("text", "") or msg.get("caption", "")
    attachments = []
    if bot:
        photos = msg.get("photo") or []
        if photos:
            b64, mt = tg_fetch_image(bot, photos[-1]["file_id"])
            if b64:
                attachments.append({"media_type": mt, "data": b64})
        doc = msg.get("document") or {}
        if (doc.get("mime_type") or "").startswith("image/"):
            b64, _ = tg_fetch_image(bot, doc["file_id"])
            if b64:
                attachments.append({"media_type": doc["mime_type"], "data": b64})
    if attachments and not text:
        text = "(the user sent this image with no caption — look at it and respond)"
    return text, attachments


# ---------- cold start (single-writer lock via conditional update) ----------
def cold_start(tid, item):
    gen = int(item.get("generation", 0)) + 1
    # Lock: only one launcher may flip state PENDING for this generation.
    try:
        ddb.update_item(
            Key={"tenantId": tid},
            UpdateExpression="SET #s=:p, generation=:g, launchedAt=:t",
            ConditionExpression=Attr("state").ne("LAUNCHING"),
            ExpressionAttributeNames={"#s": "state"},
            ExpressionAttributeValues={":p": "LAUNCHING", ":g": gen, ":t": now()})
    except Exception:
        # Another invocation is already launching; wait for it to publish endpoint.
        for _ in range(40):
            time.sleep(3)
            it = get_tenant(tid)
            if it and it.get("state") == "RUNNING" and it.get("endpoint"):
                return it
        raise RuntimeError("concurrent launch did not converge")

    r = mv.run_microvm(
        imageIdentifier=IMAGE_ARN, imageVersion=IMAGE_VERSION,
        executionRoleArn=EXEC_ROLE_ARN,
        ingressNetworkConnectors=[INGRESS],
        egressNetworkConnectors=[EGRESS],
        idlePolicy={"autoResumeEnabled": True, "maxIdleDurationSeconds": 900,
                    "suspendedDurationSeconds": 3600},
        maximumDurationInSeconds=28800)
    microvm_id, endpoint = r["microvmId"], r["endpoint"]

    # wait RUNNING
    for _ in range(40):
        if mv_state(microvm_id) == "RUNNING":
            break
        time.sleep(3)
    token = mint_token(microvm_id)

    # assign tenant -> unblocks efs-monitor -> mounts per-tenant subdir -> bounces gateway
    for _ in range(20):
        try:
            call_vm(endpoint, "/tenant", token, "POST", {"tenantId": tid}, timeout=15)
            break
        except Exception:
            time.sleep(3)

    # gate on EFS adoption + gateway healthy
    ready = False
    for _ in range(40):
        try:
            st, body = call_vm(endpoint, "/health", token, timeout=15)
            h = json.loads(body)
            if h.get("efsReady") and h.get("healthz") == 200:
                ready = True
                break
        except Exception:
            pass
        time.sleep(3)

    item = {**item, "tenantId": tid, "microvmId": microvm_id, "endpoint": endpoint,
            "generation": gen, "state": "RUNNING", "launchedAt": now(),
            "lastActiveAt": now(), "authToken": token}
    ddb.put_item(Item=item)
    if not ready:
        raise RuntimeError("cold start: VM did not become EFS-ready")
    return item


def ensure_vm(tid, item):
    """Two-branch decision: alive -> reuse; dead -> cold start."""
    mid = item.get("microvmId")
    state = mv_state(mid) if mid else None
    if state in ("RUNNING", "SUSPENDED"):
        # alive (SUSPENDED auto-resumes on the forwarded request)
        return item, False
    return cold_start(tid, item), True


# ---------- WORKER (async) ----------
def resume_turn(payload, ctx):
    """Successor invocation in a turn relay: keep polling an in-flight turn."""
    tid = payload["tenantId"]
    resume = payload["resume"]
    item = get_tenant(tid)
    bot, chat_id = item.get("botToken"), resume["chatId"]
    try:
        endpoint = item["endpoint"]
        token = mint_token(item["microvmId"])
    except Exception as e:
        # VM died mid-turn (e.g. hit its 8h max lifetime) — tell the user
        # instead of failing silently.
        print(f"[worker] resume for {tid} found no live VM: {e}", flush=True)
        note = "(turn lost — the VM ended mid-turn, please retry)"
        if resume.get("msgId"):
            tg_edit(bot, chat_id, resume["msgId"], note)
        else:
            tg_send(bot, chat_id, note)
        return {"tenant": tid, "resumed": False, "error": "vm gone"}
    reply = stream_turn_to_telegram(endpoint, token, None, None, None,
                                    bot, chat_id, tid, ctx, resume=resume)
    if reply is None:
        return {"tenant": tid, "handedOff": True}
    ddb.update_item(Key={"tenantId": tid},
                    UpdateExpression="SET lastActiveAt=:t",
                    ExpressionAttributeValues={":t": now()})
    return {"tenant": tid, "resumed": True, "reply": reply[:80]}


def worker(payload, ctx):
    tid = payload["tenantId"]
    update = payload["update"]
    item = get_tenant(tid)
    bot = item.get("botToken")
    msg = update.get("message") or {}
    chat_id = str((msg.get("chat") or {}).get("id", ""))
    text, attachments = extract_content(msg, bot)
    if not text or not chat_id:
        return {"skipped": "no content/chat"}

    # Telegram chat ids are numeric; chat.sh passes a session string (e.g. "cli")
    # here. Only numeric ids go down the Telegram send/edit path — otherwise a
    # Telegram-enabled tenant crashes every chat.sh turn on sendMessage 400.
    is_tg = bool(bot) and chat_id.lstrip("-").isdigit()
    if is_tg:
        tg_typing(bot, chat_id)

    item, cold = ensure_vm(tid, item)
    endpoint = item["endpoint"]
    # Always mint a fresh token per turn: token TTL (<=60min) < VM lifetime (8h),
    # so a cached token from cold-start time is often already expired -> 403.
    token = mint_token(item["microvmId"])

    session = f"tg-{chat_id}"
    if is_tg:
        # Telegram path: pseudo-stream via placeholder + editMessageText.
        try:
            reply = stream_turn_to_telegram(
                endpoint, token, text, session, attachments, bot, chat_id,
                tid, ctx)
            if reply is None:
                # Turn outlived this invocation; a chained self-invoke now owns
                # polling + delivery. lastActiveAt is updated by the last hop.
                return {"tenant": tid, "cold": cold, "handedOff": True}
        except Exception as e:
            # Streaming plumbing failed (old image, bridge restart, ...):
            # fall back to the sync turn + single send.
            print(f"[worker] stream path failed ({e}); falling back to sync", flush=True)
            st, body = run_turn(endpoint, token, text, session, attachments)
            d = json.loads(body)
            reply = " ".join(p.get("text", "") for p in
                             d.get("result", {}).get("payloads", [])) or "(no reply)"
            tg_send(bot, chat_id, reply)
    else:
        # No bot token (chat.sh / HTTP test path): synchronous turn, unchanged.
        st, body = run_turn(endpoint, token, text, session, attachments)
        d = json.loads(body)
        reply = " ".join(p.get("text", "") for p in
                         d.get("result", {}).get("payloads", [])) or "(no reply)"
    ddb.update_item(Key={"tenantId": tid},
                    UpdateExpression="SET lastActiveAt=:t",
                    ExpressionAttributeValues={":t": now()})
    return {"tenant": tid, "cold": cold, "reply": reply[:80]}


# ---------- ROUTER (Function URL) ----------
def router(event):
    raw = event.get("rawPath", "/")
    body = event.get("body") or ""
    if event.get("isBase64Encoded"):
        import base64
        body = base64.b64decode(body).decode()
    headers = {k.lower(): v for k, v in (event.get("headers") or {}).items()}

    # /tg/<tenantId>
    parts = [p for p in raw.split("/") if p]
    if len(parts) == 2 and parts[0] == "tg":
        tid = parts[1]
        item = get_tenant(tid)
        if not item:
            return {"statusCode": 404, "body": "unknown tenant"}
        # Verify the Telegram secret token. Fail closed: a Telegram-bound tenant
        # (one with a botToken) MUST present a matching secret. add-tenant.sh
        # enforces that such tenants are always registered with a webhookSecret,
        # so a missing 'want' here means a misconfigured tenant, not a public one.
        want = item.get("webhookSecret")
        got = headers.get("x-telegram-bot-api-secret-token")
        if item.get("botToken") and (not want or got != want):
            return {"statusCode": 403, "body": "bad secret"}
        update = json.loads(body or "{}")
        # hand off to worker asynchronously; ACK Telegram immediately
        lam.invoke(FunctionName=FN_NAME, InvocationType="Event",
                   Payload=json.dumps({"_worker": {"tenantId": tid, "update": update}}).encode())
        return {"statusCode": 200, "body": "ok"}

    # /chat/<tenantId>?m=... — synchronous test entry (no Telegram); ensures VM + runs a turn inline.
    #
    # SECURITY NOTE — this route is intentionally UNAUTHENTICATED for demo ergonomics.
    # It cold-starts a billable MicroVM and drives Bedrock inference, so an exposed
    # endpoint is a denial-of-wallet vector: anyone who learns the API URL + a tenant
    # id can run turns on your account. We deliberately keep it open here to make the
    # HTTP path trivially curl-testable in a throwaway demo stack.
    #   WHAT GOOD LOOKS LIKE (do this before any real/shared deployment):
    #     * put an Amazon API Gateway authorizer (IAM / JWT-Cognito / Lambda authorizer)
    #       in front of the HTTP API, OR
    #     * require a per-tenant shared-secret header here, mirroring the /tg check
    #       (e.g. compare headers['x-chat-secret'] to a value stored on the tenant),
    #     * and/or drop this route entirely and test only via chat.sh, which invokes
    #       the Lambda directly (aws lambda invoke) and never touches this public path.
    # The documented test flow (chat.sh) uses the direct-invoke path, so removing or
    # locking down /chat does NOT break the pattern's happy path. See README "Security".
    if len(parts) == 2 and parts[0] == "chat":
        tid = parts[1]
        item = get_tenant(tid)
        if not item:
            return {"statusCode": 404, "body": "unknown tenant"}
        qs = urllib.parse.parse_qs(event.get("rawQueryString", ""))
        msg = (qs.get("m") or ["Say pong"])[0]
        sess = (qs.get("s") or ["http-demo"])[0]
        try:
            item, cold = ensure_vm(tid, item)
            token = mint_token(item["microvmId"])  # fresh per call (see worker note)
            q2 = urllib.parse.urlencode({"m": msg, "s": sess})
            st, body = call_vm(item["endpoint"], f"/chat?{q2}", token, timeout=280)
            ddb.update_item(Key={"tenantId": tid},
                            UpdateExpression="SET lastActiveAt=:t",
                            ExpressionAttributeValues={":t": now()})
            d = json.loads(body)
            reply = " ".join(p.get("text", "") for p in
                             d.get("result", {}).get("payloads", [])) or body.decode()[:200]
            return {"statusCode": 200, "body": json.dumps({"tenant": tid, "cold": cold, "reply": reply})}
        except Exception as e:
            return {"statusCode": 500, "body": json.dumps({"error": str(e)})}

    if raw == "/health":
        return {"statusCode": 200, "body": json.dumps({"ok": True, "role": "router"})}
    return {"statusCode": 404, "body": "not found"}


# ---------- SWEEPER (EventBridge) ----------
def scan_all_tenants():
    """Yield every tenant, paging past DynamoDB's 1 MB-per-Scan limit.

    A single Scan returns at most 1 MB; without this loop the sweeper would only
    ever see the first page and silently stop reaping/reconciling the rest, leaking
    idle MicroVMs (and their cost) once the registry outgrows one page.
    """
    kwargs = {}
    while True:
        resp = ddb.scan(**kwargs)
        yield from resp.get("Items", [])
        lek = resp.get("LastEvaluatedKey")
        if not lek:
            break
        kwargs["ExclusiveStartKey"] = lek


def sweeper():
    reaped, reconciled = [], []
    for item in scan_all_tenants():
        tid, mid = item["tenantId"], item.get("microvmId")
        if not mid:
            continue
        state = mv_state(mid)
        if state is None or state == "TERMINATED":
            if item.get("state") != "COLD":
                ddb.update_item(Key={"tenantId": tid},
                                UpdateExpression="SET #s=:c",
                                ExpressionAttributeNames={"#s": "state"},
                                ExpressionAttributeValues={":c": "COLD"})
                reconciled.append(tid)
            continue
        idle = now() - int(item.get("lastActiveAt", 0))
        if state == "SUSPENDED" and idle > IDLE_REAP_SECONDS:
            try:
                mv.terminate_microvm(microvmIdentifier=mid)
                ddb.update_item(Key={"tenantId": tid},
                                UpdateExpression="SET #s=:c",
                                ExpressionAttributeNames={"#s": "state"},
                                ExpressionAttributeValues={":c": "COLD"})
                reaped.append(tid)
            except Exception as e:
                # Don't drop silently: a failed reap (permissions, throttling) leaves
                # a billable VM running and the registry unreconciled — surface it.
                print(f"[sweeper] terminate failed for {tid}: {e}", flush=True)
    return {"reaped": reaped, "reconciled": reconciled}


def handler(event, context):
    if isinstance(event, dict) and "_worker" in event:
        if "resume" in event["_worker"]:
            return resume_turn(event["_worker"], context)
        return worker(event["_worker"], context)
    if isinstance(event, dict) and event.get("_sweeper"):
        return sweeper()
    if isinstance(event, dict) and ("rawPath" in event or "requestContext" in event):
        return router(event)
    return {"statusCode": 400, "body": "unrecognized event"}
