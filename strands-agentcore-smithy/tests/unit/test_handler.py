"""Unit tests for the agent Lambda handler.

Tests JWT extraction from events, validation error responses,
missing prompt handling, and successful delegation to agent_processor.

Requirements: 5.1, 5.5, 5.6
"""

import sys
from types import ModuleType
from unittest.mock import patch, MagicMock

import pytest

# Mock third-party modules not installed in test env
_strands_mod = ModuleType("strands")
_strands_mod.Agent = MagicMock()
_mcp_mod = ModuleType("mcp")
_mcp_client_mod = ModuleType("mcp.client")
_mcp_http_mod = ModuleType("mcp.client.streamable_http")
_mcp_http_mod.streamablehttp_client = MagicMock()
_bedrock_mod = ModuleType("strands.models")
_bedrock_bedrock_mod = ModuleType("strands.models.bedrock")
_bedrock_bedrock_mod.BedrockModel = MagicMock()
_strands_tools_mod = ModuleType("strands.tools")
_strands_tools_mcp_mod = ModuleType("strands.tools.mcp")
_strands_tools_mcp_mod.MCPClient = MagicMock()

sys.modules.setdefault("strands", _strands_mod)
sys.modules.setdefault("strands.models", _bedrock_mod)
sys.modules.setdefault("strands.models.bedrock", _bedrock_bedrock_mod)
sys.modules.setdefault("strands.tools", _strands_tools_mod)
sys.modules.setdefault("strands.tools.mcp", _strands_tools_mcp_mod)
sys.modules.setdefault("mcp", _mcp_mod)
sys.modules.setdefault("mcp.client", _mcp_client_mod)
sys.modules.setdefault("mcp.client.streamable_http", _mcp_http_mod)

from agent.handler import lambda_handler, _extract_token
from shared.models import AgentResponse


# --- _extract_token ---

class TestExtractToken:
    def test_extracts_direct_token(self):
        event = {"token": "my-jwt"}
        assert _extract_token(event) == "my-jwt"

    def test_extracts_bearer_token_from_headers(self):
        event = {"headers": {"Authorization": "Bearer abc123"}}
        assert _extract_token(event) == "abc123"

    def test_direct_token_takes_precedence_over_header(self):
        event = {"token": "direct", "headers": {"Authorization": "Bearer header"}}
        assert _extract_token(event) == "direct"

    def test_returns_raw_auth_header_if_not_bearer(self):
        event = {"headers": {"Authorization": "Basic creds"}}
        assert _extract_token(event) == "Basic creds"

    def test_returns_none_when_no_token(self):
        assert _extract_token({}) is None

    def test_returns_none_for_empty_auth_header(self):
        event = {"headers": {"Authorization": ""}}
        assert _extract_token(event) is None

    def test_returns_none_for_missing_headers(self):
        event = {"headers": {}}
        assert _extract_token(event) is None


# --- lambda_handler ---

class TestLambdaHandler:
    """Tests for the Lambda entry point."""

    def test_missing_token_returns_unauthorized(self):
        result = lambda_handler({}, None)
        assert result["success"] is False
        assert "authentication" in result["error"].lower() or "token" in result["error"].lower()

    @patch("agent.handler.validate_token")
    def test_invalid_jwt_returns_unauthorized(self, mock_validate):
        from src.shared.jwt_utils import JWTValidationError
        mock_validate.side_effect = JWTValidationError("Token expired")

        result = lambda_handler({"token": "bad-jwt"}, None)
        assert result["success"] is False
        assert "expired" in result["error"].lower()

    @patch("agent.handler.extract_username")
    @patch("agent.handler.validate_token")
    def test_missing_prompt_returns_error(self, mock_validate, mock_extract):
        mock_validate.return_value = {"cognito:username": "alice"}
        mock_extract.return_value = "alice"

        result = lambda_handler({"token": "valid-jwt"}, None)
        assert result["success"] is False
        assert "prompt" in result["error"].lower()

    @patch("agent.handler.process_request")
    @patch("agent.handler.extract_username")
    @patch("agent.handler.validate_token")
    def test_successful_request(self, mock_validate, mock_extract, mock_process):
        mock_validate.return_value = {"cognito:username": "alice"}
        mock_extract.return_value = "alice"
        mock_process.return_value = AgentResponse(success=True, response="done")

        result = lambda_handler({"token": "jwt", "prompt": "hello"}, None)
        assert result["success"] is True
        assert result["response"] == "done"
        assert result["error"] is None

        # Verify process_request was called with correct AgentRequest
        call_args = mock_process.call_args[0][0]
        assert call_args.prompt == "hello"
        assert call_args.user_context.username == "alice"
        assert call_args.user_context.token == "jwt"

    @patch("agent.handler.process_request")
    @patch("agent.handler.extract_username")
    @patch("agent.handler.validate_token")
    def test_processor_exception_returns_internal_error(self, mock_validate, mock_extract, mock_process):
        mock_validate.return_value = {"cognito:username": "alice"}
        mock_extract.return_value = "alice"
        mock_process.side_effect = RuntimeError("boom")

        result = lambda_handler({"token": "jwt", "prompt": "hello"}, None)
        assert result["success"] is False
        assert result["error"] is not None
