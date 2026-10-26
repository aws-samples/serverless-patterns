# Amazon Aurora DSQL CDC to Amazon EventBridge

This pattern deploys an event-driven pipeline that captures real-time database changes from Amazon Aurora DSQL using Change Data Capture (CDC), streams them through Amazon Kinesis Data Streams, processes them with AWS Lambda, and publishes typed events to an Amazon EventBridge custom event bus for downstream consumption.

Learn more about this pattern at Serverless Land Patterns: https://serverlessland.com/patterns/dsql-cdc-eventbridge-fanout-cdk

Important: this application uses various AWS services and there are costs associated with these services after the Free Tier usage - please see the [AWS Pricing page](https://aws.amazon.com/pricing/) for details. Amazon Aurora DSQL and Amazon Kinesis Data Streams bill while they exist, so run the Cleanup section when you are done. You are responsible for any AWS costs incurred. No warranty is implied in this example.

## Architecture

```
┌──────────────────┐     ┌─────────────────────┐     ┌──────────────────────┐     ┌─────────────────────┐
│ Amazon Aurora    │────▶│ Amazon Kinesis Data  │────▶│ AWS Lambda           │────▶│ Amazon EventBridge   │
│ DSQL (CDC)       │     │ Streams              │     │ (CDC Processor)      │     │ (Custom Bus)         │
└──────────────────┘     └─────────────────────┘     └──────────────────────┘     └─────────────────────┘
```

**How it works:**

1. Amazon Aurora DSQL emits one record per row with a net change per transaction (write-set compaction) to Amazon Kinesis Data Streams. Delivery is at-least-once and unordered, so consumers must de-duplicate and handle out-of-order events (use `txId`, `recordId` and the commit timestamp included in `detail`). `oldImage` contains only the primary-key columns, and only for DELETE events; it is null for INSERT and UPDATE.
2. AWS Lambda reads the records from Amazon Kinesis Data Streams, parses the CDC payload (Debezium-style op codes), classifies the operation type, and publishes typed events to an Amazon EventBridge custom event bus.
3. Amazon EventBridge receives events with source `dsql.cdc` and detail-type `INSERT`, `UPDATE`, or `DELETE`. The `detail` holds `tableName`, `operation`, `newImage`, `oldImage`, `txId`, `recordId`, `timestamp` (commit time in milliseconds), `commitTimestampNs` (commit time in nanoseconds, as a string) and `sequenceNumber`. Add your own rules and targets to route events to any downstream consumer.

## Requirements

- [Create an AWS account](https://portal.aws.amazon.com/gp/aws/developer/registration/index.html) if you do not already have one and log in.
- [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html) installed and configured
- [Git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git) installed
- [Node.js 22+](https://nodejs.org/) with npm
- [AWS CDK v2](https://docs.aws.amazon.com/cdk/v2/guide/getting_started.html) installed, and the account and Region [bootstrapped for CDK](https://docs.aws.amazon.com/cdk/v2/guide/bootstrapping.html) (`cdk bootstrap`)
- Docker running (or Finch with `CDK_DOCKER=finch`): CDK builds the Python dependencies of the custom resource in a container
- A PostgreSQL client (`psql`) to run the SQL in the Testing section

## Important Notes

- The Amazon Aurora DSQL cluster, the stream in Amazon Kinesis Data Streams, the AWS Identity and Access Management (IAM) role and the stack must be in the same AWS account and Region.
- Amazon Aurora DSQL creates a CDC stream only for a cluster in ACTIVE status. If an existing cluster is idle, connect to it once with `psql` (see Testing) before you deploy.
- The stack creates the stream in Amazon Kinesis Data Streams in on-demand mode with a 10 MiB maximum record size, as the [Aurora DSQL CDC guide](https://docs.aws.amazon.com/aurora-dsql/latest/userguide/cdc-streams.html) recommends.
- Records larger than 9 MiB are split into chunked and fragment records. The processor publishes `full` records only and logs the others, so those rows are not delivered to the event bus. An Amazon EventBridge `PutEvents` entry must be smaller than 1 MB ([API reference](https://docs.aws.amazon.com/eventbridge/latest/APIReference/API_PutEvents.html)), so this pattern does not handle rows of that size.
- The Amazon Kinesis Data Streams event source has no on-failure destination: a batch that still fails after 3 retries is discarded. Add an `onFailure` destination, for example an Amazon SQS queue, before you use this beyond a demo.
- The stack keeps the AWS Lambda logs for one week. `cdk destroy` removes the log groups, the stream in Amazon Kinesis Data Streams and the CDC stream, except that the log group of the custom resource provider can reappear (Cleanup step 4).
- Deployed and tested in `us-west-2` only.

## Deployment

1. Clone the repository and change to the pattern folder:

    ```bash
    git clone https://github.com/aws-samples/serverless-patterns
    cd serverless-patterns/dsql-cdc-eventbridge-fanout-cdk
    ```

2. Create an Amazon Aurora DSQL cluster (if you don't have one) in the Region you deploy to, and wait until it is ACTIVE:

    ```bash
    export AWS_REGION=us-west-2
    export CLUSTER_ID=$(aws dsql create-cluster --query identifier --output text)
    aws dsql wait cluster-active --identifier $CLUSTER_ID
    ```

3. Install dependencies, type-check and deploy (about 2 to 3 minutes):

    ```bash
    cd cdk
    npm install
    npm run build
    npx cdk deploy --parameters DsqlClusterId=$CLUSTER_ID
    ```

## Testing

If you opened a new shell, set `AWS_REGION` and `CLUSTER_ID` again first (`aws dsql list-clusters` shows the identifiers).

1. Create a temporary rule on the custom event bus that sends every CDC event to a temporary Amazon SQS queue:

    ```bash
    ACCOUNT_ID=$(aws sts get-caller-identity --query Account --output text)
    RULE_ARN=$(aws events put-rule --name dsql-cdc-test --event-bus-name dsql-cdc-events \
      --event-pattern '{"source": ["dsql.cdc"]}' --query RuleArn --output text)
    cat > /tmp/queue-attributes.json <<EOF
    {"Policy": "{\"Version\":\"2012-10-17\",\"Statement\":[{\"Effect\":\"Allow\",\"Principal\":{\"Service\":\"events.amazonaws.com\"},\"Action\":\"sqs:SendMessage\",\"Resource\":\"arn:aws:sqs:$AWS_REGION:$ACCOUNT_ID:dsql-cdc-test\",\"Condition\":{\"ArnEquals\":{\"aws:SourceArn\":\"$RULE_ARN\"}}}]}"}
    EOF
    export QUEUE_URL=$(aws sqs create-queue --queue-name dsql-cdc-test \
      --attributes file:///tmp/queue-attributes.json --query QueueUrl --output text)
    aws events put-targets --rule dsql-cdc-test --event-bus-name dsql-cdc-events \
      --targets "Id=1,Arn=arn:aws:sqs:$AWS_REGION:$ACCOUNT_ID:dsql-cdc-test"
    ```

2. Connect to the cluster with `psql` and run the SQL. Run the SQL as separate statements: each `INSERT`, `UPDATE` and `DELETE` is its own transaction and produces one CDC record (`CREATE TABLE` produces none). The token from `generate-db-connect-admin-auth-token` is valid for 15 minutes by default; run the three `export` lines again if `psql` rejects it:

    ```bash
    export ENDPOINT=$CLUSTER_ID.dsql.$AWS_REGION.on.aws
    export PGPASSWORD=$(aws dsql generate-db-connect-admin-auth-token --hostname $ENDPOINT)
    export PGSSLMODE=require
    psql --username admin --dbname postgres --host $ENDPOINT
    ```

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

3. Read the events from the queue. Run the command again until you see three events (INSERT, UPDATE, DELETE); `None` means that no message has arrived yet. Amazon SQS standard queues do not preserve order and return a message again after the visibility timeout unless you delete it:

    ```bash
    aws sqs receive-message --queue-url $QUEUE_URL --max-number-of-messages 10 \
      --wait-time-seconds 20 --query 'Messages[].Body' --output text
    ```

    Each message is an Amazon EventBridge event. The `detail` of the DELETE event looks like this (`oldImage` has the primary key only, `newImage` is null):

    ```json
    {
      "tableName": "orders",
      "operation": "DELETE",
      "newImage": null,
      "oldImage": { "id": "28dbeb81-2667-454a-96b9-ab245b1255b9" },
      "txId": "avuf3nwkbv2hjulndlyfe3phvi",
      "recordId": "dd1b7d8c7de133532cdbaf7dace0832d",
      "timestamp": 1792995436605,
      "commitTimestampNs": "1792995436605540491",
      "sequenceNumber": "49679619397596771748604543873390443667452088216532811826"
    }
    ```

    The INSERT and UPDATE events carry the full row in `newImage` and `null` in `oldImage`. Two rows written in one transaction arrive as two events with the same `txId` and different `recordId` values.

4. To see what the processor did, read its log group. The name is in the `CdcProcessorLogGroup` stack output:

    ```bash
    LOG_GROUP=$(aws cloudformation describe-stacks --stack-name DsqlCdcEventbridgeFanoutStack \
      --query "Stacks[0].Outputs[?OutputKey=='CdcProcessorLogGroup'].OutputValue" --output text)
    aws logs tail $LOG_GROUP --since 15m
    ```

    A successful batch logs a line such as `Processed 1 records, published 1 events, 0 failures`.

## Extending This Pattern

Add Amazon EventBridge rules and targets to route CDC events to any consumer:

- Route ALL changes to Amazon SQS for audit
- Route INSERT events to AWS Step Functions for validation
- Route DELETE events to Amazon SNS for alerting

## Cleanup

> **Warning:** This deletes the stack with its stream in Amazon Kinesis Data Streams, CDC stream and AWS Lambda log groups, and the Amazon Aurora DSQL cluster with all its data.

In a new shell, set `AWS_REGION` and `CLUSTER_ID` again and change to the `cdk` folder (`cd serverless-patterns/dsql-cdc-eventbridge-fanout-cdk/cdk`) first.

1. Delete the temporary rule and queue from the Testing section. Do this first: an Amazon EventBridge event bus cannot be deleted while it has rules ([API reference](https://docs.aws.amazon.com/eventbridge/latest/APIReference/API_DeleteEventBus.html)), so `cdk destroy` would fail.

    ```bash
    aws events remove-targets --rule dsql-cdc-test --event-bus-name dsql-cdc-events --ids 1
    aws events delete-rule --name dsql-cdc-test --event-bus-name dsql-cdc-events
    QUEUE_URL=$(aws sqs get-queue-url --queue-name dsql-cdc-test --query QueueUrl --output text)
    aws sqs delete-queue --queue-url $QUEUE_URL
    rm /tmp/queue-attributes.json
    ```

2. Delete the stack (this also deletes the CDC stream):

    ```bash
    npx cdk destroy
    ```

3. Delete the Amazon Aurora DSQL cluster. New clusters have deletion protection enabled, so turn it off first. If you used an existing cluster, skip this step and run `DROP TABLE orders;` in `psql` instead:

    ```bash
    aws dsql update-cluster --identifier $CLUSTER_ID --no-deletion-protection-enabled
    aws dsql delete-cluster --identifier $CLUSTER_ID
    ```

4. In the test runs, the custom resource provider wrote its last log lines after AWS CloudFormation had deleted its log group, and AWS Lambda then created the group again, without retention. Delete it if it is there:

    ```bash
    for g in $(aws logs describe-log-groups --log-group-name-prefix DsqlCdcEventbridgeFanoutStack-CdcStreamProviderLogs \
      --query 'logGroups[].logGroupName' --output text); do aws logs delete-log-group --log-group-name $g; done
    ```

## Services Used

| Service | Role |
|---------|------|
| Amazon Aurora DSQL | Source database with CDC enabled |
| Amazon Kinesis Data Streams | Receives CDC event stream from Amazon Aurora DSQL |
| AWS Lambda | Processes CDC events, classifies operations, publishes to Amazon EventBridge |
| Amazon EventBridge | Custom event bus for content-based routing of CDC events |

----
Copyright 2026 Amazon.com, Inc. or its affiliates. All Rights Reserved.

SPDX-License-Identifier: MIT-0
