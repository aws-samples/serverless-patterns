# Amazon EventBridge custom event bus to AWS Lambda with AWS Glue Schema Registry Avro

This pattern publishes a rich domain event, Avro-encoded, to an Amazon EventBridge custom event bus (the `eventsv2` API) using `PutRawEvents` with an AWS Glue Schema Registry. EventBridge decodes the Avro server-side and a subscriber delivers the event as JSON to an AWS Lambda function, which logs it to Amazon CloudWatch, showing the event survives the round trip intact.

Learn more about this pattern at Serverless Land Patterns: https://serverlessland.com/patterns/eventbridge-custom-avro-python-sam

Important: this application uses various AWS services and there are costs associated with these services after the Free Tier usage - please see the [AWS Pricing page](https://aws.amazon.com/pricing/) for details. You are responsible for any AWS costs incurred. No warranty is implied in this example.

## Requirements

* [Create an AWS account](https://portal.aws.amazon.com/gp/aws/developer/registration/index.html) if you do not already have one and log in. Use a **non-production** account. The IAM user that you use must have permission to create an EventsV2 event bus and subscriber, an AWS Glue registry and schema, a Lambda function, an IAM role, and an Amazon SQS queue.
* [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html) v2.37.3 or later installed and configured. This is the first release with the `aws eventsv2` commands for the enhanced custom event bus (v2.37.2 shipped them as `aws eventbridgev2`). Check with `aws --version`.
* [Git Installed](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)
* [AWS Serverless Application Model](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-sam-cli-install.html) (AWS SAM) CLI v1.168.0 or later installed. Check with `sam --version`.
* Python 3.14 (matches the Lambda runtime, so `sam build` runs natively). Without it, use `sam build --use-container` (requires Docker).
* The new custom event bus available in your Region. Check [feature availability](https://docs.aws.amazon.com/eventbridge/latest/userguide/feature-availability.html) for the latest.

## Deployment Instructions

1. Create a new directory, navigate to that directory in a terminal and clone the GitHub repository:
    ```
    git clone https://github.com/aws-samples/serverless-patterns
    ```
1. Change directory to the pattern directory:
    ```
    cd serverless-patterns/eventbridge-custom-avro/python/sam
    ```
1. From the command line, use AWS SAM to build and deploy the AWS resources for the pattern as specified in the `template.yaml` file:
    ```
    sam build
    sam deploy --guided --capabilities CAPABILITY_NAMED_IAM
    ```
    The stack creates a role with an explicit name (`<AppName>-delivery-role`), which requires `CAPABILITY_NAMED_IAM`. The guided flow does not prompt for it, so pass it on the command line as shown.
1. During the prompts:
    * Enter a stack name
    * Enter the desired AWS Region
    * Allow SAM CLI to create IAM roles with the required permissions.

    Once you have run `sam deploy --guided` mode once and saved arguments to a configuration file (samconfig.toml), you can use `sam deploy` in future to use these defaults.
1. Note the outputs from the SAM deployment process. These contain the resource names and ARNs which are used for testing, including `EventBusArn`, `SchemaRegistryArn` and `DeadLetterQueueUrl`:
    ```bash
    aws cloudformation describe-stacks --stack-name <stack-name> \
      --query "Stacks[0].Outputs" --output table
    ```

`scripts/deploy.sh [stack-name] [region]` is a convenience wrapper that runs the same build and deploy non-interactively and prints those ARNs.

## How it works

The template (`template.yaml`) provisions the event bus and subscriber (`AWS::EventsV2::EventBus` and `AWS::EventsV2::Subscriber`), the Glue registry and Avro schema, the consumer Lambda function, an SQS dead-letter queue, and the delivery role EventBridge assumes to invoke the function.

The publisher (`publisher/publish.py`) encodes an `OrderPlaced` event with `schema/order_placed.avsc` and wraps it in the Glue wire format. It calls `PutRawEvents` with `EventBusArn` set to the bus and `SchemaRegistryConfiguration.RegistryUri` set to the Glue registry ARN. EventBridge decodes the Avro against the registry server-side and the subscriber delivers `Data` as plain JSON, so the consumer (`consumer/handler.py`) needs no Avro library and just logs it. A matching `orderId`, fields and metadata show the delivered event equals the one that was published. Failed deliveries go to the dead-letter queue.

```
schema/order_placed.avsc     # canonical Avro schema (source of truth)
common/avroio.py             # shared encode/decode helper (publisher + tests)
publisher/publish.py         # Avro-encode + PutRawEvents with a per-request Glue registry
consumer/handler.py          # Lambda: logs the server-decoded JSON event
template.yaml                # bus, subscriber, Glue registry+schema, Lambda, DLQ, delivery role
                             #   (inlines the same schema as schema/order_placed.avsc)
scripts/                     # convenience wrappers: deploy, publish, teardown
tests/                       # pytest: round-trip, publisher (stubbed), handler
```

### Publisher IAM

The registry is named on the publish request, not configured on the bus, and EventBridge reads it with the **caller's own credentials**. The identity running `publish.py` needs `events:PutRawEvents` on the bus, plus `glue:GetSchemaVersion` scoped to the registry and its schemas. That one action covers both the publisher resolving the schema-version id for the wire header and EventBridge reading the schema to decode. This is the minimum policy from the [EventBridge open formats guide](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-custom-bus-open-formats.html):

```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": ["events:PutRawEvents"],
      "Resource": "arn:aws:events:<region>:<account>:event-busv2/avro-orders-bus/*"
    },
    {
      "Effect": "Allow",
      "Action": ["glue:GetSchemaVersion"],
      "Resource": [
        "arn:aws:glue:<region>:<account>:registry/avro-orders-registry",
        "arn:aws:glue:<region>:<account>:schema/avro-orders-registry/*"
      ]
    }
  ]
}
```

### Key considerations

- **`Data` must carry the Glue wire header, not bare Avro.** The frame is `0x03` (version) + `0x00` (no compression) + the 16-byte schema-version UUID + the Avro bytes. Bare Avro is rejected with `Malformed Glue wire format`. `common/avroio.py` builds this via `encode_framed(record, schema_version_id)`; the publisher looks the version id up with `glue:GetSchemaVersion`.
- **Don't base64-encode before boto3.** `PutRawEvents` `Data` is a blob; the SDK does the wire encoding. Hand it the raw framed bytes.
- **EventBridge decodes the Avro server-side.** With a Glue registry named on the request, the delivered `Data` is a decoded JSON object, and `SystemMetadata` gains `aws:SchemaId` and `aws:RegistryType: Glue`.
- **The Glue registry is named on each `PutRawEvents` request** (via `SchemaRegistryConfiguration.RegistryUri`), not on the bus. A registry set on the bus is ignored.
- **The service has different names in the CLI and boto3.** The AWS CLI calls it `aws eventsv2`, but boto3 calls it `eventbridgev2` (`boto3.client("eventbridgev2")`, botocore 1.43.102 or later). `boto3.client("eventsv2")` fails with `UnknownServiceError: Unknown service: 'eventsv2'`.
- **IAM actions are `events:`, never `eventsv2:` or `eventbridgev2:`.** Those are only the CLI and SDK names; such a prefix in a policy is accepted but grants nothing.
- **The Lambda receives a batch (a JSON array).** The handler iterates it.
- **The subscriber can filter on `METADATA` or `DATA`.** This pattern routes on the publisher-set `METADATA` key `eventType = OrderPlaced`. `METADATA` filters match exact values only: each value must be a JSON array of exact values, and operators such as `prefix`, `numeric`, `exists` and `$or` are not supported. Because `ContentType` is `application/avro`, EventBridge deserializes the payload to JSON, so a `DATA` filter on a record field also works, for example `{"orderId":["1001"]}`, and supports every event pattern operator except wildcards. An `application/octet-stream` event has no data a `DATA` filter can read. See [Filtering events for a subscriber](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-custom-bus-filtering.html).
- **The subscriber uses a `WITH_METADATA` transformer** so the Lambda receives the `Data` + `Metadata` + `SystemMetadata` envelope. The default `RAW` would deliver the payload alone.
- **The schema lives in two places that must match by hand.** `template.yaml` inlines the same Avro schema as `schema/order_placed.avsc` (compact form). If you change one, edit the other, or publishes fail to decode.
- **cfn-lint and `AWS::EventsV2::*`.** If cfn-lint's bundled resource spec hasn't caught up, it reports `E3006` ("resource type does not exist") for these types. The template suppresses that check on the two resources; the types deploy fine.

## Testing

1. Install the publisher dependencies locally:
    ```bash
    python3 -m venv .venv
    ./.venv/bin/pip install -r publisher/requirements.txt pytest
    ```
1. (Optional) Run the unit tests. They cover the Avro round trip (including the Glue wire framing), the publisher's request shaping and result handling (validated against the real `eventbridgev2` boto3 model with a botocore stubber), and the Lambda handler:
    ```bash
    ./.venv/bin/python -m pytest tests/ -q
    ```
1. Publish one `OrderPlaced` event. The script reads the bus and registry ARNs from the stack outputs and prints the command to watch the log:
    ```bash
    scripts/run_publish.sh <stack-name> <region> [order-id]
    ```
1. View the delivered event in CloudWatch Logs:
    ```bash
    aws logs tail /aws/lambda/avro-orders-consumer --since 5m --format short
    ```
    You should see an `OrderPlaced[...]` line with the `orderId` you published, the full record (delivered as JSON), the custom `metadata`, and the Glue `schemaId` the service used to decode it.
1. Confirm the dead-letter queue is empty (use `DeadLetterQueueUrl` from the stack outputs):
    ```bash
    aws sqs get-queue-attributes --queue-url <DeadLetterQueueUrl> \
      --attribute-names ApproximateNumberOfMessages
    ```

## Cleanup

1. Delete the stack. This removes the bus, subscriber, Glue registry and schema, Lambda function, DLQ and delivery role:
    ```bash
    sam delete
    ```
    `sam delete` uses the stack name saved in `samconfig.toml`; pass `--stack-name <name>` if you deployed without `--guided`. `scripts/teardown.sh [stack-name] [region]` is a convenience wrapper that deletes the stack and waits for completion.
1. Confirm the stack has been deleted:
    ```bash
    aws cloudformation list-stacks --query "StackSummaries[?contains(StackName,'STACK_NAME')].StackStatus"
    ```

----
Copyright 2026 Amazon.com, Inc. or its affiliates. All Rights Reserved.

SPDX-License-Identifier: MIT-0
