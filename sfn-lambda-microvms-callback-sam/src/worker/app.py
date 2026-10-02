"""Job worker that runs inside an AWS Lambda MicroVM and reports to AWS Step Functions.

The state machine starts this MicroVM, stores its task token in Amazon DynamoDB under
the MicroVM ID, and waits. This worker then:

  1. receives the job input and its own MicroVM ID in the /run lifecycle hook
  2. reads the task token from DynamoDB (key = MicroVM ID)
  3. runs the job, sending SendTaskHeartbeat while it works
  4. returns the result with SendTaskSuccess, or the error with SendTaskFailure

Lifecycle hooks are served on port 9000:
  POST /aws/lambda-microvms/runtime/v1/ready  image build, 200 = ready to snapshot
  POST /aws/lambda-microvms/runtime/v1/run    once per RunMicrovm, starts the job

AWS clients are created after /run, never at build time, so no credentials or open
connections are captured in the snapshot.
"""

import json
import os
import threading
import time
from datetime import datetime, timezone
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer

import boto3
from botocore.config import Config

HOOK_PATH = "/aws/lambda-microvms/runtime/v1"
HOOK_PORT = int(os.environ.get("HOOK_PORT", "9000"))
TABLE_NAME = os.environ["TASK_TOKEN_TABLE"]
HEARTBEAT_INTERVAL = int(os.environ.get("HEARTBEAT_INTERVAL_SECONDS", "20"))
TOKEN_WAIT_SECONDS = 120
MAX_PRIME_LIMIT = 50_000_000
MAX_SIMULATED_SECONDS = 7200

_started = threading.Event()


def log(msg, **fields):
    """Write one JSON line to stdout, which the platform ships to CloudWatch Logs."""
    entry = {"ts": datetime.now(timezone.utc).isoformat(), "msg": msg, **fields}
    print(json.dumps(entry), flush=True)


def parse_run_hook(raw):
    """Return (microvm_id, job) from the /run hook body.

    The platform wraps the RunHookPayload string from RunMicrovm in an envelope:
    {"microvmId": "...", "runHookPayload": "<the string passed to RunMicrovm>"}
    """
    envelope = json.loads(raw or "{}")
    payload = envelope.get("runHookPayload") or "{}"
    if isinstance(payload, str):
        payload = json.loads(payload)
    return envelope.get("microvmId"), payload.get("job") or {}


def wait_for_task_token(dynamodb, microvm_id):
    """Poll DynamoDB until the state machine has stored the task token for this MicroVM."""
    deadline = time.monotonic() + TOKEN_WAIT_SECONDS
    while time.monotonic() < deadline:
        item = dynamodb.get_item(
            TableName=TABLE_NAME,
            Key={"microvmId": {"S": microvm_id}},
            ConsistentRead=True,
        ).get("Item")
        if item:
            return item["taskToken"]["S"]
        time.sleep(1)
    return None


def run_job(job, stop_heartbeats):
    """Example workload. Replace this function with your own long-running job.

    Counts the prime numbers below job["limit"]. Optional fields used to exercise the
    workflow: job["durationSeconds"] keeps the job busy for longer (heartbeats continue),
    job["simulate"] = "failure" raises an error, job["simulate"] = "hang" stops
    heartbeats and never returns, as a crashed or wedged process would.
    """
    simulate = job.get("simulate")
    if simulate == "failure":
        raise ValueError("Simulated failure requested in the job input")
    if simulate == "hang":
        stop_heartbeats.set()
        log("simulating_hang")
        threading.Event().wait()

    started = time.monotonic()
    limit = min(int(job.get("limit", 1_000_000)), MAX_PRIME_LIMIT)
    sieve = bytearray([1]) * (limit + 1)
    sieve[0:2] = b"\x00\x00"
    for n in range(2, int(limit**0.5) + 1):
        if sieve[n]:
            sieve[n * n :: n] = bytearray(len(range(n * n, limit + 1, n)))
    prime_count = sum(sieve)

    extra = min(int(job.get("durationSeconds", 0)), MAX_SIMULATED_SECONDS)
    if extra > 0:
        time.sleep(extra)

    return {
        "limit": limit,
        "primeCount": prime_count,
        "elapsedSeconds": round(time.monotonic() - started, 3),
    }


def heartbeat_loop(sfn, token, stop):
    """Tell Step Functions the job is alive until the job finishes or stops heartbeating."""
    while not stop.wait(HEARTBEAT_INTERVAL):
        try:
            sfn.send_task_heartbeat(taskToken=token)
            log("heartbeat_sent")
        except Exception as err:  # noqa: BLE001  keep the job running, the next beat may succeed
            log("heartbeat_failed", error=str(err))


def process(raw_run_hook_body):
    microvm_id, job = parse_run_hook(raw_run_hook_body)
    region = os.environ.get("AWS_REGION")  # set by the Lambda MicroVMs platform
    log("job_received", microvmId=microvm_id, region=region, job=job)

    config = Config(retries={"max_attempts": 5, "mode": "standard"})
    dynamodb = boto3.client("dynamodb", region_name=region, config=config)
    sfn = boto3.client("stepfunctions", region_name=region, config=config)

    token = wait_for_task_token(dynamodb, microvm_id)
    if token is None:
        # Nothing to report to. The state machine's heartbeat timeout fires and
        # terminates this MicroVM.
        log("task_token_not_found", microvmId=microvm_id)
        return

    stop_heartbeats = threading.Event()
    threading.Thread(target=heartbeat_loop, args=(sfn, token, stop_heartbeats), daemon=True).start()
    try:
        result = run_job(job, stop_heartbeats)
        stop_heartbeats.set()
        sfn.send_task_success(taskToken=token, output=json.dumps({"microvmId": microvm_id, **result}))
        log("job_succeeded", microvmId=microvm_id, result=result)
    except Exception as err:  # noqa: BLE001  every job error is reported to the workflow
        stop_heartbeats.set()
        sfn.send_task_failure(taskToken=token, error="JobFailed", cause=str(err)[:32768])
        log("job_failed", microvmId=microvm_id, error=str(err))


class HookHandler(BaseHTTPRequestHandler):
    def _reply(self, status, body):
        data = json.dumps(body).encode()
        self.send_response(status)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(data)))
        self.end_headers()
        self.wfile.write(data)

    def do_POST(self):  # noqa: N802  name required by BaseHTTPRequestHandler
        length = int(self.headers.get("Content-Length") or 0)
        body = self.rfile.read(length).decode() if length else ""

        if self.path == f"{HOOK_PATH}/ready":
            self._reply(200, {"status": "ready"})
        elif self.path == f"{HOOK_PATH}/run":
            # The run hook must answer within its timeout, so the job runs on a thread.
            if not _started.is_set():
                _started.set()
                threading.Thread(target=process, args=(body,), daemon=True).start()
            self._reply(200, {"status": "started"})
        else:
            self._reply(404, {"error": "unknown hook"})

    def log_message(self, fmt, *args):
        pass  # structured logs are written by log()


if __name__ == "__main__":
    log("worker_starting", port=HOOK_PORT)
    ThreadingHTTPServer(("0.0.0.0", HOOK_PORT), HookHandler).serve_forever()
