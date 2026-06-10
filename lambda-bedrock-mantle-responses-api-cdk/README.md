# Amazon Bedrock Mantle Responses API with AWS Lambda (OpenAI SDK Compatible)

This pattern deploys an API Gateway REST API backed by an AWS Lambda function that calls Amazon Bedrock via the OpenAI-compatible Responses API (bedrock-mantle endpoint) using the standard OpenAI Python SDK.

Learn more about this pattern at Serverless Land Patterns: https://serverlessland.com/patterns/lambda-bedrock-mantle-responses-api-cdk

Important: this application uses various AWS services and there are costs associated with these services after the Free Tier usage - please see the [AWS Pricing page](https://aws.amazon.com/pricing/) for details. You are responsible for any AWS costs incurred. No warranty is implied in this example.

## Requirements

- [Create an AWS account](https://portal.aws.amazon.com/gp/aws/developer/registration/index.html) if you do not already have one and log in. The IAM user that you use must have sufficient permissions to make necessary AWS service calls and manage AWS resources.
- [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html) installed and configured
- [Node.js 20+](https://nodejs.org/en/download/) installed
- [AWS CDK v2](https://docs.aws.amazon.com/cdk/v2/guide/getting_started.html) installed (`npm install -g aws-cdk`)
- [Python 3.12](https://www.python.org/downloads/) installed (for Lambda bundling)
- [Docker](https://docs.docker.com/get-docker/) installed (for CDK asset bundling)
- A Bedrock API key (see below)

## Generating a Bedrock API Key

1. Open the [Amazon Bedrock console](https://console.aws.amazon.com/bedrock/)
2. Navigate to **API keys** in the left navigation
3. Click **Create API key**
4. Copy the generated key — you will pass it as a parameter during deployment

## Deployment Instructions

1. Create a new directory, navigate to the directory, and clone the repository:
    ```bash
    git clone https://github.com/aws-samples/serverless-patterns
    cd serverless-patterns/lambda-bedrock-mantle-responses-api-cdk
    ```

2. Install dependencies:
    ```bash
    npm install
    ```

3. Bootstrap CDK (if not already done):
    ```bash
    cdk bootstrap
    ```

4. Deploy the stack, providing your Bedrock API key:
    ```bash
    cdk deploy --parameters BedrockApiKey=YOUR_BEDROCK_API_KEY
    ```

5. Note the `ApiEndpoint` output URL.

## How it works

- API Gateway receives a POST request at `/ask`
- Lambda is invoked with the request body
- The Lambda function uses the OpenAI Python SDK configured to point to `https://bedrock-mantle.<region>.api.aws/v1`
- Authentication is handled via the Bedrock API key (no `bedrock:InvokeModel` IAM permission needed)
- The Responses API response is returned to the caller

## Available Regions

The bedrock-mantle endpoint is available in: `us-east-1`, `us-east-2`, `us-west-2`, and other regions.

## Testing

After deployment, send a POST request to the API endpoint:

```bash
curl -X POST https://<api-id>.execute-api.<region>.amazonaws.com/prod/ask \
  -H "Content-Type: application/json" \
  -d '{"prompt": "What is Amazon Bedrock?", "model": "us.anthropic.claude-sonnet-4-20250514-v1:0"}'
```

Expected response:
```json
{
  "response": "Amazon Bedrock is a fully managed service...",
  "model": "us.anthropic.claude-sonnet-4-20250514-v1:0",
  "id": "resp_..."
}
```

## Cleanup

To delete the stack and all associated resources:

```bash
cdk destroy
```

> **Warning:** This will permanently delete all resources created by this stack. The removal policy is set to DESTROY.

## Architecture

```
Client -> API Gateway (POST /ask) -> Lambda (Python 3.12 + OpenAI SDK) -> Bedrock Mantle Responses API
```
