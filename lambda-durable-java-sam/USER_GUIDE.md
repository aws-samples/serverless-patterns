# Lambda Durable Functions in Java - Workshop User Guide

## Introduction

Welcome to the **AWS Lambda Durable Functions in Java** workshop! In this workshop, you will learn how to build resilient, long-running workflows using Lambda Durable Functions. You'll deploy and run eight different patterns that demonstrate the full capability of durable execution in Java.

### Visual Step Diagrams

To see the visual flow of each pattern, refer to [DIAGRAMS.md](DIAGRAMS.md).

### What are Lambda Durable Functions?

Lambda Durable Functions enable you to build multi-step applications that can execute for up to **one year** while maintaining reliable progress despite interruptions. Key capabilities:

- **Automatic checkpointing**: Each step's result is saved. If the function is interrupted, it resumes from the last checkpoint without re-executing completed work.
- **Suspend without cost**: The `wait()` operation suspends your function without incurring compute charges. You pay only for actual processing time.
- **Replay mechanism**: After resuming, your code runs from the beginning but skips completed checkpoints, using stored results instead.

### How is this different from Step Functions?

| Feature | Durable Functions | Step Functions |
|---------|-------------------|----------------|
| Definition | Code (Java/Python/TypeScript) | JSON/YAML DSL or visual designer |
| Runs in | Lambda | Standalone service |
| Best for | Tightly-coupled business logic | Service orchestration across AWS |
| State management | SDK handles automatically | Managed by service |

---

## Prerequisites

Before starting this workshop, ensure you have:

- An AWS account with admin permissions
- Basic familiarity with Java and AWS Lambda
- One of:
  - **Option A**: Deploy the EC2 instance (everything pre-installed)
  - **Option B**: Local machine with Java 21, Maven 3.8+, Docker, AWS CLI v2, and SAM CLI

---

## Module 1: Environment Setup

### Option A: Deploy EC2 Development Environment

This creates a VPC with a public subnet and an EC2 instance pre-configured with all tools.

```bash
aws cloudformation create-stack \
  --stack-name durable-functions-infra \
  --template-body file://infrastructure/ec2-client-instance.yaml \
  --capabilities CAPABILITY_NAMED_IAM \
  --parameters \
    ParameterKey=JavaVersion,ParameterValue=java21
```

Wait for the stack to complete (~5 minutes):
```bash
aws cloudformation wait stack-create-complete --stack-name durable-functions-infra
```

Connect to the instance via EC2 Instance Connect:
```bash
INSTANCE_ID=$(aws cloudformation describe-stacks --stack-name durable-functions-infra \
  --query 'Stacks[0].Outputs[?OutputKey==`EC2InstanceId`].OutputValue' --output text)
aws ec2-instance-connect ssh --instance-id $INSTANCE_ID
```

### Option B: Local Development

Ensure you have:
```bash
java -version    # Should be 21+
mvn -version     # Should be 3.8+
docker --version
aws --version    # Should be v2
sam --version
```

Clone the project:
```bash
git clone https://github.com/aws-samples/serverless-patterns.git
cd serverless-patterns/lambda-durable-java-sam
```

---

## Module 2: Build and Deploy

### Step 1: Build the Lambda functions

```bash
cd durable-functions-sam/durable-functions
mvn clean package
```

You should see `BUILD SUCCESS`.

### Step 2: Build the Docker container image

```bash
docker build --platform linux/amd64 --provenance=false -t durable-functions-java-examples .
```

> **Note:** The `--platform linux/amd64` flag is required when building on Apple Silicon (M1/M2/M3) Macs. The `--provenance=false` flag ensures the image is pushed in Docker V2 manifest format rather than OCI format, which Lambda requires.

### Step 3: Create ECR repository and push

```bash
AWS_ACCOUNT_ID=$(aws sts get-caller-identity --query Account --output text)
AWS_REGION=${AWS_REGION:-$(aws configure get region)}

# Login to ECR
aws ecr get-login-password --region $AWS_REGION \
  | docker login --username AWS --password-stdin \
    $AWS_ACCOUNT_ID.dkr.ecr.$AWS_REGION.amazonaws.com

# Delete the repository if it already exists, then recreate it
aws ecr delete-repository --repository-name durable-functions-java-examples --force 2>/dev/null
aws ecr create-repository --repository-name durable-functions-java-examples

# Tag and push
docker tag durable-functions-java-examples:latest \
  $AWS_ACCOUNT_ID.dkr.ecr.$AWS_REGION.amazonaws.com/durable-functions-java-examples:latest

docker push \
  $AWS_ACCOUNT_ID.dkr.ecr.$AWS_REGION.amazonaws.com/durable-functions-java-examples:latest
```

### Step 4: Deploy with SAM

```bash
cd ..
sam deploy --guided --capabilities CAPABILITY_NAMED_IAM
```

Accept the defaults or customize:
- Stack name: `durable-functions-java-examples`
- Region: your preferred region
- Confirm changeset: Yes
- Allow SAM CLI to create IAM roles: Yes

> **Note:** If redeploying, delete the existing stack first since durable execution config cannot be added to existing functions:
> ```bash
> aws cloudformation delete-stack --stack-name durable-functions-java-examples
> aws cloudformation wait stack-delete-complete --stack-name durable-functions-java-examples
> ```

### Step 5: Build the SNS message sender

```bash
cd ../sns-message-sender
mvn clean package
```

---

## Module 3: Function Chaining

**Pattern**: Execute steps sequentially where each step's output feeds the next.

**Why durable**: If the function is interrupted after step 3 of 5, it resumes from step 4 on replay without re-executing steps 1-3.

### Run it

```bash
java -cp target/sns-message-sender-1.0-SNAPSHOT.jar \
  sns.producer.DurableFunctionsTrigger DurableFunctionsSNSTopic chaining
```

### What happens

1. **validate-order** - Validates order ID and amount
2. **reserve-inventory** - Reserves items in warehouse
3. **process-payment** - Charges the customer
4. **ship-order** - Creates shipping label and tracking number
5. **notify-customer** - Sends shipment notification

### Observe

Check CloudWatch Logs:
```bash
aws logs tail /aws/lambda/durable-chaining-example --follow
```

Check execution status:
```bash
aws lambda list-durable-executions --function-name durable-chaining-example:1
```

### Key takeaway

Each `context.step()` checkpoints its result. The variable returned from step N is safely used in step N+1 even after a replay because the SDK restores it from the checkpoint.

---

## Module 4: Fan-Out / Fan-In

**Pattern**: Execute multiple independent operations in parallel, then aggregate results.

**Why durable**: Each parallel branch checkpoints independently. If one branch fails after others complete, only the failed branch re-executes.

### Run it

```bash
java -cp target/sns-message-sender-1.0-SNAPSHOT.jar \
  sns.producer.DurableFunctionsTrigger DurableFunctionsSNSTopic fanout
```

### What happens

1. Three analyses run **concurrently** via `parallel()`:
   - Sentiment analysis
   - Entity extraction
   - Summarization
2. Five documents are processed via `map()` with the same logic per item
3. All results are aggregated in a final step

### Key takeaway

- `parallel()` is for **different** operations running concurrently
- `map()` is for the **same** operation applied to each item in a collection
- Both support concurrency limits and failure tolerance

---

## Module 5: Human Interaction (Callbacks)

**Pattern**: Suspend execution while waiting for external human input.

**Why durable**: The function suspends (no compute charges) for hours or days while waiting for a human to respond.

### Run it

```bash
java -cp target/sns-message-sender-1.0-SNAPSHOT.jar \
  sns.producer.DurableFunctionsTrigger DurableFunctionsSNSTopic approval
```

### Complete the callback

Check the logs for the callback ID:
```bash
aws logs tail /aws/lambda/durable-human-interaction-example --follow
```

Look for: `Approval callback created. Callback ID: <ID>`

Then approve:
```bash
aws lambda send-durable-execution-callback-success \
  --callback-id <CALLBACK_ID> \
  --cli-binary-format raw-in-base64-out \
  --result '{"decision":"APPROVED","approver":"manager@example.com"}'
```

Or reject:
```bash
aws lambda send-durable-execution-callback-failure \
  --callback-id <CALLBACK_ID> \
  --error ErrorType=Rejected,ErrorMessage="Budget exceeded"
```

### Key takeaway

- `createCallback()` returns a callback ID that you send to the external system
- The function **suspends** (exits) - no compute charges while waiting
- When the external system calls `send-durable-execution-callback-success`, the function resumes
- Timeout and heartbeat can detect stalled approvers

---

## Module 6: Monitoring / Polling

**Pattern**: Poll an external system on a schedule until a condition is met.

**Why durable**: The function suspends between polling attempts. You don't consume compute while waiting for the external system.

### Run it

```bash
java -cp target/sns-message-sender-1.0-SNAPSHOT.jar \
  sns.producer.DurableFunctionsTrigger DurableFunctionsSNSTopic monitoring
```

### What happens

1. Acknowledges the job
2. Polls every few seconds with exponential backoff (5s, 10s, 20s...)
3. Between polls, the function **suspends** (no compute)
4. When the job reports COMPLETED, polling stops
5. Processes the final result

### Key takeaway

- `waitForCondition()` handles the entire poll-wait-check cycle
- Return `WaitForConditionResult.stopPolling(state)` to end
- Return `WaitForConditionResult.continuePolling(state)` to keep going
- The wait strategy controls backoff between attempts

---

## Module 7: Timers / Scheduled Delays

**Pattern**: Insert delays between steps without consuming compute.

**Why durable**: `context.wait()` suspends the function. You pay nothing during the wait, whether it's 5 seconds or 5 days.

### Run it

```bash
java -cp target/sns-message-sender-1.0-SNAPSHOT.jar \
  sns.producer.DurableFunctionsTrigger DurableFunctionsSNSTopic timer
```

### What happens

1. Creates a task assignment
2. Sends initial notification
3. **Waits 30 seconds** (function suspends, no compute)
4. Sends first reminder
5. **Waits 60 seconds** (function suspends again)
6. Escalates to manager
7. Demonstrates async wait pattern (minimum duration guarantee)

### Key takeaway

- `context.wait("name", Duration.ofSeconds(30))` suspends for 30s at zero cost
- `context.waitAsync()` combined with `stepAsync()` ensures minimum elapsed time
- Maximum wait is 1 year
- Minimum wait is 1 second

---

## Module 8: Error Handling and Compensation

**Pattern**: Automatic retries with saga compensation when later steps fail.

**Why durable**: Retry delays don't consume compute. Failed steps checkpoint the error so compensation logic runs only once.

### Run it (success path)

```bash
java -cp target/sns-message-sender-1.0-SNAPSHOT.jar \
  sns.producer.DurableFunctionsTrigger DurableFunctionsSNSTopic errorhandling
```

### Run it (compensation path)

Trigger with `simulateInventoryFailure=true` by modifying the event or using the AWS CLI directly:
```bash
aws lambda invoke \
  --function-name durable-error-handling-example:1 \
  --cli-binary-format raw-in-base64-out \
  --payload '{"orderId":"ORD-FAIL","amount":99.99,"simulateInventoryFailure":true}' \
  response.json && cat response.json
```

### What happens

1. **Validate** - Standard retry (3 attempts, exponential backoff)
2. **Charge payment** - Custom retry strategy + at-most-once semantics
3. **Reserve inventory** - If this fails, triggers compensation
4. **Compensation** - Refunds the payment (saga pattern)

### Key takeaway

- `RetryStrategies.exponentialBackoff()` for standard retries
- Custom `RetryStrategy` lambda for error-type filtering
- `StepSemantics.AT_MOST_ONCE_PER_RETRY` prevents double-charging
- Catch `StepFailedException` to implement compensation logic
- Between retry attempts, the function suspends (no compute)

---

## Module 9: Map Processing

**Pattern**: Process a collection of items concurrently with rate limiting and failure tolerance.

**Why durable**: Each item checkpoints independently. Partial failures don't prevent successful items from being recorded.

### Run it

```bash
java -cp target/sns-message-sender-1.0-SNAPSHOT.jar \
  sns.producer.DurableFunctionsTrigger DurableFunctionsSNSTopic mapprocessing
```

### What happens

1. Generates a batch of 10 items
2. Processes them with `maxConcurrency=3` (only 3 run at once)
3. Each item goes through: validate → transform → store
4. Every 5th item fails validation (to demonstrate failure tolerance)
5. With `toleratedFailures=2`, the overall operation succeeds
6. Produces a summary with success/failure counts

### Key takeaway

- `MapConfig.builder().maxConcurrency(N)` limits parallel execution
- `CompletionConfig.toleratedFailureCount(N)` allows N failures
- Each item runs in its own child context (isolated checkpoints)
- `mapResult.succeeded()` and `mapResult.failed()` access results

---

## Module 10: Sub-Orchestration

**Pattern**: Compose complex workflows from isolated, reusable sub-workflows.

**Why durable**: Each child context checkpoints as a unit. On replay, entire sub-workflows are skipped if already complete.

### Run it

```bash
java -cp target/sns-message-sender-1.0-SNAPSHOT.jar \
  sns.producer.DurableFunctionsTrigger DurableFunctionsSNSTopic suborchestration
```

### What happens

1. Validates the order (main context)
2. Runs **Payment** and **Inventory** sub-workflows **concurrently** via `runInChildContextAsync()`
3. Runs **Shipping** sub-workflow (sequential, depends on inventory)
4. Runs **Notification** sub-workflow

Each sub-workflow contains multiple steps internally (e.g., Payment: authorize → fraud check → capture).

### Key takeaway

- `runInChildContext()` creates an isolated scope with its own checkpoints
- `runInChildContextAsync()` + `DurableFuture.allOf()` runs sub-workflows concurrently
- Child contexts provide namespace isolation (operation IDs don't conflict)
- On replay, a completed child context returns its checkpointed result instantly

---

## Module 11: Cleanup

Delete all deployed resources:

```bash
# Delete the SAM stack
aws cloudformation delete-stack --stack-name durable-functions-java-examples
aws cloudformation wait stack-delete-complete --stack-name durable-functions-java-examples

# Delete the ECR repository
aws ecr delete-repository --repository-name durable-functions-java-examples --force

# Delete the infrastructure stack (if deployed)
aws cloudformation delete-stack --stack-name durable-functions-infra
aws cloudformation wait stack-delete-complete --stack-name durable-functions-infra
```

---

## Troubleshooting

### Build fails with "package software.amazon.lambda.durable does not exist"

The Durable Execution SDK may not yet be in Maven Central. Check the [SDK repository](https://github.com/aws/aws-durable-execution-sdk-java) for the latest installation instructions. You may need to build from source or use a pre-release repository.

### "Function not found" when invoking

Ensure you published a version and are using the qualified ARN:
```bash
aws lambda publish-version --function-name durable-chaining-example
# Then invoke with :1 qualifier
```

### Callback not resuming

- Verify the callback ID is correct (check CloudWatch Logs)
- Ensure you're using `--cli-binary-format raw-in-base64-out`
- Check that the function's IAM role has `lambda:SendDurableExecutionCallbackSuccess` permission

### Durable execution stuck

List and inspect executions:
```bash
aws lambda list-durable-executions --function-name <function-name>:1
aws lambda get-durable-execution --function-name <function-name>:1 --execution-id <id>
```

Stop a stuck execution:
```bash
aws lambda stop-durable-execution --function-name <function-name>:1 --execution-id <id>
```

---

## Next Steps

- Read the [AWS Durable Execution SDK Developer Guide](https://docs.aws.amazon.com/durable-execution/)
- Explore the [Lambda Durable Functions documentation](https://docs.aws.amazon.com/lambda/latest/dg/durable-functions.html)
- Try combining patterns (e.g., chaining + callbacks + map processing in one workflow)
- Add DynamoDB persistence to store execution results
- Implement idempotency keys for production payment flows
