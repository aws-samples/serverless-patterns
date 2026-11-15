"""Tool Lambda handler for MCP tool execution with user attribution."""

import os
import json
import boto3
from typing import Dict, Any
from datetime import datetime
from botocore.exceptions import ClientError

from shared.models import ToolRequest, ToolResponse, UserContext
from shared.logging_utils import get_logger, StructuredLogger
from shared.error_utils import (
    retry_with_backoff,
    get_user_friendly_message,
    is_transient_error,
    ErrorHandler
)


# Initialize logger
logger = get_logger(__name__, level=os.environ.get('LOG_LEVEL', 'INFO'))

# Initialize AWS clients
s3_client = boto3.client('s3', region_name=os.environ.get('AWS_REGION', 'us-east-1'))


def list_s3_buckets(user_context: UserContext) -> Dict[str, Any]:
    """List all S3 buckets with creation dates.
    
    Args:
        user_context: User context for attribution
        
    Returns:
        Dictionary with bucket list and user context
        
    Raises:
        ClientError: If S3 API call fails
    """
    structured_logger = StructuredLogger(logger, user_context)
    
    structured_logger.info(
        "Executing list-s3-buckets tool",
        tool_name="list-s3-buckets"
    )
    
    try:
        # Execute S3 ListBuckets with retry logic
        def list_buckets_call():
            return s3_client.list_buckets()
        
        response = retry_with_backoff(list_buckets_call, max_attempts=3)
        
        # Format bucket list
        buckets = []
        for bucket in response.get('Buckets', []):
            buckets.append({
                'name': bucket['Name'],
                'creation_date': bucket['CreationDate'].isoformat()
            })
        
        structured_logger.info(
            "Successfully listed S3 buckets",
            tool_name="list-s3-buckets",
            bucket_count=len(buckets)
        )
        
        return {
            'buckets': buckets,
            'count': len(buckets)
        }
        
    except ClientError as e:
        error_code = e.response['Error']['Code']
        structured_logger.error(
            f"AWS service error: {error_code}",
            tool_name="list-s3-buckets",
            error_code=error_code
        )
        raise


def route_tool_execution(tool_name: str, user_context: UserContext) -> Dict[str, Any]:
    """Route tool execution to appropriate implementation.
    
    Args:
        tool_name: Name of the tool to execute
        user_context: User context for attribution
        
    Returns:
        Tool execution result
        
    Raises:
        ValueError: If tool name is not recognized
        ClientError: If AWS operation fails
    """
    tool_registry = {
        'list-s3-buckets': list_s3_buckets,
        'list-s3-buckets___list-s3-buckets': list_s3_buckets  # Handle Gateway format
    }
    
    if tool_name not in tool_registry:
        raise ValueError(f"Unknown tool: {tool_name}")
    
    tool_func = tool_registry[tool_name]
    return tool_func(user_context)


def lambda_handler(event: Dict[str, Any], context: Any) -> Dict[str, Any]:
    """Tool Lambda handler for MCP tool execution.
    
    Args:
        event: Lambda event from AgentCore Gateway containing:
            - user_context: User context added by Gateway Interceptor
        context: Lambda context
        
    Returns:
        Tool execution result with user attribution
    """
    request_id = context.aws_request_id if context else 'local'
    
    try:
        # Parse ToolRequest from event
        tool_request = ToolRequest.from_event(event)
        
        # Create structured logger with user context
        structured_logger = StructuredLogger(
            logger,
            tool_request.user_context,
            request_id
        )
        
        structured_logger.info(
            "Tool Lambda invocation started",
            tool_name=tool_request.tool_name
        )
        
        # Validate user context
        if not tool_request.user_context.user_id or tool_request.user_context.user_id == 'unknown':
            structured_logger.warning(
                "Missing or invalid user context",
                tool_name=tool_request.tool_name
            )
        
        # Route to appropriate tool implementation
        result = route_tool_execution(
            tool_request.tool_name,
            tool_request.user_context
        )
        
        # Create ToolResponse with user attribution
        tool_response = ToolResponse(
            result=result,
            user_context=tool_request.user_context
        )
        
        structured_logger.info(
            "Tool Lambda invocation completed successfully",
            tool_name=tool_request.tool_name
        )
        
        return tool_response.to_dict()
        
    except ValueError as e:
        # Validation error
        structured_logger = StructuredLogger(logger, None, request_id)
        structured_logger.error(
            f"Validation error: {str(e)}",
            error_type="ValidationError"
        )
        return ErrorHandler.handle_validation_error(e)
        
    except ClientError as e:
        # AWS service error
        error_code = e.response['Error']['Code']
        user_context = getattr(tool_request, 'user_context', None) if 'tool_request' in locals() else None
        structured_logger = StructuredLogger(logger, user_context, request_id)
        
        structured_logger.error(
            f"AWS service error: {error_code}",
            error_code=error_code,
            error_type="AWSServiceError"
        )
        
        # Return user-friendly error message
        error_response = ErrorHandler.handle_aws_error(e)
        return {
            'error': json.loads(error_response['body'])['error'],
            'error_code': error_code
        }
        
    except Exception as e:
        # Generic error
        user_context = getattr(tool_request, 'user_context', None) if 'tool_request' in locals() else None
        structured_logger = StructuredLogger(logger, user_context, request_id)
        
        structured_logger.error(
            f"Unexpected error: {str(e)}",
            error_type="UnexpectedError"
        )
        
        error_response = ErrorHandler.handle_generic_error(e)
        return {
            'error': json.loads(error_response['body'])['error']
        }
