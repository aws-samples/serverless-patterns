# Amazon Bedrock AgentCore Gateway with AWS Lambda tools

This pattern deploys an Amazon Bedrock AgentCore Gateway that exposes AWS Lambda functions as MCP (Model Context Protocol) tools. Any MCP-compatible client can discover and invoke the tools via the Gateway's MCP endpoint.

Learn more about this pattern at Serverless Land Patterns: https://serverlessland.com/patterns/agentcore-gateway-lambda-typescript-cdk

Important: this application uses various AWS services and there are costs associated with these services after the Free Tier usage - please see the [AWS Pricing page](https://aws.amazon.com/pricing/) for details. You are responsible for any AWS costs incurred. No warranty is implied in this example.

## Requirements

* [Create an AWS account](https://portal.aws.amazon.com/gp/aws/developer/registration/index.html) if you do not already have one and log in. The IAM user that you use must have sufficient permissions to make necessary AWS service calls and manage AWS resources.
* [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html) installed and configured
* [Git Installed](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)
* [Node.js 22+](https://nodejs.org/en/download/) installed
* [AWS CDK v2](https://docs.aws.amazon.com/cdk/v2/guide/getting-started.html) installed
* [Python 3.9+](https://www.python.org/downloads/) installed, with the test dependencies installed by `python3 -m pip install boto3 botocore` (for testing)

## Architecture

```
┌──────────────┐     ┌──────────────────────────┐     ┌──────────────────┐
│  MCP Client  │────▶│  AgentCore Gateway       │────▶│  Lambda Function │
│  (Agent/CLI) │     │  (MCP protocol, IAM auth) │     │  (Tool handler)  │
└──────────────┘     └──────────────────────────┘     └──────────────────┘
                      │ tools/list               │     │ get_weather      │
                      │ tools/call               │     │ get_time         │
                      └──────────────────────────┘     └──────────────────┘
```

## How it works

1. The AgentCore Gateway is created with MCP protocol and IAM authentication.
2. A Lambda function is registered as a Gateway target with inline tool definitions (get_weather, get_time).
3. MCP clients send `tools/list` to discover available tools and `tools/call` to invoke them.
4. The Gateway routes tool calls to the Lambda function, passing the tool arguments as the event and the invoked tool name (`<target name>___<tool name>`, for example `city-tools___get_time`) in `context.clientContext.custom.bedrockAgentCoreToolName`. The function branches on the tool name and returns an MCP `content` item with the result as JSON text.

## Deployment Instructions

1. Clone the repository:
    ```bash
    git clone https://github.com/aws-samples/serverless-patterns
    cd serverless-patterns/agentcore-gateway-lambda/typescript/cdk
    ```

2. Install dependencies:
    ```bash
    npm install
    ```

3. If this is the first time you deploy CDK stacks into this AWS account and Region, [bootstrap](https://docs.aws.amazon.com/cdk/v2/guide/bootstrapping.html) the environment:
    ```bash
    cdk bootstrap
    ```

4. Deploy the stack:
    ```bash
    cdk deploy
    ```

5. Note the outputs printed after deployment. You will need `GatewayUrl` for testing.
    Example output:
    ```
    Outputs:
    AgentcoreGatewayLambdaStack.GatewayId = tool-gateway-bdastack-mkrkf8fntt
    AgentcoreGatewayLambdaStack.GatewayUrl = https://tool-gateway-bdastack-mkrkf8fntt.gateway.bedrock-agentcore.us-east-1.amazonaws.com/mcp
    AgentcoreGatewayLambdaStack.TargetId = KNBRZ24GFJ
    AgentcoreGatewayLambdaStack.FunctionName = AgentcoreGatewayLambdaStack-ToolFn-AbCdEfGh
    ```

## Testing

The Gateway uses IAM authentication, so requests must be signed with SigV4, and the calling identity needs the `bedrock-agentcore:InvokeGateway` permission on the gateway ARN (`arn:aws:bedrock-agentcore:<your-region>:<account-id>:gateway/<GatewayId>`, using the `GatewayId` deploy output); without it the signed request is denied ([IAM-based inbound authorization](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/gateway-inbound-auth.html#gateway-inbound-auth-iam)). Any IAM principal in the account whose identity-based policy allows that action can call the gateway. To narrow that down, attach a [resource-based policy](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/resource-based-policies.html) to the gateway; an explicit deny in either kind of policy takes precedence. Replace `<GatewayUrl>` with the `GatewayUrl` value from the deploy output, and `<your-region>` with your deployment region (e.g. `us-east-1`).

1. List available tools:
    ```python
    import boto3, json, urllib.request
    from botocore.auth import SigV4Auth
    from botocore.awsrequest import AWSRequest

    session = boto3.Session()
    creds = session.get_credentials().get_frozen_credentials()
    url = "<GatewayUrl>"
    region = "<your-region>"

    payload = json.dumps({"jsonrpc": "2.0", "method": "tools/list", "id": 1})
    req = AWSRequest(method="POST", url=url, data=payload,
                     headers={"Content-Type": "application/json"})
    SigV4Auth(creds, "bedrock-agentcore", region).add_auth(req)

    http_req = urllib.request.Request(url, data=payload.encode(),
                                      headers=dict(req.headers), method="POST")
    resp = urllib.request.urlopen(http_req, timeout=30)
    print(json.dumps(json.loads(resp.read()), indent=2))
    ```

2. Call a tool:
    ```python
    payload = json.dumps({
        "jsonrpc": "2.0", "method": "tools/call", "id": 2,
        "params": {"name": "city-tools___get_weather",
                   "arguments": {"city": "Tokyo"}}
    })
    req = AWSRequest(method="POST", url=url, data=payload,
                     headers={"Content-Type": "application/json"})
    SigV4Auth(creds, "bedrock-agentcore", region).add_auth(req)

    http_req = urllib.request.Request(url, data=payload.encode(),
                                      headers=dict(req.headers), method="POST")
    resp = urllib.request.urlopen(http_req, timeout=30)
    print(json.dumps(json.loads(resp.read()), indent=2))
    ```

3. Call the other tool by running the code from step 2 again with `"name": "city-tools___get_time"`. The `text` value in the result holds only the city and the UTC time, with no weather values:
    ```json
    {"city":"Tokyo","utcTime":"2026-11-16T13:49:08.564Z"}
    ```

## Cleanup

```bash
cdk destroy
```

----
Copyright 2026 Amazon.com, Inc. or its affiliates. All Rights Reserved.

SPDX-License-Identifier: MIT-0
