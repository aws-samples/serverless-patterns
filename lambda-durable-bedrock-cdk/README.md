# Lambda Durable Functions with Amazon Bedrock

This pattern deploys a Lambda durable function that orchestrates a multi-step AI content pipeline using Amazon Bedrock. Each step is automatically checkpointed, so the workflow resumes from the last completed step after any interruption — without re-invoking Bedrock.

Learn more about this pattern at Serverless Land Patterns: https://serverlessland.com/patterns/lambda-durable-bedrock-cdk

Important: this application uses various AWS services and there are costs associated with these services after the Free Tier usage - please see the [AWS Pricing page](https://aws.amazon.com/pricing/) for details. You are responsible for any AWS costs incurred. No warranty is implied in this example.

## Requirements

* [Create an AWS account](https://portal.aws.amazon.com/gp/aws/developer/registration/index.html) if you do not already have one and log in. The IAM user that you use must have sufficient permissions to make necessary AWS service calls and manage AWS resources.
* [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html) installed and configured
* [Git Installed](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)
* [Node.js 18+](https://nodejs.org/en/download/) installed
* [AWS CDK v2](https://docs.aws.amazon.com/cdk/v2/guide/getting-started.html) installed
* [Amazon Bedrock model access](https://docs.aws.amazon.com/bedrock/latest/userguide/model-access.html) enabled for Anthropic Claude Sonnet in your target region

## Architecture

```
┌─────────────┐     ┌──────────────────────────────────────────────────┐
│   Invoke     │────▶│  Lambda Durable Function                         │
│  (CLI/SDK)   │     │                                                  │
└─────────────┘     │  Step 1: Generate Outline ──▶ Bedrock (Claude)   │
                    │       ✓ checkpoint                               │
                    │  Wait: 5s (simulate review)                      │
                    │       ✓ checkpoint                               │
                    │  Step 2: Expand Draft ──▶ Bedrock (Claude)       │
                    │       ✓ checkpoint                               │
                    │  Step 3: Summarize ──▶ Bedrock (Claude)          │
                    │       ✓ checkpoint                               │
                    └──────────────────────────────────────────────────┘
```

## How it works

1. The Lambda durable function receives a topic as input.
2. **Step 1** calls Amazon Bedrock (Claude Sonnet) to generate a blog outline from the topic. The result is checkpointed.
3. The function **waits** 5 seconds (simulating an editorial review pause). During the wait, no compute charges are incurred.
4. **Step 2** calls Bedrock to expand the outline into a full blog draft. Checkpointed.
5. **Step 3** calls Bedrock to generate a concise summary. Checkpointed.
6. If the function is interrupted at any point, it replays from the last checkpoint — completed Bedrock calls are not re-executed.

## Deployment Instructions

1. Clone the repository:
    ```bash
    git clone https://github.com/aws-samples/serverless-patterns
    cd serverless-patterns/lambda-durable-bedrock-cdk
    ```

2. Install dependencies:
    ```bash
    npm install
    ```

3. Deploy the stack:
    ```bash
    cdk deploy
    ```

4. Note the Lambda function name from the stack outputs.

## Testing

1. Invoke the durable function (use the published version from the output):
    ```bash
    aws lambda invoke \
      --function-name <FunctionName> \
      --qualifier 1 \
      --payload '{"topic": "Serverless AI workflows with Lambda durable functions"}' \
      --cli-binary-format raw-in-base64-out \
      output.json
    ```

2. Since the function includes a wait, the initial invocation returns quickly. Check the durable execution status:
    ```bash
    aws lambda list-durable-executions \
      --function-name <FunctionName> \
      --qualifier 1
    ```

3. Once the execution completes, view the result:
    ```bash
    cat output.json | jq .
    ```

## Cleanup

```bash
cdk destroy
```

----
Copyright 2026 Amazon.com, Inc. or its affiliates. All Rights Reserved.

SPDX-License-Identifier: MIT-0
