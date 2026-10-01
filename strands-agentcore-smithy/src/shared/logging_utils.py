"""Structured logging with correlation IDs.

Target-type agnostic logging utilities that provide consistent structured
logging across the agent application. Supports correlation IDs for request
tracing through Lambda invocations.
"""

import logging
import uuid
from typing import Any, Dict, Optional


def get_correlation_id(event: Optional[Dict[str, Any]] = None) -> str:
    """Extract or generate a correlation ID for request tracing.

    Attempts to extract a correlation ID from the Lambda event's request
    context. Falls back to generating a new UUID if none is found.

    Args:
        event: Optional Lambda event dictionary.

    Returns:
        A correlation ID string.
    """
    if event:
        # Check for AWS request ID in the event context
        request_context = event.get("requestContext", {})
        request_id = request_context.get("requestId")
        if request_id:
            return request_id

    return str(uuid.uuid4())


def configure_logging(
    level: int = logging.INFO,
    correlation_id: Optional[str] = None,
) -> logging.Logger:
    """Configure structured logging for the application.

    Sets up the root logger with a structured format that includes
    the correlation ID for request tracing.

    Args:
        level: Logging level (default INFO).
        correlation_id: Optional correlation ID to include in log format.

    Returns:
        The configured root logger.
    """
    log_format = "[%(levelname)s]"
    if correlation_id:
        log_format += f" [{correlation_id}]"
    log_format += " %(name)s - %(message)s"

    logging.basicConfig(level=level, format=log_format, force=True)
    # Enable debug logging for strands to see tool call details
    logging.getLogger("strands").setLevel(logging.DEBUG)
    return logging.getLogger()


def get_logger(name: str) -> logging.Logger:
    """Get a named logger instance.

    Convenience wrapper around logging.getLogger for consistent
    logger creation across modules.

    Args:
        name: Logger name, typically __name__ of the calling module.

    Returns:
        A named Logger instance.
    """
    return logging.getLogger(name)
