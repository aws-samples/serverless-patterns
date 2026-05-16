# API Gateway to Lambda to Amazon Bedrock with Application-Level Guardrails

This pattern deploys a REST API that invokes Amazon Bedrock with **per-request Guardrails** — content and topic filtering applied at the application level on each individual API call.

> **Application-level vs Account-level:** This pattern applies guardrails per-request by passing `guardrailIdentifier` and `guardrailVersion` in each InvokeModel call. This gives you fine-grained control — different APIs can use different guardrails, or skip them entirely. For account-wide enforcement that applies to ALL Bedrock calls automatically, see the [bedrock-guardrails-cross-account-cdk](../bedrock-guardrails-cross-account-cdk) pattern.

Learn more about this pattern at Serverless Land Patterns: https://serverlessland.com/patterns/apigw-lambda-bedrock-guardrails-cdk

Important: this application uses various AWS services and there are costs associated with these services after the Free Tier usage - please see the [AWS Pricing page](https://aws.amazon.com/pricing/) for details.

## Requirements

- [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html) installed and configured
- [AWS CDK](https://docs.aws.amazon.com/cdk/latest/guide/cli.html) installed
- [Node.js](https://nodejs.org/) 20.x or later
- [Amazon Bedrock model access](https://docs.aws.amazon.com/bedrock/latest/userguide/model-access.html) enabled for a model of your choice in your AWS account

## How it works

1. Client sends a POST request to API Gateway with a `prompt` field
2. Lambda invokes Bedrock InvokeModel with `guardrailIdentifier` and `guardrailVersion` parameters
3. Bedrock evaluates the input against content filters (sexual, violence, hate, insults, misconduct) and topic filters (financial advice)
4. If the guardrail triggers, the response contains the blocked message — no model tokens consumed
5. If the guardrail passes, the model generates a response normally

## Deployment

```bash
cd apigw-lambda-bedrock-guardrails-cdk
npm install
cdk deploy
```

## Testing

```bash
API_URL=$(aws cloudformation describe-stacks \
  --stack-name ApigwLambdaBedrockGuardrailsStack \
  --query 'Stacks[0].Outputs[?OutputKey==`ApiEndpoint`].OutputValue' --output text)

# Safe prompt — should pass guardrails
curl -X POST "$API_URL" -H "Content-Type: application/json" \
  -d '{"prompt": "What is Amazon S3?"}'

# Blocked prompt — triggers topic filter (financial advice)
curl -X POST "$API_URL" -H "Content-Type: application/json" \
  -d '{"prompt": "What stocks should I buy for maximum returns in 2026?"}'
```

Expected: The first request returns a normal Bedrock response. The second returns the blocked message with `guardrailAction: "GUARDRAIL_INTERVENED"`.

## Cleanup

```bash
cdk destroy
```

---

Copyright 2026 Amazon.com, Inc. or its affiliates. All Rights Reserved.

SPDX-License-Identifier: MIT-0
