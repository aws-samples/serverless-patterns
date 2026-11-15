"""Error handling utilities with retry logic and timeout management."""

import time
import json
from typing import Callable, Any, Optional, Dict
from functools import wraps
import signal


class TimeoutError(Exception):
    """Raised when an operation times out."""
    pass


class TransientError(Exception):
    """Raised for transient errors that should be retried."""
    pass


def format_error_response(
    status_code: int,
    error_message: str,
    error_code: Optional[str] = None
) -> dict:
    """Format error response for Lambda.
    
    Args:
        status_code: HTTP status code
        error_message: User-friendly error message
        error_code: Optional error code for categorization
        
    Returns:
        Lambda response dictionary
    """
    body = {'error': error_message}
    if error_code:
        body['error_code'] = error_code
    
    return {
        'statusCode': status_code,
        'body': json.dumps(body)
    }


def get_user_friendly_message(error_code: str) -> str:
    """Get user-friendly error message for AWS error codes.
    
    Args:
        error_code: AWS error code
        
    Returns:
        User-friendly error message
    """
    error_messages = {
        'AccessDenied': 'You do not have permission to perform this operation.',
        'AccessDeniedException': 'You do not have permission to perform this operation.',
        'Throttling': 'The service is temporarily busy. Please try again.',
        'ThrottlingException': 'The service is temporarily busy. Please try again.',
        'ServiceUnavailable': 'The service is temporarily unavailable. Please try again.',
        'InternalError': 'An internal error occurred. Please try again.',
        'InvalidParameterValue': 'Invalid parameter provided.',
        'ResourceNotFoundException': 'The requested resource was not found.',
        'ValidationException': 'Invalid request parameters.',
        'RequestTimeout': 'The request timed out. Please try again.',
        'NetworkingError': 'Network connection error. Please try again.',
    }
    
    return error_messages.get(
        error_code,
        'An error occurred while processing your request. Please try again.'
    )


def is_transient_error(error_code: str) -> bool:
    """Check if an error code represents a transient error.
    
    Args:
        error_code: AWS error code
        
    Returns:
        True if error is transient and should be retried
    """
    transient_codes = {
        'Throttling',
        'ThrottlingException',
        'ServiceUnavailable',
        'InternalError',
        'RequestTimeout',
        'NetworkingError',
        'TooManyRequestsException',
        'ProvisionedThroughputExceededException',
    }
    
    return error_code in transient_codes


def retry_with_backoff(
    func: Callable,
    max_attempts: int = 3,
    initial_delay: float = 1.0,
    backoff_factor: float = 2.0,
    max_delay: float = 10.0
) -> Any:
    """Retry function with exponential backoff.
    
    Args:
        func: Function to retry
        max_attempts: Maximum number of retry attempts
        initial_delay: Initial delay in seconds
        backoff_factor: Multiplier for delay after each attempt
        max_delay: Maximum delay between retries
        
    Returns:
        Function result
        
    Raises:
        Exception: If all retry attempts fail
    """
    delay = initial_delay
    last_exception = None
    
    for attempt in range(max_attempts):
        try:
            return func()
        except Exception as e:
            last_exception = e
            
            # Check if error is transient
            error_code = getattr(e, 'response', {}).get('Error', {}).get('Code', '')
            if not is_transient_error(error_code) and attempt == 0:
                # Non-transient error, don't retry
                raise
            
            if attempt < max_attempts - 1:
                # Calculate delay with exponential backoff
                wait_time = min(delay, max_delay)
                time.sleep(wait_time)
                delay *= backoff_factor
            else:
                # Last attempt failed
                raise last_exception
    
    raise last_exception


def timeout_wrapper(timeout_seconds: int):
    """Decorator to add timeout to function execution.
    
    Args:
        timeout_seconds: Timeout in seconds
        
    Returns:
        Decorated function
        
    Raises:
        TimeoutError: If function execution exceeds timeout
    """
    def decorator(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(*args, **kwargs):
            def timeout_handler(signum, frame):
                raise TimeoutError(f"Function {func.__name__} timed out after {timeout_seconds} seconds")
            
            # Set up signal handler
            old_handler = signal.signal(signal.SIGALRM, timeout_handler)
            signal.alarm(timeout_seconds)
            
            try:
                result = func(*args, **kwargs)
            finally:
                # Restore old handler and cancel alarm
                signal.alarm(0)
                signal.signal(signal.SIGALRM, old_handler)
            
            return result
        
        return wrapper
    
    return decorator


class ErrorHandler:
    """Centralized error handler for Lambda functions."""
    
    @staticmethod
    def handle_authentication_error(error: Exception) -> dict:
        """Handle authentication errors with generic messages.
        
        Args:
            error: Authentication error
            
        Returns:
            Lambda error response
        """
        # Return generic message to avoid exposing authentication details
        return format_error_response(
            401,
            'Invalid credentials',
            'AuthenticationError'
        )
    
    @staticmethod
    def handle_aws_error(error: Exception) -> dict:
        """Handle AWS service errors.
        
        Args:
            error: AWS ClientError
            
        Returns:
            Lambda error response
        """
        error_code = getattr(error, 'response', {}).get('Error', {}).get('Code', 'Unknown')
        message = get_user_friendly_message(error_code)
        
        status_code = 500
        if error_code in ['AccessDenied', 'AccessDeniedException']:
            status_code = 403
        elif error_code in ['ResourceNotFoundException']:
            status_code = 404
        elif error_code in ['Throttling', 'ThrottlingException']:
            status_code = 429
        
        return format_error_response(status_code, message, error_code)
    
    @staticmethod
    def handle_validation_error(error: Exception) -> dict:
        """Handle validation errors.
        
        Args:
            error: Validation error
            
        Returns:
            Lambda error response
        """
        return format_error_response(
            400,
            str(error),
            'ValidationError'
        )
    
    @staticmethod
    def handle_generic_error(error: Exception) -> dict:
        """Handle generic errors.
        
        Args:
            error: Generic error
            
        Returns:
            Lambda error response
        """
        return format_error_response(
            500,
            'An unexpected error occurred. Please try again.',
            'InternalError'
        )
