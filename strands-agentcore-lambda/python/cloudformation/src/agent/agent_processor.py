"""Agent processor orchestrating Strands SDK-based AI pipeline."""

import uuid
from typing import Optional, Tuple

import boto3

from shared.models import UserContext
from shared.logging_utils import StructuredLogger

from .strands_client import create_mcp_client, create_agent


class AgentProcessor:
    """Orchestrates Strands Agent processing for each Lambda invocation."""

    def __init__(
        self,
        gateway_id: str,
        model_id: str,
        region: str,
        logger: StructuredLogger,
    ):
        """Initialize processor.

        Caches gateway_url across invocations within the same Lambda container.

        Args:
            gateway_id: AgentCore Gateway identifier
            model_id: Bedrock model identifier
            region: AWS region
            logger: Structured logger with user context
        """
        self.gateway_id = gateway_id
        self.model_id = model_id
        self.region = region
        self.logger = logger
        self._gateway_url: Optional[str] = None

        logger.info("Agent processor initialized")

    def process(
        self,
        prompt: str,
        jwt_token: str,
        user_context: UserContext,
        session_id: Optional[str],
    ) -> Tuple[str, str]:
        """Process a user prompt through the Strands Agent.

        1. Generate session_id if not provided
        2. Get gateway URL (cached)
        3. Create MCPClient with jwt_token
        4. Create Agent with MCPClient
        5. Call agent(prompt)
        6. Return (str(result), session_id)
        7. Always stop MCPClient in finally block

        Args:
            prompt: User's natural language prompt
            jwt_token: JWT token for Gateway authorization
            user_context: User identity information
            session_id: Optional session ID for conversation continuity

        Returns:
            Tuple of (response_text, session_id)

        Raises:
            Exception: If processing fails critically
        """
        if not session_id:
            session_id = str(uuid.uuid4())
            self.logger.info("New conversation started", session_id=session_id)
        else:
            self.logger.info("Continuing conversation", session_id=session_id)

        gateway_url = self._get_gateway_url()
        mcp_client = create_mcp_client(gateway_url, jwt_token)

        try:
            agent = create_agent(self.model_id, self.region, mcp_client)
            self.logger.info("Invoking agent")
            result = agent(prompt)
            response_text = str(result)
            self.logger.info("Agent invocation completed")
            return response_text, session_id
        finally:
            try:
                mcp_client.stop(None, None, None)
            except Exception:
                pass  # Suppress to avoid masking original error

    def _get_gateway_url(self) -> str:
        """Retrieve and cache Gateway MCP endpoint URL via get_gateway API.

        Returns:
            Gateway MCP endpoint URL
        """
        if self._gateway_url is not None:
            return self._gateway_url

        self.logger.info("Retrieving gateway URL", gateway_id=self.gateway_id)
        client = boto3.client("bedrock-agentcore-control", region_name=self.region)
        response = client.get_gateway(gatewayIdentifier=self.gateway_id)
        self._gateway_url = response["gatewayUrl"]
        self.logger.info("Gateway URL cached", gateway_url=self._gateway_url)
        return self._gateway_url
