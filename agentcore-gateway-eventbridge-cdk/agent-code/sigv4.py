"""
SigV4 authentication for the MCP streamable-HTTP transport.

The MCP Python SDK's streamablehttp_client is a plain httpx-based client
with no native AWS SigV4 support. AgentCore Gateway's AWS_IAM inbound
authorizer requires each HTTP request to be signed with SigV4 (service
"bedrock-agentcore"). This wraps botocore's SigV4Auth as an httpx.Auth
so it can be passed directly to streamablehttp_client's `auth=` parameter.

Reference pattern: awslabs/agentcore-samples gatewaylabproject/streamable_http_sigv4.py
"""
import boto3
import httpx
from botocore.auth import SigV4Auth
from botocore.awsrequest import AWSRequest


class SigV4HTTPXAuth(httpx.Auth):
    """httpx.Auth implementation that signs requests with AWS SigV4."""

    def __init__(self, region: str, service: str = "bedrock-agentcore"):
        session = boto3.Session()
        credentials = session.get_credentials()
        if credentials is None:
            raise RuntimeError("No AWS credentials available to sign Gateway requests")
        self._signer = SigV4Auth(credentials, service, region)

    def auth_flow(self, request: httpx.Request):
        headers = dict(request.headers)
        # The "connection" header is not part of the canonical request and
        # including it breaks the signature validation on the server side.
        headers.pop("connection", None)

        aws_request = AWSRequest(
            method=request.method,
            url=str(request.url),
            data=request.content,
            headers=headers,
        )
        self._signer.add_auth(aws_request)
        request.headers.update(dict(aws_request.headers))
        yield request
