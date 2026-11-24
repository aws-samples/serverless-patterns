import datetime
import json
import logging
import os

import boto3
from boto3.dynamodb.conditions import Key
from botocore.exceptions import ClientError

logger = logging.getLogger()
logger.setLevel(logging.INFO)

WORKFLOW_EXECUTION_TRACKER_TABLE_NAME = os.environ["WORKFLOW_EXECUTION_TRACKER_TABLE_NAME"]
STATUS_LAST_UPDATED_AT_INDEX_NAME = os.environ["STATUS_LAST_UPDATED_AT_INDEX_NAME"]
WORKFLOW_EVENT_BUS_NAME = os.environ["WORKFLOW_EVENT_BUS_NAME"]
WORKFLOW_EVENT_SOURCE = os.environ["WORKFLOW_EVENT_SOURCE"]
WORKFLOW_EVENT_DETAIL_TYPE = os.environ["WORKFLOW_EVENT_DETAIL_TYPE"]
EXECUTION_RETENTION_DAYS = int(os.environ["EXECUTION_RETENTION_DAYS"])
STALE_AFTER_SECONDS = int(os.environ.get("STALE_AFTER_SECONDS", "120"))
MAX_RECORDS_PER_RUN = int(os.environ.get("MAX_RECORDS_PER_RUN", "100"))
MAX_STATUS_VALUE_BYTES = int(os.environ.get("MAX_STATUS_VALUE_BYTES", "65536"))

_execution_table = boto3.resource("dynamodb").Table(WORKFLOW_EXECUTION_TRACKER_TABLE_NAME)
_stepfunctions = boto3.client("stepfunctions")
_eventbridge = boto3.client("events")
_RECONCILABLE_STATUSES = (
    "REQUESTED",
    "DISPATCH_FAILED",
    "STARTING",
    "START_FAILED",
    "RUNNING",
    "PENDING_REDRIVE",
)
_TERMINAL_STATUSES = {"SUCCEEDED", "FAILED", "TIMED_OUT", "ABORTED"}


class RetryPublicationError(RuntimeError):
    pass


def _bounded_value(value):
    if not isinstance(value, str):
        value = str(value)
    encoded = value.encode("utf-8")
    if len(encoded) <= MAX_STATUS_VALUE_BYTES:
        return value, False
    return encoded[:MAX_STATUS_VALUE_BYTES].decode("utf-8", errors="ignore"), True


def _execution_arn(item):
    if item.get("executionArn"):
        return item["executionArn"]
    prefix, qualified_name = item["stateMachineArn"].split(":stateMachine:", 1)
    state_machine_name = qualified_name.split(":", 1)[0]
    return f"{prefix}:execution:{state_machine_name}:{item['executionId']}"


def _conditional_update(item, new_status, attributes):
    names = {"#status": "status"}
    values = {
        ":newStatus": new_status,
        ":expectedStatus": item["status"],
        ":stateMachineArn": item.get("stateMachineArn", ""),
    }
    assignments = ["#status = :newStatus"]
    for index, (name, value) in enumerate(attributes.items()):
        name_token = f"#name{index}"
        value_token = f":value{index}"
        names[name_token] = name
        values[value_token] = value
        assignments.append(f"{name_token} = {value_token}")

    condition = "#status = :expectedStatus"
    if item.get("stateMachineArn"):
        condition += " AND stateMachineArn = :stateMachineArn"
    else:
        values.pop(":stateMachineArn")

    try:
        _execution_table.update_item(
            Key={"executionId": item["executionId"]},
            UpdateExpression="SET " + ", ".join(assignments),
            ConditionExpression=condition,
            ExpressionAttributeNames=names,
            ExpressionAttributeValues=values,
        )
        return True
    except ClientError as error:
        if error.response.get("Error", {}).get("Code") == "ConditionalCheckFailedException":
            logger.info("Execution %s changed while reconciling", item["executionId"])
            return False
        raise


def _publish_retry(item):
    response = _eventbridge.put_events(
        Entries=[
            {
                "EventBusName": WORKFLOW_EVENT_BUS_NAME,
                "Source": WORKFLOW_EVENT_SOURCE,
                "DetailType": WORKFLOW_EVENT_DETAIL_TYPE,
                "Detail": json.dumps(
                    {
                        "executionId": item["executionId"],
                        "workflowType": item["workflowType"],
                    },
                    separators=(",", ":"),
                ),
            }
        ]
    )
    if response.get("FailedEntryCount", 0):
        failure = response.get("Entries", [{}])[0]
        raise RetryPublicationError(
            failure.get("ErrorMessage", "EventBridge rejected retry event")
        )


def _publish_and_touch(item, now):
    _publish_retry(item)
    return _conditional_update(item, item["status"], {"lastUpdatedAt": now})


def _mark_for_retry(item, now, reason):
    changed = _conditional_update(
        item,
        "START_FAILED",
        {
            "error": "ExecutionNotFound",
            "cause": reason,
        },
    )
    if changed:
        retry_item = dict(item)
        retry_item["status"] = "START_FAILED"
        _publish_and_touch(retry_item, now)
    return changed


def _refresh_retryable(item, now):
    if item["status"] in {"REQUESTED", "DISPATCH_FAILED"}:
        return _publish_and_touch(item, now)

    if not item.get("stateMachineArn"):
        return _mark_for_retry(
            item,
            now,
            "The tracker record has no state machine ARN",
        )

    try:
        response = _stepfunctions.describe_execution(executionArn=_execution_arn(item))
    except ClientError as error:
        code = error.response.get("Error", {}).get("Code")
        if code in {"ExecutionDoesNotExist", "ExecutionDoesNotExistException"}:
            if item["status"] == "START_FAILED":
                return _publish_and_touch(item, now)
            return _mark_for_retry(
                item,
                now,
                "No Step Functions execution exists for the tracker record",
            )
        raise

    actual_status = response["status"]
    attributes = {
        "executionArn": response["executionArn"],
        "startedAt": response["startDate"].isoformat(),
        "lastUpdatedAt": now,
    }
    if actual_status in _TERMINAL_STATUSES:
        stop_date = response.get("stopDate") or datetime.datetime.now(datetime.timezone.utc)
        attributes["finishedAt"] = stop_date.isoformat()
        attributes["expiresAt"] = int(
            (stop_date + datetime.timedelta(days=EXECUTION_RETENTION_DAYS)).timestamp()
        )
        for field in ("output", "error", "cause"):
            if field in response:
                bounded, truncated = _bounded_value(response[field])
                attributes[field] = bounded
                if truncated:
                    attributes[f"{field}Truncated"] = True
    return _conditional_update(item, actual_status, attributes)


def _stale_records(cutoff):
    records = []
    per_status_limit = max(1, MAX_RECORDS_PER_RUN // len(_RECONCILABLE_STATUSES))
    for status in _RECONCILABLE_STATUSES:
        remaining = MAX_RECORDS_PER_RUN - len(records)
        if remaining <= 0:
            break
        response = _execution_table.query(
            IndexName=STATUS_LAST_UPDATED_AT_INDEX_NAME,
            KeyConditionExpression=(
                Key("status").eq(status) & Key("lastUpdatedAt").lte(cutoff)
            ),
            Limit=min(per_status_limit, remaining),
            ScanIndexForward=True,
        )
        records.extend(response.get("Items", []))
    return records


def _record_reconciliation_failure(item, now, error):
    try:
        _execution_table.update_item(
            Key={"executionId": item["executionId"]},
            UpdateExpression=(
                "SET lastUpdatedAt = :updatedAt, reconciliationError = :error "
                "ADD reconciliationFailureCount :one"
            ),
            ConditionExpression="#status = :expectedStatus",
            ExpressionAttributeNames={"#status": "status"},
            ExpressionAttributeValues={
                ":updatedAt": now,
                ":error": f"{type(error).__name__}: {str(error)[:512]}",
                ":one": 1,
                ":expectedStatus": item["status"],
            },
        )
    except ClientError as update_error:
        if update_error.response.get("Error", {}).get("Code") != "ConditionalCheckFailedException":
            raise


def lambda_handler(_event, _context):
    now_datetime = datetime.datetime.now(datetime.timezone.utc)
    now = now_datetime.isoformat()
    cutoff = (now_datetime - datetime.timedelta(seconds=STALE_AFTER_SECONDS)).isoformat()
    records = _stale_records(cutoff)
    reconciled = 0
    failures = []

    for item in records:
        try:
            if _refresh_retryable(item, now):
                reconciled += 1
        except Exception as error:
            logger.exception("Failed to reconcile execution %s", item.get("executionId"))
            if not isinstance(error, RetryPublicationError):
                _record_reconciliation_failure(item, now, error)
            failures.append(f"{item.get('executionId')}: {type(error).__name__}")

    logger.info(
        "Reconciliation checked %d stale records and updated %d",
        len(records),
        reconciled,
    )
    if failures:
        raise RuntimeError("Reconciliation failures: " + ", ".join(failures))
    return {"checked": len(records), "reconciled": reconciled}
