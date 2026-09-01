"""Property-based tests for JWT validation (Properties 4 and 5).

Feature: agentcore-smithy-bedrock
Property 4: JWT validation accepts both token_use values
  Validates: Requirements 4.4
Property 5: Username extraction from cognito:username claim
  Validates: Requirements 4.6
"""

import time

import jwt
import pytest
from hypothesis import given, settings, assume
from hypothesis import strategies as st

from shared.jwt_utils import validate_token, extract_username, JWTValidationError


# ---------------------------------------------------------------------------
# Strategies
# ---------------------------------------------------------------------------

# Printable text that won't be empty, for usernames
username_st = st.text(
    alphabet=st.characters(whitelist_categories=("L", "N", "P")),
    min_size=1,
    max_size=64,
).filter(lambda s: s.strip() != "")

token_use_st = st.sampled_from(["access", "id"])


def _encode(claims: dict, exp_offset: int = 3600) -> str:
    """Encode a JWT with HS256 for testing (no signature verification)."""
    payload = {
        "iat": int(time.time()),
        "exp": int(time.time()) + exp_offset,
        **claims,
    }
    return jwt.encode(payload, "test-secret", algorithm="HS256")


# ---------------------------------------------------------------------------
# Property 4: JWT validation accepts both token_use values
# Tag: Feature: agentcore-smithy-bedrock, Property 4: JWT validation accepts
#      both token_use values
# ---------------------------------------------------------------------------


@given(token_use=token_use_st)
@settings(max_examples=100)
def test_property4_validate_token_accepts_access_and_id(token_use):
    """For any valid JWT with token_use set to 'access' or 'id',
    validate_token shall accept the token without raising an error."""
    token = _encode({"token_use": token_use, "cognito:username": "testuser"})
    claims = validate_token(token)
    assert claims["token_use"] == token_use


@given(
    token_use=token_use_st,
    extra_claims=st.fixed_dictionaries(
        {},
        optional={
            "sub": st.uuids().map(str),
            "email": st.emails(),
            "custom:role": st.sampled_from(["admin", "user", "viewer"]),
        },
    ),
)
@settings(max_examples=100)
def test_property4_validate_token_with_extra_claims(token_use, extra_claims):
    """Acceptance of token_use holds regardless of other claims present."""
    all_claims = {
        "token_use": token_use,
        "cognito:username": "anyuser",
        **extra_claims,
    }
    token = _encode(all_claims)
    claims = validate_token(token)
    assert claims["token_use"] == token_use


# ---------------------------------------------------------------------------
# Property 5: Username extraction from cognito:username claim
# Tag: Feature: agentcore-smithy-bedrock, Property 5: Username extraction
#      from cognito:username claim
# ---------------------------------------------------------------------------


@given(cognito_username=username_st)
@settings(max_examples=100)
def test_property5_extracts_cognito_username(cognito_username):
    """For any JWT containing a cognito:username claim, extract_username
    shall return that claim's value."""
    claims = {"cognito:username": cognito_username}
    assert extract_username(claims) == cognito_username


@given(
    cognito_username=username_st,
    other_username=username_st,
    sub_value=st.uuids().map(str),
)
@settings(max_examples=100)
def test_property5_cognito_username_preferred_over_others(
    cognito_username, other_username, sub_value
):
    """extract_username returns cognito:username even when 'username' and
    'sub' claims are also present with different values."""
    assume(cognito_username != other_username)
    claims = {
        "cognito:username": cognito_username,
        "username": other_username,
        "sub": sub_value,
    }
    result = extract_username(claims)
    assert result == cognito_username
    assert result != other_username
