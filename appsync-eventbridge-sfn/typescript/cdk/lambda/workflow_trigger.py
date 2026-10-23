import datetime
import decimal
import json
import logging
import os

import boto3
from botocore.exceptions import ClientError

logger = logging.getLogger()
logger.setLevel(logging.INFO)

WORKFLOW_REGISTRY_TABLE_NAME = os.environ["WORKFLOW_REGISTRY_TABLE_NAME"]
WORKFLOW_EXECUTION_TRACKER_TABLE_NAME = os.environ["WORKFLOW_EXECUTION_TRACKER_TABLE_NAME"]
EXECUTION_RETENTION_DAYS = int(os.environ["EXECUTION_RETENTION_DAYS"])

_dynamodb = boto3.resource("dynamodb")
_registry_table = _dynamodb.Table(WORKFLOW_REGISTRY_TABLE_NAME)
_execution_table = _dynamodb.Table(WORKFLOW_EXECUTION_TRACKER_TABLE_NAME)
_stepfunctions = boto3.client("stepfunctions")
_TERMINAL_STATUSES = {"SUCCEEDED", "FAILED", "TIMED_OUT", "ABORTED", "REJECTED"}


def _json_default(value):
    if isinstance(value, decimal.Decimal):
        return int(value) if value % 1 == 0 else float(value)
    raise TypeError(f"Cannot serialize {type(value).__name__}")


def _conditional_update(execution_id, status, allowed_statuses, **attributes):
    names = {"#status": "status"}
    values = {":status": status}
    assignments = ["#status = :status"]
    allowed_tokens = []
    for index, allowed_status in enumerate(allowed_statuses):
        token = f":allowed{index}"
        values[token] = allowed_status
        allowed_tokens.append(token)
    for index, (name, value) in enumerate(attributes.items()):
        name_token = f"#name{index}"
        value_token = f":value{index}"
        names[name_token] = name
        values[value_token] = value
        assignments.append(f"{name_token} = {value_token}")

    try:
        _execution_table.update_item(
            Key={"executionId": execution_id},
            UpdateExpression="SET " + ", ".join(assignments),
            ExpressionAttributeNames=names,
            ExpressionAttributeValues=values,
            ConditionExpression=f"attribute_exists(executionId) AND #status IN ({', '.join(allowed_tokens)})",
        )
        return True
    except ClientError as error:
        if error.response.get("Error", {}).get("Code") == "ConditionalCheckFailedException":
            return False
        raise


def _execution_arn(state_machine_arn, execution_id):
    prefix, qualified_name = state_machine_arn.split(":stateMachine:", 1)
    state_machine_name = qualified_name.split(":", 1)[0]
    return f"{prefix}:execution:{state_machine_name}:{execution_id}"


def _reconcile_existing(execution_id, state_machine_arn):
    execution_arn = _execution_arn(state_machine_arn, execution_id)
    response = _stepfunctions.describe_execution(executionArn=execution_arn)
    status = response["status"]
    attributes = {
        "executionArn": execution_arn,
        "startedAt": response["startDate"].isoformat(),
        "lastUpdatedAt": datetime.datetime.now(datetime.timezone.utc).isoformat(),
    }
    if status in _TERMINAL_STATUSES:
        stop_date = response.get("stopDate") or datetime.datetime.now(datetime.timezone.utc)
        attributes["finishedAt"] = stop_date.isoformat()
        attributes["expiresAt"] = int(
            (stop_date + datetime.timedelta(days=EXECUTION_RETENTION_DAYS)).timestamp()
        )
    _conditional_update(execution_id, status, ["STARTING"], **attributes)
    return {"executionArn": execution_arn, "status": status, "reconciled": True}


def _reject(execution_id, current_status, error):
    finished_at = datetime.datetime.now(datetime.timezone.utc)
    _conditional_update(
        execution_id,
        "REJECTED",
        [current_status],
        error=error,
        finishedAt=finished_at.isoformat(),
        lastUpdatedAt=finished_at.isoformat(),
        expiresAt=int(
            (finished_at + datetime.timedelta(days=EXECUTION_RETENTION_DAYS)).timestamp()
        ),
    )


def lambda_handler(event, _context):
    detail = event.get("detail", {})
    execution_id = detail.get("executionId")
    workflow_type = detail.get("workflowType")
    if not execution_id or not workflow_type:
        raise ValueError("Workflow event must include executionId and workflowType")

    execution = _execution_table.get_item(
        Key={"executionId": execution_id},
        ConsistentRead=True,
    ).get("Item")
    if execution is None:
        logger.warning("Ignoring event for unknown execution %s", execution_id)
        return {"ignored": True}

    current_status = execution.get("status", "REQUESTED")
    if execution.get("workflowType") != workflow_type:
        if current_status not in _TERMINAL_STATUSES:
            _reject(execution_id, current_status, "WorkflowTypeMismatch")
        return {"rejected": True}
    if current_status in _TERMINAL_STATUSES or current_status in {
        "RUNNING",
        "PENDING_REDRIVE",
    }:
        logger.info(
            "Ignoring duplicate event for execution %s in status %s",
            execution_id,
            current_status,
        )
        return {"duplicate": True, "status": current_status}
    if current_status == "STARTING":
        state_machine_arn = execution.get("stateMachineArn")
        if not state_machine_arn:
            logger.warning("STARTING execution %s has no state machine ARN", execution_id)
            return {"pendingReconciliation": True}
        try:
            return _reconcile_existing(execution_id, state_machine_arn)
        except ClientError as error:
            if error.response.get("Error", {}).get("Code") in {
                "ExecutionDoesNotExist",
                "ExecutionDoesNotExistException",
            }:
                logger.info("STARTING execution %s has not started yet", execution_id)
                return {"pendingReconciliation": True}
            raise

    workflow = _registry_table.get_item(
        Key={"workflowType": workflow_type},
        ConsistentRead=True,
    ).get("Item")
    if workflow is None or not workflow.get("enabled", True):
        _reject(execution_id, current_status, "WorkflowNotRegistered")
        return {"rejected": True}
    if workflow.get("stateMachineType", "STANDARD") != "STANDARD":
        _reject(execution_id, current_status, "UnsupportedStateMachineType")
        return {"rejected": True}

    state_machine_arn = workflow["stateMachineArn"]
    claimed = _conditional_update(
        execution_id,
        "STARTING",
        ["REQUESTED", "DISPATCH_FAILED", "START_FAILED"],
        stateMachineArn=state_machine_arn,
        lastUpdatedAt=datetime.datetime.now(datetime.timezone.utc).isoformat(),
    )
    if not claimed:
        logger.info("Execution %s was claimed by another invocation", execution_id)
        return {"duplicate": True}

    try:
        response = _stepfunctions.start_execution(
            stateMachineArn=state_machine_arn,
            name=execution_id,
            input=json.dumps(execution.get("requestPayload", {}), default=_json_default),
        )
        started_at = response["startDate"].isoformat()
        _conditional_update(
            execution_id,
            "RUNNING",
            ["STARTING"],
            executionArn=response["executionArn"],
            startedAt=started_at,
            lastUpdatedAt=started_at,
        )
        logger.info("Started execution %s for workflow %s", execution_id, workflow_type)
        return {"executionArn": response["executionArn"]}
    except ClientError as error:
        error_code = error.response.get("Error", {}).get("Code", "StartExecutionFailed")
        if error_code == "ExecutionAlreadyExists":
            logger.warning("Reconciling already-started execution %s", execution_id)
            return _reconcile_existing(execution_id, state_machine_arn)
        _conditional_update(
            execution_id,
            "START_FAILED",
            ["STARTING"],
            error=error_code,
            cause=error.response.get("Error", {}).get("Message", str(error)),
            lastUpdatedAt=datetime.datetime.now(datetime.timezone.utc).isoformat(),
        )
        raise
    except Exception as error:
        _conditional_update(
            execution_id,
            "START_FAILED",
            ["STARTING"],
            error=type(error).__name__,
            cause=str(error),
            lastUpdatedAt=datetime.datetime.now(datetime.timezone.utc).isoformat(),
        )
        raise
