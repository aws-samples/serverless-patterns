# Protobuf on an EventBridge custom event bus (TypeScript + CloudFormation)

A runnable sample that publishes a rich domain event, Protobuf-encoded, to a
new EventBridge custom event bus (the `eventsv2` API) using `PutRawEvents` with
an AWS Glue Schema Registry, then delivers that same event to a Lambda
subscriber that logs it to CloudWatch — proving the event survives the round
trip intact.

![Architecture: publish.ts Protobuf-encodes and Glue-frames an OrderPlaced event, publishes it to an EventBridge custom event bus via PutRawEvents; the bus decodes the Protobuf against the Glue Schema Registry server-side and a subscriber delivers the JSON to a consumer Lambda that logs it to CloudWatch, with an SQS dead-letter queue on failure.](docs/architecture.svg)

The publisher encodes `OrderPlaced` (defined in `proto/order_placed.proto`) and
wraps it in the Glue wire format. EventBridge decodes the Protobuf against the
Glue registry server-side and delivers `Data` as plain JSON, so the consumer
just logs it — a matching `orderId`, fields, and metadata prove the delivered
event equals the originating one.

## Language

This is the TypeScript version. The publisher uses the AWS SDK for
JavaScript v3 (`@aws-sdk/client-eventbridgev2` and `@aws-sdk/client-glue`) and
[`protobufjs`](https://www.npmjs.com/package/protobufjs), which loads
`proto/order_placed.proto` at runtime — so there is no codegen step and no
generated bindings to commit. The consumer Lambda runs on the Node.js 24
runtime, bundled by SAM with esbuild. Python and Java versions of this pattern
live in sibling `-python` / `-java` folders.

## Layout

```
eventbridge-custom-protobuf-sam-typescript/
  proto/order_placed.proto     # Protobuf schema — the source of truth (loaded at runtime)
  common/protoio.ts            # protobufjs encode/decode + Glue wire framing (with message index)
  publisher/publish.ts         # Protobuf-encode + PutRawEvents with a per-request Glue registry
  consumer/handler.ts          # Lambda: logs the server-decoded JSON event
  consumer/package.json        # marks the consumer as ESM + esbuild for the SAM build
  infra/template.yaml          # bus, subscriber, Glue registry+schema, Lambda (nodejs24.x), DLQ, role
  scripts/run_publish.sh       # convenience: publish one event, print the log command
  scripts/deploy.sh            # convenience wrapper around sam build + sam deploy
  scripts/teardown.sh          # convenience wrapper around sam delete
  tests/                       # vitest: round-trip, framing, message index, handler, publisher
  package.json, tsconfig.json  # deps, build, and test config
  docs/architecture.svg        # the architecture diagram shown above
```

## Deployment model (all CloudFormation)

Everything is provisioned by one CloudFormation template (`infra/template.yaml`):
the event bus and subscriber (`AWS::EventsV2::EventBus` and
`AWS::EventsV2::Subscriber`), the Glue registry + schema, the consumer Lambda,
the dead-letter queue, and the delivery role. SAM builds the TypeScript consumer
with esbuild.


## Prerequisites

- Node.js 20+ (the publisher and tests run locally; the Lambda runs on
  `nodejs24.x`).
- AWS SAM CLI and AWS CLI v2.
- AWS credentials for a **non-production** account, with permission to create an
  EventsV2 event bus + subscriber, a Glue registry/schema, a Lambda function, an
  IAM role, and an SQS queue.
- The new custom event bus (`eventsv2`) available in your Region — confirm with
  `aws eventsv2 list-event-buses`.

Install dependencies (for running the publisher and the tests):

```bash
npm install
```

## Run the tests 

```bash
npm test
```

These cover the Protobuf round trip (including the Glue wire framing and the
message index), the publisher's request-shaping, schema-version lookup, and
result handling (validated against the `EventBridgeV2Client` and `GlueClient`
with `aws-sdk-client-mock`), and the Lambda handler processing a delivered event
— all fully offline.

## Deploy

The whole stack (bus, subscriber, Glue registry/schema, Lambda, DLQ, role) is one
CloudFormation template, so after installing deps a plain SAM build + deploy is
all you need:

```bash
npm install
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

> `sam build` runs esbuild for the TypeScript consumer. If you build without a
> local esbuild, use `sam build --use-container` (needs Docker); it builds in the
> Lambda `nodejs24.x` image.

## Publish and verify

```bash
scripts/run_publish.sh [stack-name] [region] [order-id]
```

It reads the Glue registry and the bus from the stack outputs and publishes one
`OrderPlaced` (naming the registry on the request). You can also run the
publisher directly:

```bash
BUS_ARN=<bus-arn> REGISTRY_ARN=<registry-arn> AWS_REGION=<region> \
  npx tsx publisher/publish.ts --order-id order-123
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
registry named **on the publish request itself**. `publish.ts` calls
`PutRawEvents` with `EventBusArn` set to the bus and
`SchemaRegistryConfiguration.RegistryUri` set to the Glue registry ARN. The
registry is not configured on the bus. EventBridge reads the registry with the
**caller's own credentials**, so the identity running `publish.ts` needs Glue
read access on the registry.

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
  a **message-index** varint + the Protobuf bytes. `common/protoio.ts` builds
  this via `encodeFramed(record, schemaVersionId)`; the publisher looks the
  version id up with `glue:GetSchemaVersion`.
- **The message-index picks which message type to decode as.** Glue numbers the
  file's messages by full name sorted lexicographically (here `OrderItem`=0,
  `OrderPlaced`=1). A wrong index still publishes `PUBLISHED` but decodes as the
  wrong type. `protoio.ts` computes the index Glue's way, so adding or renaming
  messages keeps it correct.
- **`Data` is raw bytes (a `Uint8Array`).** Don't base64-encode before the SDK;
  the SDK does the wire encoding. Hand it the framed bytes.
- **protobufjs uses camelCase (JSON) field names.** `orderId`, `placedAt`, etc.,
  not the `.proto` snake_case — `protoio.ts` encodes/decodes the camelCase object
  directly. (EventBridge's server-side Glue decode delivers its own field names to
  the consumer, which treats the delivered `Data` as opaque JSON, so the two
  decode paths are independent.)
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
- **The schema lives in two places that must match by hand.**
  `infra/template.yaml` inlines the same Protobuf schema as
  `proto/order_placed.proto`. There's no sync step — if you change one, edit the
  other, or the publisher and the Glue-registered schema drift and publishes fail
  to decode. Glue supports proto2/proto3 but not `extensions` or `groups`.
