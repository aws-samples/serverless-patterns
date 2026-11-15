"""Shared fixtures and helpers for JWT property-based tests.

Provides a session-scoped RSA keypair, a JWKS mock fixture, and a
make_jwt() helper that signs tokens with the test key.
"""

import time
from typing import Any, Dict, Optional

import jwt
import pytest
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import rsa


# ---------------------------------------------------------------------------
# Session-scoped RSA keypair
# ---------------------------------------------------------------------------

@pytest.fixture(scope="session")
def rsa_private_key():
    """Generate a 2048-bit RSA private key once per test session."""
    return rsa.generate_private_key(
        public_exponent=65537,
        key_size=2048,
    )


@pytest.fixture(scope="session")
def rsa_public_key(rsa_private_key):
    """Return the public key counterpart of the session RSA key."""
    return rsa_private_key.public_key()


# ---------------------------------------------------------------------------
# Alternative RSA key (for bad-signature tests)
# ---------------------------------------------------------------------------

@pytest.fixture(scope="session")
def rsa_other_private_key():
    """A second RSA key used to produce tokens with invalid signatures."""
    return rsa.generate_private_key(
        public_exponent=65537,
        key_size=2048,
    )


# ---------------------------------------------------------------------------
# JWKS mock document
# ---------------------------------------------------------------------------

_FIXED_KID = "test-key-id"


@pytest.fixture(scope="session")
def mock_jwks(rsa_public_key):
    """Return a minimal JWKS document exposing the test public key."""
    from jwt.algorithms import RSAAlgorithm
    import json

    jwk_dict = json.loads(RSAAlgorithm.to_jwk(rsa_public_key))
    jwk_dict["kid"] = _FIXED_KID
    jwk_dict["use"] = "sig"
    return {"keys": [jwk_dict]}


# ---------------------------------------------------------------------------
# make_jwt helper
# ---------------------------------------------------------------------------

def make_jwt(
    claims: Dict[str, Any],
    *,
    key,
    kid: str = _FIXED_KID,
    expired: bool = False,
    bad_signature: bool = False,
    alg: str = "RS256",
) -> str:
    """Encode a JWT with the given claims and signing key.

    Args:
        claims: Base claims dict (will be shallow-copied before modification).
        key: RSA private key to sign with.
        kid: Key ID to embed in the JWT header.
        expired: If True, force ``exp`` to a past timestamp.
        bad_signature: If True, sign with a freshly generated throwaway key
            so the signature will not match the test JWKS.
        alg: JWT algorithm (default RS256).

    Returns:
        Encoded JWT string.
    """
    payload = dict(claims)

    if expired:
        payload["exp"] = int(time.time()) - 3600  # 1 hour in the past

    signing_key = key
    if bad_signature:
        signing_key = rsa.generate_private_key(
            public_exponent=65537,
            key_size=2048,
        )

    private_pem = signing_key.private_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PrivateFormat.TraditionalOpenSSL,
        encryption_algorithm=serialization.NoEncryption(),
    )

    return jwt.encode(
        payload,
        private_pem,
        algorithm=alg,
        headers={"kid": kid},
    )


# ---------------------------------------------------------------------------
# Fixture that patches jwt_utils._JWKS_CLIENTS to use the mock JWKS
# ---------------------------------------------------------------------------

TEST_ISSUER = "https://cognito-idp.us-east-1.amazonaws.com/us-east-1_TESTPOOL"


@pytest.fixture()
def patched_jwks_client(mock_jwks, monkeypatch):
    """Patch src.shared.jwt_utils._JWKS_CLIENTS with a mock PyJWKClient.

    The mock client's get_signing_key_from_jwt() returns the test public key
    for any token whose header contains the fixed kid.
    """
    from unittest.mock import MagicMock
    import src.shared.jwt_utils as jwt_utils_module

    mock_client = MagicMock()

    def _get_signing_key(token):
        # Parse the kid from the token header
        header = jwt.get_unverified_header(token)
        kid = header.get("kid")
        # Find the matching key in the mock JWKS
        for key_data in mock_jwks["keys"]:
            if key_data.get("kid") == kid:
                from jwt.algorithms import RSAAlgorithm
                import json
                public_key = RSAAlgorithm.from_jwk(json.dumps(key_data))
                result = MagicMock()
                result.key = public_key
                return result
        raise jwt.exceptions.PyJWKClientError(f"No key found for kid={kid}")

    mock_client.get_signing_key_from_jwt.side_effect = _get_signing_key

    monkeypatch.setitem(jwt_utils_module._JWKS_CLIENTS, TEST_ISSUER, mock_client)
    return mock_client
