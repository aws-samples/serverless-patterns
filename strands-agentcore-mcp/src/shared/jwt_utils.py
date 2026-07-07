"""JWT validation utilities for Cognito token handling.

Target-type agnostic JWT validation that works with any AgentCore Gateway
target type. Verifies signatures via JWKS fetched from the Cognito User Pool
issuer, accepts both access and ID tokens, disables audience verification
(gateway handles it via AllowedAudience), and extracts the cognito:username
claim.

Mandatory rules (see .kiro/steering/project-conventions.md):
    - Accept both token_use: access AND token_use: id
    - Pass verify_aud=False to jwt.decode (Gateway enforces audience)
    - Extract username from the cognito:username claim (NOT username, NOT sub)
"""

import logging
from typing import Any, Dict, Optional

import jwt
from jwt import PyJWKClient

logger = logging.getLogger(__name__)

# Valid token_use claim values accepted by the validator
VALID_TOKEN_USE_VALUES = {"access", "id"}

# Module-level JWKS client cache keyed by issuer URL so we avoid re-fetching
# the JWKS document on every invocation within a warm Lambda container.
_JWKS_CLIENTS: Dict[str, PyJWKClient] = {}


class JWTValidationError(Exception):
    """Raised when JWT validation fails."""
    pass


def _get_jwks_client(issuer: str) -> PyJWKClient:
    """Return a cached PyJWKClient for the given issuer.

    The JWKS URL is derived from the Cognito User Pool issuer as
    ``{issuer}/.well-known/jwks.json``.
    """
    client = _JWKS_CLIENTS.get(issuer)
    if client is None:
        jwks_url = f"{issuer.rstrip('/')}/.well-known/jwks.json"
        logger.info("Creating PyJWKClient for JWKS URL: %s", jwks_url)
        client = PyJWKClient(jwks_url)
        _JWKS_CLIENTS[issuer] = client
    return client


def validate_token(
    token: str,
    issuer: Optional[str] = None,
    options: Optional[Dict[str, Any]] = None,
) -> Dict[str, Any]:
    """Decode and validate a JWT token.

    Verifies the token's signature against the Cognito User Pool JWKS when an
    issuer is provided. Always disables audience verification — the AgentCore
    Gateway's CUSTOM_JWT authorizer enforces audience via AllowedAudience.
    Requires the token_use claim to be either 'access' or 'id'.

    Args:
        token: The JWT token string to validate.
        issuer: Optional Cognito User Pool issuer URL (e.g.
            ``https://cognito-idp.us-east-1.amazonaws.com/<pool-id>``). When
            provided, the signature is verified via JWKS. When omitted,
            signature verification is skipped (useful for unit tests).
        options: Optional PyJWT decode options override.

    Returns:
        The decoded JWT claims dictionary.

    Raises:
        JWTValidationError: If the token is invalid, expired, signature
            verification fails, or the token_use claim is unsupported.
    """
    if not token:
        raise JWTValidationError("Token is empty or missing")

    try:
        if issuer:
            jwks_client = _get_jwks_client(issuer)
            signing_key = jwks_client.get_signing_key_from_jwt(token).key
            decode_options = options or {"verify_aud": False}
            claims = jwt.decode(
                token,
                signing_key,
                algorithms=["RS256"],
                options=decode_options,
            )
        else:
            # No issuer: decode without signature verification. Audience
            # verification is still disabled — the Gateway handles audience
            # via AllowedAudience.
            decode_options = options or {
                "verify_signature": False,
                "verify_aud": False,
                "verify_exp": True,
            }
            claims = jwt.decode(
                token,
                algorithms=["RS256"],
                options=decode_options,
            )
    except jwt.ExpiredSignatureError:
        logger.warning("JWT token has expired")
        raise JWTValidationError("Token has expired")
    except jwt.InvalidSignatureError as e:
        logger.warning("JWT signature invalid: %s", e)
        raise JWTValidationError(f"Invalid token signature: {e}")
    except jwt.DecodeError as e:
        logger.warning("JWT decode error: %s", str(e))
        raise JWTValidationError(f"Invalid token: {e}")
    except jwt.InvalidTokenError as e:
        logger.warning("JWT validation error: %s", str(e))
        raise JWTValidationError(f"Token validation failed: {e}")
    except Exception as e:  # PyJWKClient can raise its own errors
        logger.warning("JWT validation failed: %s", e)
        raise JWTValidationError(f"Token validation failed: {e}")

    # Validate token_use claim — accept both 'access' and 'id'
    token_use = claims.get("token_use")
    if token_use is not None and token_use not in VALID_TOKEN_USE_VALUES:
        raise JWTValidationError(
            f"Unsupported token_use: {token_use}. "
            f"Must be one of: {VALID_TOKEN_USE_VALUES}"
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
