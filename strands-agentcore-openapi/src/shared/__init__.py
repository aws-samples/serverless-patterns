"""Shared utilities and data models for OpenAPI Agent Gateway."""

from .models import (
    UserContext,
    AgentRequest,
    AgentResponse,
    ToolDefinition,
    WeatherData,
    DailyForecast,
    ForecastData,
    ToolRequest,
    ToolResponse,
    ConversationTurn,
    ConversationContext,
)

from .logging_utils import (
    get_logger,
    log_with_user_context,
    sanitize_log_data,
    StructuredLogger,
)

from .error_utils import (
    format_error_response,
    get_user_friendly_message,
    is_transient_error,
    retry_with_backoff,
    timeout_wrapper,
    ErrorHandler,
    TimeoutError,
    TransientError,
)

from .jwt_utils import (
    validate_jwt,
    extract_user_context,
    decode_jwt_payload,
    get_jwks,
)

__all__ = [
    # Models
    'UserContext',
    'AgentRequest',
    'AgentResponse',
    'ToolDefinition',
    'WeatherData',
    'DailyForecast',
    'ForecastData',
    'ToolRequest',
    'ToolResponse',
    'ConversationTurn',
    'ConversationContext',
    # Logging
    'get_logger',
    'log_with_user_context',
    'sanitize_log_data',
    'StructuredLogger',
    # Error handling
    'format_error_response',
    'get_user_friendly_message',
    'is_transient_error',
    'retry_with_backoff',
    'timeout_wrapper',
    'ErrorHandler',
    'TimeoutError',
    'TransientError',
    # JWT
    'validate_jwt',
    'extract_user_context',
    'decode_jwt_payload',
    'get_jwks',
]
