# Amazon Bedrock AgentCore Memory record streaming to Amazon Kinesis Data Streams

This pattern turns on record streaming for an Amazon Bedrock AgentCore Memory with built-in semantic and user-preference strategies. Amazon Bedrock AgentCore Memory publishes a lifecycle event to Amazon Kinesis Data Streams each time it creates, updates or deletes a long-term memory record. A short AWS Lambda function reads those events through a filtered event source mapping and keeps an Amazon DynamoDB table of memory records in sync, including deletions.

Learn more about this pattern at Serverless Land Patterns: https://serverlessland.com/patterns/agentcore-memory-kinesis-typescript-cdk

Important: this application uses various AWS services and there are costs associated with these services after the Free Tier usage - please see the [AWS Pricing page](https://aws.amazon.com/pricing/) for details. The Amazon Kinesis Data Streams shard bills for every hour the stack exists, so run `cdk destroy` when you finish testing. You are responsible for any AWS costs incurred. No warranty is implied in this example.

## Requirements

* [Create an AWS account](https://portal.aws.amazon.com/gp/aws/developer/registration/index.html) if you do not already have one and log in. The IAM user that you use must have sufficient permissions to make necessary AWS service calls and manage AWS resources.
* [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html) installed and configured. The Testing section uses `create-event` and `delete-memory-record` of `aws bedrock-agentcore`, which exist in AWS CLI 2.31.3.
* [Git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git) installed
* [Node.js 22 or later](https://nodejs.org/en/download/) installed
* [AWS CDK v2](https://docs.aws.amazon.com/cdk/v2/guide/getting_started.html) installed (`npm install -g aws-cdk`)
* [Python 3](https://www.python.org/downloads/) installed (used once in Testing, to compute a timestamp)

## Supported Regions

This pattern was tested in us-east-1, us-west-2 and eu-central-1. The [AgentCore supported Regions page](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/agentcore-regions.html) lists the Regions for AgentCore Memory and the [memory record streaming page](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/memory-record-streaming.html) does not list Regions separately, so check both pages before you deploy elsewhere. The stack takes its Region from your CLI configuration.

## Architecture

```
Amazon Bedrock AgentCore Memory
  (semantic + user-preference strategies, stream delivery: MEMORY_RECORDS, FULL_CONTENT)
        |  MemoryRecordCreated / MemoryRecordUpdated / MemoryRecordDeleted
        v
Amazon Kinesis Data Streams (1 shard, encrypted with an AWS KMS key)
        |  event source mapping filter on memoryStreamEvent.eventType
        v
AWS Lambda  --->  Amazon DynamoDB (key: memoryRecordId, index: actorId)
```

## How it works

1. `CreateEvent` stores conversation turns as short-term events. AgentCore Memory then extracts long-term records asynchronously with the built-in semantic and user-preference strategies, which need no Amazon Bedrock model permissions in the stack (extraction worked without any in the test runs).
2. The memory has a stream delivery resource that points at the Kinesis stream. For each record that is created, updated or deleted, AgentCore Memory assumes the memory execution role and puts an event on the stream. With `FULL_CONTENT` the event includes `memoryRecordText`.
3. The event source mapping filters on `memoryStreamEvent.eventType`. This keeps the `StreamingEnabled` validation event, which AgentCore Memory publishes when streaming is enabled and which has no record ID, away from the function.
4. The function upserts an item for created and updated events, and deletes the item for deleted events. It parses the actor ID from the namespace, because only created and updated events carry a namespace. The table key is `memoryRecordId` because deleted events carry only `memoryId` and `memoryRecordId`.

The memory execution role comes from the `aws-cdk-lib/aws-bedrockagentcore` Memory construct. Its trust policy has `aws:SourceAccount` and `aws:SourceArn` conditions. Its permissions policy allows `kinesis:ListShards`, `kinesis:PutRecord`, `kinesis:PutRecords` and `kinesis:DescribeStream` on this stream, and `kms:Encrypt`, `kms:ReEncrypt*` and `kms:GenerateDataKey*` on the stream key.

## Important Notes

* `FULL_CONTENT` puts the extracted text on the stream and in the table, and it can contain personal information from conversations. Set the level to `METADATA_ONLY` in `lib/agentcore-memory-kinesis-stack.ts` if you do not need the text; the function then stores the metadata without it.
* The [documented event schema](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/memory-record-streaming.html#memory-record-streaming-event-schema) has no field that links a memory record to the `CreateEvent` call that produced it.
* The documentation does not state a partition key or an ordering guarantee for the events that AgentCore Memory publishes (in the test runs the partition key was `<memory ID>#<memory record ID>`). The function applies each event as it arrives, so a `MemoryRecordDeleted` event processed before its created event, or an older update that arrives after a newer one, can leave a stale item in the table. Treat the table as eventually consistent.
* The function reads the actor ID from the default built-in namespace `/strategies/{memoryStrategyId}/actors/{actorId}`; a record in another namespace layout is stored with the actor ID `unknown`.
* Long-term memory consolidation can also delete records, so `MemoryRecordDeleted` events can arrive without a delete call from you (see [Stream event types](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/memory-record-streaming.html#memory-record-streaming-event-types)).
* The event source mapping retries from a failing record onward up to 3 times and then discards the records, because it has no on-failure destination (this keeps the pattern at four services; the AWS KMS key only encrypts the stream).
* The Lambda function uses the `nodejs24.x` runtime and the AWS SDK for JavaScript v3 that the runtime provides.

## Deployment Instructions

1. Clone the repository:
    ```bash
    git clone https://github.com/aws-samples/serverless-patterns
    cd serverless-patterns/agentcore-memory-kinesis/typescript/cdk
    ```

2. Install dependencies and type-check:
    ```bash
    npm install
    npm run build
    ```

3. If the account and Region have never been used with the AWS CDK, bootstrap them once:
    ```bash
    npx cdk bootstrap
    ```

4. Deploy the stack:
    ```bash
    npx cdk deploy
    ```

5. Note the stack outputs: `MemoryId`, `MemoryArn`, `StreamName`, `TableName`, `FunctionName` and `ProjectorLogGroupName`.

## Testing

Use the AWS CLI configured for the Region you deployed to. Start every new shell with these variables:

```bash
STACK=AgentcoreMemoryKinesisStack
out() { aws cloudformation describe-stacks --stack-name "$STACK" --query "Stacks[0].Outputs[?OutputKey=='$1'].OutputValue" --output text; }
MEMORY_ID=$(out MemoryId); MEMORY_ARN=$(out MemoryArn); STREAM=$(out StreamName)
TABLE=$(out TableName); FUNCTION=$(out FunctionName); LOG_GROUP=$(out ProjectorLogGroupName)
```

1. Check that the event source mapping is enabled. Expected: `Enabled`.
    ```bash
    aws lambda list-event-source-mappings --function-name "$FUNCTION" --query 'EventSourceMappings[0].State' --output text
    ```

2. Send a conversation to the memory:
    ```bash
    aws bedrock-agentcore create-event --memory-id "$MEMORY_ID" --actor-id test-user --session-id test-session-1 \
      --event-timestamp "$(date -u +%Y-%m-%dT%H:%M:%SZ)" \
      --payload '[{"conversational":{"content":{"text":"I prefer Italian restaurants with outdoor seating"},"role":"USER"}},{"conversational":{"content":{"text":"Noted, I will remember your preference for Italian restaurants with outdoor seating."},"role":"ASSISTANT"}}]'
    ```

3. Extraction is asynchronous and the documentation gives no fixed time, so repeat this query until items appear (about 70 seconds in the test runs). Expected: one or more items for `test-user`, each with a `memoryRecordId`, a strategy type and the extracted text.
    ```bash
    aws dynamodb query --table-name "$TABLE" --index-name actor-index \
      --key-condition-expression 'actorId = :a' --expression-attribute-values '{":a":{"S":"test-user"}}' \
      --query 'Items[].{id:memoryRecordId.S,strategy:strategyType.S,text:memoryRecordText.S,namespace:namespace.S}'
    ```

4. Delete one record by the `id` from step 3. Memory record deletion publishes a `MemoryRecordDeleted` event:
    ```bash
    aws bedrock-agentcore delete-memory-record --memory-id "$MEMORY_ID" --memory-record-id RECORD_ID
    ```
   Replace `RECORD_ID` with the `id` value. Repeat the query from step 3. The item with that `id` should disappear once the event is processed (within 15 seconds in the test runs).

5. Read the delivery metric. The [memory record streaming page](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/memory-record-streaming.html#memory-record-streaming-metrics) documents `StreamPublishingSuccess` in the `AWS/Bedrock-AgentCore` namespace with the dimensions `Operation` (`MemoryStreamEvent`) and `Resource` (the memory ARN). In the test runs the Sum was 3 (two `MemoryRecordCreated` events and one `MemoryRecordDeleted` event); the `StreamingEnabled` validation event is not counted. Allow a few minutes for the datapoints to appear.
    ```bash
    START=$(python3 -c "import datetime as d;print((d.datetime.now(d.timezone.utc)-d.timedelta(hours=1)).strftime('%Y-%m-%dT%H:%M:%SZ'))")
    END=$(date -u +%Y-%m-%dT%H:%M:%SZ)
    aws cloudwatch get-metric-statistics --namespace AWS/Bedrock-AgentCore --metric-name StreamPublishingSuccess \
      --dimensions Name=Operation,Value=MemoryStreamEvent Name=Resource,Value="$MEMORY_ARN" \
      --start-time "$START" --end-time "$END" --period 300 --statistics Sum
    ```
   If the output has no datapoints, list the metrics that exist for this memory and use the dimensions it shows:
    ```bash
    aws cloudwatch list-metrics --namespace AWS/Bedrock-AgentCore
    ```

6. If items do not appear, read the function logs:
    ```bash
    aws logs tail "$LOG_GROUP" --since 30m
    ```

## Cleanup

1. Delete the stack. This deletes the memory and its records, the Kinesis stream, the DynamoDB table with its items, the function log group and schedules the AWS KMS key for deletion:
    ```bash
    npx cdk destroy
    ```

2. The AWS KMS key stays in the pending deletion state for 7 days and is then deleted. Confirm the stack is gone:
    ```bash
    aws cloudformation describe-stacks --stack-name AgentcoreMemoryKinesisStack
    ```
   Expected: a `does not exist` error.

----
Copyright 2026 Amazon.com, Inc. or its affiliates. All Rights Reserved.

SPDX-License-Identifier: MIT-0
