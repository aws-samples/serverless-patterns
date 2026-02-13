"""
Workflow Lambda Function - Durable Execution with Human-in-the-Loop

This Lambda function orchestrates the approval workflow using AWS Lambda Durable Functions.
It pauses execution, waits for human approval, and resumes based on the decision.

Primary Use Case: Document Approval Workflow
--------------------------------------------
When a document is submitted for review (e.g., contract, policy, technical design),
this function pauses execution, sends a notification to an approver, and resumes
with the approval decision. The workflow maintains state across the pause/resume cycle.

Additional Use Cases:
--------------------
1. Expense Approval System: Employee submits expense report, manager reviews and
   approves/rejects, workflow resumes to process the expense accordingly.

2. Content Moderation Workflow: User-generated content is flagged for human review,
   moderator reviews and approves/rejects, workflow resumes to publish or remove content.

3. Budget Proposal Review: Department submits budget proposal, finance team reviews
   and approves/rejects, workflow resumes to allocate or deny budget.

Key Features:
- Durable execution ensures no data loss during pause/resume
- Automatic timeout handling for overdue approvals
- Complete audit trail in DynamoDB
- Flexible decision recording with comments
"""

import json
import logging
import os
import sys
from typing import Dict, Any, Optional

# Add shared module to path
sys.path.insert(0, os.path.dirname(__file__))

from models import WorkflowEvent, WorkflowResult, Decision
from dynamodb_operations import create_approval_request, update_approval_status

# Import AWS Durable Execution SDK
from aws_durable_execution_sdk_python import (
    DurableContext,
    durable_execution,
    durable_step,
)
from aws_durable_execution_sdk_python.config import Duration

# Configure structured JSON logging
logger = logging.getLogger()
logger.setLevel(os.environ.get('LOG_LEVEL', 'INFO'))


@durable_step
def create_approval_record(step_context, callback_token: str, document_id: str, 
                          document_name: str, requester: str, timeout_seconds: int):
    """
    Durable step that creates the approval request in DynamoDB.
    This step is checkpointed, so if interrupted, it won't re-execute.
    """
    step_context.logger.info(
        json.dumps({
            "message": "Creating approval request",
            "document_id": document_id
        })
    )
    
    approval_request = create_approval_request(
        callback_token=callback_token,
        document_id=document_id,
        document_name=document_name,
        requester=requester,
        timeout_seconds=timeout_seconds
    )
    
    step_context.logger.info(
        json.dumps({
            "message": "Approval request created",
            "approval_id": approval_request.approval_id,
            "document_id": approval_request.document_id,
            "expires_at": approval_request.expires_at.isoformat()
        })
    )
    
    return approval_request


@durable_step
def send_notification(step_context, approval_id: str, document_name: str, 
                     requester: str, expires_at: str) -> bool:
    """
    Durable step that sends SNS notification to approvers.
    This step is checkpointed and can be retried if it fails.
    """
    import boto3
    from botocore.exceptions import ClientError
    
    sns_client = boto3.client('sns')
    sns_topic_arn = os.environ.get('SNS_TOPIC_ARN')
    
    if not sns_topic_arn:
        step_context.logger.error(
            json.dumps({
                "message": "SNS topic ARN not configured",
                "approval_id": approval_id
            })
        )
        return False
    
    # Format notification message
    message = f"""Approval Required: {document_name}

A document requires your approval:

Document: {document_name}
Submitted by: {requester}
Approval ID: {approval_id}
Expires: {expires_at}

To approve or reject, use the CLI tool:
python approval_cli.py list
python approval_cli.py approve {approval_id}
python approval_cli.py reject {approval_id}
"""
    
    subject = f"Approval Required: {document_name}"
    
    try:
        response = sns_client.publish(
            TopicArn=sns_topic_arn,
            Subject=subject,
            Message=message,
            MessageAttributes={
                'approval_id': {
                    'DataType': 'String',
                    'StringValue': approval_id
                },
                'document_name': {
                    'DataType': 'String',
                    'StringValue': document_name
                },
                'requester': {
                    'DataType': 'String',
                    'StringValue': requester
                }
            }
        )
        
        step_context.logger.info(
            json.dumps({
                "message": "SNS notification sent",
                "approval_id": approval_id,
                "message_id": response.get('MessageId')
            })
        )
        
        return True
        
    except ClientError as e:
        step_context.logger.error(
            json.dumps({
                "message": "Failed to send SNS notification",
                "approval_id": approval_id,
                "error": str(e),
                "error_code": e.response['Error']['Code']
            })
        )
        return False
        
    except Exception as e:
        step_context.logger.error(
            json.dumps({
                "message": "Unexpected error sending SNS notification",
                "approval_id": approval_id,
                "error": str(e),
                "error_type": type(e).__name__
            })
        )
        return False


@durable_step
def check_approval_status(step_context, approval_id: str) -> Dict[str, Any]:
    """
    Durable step that checks the approval status in DynamoDB.
    This step is checkpointed and can be retried if it fails.
    """
    import boto3
    from botocore.exceptions import ClientError
    
    dynamodb = boto3.resource('dynamodb')
    table_name = os.environ.get('APPROVALS_TABLE_NAME')
    table = dynamodb.Table(table_name)
    
    try:
        response = table.get_item(Key={'approval_id': approval_id})
        
        if 'Item' not in response:
            step_context.logger.error(
                json.dumps({
                    "message": "Approval request not found",
                    "approval_id": approval_id
                })
            )
            return {"decision": "timeout", "comments": None}
        
        item = response['Item']
        decision = item.get('decision', 'pending')
        comments = item.get('comments')
        
        step_context.logger.info(
            json.dumps({
                "message": "Approval status checked",
                "approval_id": approval_id,
                "decision": decision
            })
        )
        
        return {
            "decision": decision,
            "comments": comments
        }
        
    except ClientError as e:
        step_context.logger.error(
            json.dumps({
                "message": "Failed to check approval status",
                "approval_id": approval_id,
                "error": str(e)
            })
        )
        return {"decision": "timeout", "comments": None}


def send_approval_notification(
    approval_id: str,
    document_name: str,
    requester: str,
    expires_at: str
) -> bool:
    """
    Send SNS notification to approvers about pending approval request.
    
    This function publishes a notification to the SNS topic with approval details.
    Notification failures are logged but do not block workflow execution.
    
    Args:
        approval_id: Unique identifier for the approval request
        document_name: Name of the document requiring approval
        requester: User who submitted the document
        expires_at: ISO format timestamp when approval expires
    
    Returns:
        bool: True if notification sent successfully, False otherwise
    """
    import boto3
    from botocore.exceptions import ClientError
    
    sns_client = boto3.client('sns')
    sns_topic_arn = os.environ.get('SNS_TOPIC_ARN')
    
    if not sns_topic_arn:
        logger.error(
            json.dumps({
                "message": "SNS topic ARN not configured",
                "approval_id": approval_id
            })
        )
        return False
    
    # Format notification message
    message = f"""Approval Required: {document_name}

A document requires your approval:

Document: {document_name}
Submitted by: {requester}
Approval ID: {approval_id}
Expires: {expires_at}

To approve or reject, use the CLI tool:
python approval_cli.py list
python approval_cli.py approve {approval_id}
python approval_cli.py reject {approval_id}
"""
    
    subject = f"Approval Required: {document_name}"
    
    try:
        # Publish notification to SNS
        response = sns_client.publish(
            TopicArn=sns_topic_arn,
            Subject=subject,
            Message=message,
            MessageAttributes={
                'approval_id': {
                    'DataType': 'String',
                    'StringValue': approval_id
                },
                'document_name': {
                    'DataType': 'String',
                    'StringValue': document_name
                },
                'requester': {
                    'DataType': 'String',
                    'StringValue': requester
                }
            }
        )
        
        logger.info(
            json.dumps({
                "message": "SNS notification sent",
                "approval_id": approval_id,
                "message_id": response.get('MessageId')
            })
        )
        
        return True
        
    except ClientError as e:
        # Log error but don't block workflow execution
        logger.error(
            json.dumps({
                "message": "Failed to send SNS notification",
                "approval_id": approval_id,
                "error": str(e),
                "error_code": e.response['Error']['Code']
            })
        )
        return False
        
    except Exception as e:
        # Log unexpected errors but don't block workflow
        logger.error(
            json.dumps({
                "message": "Unexpected error sending SNS notification",
                "approval_id": approval_id,
                "error": str(e),
                "error_type": type(e).__name__
            })
        )
        return False


@durable_execution
def lambda_handler(event: Dict[str, Any], context: DurableContext) -> Dict[str, Any]:
    """
    Main workflow orchestrator using durable execution.
    
    This function coordinates the approval workflow by:
    1. Parsing the workflow event
    2. Creating an approval request (checkpointed)
    3. Sending a notification (checkpointed)
    4. Polling for approval decision with durable waits
    5. Returning the result
    
    The durable execution SDK ensures that:
    - Each step is checkpointed and won't re-execute on replay
    - Waits don't consume compute resources
    - The function can run for extended periods (up to 1 year)
    
    Args:
        event: Contains document_id, document_name, requester, timeout_seconds (optional)
        context: DurableContext with durable execution capabilities
    
    Returns:
        Dict containing workflow result with approval decision
        
    Raises:
        ValueError: If required event fields are missing
        Exception: For unexpected errors during workflow execution
    """
    # Log invocation with structured logging
    context.logger.info(
        json.dumps({
            "message": "Workflow Lambda invoked",
            "event": event
        })
    )
    
    try:
        # Parse workflow event from Lambda event
        workflow_event = WorkflowEvent.from_lambda_event(event)
        
        context.logger.info(
            json.dumps({
                "message": "Workflow event parsed",
                "document_id": workflow_event.document_id,
                "document_name": workflow_event.document_name,
                "requester": workflow_event.requester,
                "timeout_seconds": workflow_event.timeout_seconds
            })
        )
        
        # Generate callback token (placeholder - in real implementation this would be from SDK)
        import uuid
        callback_token = f"durable-token-{str(uuid.uuid4())}"
        
        context.logger.info(
            json.dumps({
                "message": "Callback token generated",
                "document_id": workflow_event.document_id
            })
        )
        
        # Step 1: Create approval request (checkpointed)
        approval_request = context.step(create_approval_record(
            callback_token,
            workflow_event.document_id,
            workflow_event.document_name,
            workflow_event.requester,
            workflow_event.timeout_seconds
        ))
        
        # Step 2: Send SNS notification (checkpointed)
        notification_sent = context.step(send_notification(
            approval_request.approval_id,
            approval_request.document_name,
            approval_request.requester,
            approval_request.expires_at.isoformat()
        ))
        
        if not notification_sent:
            context.logger.warning(
                json.dumps({
                    "message": "Notification failed but workflow continues",
                    "approval_id": approval_request.approval_id
                })
            )
        
        # Poll for approval decision using durable waits
        max_attempts = workflow_event.timeout_seconds // 5  # Check every 5 seconds
        poll_interval = 5
        
        context.logger.info(
            json.dumps({
                "message": "Starting approval polling",
                "approval_id": approval_request.approval_id,
                "max_attempts": max_attempts,
                "poll_interval": poll_interval
            })
        )
        
        decision_result = None
        for attempt in range(max_attempts):
            # Wait before checking status (no compute charges during wait)
            context.wait(Duration.from_seconds(poll_interval))
            
            # Check approval status (checkpointed)
            status_result = context.step(check_approval_status(approval_request.approval_id))
            
            decision_str = status_result.get("decision", "pending")
            
            if decision_str != "pending":
                # Decision received
                context.logger.info(
                    json.dumps({
                        "message": "Approval decision received",
                        "approval_id": approval_request.approval_id,
                        "decision": decision_str,
                        "attempt": attempt + 1
                    })
                )
                decision_result = status_result
                break
        
        # Handle timeout if no decision received
        if decision_result is None or decision_result.get("decision") == "pending":
            context.logger.warning(
                json.dumps({
                    "message": "Approval request timed out",
                    "approval_id": approval_request.approval_id
                })
            )
            
            # Update approval status to timeout in DynamoDB
            try:
                update_approval_status(
                    approval_id=approval_request.approval_id,
                    decision=Decision.TIMEOUT,
                    comments="Approval request timed out - no decision received within timeout period"
                )
                context.logger.info(
                    json.dumps({
                        "message": "Approval status updated to timeout",
                        "approval_id": approval_request.approval_id
                    })
                )
            except Exception as e:
                context.logger.error(
                    json.dumps({
                        "message": "Failed to update approval status to timeout",
                        "approval_id": approval_request.approval_id,
                        "error": str(e),
                        "error_type": type(e).__name__
                    })
                )
            
            decision_result = {
                "decision": "timeout",
                "comments": "Approval request timed out - no decision received within timeout period"
            }
        
        # Parse decision
        decision_str = decision_result.get("decision", "timeout")
        decision = Decision(decision_str)
        comments = decision_result.get("comments")
        
        # Create workflow result
        from datetime import datetime
        workflow_result = WorkflowResult(
            approval_id=approval_request.approval_id,
            document_id=approval_request.document_id,
            decision=decision,
            comments=comments,
            decided_at=datetime.now()
        )
        
        context.logger.info(
            json.dumps({
                "message": "Workflow completed successfully",
                "approval_id": approval_request.approval_id,
                "document_id": workflow_result.document_id,
                "decision": workflow_result.decision.value
            })
        )
        
        # Return workflow result
        return {
            "statusCode": 200,
            "body": json.dumps(workflow_result.to_dict())
        }
        
    except KeyError as e:
        error_msg = f"Missing required field in event: {str(e)}"
        context.logger.error(
            json.dumps({
                "message": "Event validation failed",
                "error": error_msg,
                "event": event
            })
        )
        raise ValueError(error_msg)
        
    except Exception as e:
        context.logger.error(
            json.dumps({
                "message": "Workflow execution failed",
                "error": str(e),
                "error_type": type(e).__name__,
                "event": event
            })
        )
        raise
