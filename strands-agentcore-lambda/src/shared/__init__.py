"""Shared utilities and data models for Serverless AI Agent Gateway."""

from .models import (
    UserContext,
    AgentRequest,
    AgentResponse,
    ToolRequest,
    ToolResponse,
    ConversationContext,
    ConversationTurn,
    InterceptorRequest,
    InterceptorResponse
)
# JWT utils commented out for Tool Lambda (doesn't need JWT validation)
# from .jwt_utils import validate_jwt, extract_user_context
from .logging_utils import get_logger, log_with_user_context
from .error_utils import (
    format_error_response,
    retry_with_backoff,
    timeout_wrapper,
    get_user_friendly_message
)

__all__ = [
    'UserContext',
    'AgentRequest',
    'AgentResponse',
    'ToolRequest',
    'ToolResponse',
    'ConversationContext',
    'ConversationTurn',
    'InterceptorRequest',
    'InterceptorResponse',
    # 'validate_jwt',
    # 'extract_user_context',
    'get_logger',
    'log_with_user_context',
    'format_error_response',
    'retry_with_backoff',
    'timeout_wrapper',
    'get_user_friendly_message'
]
