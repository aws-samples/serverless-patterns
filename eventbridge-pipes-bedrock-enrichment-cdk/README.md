# Amazon EventBridge Pipes with Amazon Bedrock AI Enrichment

This pattern deploys an Amazon EventBridge Pipe that enriches messages in-flight using Amazon Bedrock before delivering them to the target. Messages from Amazon SQS pass through an AWS Lambda enrichment function that calls Amazon Bedrock to classify sentiment, extract entities, and generate summaries. The Pipe target is Amazon CloudWatch Logs, where the enriched output is delivered. The enrichment function also persists each enriched record to Amazon DynamoDB for downstream querying and analytics.

Learn more about this pattern at Serverless Land Patterns: https://serverlessland.com/patterns/eventbridge-pipes-bedrock-enrichment-cdk

## Architecture

```
┌──────────────┐     ┌─────────────────────────────────────────────┐     ┌────────────────────────┐
│ Amazon SQS   │────▶│ Amazon EventBridge Pipe                       │────▶│ Amazon CloudWatch Logs │
│ (Source)     │     │                                               │     │ (Target)               │
└──────────────┘     │  ┌─────────────────────────────────────┐      │     └────────────────────────┘
                     │  │ AWS Lambda (Enrichment)              │      │
                     │  │  → Amazon Bedrock (Claude Sonnet 4.6)│      │
                     │  │  → Classify sentiment                │      │
                     │  │  → Extract entities                  │      │              ┌──────────────────┐
                     │  │  → Generate summary                  │──────┼─────────────▶│ Amazon DynamoDB  │
                     │  └─────────────────────────────────────┘      │              │ (Enriched Store) │
                     └─────────────────────────────────────────────┘               └──────────────────┘
```

**How it works:**

1. Messages arrive in the Amazon SQS source queue (any format — customer feedback, support tickets, log entries)
2. Amazon EventBridge Pipes reads the message and invokes the AWS Lambda enrichment function
3. The enrichment function calls Amazon Bedrock (Claude Sonnet 4.6) to classify sentiment, extract named entities, and generate a one-line summary
4. The Pipe delivers the enriched message to the target, Amazon CloudWatch Logs
5. In parallel, the enrichment function writes each enriched record (original + sentiment + entities + summary) to Amazon DynamoDB for persistent storage and querying

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

### Check the enriched output in Amazon CloudWatch Logs (Pipe target)

```bash
aws logs tail /pipes/bedrock-enriched-output --since 5m --format short
```

The Pipe delivers the enriched records to the `/pipes/bedrock-enriched-output` log group. Each entry includes `sentiment`, `entities`, and `summary`.

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
| Amazon CloudWatch Logs | Target — receives the enriched output from the Pipe |
| Amazon DynamoDB | Persistent store — enriched messages with AI metadata for querying |

----
Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
SPDX-License-Identifier: MIT-0
