# Amazon Aurora DSQL CDC to Amazon EventBridge Fan-out

This pattern deploys an event-driven fan-out architecture that captures real-time database changes from Amazon Aurora DSQL using Change Data Capture (CDC), streams them through Amazon Kinesis Data Streams, processes them with AWS Lambda, and routes them to multiple consumers via Amazon EventBridge.

Important: This pattern is fundamentally different from the existing `apigw-lambda-dsql` pattern (basic CRUD) and the standalone [sample-aurora-dsql-cdc-demo](https://github.com/aws-samples/sample-aurora-dsql-cdc-demo) (RAG/semantic search chatbot). This pattern demonstrates **event-driven microservices fan-out** — using Amazon Aurora DSQL CDC as a change event source to drive multiple independent downstream workflows through Amazon EventBridge content-based routing.

Learn more about this pattern at Serverless Land Patterns: https://serverlessland.com/patterns/dsql-cdc-eventbridge-fanout-cdk

## Architecture

```
┌──────────────┐     ┌─────────────────────┐     ┌──────────────────────┐     ┌─────────────────────┐
│ Amazon Aurora │────▶│ Amazon Kinesis Data  │────▶│ AWS Lambda           │────▶│ Amazon EventBridge   │
│ DSQL (CDC)   │     │ Streams              │     │ (CDC Processor)      │     │ (Custom Bus)         │
└──────────────┘     └─────────────────────┘     └──────────────────────┘     └──────────┬──────────┘
                                                                                          │
                              ┌────────────────────────────────────────────────────────────┼───────────────────┐
                              │                                                           │                   │
                              ▼                                                           ▼                   ▼
                   ┌──────────────────┐                                      ┌─────────────────┐   ┌──────────────┐
                   │ Amazon SQS       │                                      │ AWS Step         │   │ Amazon SNS   │
                   │ (Audit Queue)    │                                      │ Functions        │   │ (Alerts)     │
                   │ ALL events       │                                      │ INSERT events    │   │ DELETE events │
                   └──────────────────┘                                      └─────────────────┘   └──────────────┘
```

**How it works:**

1. Amazon Aurora DSQL captures every committed row-level change (INSERT, UPDATE, DELETE) and delivers it as a structured JSON record to Amazon Kinesis Data Streams
2. AWS Lambda consumes the Amazon Kinesis stream, parses the CDC payload, classifies the operation type, and publishes typed events to an Amazon EventBridge custom event bus
3. Amazon EventBridge routes events to three independent consumers based on content:
   - **ALL changes** → Amazon SQS audit queue (compliance/audit trail)
   - **INSERT events** → AWS Step Functions workflow (data validation)
   - **DELETE events** → Amazon SNS topic (real-time alerting)

## Requirements

- [AWS CDK v2](https://docs.aws.amazon.com/cdk/v2/guide/getting_started.html) installed and configured
- [Node.js 20+](https://nodejs.org/) with npm
- AWS account [bootstrapped for CDK](https://docs.aws.amazon.com/cdk/v2/guide/bootstrapping.html)
- An existing Amazon Aurora DSQL cluster (see Deployment section)
- Python 3.12 (for AWS Lambda functions)

## Deployment

### Step 1: Create an Amazon Aurora DSQL cluster (if you don't have one)

```bash
aws dsql create-cluster --region us-east-1
```

Note the `identifier` from the response — you'll need it in Step 3.

### Step 2: Install dependencies and synthesize

```bash
cd dsql-cdc-eventbridge-fanout-cdk/cdk
npm install
npx cdk synth
```

### Step 3: Deploy the stack

```bash
npx cdk deploy --parameters DsqlClusterId=<your-cluster-id>
```

Replace `<your-cluster-id>` with your Amazon Aurora DSQL cluster identifier.

### Step 4: Insert data to trigger CDC events

Connect to your Amazon Aurora DSQL cluster and insert data:

```sql
CREATE TABLE orders (
  id UUID DEFAULT gen_random_uuid() PRIMARY KEY,
  customer_name TEXT NOT NULL,
  amount DECIMAL(10,2),
  created_at TIMESTAMP DEFAULT now()
);

INSERT INTO orders (customer_name, amount) VALUES ('Acme Corp', 1250.00);
INSERT INTO orders (customer_name, amount) VALUES ('Globex Inc', 780.50);
DELETE FROM orders WHERE customer_name = 'Globex Inc';
```

## Testing

After deploying, verify the fan-out is working:

### 1. Check Amazon SQS audit queue (receives ALL events)

```bash
aws sqs receive-message \
  --queue-url $(aws cloudformation describe-stacks \
    --stack-name DsqlCdcEventbridgeFanoutStack \
    --query 'Stacks[0].Outputs[?OutputKey==`AuditQueueUrl`].OutputValue' \
    --output text) \
  --max-number-of-messages 5
```

### 2. Check AWS Step Functions executions (INSERT events only)

```bash
aws stepfunctions list-executions \
  --state-machine-arn $(aws cloudformation describe-stacks \
    --stack-name DsqlCdcEventbridgeFanoutStack \
    --query 'Stacks[0].Outputs[?OutputKey==`ValidationStateMachineArn`].OutputValue' \
    --output text) \
  --max-results 5
```

### 3. Subscribe to Amazon SNS topic to receive DELETE alerts

```bash
aws sns subscribe \
  --topic-arn $(aws cloudformation describe-stacks \
    --stack-name DsqlCdcEventbridgeFanoutStack \
    --query 'Stacks[0].Outputs[?OutputKey==`AlertTopicArn`].OutputValue' \
    --output text) \
  --protocol email \
  --notification-endpoint your-email@example.com
```

## Cleanup

> **Warning:** This will delete all resources including the Amazon SQS queues and their messages. The Amazon Aurora DSQL cluster is NOT deleted (it was created externally).

```bash
cd dsql-cdc-eventbridge-fanout-cdk/cdk
npx cdk destroy
```

## Services Used

| Service | Role |
|---------|------|
| Amazon Aurora DSQL | Source database with CDC enabled |
| Amazon Kinesis Data Streams | Receives CDC event stream from Amazon Aurora DSQL |
| AWS Lambda | Processes CDC events, classifies operations, publishes to Amazon EventBridge |
| Amazon EventBridge | Content-based routing of CDC events to multiple consumers |
| Amazon SQS | Audit queue for all change events (compliance) |
| AWS Step Functions | Data validation workflow for INSERT events |
| Amazon SNS | Real-time alerting for DELETE events |

----
Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
SPDX-License-Identifier: MIT-0
