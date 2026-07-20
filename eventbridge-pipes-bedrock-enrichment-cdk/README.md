# Amazon EventBridge Pipes with Amazon Bedrock AI Enrichment

This pattern deploys an Amazon EventBridge Pipe that enriches messages in-flight using Amazon Bedrock before delivering them to the target. Messages from Amazon SQS are passed through an AWS Lambda enrichment function that calls Amazon Bedrock to classify sentiment, extract entities, and generate summaries — then writes the enriched data to Amazon DynamoDB.

Important: This is the first serverless pattern combining Amazon EventBridge Pipes with Amazon Bedrock. While 48+ Pipes patterns exist in this repo, none use AI/ML enrichment. This pattern demonstrates how to add real-time AI processing to any event pipeline without changing source or target configurations.

Learn more about this pattern at Serverless Land Patterns: https://serverlessland.com/patterns/eventbridge-pipes-bedrock-enrichment-cdk

## Architecture

```
┌──────────────┐     ┌─────────────────────────────────────────────┐     ┌──────────────────┐
│ Amazon SQS   │────▶│ Amazon EventBridge Pipe                      │────▶│ Amazon DynamoDB  │
│ (Source)     │     │                                             │     │ (Enriched Data)  │
└──────────────┘     │  ┌─────────────────────────────────────┐   │     └──────────────────┘
                     │  │ AWS Lambda (Enrichment)              │   │
                     │  │  → Amazon Bedrock (Claude Sonnet 4.6)│   │
                     │  │  → Classify sentiment                │   │
                     │  │  → Extract entities                  │   │
                     │  │  → Generate summary                  │   │
                     │  └─────────────────────────────────────┘   │
                     └─────────────────────────────────────────────┘
```

**How it works:**

1. Messages arrive in the Amazon SQS source queue (any format — customer feedback, support tickets, log entries)
2. Amazon EventBridge Pipes reads the message and invokes the AWS Lambda enrichment function
3. The enrichment function calls Amazon Bedrock (Claude Sonnet 4.6) to classify sentiment, extract named entities, and generate a one-line summary
4. The enriched message (original + sentiment + entities + summary) is written to Amazon DynamoDB

**Use cases:** Real-time sentiment analysis on customer feedback, automated ticket classification, log enrichment with AI context, content moderation pipelines.

## Requirements

- [AWS CDK v2](https://docs.aws.amazon.com/cdk/v2/guide/getting_started.html) installed and configured
- [Node.js 20+](https://nodejs.org/) with npm
- AWS account [bootstrapped for CDK](https://docs.aws.amazon.com/cdk/v2/guide/bootstrapping.html)
- Amazon Bedrock model access enabled for Claude Sonnet 4.6
- Python 3.12 (for AWS Lambda functions)

## Deployment

```bash
cd eventbridge-pipes-bedrock-enrichment-cdk/cdk
npm install
npx cdk deploy
```

## Testing

### Send a test message to Amazon SQS

```bash
QUEUE_URL=$(aws cloudformation describe-stacks \
  --stack-name EventbridgePipesBedrockEnrichmentStack \
  --query 'Stacks[0].Outputs[?OutputKey==`SourceQueueUrl`].OutputValue' \
  --output text)

aws sqs send-message \
  --queue-url "$QUEUE_URL" \
  --message-body '{"message": "I absolutely love the new feature you released! The AI suggestions save me hours every week. Your team is doing amazing work."}'
```

### Check enriched results in Amazon DynamoDB

```bash
TABLE_NAME=$(aws cloudformation describe-stacks \
  --stack-name EventbridgePipesBedrockEnrichmentStack \
  --query 'Stacks[0].Outputs[?OutputKey==`EnrichedTableName`].OutputValue' \
  --output text)

aws dynamodb scan --table-name "$TABLE_NAME" --query 'Items[0]'
```

Expected output includes: `sentiment: POSITIVE`, `entities: ["AI"]`, `summary: "Customer praising new AI feature..."`.

## Cleanup

> **Warning:** This will delete the Amazon DynamoDB table and all enriched data.

```bash
cd eventbridge-pipes-bedrock-enrichment-cdk/cdk
npx cdk destroy
```

## Services Used

| Service | Role |
|---------|------|
| Amazon SQS | Source queue — receives raw messages |
| Amazon EventBridge Pipes | Orchestrates source → enrichment → target flow |
| AWS Lambda | Enrichment step — calls Amazon Bedrock |
| Amazon Bedrock | AI classification, entity extraction, summarization |
| Amazon DynamoDB | Target — stores enriched messages with AI metadata |

----
Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
SPDX-License-Identifier: MIT-0
