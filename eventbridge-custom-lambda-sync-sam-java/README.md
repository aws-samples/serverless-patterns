# Ordered processing with a synchronous Lambda target (Java + CloudFormation)

A runnable sample that shows an EventBridge custom event bus (the `eventsv2`
API) processing events in order by invoking a Lambda synchronously
(`InvocationType: REQUEST_RESPONSE`) from a **FIFO subscriber**.

![Architecture: Publisher.java sends a sequence of OrderPlaced JSON events sharing one EventGroupId via PutEvents to an EventBridge custom event bus; a FIFO subscriber invokes a consumer Lambda synchronously (REQUEST_RESPONSE), waiting for each event to be confirmed before delivering the next; the Lambda logs the sequence numbers in order to CloudWatch. No SQS queue sits between the bus and Lambda.](docs/architecture.svg)

To support ordered processing, the custom event bus can invoke a target like
Lambda synchronously. In synchronous mode the bus confirms the target
processed an event successfully before acknowledging it and delivering the next
event in the same group. That confirmation is what makes ordered, reliable,
direct-to-Lambda processing possible — and it removes the common pattern of
placing an Amazon SQS queue between an event bus and Lambda just to get
reliability and back-pressure.

This sample demonstrates it end to end:

- The publisher sends a sequence of `OrderPlaced` events that share one
  **`EventGroupId`**, each carrying a monotonically increasing `seq` (1, 2, 3, …).
- The **FIFO** subscriber invokes the consumer Lambda synchronously, waiting
  for each event to be confirmed before delivering the next in the group.
- The consumer logs `seq` as it processes. The CloudWatch log shows the sequence
  processed in order, one at a time — the observable proof of ordered,
  synchronous delivery.

> **Synchronous vs asynchronous.** `REQUEST_RESPONSE` (this sample) makes the bus
> wait for the function and confirm success before advancing, which is what
> enables ordering and reliable direct delivery. `EVENT` invokes the function
> asynchronously (fire-and-forget), which cannot guarantee ordered, confirmed
> processing.

This sample uses plain JSON (`PutEvents`), so there is no schema registry or
codegen — the focus is the subscriber's ordering and invocation configuration.

## Language

This is the **Java** version. The publisher uses the AWS SDK for Java v2
(`software.amazon.awssdk:eventbridgev2`), and the consumer Lambda runs on the
**Java 21** runtime, built by SAM with Maven. Python and TypeScript versions of
this pattern live in sibling `-python` / `-typescript` folders.

## Layout

```
eventbridge-custom-lambda-sync-sam-java/
  src/main/java/com/example/orders/Publisher.java  # PutEvents: a sequence of grouped OrderPlaced events (--count)
  src/main/java/com/example/orders/Consumer.java    # sync FIFO target: logs each order in processing order
  src/test/java/com/example/orders/                 # JUnit 5 + Mockito: handler ordering, publisher grouping
  pom.xml                                            # java21, eventbridgev2 SDK, shade (fat jar), JUnit/Mockito
  docs/architecture.svg                              # the architecture diagram shown above
  infra/template.yaml                                # bus, FIFO subscriber, Lambda (java21), DLQ, delivery role
  scripts/run_publish.sh                             # convenience: publish an ordered sequence; print where to watch it
  scripts/deploy.sh                                  # convenience wrapper around sam build + sam deploy
  scripts/teardown.sh                                # convenience wrapper around sam delete
```

## Deployment model (all CloudFormation)

Everything is provisioned by one CloudFormation template (`infra/template.yaml`):
the event bus and the FIFO, synchronous subscriber (`AWS::EventsV2::EventBus` and
`AWS::EventsV2::Subscriber`), the consumer Lambda, a dead-letter queue (safety
net), and the delivery role. SAM builds the Java consumer with Maven.

> Note: `cfn-lint` may flag the `AWS::EventsV2::*` resources with `E3006`
> ("resource type does not exist") if its bundled resource spec has not caught
> up yet. The types deploy fine; this is a stale-spec false positive.

## Prerequisites

- JDK 21 and Apache Maven (the consumer runs on the `java21` Lambda runtime; the
  publisher and tests build and run locally).
- AWS SAM CLI and AWS CLI v2.
- AWS credentials for a **non-production** account, with permission to create a
  Lambda function, an IAM role, an SQS queue, and an EventsV2 bus + subscriber.
  Nothing here is tied to a specific account — pass any region; resource names
  come from the `AppName` parameter.
- The new custom event bus (`eventsv2`) available in your Region — confirm with
  `aws eventsv2 list-event-buses`.

## Run the tests 

```bash
mvn test
```

These cover the handler processing a batch in the order received, and the
publisher's grouping (each event carries the shared `EventGroupId`) and
result-checking — validated against a Mockito-mocked `EventBridgeV2Client`,
fully offline.

## Deploy

The whole stack (bus, FIFO subscriber, Lambda, DLQ, role) is one CloudFormation
template, so a plain SAM build + deploy is all you need:

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

> `sam build` runs Maven for the Java consumer. If you build without a local JDK
> 21 / Maven, use `sam build --use-container` (needs Docker); it builds in the
> Lambda `java21` image.

## Publish and verify

Publish an ordered sequence (default 5 events; pass a count to change it):

```bash
scripts/run_publish.sh [stack-name] [region] [count]
```

This builds the publisher's shaded jar (`mvn package`) if needed and runs it with
`java -jar`. You can also run it directly after `mvn package`:

```bash
BUS_ARN=<event-bus-arn> AWS_REGION=<region> \
  java -jar target/eventbridge-custom-lambda-sync-sam-java-1.0.0.jar --count 5
```

Give it a few seconds, then watch the consumer process the group in order:

```bash
aws logs tail /aws/lambda/sync-orders-consumer --since 5m --format short
```

The `Processing order ... seq=` lines appear in order — `seq=1`, then `seq=2`,
then `seq=3`, … — because the FIFO subscriber invokes the Lambda synchronously
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
- **`InvocationType: REQUEST_RESPONSE`** invokes the Lambda synchronously, so the
  bus waits for each event to be confirmed before delivering the next.

The publisher groups the sequence by setting **`SystemMetadata.EventGroupId`** on
each `PutEvents` entry (in the Java SDK, `PutEventsSystemMetadata.builder()
.eventGroupId(group)`); all events in a run share the same group id, so they are
ordered relative to one another.

The delivery role (trusted by `events.amazonaws.com`) has `lambda:InvokeFunction`
on the consumer and `sqs:SendMessage` on the dead-letter queue.

## Teardown

Everything is in the CloudFormation stack, so deleting the stack removes the bus,
FIFO subscriber, Lambda, DLQ, and delivery role:

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
- **No SQS buffer required.** Synchronous confirmation gives you the reliability
  and back-pressure people used to add an SQS queue between the bus and Lambda to
  get. A DLQ is still attached as a terminal safety net.
- **The Lambda receives a batch (a JSON array).** The handler iterates it. Lambda
  deserializes the delivery into a `List<Map<String,Object>>`.
- **`PutEvents` delivers the classic envelope.** With the default `RAW`
  transformer the order fields are under `detail`; the handler reads `detail`
  (and tolerates top-level fields for hand-invocation).
- **IAM actions are `events:`, never `eventsv2:`.** `eventsv2` is only the
  CLI/SDK name; `eventsv2:` in a policy is accepted but grants nothing.
- **JVM cold start.** The consumer is given 512 MB (vs. 256 for the Python/TS
  versions) for JVM cold-start headroom; tune to taste.
- **Account/region agnostic.** No account id or region is hardcoded; the stack
  names everything from `AppName`, and the scripts take a region argument.