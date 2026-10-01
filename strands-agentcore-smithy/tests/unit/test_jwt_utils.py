"""Unit tests for JWT validation edge cases.

Requirements: 4.4, 4.5, 4.6
"""

import time

import jwt as pyjwt
import pytest

from shared.jwt_utils import validate_token, extract_username, JWTValidationError


def _encode(claims: dict, exp_offset: int = 3600) -> str:
    payload = {
        "iat": int(time.time()),
        "exp": int(time.time()) + exp_offset,
        **claims,
    }
    return pyjwt.encode(payload, "test-secret", algorithm="HS256")


# --- validate_token ---

class TestValidateToken:
    def test_accepts_token_use_access(self):
        token = _encode({"token_use": "access"})
        claims = validate_token(token)
        assert claims["token_use"] == "access"

    def test_accepts_token_use_id(self):
        token = _encode({"token_use": "id"})
        claims = validate_token(token)
        assert claims["token_use"] == "id"

    def test_accepts_missing_token_use(self):
        """Tokens without token_use claim should still be accepted."""
        token = _encode({"sub": "user1"})
        claims = validate_token(token)
        assert "token_use" not in claims

    def test_rejects_invalid_token_use(self):
        token = _encode({"token_use": "refresh"})
        with pytest.raises(JWTValidationError, match="Unsupported token_use"):
            validate_token(token)

    def test_rejects_empty_token(self):
        with pytest.raises(JWTValidationError, match="empty or missing"):
            validate_token("")

    def test_rejects_none_like_empty(self):
        with pytest.raises(JWTValidationError):
            validate_token("")

    def test_rejects_malformed_token(self):
        with pytest.raises(JWTValidationError, match="Invalid token"):
            validate_token("not.a.jwt.at.all")

    def test_rejects_expired_token(self):
        token = _encode({"token_use": "id"}, exp_offset=-10)
        with pytest.raises(JWTValidationError, match="expired"):
            validate_token(token)

    def test_verify_aud_disabled_by_default(self):
        """Tokens with an aud claim should not fail since verify_aud is False."""
        token = _encode({"token_use": "id", "aud": "some-client-id"})
        claims = validate_token(token)
        assert claims["aud"] == "some-client-id"


# --- extract_username ---

class TestExtractUsername:
    def test_extracts_cognito_username(self):
        claims = {"cognito:username": "alice"}
        assert extract_username(claims) == "alice"

    def test_ignores_username_claim(self):
        claims = {"cognito:username": "alice", "username": "bob"}
        assert extract_username(claims) == "alice"

    def test_ignores_sub_claim(self):
        claims = {"cognito:username": "alice", "sub": "sub-123"}
        assert extract_username(claims) == "alice"

    def test_raises_when_cognito_username_missing(self):
        claims = {"username": "bob", "sub": "sub-123"}
        with pytest.raises(JWTValidationError, match="cognito:username"):
            extract_username(claims)

    def test_raises_on_empty_claims(self):
        with pytest.raises(JWTValidationError, match="cognito:username"):
            extract_username({})

    def test_raises_on_empty_string_cognito_username(self):
        claims = {"cognito:username": ""}
        with pytest.raises(JWTValidationError, match="cognito:username"):
            extract_username(claims)
