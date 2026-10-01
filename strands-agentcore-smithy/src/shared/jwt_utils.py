"""JWT validation utilities for Cognito token handling.

Target-type agnostic JWT validation that works with any AgentCore Gateway
target type. Accepts both access and ID tokens, disables audience verification
(gateway handles it via AllowedAudience), and extracts the cognito:username claim.
"""

import logging
from typing import Any, Dict

import jwt

logger = logging.getLogger(__name__)

# Valid token_use claim values accepted by the validator
VALID_TOKEN_USE_VALUES = {"access", "id"}


class JWTValidationError(Exception):
    """Raised when JWT validation fails."""
    pass


def validate_token(token: str, options: Dict[str, Any] | None = None) -> Dict[str, Any]:
    """Decode and validate a JWT token.

    Decodes the token without signature verification (gateway handles full
    verification via CUSTOM_JWT authorizer). Validates that the token_use
    claim is either 'access' or 'id'. Disables audience verification since
    the gateway validates audience via AllowedAudience.

    Args:
        token: The JWT token string to validate.
        options: Optional PyJWT decode options override.

    Returns:
        The decoded JWT claims dictionary.

    Raises:
        JWTValidationError: If the token is invalid, expired, or has an
            unsupported token_use claim.
    """
    if not token:
        raise JWTValidationError("Token is empty or missing")

    decode_options = options or {
        "verify_signature": False,
        "verify_aud": False,
        "verify_exp": True,
    }

    try:
        claims = jwt.decode(
            token,
            algorithms=["RS256"],
            options=decode_options,
        )
    except jwt.ExpiredSignatureError:
        logger.warning("JWT token has expired")
        raise JWTValidationError("Token has expired")
    except jwt.DecodeError as e:
        logger.warning("JWT decode error: %s", str(e))
        raise JWTValidationError(f"Invalid token: {e}")
    except jwt.InvalidTokenError as e:
        logger.warning("JWT validation error: %s", str(e))
        raise JWTValidationError(f"Token validation failed: {e}")

    # Validate token_use claim — accept both 'access' and 'id'
    token_use = claims.get("token_use")
    if token_use is not None and token_use not in VALID_TOKEN_USE_VALUES:
        raise JWTValidationError(
            f"Unsupported token_use: {token_use}. Must be one of: {VALID_TOKEN_USE_VALUES}"
        )

    return claims


def extract_username(claims: Dict[str, Any]) -> str:
    """Extract the username from JWT claims.

    Uses the 'cognito:username' claim, which is the correct claim for
    Cognito ID tokens. Does NOT fall back to 'username' or 'sub' claims.

    Args:
        claims: Decoded JWT claims dictionary.

    Returns:
        The username string from the cognito:username claim.

    Raises:
        JWTValidationError: If the cognito:username claim is missing.
    """
    username = claims.get("cognito:username")
    if not username:
        raise JWTValidationError("Missing 'cognito:username' claim in token")
    return username
