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
    """Fetch and cache JWKS keys.
    
    Args:
        jwks_url: Cognito JWKS URL
        cache_time: Cache timestamp for TTL management
        
    Returns:
        Tuple of (jwks, cache_time)
    """
    response = requests.get(jwks_url, timeout=5)
    response.raise_for_status()
    jwks = response.json()
    return jwks, cache_time


def get_jwks(jwks_url: str, ttl: int = 3600) -> dict:
    """Get JWKS with caching and TTL.
    
    Args:
        jwks_url: Cognito JWKS URL
        ttl: Time-to-live in seconds (default 1 hour)
        
    Returns:
        JWKS dictionary
    """
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
        # Fetch JWKS
        jwks = get_jwks(jwks_url)
        
        # Get token header
        unverified_header = jwt.get_unverified_header(token)
        kid = unverified_header.get('kid')
        
        if not kid:
            raise ValueError("Token missing 'kid' in header")
        
        # Find matching key
        key = next((k for k in jwks['keys'] if k['kid'] == kid), None)
        if not key:
            raise ValueError("Key not found in JWKS")
        
        # Construct public key using PyJWK
        public_key = PyJWK.from_dict(key).key
        
        # Validate token
        claims = jwt.decode(
            token,
            public_key,
            algorithms=['RS256'],
            options={'verify_exp': True}
        )
        
        # Verify token type (must be access token)
        if claims.get('token_use') != 'access':
            raise ValueError("Must use access token, not ID token")
        
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
    """Extract user context from JWT claims.
    
    Args:
        claims: Decoded JWT claims
        
    Returns:
        UserContext object
        
    Raises:
        ValueError: If required claims are missing
    """
    required_claims = ['sub', 'username', 'client_id']
    missing = [c for c in required_claims if c not in claims]
    
    if missing:
        raise ValueError(f"Missing required claims: {missing}")
    
    return UserContext(
        user_id=claims['sub'],
        username=claims['username'],
        client_id=claims['client_id']
    )


def decode_jwt_payload(token: str) -> dict:
    """Decode JWT payload without verification (for Interceptor use).
    
    This is used by the Gateway Request Interceptor to extract user claims
    without full validation, since the Gateway validates the token independently.
    
    Args:
        token: JWT token string
        
    Returns:
        Decoded JWT payload
        
    Raises:
        ValueError: If token is malformed
    """
    try:
        # Decode without verification
        claims = jwt.decode(token, options={"verify_signature": False})
        return claims
    except Exception as e:
        raise ValueError(f"Failed to decode JWT payload: {e}")
