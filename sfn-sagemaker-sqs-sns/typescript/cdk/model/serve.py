# Copyright 2026 Amazon.com, Inc. or its affiliates. All Rights Reserved.
# SPDX-License-Identifier: MIT-0
"""Amazon SageMaker AI entry point for Strands Decider.

SageMaker calls GET /ping and POST /invocations on port 8080. The checkpoint and its base model are
downloaded, loaded and warmed up before the server starts listening, so /ping answers only once the
model is ready. If any of that fails the process exits and the reason is in the endpoint's logs.

Differences from running ``strands-decider serve`` directly:
  * The checkpoint and the base model it was trained on are fetched at pinned Hugging Face commits.
    The upstream loader passes no revision for the base model.
  * Requests are serialised with a lock. The upstream server states that its behaviour under
    concurrent requests is not verified, so this container does not depend on it.

The endpoint is reachable only through the SageMaker runtime API, which authenticates callers
with IAM (SigV4). Do not publish this port.
"""
import json
import logging
import os
import threading
import time

import torch
import uvicorn
from fastapi import HTTPException
from fastapi.responses import JSONResponse
from huggingface_hub import snapshot_download
from strands_decider.modeling import config_path
from strands_decider.schema import SystemOneRequest
from strands_decider.server import create_app, get_engine

logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s")
log = logging.getLogger("decider")

CHECKPOINT = os.environ.get("DECIDER_CHECKPOINT", "StrandsAgents/strands-decider-2B-hobson-v19")
REVISION = os.environ.get("DECIDER_REVISION") or None
BASE_REVISION = os.environ.get("DECIDER_BASE_REVISION") or None
DEVICE = os.environ.get("DECIDER_DEVICE", "cpu")
MODEL_DIR = os.environ.get("DECIDER_MODEL_DIR", "/tmp/decider")
# A request that waits this long for the model is refused with 503, which keeps the queue short. The
# workflow sends that ticket to review.
QUEUE_TIMEOUT_S = float(os.environ.get("DECIDER_QUEUE_TIMEOUT_S", "30"))
PORT = int(os.environ.get("SAGEMAKER_BIND_TO_PORT", "8080"))

log.info("Fetching %s at %s", CHECKPOINT, REVISION or "main")
checkpoint_dir = snapshot_download(CHECKPOINT, revision=REVISION, local_dir=os.path.join(MODEL_DIR, "checkpoint"))

# The checkpoint names its base model but no revision. Fetch the base at a pinned commit and point
# the checkpoint's config at that copy, so the weights do not change underneath a running pattern.
config_file = config_path(checkpoint_dir)
with open(config_file, encoding="utf-8") as fh:
    config = json.load(fh)
log.info("Fetching %s at %s", config["base_model"], BASE_REVISION or "main")
config["base_model"] = snapshot_download(
    config["base_model"], revision=BASE_REVISION, local_dir=os.path.join(MODEL_DIR, "base")
)
with open(config_file, "w", encoding="utf-8") as fh:
    json.dump(config, fh)

if DEVICE == "cpu":
    # Never use every CPU: leave one for the event loop, so /ping is answered in time while the model
    # computes. This only lowers PyTorch's default thread count, never raises it.
    torch.set_num_threads(max(1, min(torch.get_num_threads(), (os.cpu_count() or 2) - 1)))
log.info("Loading the model on %s", DEVICE)
app = create_app(checkpoint_dir, device=DEVICE, model_name=os.path.basename(CHECKPOINT))

# The first request after loading is much slower than later ones (kernel setup, caches). Pay for it
# here so /ping only answers once the endpoint serves at its normal speed. An exception stops the
# process on purpose: a model that cannot answer must not report healthy.
_warmup = SystemOneRequest.model_validate(
    {
        "state": "My invoice shows a charge I do not recognise.",
        "questions": {
            "department": {"type": "choice", "instructions": "Which team should handle this?",
                           "criteria": {"billing": "charges", "technical": "bugs", "sales": "pricing"}},
            "urgency": {"type": "score", "instructions": "How urgent is this?", "criteria": ["Low", "Medium", "High"]},
            "incident": {"type": "noul", "instructions": "Is this a security incident?"},
        },
    }
)
_started = time.perf_counter()
get_engine().evaluate(_warmup)
log.info("Warm-up request took %.1f s", time.perf_counter() - _started)

_lock = threading.Lock()


@app.get("/ping")
async def ping() -> dict:
    # async, so it runs on the event loop and cannot queue behind requests that wait for the model
    return {"status": "ok"}


@app.post("/invocations")
def invocations(request: SystemOneRequest) -> JSONResponse:
    started = time.perf_counter()
    if not _lock.acquire(timeout=QUEUE_TIMEOUT_S):
        raise HTTPException(status_code=503, detail="The model is busy")
    try:
        response = get_engine().evaluate(request)
    except ValueError as exc:
        # The engine raises ValueError for a request it cannot answer, which is the caller's error.
        raise HTTPException(status_code=422, detail=str(exc)) from exc
    finally:
        _lock.release()
    payload = response.model_dump()
    payload["latency_ms"] = round((time.perf_counter() - started) * 1000, 2)
    return JSONResponse(content=payload)


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=PORT, workers=1)
