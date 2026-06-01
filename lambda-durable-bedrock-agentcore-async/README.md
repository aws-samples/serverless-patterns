# Asynchronous Amazon Bedrock AgentCore integration with AWS Lambda durable functions

This pattern shows how to asynchronously invoke an agent running on Amazon Bedrock AgentCore from AWS Lambda durable functions. The durable function uses `context.map` durable operation to fan out two trip-planning prompts in parallel, each using `waitForCallback` to pause while the agent processes the request via the Strands Agents SDK. When both agents complete, the results are combined into a single response.

Learn more about this pattern at Serverless Land Patterns: [https://serverlessland.com/patterns/lambda-durable-bedrock-agentcore-async](https://serverlessland.com/patterns/lambda-durable-bedrock-agentcore-async)

Important: this application uses various AWS services and there are costs associated with these services after the Free Tier usage - please see the [AWS Pricing page](https://aws.amazon.com/pricing/) for details. You are responsible for any AWS costs incurred. No warranty is implied in this example.

## Requirements

* [Create an AWS account](https://portal.aws.amazon.com/gp/aws/developer/registration/index.html) if you do not already have one and log in. The IAM user that you use must have sufficient permissions to make necessary AWS service calls and manage AWS resources.
* [AWS CLI v2](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html) (latest available version) installed and configured
* [Git Installed](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)
* [AWS CDK](https://docs.aws.amazon.com/cdk/latest/guide/getting_started.html) (version 2.221.0 or later) installed and configured
* [Node.js 22.x](https://nodejs.org/) installed
* [Finch](https://runfinch.com/), [Docker](https://www.docker.com/products/docker-desktop/) or a compatible tool (required to build the agent container image)

## Deployment Instructions

1. Create a new directory, navigate to that directory in a terminal and clone the GitHub repository:

    ```bash
    git clone https://github.com/aws-samples/serverless-patterns
    ```

1. Change directory to the pattern directory:

    ```bash
    cd lambda-durable-bedrock-agentcore-async
    ```

1. Install the project dependencies:

    ```bash
    npm install
    ```

1. Install the Lambda durable functions dependencies:

    ```bash
    cd durable-lambda && npm install && cd ..
    ```

1. Deploy the CDK stacks:

    ```bash
    cdk deploy --all
    ```

    Note: This deploys two stacks — `AgentCoreStrandsStack` (the agent runtime) and `DurableAgentStack` (the durable Lambda). Deploy to your default AWS region. Please refer to the [AWS capabilities explorer](https://builder.aws.com/build/capabilities/explore) for feature availability in your desired region.

1. Note the outputs from the CDK deployment process. These contain the resource ARNs used for testing.

## How it works

This pattern creates two stacks:

1. **AgentCoreStrandsStack** — Deploys a containerized Python agent on Amazon Bedrock AgentCore. The agent uses the Strands Agents SDK with Amazon Bedrock foundation models to process prompts. It is built from a local Dockerfile and pushed to ECR automatically by CDK.

2. **DurableAgentStack** — Deploys a durable function (using Node.js 22.x) that orchestrates the agent invocation using `context.map` for parallel execution:
   - The durable function receives a city name and builds two prompts: a weekend trip agenda and a weeklong trip agenda
   - `context.map` fans out both prompts in parallel, each running in its own child context
   - Inside each map iteration, `waitForCallback` pauses the execution while the agent processes the prompt
   - The agent confirms receipt immediately and processes the LLM call in a background thread
   - When each agent finishes, it calls `SendDurableExecutionCallbackSuccess` to resume its respective callback
   - A final `context.step` combines the two trip plans into a single response

The durable execution SDK automatically checkpoints progress, so when the Lambda function is paused and restarted, it resumes from the last completed checkpoint rather than re-executing completed steps. If one trip plan completes before the other, its result is checkpointed and won't be re-fetched on replay.

## Testing

After deployment, invoke the durable function using the AWS CLI or from the AWS Console.

### Invoke the durable function

Use the qualified alias ARN from the CDK output (`DurableFunctionAliasArn`):

```bash
aws lambda invoke \
  --function-name durableAgentCaller:prod \
  --payload '{"city": "Tokyo"}' \
  --cli-binary-format raw-in-base64-out \
  response.json
```

### View the response

```bash
cat response.json
```

### Expected Response

The durable function returns a JSON response after both agent calls complete:

```json
{
  "city": "Tokyo",
  "weekendTrip": "Day 1: Start your morning at Tsukiji Outer Market...",
  "weeklongTrip": "Day 1: Arrive and settle into Shinjuku...",
  "timestamp": "2026-02-26T12:00:00.000Z"
}
```

The initial `invoke` call returns immediately with a durable execution ID. The function fans out both trip-planning prompts in parallel, suspends while waiting for the agent callbacks, then resumes and combines the results.

### View CloudWatch logs

```bash
aws logs filter-log-events \
  --log-group-name /aws/lambda/durableAgentCaller \
  --start-time $(date -v-5M +%s)000
```

## Cleanup

1. Delete the stacks:

    ```bash
    cdk destroy --all
    ```

1. Confirm the stacks have been deleted by checking the AWS CloudFormation console or running:

    ```bash
    aws cloudformation list-stacks --stack-status-filter DELETE_COMPLETE
    ```

----
Copyright 2026 Amazon.com, Inc. or its affiliates. All Rights Reserved.

SPDX-License-Identifier: MIT-0
