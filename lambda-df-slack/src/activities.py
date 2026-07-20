"""
Activity Functions using AWS Lambda Durable Functions
These are durable steps that can be called within orchestrator functions
"""
import os
from typing import Dict, Any

from aws_durable_execution_sdk_python import durable_step, StepContext

from utils.slack_client import SlackClient
# from utils.bedrock_client import BedrockClient  # Not used - AgentCore handles AI

# NOTE: Bedrock functions removed - we use AgentCore for AI instead


@durable_step
def post_to_slack(step_ctx: StepContext, channel: str, text: str, blocks: list = None) -> Dict[str, Any]:
    """
    Durable step for posting to Slack

    Args:
        step_ctx: Step context
        channel: Slack channel ID
        text: Message text
        blocks: Optional Block Kit blocks

    Returns:
        Slack API response
    """
    step_ctx.logger.info(f"Posting to Slack channel: {channel}")

    slack = SlackClient()
    result = slack.post_message(
        channel=channel,
        text=text,
        blocks=blocks
    )

    step_ctx.logger.info("Message posted to Slack successfully")
    return result


def format_itinerary_blocks(itinerary_text: str) -> list:
    """
    Format itinerary text as Slack Block Kit blocks

    This is a pure function (not a step) since it doesn't interact with external services.
    """
    blocks = [
        {
            "type": "header",
            "text": {
                "type": "plain_text",
                "text": "🎉 Your Personalized Travel Itinerary"
            }
        },
        {
            "type": "divider"
        },
        {
            "type": "section",
            "text": {
                "type": "mrkdwn",
                "text": itinerary_text
            }
        },
        {
            "type": "divider"
        },
        {
            "type": "context",
            "elements": [
                {
                    "type": "mrkdwn",
                    "text": "_Have an amazing trip! Feel free to ask me to plan another one anytime._"
                }
            ]
        }
    ]

    return blocks
