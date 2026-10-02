# Java Lambda Durable Functions Examples

This project demonstrates **AWS Lambda Durable Functions** patterns in Java. It provides working examples of all major durable execution patterns including chaining, fan-out/fan-in, human interaction, monitoring/polling, timers, error handling with saga compensation, map processing, and sub-orchestration.

## Architecture

```
SNS Topic (Producer) --> Lambda Durable Functions (Consumers) --> DynamoDB (Results)
```

- **SNS Message Sender**: A Java CLI application that sends messages to SNS to trigger the durable functions
- **Durable Functions**: Eight Lambda functions, each demonstrating a different durable execution pattern
- **Infrastructure**: CloudFormation template for a VPC + EC2 instance with all tools pre-installed

## Patterns Demonstrated

| # | Pattern | Handler | Description |
|---|---------|---------|-------------|
| 1 | **Chaining** | `OrderProcessingHandler` | Sequential steps where each output feeds the next |
| 2 | **Fan-Out/Fan-In** | `ParallelProcessingHandler` | Parallel execution with result aggregation |
| 3 | **Human Interaction** | `ApprovalWorkflowHandler` | Callbacks for external human approval |
| 4 | **Monitoring/Polling** | `JobMonitorHandler` | waitForCondition with exponential backoff |
| 5 | **Timer/Delays** | `ScheduledReminderHandler` | Suspending execution without compute charges |
| 6 | **Error Handling** | `ResilientPaymentHandler` | Retries, at-most-once, and saga compensation |
| 7 | **Map Processing** | `BatchDataProcessorHandler` | Concurrent collection processing with tolerance |
| 8 | **Sub-Orchestration** | `OrderFulfillmentHandler` | Child contexts for workflow composition |

## Prerequisites

- AWS Account with permissions for Lambda, SNS, DynamoDB, ECR, IAM, CloudFormation
- Java 21 (Amazon Corretto recommended)
- Maven 3.8+
- Docker
- AWS CLI v2
- AWS SAM CLI

## Quick Start

You can run this project either from an EC2 instance (Option A) or from your local machine (Option B).

### Option A: Using the EC2 Dev Environment

The CloudFormation template deploys a VPC with a public subnet and an EC2 instance pre-configured with Java 21, Maven, Docker, AWS CLI v2, and SAM CLI. The project code is automatically cloned onto the instance.

**1. Deploy the infrastructure stack:**

1. Open the [AWS CloudFormation console](https://console.aws.amazon.com/cloudformation/)
2. Click **Create stack** > **With new resources (standard)**
3. Select **Upload a template file**, then upload `infrastructure/ec2-client-instance.yaml`
4. Enter stack name: `durable-functions-infra`
5. Click **Next** through the options, check **I acknowledge that AWS CloudFormation might create IAM resources with custom names**, then click **Submit**
6. Wait for the stack status to reach **CREATE_COMPLETE** (~5 minutes)

**2. Connect to the instance via EC2 Instance Connect:**

1. Open the [AWS EC2 console](https://console.aws.amazon.com/ec2/)
2. Click **Instances** in the left navigation
3. Select the instance named `DurableFunctionsDevInstance` (created by the stack)
4. Click **Connect** at the top
5. On the **EC2 Instance Connect** tab, click **Connect**

**3. Navigate to the project directory:**

```bash
cd /home/ec2-user/serverless-patterns/lambda-durable-java-sam
```

Then continue from [Build and Deploy](#build-and-deploy) below.

### Option B: Local Development

Ensure you have Java 21+, Maven 3.8+, Docker, AWS CLI v2, and SAM CLI installed.

**1. Set JAVA_HOME:**

Ensure `JAVA_HOME` points to your Java 21 installation directory (not the `bin` subdirectory):

**macOS (zsh/bash):**
```bash
export JAVA_HOME=/Library/Java/JavaVirtualMachines/amazon-corretto-21.jdk/Contents/Home
```

**Linux (bash):**
```bash
export JAVA_HOME=/usr/lib/jvm/java-21-amazon-corretto
```

**Windows (PowerShell):**
```powershell
$env:JAVA_HOME = "C:\Program Files\Amazon Corretto\jdk21.0.x_x"
```

**Windows (Command Prompt):**
```cmd
set JAVA_HOME=C:\Program Files\Amazon Corretto\jdk21.0.x_x
```

Verify it's correct:
```bash
echo $JAVA_HOME              # Should NOT end with /bin
$JAVA_HOME/bin/java -version # Should print Java 21
```

Add the export to your shell profile (`~/.zshrc`, `~/.bashrc`, or Windows System Environment Variables) to persist across sessions.

**2. Configure your AWS credentials and region:**

If you don't have an AWS CLI profile configured, create one pointing to the account where you want to deploy:

```bash
aws configure
```

If you have multiple profiles, set your desired profile as the default for this shell session:

**macOS/Linux:**
```bash
export AWS_PROFILE=your-profile-name
export AWS_REGION=us-east-1  # Change to your preferred region
```

**Windows (PowerShell):**
```powershell
$env:AWS_PROFILE = "your-profile-name"
$env:AWS_REGION = "us-east-1"  # Change to your preferred region
```

**Windows (Command Prompt):**
```cmd
set AWS_PROFILE=your-profile-name
set AWS_REGION=us-east-1
```

**3. Clone the project:**

```bash
git clone --depth 1 --filter=blob:none --sparse \
  https://github.com/aws-samples/serverless-patterns.git
cd serverless-patterns
git sparse-checkout set lambda-durable-java-sam
cd lambda-durable-java-sam
```

Then continue from [Build and Deploy](#build-and-deploy) below.

---

## Build and Deploy

### 1. Build the Durable Functions Container Image

```bash
cd durable-functions-sam/durable-functions
mvn clean package
```

Build the Docker image. Use the command that matches your environment:

**From EC2 instance (Amazon Linux x86_64):**
```bash
docker build -t durable-functions-java-examples .
```

**From local machine (macOS, Linux, or Windows with Docker Desktop):**
```bash
docker build --platform linux/amd64 --provenance=false -t durable-functions-java-examples .
```

> **Why these flags?**
> - `--platform linux/amd64` — Lambda runs on x86_64. Required on Apple Silicon Macs (M1/M2/M3/M4) to avoid building an ARM image. Harmless on x86_64 machines.
> - `--provenance=false` — Required on **all platforms** with Docker BuildKit (Docker 23+). Prevents Docker from producing OCI image indexes. Lambda only supports Docker V2 manifest format. Without this flag you'll see: *"The image manifest, config or layer media type... is not supported."*
>
> **Tip:** If you're unsure which platform you're on, always use the local machine command — it works everywhere.

### 2. Push to ECR

```bash
AWS_ACCOUNT_ID=$(aws sts get-caller-identity --query Account --output text)
AWS_REGION=${AWS_REGION:-$(aws configure get region)}

# Verify variables are set correctly before proceeding
echo "Account: $AWS_ACCOUNT_ID"
echo "Region:  $AWS_REGION"

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

> **Checkpoint:** Before continuing, verify the push succeeded and the image has the correct manifest type:
> ```bash
> aws ecr describe-images --repository-name durable-functions-java-examples --region $AWS_REGION \
>   --query 'imageDetails[?imageTags[0]==`latest`].imageManifestMediaType' --output text
> ```
> Expected output: `application/vnd.docker.distribution.manifest.v2+json`
>
> If you see `application/vnd.oci.image.index.v1+json` instead, rebuild the Docker image with `--provenance=false` and push again.

### 3. Deploy with SAM

Navigate to the SAM template directory:

**From EC2:**
```bash
cd /home/ec2-user/serverless-patterns/lambda-durable-java-sam/durable-functions-sam
```

**From local machine:**
```bash
cd ../..
cd durable-functions-sam
```

If you have a previously deployed stack, delete it first (durable execution config cannot be added to existing functions):
```bash
aws cloudformation delete-stack --stack-name <your-stack-name>
aws cloudformation wait stack-delete-complete --stack-name <your-stack-name>
```

Deploy:
```bash
sam deploy --guided --capabilities CAPABILITY_NAMED_IAM
```

When prompted:
- **Stack Name**: choose a name (e.g., `lambda-durable-java-sam`)
- **AWS Region**: enter your region (must match where you pushed the ECR image)
- **Parameter SNSTopicName**: press Enter to accept default
- **Confirm changes before deploy**: `N`
- **Allow SAM CLI IAM role creation**: `Y`
- **Disable rollback**: `N`
- **Save arguments to configuration file**: `Y`

Wait for `CREATE_COMPLETE`. If it fails, check the [Troubleshooting](#troubleshooting) section below.

### 4. Build the SNS Message Sender

```bash
cd ../sns-message-sender
mvn clean package
```

### 5. Trigger a Durable Function

Ensure `AWS_PROFILE` and `AWS_REGION` are set to the same profile/region you used for deployment (see Step 2 under Option B), then run:

```bash
java -cp target/sns-message-sender-1.0-SNAPSHOT.jar \
  sns.producer.DurableFunctionsTrigger DurableFunctionsSNSTopic chaining
```

> **Note:** On the EC2 instance (Option A), credentials are provided automatically via the instance role — no extra setup needed. If you get credential errors locally, see the [Troubleshooting](#troubleshooting) section.

---

## Troubleshooting

### "The image manifest, config or layer media type... is not supported"

The Docker image was pushed in OCI format. Lambda requires Docker V2 format. Fix:
```bash
docker build --platform linux/amd64 --provenance=false -t durable-functions-java-examples .
aws ecr delete-repository --repository-name durable-functions-java-examples --force
aws ecr create-repository --repository-name durable-functions-java-examples
docker tag durable-functions-java-examples:latest \
  $AWS_ACCOUNT_ID.dkr.ecr.$AWS_REGION.amazonaws.com/durable-functions-java-examples:latest
docker push \
  $AWS_ACCOUNT_ID.dkr.ecr.$AWS_REGION.amazonaws.com/durable-functions-java-examples:latest
```

### "JAVA_HOME environment variable is not defined correctly"

`JAVA_HOME` must point to the JDK root (e.g., `.../Contents/Home`), **not** the `bin` directory. Fix:
```bash
# Wrong:
export JAVA_HOME=/Library/Java/JavaVirtualMachines/amazon-corretto-21.jdk/Contents/Home/bin

# Correct:
export JAVA_HOME=/Library/Java/JavaVirtualMachines/amazon-corretto-21.jdk/Contents/Home
```

### "Cannot connect to the Docker daemon"

Docker is not running. Start your Docker runtime:
- **Docker Desktop**: Open Docker Desktop from Applications
- **Colima**: `colima start && docker context use colima`

### AWS_REGION is empty / ECR endpoint errors

Ensure `AWS_REGION` is set before running the commands:
```bash
export AWS_REGION=eu-west-2  # Your target region
```

### "Unable to load credentials from any of the providers in the chain" when triggering patterns

The Java AWS SDK cannot find valid credentials. Common causes and fixes:

1. **`AWS_PROFILE` not set** — The Java SDK uses the `default` profile unless told otherwise:
   ```bash
   export AWS_PROFILE=your-profile-name
   ```

2. **Profile uses `credential_process` or SSO** — Some credential sources (e.g., `credential_process`, `aws sso`) may not be compatible with all versions of the Java AWS SDK. Resolve by exporting credentials into the environment:
   ```bash
   eval $(aws configure export-credentials --profile your-profile --format env)
   ```

3. **Verify credentials work** — Test that the Java SDK can reach AWS:
   ```bash
   aws sts get-caller-identity
   ```
   If this works but the Java app doesn't, your profile likely uses a credential method the Java SDK can't invoke. Use the `eval` command above.

### Stack stuck in ROLLBACK_COMPLETE

Delete the failed stack before redeploying:
```bash
aws cloudformation delete-stack --stack-name <your-stack-name>
aws cloudformation wait stack-delete-complete --stack-name <your-stack-name>
```

## Triggering Each Pattern

```bash
# Pattern 1: Chaining - Sequential order processing
java -cp target/sns-message-sender-1.0-SNAPSHOT.jar \
  sns.producer.DurableFunctionsTrigger DurableFunctionsSNSTopic chaining

# Pattern 2: Fan-Out/Fan-In - Parallel data analysis
java -cp target/sns-message-sender-1.0-SNAPSHOT.jar \
  sns.producer.DurableFunctionsTrigger DurableFunctionsSNSTopic fanout

# Pattern 3: Human Interaction - Approval workflow (requires callback)
java -cp target/sns-message-sender-1.0-SNAPSHOT.jar \
  sns.producer.DurableFunctionsTrigger DurableFunctionsSNSTopic approval

# Pattern 4: Monitoring - Job status polling
java -cp target/sns-message-sender-1.0-SNAPSHOT.jar \
  sns.producer.DurableFunctionsTrigger DurableFunctionsSNSTopic monitoring

# Pattern 5: Timer - Scheduled reminders
java -cp target/sns-message-sender-1.0-SNAPSHOT.jar \
  sns.producer.DurableFunctionsTrigger DurableFunctionsSNSTopic timer

# Pattern 6: Error Handling - Resilient payment with saga
java -cp target/sns-message-sender-1.0-SNAPSHOT.jar \
  sns.producer.DurableFunctionsTrigger DurableFunctionsSNSTopic errorhandling

# Pattern 7: Map Processing - Batch concurrent processing
java -cp target/sns-message-sender-1.0-SNAPSHOT.jar \
  sns.producer.DurableFunctionsTrigger DurableFunctionsSNSTopic mapprocessing

# Pattern 8: Sub-Orchestration - Nested child workflows
java -cp target/sns-message-sender-1.0-SNAPSHOT.jar \
  sns.producer.DurableFunctionsTrigger DurableFunctionsSNSTopic suborchestration
```

## Completing the Human Interaction Callback

After triggering the `approval` pattern, check CloudWatch Logs for the callback ID, then:

```bash
# To approve:
aws lambda send-durable-execution-callback-success \
  --callback-id <CALLBACK_ID_FROM_LOGS> \
  --cli-binary-format raw-in-base64-out \
  --result '{"decision":"APPROVED","approver":"manager@example.com"}'

# To reject:
aws lambda send-durable-execution-callback-failure \
  --callback-id <CALLBACK_ID_FROM_LOGS> \
  --error ErrorType=Rejected,ErrorMessage="Budget exceeded policy limit"
```

## Step Diagrams

For visual step-by-step flow diagrams of each pattern, see [DIAGRAMS.md](DIAGRAMS.md).

## Key Concepts

### DurableHandler
All durable functions extend `DurableHandler<InputType, OutputType>` instead of implementing `RequestHandler`. This provides a `DurableContext` with durable operations.

### Steps
Steps checkpoint their results. On replay after a wait or failure, the SDK returns the stored result without re-executing the step body.

### Waits
`context.wait()` suspends execution without consuming compute. The backend resumes the function when the duration elapses.

### Callbacks
`context.createCallback()` suspends execution and waits for an external system to call `SendDurableExecutionCallbackSuccess`.

### Parallel & Map
`context.parallel()` runs different operations concurrently. `context.map()` applies the same operation to each item in a collection.

### Child Contexts
`context.runInChildContext()` creates isolated sub-workflows with their own operation namespaces.

### Retry Strategies
Configure automatic retries with exponential backoff, jitter, and error filtering using `StepConfig` and `RetryStrategies`.

## Monitoring

View durable execution status:
```bash
aws lambda list-durable-executions --function-name durable-chaining-example:1
aws lambda get-durable-execution --function-name durable-chaining-example:1 --execution-id <ID>
```

## Project Structure

```
lambda-durable-java-sam/
├── README.md
├── USER_GUIDE.md
├── DEVELOPER_GUIDE.md
├── build-and-deploy.sh
├── infrastructure/
│   └── ec2-client-instance.yaml      # VPC + EC2 CloudFormation template
├── durable-functions-sam/
│   ├── template.yaml                  # SAM template for all Lambda functions
│   └── durable-functions/
│       ├── pom.xml
│       ├── Dockerfile
│       └── src/main/java/com/amazonaws/samples/durable/
│           ├── models/                # Shared model classes
│           ├── chaining/              # Pattern 1: Sequential steps
│           ├── fanout/                # Pattern 2: Parallel execution
│           ├── humaninteraction/      # Pattern 3: Callbacks
│           ├── monitoring/            # Pattern 4: Polling
│           ├── timer/                 # Pattern 5: Scheduled delays
│           ├── errorhandling/         # Pattern 6: Retries & compensation
│           ├── mapprocessing/         # Pattern 7: Collection processing
│           └── suborchestration/      # Pattern 8: Child contexts
└── sns-message-sender/
    ├── pom.xml
    └── src/main/java/sns/producer/
        └── DurableFunctionsTrigger.java
```
