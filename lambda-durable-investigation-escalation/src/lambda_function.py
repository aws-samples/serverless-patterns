"""
Durable execution handler for the Investigation Failure Escalation workflow.

This Lambda function is triggered by an Amazon EventBridge rule that captures
AWS DevOps Agent investigation failure and timeout events (source: aws.aidevops).

Workflow:
1. Parses the EventBridge event from AWS DevOps Agent
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

# Module-level clients — reuse connections across invocations
ssm = boto3.client('ssm')

# Mapping from DevOps Agent event detail-type to internal failure types
DETAIL_TYPE_TO_FAILURE_TYPE = {
    'Investigation Failed': 'investigation_failed',
    'Investigation Timed Out': 'investigation_timed_out',
}


def parse_devops_agent_event(event):
    """
    Parse an EventBridge event from AWS DevOps Agent.

    Expected event structure (source: aws.aidevops):
    {
      "source": "aws.aidevops",
      "detail-type": "Investigation Failed" | "Investigation Timed Out",
      "account": "123456789012",
      "region": "us-east-1",
      "time": "2026-03-12T18:10:00Z",
      "resources": ["arn:aws:aidevops:..."],
      "detail": {
        "version": "1.0.0",
        "metadata": {
          "agent_space_id": "...",
          "task_id": "...",
          "execution_id": "..."
        },
        "data": {
          "task_type": "INVESTIGATION",
          "priority": "CRITICAL",
          "status": "FAILED" | "TIMED_OUT",
          "created_at": "...",
          "updated_at": "..."
        }
      }
    }

    Returns a normalized context dict, or (None, error_message) if invalid.
    """
    # Validate this is a DevOps Agent event
    source = event.get('source')
    detail_type = event.get('detail-type')
    detail = event.get('detail', {})
    metadata = detail.get('metadata', {})
    data = detail.get('data', {})

    if source != 'aws.aidevops':
        return None, f"Unexpected event source: '{source}'. Expected 'aws.aidevops'."

    failure_type = DETAIL_TYPE_TO_FAILURE_TYPE.get(detail_type)
    if not failure_type:
        return None, (
            f"Unsupported detail-type: '{detail_type}'. "
            f"Expected one of: {list(DETAIL_TYPE_TO_FAILURE_TYPE.keys())}"
        )

    task_id = metadata.get('task_id')
    if not task_id:
        return None, "Missing metadata.task_id in event detail."

    context_summary = {
        'incidentId': str(uuid.uuid4()),
        'investigationId': task_id,
        'executionId': metadata.get('execution_id', 'unknown'),
        'agentSpaceId': metadata.get('agent_space_id', 'unknown'),
        'failureType': failure_type,
        'priority': data.get('priority', 'UNKNOWN'),
        'service': 'devops-agent',
        'region': event.get('region', 'unknown'),
        'errorDetails': f"DevOps Agent investigation {data.get('status', 'UNKNOWN').lower()} "
                        f"(task: {task_id}, priority: {data.get('priority', 'UNKNOWN')})",
        'timestamp': data.get('updated_at', event.get('time', datetime.now(timezone.utc).isoformat())),
    }

    return context_summary, None


def build_incident_record(context_summary):
    """
    Build a full incident record from a context summary.

    Adds default fields: status=open, createdAt timestamp,
    and TTL set to 7 days from creation.
    """
    now = datetime.now(timezone.utc)
    created_at = now.isoformat()
    ttl = int(now.timestamp()) + 604800  # 7 days

    return {
        **context_summary,
        'status': 'open',
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
        f"Investigation (Task ID): {incident_data['investigationId']}\n"
        f"Execution ID: {incident_data.get('executionId', 'N/A')}\n"
        f"Agent Space: {incident_data.get('agentSpaceId', 'N/A')}\n"
        f"Failure Type: {incident_data['failureType']}\n"
        f"Priority: {incident_data.get('priority', 'UNKNOWN')}\n"
        f"Region: {incident_data['region']}\n"
        f"Error Details: {incident_data['errorDetails']}\n"
        f"Timestamp: {incident_data['timestamp']}\n"
        f"\n"
        f"Acknowledge this incident:\n"
        f"{ack_url}\n"
    )


def build_final_result(incident_id, investigation_id, status):
    """
    Build the final result object returned by the Escalation Function.
    """
    return {
        'incidentId': incident_id,
        'investigationId': investigation_id,
        'status': status,
    }


@durable_execution
def lambda_handler(event, context: DurableContext):
    """
    Durable execution handler for the investigation failure escalation workflow.

    Triggered by EventBridge when AWS DevOps Agent emits an investigation
    failure or timeout event.
    """
    # --- Parse EventBridge Event from DevOps Agent ---
    context_summary, error_message = parse_devops_agent_event(event)

    if error_message:
        now = datetime.now(timezone.utc)
        validation_record = {
            'incidentId': str(uuid.uuid4()),
            'investigationId': event.get('detail', {}).get('metadata', {}).get('task_id', 'unknown'),
            'failureType': 'parse_error',
            'service': 'devops-agent',
            'region': event.get('region', 'unknown'),
            'errorDetails': error_message,
            'timestamp': event.get('time', now.isoformat()),
            'status': 'validation_failed',
            'createdAt': now.isoformat(),
            'ttl': int(now.timestamp()) + 604800,
        }
        helpers.create_incident_ticket(validation_record)
        print(f"Event parsing failed: {error_message}")
        return {'error': error_message, 'status': 'validation_failed'}

    # --- Step 1: Gather Context ---
    def gather_context(_):
        print(f"Context gathered — incidentId: {context_summary['incidentId']}")
        return context_summary

    gathered = context.step(gather_context, name='gather-context')

    incident_id = gathered['incidentId']
    investigation_id = gathered['investigationId']

    # --- Step 2: Create Incident ---
    def create_incident(_):
        record = build_incident_record(gathered)
        helpers.create_incident_ticket(record)
        print(f"Incident created: {incident_id}")
        return record

    incident_record = context.step(create_incident, name='create-incident')

    # --- Read API Gateway URL from SSM ---
    param_name = os.environ.get('API_GATEWAY_PARAM')
    if not param_name:
        raise ValueError("API_GATEWAY_PARAM environment variable is not set")

    try:
        response = ssm.get_parameter(Name=param_name)
        api_base_url = response['Parameter']['Value']
    except Exception as e:
        print(f"Failed to retrieve API Gateway URL from SSM parameter '{param_name}': {str(e)}")
        raise

    print(f"API Base URL: {api_base_url}")

    # --- Read configurable timeout ---
    ack_timeout = int(os.environ.get('ACK_TIMEOUT', '900'))

    # Callback table entry TTL (1 hour)
    callback_ttl = int(time.time()) + 3600

    topic_arn = os.environ['NOTIFICATION_TOPIC_ARN']

    # --- Step 3: Create Callback, Store Mapping, Notify On-Call ---
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
        message = build_notification_message(gathered, ack_url)
        helpers.send_escalation_notification(topic_arn, message)
        print(f"On-call notification sent — ack URL: {ack_url}")

    context.step(notify_oncall, name='notify-oncall')

    # --- Pause: Wait for Acknowledgment ---
    try:
        result = callback.result()

        # Acknowledged
        if isinstance(result, str):
            try:
                ack_data = json.loads(result)
            except (json.JSONDecodeError, TypeError) as e:
                print(f"Failed to parse callback result as JSON: {str(e)}. Raw result: {result}")
                ack_data = {'timestamp': datetime.now(timezone.utc).isoformat()}
        else:
            ack_data = result

        ack_timestamp = ack_data.get('timestamp', datetime.now(timezone.utc).isoformat())

        def resolve_acknowledged(_):
            helpers.resolve_incident(incident_id, 'acknowledged', {
                'acknowledgedAt': ack_timestamp,
            })
            print(f"Incident {incident_id} acknowledged")

        context.step(resolve_acknowledged, name='resolve-incident')

        return build_final_result(
            incident_id, investigation_id, 'acknowledged'
        )

    except CallbackError:
        print(f"Callback timed out — resolving as unacknowledged")

    # --- Timeout → Resolve Unacknowledged ---
    def resolve_unacknowledged(_):
        helpers.resolve_incident(incident_id, 'unacknowledged', {})
        print(f"Incident {incident_id} unacknowledged — timeout expired")

    context.step(resolve_unacknowledged, name='resolve-unacknowledged')

    return build_final_result(
        incident_id, investigation_id, 'unacknowledged'
    )
