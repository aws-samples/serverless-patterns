"""
Slack API Client Wrapper
Handles posting messages to Slack channels
"""
import os
import json
import urllib.request
import urllib.error
from typing import Optional, Dict, Any


class SlackClient:
    """Simple Slack API client"""

    def __init__(self):
        self.bot_token = os.environ.get('SLACK_BOT_TOKEN')
        if not self.bot_token:
            raise ValueError("SLACK_BOT_TOKEN environment variable not set")

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
                    print(f"Slack API error: {result.get('error')}")
                    raise Exception(f"Slack API error: {result.get('error')}")

                print(f"Posted message to {channel}: {text[:50]}...")
                return result

        except urllib.error.HTTPError as e:
            error_body = e.read().decode('utf-8')
            print(f"HTTP error posting to Slack: {e.code} - {error_body}")
            raise

        except Exception as e:
            print(f"Error posting to Slack: {e}")
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
