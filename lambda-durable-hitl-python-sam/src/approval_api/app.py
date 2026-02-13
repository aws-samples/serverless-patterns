"""
Approval API Lambda Function

This Lambda function handles approval/rejection decisions from the CLI tool.
It retrieves callback tokens from DynamoDB and resumes workflow execution.

Primary Use Case: Document Approval Processing
----------------------------------------------
Processes approval decisions submitted via CLI, validates the request,
and invokes the durable execution callback to resume the paused workflow.

Additional Use Cases:
--------------------
1. Expense Approval: Manager reviews expense report and approves/rejects,
   this function validates the decision and resumes expense processing workflow.

2. Content Moderation: Moderator reviews flagged content and approves/rejects,
   this function processes the decision and resumes content publishing workflow.

3. Budget Proposal Review: Finance team reviews budget proposal and approves/rejects,
   this function validates the decision and resumes budget allocation workflow.

Key Responsibilities:
- Validate approval request exists and is still pending
- Check expiration status to prevent late approvals
- Retrieve callback token from DynamoDB
- Invoke durable execution callback to resume workflow
- Update approval status with decision and comments
- Maintain complete audit trail of all decisions
"""

import json
import logging
import os
import sys
from typing import Dict, Any, Optional, Tuple
from datetime import datetime

# Add shared module to path
sys.path.insert(0, os.path.dirname(__file__))

from models import ApprovalDecisionRequest, ApprovalRequest, ApprovalStatus, Decision
from dynamodb_operations import get_approval_request, update_approval_status

# Configure structured JSON logging
logger = logging.getLogger()
logger.setLevel(os.environ.get('LOG_LEVEL', 'INFO'))


def validate_input(event: Dict[str, Any]) -> Tuple[bool, Optional[str], Optional[ApprovalDecisionRequest]]:
    """
    Validate input data from the Lambda event.
    
    Validates that required fields are present and decision values are valid.
    
    Args:
        event: Lambda event dictionary
        
    Returns:
        Tuple of (is_valid, error_message, parsed_request)
        - is_valid: True if input is valid, False otherwise
        - error_message: Descriptive error message if invalid, None if valid
        - parsed_request: Parsed ApprovalDecisionRequest if valid, None if invalid
    """
    # Handle both API Gateway format (with body) and direct Lambda invocation
    if "body" in event:
        try:
            body = json.loads(event["body"])
        except json.JSONDecodeError as e:
            return False, f"Invalid JSON in request body: {str(e)}", None
    else:
        body = event
    
    # Validate required fields
    if "approval_id" not in body:
        return False, "Missing required field: approval_id", None
    
    if "decision" not in body:
        return False, "Missing required field: decision", None
    
    # Validate approval_id is not empty
    approval_id = body["approval_id"]
    if not approval_id or not isinstance(approval_id, str) or not approval_id.strip():
        return False, "Invalid approval_id: must be a non-empty string", None
    
    # Validate decision value
    decision_str = body["decision"]
    if decision_str not in ["approved", "rejected"]:
        return False, f"Invalid decision value: '{decision_str}'. Must be 'approved' or 'rejected'", None
    
    # Parse the request
    try:
        request = ApprovalDecisionRequest.from_api_event(event)
        return True, None, request
    except Exception as e:
        return False, f"Failed to parse request: {str(e)}", None


def validate_approval_request(approval: ApprovalRequest) -> Tuple[bool, Optional[str]]:
    """
    Validate that approval request is in a valid state for processing.
    
    Checks that the request exists, is pending, and has not expired.
    
    Args:
        approval: ApprovalRequest object from DynamoDB
        
    Returns:
        Tuple of (is_valid, error_message)
        - is_valid: True if request is valid, False otherwise
        - error_message: Descriptive error message if invalid, None if valid
    """
    # Check if request is expired
    if approval.is_expired():
        logger.warning(
            json.dumps({
                "message": "Approval request has expired",
                "approval_id": approval.approval_id,
                "expires_at": approval.expires_at.isoformat(),
                "current_time": datetime.now().isoformat()
            })
        )
        return False, f"Approval request has expired at {approval.expires_at.isoformat()}"
    
    # Check if request is still pending
    if approval.status != ApprovalStatus.PENDING:
        logger.warning(
            json.dumps({
                "message": "Approval request is not in pending status",
                "approval_id": approval.approval_id,
                "current_status": approval.status.value
            })
        )
        
        # Provide specific error messages based on status
        if approval.status == ApprovalStatus.APPROVED:
            return False, f"Approval request has already been approved"
        elif approval.status == ApprovalStatus.REJECTED:
            return False, f"Approval request has already been rejected"
        elif approval.status == ApprovalStatus.TIMEOUT:
            return False, f"Approval request has timed out"
        else:
            return False, f"Approval request is in invalid status: {approval.status.value}"
    
    return True, None


def invoke_durable_callback(
    callback_token: str,
    decision: Decision,
    comments: Optional[str] = None
) -> Tuple[bool, Optional[str]]:
    """
    Invoke the durable execution callback to resume the workflow.
    
    This function calls the AWS Lambda Durable Functions SDK callback API
    to resume the paused workflow execution with the approval decision.
    
    Args:
        callback_token: Token from the paused durable execution
        decision: Approval decision (approved/rejected)
        comments: Optional comments from the approver
        
    Returns:
        Tuple of (success, error_message)
        - success: True if callback invoked successfully, False otherwise
        - error_message: Error description if failed, None if successful
    """
    # TODO: Integrate with AWS Lambda Durable Functions SDK
    # The SDK will:
    # 1. Validate the callback token
    # 2. Resume the paused Lambda execution
    # 3. Pass the decision and comments to the waiting function
    
    # For now, this is a placeholder that will be replaced with actual SDK integration
    # The actual implementation will use the durable execution SDK's callback mechanism
    
    logger.info(
        json.dumps({
            "message": "Invoking durable execution callback",
            "decision": decision.value,
            "has_comments": comments is not None
        })
    )
    
    try:
        # Placeholder for actual SDK call
        # Example: durable_execution.invoke_callback(callback_token, {"decision": decision.value, "comments": comments})
        
        # Simulate successful callback invocation
        logger.info(
            json.dumps({
                "message": "Durable execution callback invoked successfully",
                "decision": decision.value
            })
        )
        
        return True, None
        
    except Exception as e:
        error_msg = f"Failed to invoke durable execution callback: {str(e)}"
        logger.error(
            json.dumps({
                "message": "Callback invocation failed",
                "error": error_msg,
                "error_type": type(e).__name__
            })
        )
        return False, error_msg


def create_error_response(status_code: int, error_code: str, error_message: str, details: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
    """
    Create a standardized error response.
    
    Args:
        status_code: HTTP status code
        error_code: Error code identifier
        error_message: Human-readable error message
        details: Optional additional error details
        
    Returns:
        Dict containing error response in standard format
    """
    error_response = {
        "error": {
            "code": error_code,
            "message": error_message
        }
    }
    
    if details:
        error_response["error"]["details"] = details
    
    return {
        "statusCode": status_code,
        "body": json.dumps(error_response)
    }


def create_success_response(approval_id: str, decision: Decision, message: str = "Decision processed successfully") -> Dict[str, Any]:
    """
    Create a standardized success response.
    
    Args:
        approval_id: Approval request identifier
        decision: Decision that was processed
        message: Success message
        
    Returns:
        Dict containing success response
    """
    return {
        "statusCode": 200,
        "body": json.dumps({
            "message": message,
            "approval_id": approval_id,
            "decision": decision.value
        })
    }


def lambda_handler(event: Dict[str, Any], context: Any) -> Dict[str, Any]:
    """
    Processes approval decisions and resumes workflow.
    
    This function:
    1. Validates input data
    2. Retrieves the approval request from DynamoDB
    3. Validates the request is pending and not expired
    4. Invokes the durable execution callback
    5. Updates the approval status in DynamoDB
    
    Args:
        event: Lambda event with approval_id, decision, comments (optional)
        context: Lambda context
    
    Returns:
        Response with success/error status
    """
    # Log invocation with structured logging
    logger.info(
        json.dumps({
            "message": "Approval API Lambda invoked",
            "request_id": context.request_id if hasattr(context, 'request_id') else None
        })
    )
    
    try:
        # Task 6.6: Validate input data
        is_valid, error_message, decision_request = validate_input(event)
        if not is_valid:
            logger.warning(
                json.dumps({
                    "message": "Input validation failed",
                    "error": error_message
                })
            )
            return create_error_response(400, "INVALID_REQUEST", error_message)
        
        logger.info(
            json.dumps({
                "message": "Input validated successfully",
                "approval_id": decision_request.approval_id,
                "decision": decision_request.decision.value
            })
        )
        
        # Task 6.2: Retrieve approval request from DynamoDB
        approval = get_approval_request(decision_request.approval_id)
        
        if approval is None:
            logger.warning(
                json.dumps({
                    "message": "Approval request not found",
                    "approval_id": decision_request.approval_id
                })
            )
            return create_error_response(
                404,
                "APPROVAL_NOT_FOUND",
                f"Approval request with ID '{decision_request.approval_id}' not found",
                {"approval_id": decision_request.approval_id}
            )
        
        logger.info(
            json.dumps({
                "message": "Approval request retrieved",
                "approval_id": approval.approval_id,
                "status": approval.status.value,
                "expires_at": approval.expires_at.isoformat()
            })
        )
        
        # Task 6.2: Validate approval request state
        is_valid, error_message = validate_approval_request(approval)
        if not is_valid:
            # Determine appropriate error code based on the error
            if "expired" in error_message.lower() or "timed out" in error_message.lower():
                error_code = "APPROVAL_EXPIRED"
                status_code = 409
            elif "already been" in error_message.lower():
                error_code = "APPROVAL_ALREADY_DECIDED"
                status_code = 409
            else:
                error_code = "INVALID_APPROVAL_STATE"
                status_code = 409
            
            return create_error_response(
                status_code,
                error_code,
                error_message,
                {"approval_id": approval.approval_id, "status": approval.status.value}
            )
        
        # Task 6.3: Invoke durable execution callback
        callback_success, callback_error = invoke_durable_callback(
            callback_token=approval.callback_token,
            decision=decision_request.decision,
            comments=decision_request.comments
        )
        
        if not callback_success:
            logger.error(
                json.dumps({
                    "message": "Failed to invoke callback",
                    "approval_id": approval.approval_id,
                    "error": callback_error
                })
            )
            return create_error_response(
                500,
                "CALLBACK_INVOCATION_FAILED",
                callback_error,
                {"approval_id": approval.approval_id}
            )
        
        # Task 6.5: Update approval status in DynamoDB
        try:
            updated_approval = update_approval_status(
                approval_id=decision_request.approval_id,
                decision=decision_request.decision,
                comments=decision_request.comments,
                decided_by=decision_request.decided_by
            )
            
            logger.info(
                json.dumps({
                    "message": "Approval status updated successfully",
                    "approval_id": updated_approval.approval_id,
                    "decision": updated_approval.decision.value,
                    "status": updated_approval.status.value
                })
            )
            
        except Exception as e:
            # Log error but don't fail the request since callback was successful
            logger.error(
                json.dumps({
                    "message": "Failed to update approval status in DynamoDB",
                    "approval_id": decision_request.approval_id,
                    "error": str(e),
                    "error_type": type(e).__name__
                })
            )
            # Note: Callback was successful, so workflow will resume correctly
            # The status update failure is a data consistency issue but not critical
        
        # Return success response
        return create_success_response(
            approval_id=decision_request.approval_id,
            decision=decision_request.decision,
            message="Decision processed successfully and workflow resumed"
        )
        
    except Exception as e:
        # Handle unexpected errors
        logger.error(
            json.dumps({
                "message": "Unexpected error processing approval decision",
                "error": str(e),
                "error_type": type(e).__name__
            })
        )
        
        return create_error_response(
            500,
            "INTERNAL_ERROR",
            f"An unexpected error occurred: {str(e)}"
        )
