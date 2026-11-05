# Copyright 2026 Amazon.com, Inc. or its affiliates. All Rights Reserved.
# SPDX-License-Identifier: MIT-0
"""Amazon SageMaker AI entry point for Strands Decider.

SageMaker calls GET /ping and POST /invocations on port 8080. Strands Decider 0.2.0 serves /health and
POST /v1/systemone, so this file maps the two SageMaker routes onto its server. The model is loaded
before the server starts listening, so /ping answers only once the model is ready. If the download or
the load fails the process exits and the reason is in the endpoint's logs.

/invocations answers one request at a time. The upstream server states that its behaviour under
concurrent requests is not verified, and on a CPU tickets that arrive together slow each other down. A
request that waits more than DECIDER_QUEUE_TIMEOUT_S seconds for the model is refused with 503.

The endpoint is reachable only through the SageMaker runtime API, which authenticates callers
with IAM (SigV4). Do not publish this port.
"""
import logging
import os
import threading

import uvicorn
from fastapi import HTTPException
from huggingface_hub import snapshot_download
from strands_decider.schema import SystemOneRequest
from strands_decider.server import create_app

logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s")
log = logging.getLogger("decider")

CHECKPOINT = os.environ.get("DECIDER_CHECKPOINT", "StrandsAgents/strands-decider-2B-hobson-v19")
# The Hub repo has no tags, so the commit is the only stable reference to the weights.
REVISION = os.environ.get("DECIDER_REVISION") or None
DEVICE = os.environ.get("DECIDER_DEVICE", "cpu")
MODEL_DIR = os.environ.get("DECIDER_MODEL_DIR", "/tmp/decider")
# A request that waits this long for the model is refused with 503. The workflow sends that ticket to review.
QUEUE_TIMEOUT_S = float(os.environ.get("DECIDER_QUEUE_TIMEOUT_S", "30"))
PORT = int(os.environ.get("SAGEMAKER_BIND_TO_PORT", "8080"))

log.info("Fetching %s at %s", CHECKPOINT, REVISION or "main")
checkpoint_dir = snapshot_download(CHECKPOINT, revision=REVISION, local_dir=os.path.join(MODEL_DIR, "checkpoint"))

# create_app fetches the base model at the revision that the checkpoint's provenance.json records,
# then loads the model.
log.info("Loading the model on %s", DEVICE)
app = create_app(checkpoint_dir, device=DEVICE, model_name=os.path.basename(CHECKPOINT))

handlers = {route.path: route.endpoint for route in app.routes if hasattr(route, "endpoint")}
upstream = handlers["/v1/systemone"]
_lock = threading.Lock()


@app.post("/invocations")
def invocations(request: SystemOneRequest):
    # A plain def runs in a worker thread, so waiting for the lock does not block /ping.
    if not _lock.acquire(timeout=QUEUE_TIMEOUT_S):
        raise HTTPException(status_code=503, detail="The model is busy")
    try:
        return upstream(request)
    finally:
        _lock.release()


@app.get("/ping")
async def ping() -> dict:
    return {"status": "ok"}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=PORT, workers=1)
