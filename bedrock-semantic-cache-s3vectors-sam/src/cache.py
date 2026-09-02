"""Serverless Semantic Cache for Amazon Bedrock.
Embed prompt -> query S3 Vectors for a semantically-similar prior prompt ->
HIT (similarity >= threshold, fresh by TTL, and current epoch) return cached response;
MISS -> call Bedrock, store {embedding + metadata}, return.
Force-invalidate: POST {"action":"invalidate"} bumps a global epoch (SSM) -> every
prior entry instantly becomes a miss. No deletes, no scanning, O(1)."""
import json, os, re, time, uuid
import boto3

_NEG = {"not","no","never","without","cannot","nor","neither","none","cant","dont","doesnt","isnt","arent","wont","shouldnt","wasnt","werent","hasnt","havent","didnt","aint"}
def _has_negation(text):
    for t in re.findall(r"[a-z']+", (text or "").lower()):
        if t.replace("'","") in _NEG or t.endswith("n't"):
            return True
    return False

REGION = os.environ.get("AWS_REGION", "us-east-1")
BUCKET = os.environ["VECTOR_BUCKET"]
INDEX = os.environ["VECTOR_INDEX"]
EMBED_MODEL = os.environ.get("EMBED_MODEL", "amazon.titan-embed-text-v2:0")
DEFAULT_MODEL = os.environ.get("LLM_MODEL", "amazon.nova-lite-v1:0")
SIM_THRESHOLD = float(os.environ.get("SIM_THRESHOLD", "0.85"))
TTL_SECONDS = int(os.environ.get("TTL_SECONDS", "86400"))
API_KEY = os.environ.get("API_KEY", "")
EPOCH_PARAM = os.environ.get("EPOCH_PARAM", "/semantic-cache/epoch")

br = boto3.client("bedrock-runtime", region_name=REGION)
s3v = boto3.client("s3vectors", region_name=REGION)
ssm = boto3.client("ssm", region_name=REGION)

_epoch = {"val": None, "ts": 0.0}


def current_epoch():
    now = time.time()
    if _epoch["val"] is None or now - _epoch["ts"] > 30:   # refresh at most every 30s
        try:
            _epoch["val"] = ssm.get_parameter(Name=EPOCH_PARAM)["Parameter"]["Value"]
        except Exception:
            _epoch["val"] = "1"
        _epoch["ts"] = now
    return _epoch["val"]


def bump_epoch():
    try:
        new = str(int(current_epoch()) + 1)
    except Exception:
        new = str(int(time.time()))
    ssm.put_parameter(Name=EPOCH_PARAM, Value=new, Type="String", Overwrite=True)
    _epoch["val"], _epoch["ts"] = new, time.time()
    return new


def _resp(code, obj):
    return {"statusCode": code, "headers": {"Content-Type": "application/json"}, "body": json.dumps(obj)}


def embed(text):
    r = br.invoke_model(modelId=EMBED_MODEL, body=json.dumps({"inputText": text}))
    return json.loads(r["body"].read())["embedding"]


def llm(prompt, model):
    r = br.converse(modelId=model, messages=[{"role": "user", "content": [{"text": prompt}]}])
    return r["output"]["message"]["content"][0]["text"]


def handler(event, context):
    t0 = time.time()
    headers = {k.lower(): v for k, v in (event.get("headers") or {}).items()}
    if API_KEY and headers.get("x-api-key") != API_KEY:
        return _resp(401, {"error": "unauthorized"})
    body = {}
    if event.get("body"):
        try:
            body = json.loads(event["body"])
        except Exception:
            body = {}

    # --- force-invalidate: bump epoch, everything before is now a miss ---
    if body.get("action") == "invalidate":
        new = bump_epoch()
        return _resp(200, {"invalidated": True, "epoch": new,
                           "note": "all entries cached before this epoch now miss"})

    prompt = (body.get("prompt") or "").strip()
    model = body.get("model", DEFAULT_MODEL)
    threshold = float(body.get("threshold", SIM_THRESHOLD))
    if not prompt:
        return _resp(400, {"error": "missing 'prompt'"})

    ep = current_epoch()
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

    answer = llm(prompt, model)
    s3v.put_vectors(vectorBucketName=BUCKET, indexName=INDEX, vectors=[{
        "key": uuid.uuid4().hex,
        "data": {"float32": vec},
        "metadata": {"prompt": prompt, "response": answer, "model": model,
                     "created_at": str(int(time.time())), "epoch": ep},
    }])
    return _resp(200, {"cached": False, "similarity": None, "epoch": ep, "response": answer,
                       "model": model, "latency_ms": int((time.time() - t0) * 1000)})
