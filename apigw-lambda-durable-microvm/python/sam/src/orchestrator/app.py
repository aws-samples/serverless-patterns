"""Durable orchestrator: one MicroVM per job.

Steps (each checkpointed, never re-run on replay):
  1. run-microvm        boot one VM from the snapshot; runHookPayload carries the
                        command plus the callback coordinates (under 4096 chars)
  2. callback.result()  suspend with no compute billed until the VM POSTs the
                        result to /callback, or the timeout fires
  3. terminate-microvm  always, even when the callback failed or timed out
"""
import json
import os

import boto3
from aws_durable_execution_sdk_python import DurableContext, durable_execution
from aws_durable_execution_sdk_python.context import StepContext, durable_step
from aws_durable_execution_sdk_python.exceptions import CallbackError

microvms = boto3.client("lambda-microvms")

IMAGE_ARN = os.environ["IMAGE_ARN"]
IMAGE_VERSION = os.environ["IMAGE_VERSION"]
EXECUTION_ROLE_ARN = os.environ["EXECUTION_ROLE_ARN"]
JOB_TIMEOUT_SECONDS = int(os.environ["JOB_TIMEOUT_SECONDS"])


@durable_step
def run_microvm(_: StepContext, command: str, callback_id: str, callback_url: str) -> dict:
    payload = json.dumps(
        {"command": command, "callbackId": callback_id, "callbackUrl": callback_url}
    )
    # No idlePolicy: idle is measured on inbound proxy traffic, and this VM only
    # receives the run hook, so an idle policy would suspend it mid-job. Lifetime
    # is bounded by maximumDurationInSeconds instead, matched to the durable
    # execution timeout so a hung VM is still torn down.
    resp = microvms.run_microvm(
        imageIdentifier=IMAGE_ARN,
        imageVersion=IMAGE_VERSION,
        executionRoleArn=EXECUTION_ROLE_ARN,
        maximumDurationInSeconds=JOB_TIMEOUT_SECONDS,
        runHookPayload=payload,
    )
    return {"microvmId": resp["microvmId"]}


@durable_step
def terminate_microvm(_: StepContext, microvm_id: str) -> dict:
    try:
        microvms.terminate_microvm(microvmIdentifier=microvm_id)
    except microvms.exceptions.ResourceNotFoundException:
        pass  # already gone
    return {"terminated": microvm_id}


@durable_execution
def handler(event: dict, context: DurableContext) -> dict:
    command = event["command"]
    # The API handler derives this from its own request; passing it in the
    # payload avoids a template cycle (API -> function -> orchestrator -> API).
    callback_url = event["callbackUrl"]

    # Mint the callback first so its id can ride in runHookPayload.
    callback = context.create_callback(name="job-result")
    vm = context.step(
        run_microvm(command, callback.callback_id, callback_url), name="run-microvm"
    )

    try:
        # The callback result is the JSON string the VM posted; decode it so the
        # execution result is a nested object rather than an escaped string.
        result = json.loads(callback.result())
        status = "completed"
    except CallbackError as err:
        # The VM reported failure (or the callback timed out). err.data carries
        # the ErrorData the API handler attached: the VM's exit code and output.
        try:
            data = json.loads(err.data) if err.data else None
        except ValueError:
            data = err.data
        result = {"errorType": err.error_type, "message": err.message, "data": data}
        status = "failed"

    context.step(terminate_microvm(vm["microvmId"]), name="terminate-microvm")
    return {"status": status, "microvmId": vm["microvmId"], "result": result}
