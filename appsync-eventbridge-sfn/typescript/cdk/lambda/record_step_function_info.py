import base64
import binascii
import datetime
import decimal
import hashlib
import json
import logging
import os
import re

import boto3
import fastjsonschema
from boto3.dynamodb.conditions import Key
from botocore.exceptions import ClientError

logger = logging.getLogger()
logger.setLevel(logging.INFO)

WORKFLOW_REGISTRY_TABLE_NAME = os.environ["WORKFLOW_REGISTRY_TABLE_NAME"]
STATE_MACHINE_ARN_INDEX_NAME = os.environ["STATE_MACHINE_ARN_INDEX_NAME"]
REQUIRE_WORKFLOW_TYPE_TAG = (
    os.environ.get("REQUIRE_WORKFLOW_TYPE_TAG", "true").lower() == "true"
)
REQUIRE_EXPLICIT_SCHEMA = (
    os.environ.get("REQUIRE_EXPLICIT_SCHEMA", "true").lower() == "true"
)
MAX_SCHEMA_BYTES = int(os.environ.get("MAX_SCHEMA_BYTES", "131072"))
MAX_ALLOWED_CALLERS = int(os.environ.get("MAX_ALLOWED_CALLERS", "50"))
MAX_CALLER_LENGTH = 2048
ADMIN_GROUPS = frozenset(json.loads(os.environ.get("ADMIN_GROUPS", "[]")))

_dynamodb = boto3.resource("dynamodb")
_registry_table = _dynamodb.Table(WORKFLOW_REGISTRY_TABLE_NAME)
_stepfunctions = boto3.client("stepfunctions")

_UUID_SUFFIX = re.compile(
    r"-[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[1-5][0-9a-fA-F]{3}-"
    r"[89abAB][0-9a-fA-F]{3}-[0-9a-fA-F]{12}$"
)
_JSON_PATH_PARAMETER = re.compile(r"\$\.([a-zA-Z_][a-zA-Z0-9_]*)")


def _json_default(value):
    if isinstance(value, decimal.Decimal):
        return int(value) if value % 1 == 0 else float(value)
    raise TypeError(f"Cannot serialize {type(value).__name__}")


def extract_parameters(definition):
    """Infer top-level JSONPath inputs from the first state as a draft contract."""
    try:
        definition_dict = json.loads(definition)
    except json.JSONDecodeError as error:
        logger.error("Unable to parse state machine definition: %s", error)
        return []

    start_state = definition_dict.get("States", {}).get(definition_dict.get("StartAt"))
    if not isinstance(start_state, dict):
        logger.warning("State machine definition has no valid start state")
        return []
    return sorted(
        {match.group(1) for match in _JSON_PATH_PARAMETER.finditer(json.dumps(start_state))}
    )


def _inferred_schema(required_parameters):
    return {
        "type": "object",
        "required": required_parameters,
        "properties": {parameter: {} for parameter in required_parameters},
        "additionalProperties": True,
    }


def _parse_schema(value):
    if isinstance(value, str):
        try:
            value = json.loads(value)
        except json.JSONDecodeError as error:
            raise ValueError("inputSchema must contain valid JSON") from error
    if not isinstance(value, dict):
        raise ValueError("inputSchema must be a JSON object")
    if value.get("type") != "object":
        raise ValueError("inputSchema must declare a top-level object type")

    canonical = json.dumps(value, sort_keys=True, separators=(",", ":"))
    if len(canonical.encode("utf-8")) > MAX_SCHEMA_BYTES:
        raise ValueError(f"inputSchema must not exceed {MAX_SCHEMA_BYTES} bytes")
    try:
        fastjsonschema.compile(value)
    except fastjsonschema.JsonSchemaException as error:
        # Schema-definition errors (JsonSchemaDefinitionException) do not carry a
        # .message attribute, so fall back to str(error).
        detail = getattr(error, "message", None) or str(error)
        raise ValueError(f"inputSchema is invalid: {detail}") from error
    return value, canonical, hashlib.sha256(canonical.encode("utf-8")).hexdigest()


def _parse_allowed_callers(value):
    """Validate the optional allowedCallers list on a workflow contract.

    Returns None when the argument is omitted (leave any existing value
    unchanged), an empty list when the restriction should be cleared, or a
    deduplicated list of principal identifiers to enforce.
    """
    if value is None:
        return None
    if not isinstance(value, list):
        raise ValueError("allowedCallers must be a list of principal identifiers")
    if len(value) > MAX_ALLOWED_CALLERS:
        raise ValueError(
            f"allowedCallers must not exceed {MAX_ALLOWED_CALLERS} entries"
        )
    deduped = []
    seen = set()
    for entry in value:
        if not isinstance(entry, str) or not entry.strip():
            raise ValueError("allowedCallers entries must be non-empty strings")
        entry = entry.strip()
        if len(entry) > MAX_CALLER_LENGTH:
            raise ValueError(
                f"allowedCallers entries must not exceed {MAX_CALLER_LENGTH} characters"
            )
        if entry not in seen:
            seen.add(entry)
            deduped.append(entry)
    return deduped


def _tag_map(state_machine_arn):
    response = _stepfunctions.list_tags_for_resource(resourceArn=state_machine_arn)
    return {tag["key"]: tag.get("value", "") for tag in response.get("tags", [])}


def _workflow_type(state_machine_name, tags):
    tagged_type = tags.get("workflowType", "").strip()
    if tagged_type:
        return tagged_type
    if REQUIRE_WORKFLOW_TYPE_TAG:
        return None
    return _UUID_SUFFIX.sub("", state_machine_name)


def _find_state_machine_arn(detail):
    request_parameters = detail.get("requestParameters") or {}
    response_elements = detail.get("responseElements") or {}
    arn = (
        response_elements.get("stateMachineArn")
        or request_parameters.get("stateMachineArn")
        or request_parameters.get("resourceArn")
    )
    if arn:
        return arn
    for resource in detail.get("resources") or []:
        if (
            resource.get("type") == "AWS::StepFunctions::StateMachine"
            and resource.get("ARN")
        ):
            return resource["ARN"]
    return None


def _requester_id(event):
    identity = event.get("identity") or {}
    requester = identity.get("sub") or identity.get("userArn") or identity.get(
        "username"
    )
    if not requester:
        raise PermissionError("Unable to identify the AppSync caller")
    return requester


def _caller_groups(event):
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


def _require_admin(event):
    """Authorize an admin-only field.

    An IAM caller that reaches the resolver was already vetted by the admin
    field-level IAM policy, so it passes. A user-pool caller must belong to one
    of the configured admin Cognito groups (the adminGroups construct prop).
    With no admin groups configured, user-pool callers are always denied.
    """
    identity = event.get("identity") or {}
    if identity.get("userArn"):
        return
    if not ADMIN_GROUPS.intersection(_caller_groups(event)):
        raise PermissionError("Administrator access is required for this operation")


def _format_registration(item):
    result = dict(item)
    for field in ("inputSchema", "inferredInputSchema"):
        if field in result:
            result[field] = json.dumps(result[field], default=_json_default)
    return json.loads(json.dumps(result, default=_json_default))


def _remove_registration(state_machine_arn):
    response = _registry_table.query(
        IndexName=STATE_MACHINE_ARN_INDEX_NAME,
        KeyConditionExpression=Key("stateMachineArn").eq(state_machine_arn),
    )
    for item in response.get("Items", []):
        try:
            _registry_table.delete_item(
                Key={"workflowType": item["workflowType"]},
                ConditionExpression="stateMachineArn = :stateMachineArn",
                ExpressionAttributeValues={":stateMachineArn": state_machine_arn},
            )
            logger.info("Removed workflow registration %s", item["workflowType"])
        except ClientError as error:
            if (
                error.response.get("Error", {}).get("Code")
                != "ConditionalCheckFailedException"
            ):
                raise


def _remove_renamed_registrations(state_machine_arn, workflow_type):
    response = _registry_table.query(
        IndexName=STATE_MACHINE_ARN_INDEX_NAME,
        KeyConditionExpression=Key("stateMachineArn").eq(state_machine_arn),
    )
    for item in response.get("Items", []):
        if item["workflowType"] != workflow_type:
            _registry_table.delete_item(
                Key={"workflowType": item["workflowType"]},
                ConditionExpression="stateMachineArn = :stateMachineArn",
                ExpressionAttributeValues={":stateMachineArn": state_machine_arn},
            )
            logger.info(
                "Removed renamed workflow registration %s", item["workflowType"]
            )


def _initialize_contract(workflow_type, state_machine_arn, inferred_schema):
    if REQUIRE_EXPLICIT_SCHEMA:
        update_expression = (
            "SET contractStatus = :status, #enabled = :enabled, "
            "schemaSource = :source"
        )
        values = {
            ":status": "PENDING_CONTRACT",
            ":enabled": False,
            ":source": "INFERRED_DRAFT",
        }
    else:
        canonical = json.dumps(
            inferred_schema, sort_keys=True, separators=(",", ":")
        )
        update_expression = (
            "SET contractStatus = :status, #enabled = :enabled, "
            "schemaSource = :source, inputSchema = :schema, "
            "schemaVersion = :version, schemaHash = :hash"
        )
        values = {
            ":status": "ACTIVE",
            ":enabled": True,
            ":source": "INFERRED",
            ":schema": inferred_schema,
            ":version": "inferred",
            ":hash": hashlib.sha256(canonical.encode("utf-8")).hexdigest(),
        }

    try:
        _registry_table.update_item(
            Key={"workflowType": workflow_type},
            UpdateExpression=update_expression,
            ConditionExpression=(
                "stateMachineArn = :stateMachineArn "
                "AND attribute_not_exists(contractStatus)"
            ),
            ExpressionAttributeNames={"#enabled": "enabled"},
            ExpressionAttributeValues={
                **values,
                ":stateMachineArn": state_machine_arn,
            },
        )
    except ClientError as error:
        if (
            error.response.get("Error", {}).get("Code")
            != "ConditionalCheckFailedException"
        ):
            raise


def _upsert_discovered_workflow(state_machine_arn):
    description = _stepfunctions.describe_state_machine(
        stateMachineArn=state_machine_arn
    )
    tags = _tag_map(state_machine_arn)
    workflow_type = _workflow_type(description["name"], tags)
    if workflow_type is None:
        _remove_registration(state_machine_arn)
        logger.info("Ignoring untagged state machine %s", state_machine_arn)
        return None

    state_machine_type = description.get("type", "STANDARD")
    required_parameters = extract_parameters(description["definition"])
    inferred_schema = _inferred_schema(required_parameters)
    now = datetime.datetime.now(datetime.timezone.utc).isoformat()

    _remove_renamed_registrations(state_machine_arn, workflow_type)
    _registry_table.update_item(
        Key={"workflowType": workflow_type},
        UpdateExpression=(
            "SET stateMachineArn = :stateMachineArn, "
            "stateMachineType = :stateMachineType, "
            "requiredParameters = :requiredParameters, "
            "inferredInputSchema = :inferredInputSchema, "
            "registrationSource = :registrationSource, updatedAt = :updatedAt"
        ),
        ConditionExpression=(
            "attribute_not_exists(workflowType) OR stateMachineArn = :stateMachineArn"
        ),
        ExpressionAttributeValues={
            ":stateMachineArn": state_machine_arn,
            ":stateMachineType": state_machine_type,
            ":requiredParameters": required_parameters,
            ":inferredInputSchema": inferred_schema,
            ":registrationSource": "EVENTBRIDGE_DISCOVERY",
            ":updatedAt": now,
        },
    )
    _initialize_contract(workflow_type, state_machine_arn, inferred_schema)

    if state_machine_type != "STANDARD":
        _registry_table.update_item(
            Key={"workflowType": workflow_type},
            UpdateExpression="SET #enabled = :enabled, contractStatus = :status",
            ExpressionAttributeNames={"#enabled": "enabled"},
            ExpressionAttributeValues={
                ":enabled": False,
                ":status": "UNSUPPORTED_WORKFLOW_TYPE",
            },
        )

    logger.info(
        "Discovered workflow %s with contract status %s",
        workflow_type,
        "PENDING_CONTRACT" if REQUIRE_EXPLICIT_SCHEMA else "ACTIVE",
    )
    return workflow_type


def _get_workflow_registration(arguments):
    workflow_type = arguments.get("workflowType")
    if not isinstance(workflow_type, str) or not workflow_type.strip():
        raise ValueError("workflowType must be a non-empty string")
    response = _registry_table.get_item(
        Key={"workflowType": workflow_type.strip()},
        ConsistentRead=True,
    )
    item = response.get("Item")
    return _format_registration(item) if item else None


def _encode_next_token(last_evaluated_key):
    if not last_evaluated_key:
        return None
    serialized = json.dumps(
        last_evaluated_key, default=_json_default, separators=(",", ":")
    )
    return base64.urlsafe_b64encode(serialized.encode("utf-8")).decode("ascii")


def _decode_next_token(token):
    if not token:
        return None
    try:
        decoded = base64.urlsafe_b64decode(token.encode("ascii")).decode("utf-8")
        return json.loads(decoded)
    except (binascii.Error, UnicodeDecodeError, ValueError, json.JSONDecodeError) as error:
        raise ValueError("Invalid nextToken") from error


def _list_workflow_registrations(arguments):
    """Catalog listing: all registered workflows (self-service discovery).

    Scans the small registry table (one item per workflow type) with
    pagination. Not scoped to the caller - this is the discoverable catalog.
    """
    limit = arguments.get("limit") or 25
    if not 1 <= limit <= 100:
        raise ValueError("limit must be between 1 and 100")
    scan_kwargs = {"Limit": limit}
    exclusive_start_key = _decode_next_token(arguments.get("nextToken"))
    if exclusive_start_key:
        scan_kwargs["ExclusiveStartKey"] = exclusive_start_key
    response = _registry_table.scan(**scan_kwargs)
    return {
        "items": [_format_registration(item) for item in response.get("Items", [])],
        "nextToken": _encode_next_token(response.get("LastEvaluatedKey")),
    }


def _register_workflow_contract(event):
    _require_admin(event)
    arguments = event.get("arguments", {})
    workflow_type = arguments.get("workflowType")
    state_machine_arn = arguments.get("stateMachineArn")
    schema_version = arguments.get("schemaVersion")
    if not isinstance(workflow_type, str) or not workflow_type.strip():
        raise ValueError("workflowType must be a non-empty string")
    workflow_type = workflow_type.strip()

    # stateMachineArn is optional for an already-discovered workflow. A tagged
    # state machine auto-registers (as PENDING_CONTRACT by default), so an admin
    # can activate it by supplying just the schema; the ARN is resolved from the
    # existing registry record. It is still required for a brand-new, never
    # discovered direct registration.
    if state_machine_arn is None:
        existing = _registry_table.get_item(
            Key={"workflowType": workflow_type},
            ConsistentRead=True,
        ).get("Item")
        if existing is None or not existing.get("stateMachineArn"):
            raise ValueError(
                "stateMachineArn is required when the workflow has not been discovered"
            )
        state_machine_arn = existing["stateMachineArn"]
    elif not isinstance(state_machine_arn, str) or not state_machine_arn.strip():
        raise ValueError("stateMachineArn must be a non-empty string")
    else:
        state_machine_arn = state_machine_arn.strip()

    if (
        not isinstance(schema_version, str)
        or not schema_version.strip()
        or len(schema_version) > 64
    ):
        raise ValueError("schemaVersion must be between 1 and 64 characters")

    schema_version = schema_version.strip()
    input_schema, _canonical, schema_hash = _parse_schema(
        arguments.get("inputSchema")
    )
    allowed_callers = _parse_allowed_callers(arguments.get("allowedCallers"))

    description = _stepfunctions.describe_state_machine(
        stateMachineArn=state_machine_arn
    )
    if description.get("type", "STANDARD") != "STANDARD":
        raise ValueError("Only Standard Step Functions workflows are supported")

    tags = _tag_map(state_machine_arn)
    tagged_workflow_type = tags.get("workflowType", "").strip()
    if REQUIRE_WORKFLOW_TYPE_TAG and tagged_workflow_type != workflow_type:
        raise ValueError(
            "The state machine workflowType tag must match the registration"
        )

    required_parameters = input_schema.get("required", [])
    if not isinstance(required_parameters, list) or not all(
        isinstance(parameter, str) for parameter in required_parameters
    ):
        raise ValueError("inputSchema required must be a list of property names")

    now = datetime.datetime.now(datetime.timezone.utc).isoformat()
    set_clause = (
        "SET stateMachineArn = :stateMachineArn, "
        "stateMachineType = :stateMachineType, inputSchema = :inputSchema, "
        "schemaVersion = :schemaVersion, schemaHash = :schemaHash, "
        "schemaSource = :schemaSource, contractStatus = :contractStatus, "
        "requiredParameters = :requiredParameters, "
        "#enabled = :enabled, contractUpdatedAt = :updatedAt, "
        "updatedAt = :updatedAt, registrationSource = :registrationSource, "
        "contractUpdatedBy = :updatedBy"
    )
    remove_clause = ""
    values = {
        ":stateMachineArn": state_machine_arn,
        ":stateMachineType": "STANDARD",
        ":inputSchema": input_schema,
        ":schemaVersion": schema_version,
        ":schemaHash": schema_hash,
        ":schemaSource": "EXPLICIT",
        ":contractStatus": "ACTIVE",
        ":requiredParameters": required_parameters,
        ":enabled": True,
        ":registrationSource": "EXPLICIT_CONTRACT",
        ":updatedAt": now,
        ":updatedBy": _requester_id(event),
    }
    # Omitted -> leave any existing allowedCallers untouched. Empty list ->
    # clear the restriction. Non-empty list -> store the caller allowlist.
    if allowed_callers is not None:
        if allowed_callers:
            set_clause += ", allowedCallers = :allowedCallers"
            values[":allowedCallers"] = allowed_callers
        else:
            remove_clause = " REMOVE allowedCallers"

    response = _registry_table.update_item(
        Key={"workflowType": workflow_type},
        UpdateExpression=set_clause + remove_clause,
        ConditionExpression=(
            "(attribute_not_exists(workflowType) "
            "OR stateMachineArn = :stateMachineArn) "
            "AND (attribute_not_exists(schemaVersion) "
            "OR schemaVersion <> :schemaVersion OR schemaHash = :schemaHash)"
        ),
        ExpressionAttributeNames={"#enabled": "enabled"},
        ExpressionAttributeValues=values,
        ReturnValues="ALL_NEW",
    )
    logger.info(
        "Activated contract version %s for workflow %s",
        schema_version,
        workflow_type,
    )
    return _format_registration(response["Attributes"])


def lambda_handler(event, _context):
    field_name = event.get("info", {}).get("fieldName")
    if field_name == "registerWorkflowContract":
        return _register_workflow_contract(event)
    if field_name == "getWorkflowRegistration":
        return _get_workflow_registration(event.get("arguments", {}))
    if field_name == "listWorkflowRegistrations":
        return _list_workflow_registrations(event.get("arguments", {}))

    detail = event.get("detail", {})
    if detail.get("errorCode"):
        logger.info(
            "Ignoring failed Step Functions API call %s: %s",
            detail.get("eventName"),
            detail["errorCode"],
        )
        return {"ignored": True}

    event_name = detail.get("eventName")
    state_machine_arn = _find_state_machine_arn(detail)
    if not event_name or not state_machine_arn:
        raise ValueError(
            "Step Functions API event is missing eventName or stateMachineArn"
        )

    if event_name == "DeleteStateMachine":
        _remove_registration(state_machine_arn)
        return {"removed": state_machine_arn}

    try:
        workflow_type = _upsert_discovered_workflow(state_machine_arn)
    except ClientError as error:
        error_code = error.response.get("Error", {}).get("Code")
        if error_code == "StateMachineDoesNotExist":
            _remove_registration(state_machine_arn)
            return {"removed": state_machine_arn}
        if error_code == "ConditionalCheckFailedException":
            logger.error(
                "Workflow type collision while registering %s", state_machine_arn
            )
        raise
    return {
        "registered": state_machine_arn if workflow_type else None,
        "workflowType": workflow_type,
    }
