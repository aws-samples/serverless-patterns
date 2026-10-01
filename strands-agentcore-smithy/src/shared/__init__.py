"""Shared modules for the agent application.

Provides target-type agnostic data models, utilities, and helpers.
"""

from src.shared.models import AgentRequest, AgentResponse, UserContext
from src.shared.jwt_utils import (
    JWTValidationError,
    extract_username,
    validate_token,
)
from src.shared.error_utils import (
    format_error_response,
    format_internal_error_response,
    format_unauthorized_response,
)
from src.shared.logging_utils import (
    configure_logging,
    get_correlation_id,
    get_logger,
)

__all__ = [
    "UserContext",
    "AgentRequest",
    "AgentResponse",
    "JWTValidationError",
    "extract_username",
    "validate_token",
    "format_error_response",
    "format_internal_error_response",
    "format_unauthorized_response",
    "configure_logging",
    "get_correlation_id",
    "get_logger",
]
