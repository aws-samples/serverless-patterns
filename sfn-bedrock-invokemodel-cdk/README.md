# AWS Step Functions Express workflow with optimized integration for Amazon Bedrock InvokeModel

This pattern deploys a Step Functions Express workflow that invokes Amazon Bedrock (Claude Sonnet) directly using the optimized integration. Deployed with AWS CDK.

Learn more about this pattern at Serverless Land Patterns: https://serverlessland.com/patterns/sfn-bedrock-invokemodel-cdk

Important: this application uses various AWS services and there are costs associated with these services after the Free Tier usage - please see the [AWS Pricing page](https://aws.amazon.com/pricing/) for details. You are responsible for any AWS costs incurred. No warranty is implied in this example.

## Requirements

- [Create an AWS account](https://portal.aws.amazon.com/gp/aws/developer/registration/index.html) if you do not already have one and log in. The IAM user that you use must have sufficient permissions to make necessary AWS service calls and manage AWS resources.
- [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html) installed and configured
- [AWS CDK](https://docs.aws.amazon.com/cdk/latest/guide/cli.html) installed
- [Node.js](https://nodejs.org/) 20.x or later
- [Amazon Bedrock model access](https://docs.aws.amazon.com/bedrock/latest/userguide/model-access.html) enabled for a model of your choice (Anthropic Claude Sonnet is the default in this pattern) in your AWS account

## How it works

Step Functions has an optimized integration with Amazon Bedrock that lets you call `bedrock:InvokeModel` directly from a workflow state. The optimized integration provides native error handling, automatic retries, and direct payload mapping without intermediate compute.

**Key points:**
- Uses `arn:aws:states:::bedrock:invokeModel` resource (optimized integration)
- Express workflow for synchronous execution (lower cost, sub-5-minute executions)
- Built-in retry with exponential backoff for transient failures
- `resultSelector` extracts just the response text, model, and usage from the Bedrock response

```
┌──────────────────────┐         ┌──────────────────────┐
│                      │         │                      │
│   Step Functions     │────────▶│   Amazon Bedrock     │
│   (Express)          │         │   Claude Sonnet      │
│                      │◀────────│                      │
└──────────────────────┘         └──────────────────────┘
```

## Deployment

1. Install dependencies:
   ```bash
   cd sfn-bedrock-invokemodel-cdk
   npm install
   ```

2. Deploy the stack:
   ```bash
   cdk deploy
   ```

## Testing

Start a synchronous execution of the Express workflow:

```bash
aws stepfunctions start-sync-execution \
  --state-machine-arn $(aws cloudformation describe-stacks \
    --stack-name SfnBedrockInvokemodelStack \
    --query 'Stacks[0].Outputs[?OutputKey==`StateMachineArn`].OutputValue' \
    --output text) \
  --input '{"prompt": "What are the benefits of Step Functions native Bedrock integration?"}' \
  --query '{status: status, output: output}' \
  --output json
```

The response includes the generated text, model ID, and token usage:

```json
{
  "status": "SUCCEEDED",
  "output": "{\"response\": \"...\", \"model\": \"claude-...\", \"usage\": {\"input_tokens\": 15, \"output_tokens\": 200}}"
}
```

## Cleanup

```bash
cdk destroy
```

---

Copyright 2026 Amazon.com, Inc. or its affiliates. All Rights Reserved.

SPDX-License-Identifier: MIT-0
