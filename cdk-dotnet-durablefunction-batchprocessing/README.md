# AWS Lambda Durable Function — Batch File Processing (Dynamic Fan-Out/Fan-In)

This sample demonstrates how to build a dynamic batch processing pipeline using **AWS Lambda Durable Functions** for .NET. Unlike the image processing sample where parallel branches are hardcoded, this workflow discovers files at runtime and dynamically creates a parallel task for each one — the number of branches is unknown at design time.

## Architecture

```
┌──────────────┐       ┌──────────────────────────────────────────────────────────────┐
│  Invoke with │       │            Lambda Durable Function                           │
│  S3 prefix   │──────▶│                                                              │
└──────────────┘       │  ┌───────────────────────────────────────────────────┐       │
                       │  │  Step: List files under prefix                    │       │
                       │  │  (discovers N files at runtime)                   │       │
                       │  └────────────────────┬──────────────────────────────┘       │
                       │                       ▼                                      │
                       │  ┌────────── ParallelAsync (N branches) ─────────┐           │
                       │  │                                               │           │
                       │  │  ┌─────────┐ ┌─────────┐       ┌─────────┐    │           │
                       │  │  │ File 1  │ │ File 2  │  ...  │ File N  │    │           │
                       │  │  │ process │ │ process │       │ process │    │           │
                       │  │  │ + write │ │ + write │       │ + write │    │           │
                       │  │  └────┬────┘ └────┬────┘       └────┬────┘    │           │
                       │  │       │           │                  │        │           │
                       │  └───────┼───────────┼──────────────────┼────────┘           │
                       │          └───────────┼──────────────────┘                    │
                       │                      ▼                                       │
                       │  ┌───────────────────────────────────────────────────┐       │
                       │  │  Step: Aggregate results + write summary to S3    │       │
                       │  └───────────────────────────────────────────────────┘       │
                       └──────────────────────────────────────────────────────────────┘
```

## What It Demonstrates

- **Dynamic fan-out** — The number of parallel branches is determined at runtime by listing S3 objects. The workflow handles 1 file or 1,000 files with the same code.
- **Automatic checkpointing** — Each file's processing is independently checkpointed. If the Lambda is interrupted, completed files resume from cache.
- **Partial failure tolerance** — Uses `CompletionConfig.AllCompleted()` so all files are processed even if some fail. The summary report captures both successes and failures.
- **Per-file processing** — Each branch downloads the file, computes line count, word count, byte size, and SHA-256 hash.
- **Summary report** — After all files complete, a JSON report is written to S3 with aggregated statistics.
- **CDK infrastructure** — Deploys S3 bucket, DynamoDB table, and Lambda function with least-privilege IAM permissions.

## Project Structure

```
├── cdk.json
├── src/
│   ├── CdkDotnetDurablefunctionBatchprocessing.slnx
│   ├── .globalconfig
│   ├── Infra/
│   │   ├── Program.cs
│   │   ├── InfraStack.cs
│   │   ├── GlobalSuppressions.cs
│   │   └── Infra.csproj
│   └── BatchProcessor/
│       ├── Function.cs              # Durable workflow with dynamic ParallelAsync
│       ├── FileProcessingService.cs # S3 listing + per-file processing
│       ├── ReportWriter.cs          # DynamoDB + S3 report persistence
│       ├── Models.cs                # Input/output record types
│       └── BatchProcessor.csproj
└── README.md
```

---

## Prerequisites

- [.NET 10 SDK](https://dotnet.microsoft.com/download/dotnet/10.0)
- [AWS CDK CLI](https://docs.aws.amazon.com/cdk/v2/guide/getting-started.html) (`npm install -g aws-cdk`)
- AWS account with credentials configured (`aws configure`)
- CDK bootstrapped in your target account/region (`cdk bootstrap`)

---

## Build & Deploy

### Step 1: Build the solution

```bash
dotnet build src/CdkDotnetDurablefunctionBatchprocessing.slnx -c Release
```

### Step 2: Deploy

```bash
cdk deploy
```

The CDK automatically publishes the Lambda function during synthesis. This creates:

| Resource | Description |
|----------|-------------|
| S3 Bucket | Stores input files and JSON summary reports |
| DynamoDB Table | Stores per-file processing results (`BatchId` + `FileName`) |
| Lambda Function | Durable workflow (512 MB, 60 min execution timeout) |
| IAM Role | Least-privilege: S3 read/write + DynamoDB write |

---

## Testing

### Capture stack outputs

```bash
STACK_NAME="CdkDotnetDurablefunctionBatchprocessingStack"

BUCKET_NAME=$(aws cloudformation describe-stacks \
    --stack-name $STACK_NAME \
    --query "Stacks[0].Outputs[?OutputKey=='FilesBucketName'].OutputValue" \
    --output text)

FUNCTION_ARN=$(aws cloudformation describe-stacks \
    --stack-name $STACK_NAME \
    --query "Stacks[0].Outputs[?OutputKey=='BatchProcessorFunctionArn'].OutputValue" \
    --output text)
```

### Upload test files to S3

The project includes scripts to download real-world data from [NOAA's Global Historical Climatology Network (GHCN)](https://registry.opendata.aws/noaa-ghcn/) on Amazon S3 Open Data and upload it for processing.

```bash
# Download ~75 small CSV weather station files to ./testdata/ (excluded from git)
./download-testdata.sh

# Upload them to the deployed S3 bucket
./upload-testdata.sh
```

You can adjust the file count: `./download-testdata.sh 100` downloads 100 files.

Alternatively, create your own test files manually:

```bash
# Create some sample text files
for i in $(seq 1 5); do
    echo "This is test file number $i with some sample content." > /tmp/file-$i.txt
    echo "Line 2 of file $i." >> /tmp/file-$i.txt
    echo "Line 3 with extra words to count." >> /tmp/file-$i.txt
done

# Upload them under a common prefix
for i in $(seq 1 5); do
    aws s3 cp /tmp/file-$i.txt s3://$BUCKET_NAME/input/batch-test/file-$i.txt
done
```

### Invoke the durable function

```bash
aws lambda invoke \
    --function-name "$FUNCTION_ARN:\$LATEST" \
    --invocation-type Event \
    --cli-binary-format raw-in-base64-out \
    --payload '{"Bucket":"'$BUCKET_NAME'","Prefix":"input/batch-test/"}' \
    /tmp/invoke-response.json
```

> **Note:** Durable functions require a qualified ARN (append `:\$LATEST`). Functions with `ExecutionTimeout` greater than 15 minutes must be invoked asynchronously (`--invocation-type Event`).

### Check execution status

```bash
aws lambda list-durable-executions-by-function \
    --function-name $FUNCTION_ARN
```

### Verify the summary report

```bash
# List reports
aws s3 ls s3://$BUCKET_NAME/reports/

# Download and view the latest report
REPORT_KEY=$(aws s3 ls s3://$BUCKET_NAME/reports/ --recursive | sort | tail -1 | awk '{print $4}')
aws s3 cp s3://$BUCKET_NAME/$REPORT_KEY - | jq .
```

Expected report structure:

```json
{
  "BatchId": "batch-20260713-143000",
  "SourceBucket": "<bucket-name>",
  "SourcePrefix": "input/batch-test/",
  "TotalFiles": 5,
  "TotalBytes": 475,
  "SuccessCount": 5,
  "FailureCount": 0,
  "CompletedAt": "2026-07-13T14:30:05.0000000Z",
  "Files": [
    {
      "FileName": "file-1.txt",
      "SizeBytes": 95,
      "LineCount": 3,
      "WordCount": 17,
      "ContentHash": "a1b2c3..."
    }
  ]
}
```

### Verify per-file results in DynamoDB

```bash
TABLE_NAME=$(aws cloudformation describe-stacks \
    --stack-name $STACK_NAME \
    --query "Stacks[0].Outputs[?OutputKey=='ResultsTableName'].OutputValue" \
    --output text)

aws dynamodb scan --table-name $TABLE_NAME
```

---

## How the Dynamic Fan-Out Works

The key difference from static parallelism is that branches are built from runtime data:

```csharp
// Step 1: Discover files (count unknown at design time)
var fileKeys = await ctx.StepAsync(
    async (_, ct) => await _fileService.ListFilesAsync(bucket, prefix, ct),
    name: "list-files");

// Step 2: Dynamically create one branch per file
var branches = fileKeys.Select(key =>
    new DurableBranch<FileProcessingResult>(
        Path.GetFileName(key),
        async (branchCtx, ct) =>
        {
            var result = await branchCtx.StepAsync(
                async (_, t) => await _fileService.ProcessFileAsync(bucket, key, t),
                name: "process-file",
                cancellationToken: ct);
            return result;
        }))
    .ToList();

// Step 3: Execute all branches (max 10 concurrent)
var batch = await ctx.ParallelAsync(branches, name: "process-all-files",
    config: new ParallelConfig
    {
        MaxConcurrency = 10,
        CompletionConfig = CompletionConfig.AllCompleted()
    });
```

`MaxConcurrency = 10` bounds how many branches run at once, preventing downstream service overload while still processing files in parallel.

---

## Cleanup

```bash
cdk destroy
```

---

## Useful Commands

| Command | Description |
|---------|-------------|
| `dotnet build src/CdkDotnetDurablefunctionBatchprocessing.slnx` | Build the entire solution |
| `cdk synth` | Emit the synthesized CloudFormation template (publishes Lambda automatically) |
| `cdk diff` | Compare deployed stack with current state |
| `cdk deploy` | Deploy this stack to your default AWS account/region |
| `cdk destroy` | Tear down the stack and all resources |

---

## References

- [Amazon.Lambda.DurableExecution SDK](https://github.com/aws/aws-lambda-dotnet/tree/master/Libraries/src/Amazon.Lambda.DurableExecution)
- [Parallel documentation](https://github.com/aws/aws-lambda-dotnet/blob/master/Libraries/src/Amazon.Lambda.DurableExecution/docs/core/parallel.md)
- [Steps documentation](https://github.com/aws/aws-lambda-dotnet/blob/master/Libraries/src/Amazon.Lambda.DurableExecution/docs/core/steps.md)
- [AWS CDK .NET Reference](https://docs.aws.amazon.com/cdk/api/v2/dotnet/)
