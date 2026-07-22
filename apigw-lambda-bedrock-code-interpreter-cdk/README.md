# AI Data Analyst with Amazon Bedrock and Amazon Bedrock AgentCore Code Interpreter

This pattern deploys an Amazon API Gateway REST API backed by an AWS Lambda function that uses Amazon Bedrock to generate Python analysis code from natural language questions, then executes it safely in Amazon Bedrock AgentCore Code Interpreter.

Learn more about this pattern at Serverless Land Patterns: https://serverlessland.com/patterns/apigw-lambda-bedrock-code-interpreter-cdk

Important: this application uses various AWS services and there are costs associated with these services after the Free Tier usage - please see the [AWS Pricing page](https://aws.amazon.com/pricing/) for details. You are responsible for any AWS costs incurred. No warranty is implied in this example.

## Requirements

* [Create an AWS account](https://portal.aws.amazon.com/gp/aws/developer/registration/index.html) if you do not already have one and log in. The IAM user that you use must have sufficient permissions to make necessary AWS service calls and manage AWS resources.
* [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html) installed and configured
* [Node.js 20+](https://nodejs.org/en/download/) installed
* [AWS CDK v2](https://docs.aws.amazon.com/cdk/v2/guide/getting_started.html) installed (`npm install -g aws-cdk`)
* [Git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git) installed
* [Amazon Bedrock model access](https://docs.aws.amazon.com/bedrock/latest/userguide/model-access.html) enabled for Anthropic Claude Sonnet in your target region

## Architecture

```
Client (POST /analyze) → Amazon API Gateway → AWS Lambda → Amazon Bedrock (generates Python code)
                                                          → Amazon Bedrock AgentCore Code Interpreter (executes code safely)
                                                          → Response (results + generated code)
```

## How it works

1. A user submits a data analysis question in natural language via `POST /analyze`.
2. The AWS Lambda function sends the question to Amazon Bedrock (Claude Sonnet), which generates Python code to answer it.
3. The generated code is executed in Amazon Bedrock AgentCore Code Interpreter — a sandboxed environment with no access to the host system.
4. Results are returned to the user along with the generated code for transparency.

Neither Amazon Bedrock nor Amazon Bedrock AgentCore Code Interpreter alone can solve this problem. Amazon Bedrock generates code but cannot execute it. Code Interpreter executes code but cannot reason about what to write. The composition of both services is what creates the value.

## Deployment Instructions

1. Clone the repository:
    ```bash
    git clone https://github.com/aws-samples/serverless-patterns
    cd serverless-patterns/apigw-lambda-bedrock-code-interpreter-cdk
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

Invoke the API with a natural language data question:

```bash
curl -X POST $(aws cloudformation describe-stacks \
  --stack-name ApigwLambdaBedrockCodeInterpreterStack \
  --query 'Stacks[0].Outputs[?contains(OutputKey,`Endpoint`)].OutputValue' \
  --output text)analyze \
  -H "Content-Type: application/json" \
  -d '{"question": "Calculate the compound interest on $10,000 at 5% annual rate over 10 years"}'
```

Expected output includes the generated Python code and the computed result.

## Cleanup

```bash
cdk destroy
```

**Warning:** This will delete all resources including the Amazon Bedrock AgentCore Code Interpreter sandbox. This action cannot be undone.

----
Copyright 2026 Amazon.com, Inc. or its affiliates. All Rights Reserved.

SPDX-License-Identifier: MIT-0
