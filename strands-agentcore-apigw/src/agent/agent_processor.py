"""Agent processor orchestrating AI pipeline via Strands Agents SDK.

Uses the official strands-agents SDK. The SDK's Agent class handles the
full agentic loop automatically — multi-turn tool use, parallel tool
calls, and response generation are all managed by the SDK.
"""

import uuid
from typing import Optional, Tuple

import boto3

from shared.logging_utils import StructuredLogger
from .strands_client import create_mcp_client, create_agent


class AgentProcessor:
    """Orchestrates AI agent processing via Strands Agents SDK + AgentCore Gateway."""

    def __init__(
        self,
        gateway_id: str,
        model_id: str,
        region: str,
        logger: StructuredLogger,
    ):
        self.gateway_id = gateway_id
        self.model_id = model_id
        self.region = region
        self.logger = logger

        # Resolve Gateway MCP URL once
        self._gateway_url: Optional[str] = None

        logger.info("Agent processor initialized")

    # ------------------------------------------------------------------
    # Public API
    # ------------------------------------------------------------------

    def process_request(
        self,
        prompt: str,
        jwt_token: str,
        session_id: Optional[str] = None,
    ) -> Tuple[str, str]:
        """Process a user prompt end-to-end.

        1. Resolve session
        2. Connect to Gateway via MCPClient
        3. Create Strands Agent with MCP tools
        4. Run the agent (SDK handles tool loop)
        5. Return response text + session_id

        Args:
            prompt: User's natural language prompt
            jwt_token: Cognito JWT for Gateway auth
            session_id: Optional conversation session ID

        Returns:
            Tuple of (response_text, session_id)
        """
        if not session_id:
            session_id = str(uuid.uuid4())
            self.logger.info("New conversation started", session_id=session_id)
        else:
            self.logger.info("Continuing conversation", session_id=session_id)

        gateway_url = self._get_gateway_url()

        # Create MCPClient for this invocation (per Lambda best practice).
        # Do NOT use `with mcp_client:` — the Agent's tool registry calls
        # load_tools() → start() internally. Starting it beforehand causes
        # "the client session is currently running" error.
        mcp_client = create_mcp_client(gateway_url, jwt_token)

        try:
            agent = create_agent(
                model_id=self.model_id,
                region=self.region,
                mcp_client=mcp_client,
            )

            self.logger.info("Invoking Strands agent", prompt_length=len(prompt))

            # The SDK handles the full agentic loop:
            # prompt → model reasoning → tool selection → tool execution → repeat → final response
            result = agent(prompt)
            response_text = str(result)

            self.logger.info(
                "Agent request processed successfully",
                session_id=session_id,
                response_length=len(response_text),
            )

            return response_text, session_id

        except Exception as e:
            self.logger.error("Agent processing failed", error=str(e))
            raise
        finally:
            # Clean up MCP connection
            try:
                mcp_client.stop(None, None, None)
            except Exception:
                pass

    # ------------------------------------------------------------------
    # Internal helpers
    # ------------------------------------------------------------------

    def _get_gateway_url(self) -> str:
        """Resolve and cache the Gateway MCP endpoint URL."""
        if self._gateway_url:
            return self._gateway_url

        client = boto3.client("bedrock-agentcore-control", region_name=self.region)
        response = client.get_gateway(gatewayIdentifier=self.gateway_id)
        gateway_url = response.get("gatewayUrl")

        if not gateway_url:
            raise RuntimeError("Gateway URL not found in get_gateway response")

        self._gateway_url = gateway_url
        self.logger.info("Gateway URL resolved", gateway_url=gateway_url)
        return gateway_url
