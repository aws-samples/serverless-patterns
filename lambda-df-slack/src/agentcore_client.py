"""
AgentCore Client - Invokes AgentCore agent runtime
"""
import os
import json
import logging
import boto3
from typing import Optional, Dict, Any

logger = logging.getLogger(__name__)


class AgentCoreClient:
    """Client for invoking AgentCore agent runtime"""

    def __init__(self, agent_runtime_arn: Optional[str] = None):
        """
        Initialize AgentCore client

        Args:
            agent_runtime_arn: ARN of the AgentCore agent runtime
        """
        self.agent_runtime_arn = agent_runtime_arn or os.environ.get('AGENT_RUNTIME_ARN')
        if not self.agent_runtime_arn:
            raise ValueError("AGENT_RUNTIME_ARN environment variable or parameter required")

        # Initialize Bedrock AgentCore client
        self.client = boto3.client('bedrock-agentcore', region_name=os.environ['AWS_REGION'])

        logger.info("Initialized with runtime: %s", self.agent_runtime_arn)

    def invoke_agent(self, payload: Dict[str, Any]) -> Dict[str, Any]:
        """
        Invoke the AgentCore agent runtime

        Args:
            payload: Payload to send to agent (must include callbackId and prompt)

        Returns:
            Response from agent runtime (immediate confirmation)
        """
        logger.info("Invoking agent with payload: %s", json.dumps(payload, default=str)[:200])

        try:
            response = self.client.invoke_agent_runtime(
                agentRuntimeArn=self.agent_runtime_arn,
                payload=json.dumps(payload).encode('utf-8')
            )

            # Parse response
            response_body = response['response'].read().decode('utf-8')
            result = json.loads(response_body)

            logger.info("Agent response: %s", result)
            return result

        except Exception as e:
            logger.error("Error invoking agent: %s", e)
            raise

    def generate_itinerary(
        self,
        destination: str,
        dates: str,
        budget: str,
        interests: str,
        callback_id: str
    ) -> Dict[str, Any]:
        """
        Generate travel itinerary via AgentCore agent

        Args:
            destination: Travel destination
            dates: Travel dates
            budget: Budget amount
            interests: User interests
            callback_id: Durable callback ID

        Returns:
            Confirmation from agent (actual result comes via callback)
        """
        prompt = f"""Create a detailed travel itinerary with the following details:

**Destination:** {destination}
**Dates:** {dates}
**Budget:** {budget}
**Interests:** {interests}

Please provide:
1. **Day-by-Day Itinerary** - Specific activities and timing for each day
2. **Accommodations** - Recommended hotels/areas to stay with price ranges
3. **Must-See Attractions** - Top sights aligned with their interests
4. **Food Recommendations** - Local cuisine and specific restaurant suggestions
5. **Budget Breakdown** - Estimated costs (accommodation, food, activities, transport)
6. **Travel Tips** - Local customs, transportation, best times to visit attractions

Make it practical and actionable. Use bullet points and clear sections."""

        payload = {
            "prompt": prompt,
            "callbackId": callback_id,
            "model": {
                "modelId": os.environ.get('BEDROCK_MODEL_ID', 'us.anthropic.claude-sonnet-4-6')
            },
            "systemPrompt": """You are a knowledgeable travel advisor who creates detailed,
personalized travel itineraries. Provide practical, specific recommendations with
clear day-by-day plans. Format output to be readable in Slack."""
        }

        return self.invoke_agent(payload)
