"""Lambda entry point for the agent function.

Target-type agnostic handler that extracts JWT tokens from the Lambda event,
validates them, creates a UserContext, and delegates processing to the
agent_processor module. Returns AgentResponse as a dict suitable for
Lambda response serialization.
"""

import json
from dataclasses import asdict

from src.agent.agent_processor import process_request
from src.shared.error_utils import (
    format_internal_error_response,
    format_unauthorized_response,
)
from src.shared.jwt_utils import JWTValidationError, extract_username, validate_token
from src.shared.logging_utils import configure_logging, get_correlation_id
from src.shared.models import AgentRequest, UserContext


def _extract_token(event: dict) -> str | None:
    """Extract JWT token from the Lambda event.

    Checks for the token in two locations:
    1. event["token"] — direct token field
    2. event["headers"]["Authorization"] — Bearer token from headers

    Args:
        event: The Lambda event dictionary.

    Returns:
        The JWT token string, or None if not found.
    """
    token = event.get("token")
    if token:
        return token

    headers = event.get("headers", {})
    auth_header = headers.get("Authorization", "")
    if auth_header.startswith("Bearer "):
        return auth_header[len("Bearer "):]

    # Return raw Authorization header if present (non-Bearer)
    return auth_header or None


def lambda_handler(event: dict, context) -> dict:
    """Lambda entry point for agent invocations.

    Extracts and validates the JWT token from the event, builds an
    AgentRequest with the user's prompt and context, and delegates
    to the agent processor. Returns the AgentResponse as a dict.

    Args:
        event: Lambda event containing token/headers and prompt.
        context: Lambda context object (unused).

    Returns:
        A dict representation of AgentResponse.
    """
    correlation_id = get_correlation_id(event)
    logger = configure_logging(correlation_id=correlation_id)

    logger.info("Agent handler invoked")

    # Extract JWT token
    token = _extract_token(event)
    if not token:
        logger.warning("Missing JWT token in request")
        return asdict(format_unauthorized_response("Missing authentication token"))

    # Validate JWT and extract username
    try:
        claims = validate_token(token)
        username = extract_username(claims)
    except JWTValidationError as e:
        logger.warning("JWT validation failed: %s", e)
        return asdict(format_unauthorized_response(str(e)))

    # Build request and process
    user_context = UserContext(username=username, token=token)
    prompt = event.get("prompt", "")

    # Also check nested body.prompt (from test script payloads)
    if not prompt:
        body = event.get("body", {})
        if isinstance(body, dict):
            prompt = body.get("prompt", "")
        elif isinstance(body, str):
            try:
                body = json.loads(body)
                prompt = body.get("prompt", "")
            except (json.JSONDecodeError, AttributeError):
                pass

    if not prompt:
        logger.warning("Empty prompt received from user: %s", username)
        return asdict(format_unauthorized_response("Missing prompt"))

    request = AgentRequest(prompt=prompt, user_context=user_context)

    try:
        response = process_request(request)
        return asdict(response)
    except Exception as e:
        logger.error("Unexpected error processing request: %s", e)
        return asdict(format_internal_error_response("Unexpected error", exception=e))
