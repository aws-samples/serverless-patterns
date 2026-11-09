# Ordered processing with a synchronous AWS Lambda target (TypeScript + SAM)

A runnable sample that shows an Amazon EventBridge custom event bus (the `eventsv2`
API) processing events in order by invoking an AWS Lambda function synchronously
(`InvocationType: REQUEST_RESPONSE`) from a FIFO subscriber.

![Architecture: publish.ts sends a sequence of OrderPlaced JSON events sharing one EventGroupId via PutEvents to an Amazon EventBridge custom event bus; a FIFO subscriber invokes a consumer AWS Lambda function synchronously (REQUEST_RESPONSE), waiting for each event to be confirmed before delivering the next; the function logs the sequence numbers in order to Amazon CloudWatch. No Amazon SQS queue sits between the bus and AWS Lambda.](docs/architecture.svg)

To support ordered processing, the custom event bus can invoke a target like
AWS Lambda synchronously. In synchronous mode the bus confirms the target
processed an event successfully before acknowledging it and delivering the next
event in the same group. That confirmation is what makes ordered, reliable,
direct-to-AWS Lambda processing possible — and it removes the common pattern of
placing an Amazon SQS queue between an event bus and AWS Lambda just to get
reliability and back-pressure.

This sample demonstrates it end to end:

- The publisher sends a sequence of `OrderPlaced` events that share one
  **`EventGroupId`**, each carrying a monotonically increasing `seq` (1, 2, 3, …).
- The **FIFO** subscriber invokes the consumer AWS Lambda function synchronously, waiting
  for each event to be confirmed before delivering the next in the group.
- The consumer logs `seq` as it processes. The Amazon CloudWatch log shows the sequence
  processed in order, one at a time — the observable proof of ordered,
  synchronous delivery.

> **Synchronous vs asynchronous.** `REQUEST_RESPONSE` makes the bus
> wait for the function and confirm success before advancing, which is what
> enables ordering and reliable direct delivery. `EVENT` invokes the function
> asynchronously (fire-and-forget), which cannot guarantee ordered, confirmed
> processing.

## Language

The publisher uses the AWS SDK for
JavaScript v3 (`@aws-sdk/client-eventbridgev2`), and the consumer AWS Lambda function runs on
the Node.js 24 runtime, bundled by AWS SAM with esbuild. Python and Java versions
of this pattern live in sibling `-python` / `-java` folders.

## Layout

```
eventbridge-custom-lambda-sync-sam-typescript/
  publisher/publish.ts         # PutEvents: a sequence of grouped OrderPlaced events (--count)
  consumer/handler.ts          # sync FIFO target: logs each order in processing order
  consumer/package.json        # marks the consumer as an ESM module for the esbuild build
  infra/template.yaml          # bus, FIFO subscriber, Lambda (nodejs24.x), DLQ (safety net), delivery role
  scripts/run_publish.sh       # convenience: publish an ordered sequence; print where to watch it
  scripts/deploy.sh            # convenience wrapper around sam build + sam deploy
  scripts/teardown.sh          # convenience wrapper around sam delete
  tests/                       # vitest: handler ordering, publisher grouping (aws-sdk-client-mock)
  package.json, tsconfig.json  # deps, build, and test config
  docs/architecture.svg        # the architecture diagram shown above
```

## Deployment model 

Everything is provisioned by one AWS SAM template (`infra/template.yaml`):
the event bus and the FIFO, synchronous subscriber (`AWS::EventsV2::EventBus` and
`AWS::EventsV2::Subscriber`), the consumer AWS Lambda function, an Amazon SQS dead-letter queue (safety
net), and the delivery role. AWS SAM builds the TypeScript consumer with esbuild.


## Prerequisites

- Node.js 22.12+ or 24+ (the publisher and tests run locally; the test runner,
  vitest 5, requires `^22.12.0 || ^24.0.0 || >=26.0.0`). The AWS Lambda function runs on
  `nodejs24.x`, so Node.js 24 locally matches it.
- AWS SAM CLI version 1.168.0+ and AWS Command Line Interface (AWS CLI) v2.
- AWS credentials for a **non-production** account, with permission to create an
  AWS Lambda function, an AWS Identity and Access Management (IAM) role, an Amazon SQS queue, and an Amazon EventBridge (EventsV2) bus + subscriber.
  Nothing here is tied to a specific account — pass any region; resource names
  come from the `AppName` parameter.
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

These cover the handler processing a batch in the order received, and the
publisher's grouping (each event carries the shared `EventGroupId`) and
result-checking — validated against the `EventBridgeV2Client` with
`aws-sdk-client-mock`, fully offline.

## Deploy

The whole stack (bus, FIFO subscriber, AWS Lambda function, DLQ, role) is one AWS CloudFormation
template, so a plain AWS SAM build + deploy is all you need:

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

The event bus ARN is in the stack outputs (`EventBusArn`) — read it with:

```bash
aws cloudformation describe-stacks --stack-name <stack-name> \
  --query "Stacks[0].Outputs" --output table
```

> There is also a `scripts/deploy.sh [stack-name] [region]` convenience wrapper
> that runs the same build + deploy non-interactively and prints the bus ARN.

> `sam build` runs esbuild for the TypeScript consumer. If you build without a
> local esbuild, use `sam build --use-container` (needs Docker); it builds in the
> AWS Lambda `nodejs24.x` image.

## Publish and verify

Publish an ordered sequence (default 5 events; pass a count to change it):

```bash
scripts/run_publish.sh [stack-name] [region] [count]
```

This runs the publisher with `npx tsx`. You can also run it directly:

```bash
BUS_ARN=<event-bus-arn> AWS_REGION=<region> npx tsx publisher/publish.ts --count 5
```

Give it a few seconds, then watch the consumer process the group in order:

```bash
aws logs tail /aws/lambda/sync-orders-consumer --since 5m --format short
```

The `Processing order ... seq=` lines appear in order — `seq=1`, then `seq=2`,
then `seq=3`, … — because the FIFO subscriber invokes the AWS Lambda function synchronously
and confirms each event before delivering the next.

## How ordered, synchronous processing is configured

The subscriber is defined in `infra/template.yaml` with two settings that work
together:

```yaml
Type: FIFO
InvokeConfiguration:
  TargetArn: <consumer lambda arn>
  RoleArn: <delivery role arn>
  LambdaParameters:
    InvocationType: REQUEST_RESPONSE
```

- **`Type: FIFO`** orders events within an event group.
- **`InvocationType: REQUEST_RESPONSE`** invokes the AWS Lambda function synchronously, so the
  bus waits for each event to be confirmed before delivering the next.

The publisher groups the sequence by setting **`SystemMetadata.EventGroupId`** on
each `PutEvents` entry; all events in a run share the same group id, so they are
ordered relative to one another.

The delivery role (trusted by `events.amazonaws.com`) has `lambda:InvokeFunction`
on the consumer and `sqs:SendMessage` on the dead-letter queue.


## Teardown

Everything is in the AWS CloudFormation stack, so deleting the stack removes the bus,
FIFO subscriber, AWS Lambda function, DLQ, and delivery role:

```bash
sam delete
```

`sam delete` uses the stack name saved in `samconfig.toml`; pass
`--stack-name <name> --region <region>` if you deployed without `--guided`.

> There is also a `scripts/teardown.sh [stack-name] [region]` convenience wrapper
> that deletes the stack and waits for completion.

## Key considerations

- **Ordering needs both FIFO and synchronous invocation.** `Type: FIFO` defines
  the order; `REQUEST_RESPONSE` makes the bus confirm each event before advancing,
  which is what actually enforces one-at-a-time, in-order delivery.
- **Events are ordered within an `EventGroupId`.** Give related events the same
  group id. Events in different groups are not ordered relative to each other.
- **No Amazon SQS buffer required.** Synchronous confirmation gives you the reliability
  and back-pressure people used to add an Amazon SQS queue between the bus and AWS Lambda to
  get. A DLQ is still attached as a terminal safety net.
- **A failing event blocks its group until it is dead-lettered.** On a FIFO
  subscriber, an event that cannot be delivered holds up later events with the
  same `EventGroupId` until it succeeds or exhausts retries. The subscriber sets
  an explicit `RetryPolicy` (`MaxRetryAttempts: 10`,
  `MaxEventAgeInSeconds: 3600`) so a poison event drains to the DLQ promptly and
  unblocks its group. Delivery stops at whichever limit is reached first. Lower
  values unblock the group sooner but give transient errors less time to clear.
- **The AWS Lambda function receives a batch (a JSON array).** The handler iterates it.
- **`PutEvents` delivers the classic envelope.** With the default `RAW`
  transformer the order fields are under `detail`; the handler reads `detail`
  (and tolerates top-level fields for hand-invocation).
- **IAM actions are `events:`, never `eventsv2:`.** `eventsv2` is only the
  CLI/SDK name; `eventsv2:` in a policy is accepted but grants nothing.
- **Account/region agnostic.** No account id or region is hardcoded; the stack
  names everything from `AppName`, and the scripts take a region argument.