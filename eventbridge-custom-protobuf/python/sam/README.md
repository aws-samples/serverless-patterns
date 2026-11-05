# Amazon EventBridge custom event bus with Protobuf and AWS Glue Schema Registry to AWS Lambda

This pattern publishes a Protobuf-encoded domain event to a new Amazon EventBridge custom event bus (the `eventsv2` API) using `PutRawEvents` with an AWS Glue Schema Registry. EventBridge decodes the Protobuf server-side and a subscriber delivers the event as JSON to an AWS Lambda function that logs it to Amazon CloudWatch Logs, showing the event survives the round trip intact. Failed deliveries go to an Amazon SQS dead-letter queue.

Learn more about this pattern at Serverless Land Patterns: https://serverlessland.com/patterns/eventbridge-custom-protobuf-python-sam

Important: this application uses various AWS services and there are costs associated with these services after the Free Tier usage - please see the [AWS Pricing page](https://aws.amazon.com/pricing/) for details. You are responsible for any AWS costs incurred. No warranty is implied in this example.

## Requirements

* [Create an AWS account](https://portal.aws.amazon.com/gp/aws/developer/registration/index.html) if you do not already have one and log in. Use a **non-production** account. The IAM identity you use must be able to create an EventsV2 event bus and subscriber, a Glue registry and schema, a Lambda function, an IAM role, and an SQS queue.
* [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html) **v2.37.3 or later**, installed and configured. Check with `aws --version`. v2.37.3 is the first release with `aws eventsv2`.
* [AWS Serverless Application Model](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-sam-cli-install.html) (AWS SAM) CLI **v1.168.0 or later**. Check with `sam --version`.
* [Git installed](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)
* [Python 3.14](https://www.python.org/downloads/) (matches the Lambda runtime, so `sam build` runs natively). Without it, use `sam build --use-container` (needs Docker).
* The new EventBridge custom event bus available in your Region. See [feature availability](https://docs.aws.amazon.com/eventbridge/latest/userguide/feature-availability.html).

## Deployment Instructions

1. Create a new directory, navigate to that directory in a terminal and clone the GitHub repository:
    ```bash
    git clone https://github.com/aws-samples/serverless-patterns
    ```
1. Change directory to the pattern directory:
    ```bash
    cd serverless-patterns/eventbridge-custom-protobuf/python/sam
    ```
1. Create a virtual environment and install the publisher dependencies, the test runner, and the Protobuf codegen tools (`buf` and the `protoc-gen-py` plugin are plain pip packages, so no system install is needed):
    ```bash
    python3 -m venv .venv
    ./.venv/bin/pip install -r publisher/requirements.txt pytest
    ./.venv/bin/pip install protoc-gen-py buf-bin
    ```
1. Generate the Protobuf bindings from `proto/order_placed.proto`. This writes `common/gen/order_placed_pb.py`, which is a build artifact and is git-ignored:
    ```bash
    scripts/generate.sh
    ```
1. Build and deploy the stack. The stack creates an explicitly named role (`<AppName>-delivery-role`), so it needs `CAPABILITY_NAMED_IAM`:
    ```bash
    sam build
    sam deploy --guided --capabilities CAPABILITY_NAMED_IAM
    ```
1. During the prompts:
    * Enter a stack name
    * Enter the desired AWS Region
    * Accept the default `AppName` (`proto-orders`) or enter your own prefix

    Once you have run `sam deploy --guided` once and saved arguments to a configuration file (`samconfig.toml`), you can use `sam deploy` in future to use these defaults.

1. Note the outputs from the SAM deployment process. These contain the event bus ARN (`EventBusArn`), the Glue registry ARN (`SchemaRegistryArn`), and the dead-letter queue URL (`DeadLetterQueueUrl`) used for testing:
    ```bash
    aws cloudformation describe-stacks --stack-name <stack-name> \
      --query "Stacks[0].Outputs" --output table
    ```

`scripts/deploy.sh [stack-name] [region]` is a convenience wrapper that runs the same build and deploy non-interactively and prints those ARNs.

## How it works

The template (`template.yaml`) provisions an `AWS::EventsV2::EventBus`, an `AWS::EventsV2::Subscriber`, a Glue registry with the `OrderPlaced` Protobuf schema, the consumer Lambda function, an SQS dead-letter queue, and the delivery role EventBridge assumes to invoke the function.

1. `publisher/publish.py` builds an `OrderPlaced` message (defined in `proto/order_placed.proto`), encodes it as Protobuf, and wraps it in the Glue wire format.
1. It calls `PutRawEvents` on the bus with `ContentType: application/protobuf` and names the Glue registry on the request (`SchemaRegistryConfiguration.RegistryUri`). It also sets custom `Metadata` keys such as `eventType`.
1. EventBridge decodes the Protobuf against the Glue registry, using the publisher's own credentials, and stores the event on the bus.
1. The subscriber filters on `METADATA` (`eventType = OrderPlaced`) and uses a `WITH_METADATA` transformer, so the Lambda function receives the `Data` + `Metadata` + `SystemMetadata` envelope with `Data` as plain JSON.
1. The consumer logs each delivered event. A matching `orderId`, fields, and metadata show the delivered event equals the published one. Failed deliveries are recorded in the dead-letter queue.

Key considerations:

- **`Data` must carry the Glue wire header, not bare Protobuf.** The frame is `0x03` (version) + `0x00` (no compression) + the 16-byte schema-version UUID + a message-index varint + the Protobuf bytes. `common/protoio.py` builds it with `encode_framed(message, schema_version_id)`; the publisher looks up the version id with `glue:GetSchemaVersion`.
- **The message-index picks which message type to decode as.** Glue numbers the file's messages by full name, sorted lexicographically (here `OrderItem`=0, `OrderPlaced`=1). A wrong index still returns `PUBLISHED` but decodes as the wrong type. `protoio.py` computes the index the same way Glue does.
- **Don't base64-encode before boto3.** `PutRawEvents` `Data` is a blob; the SDK does the wire encoding.
- **The registry is named on each `PutRawEvents` request, not on the bus.** The delivered `SystemMetadata` gains `aws:SchemaId` and `aws:RegistryType: Glue`, and the consumer needs no Protobuf library.
- **SDK and IAM naming differ.** The AWS CLI calls the service `aws eventsv2`, boto3 calls it `eventbridgev2` (`boto3.client("eventsv2")` raises `UnknownServiceError`), and IAM actions use the `events:` prefix.
- **Filtering.** Because EventBridge deserializes `application/protobuf` against the Glue registry before filtering, a `DATA` filter can match decoded fields by their schema names (for example `{"currency":["USD"]}`). This pattern filters on `METADATA` (`eventType`) so routing doesn't depend on the payload schema. Payloads sent as `application/octet-stream` are opaque and can only be filtered on `METADATA` or `SYSTEM_METADATA`.
- **The Lambda function receives a batch** (a JSON array), so the handler iterates it.
- **The schema lives in two places that must match by hand.** `template.yaml` inlines the same schema as `proto/order_placed.proto`. If you change one, change the other and re-run `scripts/generate.sh`. Glue supports proto2/proto3 but not `extensions` or `groups`.
- **Hardening the delivery role.** The role trusts only `events.amazonaws.com` and is scoped to the specific function and queue ARNs. In a shared account, add an `aws:SourceAccount: !Ref AWS::AccountId` condition to its `lambda:InvokeFunction` and `sqs:SendMessage` statements.
- `cfn-lint` may flag `AWS::EventsV2::*` with `E3006` if its bundled resource spec is older than the resource types. The types deploy fine.

The identity that runs the publisher needs `events:PutRawEvents` on the bus and `glue:GetSchemaVersion` on the registry and its schemas. That is the only Glue action required, and it is used twice: the publisher calls it to look up the schema-version UUID for the wire header, and EventBridge calls it with the publisher's credentials to decode the payload. Without it, the entry fails with `Access denied to schema registry`.

```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": ["events:PutRawEvents"],
      "Resource": "arn:aws:events:<region>:<account>:event-busv2/proto-orders-bus/*"
    },
    {
      "Effect": "Allow",
      "Action": ["glue:GetSchemaVersion"],
      "Resource": [
        "arn:aws:glue:<region>:<account>:registry/proto-orders-registry",
        "arn:aws:glue:<region>:<account>:schema/proto-orders-registry/*"
      ]
    }
  ]
}
```

## Testing

### Unit tests

```bash
./.venv/bin/python -m pytest tests/ -q
```

These cover the Protobuf round trip (including the Glue wire framing), the publisher's request shaping and result handling (validated against the service model with a botocore stubber), and the Lambda handler. If the bindings have not been generated, the suite skips with a message telling you to run `scripts/generate.sh`.

### End to end

1. Publish one `OrderPlaced` event. The script reads the bus and registry ARNs from the stack outputs:
    ```bash
    scripts/run_publish.sh <stack-name> <region> [order-id]
    ```
    You should see `SuccessCode=PUBLISHED` and an `EventId`.
1. After a few seconds, check the consumer logs:
    ```bash
    aws logs tail /aws/lambda/proto-orders-consumer --since 5m --format short
    ```
    You should see an `OrderPlaced[0]` line with the `orderId` you published, the full record as JSON, the custom `metadata`, and the Glue `schemaId` the service used to decode it.
1. Confirm the dead-letter queue is empty:
    ```bash
    aws sqs get-queue-attributes --queue-url <DeadLetterQueueUrl> \
      --attribute-names ApproximateNumberOfMessages
    ```

## Cleanup

1. Delete the stack. This removes the bus, subscriber, Glue registry and schema, Lambda function, dead-letter queue, and delivery role:
    ```bash
    sam delete
    ```
    `sam delete` uses the stack name saved in `samconfig.toml`; pass `--stack-name <stack-name> --region <region>` if you deployed without `--guided`. `scripts/teardown.sh [stack-name] [region]` is an equivalent wrapper.
1. Confirm the stack has been deleted:
    ```bash
    aws cloudformation list-stacks --query "StackSummaries[?contains(StackName,'<stack-name>')].StackStatus"
    ```

----
Copyright 2026 Amazon.com, Inc. or its affiliates. All Rights Reserved.

SPDX-License-Identifier: MIT-0
