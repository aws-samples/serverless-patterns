"""Property-based tests for agent_processor.py."""

import sys
from unittest.mock import MagicMock, patch, call

from hypothesis import given, settings, strategies as st

# Mock external SDK modules before importing agent_processor
_mock_modules = {}
for mod_name in [
    "mcp", "mcp.client", "mcp.client.streamable_http",
    "strands", "strands.models", "strands.models.bedrock",
    "strands.tools", "strands.tools.mcp",
]:
    if mod_name not in sys.modules:
        _mock_modules[mod_name] = MagicMock()
        sys.modules[mod_name] = _mock_modules[mod_name]

from src.agent.agent_processor import AgentProcessor  # noqa: E402
from src.shared.models import UserContext  # noqa: E402


def _make_processor(gateway_id: str = "gw-test", model_id: str = "model-test", region: str = "us-east-1") -> AgentProcessor:
    """Create an AgentProcessor with a mock logger."""
    mock_logger = MagicMock()
    return AgentProcessor(
        gateway_id=gateway_id,
        model_id=model_id,
        region=region,
        logger=mock_logger,
    )


def _make_user_context() -> UserContext:
    """Create a minimal UserContext for testing."""
    return UserContext(user_id="u-1", username="tester", client_id="c-1")


@settings(max_examples=100)
@given(
    jwt_tokens=st.lists(
        st.text(min_size=1, max_size=200),
        min_size=1,
        max_size=5,
    ),
)
def test_per_request_mcp_client_lifecycle(jwt_tokens: list[str]) -> None:
    """Property 3: Per-request MCPClient lifecycle.

    For any sequence of process() calls with different JWT tokens, each call
    creates a new MCPClient instance (never reuses a previous client).

    **Validates: Requirements 3.1**
    """
    # Feature: strands-sdk-migration, Property 3: Per-request MCPClient lifecycle
    processor = _make_processor()
    user_context = _make_user_context()

    mock_mcp_clients = []

    with (
        patch("src.agent.agent_processor.create_mcp_client") as mock_create_mcp,
        patch("src.agent.agent_processor.create_agent") as mock_create_agent,
        patch("src.agent.agent_processor.boto3") as mock_boto3,
    ):
        # Set up gateway URL retrieval
        mock_control_client = MagicMock()
        mock_boto3.client.return_value = mock_control_client
        mock_control_client.get_gateway.return_value = {"endpoint": "https://gw.example.com/mcp"}

        # Each call to create_mcp_client returns a distinct mock
        def side_effect_create_mcp(*args, **kwargs):
            client = MagicMock()
            mock_mcp_clients.append(client)
            return client

        mock_create_mcp.side_effect = side_effect_create_mcp

        # Agent returns a simple result when called
        mock_agent = MagicMock()
        mock_agent.return_value = "agent response"
        mock_create_agent.return_value = mock_agent

        # Invoke process() once per JWT token
        for token in jwt_tokens:
            processor.process(
                prompt="hello",
                jwt_token=token,
                user_context=user_context,
                session_id=None,
            )

        # create_mcp_client must be called exactly once per process() call
        assert mock_create_mcp.call_count == len(jwt_tokens)

        # Each call must use the corresponding JWT token
        for i, token in enumerate(jwt_tokens):
            assert mock_create_mcp.call_args_list[i] == call("https://gw.example.com/mcp", token)

        # Every MCPClient instance must be unique (no reuse)
        assert len(mock_mcp_clients) == len(jwt_tokens)
        client_ids = [id(c) for c in mock_mcp_clients]
        assert len(set(client_ids)) == len(client_ids), "MCPClient instances must not be reused"


@settings(max_examples=100)
@given(
    prompt=st.text(min_size=1, max_size=200),
    agent_succeeds=st.booleans(),
    agent_result=st.text(min_size=1, max_size=200),
    stop_raises=st.booleans(),
)
def test_mcp_client_cleanup_on_all_paths(
    prompt: str,
    agent_succeeds: bool,
    agent_result: str,
    stop_raises: bool,
) -> None:
    """Property 4: MCPClient cleanup on all paths.

    Whether the agent succeeds or raises, mcp_client.stop(None, None, None)
    is called exactly once. If stop() itself raises, the original result or
    error is preserved.

    **Validates: Requirements 3.4, 3.5**
    """
    # Feature: strands-sdk-migration, Property 4: MCPClient cleanup on all paths
    processor = _make_processor()
    user_context = _make_user_context()

    mock_mcp_client = MagicMock()
    agent_error = RuntimeError("agent boom")

    if stop_raises:
        mock_mcp_client.stop.side_effect = RuntimeError("stop boom")

    with (
        patch("src.agent.agent_processor.create_mcp_client", return_value=mock_mcp_client) as mock_create_mcp,
        patch("src.agent.agent_processor.create_agent") as mock_create_agent,
        patch("src.agent.agent_processor.boto3") as mock_boto3,
    ):
        # Set up gateway URL retrieval
        mock_control_client = MagicMock()
        mock_boto3.client.return_value = mock_control_client
        mock_control_client.get_gateway.return_value = {"endpoint": "https://gw.example.com/mcp"}

        mock_agent = MagicMock()
        if agent_succeeds:
            mock_agent.return_value = agent_result
        else:
            mock_agent.side_effect = agent_error
        mock_create_agent.return_value = mock_agent

        if agent_succeeds:
            result_text, _ = processor.process(
                prompt=prompt,
                jwt_token="tok",
                user_context=user_context,
                session_id=None,
            )
            # Original result must be preserved regardless of stop() behaviour
            assert result_text == str(agent_result)
        else:
            try:
                processor.process(
                    prompt=prompt,
                    jwt_token="tok",
                    user_context=user_context,
                    session_id=None,
                )
                assert False, "Expected RuntimeError from agent"
            except RuntimeError as exc:
                # Original error must be preserved, not masked by stop() error
                assert exc is agent_error

        # stop(None, None, None) must be called exactly once on every path
        mock_mcp_client.stop.assert_called_once_with(None, None, None)


@settings(max_examples=100)
@given(
    prompt=st.text(min_size=1, max_size=500),
    agent_result_str=st.text(min_size=0, max_size=500),
)
def test_agent_invocation_and_result_conversion(
    prompt: str,
    agent_result_str: str,
) -> None:
    """Property 5: Agent invocation and result conversion.

    For any prompt string and mock agent result, process() invokes agent(prompt)
    and returns str(result) as the response text.

    **Validates: Requirements 4.1, 4.5**
    """
    # Feature: strands-sdk-migration, Property 5: Agent invocation and result conversion
    processor = _make_processor()
    user_context = _make_user_context()

    # Create a mock result object whose str() returns agent_result_str
    mock_result = MagicMock()
    mock_result.__str__ = MagicMock(return_value=agent_result_str)

    with (
        patch("src.agent.agent_processor.create_mcp_client") as mock_create_mcp,
        patch("src.agent.agent_processor.create_agent") as mock_create_agent,
        patch("src.agent.agent_processor.boto3") as mock_boto3,
    ):
        # Set up gateway URL retrieval
        mock_control_client = MagicMock()
        mock_boto3.client.return_value = mock_control_client
        mock_control_client.get_gateway.return_value = {"endpoint": "https://gw.example.com/mcp"}

        mock_mcp_client = MagicMock()
        mock_create_mcp.return_value = mock_mcp_client

        mock_agent = MagicMock()
        mock_agent.return_value = mock_result
        mock_create_agent.return_value = mock_agent

        response_text, session_id = processor.process(
            prompt=prompt,
            jwt_token="test-jwt",
            user_context=user_context,
            session_id=None,
        )

        # Agent must be invoked with the exact prompt
        mock_agent.assert_called_once_with(prompt)

        # Response text must be str(result)
        assert response_text == agent_result_str


@settings(max_examples=100)
@given(
    num_calls=st.integers(min_value=1, max_value=10),
)
def test_gateway_url_caching(num_calls: int) -> None:
    """Property 6: Gateway URL caching.

    For any AgentProcessor instance, calling process() N times (N >= 1)
    results in exactly one get_gateway API call. Subsequent invocations
    reuse the cached Gateway URL.

    **Validates: Requirements 4.2**
    """
    # Feature: strands-sdk-migration, Property 6: Gateway URL caching
    processor = _make_processor(gateway_id="gw-cache-test")
    user_context = _make_user_context()

    with (
        patch("src.agent.agent_processor.create_mcp_client") as mock_create_mcp,
        patch("src.agent.agent_processor.create_agent") as mock_create_agent,
        patch("src.agent.agent_processor.boto3") as mock_boto3,
    ):
        # Set up gateway URL retrieval
        mock_control_client = MagicMock()
        mock_boto3.client.return_value = mock_control_client
        mock_control_client.get_gateway.return_value = {"endpoint": "https://gw.example.com/mcp"}

        mock_mcp_client = MagicMock()
        mock_create_mcp.return_value = mock_mcp_client

        mock_agent = MagicMock()
        mock_agent.return_value = "response"
        mock_create_agent.return_value = mock_agent

        # Call process() N times
        for i in range(num_calls):
            processor.process(
                prompt=f"prompt-{i}",
                jwt_token=f"token-{i}",
                user_context=user_context,
                session_id=None,
            )

        # get_gateway must be called exactly once regardless of N
        mock_control_client.get_gateway.assert_called_once_with(gatewayId="gw-cache-test")

        # boto3.client should also be called only once (for the control client)
        mock_boto3.client.assert_called_once_with("bedrock-agentcore-control", region_name="us-east-1")

        # create_mcp_client should be called N times (per-request), all with the cached URL
        assert mock_create_mcp.call_count == num_calls
        for i in range(num_calls):
            assert mock_create_mcp.call_args_list[i] == call("https://gw.example.com/mcp", f"token-{i}")
