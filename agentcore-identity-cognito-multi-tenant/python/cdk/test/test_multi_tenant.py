#!/usr/bin/env python3
"""Invoke the multi-tenant AgentCore Runtime over HTTPS using a Cognito bearer token.

Because the runtime uses OAuth/JWT inbound auth, requests are sent directly to
the InvokeAgentRuntime HTTPS endpoint with an "Authorization: Bearer <token>"
header (the AWS SDK / SigV4 path cannot be used with JWT inbound auth).

Usage:
    export AGENT_ARN="arn:aws:bedrock-agentcore:us-west-2:<acct>:runtime/<id>"
    export REGION="us-west-2"
    export BEARER_TOKEN="<access-token-from-get_token.sh>"
    python test_multi_tenant.py "List my orders"
"""

import os
import sys
import uuid
from urllib.parse import quote

import requests


def main():
    prompt = sys.argv[1] if len(sys.argv) > 1 else "List all of my orders."
    agent_arn = os.environ.get("AGENT_ARN", "")
    region = os.environ.get("REGION", "us-west-2")
    token = os.environ.get("BEARER_TOKEN", "")

    if not agent_arn or not token:
        print("Set AGENT_ARN and BEARER_TOKEN environment variables.")
        print("AGENT_ARN comes from the CDK output 'AgentRuntimeArn'.")
        sys.exit(1)

    encoded_arn = quote(agent_arn, safe="")
    url = (
        f"https://bedrock-agentcore.{region}.amazonaws.com/"
        f"runtimes/{encoded_arn}/invocations?qualifier=DEFAULT"
    )

    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json",
        # Session id must be at least 33 characters.
        "X-Amzn-Bedrock-AgentCore-Runtime-Session-Id": uuid.uuid4().hex + uuid.uuid4().hex,
    }

    print("=" * 60)
    print("Multi-Tenant AgentCore Invocation")
    print("=" * 60)
    print(f"Prompt: {prompt}")
    print(f"Token:  {token[:20]}...")
    print("-" * 60)

    resp = requests.post(url, headers=headers, json={"prompt": prompt}, stream=True, timeout=120)
    print(f"Status: {resp.status_code}")
    if resp.status_code != 200:
        print(resp.text[:1000])
        sys.exit(1)

    for line in resp.iter_lines():
        if line:
            print(line.decode("utf-8"))


if __name__ == "__main__":
    main()
