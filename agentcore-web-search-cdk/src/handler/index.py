"""
AWS Lambda function that invokes an Amazon Bedrock AgentCore Gateway
with the Web Search Tool to answer questions using live web data.
"""

import json
import os
import urllib.request


def handler(event, context):
    """Invoke the Amazon Bedrock AgentCore Gateway web search tool via MCP protocol."""
    try:
        gateway_id = os.environ["GATEWAY_ID"]
        region = os.environ.get("AWS_REGION", "us-east-1")
        endpoint = os.environ.get(
            "GATEWAY_URL",
            f"https://{gateway_id}.gateway.bedrock-agentcore.{region}.amazonaws.com/mcp",
        )

        import botocore.session
        from botocore.auth import SigV4Auth
        from botocore.awsrequest import AWSRequest

        session = botocore.session.get_session()
        credentials = session.get_credentials().get_frozen_credentials()

        action = event.get("action", "search")

        if action == "list_tools":
            mcp_request = {"jsonrpc": "2.0", "id": "1", "method": "tools/list", "params": {}}
        else:
            query = event.get("query", "What is Amazon Bedrock AgentCore?")
            max_results = event.get("maxResults", 5)
            tool_name = event.get("toolName", "web-search-target___WebSearch")
            mcp_request = {
                "jsonrpc": "2.0",
                "id": "1",
                "method": "tools/call",
                "params": {
                    "name": tool_name,
                    "arguments": {
                        "query": query[:200],
                        "maxResults": min(max(int(max_results), 1), 25),
                    },
                },
            }

        payload = json.dumps(mcp_request).encode("utf-8")

        request = AWSRequest(
            method="POST",
            url=endpoint,
            data=payload,
            headers={"Content-Type": "application/json", "Accept": "application/json"},
        )
        SigV4Auth(credentials, "bedrock-agentcore", region).add_auth(request)

        req = urllib.request.Request(
            endpoint, data=payload, headers=dict(request.headers), method="POST",
        )

        with urllib.request.urlopen(req, timeout=25) as resp:
            response_body = json.loads(resp.read().decode("utf-8"))

        return {
            "statusCode": 200,
            "body": json.dumps({"results": response_body}),
        }

    except Exception as e:
        return {
            "statusCode": 500,
            "body": json.dumps({"error": str(e)}),
        }
