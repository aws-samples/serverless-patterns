# Amazon Bedrock AgentCore Gateway with Web Search Tool

This pattern deploys an Amazon Bedrock AgentCore Gateway with a managed Web Search Tool connector target and an AWS Lambda function that invokes the gateway to answer questions using live web data.

Learn more about this pattern at Serverless Land Patterns: https://serverlessland.com/patterns/agentcore-web-search-cdk

Important: this application uses various AWS services and there are costs associated with these services after the Free Tier usage - please see the [AWS Pricing page](https://aws.amazon.com/pricing/) for details. You are responsible for any AWS costs incurred. No warranty is implied in this example.

## Requirements

* [Create an AWS account](https://portal.aws.amazon.com/gp/aws/developer/registration/index.html) if you do not already have one and log in. The IAM user that you use must have sufficient permissions to make necessary AWS service calls and manage AWS resources.
* [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html) installed and configured
* [Node.js 18+](https://nodejs.org/en/download/) installed
* [AWS CDK v2](https://docs.aws.amazon.com/cdk/v2/guide/getting-started.html) installed

## Architecture

1. **Amazon Bedrock AgentCore Gateway** - Hosts the Web Search Tool as a connector target with IAM authorization
2. **Web Search Tool Connector** - A managed connector that provides live web search capabilities without external API keys
3. **AWS Lambda Function** - Invokes the gateway to perform web searches and return results

## Deployment Instructions

1. Install dependencies:
   ```bash
   npm install
   ```

2. Build the project:
   ```bash
   npx tsc
   ```

3. Deploy the stack (us-east-1 only):
   ```bash
   npx cdk deploy
   ```

## How it works

The Amazon Bedrock AgentCore Gateway provides a unified connectivity layer between agents and tools. The Web Search Tool is a managed connector (`web-search`) that lets agents retrieve information from the live web without any external search service API keys or infrastructure.

The AWS Lambda function demonstrates invoking the gateway's web search tool by calling the `invoke_tool` API with a query string (max 200 characters) and optional `maxResults` parameter (1-25).

## Testing

After deployment, invoke the AWS Lambda function:

```bash
aws lambda invoke \
  --function-name <FunctionName from stack output> \
  --payload '{"query": "What is Amazon Bedrock AgentCore?"}' \
  --cli-binary-format raw-in-base64-out \
  output.json && cat output.json
```

You can also pass `maxResults` (1-25) in the event payload to control the number of search results returned.

## Cleanup

```bash
npx cdk destroy
```

## Author

* **Nithin Chandran R** - [LinkedIn](https://www.linkedin.com/in/nithin-chandran-r/)

----
Copyright 2024 Amazon.com, Inc. or its affiliates. All Rights Reserved.

SPDX-License-Identifier: MIT-0
