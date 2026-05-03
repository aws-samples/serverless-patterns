# AWS Lambda with Strands Agents SDK and Amazon Bedrock

This pattern deploys an AWS Lambda function running a [Strands Agents SDK](https://strandsagents.com/) agent with Amazon Bedrock as the model provider. The agent uses custom Python tools that the model invokes autonomously during reasoning.

Learn more about this pattern at Serverless Land Patterns: https://serverlessland.com/patterns/lambda-strands-agent-bedrock-cdk

Important: this application uses various AWS services and there are costs associated with these services after the Free Tier usage - please see the [AWS Pricing page](https://aws.amazon.com/pricing/) for details. You are responsible for any AWS costs incurred. No warranty is implied in this example.

## Requirements

* [Create an AWS account](https://portal.aws.amazon.com/gp/aws/developer/registration/index.html) if you do not already have one and log in. The IAM user that you use must have sufficient permissions to make necessary AWS service calls and manage AWS resources.
* [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html) installed and configured
* [Git Installed](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)
* [Node and NPM](https://nodejs.org/en/download/) installed
* [AWS CDK](https://docs.aws.amazon.com/cdk/latest/guide/cli.html) installed
* [Amazon Bedrock model access](https://docs.aws.amazon.com/bedrock/latest/userguide/model-access.html) enabled for Anthropic Claude Sonnet in your target region

## How it works

![Architecture](architecture.png)

1. A client invokes the Lambda function with a JSON payload containing a `prompt` field.
2. The Lambda function initializes a Strands Agents SDK agent with the official Lambda layer (no custom packaging required).
3. The agent uses Amazon Bedrock (Claude Sonnet) as its reasoning engine.
4. When the model decides a tool is needed, the SDK automatically invokes the registered Python tool (e.g., `calculate`) and feeds the result back to the model.
5. The agent returns the final response to the caller.

## Deployment

1. Clone the repository and navigate to the pattern directory:
    ```bash
    git clone https://github.com/aws-samples/serverless-patterns
    cd serverless-patterns/lambda-strands-agent-bedrock-cdk
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

Invoke the Lambda function with a prompt:

```bash
aws lambda invoke \
  --function-name $(aws cloudformation describe-stacks \
    --stack-name LambdaStrandsAgentBedrockStack \
    --query 'Stacks[0].Outputs[?OutputKey==`FunctionName`].OutputValue' \
    --output text) \
  --cli-binary-format raw-in-base64-out \
  --payload '{"prompt": "What is 25 * 47 + 13?"}' \
  output.json

cat output.json | python3 -m json.tool
```

Expected output: The agent will use the `calculate` tool to compute `25 * 47 + 13 = 1188` and explain its reasoning.

## Cleanup

```bash
cdk destroy
```

----
Copyright 2026 Amazon.com, Inc. or its affiliates. All Rights Reserved.

SPDX-License-Identifier: MIT-0
