"""
The job's business steps. Identical in before/ and after/.

Three steps, each slow or flaky in a way real jobs are:
  1. fetch_source   - pulls input (simulated I/O)
  2. transform      - CPU work; fails on attempt 1 for 'flaky' inputs
  3. publish_result - writes the output somewhere

The migration changes HOW these run, not WHAT they do.

Step outputs hold only str/int/bool: DynamoDB (before/) rejects float.
"""

import hashlib
import time

# transform() raises on its FIRST attempt for inputs containing this word,
# then succeeds. It stands in for a transient dependency failure (throttle,
# timeout, 5xx). Keyed off the attempt number the caller passes in, so it
# behaves the same in a fresh execution environment as in a warm one.
FLAKY_MARKER = "flaky"


class TransientError(Exception):
    """A failure that is safe to retry."""


def fetch_source(job_id: str, payload: dict) -> dict:
    time.sleep(0.5)
    text = payload.get("input", "")
    return {"job_id": job_id, "source": text, "bytes": len(text)}


def transform(job_id: str, source: dict, attempt: int) -> dict:
    text = source["source"]
    if FLAKY_MARKER in text and attempt == 1:
        raise TransientError("downstream dependency timed out")
    time.sleep(0.5)
    digest = hashlib.sha256(text.encode()).hexdigest()
    return {"job_id": job_id, "digest": digest, "length": source["bytes"]}


def publish_result(job_id: str, result: dict) -> dict:
    time.sleep(0.5)
    return {"job_id": job_id, "published": True, "digest": result["digest"]}
