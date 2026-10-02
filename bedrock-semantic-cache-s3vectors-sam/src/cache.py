"""Serverless semantic cache for Amazon Bedrock.
Embed the prompt -> query Amazon S3 Vectors for a semantically similar prior prompt ->
HIT (similarity >= threshold, fresh by TTL, and current epoch) return the cached response;
MISS -> call Amazon Bedrock, store {embedding + metadata}, return.
Force-invalidate: POST {"action":"invalidate"} bumps a global epoch held in AWS Systems
Manager Parameter Store -> every prior entry instantly becomes a miss. No deletes, no
scanning, O(1)."""
import json, os, re, time, uuid
import boto3

_NEG = {"not","no","never","without","cannot","nor","neither","none","cant","dont","doesnt","isnt","arent","wont","shouldnt","wasnt","werent","hasnt","havent","didnt","aint"}
def _has_negation(text):
    # ASCII English negation words only: the token regex drops every other token, and
    # stripping the apostrophe maps don't, isn't and so on onto the entries above.
    for t in re.findall(r"[a-z']+", (text or "").lower()):
        if t.replace("'","") in _NEG:
            return True
    return False

REGION = os.environ.get("AWS_REGION", "us-east-1")
BUCKET = os.environ["VECTOR_BUCKET"]
INDEX = os.environ["VECTOR_INDEX"]
EMBED_MODEL = os.environ.get("EMBED_MODEL", "amazon.titan-embed-text-v2:0")
# Fixed per deployment, never taken from the request body: the cache key is the prompt
# embedding alone, so a caller supplied model could be served an answer that a different
# model generated. Entries still record the model that produced them.
LLM_MODEL = os.environ.get("LLM_MODEL", "amazon.nova-lite-v1:0")
SIM_THRESHOLD = float(os.environ.get("SIM_THRESHOLD", "0.85"))
TTL_SECONDS = int(os.environ.get("TTL_SECONDS", "86400"))
API_KEY_PARAM = os.environ.get("API_KEY_PARAM", "")
EPOCH_PARAM = os.environ.get("EPOCH_PARAM", "/semantic-cache/epoch")

# Amazon S3 Vectors allows up to 40 KB of metadata per vector (filterable plus
# non-filterable), so an oversized prompt and answer pair cannot be cached.
# https://docs.aws.amazon.com/AmazonS3/latest/userguide/s3-vectors-limitations.html
METADATA_LIMIT_BYTES = 40 * 1024

br = boto3.client("bedrock-runtime", region_name=REGION)
s3v = boto3.client("s3vectors", region_name=REGION)
ssm = boto3.client("ssm", region_name=REGION)

_epoch = {"val": None, "ts": 0.0}
_api_key = {"val": None, "loaded": False}


class ApiKeyUnavailable(Exception):
    """The API key is configured but could not be read, so requests must be refused."""


class EpochUnavailable(Exception):
    """The cache epoch could not be read, so requests must be refused."""


def api_key():
    """Read the optional app-level key from Parameter Store, once per environment.

    Only the parameter name is configured on the function. The secret value is never
    stored in a Lambda environment variable; it is fetched here with decryption.

    Fails closed: if a key is configured but cannot be read (missing parameter, access
    denied, throttling), this raises instead of returning an empty key, so a transient
    or permission error can never switch authentication off. A failed read is not
    cached, so the next request retries.
    """
    if not API_KEY_PARAM:
        return ""
    if not _api_key["loaded"]:
        try:
            value = ssm.get_parameter(
                Name=API_KEY_PARAM, WithDecryption=True
            )["Parameter"]["Value"]
        except Exception as e:
            print(f"ERROR reading API key parameter {API_KEY_PARAM}: {type(e).__name__}")
            raise ApiKeyUnavailable() from e
        if not value:
            print(f"ERROR API key parameter {API_KEY_PARAM} is empty")
            raise ApiKeyUnavailable()
        _api_key["val"], _api_key["loaded"] = value, True
    return _api_key["val"]


def current_epoch():
    now = time.time()
    if _epoch["val"] is None or now - _epoch["ts"] > 30:   # refresh at most every 30s
        try:
            _epoch["val"] = ssm.get_parameter(Name=EPOCH_PARAM)["Parameter"]["Value"]
        except Exception as e:
            # Keep serving the last known epoch through a transient read error. With no
            # known epoch yet, raise rather than guess, because a guessed epoch could
            # serve entries that a force-invalidate already retired.
            if _epoch["val"] is None:
                print(f"ERROR reading cache epoch parameter {EPOCH_PARAM}: {type(e).__name__}")
                raise EpochUnavailable() from e
            print(f"WARN epoch refresh failed, keeping {_epoch['val']}: {type(e).__name__}")
        _epoch["ts"] = now
    return _epoch["val"]


def bump_epoch():
    """Advance the epoch counter by one.

    A read failure propagates as EpochUnavailable so the caller is refused, rather than
    being replaced by a guessed value that could resurrect entries a previous
    force-invalidate already retired.
    """
    try:
        new = str(int(current_epoch()) + 1)
    except ValueError as e:
        print(f"ERROR cache epoch parameter {EPOCH_PARAM} is not an integer")
        raise EpochUnavailable() from e
    ssm.put_parameter(Name=EPOCH_PARAM, Value=new, Type="String", Overwrite=True)
    _epoch["val"], _epoch["ts"] = new, time.time()
    return new


def _resp(code, obj):
    return {"statusCode": code, "headers": {"Content-Type": "application/json"}, "body": json.dumps(obj)}


def _unavailable(what):
    # One shape for every input the function must have but could not read.
    return _resp(503, {"error": f"{what} unavailable"})


def embed(text):
    r = br.invoke_model(modelId=EMBED_MODEL, body=json.dumps({"inputText": text}))
    return json.loads(r["body"].read())["embedding"]


def llm(prompt, model):
    r = br.converse(modelId=model, messages=[{"role": "user", "content": [{"text": prompt}]}])
    return r["output"]["message"]["content"][0]["text"]


def handler(event, context):
    t0 = time.time()
    headers = {k.lower(): v for k, v in (event.get("headers") or {}).items()}
    try:
        expected_key = api_key()
    except ApiKeyUnavailable:
        return _unavailable("api key")
    if expected_key and headers.get("x-api-key") != expected_key:
        return _resp(401, {"error": "unauthorized"})
    body = {}
    if event.get("body"):
        try:
            body = json.loads(event["body"])
        except Exception:
            body = {}

    # --- force-invalidate: bump epoch, everything before is now a miss ---
    if body.get("action") == "invalidate":
        try:
            new = bump_epoch()
        except EpochUnavailable:
            return _unavailable("cache epoch")
        return _resp(200, {"invalidated": True, "epoch": new,
                           "note": "all entries cached before this epoch now miss"})

    prompt = (body.get("prompt") or "").strip()
    if not prompt:
        return _resp(400, {"error": "missing 'prompt'"})
    try:
        threshold = float(body.get("threshold", SIM_THRESHOLD))
    except (TypeError, ValueError):
        return _resp(400, {"error": "threshold must be a number between 0 and 1"})
    if not 0.0 <= threshold <= 1.0:
        return _resp(400, {"error": "threshold must be a number between 0 and 1"})

    try:
        ep = current_epoch()
    except EpochUnavailable:
        return _unavailable("cache epoch")
    vec = embed(prompt)

    q = s3v.query_vectors(vectorBucketName=BUCKET, indexName=INDEX, topK=5,
                          queryVector={"float32": vec}, returnDistance=True, returnMetadata=True)
    for m in q.get("vectors", []):
        sim = 1.0 - float(m.get("distance", 2.0))
        md = m.get("metadata", {}) or {}
        fresh = (time.time() - int(md.get("created_at", "0") or 0)) < TTL_SECONDS
        current = md.get("epoch") == ep
        # negation-parity guard: 'X' vs 'NOT X' embed ~identically but mean the opposite
        neg_ok = _has_negation(prompt) == _has_negation(md.get("prompt", ""))
        if sim >= threshold and fresh and current and neg_ok and md.get("response"):
            return _resp(200, {"cached": True, "similarity": round(sim, 4), "epoch": ep,
                               "matched_prompt": md.get("prompt"), "response": md["response"],
                               "model": md.get("model"), "latency_ms": int((time.time() - t0) * 1000)})

    answer = llm(prompt, LLM_MODEL)
    metadata = {"prompt": prompt, "response": answer, "model": LLM_MODEL,
                "created_at": str(int(time.time())), "epoch": ep}
    # Caching is best effort: the answer has already been paid for, so an entry that
    # would exceed the 40 KB metadata cap, or a write that fails, is logged and the
    # answer is still returned.
    size = len(json.dumps(metadata).encode("utf-8"))
    if size > METADATA_LIMIT_BYTES:
        print(f"WARN not caching: metadata is {size} bytes, over the {METADATA_LIMIT_BYTES} byte limit")
    else:
        try:
            s3v.put_vectors(vectorBucketName=BUCKET, indexName=INDEX, vectors=[{
                "key": uuid.uuid4().hex,
                "data": {"float32": vec},
                "metadata": metadata,
            }])
        except Exception as e:
            print(f"WARN not caching: put_vectors failed with {type(e).__name__}")
    return _resp(200, {"cached": False, "similarity": None, "epoch": ep, "response": answer,
                       "model": LLM_MODEL, "latency_ms": int((time.time() - t0) * 1000)})
