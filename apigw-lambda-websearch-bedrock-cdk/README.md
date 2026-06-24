# Grounded AI Answers with Amazon Bedrock AgentCore Web Search and Amazon Bedrock (CDK)

This pattern deploys an Amazon API Gateway REST API backed by an AWS Lambda function that searches the live web via Amazon Bedrock AgentCore Web Search, then uses Amazon Bedrock to synthesize accurate, cited answers grounded in current facts.

Learn more about this pattern at Serverless Land Patterns: https://serverlessland.com/patterns/apigw-lambda-websearch-bedrock-cdk

Important: this application uses various AWS services and there are costs associated with these services after the Free Tier usage - please see the [AWS Pricing page](https://aws.amazon.com/pricing/) for details.

## Requirements

* [Create an AWS account](https://portal.aws.amazon.com/gp/aws/developer/registration/index.html) if you do not already have one and log in.
* [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html) installed and configured
* [Node.js 20+](https://nodejs.org/en/download/) installed
* [AWS CDK v2](https://docs.aws.amazon.com/cdk/v2/guide/getting_started.html) installed (`npm install -g aws-cdk`)
* CDK bootstrapped in your account/region (`cdk bootstrap`)
* Amazon Bedrock model access enabled for Claude Sonnet 4 in us-east-1

## Deployment Instructions

1. Navigate to the pattern directory:
    ```bash
    cd apigw-lambda-websearch-bedrock-cdk
    ```

2. Install dependencies:
    ```bash
    npm install
    ```

3. Deploy:
    ```bash
    npx cdk deploy
    ```

## How it works

This pattern demonstrates **Retrieval-Augmented Generation (RAG) using live web data** instead of a static vector database:

1. **Amazon API Gateway** receives user questions via POST /ask
2. **AWS Lambda** orchestrates the two-step process:
   - Searches the live web via Amazon Bedrock AgentCore Gateway's Web Search connector (MCP protocol + SigV4)
   - Passes search results as context to Amazon Bedrock (Claude Sonnet 4) for inference
3. **Amazon Bedrock** synthesizes a grounded answer with numbered citation references
4. Response includes the answer text and source URLs for verification

This eliminates the need for maintaining a vector database, embedding pipeline, or data ingestion — the web IS the knowledge base, always current.

## Testing

```bash
curl -X POST https://YOUR_API_ID.execute-api.us-east-1.amazonaws.com/prod/ask \
  -H "Content-Type: application/json" \
  -d '{"question": "What was announced at AWS Summit NYC 2026?"}'
```

Or via AWS Lambda directly:
```bash
aws lambda invoke --function-name FUNCTION_NAME \
  --payload '{"body": "{\"question\": \"What is Amazon Aurora DSQL?\"}"}' \
  --cli-binary-format raw-in-base64-out output.json && cat output.json
```

## Example Response

```json
{
  "answer": "Amazon Aurora DSQL is a serverless, distributed SQL database [1] that provides active-active multi-region support with PostgreSQL compatibility [2]...",
  "sources": [
    {"title": "Amazon Aurora DSQL documentation", "url": "https://docs.aws.amazon.com/aurora-dsql/..."},
    {"title": "Aurora DSQL launch blog", "url": "https://aws.amazon.com/blogs/..."}
  ]
}
```

## Cleanup

```bash
npx cdk destroy
```

---

Copyright 2026 Amazon.com, Inc. or its affiliates. All Rights Reserved.

SPDX-License-Identifier: MIT-0
