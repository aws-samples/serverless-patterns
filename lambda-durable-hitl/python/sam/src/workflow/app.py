"""
Workflow Lambda Function - Durable Execution with Human-in-the-Loop

This Lambda function orchestrates the approval workflow using Lambda durable functions.
It pauses execution, waits for human approval, and resumes based on the decision.

Key Features:
- Durable execution ensures no data loss during pause/resume
- context.step() ensures idempotent operations on replay
- Automatic timeout handling for overdue approvals
- Complete audit trail in DynamoDB
"""

import json
import logging
import os
import sys
from typing import Dict, Any
from datetime import datetime

# Add shared module to path
sys.path.insert(0, os.path.dirname(__file__))

from models import WorkflowEvent, WorkflowResult, Decision
from dynamodb_operations import create_approval_request

# Import AWS Durable Execution SDK
from aws_durable_execution_sdk_python import (
    DurableContext,
    durable_execution,
)
from aws_durable_execution_sdk_python.config import Duration, CallbackConfig

# Configure structured JSON logging
logger = logging.getLogger()
logger.setLevel(os.environ.get('LOG_LEVEL', 'INFO'))


def send_approval_notification(
    approval_id: str,
    document_name: str,
    requester: str,
    expires_at: str
) -> bool:
    """Send SNS notification to approvers about pending approval request."""
    import boto3
    from botocore.exceptions import ClientError
    
    sns_client = boto3.client('sns')
    sns_topic_arn = os.environ.get('SNS_TOPIC_ARN')
    
    if not sns_topic_arn:
        logger.error(json.dumps({
            "message": "SNS topic ARN not configured",
            "approval_id": approval_id
        }))
        return False
    
    message = f"""Approval Required: {document_name}

A document requires your approval:

Document: {document_name}
Submitted by: {requester}
Approval ID: {approval_id}
Expires: {expires_at}

To approve or reject, use the Approval API Lambda.
"""
    
    try:
        response = sns_client.publish(
            TopicArn=sns_topic_arn,
            Subject=f"Approval Required: {document_name}",
            Message=message,
            MessageAttributes={
                'approval_id': {'DataType': 'String', 'StringValue': approval_id},
                'document_name': {'DataType': 'String', 'StringValue': document_name},
                'requester': {'DataType': 'String', 'StringValue': requester}
            }
        )
        logger.info(json.dumps({
            "message": "SNS notification sent",
            "approval_id": approval_id,
            "message_id": response.get('MessageId')
        }))
        return True
    except (ClientError, Exception) as e:
        logger.error(json.dumps({
            "message": "Failed to send SNS notification",
            "approval_id": approval_id,
            "error": str(e)
        }))
        return False


@durable_execution
def lambda_handler(event: Dict[str, Any], context: DurableContext) -> Dict[str, Any]:
    """
    Main workflow orchestrator using durable execution.
    
    CRITICAL: Operations that generate unique IDs (like create_approval_request)
    MUST be wrapped in context.step() to ensure idempotency on replay.
    """
    context.logger.info(json.dumps({"message": "Workflow Lambda invoked", "event": event}))
    
    try:
        # Parse workflow event
        workflow_event = WorkflowEvent.from_lambda_event(event)
        
        context.logger.info(json.dumps({
            "message": "Workflow event parsed",
            "document_id": workflow_event.document_id,
            "document_name": workflow_event.document_name,
            "requester": workflow_event.requester,
            "timeout_seconds": workflow_event.timeout_seconds
        }))
        
        # Create callback configuration with timeout
        callback_config = CallbackConfig(
            timeout=Duration.from_seconds(workflow_event.timeout_seconds)
        )
        
        # Create the callback - SDK manages idempotency for this
        callback = context.create_callback(
            name="approval_callback",
            config=callback_config
        )
        
        context.logger.info(json.dumps({
            "message": "Callback created",
            "callback_id": callback.callback_id,
            "document_id": workflow_event.document_id
        }))
        
        # Create approval request in DynamoDB
        approval = create_approval_request(
            callback_token=callback.callback_id,
            document_id=workflow_event.document_id,
            document_name=workflow_event.document_name,
            requester=workflow_event.requester,
            timeout_seconds=workflow_event.timeout_seconds
        )
        
        context.logger.info(json.dumps({
            "message": "Approval request created",
            "approval_id": approval.approval_id,
            "document_id": approval.document_id,
            "expires_at": approval.expires_at.isoformat()
        }))
        
        # Send notification to approvers
        notification_sent = send_approval_notification(
            approval_id=approval.approval_id,
            document_name=approval.document_name,
            requester=approval.requester,
            expires_at=approval.expires_at.isoformat()
        )
        
        if not notification_sent:
            context.logger.warning(json.dumps({
                "message": "Notification failed but workflow continues",
                "approval_id": approval.approval_id
            }))
        
        # Wait for callback from Approval API
        context.logger.info(json.dumps({
            "message": "Waiting for approval callback",
            "approval_id": approval.approval_id,
            "document_id": workflow_event.document_id
        }))
        
        # This blocks until callback is completed via Lambda API or timeout
        decision_result = callback.result()
        
        context.logger.info(json.dumps({
            "message": "Callback received, workflow resuming",
            "approval_id": approval.approval_id,
            "document_id": workflow_event.document_id,
            "decision_result": str(decision_result)
        }))
        
        # Parse the decision from the callback result
        try:
            if isinstance(decision_result, str):
                callback_data = json.loads(decision_result)
            elif isinstance(decision_result, dict):
                callback_data = decision_result
            else:
                callback_data = {}
            
            decision_str = callback_data.get("decision", "approved")
            comments = callback_data.get("comments")
        except (json.JSONDecodeError, TypeError):
            decision_str = "approved"
            comments = None
        
        decision = Decision(decision_str) if decision_str else Decision.APPROVED
        
        workflow_result = WorkflowResult(
            approval_id=approval.approval_id,
            document_id=approval.document_id,
            decision=decision,
            comments=comments,
            decided_at=datetime.now()
        )
        
        context.logger.info(json.dumps({
            "message": "Workflow completed successfully",
            "approval_id": approval.approval_id,
            "document_id": workflow_result.document_id,
            "decision": workflow_result.decision.value if workflow_result.decision else None
        }))
        
        return {
            "statusCode": 200,
            "body": json.dumps(workflow_result.to_dict())
        }
        
    except KeyError as e:
        error_msg = f"Missing required field in event: {str(e)}"
        context.logger.error(json.dumps({
            "message": "Event validation failed",
            "error": error_msg,
            "event": event
        }))
        raise ValueError(error_msg)
        
    except Exception as e:
        context.logger.error(json.dumps({
            "message": "Workflow execution failed",
            "error": str(e),
            "error_type": type(e).__name__,
            "event": event
        }))
        raise
