# Amazon Bedrock Async Invoke with AWS Lambda durable functions

This pattern shows how to use AWS Lambda durable functions to orchestrate [Amazon Bedrock Async Invoke](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_runtime_StartAsyncInvoke.html) for AI video generation. The durable function starts an Amazon Nova Reel video generation job, then polls for completion using `waitForCondition` with exponential backoff. During each polling interval the function suspends execution entirely, incurring zero compute charges while Bedrock processes the video.

Without durable functions this pattern would require a separate polling mechanism such as Step Functions, EventBridge rules, or a cron-based poller. Here the entire workflow is a single, linear function that reads top-to-bottom.

Learn more about this pattern at Serverless Land Patterns: [https://serverlessland.com/patterns/lambda-durable-bedrock-async-invoke](https://serverlessland.com/patterns/lambda-durable-bedrock-async-invoke)

Important: this application uses various AWS services and there are costs associated with these services after the Free Tier usage - please see the [AWS Pricing page](https://aws.amazon.com/pricing/) for details. You are responsible for any AWS costs incurred. No warranty is implied in this example.

## Requirements

* [Create an AWS account](https://portal.aws.amazon.com/gp/aws/developer/registration/index.html) if you do not already have one and log in. The IAM user that you use must have sufficient permissions to make necessary AWS service calls and manage AWS resources.
* [AWS CLI v2](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html) (latest available version) installed and configured
* [Git Installed](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)
* [AWS CDK](https://docs.aws.amazon.com/cdk/latest/guide/getting_started.html) (version 2.232.1 or later) installed and configured
* [Node.js 22.x](https://nodejs.org/) installed
* Amazon Bedrock model access enabled for **Amazon Nova Reel** (`amazon.nova-reel-v1:1`) in your target region

## Deployment Instructions

1. Create a new directory, navigate to that directory in a terminal and clone the GitHub repository:

    ```bash
    git clone https://github.com/aws-samples/serverless-patterns
    ```

1. Change directory to the pattern directory:

    ```bash
    cd lambda-durable-bedrock-async-invoke
    ```

1. Install the project dependencies:

    ```bash
    npm install
    ```

1. Deploy the CDK stack:

    ```bash
    npx cdk deploy
    ```

    The stack creates:
    - An S3 bucket for video output (auto-deleted on stack destroy, 7-day lifecycle)
    - A durable Lambda function with 30-minute execution timeout
    - IAM permissions for Bedrock and S3 access
    - A CloudWatch log group with 1-week retention

1. Note the outputs from the CDK deployment process. These contain the resource names and ARNs used for testing.

## How it works

The durable function performs three logical phases:

1. **`start-video-generation` step** — calls `StartAsyncInvoke` with a `clientRequestToken` for Bedrock-level idempotency. Because this runs inside a durable step, the Bedrock invocation ARN is checkpointed and will not be re-executed on replay.

2. **`wait-for-video-ready` waitForCondition** — polls `GetAsyncInvoke` with exponential backoff (30 s → 60 s cap). The function suspends during each wait interval, consuming no compute time while the video is being generated.

3. **`build-result` step** — assembles the final response with the S3 output location and metadata, or throws an error if the generation failed.

```
Client ──► Lambda (durable) ──► Bedrock StartAsyncInvoke ──► S3 (video output)
               │                           │
               │  ◄── waitForCondition ──► │
               │       (poll with          │
               │        exponential        │
               │        backoff)           │
               │                           │
               └── GetAsyncInvoke ─────────┘
```

Key concepts:

| Concept | How it is used |
|---|---|
| `step` | Wraps the `StartAsyncInvoke` call so it is checkpointed and never re-executed on replay |
| `waitForCondition` | Polls `GetAsyncInvoke` with exponential backoff; the function suspends between polls |
| `clientRequestToken` | Bedrock idempotency token generated inside a step, ensuring replays cannot create duplicate invocations |
| `context.logger` | Replay-aware structured logging throughout the workflow |
| S3 output | Bedrock writes the generated video directly to an S3 bucket provisioned by CDK |

## Testing

After deployment, invoke the durable function using the AWS CLI.

Because the durable execution timeout is 30 minutes (exceeding Lambda's 15-minute synchronous limit), you must invoke the function **asynchronously**. Use `--durable-execution-name` for idempotency at the Lambda level.

### Invoke the durable function

```bash
aws lambda invoke \
  --function-name 'video-generator-durable:$LATEST' \
  --invocation-type Event \
  --durable-execution-name "my-beach-video-001" \
  --payload '{"prompt":"A golden retriever playing fetch on a sunny beach","durationSeconds":6}' \
  --cli-binary-format raw-in-base64-out \
  response.json
```

Repeat the same command with the same `--durable-execution-name` to safely retry without creating a duplicate execution.

### Check execution status

```bash
aws lambda get-durable-execution \
  --function-name 'video-generator-durable:$LATEST' \
  --durable-execution-name "my-beach-video-001"
```

Once the status shows `SUCCEEDED`, the result will contain the S3 URI where the video was written.

### Run unit tests

```bash
npm test
```

This runs both CDK infrastructure tests and durable handler tests (with mocked Bedrock calls).

## Cleanup

1. Delete the stack:

    ```bash
    npx cdk destroy
    ```

1. Confirm the stack has been deleted by checking the AWS CloudFormation console or running:

    ```bash
    aws cloudformation list-stacks --stack-status-filter DELETE_COMPLETE
    ```

----
Copyright 2026 Amazon.com, Inc. or its affiliates. All Rights Reserved.

SPDX-License-Identifier: MIT-0
