"""
Secrets Manager integration for Slack credentials.
Fetches and caches secrets for the Lambda container lifetime.
"""
import json
import os
import logging
from typing import Optional

import boto3

logger = logging.getLogger(__name__)

_secrets_cache: Optional[dict] = None


def get_slack_secrets() -> dict:
    """
    Fetch Slack bot token and signing secret from AWS Secrets Manager.
    Caches result for Lambda container lifetime to avoid repeated API calls.

    Returns:
        dict with keys 'SLACK_BOT_TOKEN' and 'SLACK_SIGNING_SECRET'
    """
    global _secrets_cache
    if _secrets_cache is not None:
        return _secrets_cache

    secret_arn = os.environ['SLACK_SECRETS_ARN']
    client = boto3.client('secretsmanager')
    response = client.get_secret_value(SecretId=secret_arn)
    _secrets_cache = json.loads(response['SecretString'])
    logger.info("Slack secrets loaded from Secrets Manager")
    return _secrets_cache
