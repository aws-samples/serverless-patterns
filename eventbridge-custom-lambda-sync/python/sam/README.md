# Ordered processing with a synchronous AWS Lambda target on Amazon EventBridge

This pattern shows an Amazon EventBridge custom event bus (the `eventsv2` API)
processing events in order by invoking an AWS Lambda function synchronously
(`InvocationType: REQUEST_RESPONSE`) from a FIFO subscriber.

In synchronous mode the bus confirms the target processed an event successfully
before acknowledging it and delivering the next event in the same group. That
confirmation is what makes ordered, reliable, direct-to-Lambda processing
possible, and it removes the common pattern of placing an Amazon SQS queue
between an event bus and Lambda just to get reliability and back-pressure.

Learn more about this pattern at Serverless Land Patterns: https://serverlessland.com/patterns/eventbridge-custom-lambda-sync-python-sam

Important: this application uses various AWS services and there are costs associated with these services after the Free Tier usage - please see the [AWS Pricing page](https://aws.amazon.com/pricing/) for details. You are responsible for any AWS costs incurred. No warranty is implied in this example.

## Requirements

* [Create an AWS account](https://portal.aws.amazon.com/gp/aws/developer/registration/index.html) if you do not already have one and log in. The IAM user that you use must have sufficient permissions to make necessary AWS service calls and manage AWS resources (a Lambda function, an IAM role, an SQS queue, and an EventsV2 event bus and subscriber). Use a non-production account.
* [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html) **v2.37.3 or later**, installed and configured. Check with `aws --version`. v2.37.3 is the first release with `aws eventsv2` (v2.37.2 shipped it as `aws eventbridgev2`).
* [AWS Serverless Application Model](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-sam-cli-install.html) (AWS SAM) CLI **v1.168.0 or later**. Check with `sam --version`.
* [Git Installed](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)
* Python 3.14 (matches the Lambda runtime, so `sam build` runs natively). Without it, use `sam build --use-container` (needs Docker).
* The new EventBridge custom event bus available in your Region. Check the [feature availability page](https://docs.aws.amazon.com/eventbridge/latest/userguide/feature-availability.html).

## Deployment Instructions

1. Create a new directory, navigate to that directory in a terminal and clone the GitHub repository:
    ```bash
    git clone https://github.com/aws-samples/serverless-patterns
    ```
1. Change directory to the pattern directory:
    ```bash
    cd serverless-patterns/eventbridge-custom-lambda-sync/python/sam
    ```
1. Build the consumer function:
    ```bash
    sam build
    ```
1. Deploy the stack:
    ```bash
    sam deploy --guided --capabilities CAPABILITY_NAMED_IAM
    ```
    The stack creates a role with an explicit name (`<AppName>-delivery-role`), which requires `CAPABILITY_NAMED_IAM`. The guided flow does not prompt for it, so pass it on the command line as shown.
1. During the prompts:
    * Enter a stack name
    * Enter the desired AWS Region
    * Accept or change the `AppName` (resource-name prefix) and `RetentionInDays` parameters

    Once you have run `sam deploy --guided` once and saved arguments to a configuration file (`samconfig.toml`), you can use `sam deploy` in future to use these defaults.

1. Note the outputs from the SAM deployment process. `EventBusArn` is used for testing. You can read the outputs again with:
    ```bash
    aws cloudformation describe-stacks --stack-name <stack-name> \
      --query "Stacks[0].Outputs" --output table
    ```

`scripts/deploy.sh [stack-name] [region]` is a convenience wrapper that runs the same build and deploy non-interactively and prints the bus ARN.

## How it works

The template (`template.yaml`) deploys an EventBridge custom event bus (`AWS::EventsV2::EventBus`), a FIFO subscriber (`AWS::EventsV2::Subscriber`), a Python 3.14 consumer Lambda function, an SQS dead-letter queue, and the delivery role EventBridge assumes to invoke the function.

1. The publisher (`publisher/publish.py`) sends a sequence of `OrderPlaced` JSON events with `PutEvents`. Every event in a run shares one `SystemMetadata.EventGroupId` and carries an increasing `seq` (1, 2, 3, ...).
1. The subscriber filters on `detail.orderId` and delivers matching events to the consumer function. Two settings work together to enforce order:
    ```yaml
    Type: FIFO
    InvokeConfiguration:
      TargetArn: <consumer function arn>
      RoleArn: <delivery role arn>
      LambdaParameters:
        InvocationType: REQUEST_RESPONSE
    ```
    * `Type: FIFO` orders events within an event group.
    * `InvocationType: REQUEST_RESPONSE` invokes the function synchronously, so the bus waits for each event to be confirmed before delivering the next. `EVENT` (asynchronous) cannot guarantee ordered, confirmed processing.
1. The consumer (`consumer/handler.py`) receives a batch (a JSON array) and logs each order's `seq` as it processes it. With the default `RAW` transformer and `PutEvents`, the order fields are under `detail`.
1. A delivery that ultimately fails goes to the SQS dead-letter queue. The delivery role trusts `events.amazonaws.com` and has `lambda:InvokeFunction` on the consumer and `sqs:SendMessage` on the dead-letter queue.

Key considerations:

* Events are ordered within an `EventGroupId`. Events in different groups are not ordered relative to each other.
* IAM actions use the `events:` prefix, never `eventsv2:`. The AWS CLI calls the service `aws eventsv2`, but boto3 calls it `eventbridgev2`.
* No account ID or Region is hardcoded. Resource names come from the `AppName` parameter.

## Testing

### Unit tests

Create a virtual environment, install dependencies, and run the tests. They run offline against a botocore Stubber that validates requests against the real `eventbridgev2` service model.

```bash
python3 -m venv .venv
./.venv/bin/pip install -r publisher/requirements.txt pytest
./.venv/bin/python -m pytest tests/ -q
```

### End to end

1. Publish an ordered sequence (default 5 events; pass a count to change it):
    ```bash
    scripts/run_publish.sh [stack-name] [region] [count]
    ```
    Or call the publisher directly with the `EventBusArn` output:
    ```bash
    ./.venv/bin/python publisher/publish.py --bus-arn <EventBusArn> --region <region> --count 5
    ```
1. Give it a few seconds, then watch the consumer process the group in order:
    ```bash
    aws logs tail /aws/lambda/sync-orders-consumer --since 5m --format short
    ```
    (Replace `sync-orders` if you changed `AppName`.)

The `Processing order ... seq=` lines appear in order (`seq=1`, then `seq=2`, then `seq=3`, ...), because the FIFO subscriber invokes the function synchronously and confirms each event before delivering the next.

## Cleanup

1. Delete the stack. This removes the bus, subscriber, function, dead-letter queue, and delivery role:
    ```bash
    sam delete
    ```
    `sam delete` uses the stack name saved in `samconfig.toml`. Pass `--stack-name <name> --region <region>` if you deployed without `--guided`. `scripts/teardown.sh [stack-name] [region]` is a convenience wrapper that deletes the stack and waits for completion.
1. Confirm the stack has been deleted:
    ```bash
    aws cloudformation list-stacks --query "StackSummaries[?contains(StackName,'STACK_NAME')].StackStatus"
    ```

----
Copyright 2026 Amazon.com, Inc. or its affiliates. All Rights Reserved.

SPDX-License-Identifier: MIT-0
