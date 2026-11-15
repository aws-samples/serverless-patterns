"""JWT validation and user context extraction utilities."""

import json
import time
from typing import Dict, Optional
from functools import lru_cache

import jwt
import requests
from jwt import PyJWK

from .models import UserContext


@lru_cache(maxsize=1)
def _get_jwks_with_cache(jwks_url: str, cache_time: int) -> tuple:
    """Fetch and cache JWKS keys."""
    response = requests.get(jwks_url, timeout=5)
    response.raise_for_status()
    jwks = response.json()
    return jwks, cache_time


def get_jwks(jwks_url: str, ttl: int = 3600) -> dict:
    """Get JWKS with caching and TTL."""
    current_time = int(time.time())
    cache_time = current_time - (current_time % ttl)
    jwks, _ = _get_jwks_with_cache(jwks_url, cache_time)
    return jwks


def validate_jwt(token: str, jwks_url: str) -> dict:
    """Validate JWT token using JWKS from Cognito.

    Args:
        token: JWT access token
        jwks_url: Cognito JWKS URL

    Returns:
        Decoded JWT claims

    Raises:
        ValueError: If token is invalid, expired, or malformed
    """
    try:
        jwks = get_jwks(jwks_url)
        unverified_header = jwt.get_unverified_header(token)
        kid = unverified_header.get('kid')

        if not kid:
            raise ValueError("Token missing 'kid' in header")

        key = next((k for k in jwks['keys'] if k['kid'] == kid), None)
        if not key:
            raise ValueError("Key not found in JWKS")

        public_key = PyJWK.from_dict(key).key

        claims = jwt.decode(
            token,
            public_key,
            algorithms=['RS256'],
            options={'verify_exp': True, 'verify_aud': False}
        )

        token_use = claims.get('token_use')
        if token_use not in ('access', 'id'):
            raise ValueError("Token must be an access or ID token")

        return claims

    except jwt.ExpiredSignatureError:
        raise ValueError("Token has expired")
    except jwt.InvalidTokenError as e:
        raise ValueError(f"Invalid token: {e}")
    except requests.RequestException as e:
        raise ValueError(f"Failed to fetch JWKS: {e}")
    except Exception as e:
        raise ValueError(f"Token validation failed: {e}")


def extract_user_context(claims: dict) -> UserContext:
    """Extract user context from JWT claims (supports both access and ID tokens)."""
    sub = claims.get('sub')
    if not sub:
        raise ValueError("Missing required claim: sub")

    username = claims.get('username') or claims.get('cognito:username', '')
    client_id = claims.get('client_id') or claims.get('aud', '')

    return UserContext(
        user_id=sub,
        username=username,
        client_id=client_id,
    )


def decode_jwt_payload(token: str) -> dict:
    """Decode JWT payload without verification (for Interceptor use)."""
    try:
        claims = jwt.decode(token, options={"verify_signature": False})
        return claims
    except Exception as e:
        raise ValueError(f"Failed to decode JWT payload: {e}")
