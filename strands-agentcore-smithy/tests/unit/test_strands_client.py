"""Unit tests for the Strands client factory functions.

Tests MCP client creation and Bedrock model configuration.

Requirements: 5.3, 5.4
"""

import sys
from types import ModuleType
from unittest.mock import patch, MagicMock

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

from agent.strands_client import (
    create_mcp_client,
    create_bedrock_model,
    DEFAULT_MODEL_ID,
    DEFAULT_REGION,
)


class TestCreateMCPClient:
    """Tests for the MCP client factory."""

    @patch("agent.strands_client.MCPClient")
    def test_returns_mcp_client_instance(self, mock_mcp_cls):
        client = create_mcp_client("https://gw.example.com", "my-token")
        mock_mcp_cls.assert_called_once()
        assert client is mock_mcp_cls.return_value

    @patch("agent.strands_client.streamablehttp_client")
    @patch("agent.strands_client.MCPClient")
    def test_transport_factory_uses_bearer_token(self, mock_mcp_cls, mock_http):
        """The transport factory lambda should pass the Bearer token header."""
        create_mcp_client("https://gw.example.com", "tok-abc")

        # Extract the transport factory lambda passed to MCPClient
        transport_factory = mock_mcp_cls.call_args[0][0]
        transport_factory()

        mock_http.assert_called_once_with(
            "https://gw.example.com",
            headers={"Authorization": "Bearer tok-abc"},
        )

    @patch("agent.strands_client.streamablehttp_client")
    @patch("agent.strands_client.MCPClient")
    def test_different_urls_and_tokens(self, mock_mcp_cls, mock_http):
        """Verify URL and token are correctly threaded through."""
        create_mcp_client("https://other.example.com", "other-token")
        transport_factory = mock_mcp_cls.call_args[0][0]
        transport_factory()

        mock_http.assert_called_once_with(
            "https://other.example.com",
            headers={"Authorization": "Bearer other-token"},
        )


class TestCreateBedrockModel:
    """Tests for the Bedrock model factory."""

    @patch("agent.strands_client.BedrockModel")
    def test_default_model_and_region(self, mock_bedrock_cls):
        model = create_bedrock_model()
        mock_bedrock_cls.assert_called_once_with(
            model_id=DEFAULT_MODEL_ID,
            region_name=DEFAULT_REGION,
        )
        assert model is mock_bedrock_cls.return_value

    @patch("agent.strands_client.BedrockModel")
    def test_custom_model_id(self, mock_bedrock_cls):
        create_bedrock_model(model_id="custom-model")
        mock_bedrock_cls.assert_called_once_with(
            model_id="custom-model",
            region_name=DEFAULT_REGION,
        )

    @patch("agent.strands_client.BedrockModel")
    def test_custom_region(self, mock_bedrock_cls):
        create_bedrock_model(region_name="eu-west-1")
        mock_bedrock_cls.assert_called_once_with(
            model_id=DEFAULT_MODEL_ID,
            region_name="eu-west-1",
        )

    @patch("agent.strands_client.BedrockModel")
    def test_custom_model_and_region(self, mock_bedrock_cls):
        create_bedrock_model(model_id="my-model", region_name="ap-southeast-1")
        mock_bedrock_cls.assert_called_once_with(
            model_id="my-model",
            region_name="ap-southeast-1",
        )
