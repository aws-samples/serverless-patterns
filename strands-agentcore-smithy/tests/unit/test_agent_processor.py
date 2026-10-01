"""Unit tests for the agent processor module.

Tests MCP session lifecycle (try/finally), gateway URL resolution,
and error handling during agent invocation.

Requirements: 5.4, 5.5
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

from shared.models import UserContext, AgentRequest


def _make_request(prompt="test prompt", username="alice", token="jwt-tok"):
    ctx = UserContext(username=username, token=token)
    return AgentRequest(prompt=prompt, user_context=ctx)


class TestProcessRequest:
    """Tests for process_request function."""

    @patch("agent.agent_processor.Agent")
    @patch("agent.agent_processor.create_bedrock_model")
    @patch("agent.agent_processor.create_mcp_client")
    def test_successful_invocation(self, mock_mcp, mock_model, mock_agent_cls):
        agent_instance = MagicMock()
        agent_instance.return_value = "Agent says hello"
        mock_agent_cls.return_value = agent_instance
        mock_mcp_client = MagicMock()
        mock_mcp.return_value = mock_mcp_client

        from agent.agent_processor import process_request
        result = process_request(_make_request(), gateway_url="https://gw.example.com")

        assert result.success is True
        assert result.response == "Agent says hello"
        mock_mcp.assert_called_once_with("https://gw.example.com", "jwt-tok")
        mock_mcp_client.cleanup.assert_called_once()

    @patch("agent.agent_processor.Agent")
    @patch("agent.agent_processor.create_bedrock_model")
    @patch("agent.agent_processor.create_mcp_client")
    def test_cleanup_called_on_agent_exception(self, mock_mcp, mock_model, mock_agent_cls):
        """Verify MCP client cleanup happens even when the agent raises."""
        agent_instance = MagicMock()
        agent_instance.side_effect = RuntimeError("LLM failed")
        mock_agent_cls.return_value = agent_instance
        mock_mcp_client = MagicMock()
        mock_mcp.return_value = mock_mcp_client

        from agent.agent_processor import process_request
        result = process_request(_make_request(), gateway_url="https://gw.example.com")

        assert result.success is False
        assert result.error is not None
        # The critical assertion: cleanup MUST be called even on failure
        mock_mcp_client.cleanup.assert_called_once()

    @patch("agent.agent_processor.Agent")
    @patch("agent.agent_processor.create_bedrock_model")
    @patch("agent.agent_processor.create_mcp_client")
    def test_cleanup_called_on_model_creation_exception(self, mock_mcp, mock_model, mock_agent_cls):
        """Verify cleanup even if create_bedrock_model raises."""
        mock_model.side_effect = RuntimeError("Bedrock config error")
        mock_mcp_client = MagicMock()
        mock_mcp.return_value = mock_mcp_client

        from agent.agent_processor import process_request
        result = process_request(_make_request(), gateway_url="https://gw.example.com")

        assert result.success is False
        mock_mcp_client.cleanup.assert_called_once()

    def test_missing_gateway_url_returns_error(self):
        """When no gateway URL is provided and env var is unset, return error."""
        from agent.agent_processor import process_request
        with patch.dict("os.environ", {}, clear=True):
            result = process_request(_make_request())

        assert result.success is False
        assert "gateway" in result.error.lower()

    @patch("agent.agent_processor.Agent")
    @patch("agent.agent_processor.create_bedrock_model")
    @patch("agent.agent_processor.create_mcp_client")
    def test_reads_gateway_url_from_env(self, mock_mcp, mock_model, mock_agent_cls):
        """Falls back to GATEWAY_URL env var when no explicit URL given."""
        agent_instance = MagicMock()
        agent_instance.return_value = "ok"
        mock_agent_cls.return_value = agent_instance
        mock_mcp_client = MagicMock()
        mock_mcp.return_value = mock_mcp_client

        from agent.agent_processor import process_request
        with patch.dict("os.environ", {"GATEWAY_URL": "https://env-gw.example.com"}):
            result = process_request(_make_request())

        assert result.success is True
        mock_mcp.assert_called_once_with("https://env-gw.example.com", "jwt-tok")
        mock_mcp_client.cleanup.assert_called_once()

    @patch("agent.agent_processor.Agent")
    @patch("agent.agent_processor.create_bedrock_model")
    @patch("agent.agent_processor.create_mcp_client")
    def test_explicit_url_overrides_env(self, mock_mcp, mock_model, mock_agent_cls):
        agent_instance = MagicMock()
        agent_instance.return_value = "ok"
        mock_agent_cls.return_value = agent_instance
        mock_mcp_client = MagicMock()
        mock_mcp.return_value = mock_mcp_client

        from agent.agent_processor import process_request
        with patch.dict("os.environ", {"GATEWAY_URL": "https://env-gw.example.com"}):
            result = process_request(_make_request(), gateway_url="https://explicit.example.com")

        mock_mcp.assert_called_once_with("https://explicit.example.com", "jwt-tok")
