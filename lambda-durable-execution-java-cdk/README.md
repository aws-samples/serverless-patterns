# Lambda Durable Execution with Java SDK

This pattern deploys a Lambda durable function written in Java that orchestrates a multi-step order processing workflow with automatic checkpointing and failure recovery.

Learn more about this pattern at Serverless Land Patterns: https://serverlessland.com/patterns/lambda-durable-execution-java-cdk

Important: this application uses various AWS services and there are costs associated with these services after the Free Tier usage - please see the [AWS Pricing page](https://aws.amazon.com/pricing/) for details. You are responsible for any AWS costs incurred. No warranty is implied in this example.

## Requirements

- [Create an AWS account](https://portal.aws.amazon.com/gp/aws/developer/registration/index.html) if you do not already have one and log in. The IAM user that you use must have sufficient permissions to make necessary AWS service calls and manage AWS resources.
- [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html) installed and configured
- [Git Installed](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)
- [Node and NPM](https://nodejs.org/en/download/) installed
- [AWS CDK](https://docs.aws.amazon.com/cdk/latest/guide/cli.html) installed
- [Java 17+](https://docs.aws.amazon.com/corretto/latest/corretto-17-ug/downloads-list.html) installed
- [Apache Maven](https://maven.apache.org/install.html) installed

## Deployment Instructions

1. Create a new directory, navigate to that directory in a terminal and clone the GitHub repository:
   ```bash
   git clone https://github.com/aws-samples/serverless-patterns
   ```
2. Change directory to the pattern directory:
   ```bash
   cd serverless-patterns/lambda-durable-execution-java-cdk
   ```
3. Build the Java Lambda function:
   ```bash
   cd src
   mvn clean package -q
   cd ..
   ```
4. Install CDK dependencies:
   ```bash
   npm install
   ```
5. Deploy the stack:
   ```bash
   cdk deploy
   ```

## How it works

This pattern uses the [AWS Lambda Durable Execution SDK for Java](https://github.com/aws/aws-durable-execution-sdk-java/) (GA April 2026) to build a resilient order processing workflow.

The Java function extends `DurableHandler<Map, Map>` and uses `DurableContext` to:

1. **Validate order** — `ctx.step()` checkpoints the validation result
2. **Reserve inventory** — `ctx.step()` checkpoints the reservation ID
3. **Process payment** — `ctx.step()` checkpoints the payment confirmation
4. **Wait for warehouse** — `ctx.wait()` suspends execution for 5 seconds with zero compute charges
5. **Confirm shipment** — `ctx.step()` checkpoints the tracking number

If the function is interrupted at any point, it replays from the beginning but skips completed steps using stored checkpoint results.

### Architecture

```
┌─────────────────────────────────────────────────────────┐
│                  Lambda Durable Function                 │
│                                                         │
│  ┌──────────┐  ┌──────────┐  ┌──────────┐  ┌────────┐ │
│  │ Validate │→ │ Reserve  │→ │ Process  │→ │  Wait  │ │
│  │  Order   │  │Inventory │  │ Payment  │  │ (free) │ │
│  └──────────┘  └──────────┘  └──────────┘  └────────┘ │
│       ↓ checkpoint   ↓ checkpoint   ↓ checkpoint  │     │
│                                                   ↓     │
│                                            ┌──────────┐ │
│                                            │ Confirm  │ │
│                                            │ Shipment │ │
│                                            └──────────┘ │
└─────────────────────────────────────────────────────────┘
```

### Key Java SDK concepts

- **`DurableHandler<I, O>`** — Base class for durable functions. Extend this and implement `handleRequest(I input, DurableContext ctx)`.
- **`ctx.step(name, type, fn)`** — Execute code with automatic checkpointing and retry support.
- **`ctx.wait(name, duration)`** — Suspend execution without compute charges.
- **`ctx.invoke()`** — Invoke another Lambda function and wait for the result.
- **`ctx.map()`** — Apply a function across a collection concurrently.
- **`ctx.parallel()`** — Run multiple operations concurrently.

## Testing

1. After deployment, note the `FunctionAliasArn` output.

2. Invoke the durable function using the alias ARN:
   ```bash
   aws lambda invoke \
     --function-name <FunctionAliasArn> \
     --payload '{"orderId": "ORD-001", "amount": 149.99}' \
     --cli-binary-format raw-in-base64-out \
     output.json

   cat output.json
   ```

3. Expected output:
   ```json
   {
     "orderId": "ORD-001",
     "status": "COMPLETED",
     "validation": "VALIDATED",
     "reservationId": "RES-a1b2c3d4",
     "paymentId": "PAY-e5f6g7h8",
     "trackingNumber": "TRACK-i9j0k1l2"
   }
   ```

4. Monitor the durable execution in the Lambda console under the **Durable executions** tab.

## Cleanup

```bash
cdk destroy
```

---

Copyright 2026 Amazon.com, Inc. or its affiliates. All Rights Reserved.

SPDX-License-Identifier: MIT-0
