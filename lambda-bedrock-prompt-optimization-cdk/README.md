---

Copyright 2026 Amazon.com, Inc. or its affiliates. All Rights Reserved.

SPDX-License-Identifier: MIT-0

---

# Lambda to Bedrock Advanced Prompt Optimization (CDK)

This pattern deploys a Lambda function that creates an Amazon Bedrock Advanced Prompt Optimization job to automatically optimize prompts for your target model(s). The function uploads evaluation data to S3, submits the optimization job, polls for completion, and returns results.

Learn more about this pattern at Serverless Land Patterns: https://serverlessland.com/patterns/lambda-bedrock-prompt-optimization-cdk

Important: this application uses various AWS services and there are costs associated with these services after the Free Tier usage - please see the [AWS Pricing page](https://aws.amazon.com/pricing/) for details. You are responsible for any AWS costs incurred. No warranty is implied in this example.

## Requirements

- [Create an AWS account](https://portal.aws.amazon.com/gp/aws/developer/registration/index.html) if you do not already have one and log in. The IAM user that you use must have sufficient permissions to make necessary AWS service calls and manage AWS resources.
- [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html) installed and configured
- [AWS CDK](https://docs.aws.amazon.com/cdk/latest/guide/cli.html) installed
- [Node.js](https://nodejs.org/) 20.x or later
- [Amazon Bedrock model access](https://docs.aws.amazon.com/bedrock/latest/userguide/model-access.html) enabled for your target model (Anthropic Claude Sonnet is the default)

## Deployment Instructions

1. Create a new directory, navigate to the directory, and clone the repository:
   ```bash
   git clone https://github.com/aws-samples/serverless-patterns
   cd serverless-patterns/lambda-bedrock-prompt-optimization-cdk
   ```

2. Install dependencies:
   ```bash
   npm install
   ```

3. Deploy the stack:
   ```bash
   cdk deploy
   ```

## How it works

1. The Lambda function receives a prompt template and evaluation samples (or uses defaults).
2. It uploads the input data as JSONL to an S3 bucket.
3. It calls `CreateAdvancedPromptOptimizationJob` with the input S3 URI, output S3 URI, and target model configuration.
4. The service runs iterative inference-evaluate-rewrite loops to optimize the prompt.
5. The Lambda polls `GetAdvancedPromptOptimizationJob` every 10 seconds until completion.
6. Results (optimized prompts with evaluation metrics) are written to S3 and returned in the response.

## Architecture

```
┌──────────┐         ┌─────────────────┐         ┌────────┐
│  Lambda  │────────▶│ Bedrock AdvPO   │────────▶│   S3   │
│ Function │◀────────│ (Optimization)  │         │ Bucket │
└──────────┘  poll   └─────────────────┘         └────────┘
```

## Testing

Invoke the Lambda function with a test event:

```bash
aws lambda invoke \
  --function-name <FunctionName from stack output> \
  --payload '{"promptTemplate": "Answer concisely: {{question}}", "modelId": "us.anthropic.claude-sonnet-4-20250514-v1:0"}' \
  --cli-binary-format raw-in-base64-out \
  output.json

cat output.json
```

Or use the default prompt template and samples:

```bash
aws lambda invoke \
  --function-name <FunctionName from stack output> \
  --payload '{}' \
  --cli-binary-format raw-in-base64-out \
  output.json
```

## Cleanup

```bash
cdk destroy
```

---

## Author

- Nithin Chandran R - [LinkedIn](https://www.linkedin.com/in/nithin-chandran-r/)
