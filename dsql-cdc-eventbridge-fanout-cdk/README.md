# Amazon Aurora DSQL CDC to Amazon EventBridge

This pattern deploys an event-driven pipeline that captures real-time database changes from Amazon Aurora DSQL using Change Data Capture (CDC), streams them through Amazon Kinesis Data Streams, processes them with AWS Lambda, and publishes typed events to an Amazon EventBridge custom event bus for downstream consumption.

Learn more about this pattern at Serverless Land Patterns: https://serverlessland.com/patterns/dsql-cdc-eventbridge-fanout-cdk

Important: this application uses various AWS services and there are costs associated with these services after the Free Tier usage - please see the [AWS Pricing page](https://aws.amazon.com/pricing/) for details.

## Architecture

```
┌──────────────────┐     ┌─────────────────────┐     ┌──────────────────────┐     ┌─────────────────────┐
│ Amazon Aurora    │────▶│ Amazon Kinesis Data  │────▶│ AWS Lambda           │────▶│ Amazon EventBridge   │
│ DSQL (CDC)       │     │ Streams              │     │ (CDC Processor)      │     │ (Custom Bus)         │
└──────────────────┘     └─────────────────────┘     └──────────────────────┘     └─────────────────────┘
```

**How it works:**

1. Amazon Aurora DSQL captures every committed row-level change (INSERT, UPDATE, DELETE) and delivers it as a structured JSON record to Amazon Kinesis Data Streams.
2. AWS Lambda consumes the Amazon Kinesis stream, parses the CDC payload (Debezium-style op codes), classifies the operation type, and publishes typed events to an Amazon EventBridge custom event bus.
3. Amazon EventBridge receives events with source `dsql.cdc` and detail-type `INSERT`, `UPDATE`, or `DELETE`. Add your own rules and targets to route events to any downstream consumer.

## Requirements

- [AWS CDK v2](https://docs.aws.amazon.com/cdk/v2/guide/getting_started.html) installed and configured
- [Node.js 20+](https://nodejs.org/) with npm
- AWS account [bootstrapped for CDK](https://docs.aws.amazon.com/cdk/v2/guide/bootstrapping.html)
- An existing Amazon Aurora DSQL cluster
- Python 3.12 (for AWS Lambda functions)

## Deployment

1. Create an Amazon Aurora DSQL cluster (if you don't have one):

    ```bash
    aws dsql create-cluster --region us-east-1
    ```

    Note the `identifier` from the response.

2. Install dependencies and build:

    ```bash
    cd dsql-cdc-eventbridge-fanout-cdk/cdk
    npm install
    npm run build
    ```

3. Deploy the stack:

    ```bash
    npx cdk deploy --parameters DsqlClusterId=<your-cluster-id>
    ```

## Testing

After deploying, insert data into your Amazon Aurora DSQL cluster to trigger CDC events:

```sql
CREATE TABLE orders (
  id UUID DEFAULT gen_random_uuid() PRIMARY KEY,
  customer_name TEXT NOT NULL,
  amount DECIMAL(10,2),
  created_at TIMESTAMP DEFAULT now()
);

INSERT INTO orders (customer_name, amount) VALUES ('Acme Corp', 1250.00);
UPDATE orders SET amount = 1500.00 WHERE customer_name = 'Acme Corp';
DELETE FROM orders WHERE customer_name = 'Acme Corp';
```

Then verify events arrive on the custom event bus by adding a temporary rule:

```bash
aws events put-rule \
  --name test-cdc-rule \
  --event-bus-name dsql-cdc-events \
  --event-pattern '{"source": ["dsql.cdc"]}'
```

## Extending This Pattern

Add Amazon EventBridge rules and targets to route CDC events to any consumer:

- Route ALL changes to Amazon SQS for audit
- Route INSERT events to AWS Step Functions for validation
- Route DELETE events to Amazon SNS for alerting

## Cleanup

> **Warning:** This will delete all resources. The Amazon Aurora DSQL cluster is NOT deleted (it was created externally).

```bash
npx cdk destroy
```

## Services Used

| Service | Role |
|---------|------|
| Amazon Aurora DSQL | Source database with CDC enabled |
| Amazon Kinesis Data Streams | Receives CDC event stream from Amazon Aurora DSQL |
| AWS Lambda | Processes CDC events, classifies operations, publishes to Amazon EventBridge |
| Amazon EventBridge | Custom event bus for content-based routing of CDC events |

----
Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
SPDX-License-Identifier: MIT-0
