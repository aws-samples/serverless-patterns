# EventBridge to SQS Fair Queue with Lambda Consumer

This pattern deploys an EventBridge rule that routes events to an SQS fair queue, consumed by a Lambda function. Fair queues ensure equitable processing across tenants — no single tenant can monopolize the consumer.

Learn more about this pattern at Serverless Land Patterns: https://serverlessland.com/patterns/eventbridge-sqs-fair-queue-lambda-cdk

Important: this application uses various AWS services and there are costs associated with these services after the Free Tier usage - please see the [AWS Pricing page](https://aws.amazon.com/pricing/) for details. You are responsible for any AWS costs incurred. No warranty is implied in this example.

> **⚠️ Important Note:** As of April 2026, `FairQueueConfiguration` is **API-only** and not yet supported in the CloudFormation schema. This means the fair queue configuration cannot be deployed via CDK/CloudFormation. This pattern deploys the standard SQS queue, EventBridge rule, Lambda consumer, and DLQ via CDK, but the fair queue enablement must be done separately via the AWS CLI or SDK after deployment:
>
> ```bash
> aws sqs set-queue-attributes \
>   --queue-url <QueueUrl> \
>   --attributes '{"FairQueueConfiguration":"{\"MessageGroupIdFieldPath\":\"$.detail.tenantId\"}"}'
> ```
>
> Once CloudFormation adds `FairQueueConfiguration` support, this pattern will be updated to deploy fully via CDK.

## Requirements

* [Create an AWS account](https://portal.aws.amazon.com/gp/aws/developer/registration/index.html) if you do not already have one and log in.
* [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html) installed and configured
* [Git Installed](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)
* [Node.js 18+](https://nodejs.org/en/download/) installed
* [AWS CDK v2](https://docs.aws.amazon.com/cdk/v2/guide/getting-started.html) installed

## Architecture

```
┌──────────────┐     ┌──────────────────┐     ┌──────────────────┐     ┌──────────────┐
│  EventBridge  │────▶│  EventBridge     │────▶│  SQS Fair Queue  │────▶│  Lambda       │
│  PutEvents    │     │  Rule            │     │  (per-tenant     │     │  Consumer     │
│  (tenant-id)  │     │  (source match)  │     │   fair sharing)  │     │               │
└──────────────┘     └──────────────────┘     └──────────────────┘     └──────────────┘
```

## How it works

1. Events are published to EventBridge with a `detail.tenantId` field identifying the tenant.
2. An EventBridge rule matches events with `source: "com.myapp.orders"` and routes them to an SQS fair queue.
3. The fair queue uses `tenantId` as the message group ID, ensuring equitable consumption across tenants.
4. A Lambda function processes messages from the fair queue. Even if Tenant A sends 1000 messages and Tenant B sends 10, both tenants get fair processing time.
5. A dead-letter queue captures failed messages after 3 retries.

## Deployment Instructions

1. Clone the repository:
    ```bash
    git clone https://github.com/aws-samples/serverless-patterns
    cd serverless-patterns/eventbridge-sqs-fair-queue-lambda-cdk
    ```

2. Install dependencies:
    ```bash
    npm install
    ```

3. Deploy the stack:
    ```bash
    cdk deploy
    ```

4. Note the EventBridge bus name and queue URL from the stack outputs.

## Testing

1. Send events for multiple tenants:
    ```bash
    # Tenant A — burst of events
    for i in $(seq 1 5); do
      aws events put-events --entries '[{
        "Source": "com.myapp.orders",
        "DetailType": "OrderCreated",
        "Detail": "{\"tenantId\": \"tenant-a\", \"orderId\": \"order-a-'$i'\", \"amount\": 99.99}",
        "EventBusName": "<EventBusName>"
      }]'
    done

    # Tenant B — single event
    aws events put-events --entries '[{
      "Source": "com.myapp.orders",
      "DetailType": "OrderCreated",
      "Detail": "{\"tenantId\": \"tenant-b\", \"orderId\": \"order-b-1\", \"amount\": 49.99}",
      "EventBusName": "<EventBusName>"
    }]'
    ```

2. Check Lambda logs to verify fair processing — Tenant B's message should not be starved by Tenant A's burst:
    ```bash
    aws logs tail /aws/lambda/<FunctionName> --follow
    ```

## Cleanup

```bash
cdk destroy
```

----
Copyright 2026 Amazon.com, Inc. or its affiliates. All Rights Reserved.

SPDX-License-Identifier: MIT-0
