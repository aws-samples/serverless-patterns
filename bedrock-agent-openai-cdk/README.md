# Amazon Bedrock Agent with OpenAI model

This pattern deploys an Amazon Bedrock Agent powered by an OpenAI GPT OSS foundation model with a Lambda action group that provides tool-use capabilities.

Learn more about this pattern at Serverless Land Patterns: https://serverlessland.com/patterns/bedrock-agent-openai-cdk

Important: this application uses various AWS services and there are costs associated with these services after the Free Tier usage - please see the [AWS Pricing page](https://aws.amazon.com/pricing/) for details. You are responsible for any AWS costs incurred. No warranty is implied in this example.

## Requirements

* [Create an AWS account](https://portal.aws.amazon.com/gp/aws/developer/registration/index.html) if you do not already have one and log in. The IAM user that you use must have sufficient permissions to make necessary AWS service calls and manage AWS resources.
* [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html) installed and configured
* [Git Installed](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)
* [Node.js 22+](https://nodejs.org/en/download/) installed
* [AWS CDK v2](https://docs.aws.amazon.com/cdk/v2/guide/getting-started.html) installed
* [Amazon Bedrock model access](https://docs.aws.amazon.com/bedrock/latest/userguide/model-access.html) enabled for OpenAI GPT OSS 20B in your target region

## Architecture

```
┌──────────┐     ┌──────────────────────┐     ┌──────────────────┐
│  User    │────▶│  Bedrock Agent        │────▶│  Lambda Action   │
│  (CLI)   │     │  (OpenAI GPT OSS)    │     │  Group Handler   │
└──────────┘     └──────────────────────┘     └──────────────────┘
                  │ Orchestrates tool use │     │ getWeather       │
                  │ via OpenAI model      │     │ getTime          │
                  └──────────────────────┘     └──────────────────┘
```

## How it works

1. The Bedrock Agent receives a natural language query from the user.
2. The agent uses the OpenAI GPT OSS foundation model to reason about the query and decide which tools to call.
3. When the agent determines it needs weather or time data, it invokes the Lambda action group with the appropriate API path and parameters.
4. The Lambda function returns structured data, which the agent incorporates into its final natural language response.

## Deployment Instructions

1. Clone the repository:
    ```bash
    git clone https://github.com/aws-samples/serverless-patterns
    cd serverless-patterns/bedrock-agent-openai-cdk
    ```

2. Install dependencies:
    ```bash
    npm install
    ```

3. Deploy the stack:
    ```bash
    cdk deploy
    ```

4. Note the outputs printed after deployment. You will need `AgentId` and `AgentAliasId` for testing.
    Example output:
    ```
    Outputs:
    BedrockAgentOpenaiStack.AgentId = 2VHQREVYJM
    BedrockAgentOpenaiStack.AgentAliasId = WRP0JKNQFL
    BedrockAgentOpenaiStack.FunctionName = BedrockAgentOpenaiStack-ActionGroupFn-AbCdEfGh
    ```

## Testing

1. Invoke the agent. Replace `<AgentId>` and `<AgentAliasId>` with the values from the deploy output:
    ```bash
    aws bedrock-agent-runtime invoke-agent \
      --agent-id <AgentId> \
      --agent-alias-id <AgentAliasId> \
      --session-id test-session-1 \
      --input-text "What is the weather in Tokyo?" \
      --region us-east-1
    ```
    For example, if your deploy output showed AgentId = 2VHQREVYJM and AgentAliasId = WRP0JKNQFL:
    ```bash
    aws bedrock-agent-runtime invoke-agent \
      --agent-id 2VHQREVYJM \
      --agent-alias-id WRP0JKNQFL \
      --session-id test-session-1 \
      --input-text "What is the weather in Tokyo?" \
      --region us-east-1
    ```

2. Try a multi-tool query:
    ```bash
    aws bedrock-agent-runtime invoke-agent \
      --agent-id <AgentId> \
      --agent-alias-id <AgentAliasId> \
      --session-id test-session-2 \
      --input-text "What is the weather and current time in London?" \
      --region us-east-1
    ```

## Cleanup

```bash
cdk destroy
```

----
Copyright 2026 Amazon.com, Inc. or its affiliates. All Rights Reserved.

SPDX-License-Identifier: MIT-0
