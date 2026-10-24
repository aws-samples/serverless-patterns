"""Agent Lambda handler — entry point for AI agent requests.

Validates Cognito JWT, extracts user context, and delegates to
AgentProcessor which uses the Strands Agents SDK for orchestration.
"""

import os
import json
import uuid
from typing import Dict, Any

from shared.models import AgentRequest, AgentResponse, UserContext
from shared.jwt_utils import validate_jwt, extract_user_context
from shared.logging_utils import get_logger, StructuredLogger
from shared.error_utils import ErrorHandler

from .agent_processor import AgentProcessor


# Environment variables
COGNITO_JWKS_URL = os.environ.get("COGNITO_JWKS_URL", "")
GATEWAY_ID = os.environ.get("GATEWAY_ID", "")
BEDROCK_MODEL_ID = os.environ.get(
    "BEDROCK_MODEL_ID", "anthropic.claude-3-sonnet-20240229-v1:0"
)
AWS_REGION = os.environ.get("AWS_REGION", "us-east-1")
LOG_LEVEL = os.environ.get("LOG_LEVEL", "INFO")

base_logger = get_logger(__name__, LOG_LEVEL)


def lambda_handler(event: Dict[str, Any], context: Any) -> Dict[str, Any]:
    """Lambda entry point.

    1. Extract + validate JWT
    2. Parse prompt / session_id from body
    3. Run AgentProcessor (Strands SDK handles the agentic loop)
    4. Return AgentResponse
    """
    request_id = str(uuid.uuid4())
    logger = StructuredLogger(base_logger, request_id)

    try:
        # --- JWT extraction ---
        headers = event.get("headers", {})
        auth_header = headers.get("Authorization", "")

        if not auth_header or not auth_header.startswith("Bearer "):
            logger.warning("Missing or malformed Authorization header")
            return ErrorHandler.handle_authentication_error(
                ValueError("Missing or invalid Authorization header")
            )

        jwt_token = auth_header[len("Bearer "):].strip()
        if not jwt_token:
            logger.warning("Empty JWT token")
            return ErrorHandler.handle_authentication_error(
                ValueError("Empty JWT token")
            )

        # --- JWT validation ---
        try:
            claims = validate_jwt(jwt_token, COGNITO_JWKS_URL)
            logger.info("JWT validated")
        except ValueError as e:
            logger.warning("JWT validation failed", error=str(e))
            return ErrorHandler.handle_authentication_error(e)

        # --- User context ---
        try:
            user_context = extract_user_context(claims)
            logger.info("User context extracted", user_id=user_context.user_id)
        except ValueError as e:
            logger.error("User context extraction failed", error=str(e))
            return ErrorHandler.handle_validation_error(e)

        logger.user_context = user_context

        # --- Request body ---
        body_str = event.get("body", "{}")
        try:
            body = json.loads(body_str) if isinstance(body_str, str) else body_str
        except json.JSONDecodeError:
            return ErrorHandler.handle_validation_error(
                ValueError("Invalid JSON in request body")
            )

        prompt = body.get("prompt")
        if not prompt:
            return ErrorHandler.handle_missing_parameter_error("prompt")

        session_id = body.get("session_id")

        logger.info(
            "Agent request received",
            prompt_length=len(prompt),
            has_session_id=bool(session_id),
        )

        # --- Agent processing (Strands SDK) ---
        processor = AgentProcessor(
            gateway_id=GATEWAY_ID,
            model_id=BEDROCK_MODEL_ID,
            region=AWS_REGION,
            logger=logger,
        )

        try:
            response_text, final_session_id = processor.process_request(
                prompt=prompt,
                jwt_token=jwt_token,
                session_id=session_id,
            )
        except Exception as e:
            logger.error(
                "Agent processing failed",
                error_type=type(e).__name__,
                error_message=str(e),
            )
            return ErrorHandler.handle_generic_error(e)

        # --- Response ---
        agent_response = AgentResponse(
            response=response_text,
            session_id=final_session_id,
            user_context=user_context,
        )

        logger.info(
            "Agent request completed",
            session_id=final_session_id,
            response_length=len(response_text),
        )

        return agent_response.to_lambda_response()

    except Exception as e:
        logger.error(
            "Unexpected error",
            error_type=type(e).__name__,
            error_message=str(e),
        )
        return ErrorHandler.handle_generic_error(e)
