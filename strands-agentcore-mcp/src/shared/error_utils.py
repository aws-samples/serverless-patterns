"""Standardized error response formatting.

Target-type agnostic error handling utilities that produce consistent
AgentResponse objects for error conditions across the agent application.
"""

import logging
from typing import Optional

from src.shared.models import AgentResponse

logger = logging.getLogger(__name__)


def format_error_response(
    error_message: str,
    status_code: int = 500,
    log_message: Optional[str] = None,
) -> AgentResponse:
    """Create a standardized error AgentResponse.

    Logs the error and returns a consistent AgentResponse with success=False.

    Args:
        error_message: User-facing error description.
        status_code: HTTP-style status code for categorization (default 500).
        log_message: Optional detailed message for logging. If not provided,
            the error_message is logged.

    Returns:
        An AgentResponse with success=False and the error details.
    """
    log_msg = log_message or error_message
    if status_code >= 500:
        logger.error("Error [%d]: %s", status_code, log_msg)
    else:
        logger.warning("Error [%d]: %s", status_code, log_msg)

    return AgentResponse(
        success=False,
        response="",
        error=error_message,
    )


def format_unauthorized_response(detail: str = "Unauthorized") -> AgentResponse:
    """Create a 401 Unauthorized error response.

    Args:
        detail: Specific unauthorized reason (default "Unauthorized").

    Returns:
        An AgentResponse for authentication failures.
    """
    return format_error_response(detail, status_code=401)


def format_internal_error_response(
    detail: str = "Internal server error",
    exception: Optional[Exception] = None,
) -> AgentResponse:
    """Create a 500 Internal Server Error response.

    Optionally logs the full exception for debugging while returning
    a safe user-facing message.

    Args:
        detail: User-facing error description.
        exception: Optional exception to log for debugging.

    Returns:
        An AgentResponse for internal server errors.
    """
    log_msg = f"{detail}: {exception}" if exception else detail
    return format_error_response(detail, status_code=500, log_message=log_msg)
