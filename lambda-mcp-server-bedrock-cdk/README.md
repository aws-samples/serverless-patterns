# Lambda MCP Server with Amazon Bedrock

This pattern deploys a stateless [MCP (Model Context Protocol)](https://modelcontextprotocol.io/) server on AWS Lambda with a Function URL. The server exposes Bedrock-powered tools that any MCP client can use.

Learn more about this pattern at Serverless Land Patterns: https://serverlessland.com/patterns/lambda-mcp-server-bedrock-cdk

Important: this application uses various AWS services and there are costs associated with these services after the Free Tier usage - please see the [AWS Pricing page](https://aws.amazon.com/pricing/) for details. You are responsible for any AWS costs incurred. No warranty is implied in this example.

## Requirements

* [Create an AWS account](https://portal.aws.amazon.com/gp/aws/developer/registration/index.html) if you do not already have one and log in.
* [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html) installed and configured
* [Node and NPM](https://nodejs.org/en/download/) installed
* [AWS CDK](https://docs.aws.amazon.com/cdk/latest/guide/cli.html) installed

## How it works

MCP (Model Context Protocol) is an open standard for connecting AI assistants to external tools and data sources. This pattern deploys a serverless MCP server that:

- **Runs on Lambda** with a Function URL — no API Gateway needed
- **Implements MCP protocol** (JSON-RPC 2.0 over HTTP) with `initialize`, `tools/list`, and `tools/call`
- **Exposes two tools**: `ask_bedrock` (general Q&A) and `summarize` (text summarization)
- **Stateless design** — scales horizontally with no session management

```
MCP Client (Claude Desktop / Kiro / VS Code)
    ↓ HTTP POST (JSON-RPC)
Lambda Function URL
    ↓ tools/call
Amazon Bedrock (Claude) → Response
```

## Available MCP Tools

| Tool | Description | Input |
|------|-------------|-------|
| `ask_bedrock` | Ask Bedrock a question | `prompt` (string), `max_tokens` (number, optional) |
| `summarize` | Summarize text | `text` (string) |

## Deployment Instructions

1. Clone the repository and navigate to the pattern directory:
    ```bash
    git clone https://github.com/aws-samples/serverless-patterns
    cd serverless-patterns/lambda-mcp-server-bedrock-cdk
    ```

2. Install dependencies:
    ```bash
    npm install
    ```

3. Deploy the stack:
    ```bash
    cdk deploy
    ```

## Testing

Test the MCP server directly with curl:

```bash
# Initialize
curl -X POST <McpServerUrl> \
  -H "Content-Type: application/json" \
  -d '{"jsonrpc":"2.0","id":1,"method":"initialize","params":{"protocolVersion":"2025-03-26","capabilities":{},"clientInfo":{"name":"test","version":"1.0"}}}'

# List tools
curl -X POST <McpServerUrl> \
  -H "Content-Type: application/json" \
  -d '{"jsonrpc":"2.0","id":2,"method":"tools/list"}'

# Call ask_bedrock tool
curl -X POST <McpServerUrl> \
  -H "Content-Type: application/json" \
  -d '{"jsonrpc":"2.0","id":3,"method":"tools/call","params":{"name":"ask_bedrock","arguments":{"prompt":"What is MCP?"}}}'
```

## Connecting MCP Clients

Add to your MCP client configuration (e.g., Claude Desktop `claude_desktop_config.json`):

```json
{
  "mcpServers": {
    "lambda-bedrock": {
      "url": "<McpEndpoint>"
    }
  }
}
```

## Cleanup

```bash
cdk destroy
```

----
Copyright 2025 Amazon.com, Inc. or its affiliates. All Rights Reserved.

SPDX-License-Identifier: MIT-0
