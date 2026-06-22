"""Property-based tests for strands_client.py factory functions."""

import sys
from unittest.mock import MagicMock, patch

from hypothesis import given, settings, strategies as st

# Mock external SDK modules before importing strands_client
# These packages may not be installed in the test environment
_mock_modules = {}
for mod_name in [
    "mcp", "mcp.client", "mcp.client.streamable_http",
    "strands", "strands.models", "strands.models.bedrock",
    "strands.tools", "strands.tools.mcp",
]:
    if mod_name not in sys.modules:
        _mock_modules[mod_name] = MagicMock()
        sys.modules[mod_name] = _mock_modules[mod_name]

from src.agent.strands_client import SYSTEM_PROMPT, create_agent, create_mcp_client  # noqa: E402


@settings(max_examples=100)
@given(
    model_id=st.text(min_size=1, max_size=100),
    region=st.text(min_size=1, max_size=30),
    system_prompt=st.one_of(st.none(), st.text(min_size=1, max_size=500)),
)
def test_create_agent_wiring(model_id: str, region: str, system_prompt: str | None) -> None:
    """Property 1: Agent factory wiring.

    For any valid model_id, region, mock MCPClient, and optional system_prompt,
    create_agent returns an Agent with correctly configured BedrockModel
    (model_id, region_name, max_tokens=4096), the MCPClient in tool sources,
    and the correct system prompt (provided value or SYSTEM_PROMPT default).

    **Validates: Requirements 1.1, 1.2, 1.3**
    """
    # Feature: strands-sdk-migration, Property 1: Agent factory wiring
    mock_mcp_client = MagicMock()

    with (
        patch("src.agent.strands_client.BedrockModel") as MockBedrockModel,
        patch("src.agent.strands_client.Agent") as MockAgent,
    ):
        mock_bedrock_instance = MagicMock()
        MockBedrockModel.return_value = mock_bedrock_instance

        mock_agent_instance = MagicMock()
        MockAgent.return_value = mock_agent_instance

        result = create_agent(model_id, region, mock_mcp_client, system_prompt)

        # Verify BedrockModel was configured with correct parameters
        MockBedrockModel.assert_called_once_with(
            model_id=model_id,
            region_name=region,
            max_tokens=4096,
        )

        # Verify Agent was created with the BedrockModel, MCPClient, and correct system prompt
        expected_prompt = system_prompt if system_prompt else SYSTEM_PROMPT
        MockAgent.assert_called_once_with(
            model=mock_bedrock_instance,
            tools=[mock_mcp_client],
            system_prompt=expected_prompt,
        )

        # Verify the returned object is the Agent instance
        assert result is mock_agent_instance


@settings(max_examples=100)
@given(
    gateway_url=st.text(min_size=1, max_size=200),
    jwt_token=st.text(min_size=1, max_size=500),
)
def test_create_mcp_client_transport_configuration(gateway_url: str, jwt_token: str) -> None:
    """Property 2: MCPClient factory transport configuration.

    For any gateway_url and jwt_token, create_mcp_client returns an MCPClient
    configured with streamablehttp_client transport using the given URL and
    Authorization: Bearer {jwt_token} header.

    **Validates: Requirements 2.1, 2.2**
    """
    # Feature: strands-sdk-migration, Property 2: MCPClient factory transport configuration
    with (
        patch("src.agent.strands_client.MCPClient") as MockMCPClient,
        patch("src.agent.strands_client.streamablehttp_client") as mock_streamablehttp,
    ):
        mock_mcp_instance = MagicMock()
        MockMCPClient.return_value = mock_mcp_instance

        result = create_mcp_client(gateway_url, jwt_token)

        # Verify MCPClient was constructed with a transport factory callable
        MockMCPClient.assert_called_once()
        transport_factory = MockMCPClient.call_args[0][0]

        # Invoke the transport factory to verify it calls streamablehttp_client
        # with the correct URL and Authorization header
        transport_factory()

        mock_streamablehttp.assert_called_once_with(
            url=gateway_url,
            headers={"Authorization": f"Bearer {jwt_token}"},
        )

        # Verify the returned object is the MCPClient instance
        assert result is mock_mcp_instance
