# AWS Lambda Durable Function — Image Processing Pipeline (Fan-Out/Fan-In)

This sample demonstrates how to build a resilient, long-running image-processing pipeline using **AWS Lambda Durable Functions** for .NET. It uses the fan-out/fan-in pattern to process an uploaded image in parallel across three branches, then aggregates the results and writes them to DynamoDB.

## Architecture

```
┌──────────────┐       ┌───────────────┐       ┌──────────────────────────────────────────────┐
│  Upload to   │       │  S3 Trigger   │       │       Lambda Durable Function                │
│  S3 Bucket   │──────▶│  Lambda       │──────▶│                                              │
│  uploads/*   │       │               │       │  ┌────────── ParallelAsync ────────────┐     │
└──────────────┘       └───────────────┘       │  │                                     │     │
                                               │  │  ┌───────────┐ ┌───────────┐ ┌────┐│     │
    S3 Event              Invokes durable      │  │  │ Thumbnail │ │ Watermark │ │Meta││     │
    Notification          function async       │  │  │ (200px)   │ │ (logo     │ │data││     │
    (uploads/ prefix)                          │  │  │           │ │  overlay) │ │    ││     │
                                               │  │  └─────┬─────┘ └─────┬─────┘ └──┬─┘│     │
                                               │  └────────┼─────────────┼──────────┼──┘     │
                                               │           └──────┬──────┘──────────┘        │
                                               │                  ▼                          │
                                               │       ┌────────────────────┐                │
                                               │       │  Aggregate Results │                │
                                               │       └─────────┬──────────┘                │
                                               │                 ▼                          │
                                               │       ┌────────────────────┐                │
                                               │       │ Write to DynamoDB  │                │
                                               │       └────────────────────┘                │
                                               └──────────────────────────────────────────────┘
```

## What It Demonstrates

- **Parallel execution** — Three image-processing tasks (thumbnail, watermark, metadata) run concurrently using `ctx.ParallelAsync` with named `DurableBranch<T>` instances.
- **Automatic checkpointing** — Each branch is independently checkpointed. If the Lambda is interrupted, completed branches resume from cache without re-executing.
- **Fan-in aggregation** — Branch results are collected from `IBatchResult<T>` and aggregated into a single `PipelineResult`.
- **Retry resilience** — Each step uses `RetryStrategy.Default` (6 attempts with exponential backoff) to handle transient S3/DynamoDB failures.
- **CDK infrastructure** — Deploys S3 bucket, DynamoDB table, and Lambda functions with least-privilege IAM permissions.

### Processing Operations

| Branch | Operation |
|--------|-----------|
| Thumbnail | Resizes the image to a max of 200×200 px (preserving aspect ratio) and saves as JPEG |
| Watermark | Overlays a logo image (`img/Lambda.png`) in the bottom-right corner at 50% opacity, then applies 5px rounded corners and a dark border |
| Metadata | Extracts width, height, format, and file size from the original image |

## Project Structure

```
├── cdk.json                         # CDK app configuration
├── src/
│   ├── CdkDotnetDurablefunctionImageprocessing.slnx  # Solution file
│   ├── .globalconfig                # Code analysis configuration
│   ├── Infra/                       # CDK infrastructure (C#)
│   │   ├── Program.cs               # CDK app entry point
│   │   ├── InfraStack.cs            # Stack: S3, DynamoDB, Lambda
│   │   └── Infra.csproj
│   └── ImageProcessor/              # Lambda function project
│       ├── Function.cs              # Durable workflow (entry point + handler)
│       ├── S3TriggerHandler.cs      # S3 event trigger (starts durable executions)
│       ├── ImageProcessingService.cs # Image manipulation operations
│       ├── ResultsWriter.cs         # DynamoDB persistence
│       ├── Models.cs                # Input/output record types
│       └── ImageProcessor.csproj
└── README.md
```

---

## Prerequisites

### 1. .NET 10 SDK

Download and install from https://dotnet.microsoft.com/download/dotnet/10.0

Verify installation:

```bash
dotnet --version
# Expected: 10.0.x
```

### 2. Node.js (required for AWS CDK CLI)

Install Node.js 18+ from https://nodejs.org/ or via a version manager:

```bash
# macOS with Homebrew
brew install node

# Verify
node --version
```

### 3. AWS CDK CLI

Install the CDK CLI globally via npm:

```bash
npm install -g aws-cdk

# Verify
cdk --version
```

### 4. AWS CLI & Credentials

Install the AWS CLI v2 from https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html

Configure credentials for your target account:

```bash
aws configure
# Enter: AWS Access Key ID, Secret Access Key, default region (e.g. us-east-1), output format (json)
```

Verify access:

```bash
aws sts get-caller-identity
```

### 5. CDK Bootstrap

CDK requires a one-time bootstrap in each account/region pair you deploy to. This creates the staging resources CDK needs (S3 bucket, IAM roles, ECR repo):

```bash
cdk bootstrap aws://ACCOUNT_ID/REGION
# Example:
cdk bootstrap aws://123456789012/us-east-1
```

Or let it use your default credentials:

```bash
cdk bootstrap
```

---

## Build & Deploy

### Step 1: Build the solution

```bash
dotnet build src/CdkDotnetDurablefunctionImageprocessing.slnx -c Release
```

### Step 2: Preview the CloudFormation changes

```bash
cdk diff
```

### Step 3: Deploy

```bash
cdk deploy
```

When prompted, confirm the IAM changes. The deployment creates:

| Resource | Description |
|----------|-------------|
| S3 Bucket | Stores uploaded images, thumbnails, and watermarked outputs |
| DynamoDB Table | Stores aggregated pipeline results (partition key: `ImageId`) |
| Lambda Function (Durable) | Image processing workflow (1024 MB, durable execution) |
| Lambda Function (Trigger) | S3 event handler that starts durable executions on upload |
| IAM Roles | Least-privilege: S3 read/write, DynamoDB write, Lambda invoke |
| S3 Event Notification | Triggers processing on object creation in `uploads/` prefix |

Stack outputs (printed after deploy):

- `ImagesBucketName` — S3 bucket name
- `ResultsTableName` — DynamoDB table name
- `ImageProcessorFunctionArn` — Lambda function ARN

---

## Testing

### Capture stack outputs

```bash
STACK_NAME="CdkDotnetDurablefunctionImageprocessingStack"

BUCKET_NAME=$(aws cloudformation describe-stacks \
    --stack-name $STACK_NAME \
    --query "Stacks[0].Outputs[?OutputKey=='ImagesBucketName'].OutputValue" \
    --output text)

TABLE_NAME=$(aws cloudformation describe-stacks \
    --stack-name $STACK_NAME \
    --query "Stacks[0].Outputs[?OutputKey=='ResultsTableName'].OutputValue" \
    --output text)

FUNCTION_ARN=$(aws cloudformation describe-stacks \
    --stack-name $STACK_NAME \
    --query "Stacks[0].Outputs[?OutputKey=='ImageProcessorFunctionArn'].OutputValue" \
    --output text)
```

### Upload a test image to S3

Uploading to the `uploads/` prefix automatically triggers the image processing pipeline:

```bash
aws s3 cp my-photo.jpg s3://$BUCKET_NAME/uploads/my-photo.jpg
```

The S3 event notification invokes the trigger Lambda, which starts a durable execution of the image processor. No manual invoke is needed.

### (Optional) Invoke the durable function manually

You can also invoke the durable function directly:

```bash
aws lambda invoke \
    --function-name "$FUNCTION_ARN:\$LATEST" \
    --invocation-type Event \
    --cli-binary-format raw-in-base64-out \
    --payload '{"Bucket":"'$BUCKET_NAME'","Key":"uploads/my-photo.jpg"}' \
    /tmp/invoke-response.json
```

> **Note:** Durable functions require a qualified ARN (append `:\$LATEST`). Functions with `ExecutionTimeout` greater than 15 minutes must be invoked asynchronously (`--invocation-type Event`), which returns immediately with HTTP 202.

### Check execution status

```bash
aws lambda list-durable-executions-by-function \
    --function-name $FUNCTION_ARN
```

To get details on a specific execution:

```bash
aws lambda get-durable-execution \
    --function-name $FUNCTION_ARN \
    --durable-execution-arn <execution-arn>
```

### Verify results in DynamoDB

```bash
aws dynamodb scan --table-name $TABLE_NAME
```

Expected output includes:

```json
{
  "Items": [
    {
      "ImageId": {"S": "my-photo"},
      "SourceBucket": {"S": "<bucket-name>"},
      "SourceKey": {"S": "uploads/my-photo.jpg"},
      "ThumbnailKey": {"S": "thumbnails/my-photo.jpg"},
      "ThumbnailWidth": {"N": "200"},
      "ThumbnailHeight": {"N": "150"},
      "WatermarkKey": {"S": "watermarked/my-photo.jpg"},
      "OriginalWidth": {"N": "1920"},
      "OriginalHeight": {"N": "1080"},
      "Format": {"S": "Jpeg"},
      "FileSizeBytes": {"N": "524288"},
      "CompletedAt": {"S": "2026-07-13T14:30:00.0000000Z"}
    }
  ]
}
```

### Verify processed images in S3

```bash
# List thumbnails
aws s3 ls s3://$BUCKET_NAME/thumbnails/

# List watermarked images
aws s3 ls s3://$BUCKET_NAME/watermarked/

# Download the thumbnail
aws s3 cp s3://$BUCKET_NAME/thumbnails/my-photo.jpg ./my-photo-thumb.jpg
```

---

## Monitoring

### CloudWatch Logs

Lambda logs are automatically sent to CloudWatch Logs. View them in the console or via CLI:

```bash
# Get the log group name
LOG_GROUP="/aws/lambda/$(aws lambda get-function \
    --function-name $FUNCTION_ARN \
    --query 'Configuration.FunctionName' --output text)"

# Tail recent logs
aws logs tail $LOG_GROUP --follow

# Search for errors in the last hour
aws logs filter-log-events \
    --log-group-name $LOG_GROUP \
    --start-time $(date -v-1H +%s000) \
    --filter-pattern "ERROR"
```

### CloudWatch Metrics

Key metrics to monitor for the Lambda function:

| Metric | What it tells you |
|--------|-------------------|
| `Invocations` | How many times the function was invoked |
| `Duration` | Execution time per invocation |
| `Errors` | Unhandled exceptions |
| `Throttles` | Invocations rejected due to concurrency limits |
| `ConcurrentExecutions` | Number of in-flight executions |

View in the AWS Console: **CloudWatch → Metrics → Lambda → By Function Name**

### DynamoDB Metrics

| Metric | What it tells you |
|--------|-------------------|
| `ConsumedWriteCapacityUnits` | Write throughput consumed |
| `SystemErrors` | Internal DynamoDB errors |
| `UserErrors` | Client-side errors (validation, conditions) |

### Setting up a CloudWatch Alarm (example)

```bash
aws cloudwatch put-metric-alarm \
    --alarm-name "ImageProcessor-Errors" \
    --namespace "AWS/Lambda" \
    --metric-name "Errors" \
    --dimensions Name=FunctionName,Value=$(aws lambda get-function \
        --function-name $FUNCTION_ARN \
        --query 'Configuration.FunctionName' --output text) \
    --statistic Sum \
    --period 300 \
    --threshold 1 \
    --comparison-operator GreaterThanOrEqualToThreshold \
    --evaluation-periods 1 \
    --treat-missing-data notBreaching
```

### Durable Execution Monitoring

List active durable executions:

```bash
aws lambda list-durable-executions --function-name $FUNCTION_ARN
```

Get details on a specific execution:

```bash
aws lambda get-durable-execution \
    --function-name $FUNCTION_ARN \
    --execution-id <execution-id>
```

---

## Cleanup

### Delete the stack and all resources

```bash
cdk destroy
```

This removes:
- The S3 bucket and all objects (configured with `RemovalPolicy.DESTROY` and `AutoDeleteObjects`)
- The DynamoDB table and all items
- The Lambda function, IAM role, and CloudWatch log group

### Verify deletion

```bash
aws cloudformation describe-stacks \
    --stack-name CdkDotnetDurablefunctionImageprocessingStack 2>&1 \
    | grep -q "does not exist" && echo "Stack deleted successfully"
```

---

## Useful Commands

| Command | Description |
|---------|-------------|
| `dotnet build src/CdkDotnetDurablefunctionImageprocessing.slnx` | Build the entire solution |
| `cdk synth` | Emit the synthesized CloudFormation template (publishes Lambda automatically) |
| `cdk diff` | Compare deployed stack with current state |
| `cdk deploy` | Deploy this stack to your default AWS account/region |
| `cdk destroy` | Tear down the stack and all resources |
| `dotnet format src/CdkDotnetDurablefunctionImageprocessing.slnx` | Auto-format code |

---

## Troubleshooting

### "CDK bootstrap is required"

If you see `This stack uses assets, so the toolkit stack must be deployed`, run:

```bash
cdk bootstrap
```

### Lambda timeout

The function has a 15-minute timeout. If processing large images causes timeouts, increase `MemorySize` in `InfraStack.cs` — Lambda allocates CPU proportional to memory.

### S3 access denied

Verify the Lambda role has the correct permissions by checking the IAM policy in the CloudFormation template:

```bash
cdk synth | grep -A 20 "PolicyDocument"
```

### DynamoDB throttling

The table uses on-demand billing (`PAY_PER_REQUEST`) so throttling is unlikely. If it occurs, check the `ThrottledRequests` CloudWatch metric.

---

## References

- [Amazon.Lambda.DurableExecution SDK](https://github.com/aws/aws-lambda-dotnet/tree/master/Libraries/src/Amazon.Lambda.DurableExecution)
- [Parallel documentation](https://github.com/aws/aws-lambda-dotnet/blob/master/Libraries/src/Amazon.Lambda.DurableExecution/docs/core/parallel.md)
- [Steps documentation](https://github.com/aws/aws-lambda-dotnet/blob/master/Libraries/src/Amazon.Lambda.DurableExecution/docs/core/steps.md)
- [AWS CDK .NET Reference](https://docs.aws.amazon.com/cdk/api/v2/dotnet/)
- [AWS CDK Getting Started](https://docs.aws.amazon.com/cdk/v2/guide/getting-started.html)
