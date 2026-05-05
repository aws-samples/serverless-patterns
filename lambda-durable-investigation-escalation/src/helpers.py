"""
Integration helper functions for the Investigation Escalation workflow.

These functions serve as extensible integration points. Each function isolates
a specific external interaction (DynamoDB write, SNS publish) so that customers
can replace the default implementation with calls to third-party services
(e.g., Jira, ServiceNow, PagerDuty) without modifying the core orchestration logic.
"""

import os
import boto3

# Module-level clients initialized from environment variables
dynamodb = boto3.resource('dynamodb')
sns = boto3.client('sns')

incident_table = dynamodb.Table(os.environ.get('INCIDENT_TABLE_NAME', ''))
callback_table = dynamodb.Table(os.environ.get('CALLBACK_TABLE_NAME', ''))


def create_incident_ticket(incident):
    """
    Create an incident record in the Incident_Table.

    This is an Integration Point — replace this function to create tickets
    in an external system such as Jira or ServiceNow instead of DynamoDB.

    Args:
        incident (dict): The full incident record containing incidentId,
            investigationId, failureType, service, region, errorDetails,
            timestamp, status, escalationHistory, createdAt, and ttl.
    """
    incident_table.put_item(Item=incident)


def resolve_incident(incident_id, status, details):
    """
    Update the incident record with its final resolution status.

    This is an Integration Point — replace this function to transition tickets
    in an external system such as Jira or ServiceNow instead of DynamoDB.

    Args:
        incident_id (str): The incident's partition key.
        status (str): The resolution status ('acknowledged' or 'unacknowledged').
        details (dict): Additional resolution details. For acknowledged incidents,
            should contain 'acknowledgedAt' (ISO 8601 timestamp) and
            'acknowledgedTier' (int). For unacknowledged incidents, may be empty
            or contain supplementary info.
    """
    update_expr = 'SET #s = :status'
    expr_names = {'#s': 'status'}
    expr_values = {':status': status}

    if details.get('acknowledgedAt'):
        update_expr += ', acknowledgedAt = :ack_at'
        expr_values[':ack_at'] = details['acknowledgedAt']

    if details.get('acknowledgedTier'):
        update_expr += ', acknowledgedTier = :ack_tier'
        expr_values[':ack_tier'] = details['acknowledgedTier']

    incident_table.update_item(
        Key={'incidentId': incident_id},
        UpdateExpression=update_expr,
        ExpressionAttributeNames=expr_names,
        ExpressionAttributeValues=expr_values,
    )


def send_escalation_notification(topic_arn, message):
    """
    Publish an escalation notification to the Notification_Topic.

    This is an Integration Point — replace this function to send notifications
    via an external service such as PagerDuty or Opsgenie instead of SNS.

    Args:
        topic_arn (str): The ARN of the SNS topic to publish to.
        message (str): The formatted notification message body.
    """
    sns.publish(
        TopicArn=topic_arn,
        Subject='Investigation Escalation Alert',
        Message=message,
    )


def store_callback_mapping(uuid, callback_id, incident_id, tier, ttl):
    """
    Store a UUID-to-callback-ID mapping in the Callback_Table.

    This mapping enables clean acknowledgment URLs. When an on-call responder
    clicks the link, the Callback_Handler uses this mapping to look up the
    durable function callback ID.

    Args:
        uuid (str): The short UUID used in the acknowledgment URL.
        callback_id (str): The durable function callback ID.
        incident_id (str): The associated incident ID.
        tier (int): The escalation tier (1 or 2).
        ttl (int): TTL in epoch seconds for automatic cleanup.
    """
    callback_table.put_item(
        Item={
            'uuid': uuid,
            'callbackId': callback_id,
            'incidentId': incident_id,
            'tier': tier,
            'ttl': ttl,
        }
    )
