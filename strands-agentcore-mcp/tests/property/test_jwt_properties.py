"""Property-based tests for src/shared/jwt_utils.py.

# Feature: strands-agentcore-mcp, Property 1: JWT validation positive path
# Feature: strands-agentcore-mcp, Property 2: JWT validation negative path
"""

import time
from typing import Any, Dict
from unittest.mock import MagicMock

import jwt
import pytest
from hypothesis import HealthCheck, given, settings
from hypothesis import strategies as st

import src.shared.jwt_utils as jwt_utils_module
import src.agent.strands_client as strands_client_module
from src.shared.jwt_utils import JWTValidationError, extract_username, validate_token
from tests.property.conftest import TEST_ISSUER, _FIXED_KID, make_jwt


# ---------------------------------------------------------------------------
# Strategies
# ---------------------------------------------------------------------------

# Non-empty printable strings for cognito:username
username_strategy = st.text(
    alphabet=st.characters(
        whitelist_categories=("Lu", "Ll", "Nd"),
        whitelist_characters="-_.@",
    ),
    min_size=1,
    max_size=64,
)

# Valid token_use values
valid_token_use_strategy = st.sampled_from(["access", "id"])

# Invalid token_use values — anything not in {"access", "id"}
invalid_token_use_strategy = st.text(min_size=1, max_size=32).filter(
    lambda s: s not in ("access", "id")
)


def _future_exp() -> int:
    """Return an exp timestamp 1 hour in the future."""
    return int(time.time()) + 3600


# ---------------------------------------------------------------------------
# Shared helper: install the mock JWKS client into jwt_utils._JWKS_CLIENTS
# ---------------------------------------------------------------------------

def _install_mock_jwks_client(mock_jwks: dict) -> MagicMock:
    """Create and install a mock PyJWKClient for TEST_ISSUER.

    Returns the mock so callers can inspect call counts if needed.
    """
    mock_client = MagicMock()

    def _get_signing_key(token):
        header = jwt.get_unverified_header(token)
        kid = header.get("kid")
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
    jwt_utils_module._JWKS_CLIENTS[TEST_ISSUER] = mock_client
    return mock_client


# ---------------------------------------------------------------------------
# Property 1: JWT validation positive path
# Validates: Requirements 1.3, 1.4, 1.6
# ---------------------------------------------------------------------------

@settings(
    max_examples=100,
    suppress_health_check=[HealthCheck.function_scoped_fixture],
)
@given(
    username=username_strategy,
    token_use=valid_token_use_strategy,
)
def test_jwt_positive_path(username, token_use, rsa_private_key, mock_jwks):
    """Property 1: JWT validation positive path.

    For any valid claim set (token_use ∈ {access, id}, future exp,
    non-empty cognito:username), validate_token succeeds and the returned
    username matches the cognito:username claim.

    Validates: Requirements 1.3, 1.4, 1.6
    """
    _install_mock_jwks_client(mock_jwks)

    claims: Dict[str, Any] = {
        "cognito:username": username,
        "token_use": token_use,
        "exp": _future_exp(),
        "iss": TEST_ISSUER,
        "sub": "test-sub-id",
    }

    token = make_jwt(claims, key=rsa_private_key)

    # validate_token should succeed
    returned_claims = validate_token(token, issuer=TEST_ISSUER)

    # The returned username must equal the cognito:username claim
    extracted = extract_username(returned_claims)
    assert extracted == username, (
        f"Expected username={username!r}, got {extracted!r}"
    )

    # token_use must be preserved
    assert returned_claims.get("token_use") == token_use


# ---------------------------------------------------------------------------
# Property 2: JWT validation negative path
# Validates: Requirements 1.3, 1.4, 1.7
# ---------------------------------------------------------------------------

# --- 2a: Missing / empty token ---

@settings(
    max_examples=50,
    suppress_health_check=[HealthCheck.function_scoped_fixture],
)
@given(token=st.one_of(st.just(""), st.just("   ")))
def test_jwt_negative_missing_token(token, mock_jwks):
    """Property 2 (missing token): validate_token raises JWTValidationError.

    Validates: Requirements 1.3, 1.7
    """
    _install_mock_jwks_client(mock_jwks)

    with pytest.raises(JWTValidationError):
        validate_token(token.strip(), issuer=TEST_ISSUER)


# --- 2b: Expired token ---

@settings(
    max_examples=100,
    suppress_health_check=[HealthCheck.function_scoped_fixture],
)
@given(
    username=username_strategy,
    token_use=valid_token_use_strategy,
)
def test_jwt_negative_expired(username, token_use, rsa_private_key, mock_jwks):
    """Property 2 (expired exp): validate_token raises JWTValidationError.

    Validates: Requirements 1.3, 1.7
    """
    _install_mock_jwks_client(mock_jwks)

    claims: Dict[str, Any] = {
        "cognito:username": username,
        "token_use": token_use,
        "exp": int(time.time()) - 3600,  # 1 hour in the past
        "iss": TEST_ISSUER,
        "sub": "test-sub-id",
    }

    token = make_jwt(claims, key=rsa_private_key)

    with pytest.raises(JWTValidationError):
        validate_token(token, issuer=TEST_ISSUER)


# --- 2c: Bad signature (signed by a different key) ---

@settings(
    max_examples=100,
    suppress_health_check=[HealthCheck.function_scoped_fixture],
    deadline=None,  # RSA key generation per example can exceed the 200ms default
)
@given(
    username=username_strategy,
    token_use=valid_token_use_strategy,
)
def test_jwt_negative_bad_signature(username, token_use, rsa_private_key, mock_jwks):
    """Property 2 (bad signature): validate_token raises JWTValidationError.

    Validates: Requirements 1.3, 1.7
    """
    _install_mock_jwks_client(mock_jwks)

    claims: Dict[str, Any] = {
        "cognito:username": username,
        "token_use": token_use,
        "exp": _future_exp(),
        "iss": TEST_ISSUER,
        "sub": "test-sub-id",
    }

    # Sign with a different key — signature will not match the mock JWKS
    token = make_jwt(claims, key=rsa_private_key, bad_signature=True)

    with pytest.raises(JWTValidationError):
        validate_token(token, issuer=TEST_ISSUER)


# --- 2d: Invalid token_use ---

@settings(
    max_examples=100,
    suppress_health_check=[HealthCheck.function_scoped_fixture],
)
@given(
    username=username_strategy,
    token_use=invalid_token_use_strategy,
)
def test_jwt_negative_invalid_token_use(
    username, token_use, rsa_private_key, mock_jwks
):
    """Property 2 (invalid token_use): validate_token raises JWTValidationError.

    Validates: Requirements 1.4, 1.7
    """
    _install_mock_jwks_client(mock_jwks)

    claims: Dict[str, Any] = {
        "cognito:username": username,
        "token_use": token_use,
        "exp": _future_exp(),
        "iss": TEST_ISSUER,
        "sub": "test-sub-id",
    }

    token = make_jwt(claims, key=rsa_private_key)

    with pytest.raises(JWTValidationError):
        validate_token(token, issuer=TEST_ISSUER)


# ---------------------------------------------------------------------------
# Property 2 — no gateway call on auth failure
# Validates: Requirements 1.7
# ---------------------------------------------------------------------------

@settings(
    max_examples=50,
    suppress_health_check=[HealthCheck.function_scoped_fixture],
)
@given(token_use=valid_token_use_strategy)
def test_jwt_negative_no_gateway_call_on_auth_failure(
    token_use, rsa_private_key, mock_jwks, monkeypatch
):
    """Property 2 (no gateway call): when JWT validation fails, create_mcp_client
    is never called.

    Validates: Requirements 1.7
    """
    _install_mock_jwks_client(mock_jwks)

    mock_create = MagicMock()
    monkeypatch.setattr(strands_client_module, "create_mcp_client", mock_create)
    monkeypatch.setenv("COGNITO_ISSUER", TEST_ISSUER)

    # Use an expired token to trigger auth failure
    claims: Dict[str, Any] = {
        "cognito:username": "testuser",
        "token_use": token_use,
        "exp": int(time.time()) - 3600,
        "iss": TEST_ISSUER,
        "sub": "test-sub-id",
    }
    token = make_jwt(claims, key=rsa_private_key)

    from src.agent.handler import lambda_handler

    event = {"jwt": token, "prompt": "List all products."}
    response = lambda_handler(event, None)

    # Should be an auth error response
    assert response.get("success") is False
    assert response.get("error") is not None

    # create_mcp_client must never have been called
    mock_create.assert_not_called()
