"""Logging utilities with user context, request ID correlation, and security."""

import logging
import json
import re
from typing import Optional, Dict, Any
from datetime import datetime

from .models import UserContext


# Patterns for sensitive data that should not be logged
SENSITIVE_PATTERNS = [
    r'Bearer\s+[A-Za-z0-9\-_]+\.[A-Za-z0-9\-_]+\.[A-Za-z0-9\-_]+',  # JWT tokens
    r'password["\']?\s*[:=]\s*["\']?[^"\'}\s]+',  # Passwords
    r'secret["\']?\s*[:=]\s*["\']?[^"\'}\s]+',  # Secrets
    r'api[_-]?key["\']?\s*[:=]\s*["\']?[^"\'}\s]+',  # API keys
]


def sanitize_log_data(data: Any) -> Any:
    """Remove sensitive information from log data.
    
    Args:
        data: Data to sanitize (string, dict, list, etc.)
        
    Returns:
        Sanitized data
    """
    if isinstance(data, str):
        sanitized = data
        for pattern in SENSITIVE_PATTERNS:
            sanitized = re.sub(pattern, '[REDACTED]', sanitized, flags=re.IGNORECASE)
        return sanitized
    
    elif isinstance(data, dict):
        return {k: sanitize_log_data(v) for k, v in data.items()}
    
    elif isinstance(data, list):
        return [sanitize_log_data(item) for item in data]
    
    return data


def get_logger(name: str, level: str = 'INFO') -> logging.Logger:
    """Get configured logger with structured formatting.
    
    Args:
        name: Logger name (typically __name__)
        level: Log level (DEBUG, INFO, WARNING, ERROR, CRITICAL)
        
    Returns:
        Configured logger instance
    """
    logger = logging.getLogger(name)
    logger.setLevel(getattr(logging, level.upper()))
    
    # Only add handler if not already configured
    if not logger.handlers:
        handler = logging.StreamHandler()
        handler.setLevel(getattr(logging, level.upper()))
        
        # Use JSON formatter for structured logging
        formatter = logging.Formatter(
            '{"timestamp": "%(asctime)s", "level": "%(levelname)s", '
            '"logger": "%(name)s", "message": "%(message)s"}'
        )
        handler.setFormatter(formatter)
        logger.addHandler(handler)
    
    return logger


def log_with_user_context(
    logger: logging.Logger,
    level: str,
    message: str,
    user_context: Optional[UserContext] = None,
    request_id: Optional[str] = None,
    **extra_fields
) -> None:
    """Log message with user context, request ID, and additional fields.
    
    This function ensures request_id is always included in log messages for
    correlation across services (Requirement 8.9).
    
    Args:
        logger: Logger instance
        level: Log level (info, warning, error, etc.)
        message: Log message
        user_context: User context for attribution
        request_id: Request ID for tracing (REQUIRED for correlation)
        **extra_fields: Additional fields to include in log
    """
    log_data = {
        'timestamp': datetime.utcnow().isoformat(),
        'message': message
    }
    
    # Always include request_id for correlation (Requirement 8.9)
    if request_id:
        log_data['request_id'] = request_id
    else:
        # Log warning if request_id is missing
        log_data['request_id'] = 'MISSING'
        log_data['warning'] = 'request_id not provided for log correlation'
    
    if user_context:
        log_data['user_id'] = user_context.user_id
        log_data['username'] = user_context.username
        log_data['client_id'] = user_context.client_id
    
    # Add extra fields
    log_data.update(extra_fields)
    
    # Sanitize before logging
    sanitized_data = sanitize_log_data(log_data)
    
    # Log as JSON
    log_method = getattr(logger, level.lower())
    log_method(json.dumps(sanitized_data))


class StructuredLogger:
    """Structured logger with automatic user context and request ID inclusion.
    
    This logger ensures request_id is included in all log messages for
    correlation across services (Requirement 8.9).
    """
    
    def __init__(
        self,
        logger: logging.Logger,
        request_id: str,
        user_context: Optional[UserContext] = None
    ):
        """Initialize structured logger.
        
        Args:
            logger: Base logger instance
            request_id: Request ID to include in all logs (REQUIRED)
            user_context: User context to include in all logs
        """
        self.logger = logger
        self.request_id = request_id
        self.user_context = user_context
    
    def _log(self, level: str, message: str, **extra_fields) -> None:
        """Internal log method that ensures request_id is always included."""
        log_with_user_context(
            self.logger,
            level,
            message,
            self.user_context,
            self.request_id,
            **extra_fields
        )
    
    def debug(self, message: str, **extra_fields) -> None:
        """Log debug message with request_id."""
        self._log('debug', message, **extra_fields)
    
    def info(self, message: str, **extra_fields) -> None:
        """Log info message with request_id."""
        self._log('info', message, **extra_fields)
    
    def warning(self, message: str, **extra_fields) -> None:
        """Log warning message with request_id."""
        self._log('warning', message, **extra_fields)
    
    def error(self, message: str, **extra_fields) -> None:
        """Log error message with request_id."""
        self._log('error', message, **extra_fields)
    
    def critical(self, message: str, **extra_fields) -> None:
        """Log critical message with request_id."""
        self._log('critical', message, **extra_fields)
