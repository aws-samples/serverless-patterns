# AWS Lambda Ruby 4.0 with Amazon Bedrock

This pattern deploys a Ruby 4.0 Lambda function that invokes Amazon Bedrock (Claude Sonnet) for AI-powered text generation with JSON structured logging.

Learn more about this pattern at Serverless Land Patterns: https://serverlessland.com/patterns/lambda-ruby4-bedrock-cdk

Important: this application uses various AWS services and there are costs associated with these services after the Free Tier usage - please see the [AWS Pricing page](https://aws.amazon.com/pricing/) for details. You are responsible for any AWS costs incurred. No warranty is implied in this example.

## Requirements

* [Create an AWS account](https://portal.aws.amazon.com/gp/aws/developer/registration/index.html) if you do not already have one and log in. The IAM user that you use must have sufficient permissions to make necessary AWS service calls and manage AWS resources.
* [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html) installed and configured
* [AWS CDK](https://docs.aws.amazon.com/cdk/latest/guide/cli.html) installed
* [Node.js](https://nodejs.org/en/download/) installed
* [Amazon Bedrock model access](https://docs.aws.amazon.com/bedrock/latest/userguide/model-access.html) enabled for Claude Sonnet in your region

## Deployment Instructions

1. Create a new directory, navigate to that directory in a terminal and clone the GitHub repository:
    ```
    git clone https://github.com/aws-samples/serverless-patterns
    ```
2. Change directory to the pattern directory:
    ```
    cd serverless-patterns/lambda-ruby4-bedrock-cdk
    ```
3. Install dependencies:
    ```
    npm install
    ```
4. Deploy the stack:
    ```
    cdk deploy
    ```

## How it works

- A Ruby 4.0 Lambda function is deployed on ARM64 (Graviton) architecture
- The function uses the `aws-sdk-bedrockruntime` gem (bundled in the managed runtime) to invoke Amazon Bedrock
- JSON structured logging is enabled via Lambda advanced logging controls (new feature in Ruby 4.0 runtime)
- The function accepts a `prompt` field in the event payload and returns the AI-generated response

## Testing

Invoke the function with a test event:

```bash
aws lambda invoke \
  --function-name $(aws cloudformation describe-stacks --stack-name LambdaRuby4BedrockStack --query 'Stacks[0].Outputs[?OutputKey==`FunctionName`].OutputValue' --output text) \
  --payload '{"prompt": "Explain serverless computing in 3 sentences."}' \
  --cli-binary-format raw-in-base64-out \
  response.json && cat response.json
```

## Cleanup

```
cdk destroy
```

---

Copyright 2026 Amazon.com, Inc. or its affiliates. All Rights Reserved.

SPDX-License-Identifier: MIT-0
