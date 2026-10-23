import datetime
import logging
import os

import boto3
from botocore.exceptions import ClientError

logger = logging.getLogger()
logger.setLevel(logging.INFO)

WORKFLOW_EXECUTION_TRACKER_TABLE_NAME = os.environ["WORKFLOW_EXECUTION_TRACKER_TABLE_NAME"]
EXECUTION_RETENTION_DAYS = int(os.environ["EXECUTION_RETENTION_DAYS"])
MAX_STATUS_VALUE_BYTES = int(os.environ.get("MAX_STATUS_VALUE_BYTES", "65536"))

_execution_table = boto3.resource("dynamodb").Table(WORKFLOW_EXECUTION_TRACKER_TABLE_NAME)
_TERMINAL_STATUSES = {"SUCCEEDED", "FAILED", "TIMED_OUT", "ABORTED", "REJECTED"}


def _bounded_value(value):
    if not isinstance(value, str):
        value = str(value)
    encoded = value.encode("utf-8")
    if len(encoded) <= MAX_STATUS_VALUE_BYTES:
        return value, False
    truncated = encoded[:MAX_STATUS_VALUE_BYTES].decode("utf-8", errors="ignore")
    return truncated, True


def lambda_handler(event, _context):
    detail = event.get("detail", {})
    execution_arn = detail.get("executionArn")
    state_machine_arn = detail.get("stateMachineArn")
    status = detail.get("status")
    if not execution_arn or not state_machine_arn or not status:
        raise ValueError(
            "Step Functions status event is missing executionArn, stateMachineArn, or status"
        )

    execution_id = execution_arn.rsplit(":", 1)[-1]
    now_datetime = datetime.datetime.now(datetime.timezone.utc)
    now = now_datetime.isoformat()
    names = {"#status": "status", "#currentStatus": "status"}
    values = {
        ":status": status,
        ":updatedAt": now,
        ":executionArn": execution_arn,
        ":expectedStateMachineArn": state_machine_arn,
        ":succeeded": "SUCCEEDED",
        ":failed": "FAILED",
        ":timedOut": "TIMED_OUT",
        ":aborted": "ABORTED",
        ":rejected": "REJECTED",
    }
    assignments = [
        "#status = :status",
        "lastUpdatedAt = :updatedAt",
        "executionArn = :executionArn",
    ]

    if status == "RUNNING":
        names["#startedAt"] = "startedAt"
        values[":startedAt"] = detail.get("startDate") or now
        assignments.append("#startedAt = if_not_exists(#startedAt, :startedAt)")
    if status in _TERMINAL_STATUSES:
        names["#finishedAt"] = "finishedAt"
        values[":finishedAt"] = detail.get("stopDate") or now
        values[":expiresAt"] = int(
            (now_datetime + datetime.timedelta(days=EXECUTION_RETENTION_DAYS)).timestamp()
        )
        assignments.extend(["#finishedAt = :finishedAt", "expiresAt = :expiresAt"])
        for field in ("output", "error", "cause"):
            if field in detail:
                bounded, truncated = _bounded_value(detail[field])
                name_token = f"#{field}"
                value_token = f":{field}"
                names[name_token] = field
                values[value_token] = bounded
                assignments.append(f"{name_token} = {value_token}")
                if truncated:
                    truncated_name = f"#{field}Truncated"
                    truncated_value = f":{field}Truncated"
                    names[truncated_name] = f"{field}Truncated"
                    values[truncated_value] = True
                    assignments.append(f"{truncated_name} = {truncated_value}")

    condition = (
        "attribute_exists(executionId) "
        "AND stateMachineArn = :expectedStateMachineArn "
        "AND NOT (#currentStatus IN (:succeeded, :failed, :timedOut, :aborted, :rejected))"
    )
    try:
        _execution_table.update_item(
            Key={"executionId": execution_id},
            UpdateExpression="SET " + ", ".join(assignments),
            ExpressionAttributeNames=names,
            ExpressionAttributeValues=values,
            ConditionExpression=condition,
        )
    except ClientError as error:
        if error.response.get("Error", {}).get("Code") == "ConditionalCheckFailedException":
            logger.info("Ignoring mismatched, untracked, or already-terminal execution %s", execution_id)
            return {"ignored": True}
        raise

    logger.info("Updated execution %s to %s", execution_id, status)
    return {"executionId": execution_id, "status": status}
