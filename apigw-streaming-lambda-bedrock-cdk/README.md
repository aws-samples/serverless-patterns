# API Gateway REST Streaming with Lambda and Amazon Bedrock

This pattern deploys an API Gateway REST API with response streaming enabled, backed by a streaming Lambda function that returns real-time LLM responses from Amazon Bedrock using Server-Sent Events (SSE).

Learn more about this pattern at Serverless Land Patterns: https://serverlessland.com/patterns/apigw-streaming-lambda-bedrock-cdk

Important: this application uses various AWS services and there are costs associated with these services after the Free Tier usage - please see the [AWS Pricing page](https://aws.amazon.com/pricing/) for details. You are responsible for any AWS costs incurred. No warranty is implied in this example.

## Requirements

* [Create an AWS account](https://portal.aws.amazon.com/gp/aws/developer/registration/index.html) if you do not already have one and log in.
* [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html) installed and configured
* [Git Installed](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)
* [Node.js 18+](https://nodejs.org/en/download/) installed
* [AWS CDK v2](https://docs.aws.amazon.com/cdk/v2/guide/getting-started.html) installed
* [Amazon Bedrock model access](https://docs.aws.amazon.com/bedrock/latest/userguide/model-access.html) enabled for Anthropic Claude Sonnet in your target region

## Architecture

```
┌──────────┐     ┌──────────────────┐     ┌──────────────────┐     ┌─────────────┐
│  Client   │────▶│  API Gateway     │────▶│  Lambda          │────▶│  Bedrock     │
│  (curl)   │◀────│  REST (Stream)   │◀────│  (Streaming)     │◀────│  (Claude)    │
└──────────┘ SSE └──────────────────┘     └──────────────────┘     └─────────────┘
```

## How it works

1. Client sends a POST request with a prompt to the API Gateway REST endpoint.
2. API Gateway forwards the request to a Lambda function using **streaming invocation** (`InvokeWithResponseStreaming`).
3. The Lambda function calls Amazon Bedrock's `InvokeModelWithResponseStream` API.
4. As Bedrock generates tokens, Lambda writes each chunk to the response stream.
5. API Gateway streams the response back to the client in real-time using chunked transfer encoding.
6. The client receives tokens as they are generated — time-to-first-byte is typically under 1 second.

## Deployment Instructions

1. Clone the repository:
    ```bash
    git clone https://github.com/aws-samples/serverless-patterns
    cd serverless-patterns/apigw-streaming-lambda-bedrock-cdk
    ```

2. Install dependencies:
    ```bash
    npm install
    ```

3. Deploy the stack:
    ```bash
    cdk deploy
    ```

4. Note the API endpoint URL from the stack outputs.

## Testing

1. Stream a response using curl:
    ```bash
    curl --no-buffer -X POST \
      '<ApiEndpoint>/prod/chat' \
      -H 'Content-Type: application/json' \
      -d '{"prompt": "Explain serverless computing in 3 paragraphs"}'
    ```

2. You should see the response stream in real-time, token by token.

## Cleanup

```bash
cdk destroy
```

----
Copyright 2026 Amazon.com, Inc. or its affiliates. All Rights Reserved.

SPDX-License-Identifier: MIT-0
