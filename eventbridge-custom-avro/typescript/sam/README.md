# Amazon EventBridge custom event bus to AWS Lambda with Avro and AWS Glue Schema Registry

This pattern publishes a rich domain event, Avro-encoded, to an Amazon EventBridge custom event bus (the `eventsv2` API) using `PutRawEvents` with an AWS Glue Schema Registry. EventBridge decodes the Avro server-side and delivers the event as JSON to an AWS Lambda subscriber, which logs it to Amazon CloudWatch, showing the event survives the round trip intact.

The publisher uses the AWS SDK for JavaScript v3 (`@aws-sdk/client-eventbridgev2` and `@aws-sdk/client-glue`) and the [`avsc`](https://www.npmjs.com/package/avsc) library for Avro encoding. The consumer Lambda runs on the Node.js 24 runtime, bundled by AWS SAM with esbuild.

Learn more about this pattern at Serverless Land Patterns: https://serverlessland.com/patterns/eventbridge-custom-avro-typescript-sam

Important: this application uses various AWS services and there are costs associated with these services after the Free Tier usage - please see the [AWS Pricing page](https://aws.amazon.com/pricing/) for details. You are responsible for any AWS costs incurred. No warranty is implied in this example.

## Requirements

* [Create an AWS account](https://portal.aws.amazon.com/gp/aws/developer/registration/index.html) if you do not already have one and log in. The IAM user that you use must have sufficient permissions to make necessary AWS service calls and manage AWS resources: an EventsV2 event bus and subscriber, a Glue registry and schema, a Lambda function, an IAM role, and an SQS queue. Use a non-production account.
* [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html) v2 installed and configured
* [Git Installed](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)
* [AWS Serverless Application Model](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-sam-cli-install.html) (AWS SAM) installed
* [Node.js](https://nodejs.org/) 20 or later (the publisher and the tests run locally; the Lambda runs on `nodejs24.x`)
* The new custom event bus (`eventsv2`) available in your Region. Confirm with `aws eventsv2 list-event-buses`.

## Deployment Instructions

1. Create a new directory, navigate to that directory in a terminal and clone the GitHub repository:
    ```bash
    git clone https://github.com/aws-samples/serverless-patterns
    ```
1. Change directory to the pattern directory:
    ```bash
    cd serverless-patterns/eventbridge-custom-avro/typescript/sam
    ```
1. Install dependencies (used by the publisher, the tests, and the esbuild step of `sam build`):
    ```bash
    npm install
    ```
1. Build the consumer Lambda. `sam build` runs esbuild for the TypeScript handler. If you don't have esbuild available locally, use `sam build --use-container` (needs Docker), which builds in the Lambda `nodejs24.x` image.
    ```bash
    sam build
    ```
1. From the command line, use AWS SAM to deploy the AWS resources for the pattern as specified in the `template.yaml` file:
    ```bash
    sam deploy --guided --capabilities CAPABILITY_NAMED_IAM
    ```
    The stack creates a role with an explicit name (`<AppName>-delivery-role`), which requires `CAPABILITY_NAMED_IAM`. The guided flow does not prompt for it, so pass it on the command line as shown.
1. During the prompts:
    * Enter a stack name
    * Enter the desired AWS Region
    * Accept or change the `AppName` (resource-name prefix), `RetentionInDays` (bus replay window) and `LogRetentionInDays` (consumer log retention) parameters
    * Allow SAM CLI to create IAM roles with the required permissions.

    Once you have run `sam deploy --guided` mode once and saved arguments to a configuration file (samconfig.toml), you can use `sam deploy` in future to use these defaults.
1. Note the outputs from the SAM deployment process. These contain the resource names and ARNs used for testing, including `EventBusArn`, `SchemaRegistryArn` and `ConsumerLogGroup`. You can read them again at any time:
    ```bash
    aws cloudformation describe-stacks --stack-name <stack-name> \
      --query "Stacks[0].Outputs" --output table
    ```

There is also a `scripts/deploy.sh [stack-name] [region]` convenience wrapper that runs the same build and deploy non-interactively and prints those ARNs.

## How it works

`template.yaml` provisions the whole pattern: the event bus and subscriber (`AWS::EventsV2::EventBus` and `AWS::EventsV2::Subscriber`), the Glue registry and Avro schema, the consumer Lambda and its CloudWatch log group (with a retention period), an SQS dead-letter queue, and the role EventBridge assumes to deliver.

1. `publisher/publish.ts` looks up the latest `OrderPlaced` schema-version id with `glue:GetSchemaVersion`.
1. It encodes an `OrderPlaced` record with `schema/order_placed.avsc` and wraps the Avro bytes in the Glue wire format (`common/avroio.ts`).
1. It calls `PutRawEvents` with `EventBusArn` set to the bus and `SchemaRegistryConfiguration.RegistryUri` set to the Glue registry ARN. The registry is named on the request, not configured on the bus.
1. EventBridge decodes the Avro against the Glue registry server-side, using the caller's own credentials.
1. The subscriber matches on `METADATA` (`eventType = OrderPlaced`) and delivers the event, with a `WITH_METADATA` transformer, to the consumer Lambda. Failed deliveries go to the dead-letter queue.
1. `consumer/handler.ts` receives a batch (a JSON array) of decoded events and logs each one to CloudWatch.

### Publisher IAM

EventBridge reads the registry with the caller's credentials, so the identity running `publish.ts` needs `events:PutRawEvents` on the bus plus Glue read on the registry: `glue:GetSchemaVersion` (to resolve the schema-version id for the wire header) and the reads the service uses to decode.

```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": ["events:PutRawEvents"],
      "Resource": "arn:aws:events:<region>:<account>:event-busv2/<AppName>-bus/*"
    },
    {
      "Effect": "Allow",
      "Action": ["glue:GetSchemaVersion", "glue:GetSchemaByDefinition", "glue:GetRegistry"],
      "Resource": [
        "arn:aws:glue:<region>:<account>:registry/<AppName>-registry",
        "arn:aws:glue:<region>:<account>:schema/<AppName>-registry/*"
      ]
    }
  ]
}
```

### Key considerations

- **`Data` must carry the Glue wire header, not bare Avro.** The frame is `0x03` (version) + `0x00` (no compression) + the 16-byte schema-version UUID + the Avro bytes. Bare Avro is rejected with `Malformed Glue wire format`.
- **`Data` is raw bytes (a `Uint8Array`).** Don't base64-encode before the SDK; the SDK does the wire encoding.
- **EventBridge decodes the Avro server-side.** The delivered `Data` is a decoded JSON object, and `SystemMetadata` gains `aws:SchemaId` and `aws:RegistryType: Glue`. The consumer needs no Avro library.
- **IAM actions are `events:`, never `eventsv2:`.** `eventsv2` is only the CLI/SDK name; `eventsv2:` in a policy is accepted but grants nothing.
- **The Lambda receives a batch (a JSON array).** The handler iterates it.
- **The subscriber filters on `METADATA`, but a `DATA` filter works too.** With `ContentType: application/avro` and a registry on the request, EventBridge deserializes the payload to JSON first and then evaluates subscriber filters against that JSON, so a `DATA` pattern matches the decoded record's fields by their schema names (for example `{"currency":["USD"]}`). Only `application/octet-stream` payloads are left opaque. See [Supported content types](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-custom-bus-open-formats.html). This pattern filters on the publisher's `eventType` metadata key so routing stays independent of the record's fields.
- **The subscriber uses a `WITH_METADATA` transformer** so the Lambda receives the `Data` + `Metadata` + `SystemMetadata` envelope. The default `RAW` would deliver the payload alone.
- **The schema lives in two places that must match by hand.** `template.yaml` inlines the same Avro schema as `schema/order_placed.avsc` (compact form). If you change one, edit the other, or publishes fail to decode.
- **`cfn-lint` and `AWS::EventsV2::*`.** cfn-lint's bundled resource spec may not include these types yet (`E3006`). The template suppresses that one check on the two EventsV2 resources so `sam validate --lint` passes.

## Testing

### Unit tests (offline)

```bash
npm test
```

These cover the Avro encoding and Glue wire framing, the publisher's request shaping, schema-version lookup and result handling (against mocked `EventBridgeV2Client` and `GlueClient` using `aws-sdk-client-mock`), and the Lambda handler processing a delivered event. They make no AWS calls.

### End-to-end

1. Publish one `OrderPlaced` event. The script reads the bus and registry ARNs from the stack outputs:
    ```bash
    scripts/run_publish.sh <stack-name> <region> order-123
    ```
    Or run the publisher directly with the `EventBusArn` and `SchemaRegistryArn` outputs:
    ```bash
    BUS_ARN=<bus-arn> REGISTRY_ARN=<registry-arn> AWS_REGION=<region> \
      npx tsx publisher/publish.ts --order-id order-123
    ```
    Expected output:
    ```
    Published orderId=order-123 -> SuccessCode=PUBLISHED EventId=...
    ```
1. Watch the delivered event in CloudWatch, using the `ConsumerLogGroup` stack output:
    ```bash
    aws logs tail <consumer-log-group> --since 5m --format short
    ```
    You should see an `OrderPlaced[0]: ...` line with the `orderId` you published, the full record (delivered as JSON), the custom `metadata`, and the Glue `schemaId` the service used to decode it.
1. Confirm the dead-letter queue is empty (use the `DeadLetterQueueUrl` output):
    ```bash
    aws sqs get-queue-attributes --queue-url <dlq-url> \
      --attribute-names ApproximateNumberOfMessages
    ```

You can also invoke the consumer directly with a delivered-event shape:

```bash
aws lambda invoke --function-name <AppName>-consumer \
  --cli-binary-format raw-in-base64-out \
  --payload '[{"Data":{"orderId":"order-123","customerId":"cust-987","amount":129.95,"currency":"USD","items":[{"sku":"SKU-1","qty":2}],"placedAt":1789601953851},"Metadata":{"eventType":"OrderPlaced"},"SystemMetadata":{"aws:RegistryType":"Glue"}}]' \
  output.json
```

## Cleanup

1. Delete the stack. This removes the bus, subscriber, Glue registry and schema, Lambda and its log group, DLQ, and delivery role:
    ```bash
    sam delete
    ```
    `sam delete` uses the stack name saved in `samconfig.toml`; pass `--stack-name <name> --region <region>` if you deployed without `--guided`. There is also a `scripts/teardown.sh [stack-name] [region]` wrapper that deletes the stack and waits for completion.
1. Confirm the stack has been deleted:
    ```bash
    aws cloudformation list-stacks --query "StackSummaries[?contains(StackName,'STACK_NAME')].StackStatus"
    ```

----
Copyright 2026 Amazon.com, Inc. or its affiliates. All Rights Reserved.

SPDX-License-Identifier: MIT-0
