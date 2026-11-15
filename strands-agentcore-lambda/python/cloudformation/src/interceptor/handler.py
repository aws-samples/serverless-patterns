"""Gateway Request Interceptor Lambda handler.

This Lambda function extracts user identity from JWT tokens and injects
user context into tool parameters before forwarding to Tool Lambda.
"""

import json
import os
from typing import Dict, Any, Optional

from shared.models import InterceptorRequest, InterceptorResponse, UserContext
from shared.logging_utils import get_logger, StructuredLogger
from shared.jwt_utils import decode_jwt_payload


# Initialize logger
logger = get_logger(__name__, level=os.environ.get('LOG_LEVEL', 'INFO'))


def extract_user_context_from_jwt(jwt_token: str) -> Optional[UserContext]:
    """Extract user context from JWT token.
    
    Args:
        jwt_token: JWT access token
        
    Returns:
        UserContext if extraction succeeds, None otherwise
    """
    try:
        # Decode JWT payload without verification
        # Gateway validates the token independently
        claims = decode_jwt_payload(jwt_token)
        
        # Extract user claims
        user_id = claims.get('sub')
        username = claims.get('username')
        client_id = claims.get('client_id')
        
        # Return UserContext with available claims
        # If some claims are missing, use 'unknown' as fallback
        return UserContext(
            user_id=user_id if user_id else 'unknown',
            username=username if username else 'unknown',
            client_id=client_id if client_id else 'unknown'
        )
        
    except Exception as e:
        logger.error(f"Failed to extract user context from JWT: {e}")
        return None


def lambda_handler(event: Dict[str, Any], context: Any) -> Dict[str, Any]:
    """Gateway Request Interceptor Lambda handler.
    
    Extracts JWT claims and adds user_context to tool parameters.
    
    Args:
        event: Lambda event from AgentCore Gateway with format:
            {
                "mcp": {
                    "rawRequest": {...},
                    "gatewayRequest": {
                        "body": {
                            "jsonrpc": "2.0",
                            "method": "tools/call",
                            "params": {
                                "name": "tool-name",
                                "arguments": {...}
                            },
                            "id": "..."
                        },
                        "headers": {
                            "Authorization": "Bearer <jwt_token>"
                        }
                    }
                }
            }
        context: AWS Lambda context
        
    Returns:
        Transformed request with user_context added to arguments:
            {
                "interceptorOutputVersion": "1.0",
                "mcp": {
                    "transformedGatewayRequest": {
                        "body": {
                            "jsonrpc": "2.0",
                            "method": "tools/call",
                            "params": {
                                "name": "tool-name",
                                "arguments": {
                                    ...original_arguments,
                                    "user_context": {
                                        "user_id": str,
                                        "username": str,
                                        "client_id": str
                                    }
                                }
                            },
                            "id": "..."
                        }
                    }
                }
            }
    """
    request_id = context.request_id if hasattr(context, 'request_id') else 'unknown'
    
    try:
        # Extract MCP data from event
        mcp_data = event.get('mcp', {})
        gateway_request = mcp_data.get('gatewayRequest', {})
        request_body = gateway_request.get('body', {})
        headers = gateway_request.get('headers', {})
        
        # Extract JWT token from Authorization header
        auth_header = headers.get('Authorization', '')
        jwt_token = auth_header.replace('Bearer ', '') if auth_header else ''
        
        # Extract tool name and arguments from MCP request
        params = request_body.get('params', {})
        tool_name = params.get('name', '')
        arguments = params.get('arguments', {})
        
        # Log request received
        logger.info(json.dumps({
            'message': 'Interceptor request received',
            'request_id': request_id,
            'tool_name': tool_name,
            'has_jwt': bool(jwt_token)
        }))
        
        # Extract user context from JWT
        user_context = None
        if jwt_token:
            user_context = extract_user_context_from_jwt(jwt_token)
        
        # If user context extraction failed or JWT missing, return original request
        if not user_context:
            logger.warning(json.dumps({
                'message': 'Failed to extract user context, returning original request',
                'request_id': request_id,
                'has_jwt': bool(jwt_token)
            }))
            
            # Return original request unchanged
            return {
                'interceptorOutputVersion': '1.0',
                'mcp': {
                    'transformedGatewayRequest': {
                        'body': request_body
                    }
                }
            }
        
        # Add user_context to arguments
        transformed_arguments = {
            **arguments,
            'user_context': user_context.to_dict()
        }
        
        # Create transformed request body
        transformed_body = {
            **request_body,
            'params': {
                **params,
                'arguments': transformed_arguments
            }
        }
        
        # Log successful transformation
        logger.info(json.dumps({
            'message': 'User context added to tool arguments',
            'request_id': request_id,
            'tool_name': tool_name,
            'user_id': user_context.user_id,
            'username': user_context.username
        }))
        
        # Return transformed request
        return {
            'interceptorOutputVersion': '1.0',
            'mcp': {
                'transformedGatewayRequest': {
                    'body': transformed_body
                }
            }
        }
        
    except Exception as e:
        # Log error but return original request to avoid breaking the flow
        logger.error(json.dumps({
            'message': 'Interceptor error, returning original request',
            'request_id': request_id,
            'error': str(e)
        }))
        
        # Return original request unchanged
        try:
            mcp_data = event.get('mcp', {})
            gateway_request = mcp_data.get('gatewayRequest', {})
            request_body = gateway_request.get('body', {})
            
            return {
                'interceptorOutputVersion': '1.0',
                'mcp': {
                    'transformedGatewayRequest': {
                        'body': request_body
                    }
                }
            }
        except Exception:
            # If even parsing the original request fails, return minimal response
            return {
                'interceptorOutputVersion': '1.0',
                'mcp': {
                    'transformedGatewayRequest': {
                        'body': {}
                    }
                }
            }
