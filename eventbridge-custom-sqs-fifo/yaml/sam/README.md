# Amazon EventBridge enhanced custom event bus to Amazon SQS FIFO queue (AWS SAM)

This pattern delivers **ordered** events from an **enhanced custom Amazon EventBridge event bus** (the `AWS::EventsV2` service) to an **Amazon SQS FIFO queue**, using a FIFO **Subscriber**.

The enhanced custom event bus is a different service from classic EventBridge. There are **no rules or targets**. A single `AWS::EventsV2::Subscriber` bundles the event filter, the target, the retry policy, and the dead-letter destination into one resource. Setting the subscriber's `Type` to `FIFO` preserves order within an event group (events are grouped by the publisher's `EventGroupId` at publish time) and delivers them in sequence to the SQS FIFO queue.

Delivery uses an **IAM role** that EventBridge assumes to call `sqs:SendMessage` on the target queue and the dead-letter queue — this replaces the queue resource policy used in classic EventBridge.

> Naming note: this service is `eventsv2` in the AWS CLI, `eventbridgev2` in the SDKs, and `events` in the IAM namespace (shared with classic EventBridge).

Learn more about this pattern at Serverless Land Patterns: << Add the live URL here >>

Important: this application uses various AWS services and there are costs associated with these services after the Free Tier usage - please see the [AWS Pricing page](https://aws.amazon.com/pricing/) for details. You are responsible for any AWS costs incurred. No warranty is implied in this example.

## Requirements

* [Create an AWS account](https://portal.aws.amazon.com/gp/aws/developer/registration/index.html) if you do not already have one and log in. The IAM user that you use must have sufficient permissions to make necessary AWS service calls and manage AWS resources.
* [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html) **v2.37.5 or newer** installed and configured (earlier versions do not include `aws eventsv2`, which the test steps use)
* [Git Installed](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)
* [AWS Serverless Application Model](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-sam-cli-install.html) (AWS SAM) installed
* A Region where the enhanced custom event bus is available — see the [launch announcement](https://aws.amazon.com/blogs/aws/introducing-enhanced-custom-event-buses-in-amazon-eventbridge-for-enterprise-scale-event-driven-applications/) for the list.

## Deployment Instructions

1. Create a new directory, navigate to that directory in a terminal and clone the GitHub repository:

    ```
    git clone https://github.com/aws-samples/serverless-patterns
    ```

2. Change directory to the pattern directory:

    ```
    cd serverless-patterns/eventbridge-custom-sqs-fifo/yaml/sam
    ```

3. From the command line, use AWS SAM to deploy the AWS resources for the pattern as specified in the template.yaml file:

    ```
    sam deploy --guided
    ```

4. During the prompts:
    * Enter a stack name
    * Enter a Region where the enhanced custom event bus is available
    * Allow SAM CLI to create IAM roles with the required permissions.

    Once you have run `sam deploy --guided` mode once and saved arguments to a configuration file (samconfig.toml), you can use `sam deploy` in future to use these defaults.

5. Note the outputs from the SAM deployment process. These contain the resource names and/or ARNs which are used for testing.

## How it works

* An **enhanced custom event bus** (`AWS::EventsV2::EventBus`) is created with 14-day retention (`StorageConfiguration.RetentionPeriodInDays`), which enables replay and starting positions. It matches the dead-letter queue's 14-day retention, so every failure record still points at events you can replay.
* A **FIFO subscriber** (`AWS::EventsV2::Subscriber`, `Type: FIFO`) filters events on the payload (`Scope: DATA`) and delivers matching events, in order within an event group, to the SQS FIFO queue.
* `InvokeConfiguration.SqsParameters.MessageGroupId` is `{% $events.SystemMetadata.EventGroupId %}`, so each publisher event group becomes its own ordered group in the queue. Publish an `EventGroupId` on every event that needs ordering: an event published without one is still delivered, but in a group of its own.
* Each `EventGroupId` must also be a valid [SQS `MessageGroupId`](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/APIReference/API_SendMessage.html): up to 128 ASCII letters, digits and punctuation.
    * A value longer than 128 characters is rejected by `put-events`. The whole call fails, so the valid entries in the same call are not published either; correct the value and publish them again.
    * A value with any other character, such as a space, tab, line break, accented or non-Latin letter, or emoji, is accepted by the bus, but the queue rejects the delivery. The dead-letter record then fails as well, because its `MessageGroupId` comes from the same value, so the event leaves no record in the dead-letter queue. The only trace is in the subscriber delivery logs: `ON_FAILURE_DESTINATION_DELIVERY_ATTEMPT` records with the outcome `FAILURE`.
* `MessageDeduplicationId` is the bus-assigned event id, `{% $events.SystemMetadata."aws:EventId" %}`, which is unique for each accepted event and stays the same across retries. The publisher's `DeduplicationId` is not used here: the bus scopes it to one account and event group, while the queue deduplicates across all groups, so two groups reusing one id would lose the second message. Duplicate publishes are suppressed earlier, at the bus.
* Delivery is authorized by an **IAM role** (`DeliveryRole`) that trusts `events.amazonaws.com` (scoped by `aws:SourceAccount` and a subscriber `aws:SourceArn`) and grants `sqs:SendMessage` on the target queue and the DLQ.
* The **SQS FIFO queue** (`FifoQueue: true`, name ending in `.fifo`) receives the ordered messages.
* Events that exhaust the retry policy go to a **FIFO dead-letter queue**. EventBridge sets each failure record's `MessageGroupId` from the event group, so records for one group stay in order. `ContentBasedDeduplication` is enabled on it as a precaution.
* A failing event blocks the later events in its group for as long as it is retried, and reaches the dead-letter queue only when the retry policy is exhausted. With the default parameters (`MaxRetryAttempts` 10, `MaxEventAgeInSeconds` 3600), that can be up to an hour; lower them if latency matters more. If you fix the cause while the event is still being retried, for example by granting the delivery role `sqs:SendMessage` on the queue, a later retry delivers the event and the events behind it, in order, and nothing goes to the dead-letter queue. Retries are spaced further apart the longer they continue, so delivery can come several minutes after the fix. See [Retry limits](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-custom-bus-retry.html).
* An **Amazon CloudWatch Logs vended-log delivery** (`AWS::Logs::DeliverySource` with `LogType: INFO_LOGS` pointing at the subscriber ARN, plus destination and delivery) captures the subscriber's delivery records. `IncludePayload` is `ON_ERROR_ONLY`; use `FULL` only while debugging, because it copies every event body into the log group.

## Testing

These steps use the AWS CLI (`aws eventsv2`, v2.37.5+). Replace `STACK_NAME` and the Region as needed.

1. Capture the stack outputs:

    ```
    BUS_ARN=$(aws cloudformation describe-stacks --stack-name STACK_NAME \
      --query "Stacks[0].Outputs[?OutputKey=='EventBusArn'].OutputValue" --output text)

    QUEUE_URL=$(aws cloudformation describe-stacks --stack-name STACK_NAME \
      --query "Stacks[0].Outputs[?OutputKey=='TargetQueueUrl'].OutputValue" --output text)
    ```

2. Publish two ordered events in the same event group. `EventBusArn` is a top-level field; ordering within a group is set by each entry's `SystemMetadata.EventGroupId`, and `DeduplicationId` lets the bus suppress a repeated publish. Save this as `putevents.json`:

    ```json
    {
      "EventBusArn": "REPLACE_WITH_EventBusArn_OUTPUT",
      "Entries": [
        { "Source": "com.example.orders", "DetailType": "OrderPlaced",
          "Detail": "{\"orderId\":\"1001\",\"seq\":1}",
          "SystemMetadata": { "EventGroupId": "customer-42", "DeduplicationId": "evt-1" } },
        { "Source": "com.example.orders", "DetailType": "OrderPlaced",
          "Detail": "{\"orderId\":\"1001\",\"seq\":2}",
          "SystemMetadata": { "EventGroupId": "customer-42", "DeduplicationId": "evt-2" } }
      ]
    }
    ```

    Then publish:

    ```
    aws eventsv2 put-events --cli-input-json file://putevents.json
    ```

    Each result entry carries an `EventId` and a `SuccessCode` of `PUBLISHED` (or `DEDUPLICATED`, which is also a success), and `FailedEntryCount` is 0.

3. Receive from the FIFO queue and confirm order and FIFO attributes:

    ```
    aws sqs receive-message --queue-url "$QUEUE_URL" \
      --attribute-names All --message-attribute-names All \
      --max-number-of-messages 10
    ```

    You should see the events in `seq` order, each with `MessageGroupId` = `customer-42`, a `MessageDeduplicationId` equal to the `EventId` returned in step 2, and a FIFO `SequenceNumber`. The `SenderId` shows `AssumedByEventBridge`, confirming delivery via the IAM role.

4. Confirm the subscriber delivery logs landed. Records can take a minute or two to appear:

    ```
    LG=/aws/vendedlogs/STACK_NAME-subscriber
    STREAM=$(aws logs describe-log-streams --log-group-name "$LG" \
      --query 'logStreams[0].logStreamName' --output text)
    aws logs get-log-events --log-group-name "$LG" --log-stream-name "$STREAM" \
      --start-from-head --query 'events[].message'
    ```

    You should see a `SUBSCRIBER_MATCHED` and an `EVENT_DELIVERY_ATTEMPT` record for each published event.

## Testing the dead-letter queue

The dead-letter queue stays empty while deliveries succeed, so `receive-message` on it returns nothing until a delivery fails. These steps force one failure by denying the delivery role access to the target queue.

1. Redeploy with short retry limits, so the failure reaches the dead-letter queue within seconds instead of after up to an hour:

    ```
    sam deploy --parameter-overrides MaxRetryAttempts=0 MaxEventAgeInSeconds=60
    ```

2. Deny the delivery role `sqs:SendMessage` on the target queue with a queue policy. Save this as `deny.json`, replacing the placeholders with the `DeliveryRoleArn` and `TargetQueueArn` outputs (the policy is a JSON string, so its inner quotes stay escaped):

    ```json
    {
      "Policy": "{\"Version\":\"2012-10-17\",\"Statement\":[{\"Effect\":\"Deny\",\"Principal\":{\"AWS\":\"REPLACE_WITH_DeliveryRoleArn_OUTPUT\"},\"Action\":\"sqs:SendMessage\",\"Resource\":\"REPLACE_WITH_TargetQueueArn_OUTPUT\"}]}"
    }
    ```

    Then apply it:

    ```
    aws sqs set-queue-attributes --queue-url "$QUEUE_URL" --attributes file://deny.json
    ```

3. Publish the two events in `putevents.json` again. Change their `DeduplicationId` values first, so the bus does not suppress the repeat:

    ```
    aws eventsv2 put-events --cli-input-json file://putevents.json
    ```

4. Read the dead-letter queue. `--wait-time-seconds` long-polls, so the call waits for the record instead of returning empty:

    ```
    DLQ_URL=$(aws cloudformation describe-stacks --stack-name STACK_NAME \
      --query "Stacks[0].Outputs[?OutputKey=='DeliveryDLQUrl'].OutputValue" --output text)
    aws sqs receive-message --queue-url "$DLQ_URL" --max-number-of-messages 10 \
      --wait-time-seconds 20 --visibility-timeout 0 \
      --attribute-names All --message-attribute-names All
    ```

    You should see one failure record per batch. The body has `errorCode` `ACCESS_DENIED` and lists each event under `failedMessages` with its `eventId` and `eventGroupId`; `MessageGroupId` is the event group (`customer-42`). The record holds the events' ids, not the events; [Recovering events from the dead-letter queue](#recovering-events-from-the-dead-letter-queue) replays them from the bus. `--visibility-timeout 0` leaves the record visible, so you can read it again in that section.

5. Remove the deny policy and restore the default retry limits:

    ```
    aws sqs set-queue-attributes --queue-url "$QUEUE_URL" --attributes Policy=""
    sam deploy --parameter-overrides MaxRetryAttempts=10 MaxEventAgeInSeconds=3600
    ```

## Recovering events from the dead-letter queue

A dead-letter record lists the failed events' ids and timestamps; it does not contain the events. The events are still on the bus for its 14-day retention, so you recover them by replaying them from the bus with a temporary subscriber.

1. Read the failure records. Note each `failedMessages[].eventId`, the earliest and latest `timestamp`, and the `errorCode`. If no delivery has failed, the queue is empty and this returns nothing; to produce a record, follow [Testing the dead-letter queue](#testing-the-dead-letter-queue).

    ```
    DLQ_URL=$(aws cloudformation describe-stacks --stack-name STACK_NAME \
      --query "Stacks[0].Outputs[?OutputKey=='DeliveryDLQUrl'].OutputValue" --output text)
    aws sqs receive-message --queue-url "$DLQ_URL" --max-number-of-messages 10 \
      --wait-time-seconds 20 --visibility-timeout 0 --query 'Messages[].Body'
    ```

2. Fix the cause that `errorCode` names, for example the delivery role's permissions or the target queue.

3. Collect the values the replay subscriber needs:

    ```
    SUB_ARN=$(aws cloudformation describe-stacks --stack-name STACK_NAME \
      --query "Stacks[0].Outputs[?OutputKey=='SubscriberArn'].OutputValue" --output text)
    ROLE_ARN=$(aws eventsv2 describe-subscriber --subscriber-arn "$SUB_ARN" \
      --query InvokeConfiguration.RoleArn --output text)
    ```

4. Save this as `redrive.json`. Replace the placeholders with your bus ARN, target queue ARN and role ARN, the failed event ids, and a time window that covers the records' timestamps. The `aws:EventId` filter makes the replay exact, so the window can be slightly wider:

    ```json
    {
      "Name": "redrive-YYYY-MM-DD",
      "EventBusArn": "REPLACE_WITH_EventBusArn_OUTPUT",
      "Type": "FIFO",
      "StartingPosition": "POINT_IN_TIME",
      "PointInTimeConfiguration": {
        "PointType": "TIMESTAMP",
        "StartingPoint": "2026-09-30T12:29:00Z",
        "EndPoint": "2026-09-30T12:32:00Z"
      },
      "FilterConfiguration": {
        "Filters": [ { "Scope": "SYSTEM_METADATA",
                       "Pattern": "{\"aws:EventId\":[\"FAILED_EVENT_ID_1\",\"FAILED_EVENT_ID_2\"]}" } ]
      },
      "InvokeConfiguration": {
        "TargetArn": "REPLACE_WITH_TargetQueueArn_OUTPUT",
        "RoleArn": "REPLACE_WITH_ROLE_ARN",
        "SqsParameters": {
          "MessageGroupId": "{% $events.SystemMetadata.EventGroupId %}",
          "MessageDeduplicationId": "{% $events.SystemMetadata.\"aws:EventId\" %}"
        }
      }
    }
    ```

    Then create the subscriber:

    ```
    aws eventsv2 create-subscriber --cli-input-json file://redrive.json
    ```

    The replayed events keep their `EventGroupId`, so they return to their original groups in order, and they keep their `aws:EventId`, so the queue still deduplicates them.

5. When the events have arrived in the target queue, delete the temporary subscriber:

    ```
    aws eventsv2 delete-subscriber --subscriber-arn REDRIVE_SUBSCRIBER_ARN
    ```

    The dead-letter records you handled stay in the queue until its 14-day retention expires, or until you delete the stack. If you recover events again within that time, leave out the event ids you have already replayed, so they are not delivered twice.

## Cleanup

1. Delete the stack:

    ```
    sam delete
    ```

2. Confirm the stack has been deleted:

    ```
    aws cloudformation list-stacks --query "StackSummaries[?contains(StackName,'STACK_NAME')].StackStatus"
    ```

----
Copyright 2026 Amazon.com, Inc. or its affiliates. All Rights Reserved.

SPDX-License-Identifier: MIT-0
