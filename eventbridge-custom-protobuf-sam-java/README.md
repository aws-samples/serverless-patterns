# Protobuf on an EventBridge custom event bus (Java + CloudFormation)

A runnable sample that publishes a rich domain event, **Protobuf-encoded**, to a
new EventBridge custom event bus (the `eventsv2` API) using `PutRawEvents` with
an **AWS Glue Schema Registry**, then delivers that same event to a **Lambda**
subscriber that logs it to CloudWatch — proving the event survives the round
trip intact.

![Architecture: Publisher.java Protobuf-encodes and Glue-frames an OrderPlaced event, publishes it to an EventBridge custom event bus via PutRawEvents; the bus decodes the Protobuf against the Glue Schema Registry server-side and a subscriber delivers the JSON to a consumer Lambda that logs it to CloudWatch, with an SQS dead-letter queue on failure.](docs/architecture.svg)

The publisher encodes `OrderPlaced` (defined in `src/main/proto/order_placed.proto`)
and wraps it in the Glue wire format. **EventBridge decodes the Protobuf against
the Glue registry server-side and delivers `Data` as plain JSON**, so the
consumer just logs it — a matching `orderId`, fields, and metadata prove the
delivered event equals the originating one.

## Language

The publisher uses the AWS SDK for Java v2
(`software.amazon.awssdk:eventbridgev2` and `:glue`) and `protobuf-java`; the
`OrderPlaced` / `OrderItem` classes are generated from the `.proto` by the
`protobuf-maven-plugin` (which downloads `protoc`) during the build. The consumer
Lambda runs on the Java 21 runtime, built by SAM with Maven. Python and
TypeScript versions of this pattern live in sibling `-python` / `-typescript`
folders.

## Layout

```
eventbridge-custom-protobuf-sam-java/
  src/main/proto/order_placed.proto              # Protobuf schema — the source of truth (protoc codegen input)
  src/main/java/com/example/orders/ProtoIo.java    # protobuf-java encode/decode + Glue wire framing (with message index)
  src/main/java/com/example/orders/Publisher.java  # Protobuf-encode + PutRawEvents with a per-request Glue registry
  src/main/java/com/example/orders/Consumer.java   # Lambda: logs the server-decoded JSON event
  src/test/java/com/example/orders/                # JUnit 5 + Mockito: round-trip, framing, message index, handler, publisher
  pom.xml                                           # java21, eventbridgev2 + glue + protobuf-java, protoc codegen, shade
  docs/architecture.svg                             # the architecture diagram shown above
  infra/template.yaml                               # bus, subscriber, Glue registry+schema, Lambda (java21), DLQ, role
  scripts/run_publish.sh                            # convenience: publish one event, print the log command
  scripts/deploy.sh                                 # convenience wrapper around sam build + sam deploy
  scripts/teardown.sh                               # convenience wrapper around sam delete
```

The Java protobuf classes are generated at build time from
`src/main/proto/order_placed.proto` into `target/generated-sources` — regenerate,
don't hand-edit. The `.proto`'s `java_*` options only affect the generated code
layout; they don't change the wire format or the message full names Glue uses.

## Deployment model

Everything is provisioned by one CloudFormation template (`infra/template.yaml`):
the event bus and subscriber (`AWS::EventsV2::EventBus` and
`AWS::EventsV2::Subscriber`), the Glue registry + schema, the consumer Lambda,
the dead-letter queue, and the delivery role. SAM builds the Java consumer with
Maven (which runs `protoc`).

> Note: `cfn-lint` may flag the `AWS::EventsV2::*` resources with `E3006`
> ("resource type does not exist") if its bundled resource spec has not caught
> up yet. The types deploy fine; this is a stale-spec false positive.

## Prerequisites

- JDK 21 and Apache Maven (the consumer runs on the `java21` Lambda runtime; the
  publisher and tests build and run locally). The build downloads a matching
  `protoc` automatically — no separate protoc install needed.
- AWS SAM CLI and AWS CLI v2.
- AWS credentials for a **non-production** account, with permission to create an
  EventsV2 event bus + subscriber, a Glue registry/schema, a Lambda function, an
  IAM role, and an SQS queue.
- The new custom event bus (`eventsv2`) available in your Region — confirm with
  `aws eventsv2 list-event-buses`.

## Run the tests 

```bash
mvn test
```

These cover the Protobuf round trip (including the Glue wire framing and the
message index), the publisher's request-shaping, schema-version lookup, and
result handling (validated against Mockito-mocked `EventBridgeV2Client` and
`GlueClient`), and the Lambda handler processing a delivered event — all fully
offline.

## Deploy

The whole stack (bus, subscriber, Glue registry/schema, Lambda, DLQ, role) is one
CloudFormation template, so a plain SAM build + deploy is all you need:

```bash
sam build --template infra/template.yaml
sam deploy --guided --capabilities CAPABILITY_NAMED_IAM
```

`--guided` prompts for a stack name and region and saves your answers to
`samconfig.toml`, so later deploys are just `sam deploy`. The stack creates a
role with an explicit name (`<AppName>-delivery-role`), which requires
`CAPABILITY_NAMED_IAM` — the guided flow does not prompt for it, so pass it on
the command line as shown. (Non-interactively:
`sam deploy --capabilities CAPABILITY_NAMED_IAM --resolve-s3`.)

The stack outputs include the event bus ARN (`EventBusArn`) and the Glue registry
ARN (`SchemaRegistryArn`) — read them with:

```bash
aws cloudformation describe-stacks --stack-name <stack-name> \
  --query "Stacks[0].Outputs" --output table
```

> There is also a `scripts/deploy.sh [stack-name] [region]` convenience wrapper
> that runs the same build + deploy non-interactively and prints those ARNs.

> `sam build` runs Maven (including protoc codegen) for the Java consumer. If you
> build without a local JDK 21 / Maven, use `sam build --use-container` (needs
> Docker); it builds in the Lambda `java21` image.

## Publish and verify

```bash
scripts/run_publish.sh [stack-name] [region] [order-id]
```

It reads the Glue registry and the bus from the stack outputs, builds the
publisher's shaded jar (`mvn clean package`, which also runs protoc) if needed,
and publishes one `OrderPlaced`. You can also run it directly after
`mvn package`:

```bash
BUS_ARN=<bus-arn> REGISTRY_ARN=<registry-arn> AWS_REGION=<region> \
  java -jar target/eventbridge-custom-protobuf-sam-java-1.0.0.jar --order-id order-123
```

Then watch the delivered event in CloudWatch:

```bash
aws logs tail /aws/lambda/proto-orders-consumer --since 5m --format short
```

You should see an `OrderPlaced[...]` line with the `orderId` you published, the
full record (delivered as JSON), the custom `metadata`, and the Glue `schemaId`
the service used to decode it.

## How Protobuf decoding is wired

Protobuf is an open format, so the service decodes the payload against a schema
registry named **on the publish request itself**. `Publisher.java` calls
`PutRawEvents` with the bus ARN and `SchemaRegistryConfiguration.registryUri` set
to the Glue registry ARN. The registry is not configured on the bus. EventBridge
reads the registry with the **caller's own credentials**, so the identity running
the publisher needs Glue read access on the registry.

Publisher IAM (minimum): the caller needs `events:PutRawEvents` on the bus, plus
Glue read on the registry — `glue:GetSchemaVersion` so the publisher can resolve
the schema-version id for the wire header, and the read actions the service uses
to decode:

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

## Teardown

Everything is in the CloudFormation stack, so deleting the stack removes the bus,
subscriber, Glue registry/schema, Lambda, DLQ, and delivery role:

```bash
sam delete
```

`sam delete` uses the stack name saved in `samconfig.toml`; pass
`--stack-name <name> --region <region>` if you deployed without `--guided`.

> There is also a `scripts/teardown.sh [stack-name] [region]` convenience wrapper
> that deletes the stack and waits for completion.

## Key considerations

- **`Data` must carry the Glue wire header, not bare Protobuf.** The frame is
  `0x03` (version) + `0x00` (no compression) + the 16-byte schema-version UUID +
  a **message-index** varint + the Protobuf bytes. `ProtoIo.encodeFramed(order,
  schemaVersionId)` builds this; the publisher looks the version id up with
  `glue:GetSchemaVersion`.
- **The message-index picks which message type to decode as.** Glue numbers the
  file's messages by full name sorted lexicographically (here `OrderItem`=0,
  `OrderPlaced`=1). A wrong index still publishes `PUBLISHED` but decodes as the
  wrong type. `ProtoIo` computes the index Glue's way, so adding or renaming
  messages keeps it correct.
- **`Data` is raw bytes (`SdkBytes`).** Don't base64-encode before the SDK; the
  SDK does the wire encoding. Hand it the framed bytes.
- **EventBridge decodes the Protobuf server-side.** With a Glue registry named on
  the request, the delivered `Data` is a **decoded JSON object**, and
  `SystemMetadata` gains `aws:SchemaId` and `aws:RegistryType: Glue`. So the
  consumer needs no Protobuf library — it just reads JSON.
- **IAM actions are `events:`, never `eventsv2:`.** `eventsv2` is only the
  CLI/SDK name; `eventsv2:` in a policy is accepted but grants nothing.
- **The Lambda receives a batch (a JSON array).** The handler iterates it.
- **Protobuf binary can't be filtered on `DATA`.** The bytes are opaque to a
  `DATA` pattern, so the subscriber filters on `METADATA`
  (`eventType = OrderPlaced`).
- **The subscriber uses a `WITH_METADATA` transformer** so the Lambda receives the
  `Data` + `Metadata` + `SystemMetadata` envelope. The default `RAW` would deliver
  the payload alone, with no metadata.
- **JVM cold start.** The consumer is given 512 MB for JVM cold-start headroom.
- **The schema lives in two places that must match by hand.**
  `infra/template.yaml` inlines the same Protobuf message definitions as
  `src/main/proto/order_placed.proto`. There's no sync step — if you change one,
  edit the other, or the publisher and the Glue-registered schema drift and
  publishes fail to decode. Glue supports proto2/proto3 but not `extensions` or
  `groups`.