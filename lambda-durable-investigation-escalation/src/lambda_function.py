"""
Durable execution handler for the Investigation Failure Escalation workflow.

This Lambda function orchestrates an escalation workflow using the
aws_durable_execution_sdk_python SDK. When a DevOps Agent's investigation
fails or times out, this function:

1. Validates the incoming event
2. Gathers failure context and generates an incident ID
3. Creates an incident ticket (Integration Point)
4. Pages on-call personnel and waits for acknowledgment
5. Tracks final resolution (acknowledged or unacknowledged)

Each major step is checkpointed via context.step() so the workflow
survives Lambda restarts and retries automatically.
"""

import json
import os
import uuid
import time
from datetime import datetime, timezone

from aws_durable_execution_sdk_python import DurableContext, durable_execution
from aws_durable_execution_sdk_python.config import CallbackConfig, Duration
from aws_durable_execution_sdk_python.exceptions import CallbackError
import boto3

import helpers

# Valid failure types for the Investigation_Event
VALID_FAILURE_TYPES = {'investigation_failed', 'investigation_timed_out'}

# Required fields in the Investigation_Event payload
REQUIRED_FIELDS = [
    'investigationId',
    'failureType',
    'service',
    'region',
    'errorDetails',
    'timestamp',
]


def validate_event(event):
    """
    Validate the Investigation_Event payload.

    Checks that all required fields are present and that failureType
    is one of the allowed enum values.
    """
    missing = [f for f in REQUIRED_FIELDS if f not in event or event[f] is None]
    if missing:
        return False, f"Missing required fields: {', '.join(missing)}"

    if event.get('failureType') not in VALID_FAILURE_TYPES:
        return False, (
            f"Invalid failureType: '{event.get('failureType')}'. "
            f"Must be one of: {', '.join(sorted(VALID_FAILURE_TYPES))}"
        )

    return True, None


def build_context_summary(event):
    """
    Build a context summary from a validated Investigation_Event.

    Extracts all required fields and generates a new incidentId (UUID v4).
    """
    return {
        'incidentId': str(uuid.uuid4()),
        'investigationId': event['investigationId'],
        'failureType': event['failureType'],
        'service': event['service'],
        'region': event['region'],
        'errorDetails': event['errorDetails'],
        'timestamp': event['timestamp'],
    }


def build_incident_record(context_summary):
    """
    Build a full incident record from a context summary.

    Adds default fields: status=open, empty escalationHistory,
    createdAt timestamp, and TTL set to 7 days from creation.
    """
    now = datetime.now(timezone.utc)
    created_at = now.isoformat()
    ttl = int(now.timestamp()) + 604800  # 7 days in seconds

    return {
        **context_summary,
        'status': 'open',
        'escalationHistory': [],
        'createdAt': created_at,
        'ttl': ttl,
    }


def build_notification_message(incident_data, ack_url):
    """
    Build a notification message for escalation alerts.
    """
    return (
        f"INVESTIGATION ESCALATION ALERT\n"
        f"\n"
        f"Incident ID: {incident_data['incidentId']}\n"
        f"Investigation ID: {incident_data['investigationId']}\n"
        f"Failure Type: {incident_data['failureType']}\n"
        f"Service: {incident_data['service']}\n"
        f"Region: {incident_data['region']}\n"
        f"Error Details: {incident_data['errorDetails']}\n"
        f"\n"
        f"Acknowledge this incident:\n"
        f"{ack_url}\n"
    )


def build_final_result(incident_id, investigation_id, status, escalation_history):
    """
    Build the final result object returned by the Escalation_Function.
    """
    return {
        'incidentId': incident_id,
        'investigationId': investigation_id,
        'status': status,
        'escalationHistory': escalation_history,
    }


@durable_execution
def lambda_handler(event, context: DurableContext):
    """
    Durable execution handler for the investigation failure escalation workflow.

    Gathers context, creates an incident, pages on-call personnel,
    waits for acknowledgment, and tracks the final resolution.
    """
    # --- Input Validation ---
    is_valid, error_message = validate_event(event)
    if not is_valid:
        now = datetime.now(timezone.utc)
        validation_record = {
            'incidentId': str(uuid.uuid4()),
            'investigationId': event.get('investigationId', 'unknown'),
            'failureType': event.get('failureType', 'unknown'),
            'service': event.get('service', 'unknown'),
            'region': event.get('region', 'unknown'),
            'errorDetails': error_message,
            'timestamp': event.get('timestamp', now.isoformat()),
            'status': 'validation_failed',
            'escalationHistory': [],
            'createdAt': now.isoformat(),
            'ttl': int(now.timestamp()) + 604800,
        }
        helpers.create_incident_ticket(validation_record)
        print(f"Validation failed: {error_message}")
        return {'error': error_message, 'status': 'validation_failed'}

    # --- Step 1: Gather Context ---
    def gather_context(_):
        summary = build_context_summary(event)
        print(f"Context gathered — incidentId: {summary['incidentId']}")
        return summary

    context_summary = context.step(gather_context, name='gather-context')

    incident_id = context_summary['incidentId']
    investigation_id = context_summary['investigationId']

    # --- Step 2: Create Incident ---
    def create_incident(_):
        record = build_incident_record(context_summary)
        helpers.create_incident_ticket(record)
        print(f"Incident created: {incident_id}")
        return record

    incident_record = context.step(create_incident, name='create-incident')
    escalation_history = incident_record.get('escalationHistory', [])

    # --- Read API Gateway URL from SSM ---
    param_name = os.environ.get('API_GATEWAY_PARAM')
    if not param_name:
        raise ValueError("API_GATEWAY_PARAM environment variable is not set")

    ssm = boto3.client('ssm')
    response = ssm.get_parameter(Name=param_name)
    api_base_url = response['Parameter']['Value']
    print(f"API Base URL: {api_base_url}")

    # --- Read configurable timeout ---
    ack_timeout = int(os.environ.get('ACK_TIMEOUT', '900'))

    # Callback table entry TTL (1 hour)
    callback_ttl = int(time.time()) + 3600

    topic_arn = os.environ['NOTIFICATION_TOPIC_ARN']

    # --- Create Callback, Store Mapping, Notify On-Call ---
    callback = context.create_callback(
        name='wait-for-ack',
        config=CallbackConfig(timeout=Duration.from_seconds(ack_timeout)),
    )

    callback_uuid = str(uuid.uuid4())
    helpers.store_callback_mapping(
        uuid=callback_uuid,
        callback_id=callback.callback_id,
        incident_id=incident_id,
        tier=1,
        ttl=callback_ttl,
    )

    def notify_oncall(_):
        ack_url = f"{api_base_url}/{callback_uuid}"
        message = build_notification_message(context_summary, ack_url)
        helpers.send_escalation_notification(topic_arn, message)
        print(f"On-call notification sent — ack URL: {ack_url}")

    context.step(notify_oncall, name='notify-oncall')

    # --- Pause: Wait for Acknowledgment ---
    try:
        result = callback.result()

        # Acknowledged
        if isinstance(result, str):
            ack_data = json.loads(result)
        else:
            ack_data = result

        ack_timestamp = ack_data.get('timestamp', datetime.now(timezone.utc).isoformat())

        def resolve_acknowledged(_):
            helpers.resolve_incident(incident_id, 'acknowledged', {
                'acknowledgedAt': ack_timestamp,
            })
            escalation_history.append({
                'action': 'acknowledged',
                'timestamp': ack_timestamp,
            })
            print(f"Incident {incident_id} acknowledged")

        context.step(resolve_acknowledged, name='resolve-incident')

        return build_final_result(
            incident_id, investigation_id, 'acknowledged', escalation_history
        )

    except CallbackError:
        print(f"Callback timed out — resolving as unacknowledged")

    # --- Timeout → Resolve Unacknowledged ---
    def resolve_unacknowledged(_):
        timeout_timestamp = datetime.now(timezone.utc).isoformat()
        helpers.resolve_incident(incident_id, 'unacknowledged', {})
        escalation_history.append({
            'action': 'timeout',
            'timestamp': timeout_timestamp,
        })
        print(f"Incident {incident_id} unacknowledged — timeout expired")

    context.step(resolve_unacknowledged, name='resolve-unacknowledged')

    return build_final_result(
        incident_id, investigation_id, 'unacknowledged', escalation_history
    )
