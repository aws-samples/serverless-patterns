# Aurora Serverless v2 with Lambda and Amazon Bedrock

This pattern deploys an Aurora Serverless v2 PostgreSQL cluster (platform version 4) with Lambda functions that query stored knowledge and use Amazon Bedrock for AI-powered answers. Aurora Serverless v2 scales to zero when idle, making it cost-effective for agentic AI workloads.

Learn more about this pattern at Serverless Land Patterns: https://serverlessland.com/patterns/aurora-serverless-v2-lambda-bedrock-cdk

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

1. A setup Lambda creates the `knowledge` table in Aurora PostgreSQL and seeds it with sample data.
2. A query Lambda receives a question, searches Aurora for relevant context using SQL, and sends the context + question to Amazon Bedrock.
3. Bedrock (Claude Sonnet) generates an answer grounded in the database context.
4. Aurora Serverless v2 (platform version 4) automatically scales capacity based on demand and scales to zero when idle.

## Deployment

1. Clone the repository and navigate to the pattern directory:
    ```bash
    git clone https://github.com/aws-samples/serverless-patterns
    cd serverless-patterns/aurora-serverless-v2-lambda-bedrock-cdk
    ```

2. Install dependencies:
    ```bash
    npm install
    ```

3. Deploy the stack:
    ```bash
    cdk deploy
    ```

4. Seed the database:
    ```bash
    aws lambda invoke \
      --function-name $(aws cloudformation describe-stacks \
        --stack-name AuroraServerlessV2LambdaBedrockStack \
        --query 'Stacks[0].Outputs[?OutputKey==`SetupFunctionName`].OutputValue' \
        --output text) \
      --payload '{}' setup-output.json
    ```

## Testing

Query the knowledge base:

```bash
aws lambda invoke \
  --function-name $(aws cloudformation describe-stacks \
    --stack-name AuroraServerlessV2LambdaBedrockStack \
    --query 'Stacks[0].Outputs[?OutputKey==`QueryFunctionName`].OutputValue' \
    --output text) \
  --cli-binary-format raw-in-base64-out \
  --payload '{"question": "What is Aurora Serverless v2?"}' \
  output.json

cat output.json | python3 -m json.tool
```

## Cleanup

```bash
cdk destroy
```

----
Copyright 2026 Amazon.com, Inc. or its affiliates. All Rights Reserved.

SPDX-License-Identifier: MIT-0
