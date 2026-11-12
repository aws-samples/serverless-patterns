import base64
import binascii
import decimal
import datetime
import hashlib
import json
import logging
import os
import re
import uuid

import boto3
import fastjsonschema
from botocore.exceptions import ClientError

logger = logging.getLogger()
logger.setLevel(logging.INFO)

WORKFLOW_REGISTRY_TABLE_NAME = os.environ["WORKFLOW_REGISTRY_TABLE_NAME"]
WORKFLOW_EXECUTION_TRACKER_TABLE_NAME = os.environ["WORKFLOW_EXECUTION_TRACKER_TABLE_NAME"]
REQUESTER_WORKFLOW_TYPE_INDEX_NAME = os.environ["REQUESTER_WORKFLOW_TYPE_INDEX_NAME"]
WORKFLOW_TYPE_INDEX_NAME = os.environ["WORKFLOW_TYPE_INDEX_NAME"]
WORKFLOW_EVENT_BUS_NAME = os.environ["WORKFLOW_EVENT_BUS_NAME"]
WORKFLOW_EVENT_SOURCE = os.environ["WORKFLOW_EVENT_SOURCE"]
WORKFLOW_EVENT_DETAIL_TYPE = os.environ["WORKFLOW_EVENT_DETAIL_TYPE"]
MAX_REQUEST_PAYLOAD_BYTES = int(os.environ.get("MAX_REQUEST_PAYLOAD_BYTES", "131072"))
ADMIN_GROUPS = frozenset(json.loads(os.environ.get("ADMIN_GROUPS", "[]")))

_dynamodb = boto3.resource("dynamodb")
_registry_table = _dynamodb.Table(WORKFLOW_REGISTRY_TABLE_NAME)
_execution_table = _dynamodb.Table(WORKFLOW_EXECUTION_TRACKER_TABLE_NAME)
_eventbridge = boto3.client("events")
_stepfunctions = boto3.client("stepfunctions")
_schema_validators = {}
_TERMINAL_STATUSES = {"SUCCEEDED", "FAILED", "TIMED_OUT", "ABORTED", "REJECTED"}


def _schema_validator(workflow):
    schema = workflow.get("inputSchema")
    if not isinstance(schema, dict):
        raise ValueError("Workflow has no valid input schema")

    normalized_schema = json.loads(json.dumps(schema, default=_json_default))
    schema_key = workflow.get("schemaHash") or hashlib.sha256(
        json.dumps(
            normalized_schema,
            sort_keys=True,
            separators=(",", ":"),
        ).encode("utf-8")
    ).hexdigest()
    validator = _schema_validators.get(schema_key)
    if validator is None:
        try:
            validator = fastjsonschema.compile(normalized_schema)
        except fastjsonschema.JsonSchemaException as error:
            logger.error("Stored schema is invalid for workflow %s: %s", workflow.get("workflowType"), error)
            raise ValueError("Workflow input schema is invalid") from error
        _schema_validators[schema_key] = validator
    return validator


def _validate_parameters(workflow, parameters):
    if workflow.get("contractStatus") != "ACTIVE":
        raise ValueError("Workflow input contract is not active")
    try:
        _schema_validator(workflow)(parameters)
    except fastjsonschema.JsonSchemaValueException as error:
        raise ValueError(f"Invalid workflow parameters: {error.message}") from error


def _json_default(value):
    if isinstance(value, decimal.Decimal):
        return int(value) if value % 1 == 0 else float(value)
    raise TypeError(f"Cannot serialize {type(value).__name__}")


def _principal_arn(identity):
    """The caller's IAM principal, reduced to the role for assumed-role sessions.

    Assumed-role session ARNs carry an ephemeral session name
    (arn:...:assumed-role/ROLE/SESSION); stripping it yields the stable role
    identity used for role-level authorization.
    """
    principal = identity.get("userArn") or identity.get("username")
    if not principal:
        return None
    if ":assumed-role/" in principal:
        principal = principal.rsplit("/", 1)[0]
    return principal


def _requester_subject(event):
    """Stable per-user identity for ownership and per-requester listing.

    Prefers a user-level identifier when the authorization context supplies one
    (a Cognito Identity Pool identity id, or a user pool / OIDC subject) and
    falls back to the caller's IAM principal when there is no user-level
    identity (e.g. a service role calling with SigV4). Ownership is therefore
    per-user wherever the identity source supports it, and per-principal
    otherwise. The pattern never provisions an identity source itself; it reads
    whatever the caller authenticated with.
    """
    identity = event.get("identity") or {}
    subject = (
        identity.get("cognitoIdentityId")
        or identity.get("sub")
        or _principal_arn(identity)
    )
    if not subject:
        raise PermissionError("Unable to identify the AppSync caller")
    return subject


def _requester_principal(event):
    """The caller's IAM principal (role for assumed-role sessions).

    Used for role/group-level authorization such as allowedCallers, which is
    deliberately coarser than the per-user subject used for ownership.
    """
    identity = event.get("identity") or {}
    principal = _principal_arn(identity)
    if not principal:
        raise PermissionError("Unable to identify the AppSync caller")
    return principal


_ASSUMED_ROLE_ARN = re.compile(
    r"^arn:(?P<partition>[^:]+):sts::(?P<account>\d+):assumed-role/(?P<role>.+)$"
)


def _caller_identities(principal):
    """Identities a caller may be matched by in a workflow allowedCallers list.

    IAM authorization surfaces an assumed role as an STS ARN
    (arn:PARTITION:sts::ACCOUNT:assumed-role/ROLE), but operators usually think
    in IAM role ARNs (arn:PARTITION:iam::ACCOUNT:role/ROLE). Accept both forms.
    Roles that use an IAM path are not fully reconstructable from the STS form
    and should be listed using their assumed-role ARN.
    """
    identities = {principal}
    match = _ASSUMED_ROLE_ARN.match(principal)
    if match:
        identities.add(
            "arn:{partition}:iam::{account}:role/{role}".format(
                partition=match.group("partition"),
                account=match.group("account"),
                role=match.group("role"),
            )
        )
    return identities


def _require_admin(event):
    """Authorize an admin-only field.

    An IAM caller that reaches the resolver was already vetted by the admin
    field-level IAM policy, so it passes. A user-pool caller must belong to one
    of the configured admin Cognito groups (the adminGroups construct prop).
    With no admin groups configured, user-pool callers are always denied - and
    the admin fields are IAM-only at the schema level anyway, so this is a
    defense-in-depth backstop.
    """
    identity = event.get("identity") or {}
    if identity.get("userArn"):
        return
    if not ADMIN_GROUPS.intersection(_caller_groups(event)):
        raise PermissionError("Administrator access is required for this operation")


def _caller_groups(event):
    """Cognito groups the caller belongs to (empty for non-user-pool callers).

    Under Cognito User Pool authorization AppSync exposes the token's
    cognito:groups claim as identity.groups (a list). Fall back to the raw
    claim, which may be a list or a delimited string, for safety.
    """
    identity = event.get("identity") or {}
    groups = identity.get("groups")
    if groups is None:
        claims = identity.get("claims") or {}
        groups = claims.get("cognito:groups")
    if isinstance(groups, str):
        groups = [part for part in re.split(r"[,\s]+", groups) if part]
    if not isinstance(groups, list):
        return []
    return [group for group in groups if isinstance(group, str) and group]


def _parse_parameters(value):
    if isinstance(value, str):
        try:
            value = json.loads(value)
        except json.JSONDecodeError as error:
            raise ValueError("parameters must contain valid JSON") from error
    if not isinstance(value, dict):
        raise ValueError("parameters must be a JSON object")
    serialized = json.dumps(value, sort_keys=True, separators=(",", ":"), default=_json_default)
    if len(serialized.encode("utf-8")) > MAX_REQUEST_PAYLOAD_BYTES:
        raise ValueError(f"parameters must not exceed {MAX_REQUEST_PAYLOAD_BYTES} bytes")
    return value, serialized


def _format_execution(item, include_requester=False):
    if item is None:
        return None
    result = dict(item)
    result["requestPayload"] = json.dumps(result.get("requestPayload", {}), default=_json_default)
    if "output" in result and not isinstance(result["output"], str):
        result["output"] = json.dumps(result["output"], default=_json_default)
    internal_fields = [
        "clientRequestToken",
        "requestHash",
        "requesterWorkflowType",
        "expiresAt",
    ]
    # requesterSubject / requesterPrincipal are retained only for the admin
    # cross-caller listing so an operator can see who ran each execution.
    if not include_requester:
        internal_fields += ["requesterSubject", "requesterPrincipal"]
    for internal_field in internal_fields:
        result.pop(internal_field, None)
    return json.loads(json.dumps(result, default=_json_default))


def _encode_next_token(last_evaluated_key):
    if not last_evaluated_key:
        return None
    serialized = json.dumps(last_evaluated_key, default=_json_default, separators=(",", ":"))
    return base64.urlsafe_b64encode(serialized.encode("utf-8")).decode("ascii")


def _decode_next_token(token):
    if not token:
        return None
    try:
        decoded = base64.urlsafe_b64decode(token.encode("ascii")).decode("utf-8")
        return json.loads(decoded)
    except (binascii.Error, UnicodeDecodeError, ValueError, json.JSONDecodeError) as error:
        raise ValueError("Invalid nextToken") from error


def _get_execution(arguments, subject):
    response = _execution_table.get_item(
        Key={"executionId": arguments["executionId"]},
        ConsistentRead=True,
    )
    item = response.get("Item")
    if item is None:
        return None
    if item.get("requesterSubject") != subject:
        raise PermissionError("Execution is not owned by the caller")
    return _format_execution(item)


def _cancel_execution(arguments, subject):
    """Cancel a caller's own running execution via Step Functions StopExecution.

    Ownership-scoped (like the read operations). Already-terminal executions are
    a no-op (returned as-is). The authoritative ABORTED state is written by the
    status handler when Step Functions emits the status-change event, so this
    returns the current record for the caller to poll.
    """
    execution_id = arguments["executionId"]
    item = _execution_table.get_item(
        Key={"executionId": execution_id},
        ConsistentRead=True,
    ).get("Item")
    if item is None:
        raise ValueError(f"Unknown execution: {execution_id}")
    if item.get("requesterSubject") != subject:
        raise PermissionError("Execution is not owned by the caller")
    if item.get("status") in _TERMINAL_STATUSES:
        return _format_execution(item)
    execution_arn = item.get("executionArn")
    if not execution_arn:
        raise ValueError("Execution has not started and cannot be cancelled yet")
    _stepfunctions.stop_execution(executionArn=execution_arn)
    logger.info("Requested cancellation of execution %s", execution_id)
    return _format_execution(item)


def _list_executions(arguments, subject):
    limit = arguments.get("limit") or 25
    if not 1 <= limit <= 100:
        raise ValueError("limit must be between 1 and 100")

    requester_workflow_type = f"{subject}#{arguments['workflowType']}"
    query = {
        "IndexName": REQUESTER_WORKFLOW_TYPE_INDEX_NAME,
        "KeyConditionExpression": "requesterWorkflowType = :requesterWorkflowType",
        "ExpressionAttributeValues": {":requesterWorkflowType": requester_workflow_type},
        "ScanIndexForward": False,
        "Limit": limit,
    }
    exclusive_start_key = _decode_next_token(arguments.get("nextToken"))
    if exclusive_start_key:
        query["ExclusiveStartKey"] = exclusive_start_key

    response = _execution_table.query(**query)
    return {
        "items": [_format_execution(item) for item in response.get("Items", [])],
        "nextToken": _encode_next_token(response.get("LastEvaluatedKey")),
    }


def _list_executions_by_type(arguments):
    """Admin listing: all executions of a workflow type, across all callers.

    Unlike listWorkflowExecutions, this is NOT scoped to the caller's own
    executions. Access is expected to be restricted to administrators at the
    AppSync field level (IAM), so this handler intentionally applies no
    per-caller filter.
    """
    limit = arguments.get("limit") or 25
    if not 1 <= limit <= 100:
        raise ValueError("limit must be between 1 and 100")
    workflow_type = arguments.get("workflowType")
    if not isinstance(workflow_type, str) or not workflow_type.strip():
        raise ValueError("workflowType must be a non-empty string")

    query = {
        "IndexName": WORKFLOW_TYPE_INDEX_NAME,
        "KeyConditionExpression": "workflowType = :workflowType",
        "ExpressionAttributeValues": {":workflowType": workflow_type.strip()},
        "ScanIndexForward": False,
        "Limit": limit,
    }
    exclusive_start_key = _decode_next_token(arguments.get("nextToken"))
    if exclusive_start_key:
        query["ExclusiveStartKey"] = exclusive_start_key

    response = _execution_table.query(**query)
    return {
        "items": [
            _format_execution(item, include_requester=True)
            for item in response.get("Items", [])
        ],
        "nextToken": _encode_next_token(response.get("LastEvaluatedKey")),
    }


def _publish_workflow_event(execution_id, workflow_type):
    response = _eventbridge.put_events(
        Entries=[
            {
                "EventBusName": WORKFLOW_EVENT_BUS_NAME,
                "Source": WORKFLOW_EVENT_SOURCE,
                "DetailType": WORKFLOW_EVENT_DETAIL_TYPE,
                "Detail": json.dumps(
                    {"executionId": execution_id, "workflowType": workflow_type},
                    separators=(",", ":"),
                ),
            }
        ]
    )
    if response.get("FailedEntryCount", 0):
        failure = response.get("Entries", [{}])[0]
        raise RuntimeError(failure.get("ErrorMessage", "EventBridge rejected the event"))


def _mark_dispatch_failed(execution_id, error):
    try:
        _execution_table.update_item(
            Key={"executionId": execution_id},
            UpdateExpression=(
                "SET #status = :failed, #error = :error, lastUpdatedAt = :updatedAt"
            ),
            ConditionExpression="#status IN (:requested, :dispatchFailed)",
            ExpressionAttributeNames={"#status": "status", "#error": "error"},
            ExpressionAttributeValues={
                ":failed": "DISPATCH_FAILED",
                ":requested": "REQUESTED",
                ":dispatchFailed": "DISPATCH_FAILED",
                ":error": type(error).__name__,
                ":updatedAt": datetime.datetime.now(datetime.timezone.utc).isoformat(),
            },
        )
    except ClientError as update_error:
        if update_error.response.get("Error", {}).get("Code") != "ConditionalCheckFailedException":
            raise


def _request_workflow(arguments, subject, principal, groups):
    workflow_type = arguments.get("workflowType")
    if not isinstance(workflow_type, str) or not workflow_type.strip():
        raise ValueError("workflowType must be a non-empty string")
    workflow_type = workflow_type.strip()

    token = arguments.get("clientRequestToken")
    if not isinstance(token, str) or not token.strip() or len(token) > 128:
        raise ValueError("clientRequestToken must be between 1 and 128 characters")
    token = token.strip()
    parameters, canonical_parameters = _parse_parameters(arguments.get("parameters"))

    registry_response = _registry_table.get_item(
        Key={"workflowType": workflow_type},
        ConsistentRead=True,
    )
    workflow = registry_response.get("Item")
    if workflow is None or not workflow.get("enabled", True):
        raise ValueError(f"Unknown or disabled workflow type: {workflow_type}")
    if workflow.get("stateMachineType", "STANDARD") != "STANDARD":
        raise ValueError("Only Standard Step Functions workflows are supported")

    # Optional per-workflow authorization. When a contract defines allowedCallers,
    # the caller must match at least one entry. An absent or empty list leaves
    # the workflow open to any authorized API caller (default behavior).
    #
    # A caller is matched by: an IAM principal/role ARN, their immutable per-user
    # subject (Cognito sub / identity id), or any Cognito group (bare name or
    # "group:<name>"). Bare Cognito usernames are intentionally NOT matchable:
    # a username can be deleted and recreated (reused) with a new sub, so a
    # username entry could let a different person inherit access. Authorize
    # user-pool callers by group or by subject instead.
    allowed_callers = workflow.get("allowedCallers")
    if allowed_callers:
        # Authorization is by ROLE or GROUP only, never by an individual identity.
        # Match on IAM principal/role ARNs and Cognito groups. Deliberately NOT
        # matchable:
        #   - bare usernames: recyclable, so a recreated user could inherit access
        #   - the per-user subject (sub / cognitoIdentityId): pinning individual
        #     users into a workflow contract is the wrong model; put the user in a
        #     group instead.
        # Services remain matchable because their principal is itself a role ARN.
        caller_identities = set()
        if principal.startswith("arn:"):
            caller_identities |= _caller_identities(principal)
        for group in groups:
            caller_identities.add(group)
            caller_identities.add(f"group:{group}")
        if not caller_identities.intersection(allowed_callers):
            logger.warning(
                "Caller principal %s / subject %s / groups %s is not authorized "
                "for workflow %s",
                principal,
                subject,
                groups,
                workflow_type,
            )
            raise PermissionError(
                f"Caller is not authorized to request workflow type: {workflow_type}"
            )

    _validate_parameters(workflow, parameters)

    execution_id = str(
        uuid.uuid5(uuid.NAMESPACE_URL, f"{subject}\0{workflow_type}\0{token}")
    )
    request_hash = hashlib.sha256(canonical_parameters.encode("utf-8")).hexdigest()
    requested_at = datetime.datetime.now(datetime.timezone.utc).isoformat()
    execution_record = {
        "executionId": execution_id,
        "workflowType": workflow_type,
        "requestPayload": parameters,
        "requestHash": request_hash,
        "clientRequestToken": token,
        "requesterSubject": subject,
        "requesterPrincipal": principal,
        "requesterWorkflowType": f"{subject}#{workflow_type}",
        "status": "REQUESTED",
        "requestedAt": requested_at,
        "lastUpdatedAt": requested_at,
    }

    is_new = True
    try:
        _execution_table.put_item(
            Item=execution_record,
            ConditionExpression="attribute_not_exists(executionId)",
        )
        current = execution_record
    except ClientError as error:
        if error.response.get("Error", {}).get("Code") != "ConditionalCheckFailedException":
            raise
        is_new = False
        current = _execution_table.get_item(
            Key={"executionId": execution_id},
            ConsistentRead=True,
        ).get("Item")
        if current is None:
            raise RuntimeError("Idempotent execution record could not be read")
        if current.get("requestHash") != request_hash:
            raise ValueError("clientRequestToken was already used with different parameters")

    if is_new or current.get("status") in {"REQUESTED", "DISPATCH_FAILED", "START_FAILED"}:
        try:
            _publish_workflow_event(execution_id, workflow_type)
        except Exception as error:
            logger.exception("Failed to publish workflow event for %s", execution_id)
            _mark_dispatch_failed(execution_id, error)
            raise RuntimeError("Unable to queue workflow execution") from error

    logger.info("Accepted workflow execution %s for type %s", execution_id, workflow_type)
    return {
        "executionId": execution_id,
        "workflowType": workflow_type,
        "status": current.get("status", "REQUESTED"),
        "requestedAt": current["requestedAt"],
    }


def lambda_handler(event, _context):
    field_name = event.get("info", {}).get("fieldName")
    arguments = event.get("arguments", {})
    logger.info("Processing AppSync field %s", field_name)

    if field_name == "requestWorkflow":
        return _request_workflow(
            arguments,
            _requester_subject(event),
            _requester_principal(event),
            _caller_groups(event),
        )
    if field_name == "cancelWorkflowExecution":
        return _cancel_execution(arguments, _requester_subject(event))
    if field_name == "getWorkflowExecution":
        return _get_execution(arguments, _requester_subject(event))
    if field_name == "listWorkflowExecutions":
        return _list_executions(arguments, _requester_subject(event))
    if field_name == "listWorkflowExecutionsByType":
        _require_admin(event)
        return _list_executions_by_type(arguments)
    raise ValueError(f"Unsupported AppSync field: {field_name}")
