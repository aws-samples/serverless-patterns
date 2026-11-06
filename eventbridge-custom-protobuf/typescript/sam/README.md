# Amazon EventBridge custom event bus to AWS Lambda with Protobuf and AWS Glue Schema Registry

This pattern publishes a rich domain event, Protobuf-encoded, to a new Amazon
EventBridge custom event bus (the `eventsv2` API) using `PutRawEvents` with an
AWS Glue Schema Registry, then delivers that same event to an AWS Lambda
subscriber that logs it to Amazon CloudWatch, proving the event survives the
round trip intact.

This is the TypeScript version. The publisher uses the AWS SDK for JavaScript v3
(`@aws-sdk/client-eventbridgev2` and `@aws-sdk/client-glue`) and
[`protobufjs`](https://www.npmjs.com/package/protobufjs), which loads
`proto/order_placed.proto` at runtime, so there is no codegen step and no
generated bindings to commit. The consumer Lambda runs on the Node.js 24
runtime, bundled by SAM with esbuild.

Learn more about this pattern at Serverless Land Patterns: https://serverlessland.com/patterns/eventbridge-custom-protobuf-typescript-sam

Important: this application uses various AWS services and there are costs associated with these services after the Free Tier usage - please see the [AWS Pricing page](https://aws.amazon.com/pricing/) for details. You are responsible for any AWS costs incurred. No warranty is implied in this example.

## Requirements

* [Create an AWS account](https://portal.aws.amazon.com/gp/aws/developer/registration/index.html) if you do not already have one and log in. Use a **non-production** account. The IAM user that you use must have sufficient permissions to create an EventsV2 event bus and subscriber, a Glue registry and schema, a Lambda function, an IAM role, and an SQS queue.
* [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html) **v2.37.3 or later**, installed and configured. Check with `aws --version`. This is the first release with `aws eventsv2` (v2.37.2 shipped it as `aws eventbridgev2`).
* [AWS Serverless Application Model](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-sam-cli-install.html) (AWS SAM) CLI **v1.168.0 or later**. Check with `sam --version`.
* [Git Installed](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)
* [Node.js](https://nodejs.org/) 20 or later, to run the publisher and the tests locally. Check with `node --version`.
* The new custom event bus (`eventsv2`) available in your Region. Confirm with `aws eventsv2 list-event-buses`.

## Deployment Instructions

1. Create a new directory, navigate to that directory in a terminal and clone the GitHub repository:
    ```bash
    git clone https://github.com/aws-samples/serverless-patterns
    ```
1. Change directory to the pattern directory:
    ```bash
    cd serverless-patterns/eventbridge-custom-protobuf/typescript/sam
    ```
1. Install dependencies (used by the publisher, the tests, and the esbuild step):
    ```bash
    npm install
    ```
1. Build the consumer Lambda:
    ```bash
    sam build
    ```
    If you don't have esbuild locally, use `sam build --use-container` (needs Docker).
1. Deploy the AWS resources:
    ```bash
    sam deploy --guided --capabilities CAPABILITY_NAMED_IAM
    ```
    The stack creates a role with an explicit name (`<AppName>-delivery-role`), which requires `CAPABILITY_NAMED_IAM`. The guided flow does not prompt for it, so pass it on the command line as shown.
1. During the prompts:
    * Enter a stack name
    * Enter the desired AWS Region
    * Accept or change the `AppName` (resource name prefix) and `RetentionInDays` parameters
    * Allow SAM CLI to create IAM roles with the required permissions.

    Once you have run `sam deploy --guided` mode once and saved arguments to a configuration file (samconfig.toml), you can use `sam deploy` in future to use these defaults.
1. Note the outputs from the SAM deployment process. These contain the event bus ARN (`EventBusArn`) and the Glue registry ARN (`SchemaRegistryArn`) used for testing. You can read them again with:
    ```bash
    aws cloudformation describe-stacks --stack-name <stack-name> \
      --query "Stacks[0].Outputs" --output table
    ```

`scripts/deploy.sh [stack-name] [region]` is a convenience wrapper that runs the same build and deploy non-interactively and prints those ARNs.

## How it works

One template (`template.yaml`) provisions the event bus and subscriber (`AWS::EventsV2::EventBus` and `AWS::EventsV2::Subscriber`), the Glue registry and Protobuf schema, the consumer Lambda, an SQS dead-letter queue, and the delivery role.

1. `publisher/publish.ts` looks up the latest `OrderPlaced` schema-version id with `glue:GetSchemaVersion`, Protobuf-encodes an `OrderPlaced` event, and wraps it in the Glue wire format.
1. It calls `PutRawEvents` with `EventBusArn` set to the bus and `SchemaRegistryConfiguration.RegistryUri` set to the Glue registry ARN. The registry is named on the publish request, not configured on the bus.
1. EventBridge decodes the Protobuf against the Glue registry server-side, using the **caller's own credentials**.
1. The subscriber filters on `METADATA` (`eventType = OrderPlaced`) and uses a `WITH_METADATA` transformer, so the Lambda receives the `Data` + `Metadata` + `SystemMetadata` envelope with `Data` as plain JSON.
1. `consumer/handler.ts` logs each delivered event. A matching `orderId`, fields, and metadata prove the delivered event equals the one that was published. Failed deliveries go to the dead-letter queue.

Project layout:

```
eventbridge-custom-protobuf/typescript/sam/
  proto/order_placed.proto     # Protobuf schema, the source of truth (loaded at runtime)
  common/protoio.ts            # protobufjs encode/decode + Glue wire framing (with message index)
  publisher/publish.ts         # Protobuf-encode + PutRawEvents with a per-request Glue registry
  consumer/handler.ts          # Lambda: logs the server-decoded JSON event
  consumer/package.json        # marks the consumer as ESM + esbuild for the SAM build
  template.yaml                # bus, subscriber, Glue registry+schema, Lambda (nodejs24.x), DLQ, role
  scripts/run_publish.sh       # convenience: publish one event, print the log command
  scripts/deploy.sh            # convenience wrapper around sam build + sam deploy
  scripts/teardown.sh          # convenience wrapper around stack deletion
  tests/                       # vitest: round-trip, framing, message index, handler, publisher
  package.json, tsconfig.json  # deps, build, and test config
```

### Publisher IAM

The identity running the publisher needs `events:PutRawEvents` on the bus, plus Glue read on the registry: `glue:GetSchemaVersion` so the publisher can resolve the schema-version id for the wire header, and the read actions the service uses to decode.

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

## Testing

### Unit tests (offline)

```bash
npm test
```

These cover the Protobuf round trip (including the Glue wire framing and the
message index), the publisher's request shaping, schema-version lookup, and
result handling (against `EventBridgeV2Client` and `GlueClient` mocked with
`aws-sdk-client-mock`), and the Lambda handler processing a delivered event.

### End to end

1. Publish one `OrderPlaced` event. The script reads the bus and Glue registry ARNs from the stack outputs:
    ```bash
    scripts/run_publish.sh <stack-name> <region> [order-id]
    ```
    Or run the publisher directly:
    ```bash
    BUS_ARN=<bus-arn> REGISTRY_ARN=<registry-arn> AWS_REGION=<region> \
      npx tsx publisher/publish.ts --order-id order-123
    ```
    A successful publish prints `SuccessCode=PUBLISHED` and an `EventId`.
1. After a few seconds, check the delivered event in CloudWatch:
    ```bash
    aws logs tail /aws/lambda/proto-orders-consumer --since 5m --format short
    ```
    You should see an `OrderPlaced[...]` line with the `orderId` you published, the full record (delivered as JSON), the custom `metadata`, and the Glue `schemaId` the service used to decode it.
1. The dead-letter queue (`DeadLetterQueueUrl` output) should stay empty on a healthy run.

## Cleanup

1. Delete the stack. This removes the bus, subscriber, Glue registry and schema, Lambda, DLQ, and delivery role:
    ```bash
    sam delete
    ```
    `sam delete` uses the stack name saved in `samconfig.toml`; pass `--stack-name <name> --region <region>` if you deployed without `--guided`.
1. Confirm the stack has been deleted:
    ```bash
    aws cloudformation list-stacks --query "StackSummaries[?contains(StackName,'STACK_NAME')].StackStatus"
    ```

`scripts/teardown.sh [stack-name] [region]` is a convenience wrapper that deletes the stack and waits for completion.

----
Copyright 2026 Amazon.com, Inc. or its affiliates. All Rights Reserved.

SPDX-License-Identifier: MIT-0
