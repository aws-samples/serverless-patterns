"""Shared OpenSearch Serverless client configuration."""

import boto3
from opensearchpy import OpenSearch, RequestsHttpConnection
from requests_aws4auth import AWS4Auth


def get_client(endpoint: str, region: str) -> OpenSearch:
    """Create an OpenSearch client authenticated with SigV4 for AOSS.

    Args:
        endpoint: The collection endpoint URL (https://...).
        region: AWS region code (e.g. eu-west-1).
    """
    host = endpoint.replace("https://", "").rstrip("/")

    credentials = boto3.Session().get_credentials()
    auth = AWS4Auth(
        credentials.access_key,
        credentials.secret_key,
        region,
        "aoss",
        session_token=credentials.token,
    )

    return OpenSearch(
        hosts=[{"host": host, "port": 443}],
        http_auth=auth,
        use_ssl=True,
        verify_certs=True,
        connection_class=RequestsHttpConnection,
        timeout=25,
        max_retries=3,
        retry_on_timeout=True,
        retry_on_status=(502, 503),
    )
