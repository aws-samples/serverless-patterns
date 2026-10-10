"""Agent Lambda handler for AI-powered natural language processing."""

import os
import json
import uuid
from typing import Optional, Dict, Any
from datetime import datetime

from shared.models import AgentRequest, AgentResponse, UserContext
from shared.jwt_utils import validate_jwt, extract_user_context
from shared.logging_utils import get_logger, StructuredLogger
from shared.error_utils import ErrorHandler, format_error_response


# Environment variables
COGNITO_JWKS_URL = os.environ.get('COGNITO_JWKS_URL', '')
GATEWAY_ID = os.environ.get('GATEWAY_ID', '')
BEDROCK_MODEL_ID = os.environ.get('BEDROCK_MODEL_ID', 'us.anthropic.claude-sonnet-4-6')
AWS_REGION = os.environ.get('AWS_REGION', 'us-east-1')
LOG_LEVEL = os.environ.get('LOG_LEVEL', 'INFO')

# Initialize logger
logger = get_logger(__name__, LOG_LEVEL)


def lambda_handler(event: dict, context: Any) -> dict:
    """
    Process AI agent requests with user authentication.
    
    Args:
        event: Lambda event with headers and body containing:
            - headers.Authorization: Bearer JWT token
            - body.prompt: User's natural language prompt
            - body.session_id: Optional session ID for conversation continuity
        context: AWS Lambda context
        
    Returns:
        Lambda response with:
            - statusCode: HTTP status code
            - body: JSON with response, session_id, user_context
    """
    request_id = context.request_id if hasattr(context, 'request_id') else str(uuid.uuid4())
    structured_logger = None
    
    try:
        # Parse request
        agent_request = AgentRequest.from_event(event)
        
        # Validate JWT token
        if not agent_request.jwt_token:
            logger.error(json.dumps({
                'message': 'Missing JWT token',
                'request_id': request_id
            }))
            return ErrorHandler.handle_authentication_error(
                ValueError("Missing authentication token")
            )
        
        try:
            claims = validate_jwt(agent_request.jwt_token, COGNITO_JWKS_URL)
            user_context = extract_user_context(claims)
        except ValueError as e:
            logger.error(json.dumps({
                'message': 'JWT validation failed',
                'error': str(e),
                'request_id': request_id
            }))
            return ErrorHandler.handle_authentication_error(e)
        
        # Initialize structured logger with user context
        structured_logger = StructuredLogger(logger, user_context, request_id)
        structured_logger.info('Agent request received', prompt_length=len(agent_request.prompt))
        
        # Process agent request
        response_text, session_id = process_agent_request(
            agent_request.prompt,
            agent_request.jwt_token,
            user_context,
            agent_request.session_id,
            structured_logger
        )
        
        # Create response
        agent_response = AgentResponse(
            response=response_text,
            session_id=session_id,
            user_context=user_context
        )
        
        structured_logger.info('Agent request completed successfully')
        return agent_response.to_lambda_response()
        
    except Exception as e:
        if structured_logger:
            structured_logger.error('Agent request failed', error=str(e))
        else:
            logger.error(json.dumps({
                'message': 'Agent request failed',
                'error': str(e),
                'request_id': request_id
            }))
        
        return ErrorHandler.handle_generic_error(e)


def process_agent_request(
    prompt: str,
    jwt_token: str,
    user_context: UserContext,
    session_id: Optional[str],
    logger: StructuredLogger
) -> tuple[str, str]:
    """
    Process agent request through the Strands SDK AI pipeline.
    
    This function orchestrates:
    1. Strands agent initialization with MCPClient and BedrockModel
    2. Tool discovery via MCP protocol through AgentCore Gateway
    3. AI processing with Claude via SDK agentic loop
    4. Tool execution through Gateway MCP endpoint
    
    Args:
        prompt: User's natural language prompt
        jwt_token: JWT token for Gateway authorization
        user_context: User identity information
        session_id: Optional session ID for conversation continuity
        logger: Structured logger with user context
        
    Returns:
        Tuple of (response_text, session_id)
    """
    from .agent_processor import AgentProcessor
    
    processor = AgentProcessor(
        gateway_id=GATEWAY_ID,
        model_id=BEDROCK_MODEL_ID,
        region=AWS_REGION,
        logger=logger
    )
    
    # Process request
    response_text, session_id = processor.process(
        prompt=prompt,
        jwt_token=jwt_token,
        user_context=user_context,
        session_id=session_id
    )
    
    return response_text, session_id
