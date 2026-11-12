# Amazon EventBridge custom event bus (Protobuf) to AWS Lambda

This pattern publishes a rich domain event, **Protobuf-encoded**, to a new
Amazon EventBridge custom event bus (the `eventsv2` API) using `PutRawEvents` with
an AWS Glue Schema Registry, then delivers that same event to an AWS Lambda
subscriber that logs it to Amazon CloudWatch — proving the event survives the
round trip intact.

Learn more about this pattern at Serverless Land Patterns: https://serverlessland.com/patterns/eventbridge-custom-protobuf-java-sam

Important: this application uses various AWS services and there are costs associated with these services after the Free Tier usage - please see the [AWS Pricing page](https://aws.amazon.com/pricing/) for details. You are responsible for any AWS costs incurred. No warranty is implied in this example.

## Requirements

* [Create an AWS account](https://portal.aws.amazon.com/gp/aws/developer/registration/index.html) if you do not already have one and log in. Use a **non-production** account. The IAM user that you use must have sufficient permissions to make necessary AWS service calls and manage AWS resources: an Amazon EventBridge custom event bus (EventsV2) + subscriber, an AWS Glue registry/schema, an AWS Lambda function, an Amazon CloudWatch Logs log group, an AWS Identity and Access Management (IAM) role, and an Amazon SQS queue.
* [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html) version 2.37.3 or later installed and configured (earlier versions lack the `aws eventsv2` command)
* [Git Installed](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)
* [AWS Serverless Application Model](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-sam-cli-install.html) (AWS SAM) installed
* JDK 21 and Apache Maven installed (the consumer runs on the `java21` AWS Lambda runtime; the publisher and tests build and run locally). The build downloads a matching `protoc` automatically — no separate protoc install needed.
* The new Amazon EventBridge custom event bus (`eventsv2`) available in your Region — confirm with `aws eventsv2 list-event-buses`

## Deployment Instructions

1. Create a new directory, navigate to that directory in a terminal and clone the GitHub repository:
    ```
    git clone https://github.com/aws-samples/serverless-patterns
    ```
1. Change directory to the pattern directory:
    ```
    cd serverless-patterns/eventbridge-custom-protobuf/java/sam
    ```
1. Build the AWS Lambda consumer. `sam build` runs Maven (including protoc codegen) for the Java consumer. If you build without a local JDK 21 / Maven, use `sam build --use-container` (needs Docker); it builds in the AWS Lambda `java21` image.
    ```
    sam build
    ```
1. From the command line, use AWS SAM to deploy the AWS resources for the pattern as specified in the template.yaml file:
    ```
    sam deploy --guided --capabilities CAPABILITY_NAMED_IAM
    ```
1. During the prompts:
    * Enter a stack name
    * Enter the desired AWS Region
    * Allow SAM CLI to create IAM roles with the required permissions.

    The stack creates a role with an explicit name (`<AppName>-delivery-role`), which requires `CAPABILITY_NAMED_IAM` — the guided flow does not prompt for it, so pass it on the command line as shown. (Non-interactively: `sam deploy --capabilities CAPABILITY_NAMED_IAM --resolve-s3`.)

    Once you have run `sam deploy --guided` mode once and saved arguments to a configuration file (samconfig.toml), you can use `sam deploy` in future to use these defaults.
1. Note the outputs from the SAM deployment process. These contain the event bus ARN (`EventBusArn`), the AWS Glue registry ARN (`SchemaRegistryArn`), and the consumer's log group (`ConsumerLogGroup`), which are used for testing.

## How it works

Everything is provisioned by the AWS SAM template (`template.yaml`): the event
bus and subscriber (`AWS::EventsV2::EventBus` and `AWS::EventsV2::Subscriber`),
the AWS Glue registry + schema, the consumer AWS Lambda function and its Amazon
CloudWatch Logs log group (7-day retention), the Amazon SQS dead-letter queue, and
the delivery role. AWS SAM builds the Java consumer with Maven (which runs
`protoc`).

The publisher encodes `OrderPlaced` (defined in `src/main/proto/order_placed.proto`)
and wraps it in the AWS Glue wire format. **Amazon EventBridge decodes the Protobuf
against the AWS Glue registry server-side and delivers `Data` as plain JSON**, so
the consumer just logs it — a matching `order_id`, fields, and metadata prove the
delivered event equals the originating one.

The publisher uses the AWS SDK for Java v2 (`software.amazon.awssdk:eventbridgev2`
and `:glue`) and `protobuf-java`. The `OrderPlaced` / `OrderItem` classes are
generated from the `.proto` by the `protobuf-maven-plugin` into
`target/generated-sources` during the build — regenerate, don't hand-edit. The
`.proto`'s `java_*` options only affect the generated code layout; they don't
change the wire format or the message full names AWS Glue uses.

### How Protobuf decoding is wired

Protobuf is an open format, so the service decodes the payload against a schema
registry named **on the publish request itself**. `Publisher.java` calls
`PutRawEvents` with the bus ARN and `SchemaRegistryConfiguration.registryUri` set
to the AWS Glue registry ARN. The registry is not configured on the bus. Amazon
EventBridge reads the registry with the **caller's own credentials**, so the
identity running the publisher needs AWS Glue read access on the registry.

Publisher AWS Identity and Access Management (IAM) permissions (minimum): the
caller needs `events:PutRawEvents` on the bus, plus AWS Glue read on the registry —
`glue:GetSchemaVersion` so the publisher can resolve the schema-version id for the
wire header, and the read actions the service uses to decode:

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
      "Action": ["glue:GetSchemaVersion", "glue:GetSchemaByDefinition", "glue:GetRegistry"],
      "Resource": [
        "arn:aws:glue:<region>:<account>:registry/proto-orders-registry",
        "arn:aws:glue:<region>:<account>:schema/proto-orders-registry/*"
      ]
    }
  ]
}
```

## Key considerations

- **`Data` must carry the AWS Glue wire header, not bare Protobuf.** The frame is
  `0x03` (version) + `0x00` (no compression) + the 16-byte schema-version UUID +
  a **message-index** varint + the Protobuf bytes. `ProtoIo.encodeFramed(order,
  schemaVersionId)` builds this; the publisher looks the version id up with
  `glue:GetSchemaVersion`.
- **The message-index picks which message type to decode as.** AWS Glue numbers the
  file's messages by full name sorted lexicographically (here `OrderItem`=0,
  `OrderPlaced`=1). A wrong index still publishes `PUBLISHED` but decodes as the
  wrong type. `ProtoIo` computes the index the way AWS Glue does, so adding or
  renaming messages keeps it correct.
- **`Data` is raw bytes (`SdkBytes`).** Don't base64-encode before the SDK; the
  SDK does the wire encoding. Hand it the framed bytes.
- **Amazon EventBridge decodes the Protobuf server-side.** With an AWS Glue registry
  named on the request, the delivered `Data` is a **decoded JSON object**, and
  `SystemMetadata` gains `aws:SchemaId` and `aws:RegistryType: Glue`. So the
  consumer needs no Protobuf library — it just reads JSON.
- **You can filter on `DATA` or `METADATA`.** Because the event is sent with
  content type `application/protobuf` and an AWS Glue registry on the request,
  Amazon EventBridge deserializes the payload *before* it applies subscriber
  filters, so a `DATA`-scoped pattern matches the decoded fields by their
  schema names. For example, this filter works too:
  `{"Scope": "DATA", "Pattern": "{\"currency\":[\"USD\"]}"}`. Only
  `application/octet-stream` payloads are opaque to `DATA` filters. This sample
  filters on `METADATA` (`eventType = OrderPlaced`), the publisher's custom
  routing key. That's a design choice, not a requirement.
- **Decoded fields keep the `.proto` field names.** Amazon EventBridge decodes
  Protobuf using the schema's field names, not camelCase, so the delivered
  record has `order_id` and `placed_at`, not `orderId` and `placedAt`. Use the
  schema names in `DATA` filters too.
- **AWS Identity and Access Management (IAM) actions are `events:`, never
  `eventsv2:`.** `eventsv2` is only the CLI/SDK name; `eventsv2:` in a policy is
  accepted but grants nothing.
- **Throttling is retried by the SDK.** The publisher's clients use the AWS SDK for
  Java v2 standard retry strategy (exponential backoff with jitter, 5 attempts), so
  there is no hand-written retry loop.
- **The AWS Lambda function receives a batch (a JSON array).** The handler iterates it.
- **The subscriber uses a `WITH_METADATA` transformer** so the AWS Lambda function
  receives the `Data` + `Metadata` + `SystemMetadata` envelope. The default `RAW`
  would deliver the payload alone, with no metadata.
- **JVM cold start.** The consumer is given 512 MB for JVM cold-start headroom.
- **The schema lives in two places that must match by hand.**
  `template.yaml` inlines the same Protobuf message definitions as
  `src/main/proto/order_placed.proto`. There's no sync step — if you change one,
  edit the other, or the publisher and the AWS Glue-registered schema drift and
  publishes fail to decode. AWS Glue supports proto2/proto3 but not `extensions`
  or `groups`.

## Testing

### Unit tests

```bash
mvn test
```

These cover the Protobuf round trip (including the AWS Glue wire framing and the
message index), the publisher's request-shaping, retry configuration,
schema-version lookup, and result handling (validated against Mockito-mocked
`EventBridgeV2Client` and `GlueClient`), and the AWS Lambda handler processing a
delivered event — all fully offline.

### Publish and verify

```bash
scripts/run_publish.sh [stack-name] [region] [order-id]
```

The stack name and region default to the values `sam deploy --guided` saved in
`samconfig.toml`, so after a guided deploy you can run it with no arguments.
It reads the AWS Glue registry and the bus from the stack outputs, builds the
publisher's shaded jar (`mvn clean package`, which also runs protoc) if needed,
and publishes one `OrderPlaced` (naming the registry on the request). You can
also run it directly after `mvn package`:

```bash
BUS_ARN=<bus-arn> REGISTRY_ARN=<registry-arn> AWS_REGION=<region> \
  java -jar target/eventbridge-custom-protobuf-sam-java-1.0.0.jar --order-id order-123
```

Then watch the delivered event in Amazon CloudWatch, using the `ConsumerLogGroup`
stack output:

```bash
aws logs tail <consumer-log-group> --since 5m --format short
```

You should see an `OrderPlaced[...]` line with the `order_id` you published (decoded
fields use the `.proto` names, so it's `order_id`, not `orderId`), the
full record (delivered as JSON), the custom `metadata`, and the AWS Glue `schemaId`
the service used to decode it.

## Cleanup

1. Delete the stack. Everything is in the AWS CloudFormation stack, so deleting the stack removes the bus, subscriber, AWS Glue registry/schema, AWS Lambda function and its log group, Amazon SQS DLQ, and delivery role:
    ```bash
    sam delete
    ```
    `sam delete` uses the stack name saved in `samconfig.toml`; pass `--stack-name <name> --region <region>` if you deployed without `--guided`.

----
Copyright 2026 Amazon.com, Inc. or its affiliates. All Rights Reserved.

SPDX-License-Identifier: MIT-0
