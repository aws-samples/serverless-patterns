# Amazon Bedrock AgentCore Memory with AWS Lambda (CDK)

This pattern deploys an Amazon Bedrock AgentCore Memory resource with an AWS Lambda function that demonstrates storing conversation events and retrieving memory records.

Learn more about this pattern at Serverless Land Patterns: https://serverlessland.com/patterns/agentcore-memory-cdk

Important: this application uses various AWS services and there are costs associated with these services after the Free Tier usage - please see the [AWS Pricing page](https://aws.amazon.com/pricing/) for details.

## Requirements

* [Create an AWS account](https://portal.aws.amazon.com/gp/aws/developer/registration/index.html) if you do not already have one and log in.
* [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html) installed and configured
* [Node.js 20+](https://nodejs.org/en/download/) installed
* [AWS CDK v2](https://docs.aws.amazon.com/cdk/v2/guide/getting_started.html) installed (`npm install -g aws-cdk`)
* CDK bootstrapped in your account/region (`cdk bootstrap`)

## Deployment Instructions

1. Clone the repository and navigate to the pattern directory:
    ```bash
    cd agentcore-memory-cdk
    ```

2. Install dependencies:
    ```bash
    npm install
    ```

3. Build and deploy:
    ```bash
    npx cdk deploy
    ```

## How it works

Amazon Bedrock AgentCore Memory provides persistent memory for AI agents:

- **Short-term memory**: Stores raw conversation events (messages, tool calls, results) per session. Available immediately after `create_event`.
- **Long-term memory**: Automatically extracted from short-term memory using configurable strategies (semantic, summary, user profile). Enables agents to recall facts and preferences across sessions.

The AWS Lambda function demonstrates two operations:
1. **Store**: Writes conversation events to short-term memory via `create_event`
2. **Retrieve**: Searches long-term memory records via `retrieve_memory_records` using semantic similarity

## Testing

Store a conversation event:
```bash
aws lambda invoke --function-name FUNCTION_NAME \
  --payload '{"action": "store", "messages": [{"role": "user", "content": "My name is Alice and I prefer Python"}, {"role": "assistant", "content": "Nice to meet you, Alice! I will remember your Python preference."}]}' \
  --cli-binary-format raw-in-base64-out output.json && cat output.json
```

Retrieve memory (after extraction completes, typically a few minutes):
```bash
aws lambda invoke --function-name FUNCTION_NAME \
  --payload '{"action": "retrieve", "query": "What programming language does the user prefer?"}' \
  --cli-binary-format raw-in-base64-out output.json && cat output.json
```

## Cleanup

```bash
npx cdk destroy
```

⚠️ This will delete the Amazon Bedrock AgentCore Memory resource and all stored memory records.

---

Copyright 2026 Amazon.com, Inc. or its affiliates. All Rights Reserved.

SPDX-License-Identifier: MIT-0
