# Amazon EventBridge custom event bus to AWS Lambda with ordered, synchronous delivery (Java)

This pattern shows an Amazon EventBridge custom event bus (the `eventsv2` API) processing events in order by invoking an AWS Lambda function synchronously (`InvocationType: REQUEST_RESPONSE`) from a FIFO subscriber. In synchronous mode the bus confirms the function processed an event successfully before it delivers the next event in the same group. That gives you ordered, reliable, direct-to-Lambda processing without placing an Amazon SQS queue between the bus and the function.

Learn more about this pattern at Serverless Land Patterns: https://serverlessland.com/patterns

Important: this application uses various AWS services and there are costs associated with these services after the Free Tier usage - please see the [AWS Pricing page](https://aws.amazon.com/pricing/) for details. You are responsible for any AWS costs incurred. No warranty is implied in this example.

## Requirements

* [Create an AWS account](https://portal.aws.amazon.com/gp/aws/developer/registration/index.html) if you do not already have one and log in. The IAM user that you use must have sufficient permissions to create a Lambda function, an IAM role, an SQS queue, and an EventBridge (EventsV2) event bus and subscriber.
* [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html) **v2.37.3 or later**, installed and configured. Check with `aws --version`. This is the first release with `aws eventsv2` (v2.37.2 shipped it as `aws eventbridgev2`).
* [AWS Serverless Application Model](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-sam-cli-install.html) (AWS SAM) CLI **v1.168.0 or later**. Check with `sam --version`.
* [Git Installed](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)
* [JDK 21](https://docs.aws.amazon.com/corretto/latest/corretto-21-ug/downloads-list.html) and [Apache Maven](https://maven.apache.org/install.html). The consumer runs on the `java21` Lambda runtime; the publisher and unit tests run locally. If you don't have them locally, `sam build --use-container` builds the function in the Lambda `java21` image (requires Docker).
* The new EventBridge custom event bus available in your Region. Confirm with `aws eventsv2 list-event-buses`.

## Deployment Instructions

1. Create a new directory, navigate to that directory in a terminal and clone the GitHub repository:
    ```bash
    git clone https://github.com/aws-samples/serverless-patterns
    ```
1. Change directory to the pattern directory:
    ```bash
    cd serverless-patterns/eventbridge-custom-lambda-sync/java/sam
    ```
1. Build the consumer function with AWS SAM (SAM runs Maven):
    ```bash
    sam build
    ```
1. Deploy the AWS resources for the pattern as specified in `template.yaml`:
    ```bash
    sam deploy --guided --capabilities CAPABILITY_NAMED_IAM
    ```
    The stack creates a role with an explicit name (`<AppName>-delivery-role`), which requires `CAPABILITY_NAMED_IAM`. The guided flow does not prompt for it, so pass it on the command line as shown.
1. During the prompts:
    * Enter a stack name
    * Enter the desired AWS Region
    * Accept the default `AppName` (`sync-orders`) or enter your own resource-name prefix
    * Allow SAM CLI to create IAM roles with the required permissions.

    Once you have run `sam deploy --guided` mode once and saved arguments to a configuration file (samconfig.toml), you can use `sam deploy` in future to use these defaults.
1. Note the outputs from the SAM deployment process. `EventBusArn` and `ConsumerLogGroup` are used for testing. You can read them again with:
    ```bash
    aws cloudformation describe-stacks --stack-name STACK_NAME \
      --query "Stacks[0].Outputs" --output table
    ```

`scripts/deploy.sh [stack-name] [region]` is a convenience wrapper that runs the same build and deploy non-interactively and prints the bus ARN.

## How it works

The template provisions:

* An EventBridge custom event bus (`AWS::EventsV2::EventBus`) that retains events for `RetentionInDays` (default 1 day).
* A FIFO subscriber (`AWS::EventsV2::Subscriber`) that filters for events carrying an `orderId` and invokes the consumer function synchronously.
* A Java 21 consumer Lambda function that logs each order in the order it is processed.
* An SQS dead-letter queue for deliveries that ultimately fail.
* A delivery role, trusted by `events.amazonaws.com`, with `lambda:InvokeFunction` on the consumer and `sqs:SendMessage` on the dead-letter queue.

The publisher (`Publisher.java`) sends a sequence of `OrderPlaced` events with `PutEvents`. Every event in a run shares one `SystemMetadata.EventGroupId` and carries an increasing `seq` (1, 2, 3, …). Two subscriber settings work together to process them in order:

```yaml
Type: FIFO
InvokeConfiguration:
  TargetArn: <consumer function arn>
  RoleArn: <delivery role arn>
  LambdaParameters:
    InvocationType: REQUEST_RESPONSE
```

* `Type: FIFO` orders events within an event group. Events in different groups are not ordered relative to each other.
* `InvocationType: REQUEST_RESPONSE` invokes the function synchronously, so the bus waits for each event to be confirmed before delivering the next. `EVENT` (asynchronous, fire-and-forget) cannot guarantee ordered, confirmed processing.

Things to know about the EventsV2 configuration:

* `PutEvents` delivers the classic envelope, so the order fields sit under `detail`. That's why the subscriber's `DATA` filter is `{"detail":{"orderId":[{"exists":true}]}}`. A `PutRawEvents` publish would put the payload directly in `Data`, and this filter would silently match nothing.
* A Lambda target receives a batch (a JSON array of events), not a single event. The handler iterates it.
* IAM actions use the `events:` prefix (for example `events:PutEvents`), never `eventsv2:`. `eventsv2` is only the CLI and SDK name. The Java SDK artifact is `software.amazon.awssdk:eventbridgev2`.
* A dead-letter record identifies the failed event by id and timestamp but does not carry the payload. Reprocessing it requires the event to still be inside the bus retention window.
* Subscriber `Name`, `EventBusArn`, `Type` and `InvokeConfiguration.TargetArn` are create-only. Changing one replaces the subscriber, and events published during the replacement can be missed.
* The consumer is given 512 MB for JVM cold-start headroom. Tune to taste.

`cfn-lint` may flag the `AWS::EventsV2::*` resources with `E3006` ("resource type does not exist") if its bundled resource spec has not caught up yet. The types deploy fine.

## Testing

### Unit tests

Run the JUnit 5 + Mockito tests. They cover the handler processing a batch in the order received, and the publisher's grouping and per-entry result checking against a mocked `EventBridgeV2Client`, fully offline:

```bash
mvn test
```

### End-to-end

1. Publish an ordered sequence of events (default 5; the third argument changes the count):
    ```bash
    scripts/run_publish.sh STACK_NAME REGION 5
    ```
    This builds the publisher's shaded jar with `mvn package` if needed and runs it. You can also run it directly after `mvn package`:
    ```bash
    BUS_ARN=<EventBusArn output> AWS_REGION=<region> \
      java -jar target/eventbridge-custom-lambda-sync-sam-java-1.0.0.jar --count 5
    ```
    Each event prints `SuccessCode=PUBLISHED`. A `PUBLISHED` response means the bus accepted the event, not that it was delivered, so confirm at the target in the next step.
1. After a few seconds, tail the consumer log (the `ConsumerLogGroup` output):
    ```bash
    aws logs tail /aws/lambda/sync-orders-consumer --since 5m --format short
    ```
1. The `Processing order ... seq=` lines appear in order, `seq=1`, then `seq=2`, then `seq=3`, because the FIFO subscriber invokes the function synchronously and confirms each event before delivering the next (`batchIndex` can vary with batching):
    ```
    Processing order group=order-group-1735689600 seq=1 orderId=order-group-1735689600-001 (batchIndex=0)
    Processing order group=order-group-1735689600 seq=2 orderId=order-group-1735689600-002 (batchIndex=0)
    Processing order group=order-group-1735689600 seq=3 orderId=order-group-1735689600-003 (batchIndex=0)
    ```
1. The dead-letter queue should stay empty. If events don't arrive, check it for failure records (the delivery is retried for up to 5 minutes by default before it lands there).

## Cleanup

1. Delete the stack. This removes the bus, subscriber, function, dead-letter queue and delivery role:
    ```bash
    sam delete
    ```
    `sam delete` uses the stack name saved in `samconfig.toml`; pass `--stack-name STACK_NAME --region REGION` if you deployed without `--guided`. `scripts/teardown.sh [stack-name] [region]` does the same and waits for completion.
1. Confirm the stack has been deleted:
    ```bash
    aws cloudformation list-stacks --query "StackSummaries[?contains(StackName,'STACK_NAME')].StackStatus"
    ```

----
Copyright 2025 Amazon.com, Inc. or its affiliates. All Rights Reserved.

SPDX-License-Identifier: MIT-0
