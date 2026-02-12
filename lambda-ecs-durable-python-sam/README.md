# AWS Lambda Durable Functions to Amazon ECS with Python

This pattern demonstrates how to invoke an Amazon ECS task from AWS Lambda Durable Functions using Python, showcasing resilient multi-step workflows with automatic checkpointing and state management.

Lambda Durable Functions enable you to build resilient applications that can execute for up to one year while maintaining reliable progress despite interruptions. This pattern shows two integration approaches: **synchronous (polling with durable waits)** and **callback (async with durable steps)**.

Learn more about this pattern at Serverless Land Patterns: https://serverlessland.com/patterns

**Important:** This application uses various AWS services and there are costs associated with these services after the Free Tier usage - please see the [AWS Pricing page](https://aws.amazon.com/pricing/) for details.

## What are Lambda Durable Functions?

Lambda Durable Functions enable you to build resilient multi-step applications that can execute for up to one year while maintaining reliable progress despite interruptions. Key features include:

- **Automatic Checkpointing**: Each step is automatically checkpointed, so your function can resume from the last completed step after interruptions
- **Cost-Effective Waits**: During wait operations, your function suspends without incurring compute charges
- **Built-in Retries**: Steps have automatic retry logic with progress tracking
- **Deterministic Replay**: When resuming, completed steps use stored results instead of re-executing

This pattern uses the [AWS Durable Execution SDK for Python](https://docs.aws.amazon.com/lambda/latest/dg/durable-execution-sdk.html) to implement these capabilities.

## Security Note

This pattern is designed for learning and demonstration purposes. The IAM roles and security group use permissive configurations to simplify deployment and focus on the integration patterns:

- **Security Group**: Allows all outbound traffic (required for pulling Docker images and calling AWS APIs)
- **IAM Roles**: Use wildcard (`*`) resources for ECS task management

**For production use**, you should:
- Restrict security group egress to specific AWS service endpoints using VPC endpoints
- Scope IAM policies to specific resources (task definitions, DynamoDB tables)
- Implement least privilege access based on your security requirements
- Consider using AWS PrivateLink for service-to-service communication
- Enable VPC Flow Logs for network traffic monitoring
- Package the AWS SDK in your Lambda deployment package (13-14MB) instead of relying on the Lambda-provided runtime SDK
- Include the Durable Execution SDK in your deployment package for production (included in requirements.txt)

Deploy this pattern in a non-production AWS account or isolated environment for testing.

## Requirements

* [Create an AWS account](https://portal.aws.amazon.com/gp/aws/developer/registration/index.html) if you do not already have one and log in. The IAM user that you use must have sufficient permissions to make necessary AWS service calls and manage AWS resources.
* [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html) installed and configured
* [Git Installed](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)
* [AWS Serverless Application Model](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-sam-cli-install.html) (AWS SAM) installed

## Architecture

### Pattern 1: Synchronous (Durable Polling) Integration

```
┌─────────────────────┐      ┌──────────────────┐      ┌─────────────┐
│   Lambda Durable    │      │   ECS Task       │      │  CloudWatch │
│   Function (Sync)   │─────▶│   (Python)       │─────▶│    Logs     │
│                     │      │                  │      │             │
└─────────────────────┘      └──────────────────┘      └─────────────┘
      │                               │
      │  Durable Wait (no charges)    │
      └───────────────────────────────┘
         Polls with checkpointing
```

**How it works:**
1. Lambda durable function invokes the ECS task using `ecs:RunTask` (checkpointed step)
2. Function uses `context.wait()` to pause without compute charges
3. After each wait, function checks task status using `ecs:DescribeTasks` (checkpointed step)
4. If interrupted, function automatically resumes from last checkpoint
5. Once complete, Lambda returns the result
6. Can run for up to 1 year (vs 15 minutes for standard Lambda)

**Key Durable Features:**
- `@durable_execution` decorator enables durable execution
- `@durable_step` decorator marks functions as checkpointed steps
- `context.wait()` suspends execution without charges
- Automatic replay and recovery from failures

**Use cases:**
- Long-running tasks (hours to days)
- Tasks requiring reliable progress tracking
- Workflows that need automatic recovery
- Cost-sensitive polling operations

**Advantages over standard Lambda:**
- No 15-minute timeout limitation
- Pay only for active execution time (not wait time)
- Automatic checkpointing and recovery
- Built-in retry logic

### Pattern 2: Callback (Durable Async) Integration

```
┌─────────────────────┐      ┌──────────────────┐      ┌─────────────┐
│   Lambda Durable    │      │   ECS Task       │      │  CloudWatch │
│  Function (Callback)│─────▶│   (Python)       │─────▶│    Logs     │
│                     │      │                  │      │             │
└─────────────────────┘      └──────────────────┘      └─────────────┘
      │                               │                       │
      │  Checkpointed Steps           │                       │
      │                               ▼                       │
      │                      ┌─────────────────┐              │
      └──────────────────────│    DynamoDB     │◄─────────────┘
                             │     Table       │
                             └─────────────────┘
```

**How it works:**
1. Lambda durable function creates DynamoDB record (checkpointed step)
2. Lambda invokes the ECS task using `ecs:RunTask` (checkpointed step)
3. Lambda updates DynamoDB with task ARN (checkpointed step)
4. Lambda **returns immediately** (async pattern)
5. The Python application in ECS processes the work
6. When done, the ECS task updates DynamoDB with the result
7. If any step fails, automatic retry with checkpoint recovery

**Key Durable Features:**
- Each step is automatically checkpointed
- If interrupted, function resumes from last completed step
- No re-execution of completed steps
- Reliable task initiation guaranteed

**Use cases:**
- Fire-and-forget workflows
- Asynchronous processing
- When you don't need immediate results
- Decoupling task execution from API responses
- Workflows requiring guaranteed task initiation

**Advantages:**
- Reliable task initiation with automatic recovery
- Minimal Lambda execution time
- Each step is independently retryable
- No risk of duplicate task creation (idempotent)

## Deployment Instructions

### Prerequisites

* Python 3.13 or 3.14 runtime support for Lambda Durable Functions
* AWS SAM CLI version that supports DurableConfig and container images
* Docker installed (for building Lambda container images)

### Step 1: Clone the Repository

```bash
git clone https://github.com/aws-samples/serverless-patterns
cd serverless-patterns/lambda-ecs-python-sam
```

### Step 2: Build and Deploy

This pattern uses Lambda container images with Python 3.13 to support durable functions. The build process will:
- Build Docker images with the Durable Execution SDK
- Create ECR repositories automatically
- Push images to ECR
- Deploy Lambda functions using the container images

```bash
sam build
sam deploy --guided
```

During the prompts:
- **Stack Name**: `lambda-ecs-durable-demo` (or your preferred name)
- **AWS Region**: Your preferred region (e.g., `us-east-1`)
- **Parameter VpcCIDR**: Press Enter to use default (10.0.0.0/16)
- **Confirm changes before deploy**: Y
- **Allow SAM CLI IAM role creation**: Y
- **Disable rollback**: N
- **SyncLambdaFunction has no authorization defined**: Y
- **CallbackLambdaFunction has no authorization defined**: Y
- **Create managed ECR repositories for all functions**: Y (required for container images)
- **Save arguments to samconfig.toml**: Y

The deployment will take 5-10 minutes as it creates VPC, ECS cluster, Lambda functions, and other resources.

### Step 3: Note the Outputs

After deployment, note the following outputs:
- `SyncLambdaFunctionArn` - ARN for the synchronous pattern Lambda
- `CallbackLambdaFunctionArn` - ARN for the callback pattern Lambda
- `CallbackTableName` - DynamoDB table for callback tracking
- `ECSClusterName` - Name of the ECS cluster
- `LogGroupName` - CloudWatch log group for ECS tasks

**Important**: When invoking durable functions, you must use a qualified ARN (append `:$LATEST` to the function name).

## How to Test

### Testing the Synchronous (Durable) Pattern

1. **Invoke the durable function asynchronously:**

Lambda Durable Functions with execution timeout > 15 minutes must be invoked asynchronously. Use the `--invocation-type Event` flag and a qualified ARN (with `:$LATEST`):

```bash
aws lambda invoke \
    --function-name lambda-ecs-durable-demo-sync-function:\$LATEST \
    --invocation-type Event \
    --cli-binary-format raw-in-base64-out \
    --payload '{"message": "Hello from durable sync pattern", "processingTime": 10}' \
    response.json
```

**Note**: The `\$LATEST` qualifier is required for durable functions. The backslash escapes the dollar sign in bash.

2. **Monitor the Lambda execution logs:**

```bash
aws logs tail /aws/lambda/lambda-ecs-durable-demo-sync-function --follow
```

You'll see:
- Task starting with checkpointed step
- Durable waits (no compute charges during waits)
- Status checks every 5 seconds (PROVISIONING → PENDING → RUNNING → STOPPED)
- Each check is a separate checkpointed operation
- Final result when task completes

3. **View ECS task logs:**

```bash
aws logs tail /ecs/lambda-ecs-durable-demo --follow
```

4. **View execution in Lambda console:**

Navigate to the Lambda console → Your function → "Monitoring" tab → "Logs" to see the execution timeline and checkpoints.

### Testing the Callback (Durable) Pattern

1. **Invoke the durable function asynchronously:**

```bash
aws lambda invoke \
    --function-name lambda-ecs-durable-demo-callback-function:\$LATEST \
    --invocation-type Event \
    --cli-binary-format raw-in-base64-out \
    --payload '{"message": "Hello from durable callback pattern", "processingTime": 30}' \
    response.json
```

2. **Monitor the Lambda execution logs:**

```bash
aws logs tail /aws/lambda/lambda-ecs-durable-demo-callback-function --follow
```

You'll see:
- DynamoDB record creation (checkpointed)
- ECS task initiation (checkpointed)
- Function returns immediately

3. **Check the status in DynamoDB:**

```bash
# Scan the table to see all executions
aws dynamodb scan --table-name lambda-ecs-durable-demo-callbacks

# Or get a specific execution (replace with your execution ID from logs)
aws dynamodb get-item \
    --table-name lambda-ecs-durable-demo-callbacks \
    --key '{"executionId": {"S": "YOUR-EXECUTION-ID"}}'
```

4. **Monitor ECS task logs:**

```bash
aws logs tail /ecs/lambda-ecs-durable-demo --follow
```

The ECS task will update DynamoDB when processing is complete. You'll see the result in the `result` field with status `COMPLETED`.

## Key Differences Between Patterns

| Feature | Synchronous (Durable Polling) | Callback (Durable Async) |
|---------|------------------------------|--------------------------|
| **Execution Duration** | Up to 1 year | Up to 1 year |
| **Checkpointing** | Automatic for each step | Automatic for each step |
| **Wait Charges** | No charges during waits | N/A (returns immediately) |
| **Polling** | Durable waits between checks | No polling needed |
| **Task Awareness** | Task doesn't know about Lambda | Task updates DynamoDB |
| **Complexity** | Moderate (durable steps + waits) | Moderate (durable steps + DynamoDB) |
| **Use Case** | Long-running tasks needing results | Fire-and-forget workflows |
| **Cost** | Pay only for active execution | Minimal (quick execution) |
| **Result Retrieval** | Returned by function | Query DynamoDB |
| **Reliability** | Automatic recovery from failures | Guaranteed task initiation |

## Benefits of Lambda Durable Functions

Compared to standard Lambda functions:

✅ **Extended Duration**: Execute for up to 1 year (vs 15 minutes)
✅ **Cost Optimization**: No charges during wait operations
✅ **Automatic Recovery**: Built-in checkpointing and replay
✅ **Simplified Code**: No manual state management needed
✅ **Reliable Execution**: Guaranteed progress despite interruptions
✅ **Built-in Retries**: Automatic retry logic for steps

## Cleanup

To delete the resources:

```bash
sam delete
```

## Resources

- [AWS Lambda Durable Functions](https://docs.aws.amazon.com/lambda/latest/dg/durable-functions.html)
- [Durable Execution SDK](https://docs.aws.amazon.com/lambda/latest/dg/durable-execution-sdk.html)
- [AWS Lambda](https://aws.amazon.com/lambda/)
- [Amazon ECS](https://aws.amazon.com/ecs/)
- [Amazon DynamoDB](https://aws.amazon.com/dynamodb/)
- [ECS RunTask API](https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_RunTask.html)

---

Copyright 2024 Amazon.com, Inc. or its affiliates. All Rights Reserved.

SPDX-License-Identifier: MIT-0
