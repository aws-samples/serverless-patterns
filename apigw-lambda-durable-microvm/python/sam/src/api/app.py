"""API handler: start a job, read a job, receive the MicroVM's callback.

  POST /jobs          {"command": "..."}  -> 202 {"jobId": ...}
  GET  /jobs/{jobId}                      -> {"status": ..., "result": ...}
  POST /callback      {"callbackId": ..., "status": "success"|"failure", "result": ...}

The jobId is the durable execution name, so no state store is needed: GET looks
the execution up by name on the orchestrator alias.
"""
import json
import os
import uuid

import boto3

lambda_client = boto3.client("lambda")

FUNCTION_NAME = os.environ["ORCHESTRATOR_FUNCTION_NAME"]
ALIAS = os.environ["ORCHESTRATOR_ALIAS"]


def _response(status: int, body: dict) -> dict:
    return {"statusCode": status, "headers": {"Content-Type": "application/json"}, "body": json.dumps(body)}


def _start_job(body: dict, callback_url: str) -> dict:
    command = body.get("command")
    if not isinstance(command, str) or not command.strip():
        return _response(400, {"error": "body must be {\"command\": \"<shell command>\"}"})
    job_id = str(uuid.uuid4())
    # Async invoke by alias; the durable execution name doubles as our job id.
    lambda_client.invoke(
        FunctionName=FUNCTION_NAME,
        Qualifier=ALIAS,
        InvocationType="Event",
        DurableExecutionName=job_id,
        Payload=json.dumps({"command": command, "callbackUrl": callback_url}).encode(),
    )
    return _response(202, {"jobId": job_id})


def _get_job(job_id: str) -> dict:
    # The name filter is not allowed together with a Qualifier, so list by the
    # unqualified function name; execution names are unique per function.
    found = lambda_client.list_durable_executions_by_function(
        FunctionName=FUNCTION_NAME, DurableExecutionName=job_id, MaxItems=1
    ).get("DurableExecutions", [])
    if not found:
        return _response(404, {"error": "unknown jobId"})
    execution = lambda_client.get_durable_execution(DurableExecutionArn=found[0]["DurableExecutionArn"])
    out = {"jobId": job_id, "status": execution["Status"]}
    if execution.get("Result"):
        out["result"] = json.loads(execution["Result"])
    if execution.get("Error"):
        out["error"] = execution["Error"]
    return _response(200, out)


def _callback(body: dict) -> dict:
    callback_id = body.get("callbackId")
    if not callback_id:
        return _response(400, {"error": "callbackId is required"})
    try:
        if body.get("status") == "failure":
            err = body.get("error") or {}
            lambda_client.send_durable_execution_callback_failure(
                CallbackId=callback_id,
                Error={
                    "ErrorType": str(err.get("type", "JobFailed"))[:256],
                    "ErrorMessage": str(err.get("message", "the VM reported failure"))[:1024],
                    "ErrorData": json.dumps(body.get("result", {}))[:4096],
                },
            )
        else:
            lambda_client.send_durable_execution_callback_success(
                CallbackId=callback_id, Result=json.dumps(body.get("result", {}))
            )
    except lambda_client.exceptions.ResourceNotFoundException:
        return _response(409, {"error": "callback not found or already completed"})
    except lambda_client.exceptions.InvalidParameterValueException as err:
        # Lambda rejects a malformed or unknown callback id this way.
        return _response(400, {"error": str(err)})
    return _response(200, {"ok": True})


def handler(event, _context):
    method, path = event["httpMethod"], event["resource"]
    try:
        body = json.loads(event.get("body") or "{}")
    except json.JSONDecodeError:
        return _response(400, {"error": "invalid JSON body"})

    if method == "POST" and path == "/jobs":
        rc = event["requestContext"]
        callback_url = f"https://{rc['domainName']}/{rc['stage']}/callback"
        return _start_job(body, callback_url)
    if method == "GET" and path == "/jobs/{jobId}":
        return _get_job(event["pathParameters"]["jobId"])
    if method == "POST" and path == "/callback":
        return _callback(body)
    return _response(404, {"error": "not found"})
