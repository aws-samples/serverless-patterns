"""
DynamoDB operations for the Lambda Durable HITL pattern.

This module provides functions for creating, retrieving, updating, and querying
approval requests in DynamoDB with proper error handling and retry logic.
"""

import os
import uuid
import time
from datetime import datetime, timedelta
from typing import List, Optional
import boto3
from botocore.exceptions import ClientError

try:
    from .models import ApprovalRequest, ApprovalStatus, Decision
except ImportError:
    from models import ApprovalRequest, ApprovalStatus, Decision


# Initialize DynamoDB client
dynamodb = boto3.resource('dynamodb')


def get_table():
    """
    Get the DynamoDB table for approval requests.
    
    Returns:
        boto3 Table resource
    """
    table_name = os.environ.get('APPROVALS_TABLE_NAME')
    if not table_name:
        raise ValueError("APPROVALS_TABLE_NAME environment variable not set")
    return dynamodb.Table(table_name)


def _retry_with_backoff(operation, max_retries=3, initial_delay=0.1):
    """
    Execute a DynamoDB operation with exponential backoff retry logic.
    
    Args:
        operation: Callable that performs the DynamoDB operation
        max_retries: Maximum number of retry attempts
        initial_delay: Initial delay in seconds (doubles with each retry)
        
    Returns:
        Result of the operation
        
    Raises:
        ClientError: If operation fails after all retries
    """
    delay = initial_delay
    last_exception = None
    
    for attempt in range(max_retries):
        try:
            return operation()
        except ClientError as e:
            last_exception = e
            error_code = e.response['Error']['Code']
            
            # Retry on throttling and server errors
            if error_code in ['ProvisionedThroughputExceededException', 
                            'ThrottlingException',
                            'InternalServerError',
                            'ServiceUnavailable']:
                if attempt < max_retries - 1:
                    time.sleep(delay)
                    delay *= 2  # Exponential backoff
                    continue
            
            # Don't retry on other errors
            raise
    
    # All retries exhausted
    raise last_exception


def create_approval_request(
    callback_token: str,
    document_id: str,
    document_name: str,
    requester: str,
    timeout_seconds: int = 3600
) -> ApprovalRequest:
    """
    Create a new approval request in DynamoDB.
    
    Args:
        callback_token: Durable execution callback token
        document_id: Unique identifier for the document
        document_name: Human-readable document name
        requester: User who submitted the document
        timeout_seconds: Timeout duration in seconds (default 1 hour)
        
    Returns:
        ApprovalRequest: Created approval request object
        
    Raises:
        ClientError: If DynamoDB operation fails after retries
    """
    table = get_table()
    
    # Generate unique approval ID
    approval_id = str(uuid.uuid4())
    
    # Calculate timestamps
    now = datetime.now()
    expires_at = now + timedelta(seconds=timeout_seconds)
    
    # Calculate TTL (7 days after creation for automatic cleanup)
    ttl = int((now + timedelta(days=7)).timestamp())
    
    # Create approval request object
    approval = ApprovalRequest(
        approval_id=approval_id,
        callback_token=callback_token,
        document_id=document_id,
        document_name=document_name,
        requester=requester,
        status=ApprovalStatus.PENDING,
        created_at=now,
        updated_at=now,
        expires_at=expires_at,
        ttl=ttl
    )
    
    # Store in DynamoDB with retry logic
    def put_operation():
        table.put_item(Item=approval.to_dynamodb_item())
    
    _retry_with_backoff(put_operation)
    
    return approval


def get_approval_request(approval_id: str) -> Optional[ApprovalRequest]:
    """
    Retrieve an approval request from DynamoDB.
    
    Args:
        approval_id: Unique identifier for the approval request
        
    Returns:
        ApprovalRequest: Retrieved approval request, or None if not found
        
    Raises:
        ClientError: If DynamoDB operation fails after retries
    """
    table = get_table()
    
    def get_operation():
        response = table.get_item(Key={'approval_id': approval_id})
        return response
    
    response = _retry_with_backoff(get_operation)
    
    if 'Item' not in response:
        return None
    
    return ApprovalRequest.from_dynamodb_item(response['Item'])


def update_approval_status(
    approval_id: str,
    decision: Decision,
    comments: Optional[str] = None,
    decided_by: Optional[str] = None
) -> ApprovalRequest:
    """
    Update the status of an approval request with a decision.
    
    Args:
        approval_id: Unique identifier for the approval request
        decision: Approval decision (approved/rejected/timeout)
        comments: Optional comments from the approver
        decided_by: Optional identifier of who made the decision
        
    Returns:
        ApprovalRequest: Updated approval request object
        
    Raises:
        ValueError: If approval request not found
        ClientError: If DynamoDB operation fails after retries
    """
    table = get_table()
    
    # Map decision to status
    status_map = {
        Decision.APPROVED: ApprovalStatus.APPROVED,
        Decision.REJECTED: ApprovalStatus.REJECTED,
        Decision.TIMEOUT: ApprovalStatus.TIMEOUT
    }
    status = status_map[decision]
    
    # Calculate timestamps
    now = datetime.now()
    decided_at = now
    
    # Build update expression
    update_expression = "SET #status = :status, updated_at = :updated_at, decision = :decision, decided_at = :decided_at"
    expression_attribute_names = {"#status": "status"}
    expression_attribute_values = {
        ":status": status.value,
        ":updated_at": now.isoformat(),
        ":decision": decision.value,
        ":decided_at": decided_at.isoformat()
    }
    
    if comments:
        update_expression += ", comments = :comments"
        expression_attribute_values[":comments"] = comments
    
    if decided_by:
        update_expression += ", decided_by = :decided_by"
        expression_attribute_values[":decided_by"] = decided_by
    
    def update_operation():
        response = table.update_item(
            Key={'approval_id': approval_id},
            UpdateExpression=update_expression,
            ExpressionAttributeNames=expression_attribute_names,
            ExpressionAttributeValues=expression_attribute_values,
            ReturnValues='ALL_NEW'
        )
        return response
    
    response = _retry_with_backoff(update_operation)
    
    if 'Attributes' not in response:
        raise ValueError(f"Approval request with ID '{approval_id}' not found")
    
    return ApprovalRequest.from_dynamodb_item(response['Attributes'])


def query_pending_approvals(limit: int = 100) -> List[ApprovalRequest]:
    """
    Query for all pending approval requests using the StatusIndex GSI.
    
    Args:
        limit: Maximum number of results to return (default 100)
        
    Returns:
        List[ApprovalRequest]: List of pending approval requests
        
    Raises:
        ClientError: If DynamoDB operation fails after retries
    """
    table = get_table()
    
    def query_operation():
        response = table.query(
            IndexName='StatusIndex',
            KeyConditionExpression='#status = :status',
            ExpressionAttributeNames={'#status': 'status'},
            ExpressionAttributeValues={':status': ApprovalStatus.PENDING.value},
            Limit=limit,
            ScanIndexForward=False  # Sort by created_at descending (newest first)
        )
        return response
    
    response = _retry_with_backoff(query_operation)
    
    # Convert items to ApprovalRequest objects and filter out expired ones
    approvals = []
    for item in response.get('Items', []):
        approval = ApprovalRequest.from_dynamodb_item(item)
        if approval.is_pending():  # Only include non-expired pending approvals
            approvals.append(approval)
    
    return approvals
