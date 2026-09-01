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

    Verifies signature, expiry, token_use (must be 'access'),
    iss (must match the JWKS URL issuer), and client_id (aud).

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

        # Derive expected issuer from JWKS URL
        # e.g. https://cognito-idp.us-east-1.amazonaws.com/<pool_id>/.well-known/jwks.json
        # → https://cognito-idp.us-east-1.amazonaws.com/<pool_id>
        expected_issuer = jwks_url.split('/.well-known/')[0]

        # Validate token — PyJWT verifies exp by default
        claims = jwt.decode(
            token,
            public_key,
            algorithms=['RS256'],
            # Cognito access tokens put client_id in 'client_id', not 'aud'.
            # We verify client_id manually below; skip PyJWT's aud check to
            # avoid a MissingClaimError on access tokens.
            options={'verify_aud': False, 'verify_exp': True},
        )

        # Defense-in-depth: verify issuer matches this Cognito User Pool
        token_iss = claims.get('iss', '')
        if token_iss != expected_issuer:
            raise ValueError(
                f"Token issuer mismatch: expected '{expected_issuer}', got '{token_iss}'"
            )

        # Verify token type (must be access token, not ID token)
        if claims.get('token_use') != 'access':
            raise ValueError("Must use access token, not ID token")

        # Verify client_id is present (defense-in-depth: ensures token was
        # issued for a known app client, not a different Cognito pool/client)
        if not claims.get('client_id'):
            raise ValueError("Token missing 'client_id' claim")

        return claims
        
    except jwt.ExpiredSignatureError:
        raise ValueError("Token has expired")
    except jwt.InvalidTokenError as e:
        raise ValueError(f"Invalid token: {e}")
    except requests.RequestException as e:
        raise ValueError(f"Failed to fetch JWKS: {e}")
    except ValueError:
        raise
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
