"""
Slack API Client Wrapper
Handles posting messages to Slack channels
"""
import json
import logging
import urllib.request
import urllib.error
from typing import Optional, Dict, Any

from secrets import get_slack_secrets

logger = logging.getLogger(__name__)


class SlackClient:
    """Simple Slack API client"""

    def __init__(self):
        secrets = get_slack_secrets()
        self.bot_token = secrets['SLACK_BOT_TOKEN']

    def post_message(self, channel: str, text: str, blocks: Optional[list] = None) -> Dict[str, Any]:
        """
        Post a message to a Slack channel

        Args:
            channel: Channel ID or DM ID
            text: Message text (fallback if blocks not rendered)
            blocks: Optional Block Kit blocks for rich formatting

        Returns:
            API response dict
        """
        url = 'https://slack.com/api/chat.postMessage'

        payload = {
            'channel': channel,
            'text': text
        }

        if blocks:
            payload['blocks'] = blocks

        headers = {
            'Content-Type': 'application/json',
            'Authorization': f'Bearer {self.bot_token}'
        }

        try:
            req = urllib.request.Request(
                url,
                data=json.dumps(payload).encode('utf-8'),
                headers=headers,
                method='POST'
            )

            with urllib.request.urlopen(req) as response:
                result = json.loads(response.read().decode('utf-8'))

                if not result.get('ok'):
                    logger.error("Slack API error: %s", result.get('error'))
                    raise Exception(f"Slack API error: {result.get('error')}")

                logger.info("Posted message to %s: %s...", channel, text[:50])
                return result

        except urllib.error.HTTPError as e:
            error_body = e.read().decode('utf-8')
            logger.error("HTTP error posting to Slack: %s - %s", e.code, error_body)
            raise

        except Exception as e:
            logger.error("Error posting to Slack: %s", e)
            raise

    def post_rich_message(self, channel: str, text: str, sections: list) -> Dict[str, Any]:
        """
        Post a rich message using Block Kit

        Args:
            channel: Channel ID
            text: Fallback text
            sections: List of section blocks

        Example:
            sections = [
                {"type": "section", "text": {"type": "mrkdwn", "text": "*Bold* text"}}
            ]
        """
        return self.post_message(channel, text, blocks=sections)
