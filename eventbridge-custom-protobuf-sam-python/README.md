# Protobuf on an EventBridge custom event bus (Python + CloudFormation)

A runnable sample that publishes a rich domain event, Protobuf-encoded, to a
new EventBridge custom event bus (the `eventsv2` API) using `PutRawEvents` with
an AWS Glue Schema Registry, then delivers that same event to a Lambda
subscriber that logs it to CloudWatch — proving the event survives the round
trip intact.

![Architecture: publish.py Protobuf-encodes and Glue-frames an OrderPlaced event, publishes it to an EventBridge custom event bus via PutRawEvents; the bus decodes the Protobuf against the Glue Schema Registry server-side and a subscriber delivers the JSON to a consumer Lambda that logs it to CloudWatch, with an SQS dead-letter queue on failure.](docs/architecture.svg)

The publisher encodes `OrderPlaced` (defined in `proto/order_placed.proto`) and
wraps it in the Glue wire format. **EventBridge decodes the Protobuf against the
Glue registry server-side and delivers `Data` as plain JSON**, so the consumer
just logs it — a matching `orderId`, fields, and metadata prove the delivered
event equals the originating one.

> The bindings are generated from
> `proto/order_placed.proto` — see [Generate the Protobuf bindings](#generate-the-protobuf-bindings).

## Layout

```
protobuf-eventbridge-sample/
  proto/order_placed.proto     # Protobuf schema — the SOURCE OF TRUTH
  proto/buf.gen.yaml           # buf codegen config
  scripts/generate.sh          # generates the bindings into common/gen/ (git-ignored)
  common/gen/order_placed_pb.py  # GENERATED bindings (build artifact; not committed)
  common/protoio.py            # encode/decode + Glue wire framing (imports the bindings)
  publisher/publish.py         # Protobuf-encode + PutRawEvents with a per-request Glue registry
  consumer/handler.py          # Lambda: logs the server-decoded JSON event
  infra/template.yaml          # bus, subscriber, Glue registry+schema, Lambda, DLQ, delivery role
                               #   (inlines the same schema as proto/order_placed.proto)
  scripts/run_publish.sh       # convenience: publish one event, print the log command
  scripts/deploy.sh            # convenience wrapper around sam build + sam deploy
  scripts/teardown.sh          # convenience wrapper around sam delete
  tests/                       # pytest: round-trip, framing, publisher (stubbed), handler
  docs/architecture.svg        # the architecture diagram shown above
```

## Deployment model (all CloudFormation)

Everything is provisioned by one CloudFormation template (`infra/template.yaml`):
the event bus and subscriber (`AWS::EventsV2::EventBus` and
`AWS::EventsV2::Subscriber`), the Glue registry + schema, the consumer Lambda,
the dead-letter queue, and the delivery role. `scripts/deploy.sh` is a plain
`sam build` + `sam deploy`, and `scripts/teardown.sh` is a single
`delete-stack`.

> Note: `cfn-lint` may flag the `AWS::EventsV2::*` resources with `E3006`
> ("resource type does not exist") if its bundled resource spec has not caught
> up yet. The types deploy fine; this is a stale-spec false positive.

## Prerequisites

- Python 3.14 (matches the Lambda runtime, so `sam build` runs natively).
- AWS SAM CLI and AWS CLI v2.
- AWS credentials for a **non-production** account, with permission to create an
  EventsV2 event bus + subscriber, a Glue registry/schema, a Lambda function, an
  IAM role, and an SQS queue.
- The new custom event bus available in your Region.  Check the [AWS Documentation](https://docs.aws.amazon.com/eventbridge/latest/userguide/feature-availability.html) for the latest.  

Create the virtualenv and install dependencies:

```bash
python3 -m venv .venv
# Runtime deps (boto3 + bufbuild protobuf-py) and the test runner:
./.venv/bin/pip install -r publisher/requirements.txt pytest
# Codegen toolchain (dev only): the buf CLI and the protobuf-py protoc plugin.
# Both are plain pip packages — no system protoc/buf install needed.
./.venv/bin/pip install protoc-gen-py buf-bin
```

## Generate the Protobuf bindings

```bash
scripts/generate.sh
```

This runs `buf generate` (config in `proto/buf.gen.yaml`) with the
`protoc-gen-py` plugin and writes `common/gen/order_placed_pb.py`. The generated
module imports `protobuf` (protobuf-py) at runtime, which is why protobuf-py is a
runtime dependency, not just a build-time one.

To change the event shape, edit `proto/order_placed.proto`, re-run
`scripts/generate.sh`, and update the inlined schema in `infra/template.yaml` to
match (see the last gotcha).

## Run the tests

```bash
./.venv/bin/python -m pytest tests/ -q
```

These cover the Protobuf round trip (including the Glue wire framing), the
publisher's request-shaping and result handling (validated against the real
`eventsv2` model with a botocore stubber), and the Lambda handler processing a
delivered event. If the bindings have not been generated (or protobuf-py is not
installed), the suite **skips** with a message telling you to run
`scripts/generate.sh`.

## Deploy

Generate the Protobuf bindings first (see above), then a plain SAM build + deploy
provisions the whole stack (bus, subscriber, Glue registry/schema, Lambda, DLQ,
role):


```bash
scripts/generate.sh          # once, if you have not already (see above)
sam build --template infra/template.yaml 
sam deploy --guided --capabilities CAPABILITY_NAMED_IAM
```

You can accept defaults

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

> Building without local Python 3.14? Use `sam build --use-container` (needs
> Docker); it builds against the Lambda `python3.14` image regardless of your
> local interpreter.

## Publish and verify

```bash
scripts/run_publish.sh [stack-name] [region] [order-id]
```

It reads the Glue registry from the stack outputs, looks up the bus by name, and
publishes one `OrderPlaced` to it (naming the registry on the request), then
prints the command to watch the log. It runs the publisher with the sample's
`.venv` if present, otherwise `python3`/`python` (override with
`PYTHON=/path/to/python`); the chosen interpreter must have `boto3` and
`protobuf-py` installed, and the bindings must be generated. Then:

```bash
aws logs tail /aws/lambda/proto-orders-consumer --since 5m --format short
```

You should see an `OrderPlaced[...]` line with the `orderId` you published, the
full record (delivered as JSON), the custom `metadata`, and the Glue `schemaId`
the service used to decode it. The DLQ should stay empty on a healthy run:

```bash
aws sqs get-queue-attributes --queue-url <DeadLetterQueueUrl> \
  --attribute-names ApproximateNumberOfMessages
```

Note: You can retrieve the DeadLetterQueueUrl from the CloudFormation stack output.

## How Protobuf decoding is wired

Protobuf is an open format, so the service decodes the payload against a schema
registry named **on the publish request itself**. `publish.py` calls
`PutRawEvents` with `EventBusArn` set to the bus and
`SchemaRegistryConfiguration.RegistryUri` set to the Glue registry ARN. The
registry is not configured on the bus. EventBridge reads the registry with the
**caller's own credentials**, so the identity running `publish.py` needs Glue
read access on the registry (below).

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
      "Action": [
        "glue:GetSchemaVersion",
        "glue:GetSchemaByDefinition",
        "glue:GetRegistry"
      ],
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

- **Protobuf needs generated code.** `common/gen/order_placed_pb.py`
  is generated from `proto/order_placed.proto` by `scripts/generate.sh`
- **`Data` must carry the Glue wire header, not bare Protobuf.** The frame is
  `0x03` (version) + `0x00` (no compression) + the 16-byte schema-version UUID +
  a **message-index** varint + the Protobuf bytes. `common/protoio.py` builds
  this via `encode_framed(message, schema_version_id)`; the publisher looks the
  version id up with `glue:GetSchemaVersion`.
- **The message-index picks which message type to decode as.** Glue numbers the file's messages by full name sorted
  lexicographically (here `OrderItem`=0, `OrderPlaced`=1). A wrong index still
  publishes `PUBLISHED` but decodes as the wrong type (e.g. `OrderPlaced` arrived
  as `{"sku": "<orderId>", "qty": 0}`). `protoio.py` computes the index Glue's
  way, so adding or renaming messages keeps it correct.
- **Don't base64-encode before boto3.** `PutRawEvents` `Data` is a blob; the SDK
  does the wire encoding. Hand it the raw framed bytes.
- **EventBridge decodes the Protobuf server-side.** With a Glue registry named on
  the request, the delivered `Data` is a **decoded JSON object**, and
  `SystemMetadata` gains `aws:SchemaId` and `aws:RegistryType: Glue`. So the
  consumer needs no Protobuf library — it just reads JSON.
- **The Glue registry is named on each `PutRawEvents` request** (via
  `SchemaRegistryConfiguration.RegistryUri`), not on the bus. A registry set on
  the bus is ignored. The caller's own credentials read the registry.
- **IAM actions are `events:`, never `eventsv2:`.** `eventsv2` is only the
  CLI/SDK name; `eventsv2:` in a policy is accepted but grants nothing.
- **The Lambda receives a batch (a JSON array).** The handler iterates it.
- **Protobuf binary can't be filtered on `DATA`.** The bytes are opaque to a
  `DATA` pattern, so the subscriber filters on `METADATA`
  (`eventType = OrderPlaced`), and `METADATA` patterns accept only literal-scalar
  arrays — no operators.
- **The subscriber uses a `WITH_METADATA` transformer** so the Lambda receives the
  `Data` + `Metadata` + `SystemMetadata` envelope. The default `RAW` would deliver
  the payload alone, with no metadata.
- **The schema lives in two places that must match by hand.**
  `infra/template.yaml` inlines the same Protobuf schema as
  `proto/order_placed.proto`. There's no sync step — if you change one, edit the
  other, or the publisher and the Glue-registered schema drift and publishes fail
  to decode. Glue supports proto2/proto3 but not `extensions` or `groups`.
- **The delivery role is already least-privilege; add a source-account condition
  to harden it further.** The role trusts only `events.amazonaws.com` and is
  scoped to the specific Lambda and DLQ ARNs (no wildcards). For defense-in-depth
  in a shared or production account, add an `aws:SourceAccount` condition to the
  `lambda:InvokeFunction` and `sqs:SendMessage` statements so the permissions only
  apply in this account's EventBridge context:

  ```yaml
  - Effect: Allow
    Action: lambda:InvokeFunction
    Resource: !GetAtt ConsumerFunction.Arn
    Condition:
      StringEquals:
        aws:SourceAccount: !Ref AWS::AccountId
  - Effect: Allow
    Action: sqs:SendMessage
    Resource: !GetAtt DeadLetterQueue.Arn
    Condition:
      StringEquals:
        aws:SourceAccount: !Ref AWS::AccountId
  ```

  It is left off the base template to keep the delivery-role example minimal.
