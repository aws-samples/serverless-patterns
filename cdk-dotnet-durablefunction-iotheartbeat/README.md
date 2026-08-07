# AWS Lambda Durable Function — IoT Device Heartbeat Monitor (Eternal Orchestration)

This sample demonstrates the **eternal orchestration** (continue-as-new) pattern using **AWS Lambda Durable Functions** for .NET. A durable function runs indefinitely, monitoring heartbeat signals from an IoT device. If no heartbeat arrives within a timeout, it marks the device offline and sends an SNS alert. Periodically, the orchestration restarts with fresh history to prevent unbounded checkpoint growth.

## Architecture

```
┌─────────────┐       ┌───────────────┐      ┌───────────────────────┐
│  IoT Device │──────▶│ API Gateway   │─────▶│  Heartbeat Receiver   │──▶ DynamoDB
│  (periodic) │ HTTPS │ (API Key auth)│      │  (Lambda)             │   (LastHeartbeatAt)
└─────────────┘       └───────────────┘      └───────────────────────┘
               x-api-key header                                              │
                                                                             │ reads
                                                                             ▼
┌──────────────────────────────────────────────────────────────────────────────────┐
│              Heartbeat Monitor (Durable Function — Eternal)                      │
│                                                                                  │
│  ┌───────────────────────────────────────────────────────────────────────────┐  │
│  │  Cycle 1..N (loop until MaxCyclesBeforeRestart):                          │  │
│  │                                                                           │  │
│  │    ┌─────────────┐    ┌──────────────────┐    ┌───────────────────────┐  │  │
│  │    │ WaitAsync    │───▶│ Check DynamoDB   │───▶│ Online? → update      │  │  │
│  │    │ (timeout)    │    │ for heartbeat    │    │ Offline? → alert SNS  │  │  │
│  │    │ No compute!  │    │                  │    │                       │  │  │
│  │    └─────────────┘    └──────────────────┘    └───────────────────────┘  │  │
│  └───────────────────────────────────────────────────────────────────────────┘  │
│                                                                                  │
│  After N cycles: self-invoke (continue-as-new) → fresh execution                │
└──────────────────────────────────────────────────────────────────────────────────┘
```

## What It Demonstrates

- **Eternal orchestration** — The workflow runs in an infinite loop, monitoring a device forever. Each cycle waits, checks, and either confirms online or alerts offline.
- **Continue-as-new** — After a configurable number of cycles (default 100), the function self-invokes with the same input, starting a fresh durable execution. This prevents the checkpoint history from growing unboundedly.
- **Durable timers (WaitAsync)** — Each cycle suspends execution for the heartbeat timeout period. The Lambda terminates — zero compute charges during the wait.
- **API key authentication** — Devices authenticate via an `x-api-key` header on API Gateway. The simplest form of device auth — no IAM roles, no user pools.
- **SNS alerting** — When a missed heartbeat is detected, the monitor sends an alert to an SNS topic.
- **CDK infrastructure** — API Gateway with API key, DynamoDB, SNS, and two Lambda functions.

## Project Structure

```
├── cdk.json
├── src/
│   ├── CdkDotnetDurablefunctionIotheartbeat.slnx
│   ├── .globalconfig
│   ├── Infra/
│   │   ├── Program.cs
│   │   ├── InfraStack.cs
│   │   ├── GlobalSuppressions.cs
│   │   └── Infra.csproj
│   └── HeartbeatMonitor/
│       ├── HeartbeatMonitorHandler.cs   # Eternal durable workflow
│       ├── HeartbeatReceiverHandler.cs  # Device heartbeat endpoint
│       ├── DeviceService.cs             # DynamoDB + SNS operations
│       ├── Models.cs                    # Record types
│       └── HeartbeatMonitor.csproj
└── README.md
```

---

## Prerequisites

- [.NET 10 SDK](https://dotnet.microsoft.com/download/dotnet/10.0)
- [AWS CDK CLI](https://docs.aws.amazon.com/cdk/v2/guide/getting-started.html) (`npm install -g aws-cdk`)
- AWS account with credentials configured (`aws configure`)
- CDK bootstrapped (`cdk bootstrap`)

---

## Build & Deploy

```bash
dotnet build src/CdkDotnetDurablefunctionIotheartbeat.slnx -c Release
cdk deploy
```

The CDK automatically publishes the Lambda during synthesis.

---

## Testing

### Capture stack outputs

```bash
STACK_NAME="CdkDotnetDurablefunctionIotheartbeatStack"

API_URL=$(aws cloudformation describe-stacks \
    --stack-name $STACK_NAME \
    --query "Stacks[0].Outputs[?OutputKey=='HeartbeatApiUrl'].OutputValue" \
    --output text)

MONITOR_ARN=$(aws cloudformation describe-stacks \
    --stack-name $STACK_NAME \
    --query "Stacks[0].Outputs[?OutputKey=='HeartbeatMonitorFunctionArn'].OutputValue" \
    --output text)

TABLE_NAME=$(aws cloudformation describe-stacks \
    --stack-name $STACK_NAME \
    --query "Stacks[0].Outputs[?OutputKey=='DeviceTableName'].OutputValue" \
    --output text)

# Retrieve the API key value
API_KEY_ID=$(aws cloudformation describe-stacks \
    --stack-name $STACK_NAME \
    --query "Stacks[0].Outputs[?OutputKey=='ApiKeyId'].OutputValue" \
    --output text)

API_KEY=$(aws apigateway get-api-key \
    --api-key $API_KEY_ID \
    --include-value \
    --query 'value' --output text)
```

### Start monitoring a device

```bash
aws lambda invoke \
    --function-name "$MONITOR_ARN:\$LATEST" \
    --invocation-type Event \
    --cli-binary-format raw-in-base64-out \
    --payload '{"DeviceId":"sensor-001","HeartbeatTimeoutSeconds":30,"MaxCyclesBeforeRestart":50}' \
    /tmp/invoke-response.json
```

The monitor starts and waits 30 seconds for the first heartbeat.

> **Note:** After a fresh `cdk deploy`, API Gateway API key associations may take 1–2 minutes to propagate. If you receive `{"message":"Forbidden"}` immediately after deployment despite having a valid API key, wait a minute and try again.

### Send heartbeats (simulate a device)

```bash
# Send a heartbeat (include x-api-key header for authentication)
curl -X POST "${API_URL%/}/heartbeat" \
    -H "Content-Type: application/json" \
    -H "x-api-key: $API_KEY" \
    -d '{"DeviceId":"sensor-001"}'

# Repeat periodically (every 20s) to keep the device "online"
while true; do
    curl -s -X POST "${API_URL%/}/heartbeat" \
        -H "Content-Type: application/json" \
        -H "x-api-key: $API_KEY" \
        -d '{"DeviceId":"sensor-001"}'
    echo " - heartbeat sent at $(date)"
    sleep 20
done
```

### Stop sending heartbeats

Stop the loop above. After 30 seconds (the timeout), the monitor will:
1. Check DynamoDB and find no recent heartbeat
2. Mark the device as "offline"
3. Send an SNS alert

### Check device status

```bash
aws dynamodb get-item \
    --table-name $TABLE_NAME \
    --key '{"DeviceId":{"S":"sensor-001"}}'
```

### Check durable execution status

```bash
aws lambda list-durable-executions-by-function \
    --function-name $MONITOR_ARN
```

### Verify automatic restart (continue-as-new)

The monitor automatically restarts after `MaxCyclesBeforeRestart` cycles (default 50) to prevent unbounded checkpoint growth. To observe this, start a monitor with a low cycle limit and short timeout:

```bash
# Start a monitor with 5 cycles and 10-second timeout (restarts after ~50 seconds)
aws lambda invoke \
    --function-name "$MONITOR_ARN:\$LATEST" \
    --invocation-type Event \
    --cli-binary-format raw-in-base64-out \
    --payload '{"DeviceId":"sensor-restart-test","HeartbeatTimeoutSeconds":10,"MaxCyclesBeforeRestart":5}' \
    /tmp/invoke-response.json
```

Wait about 60 seconds, then list all executions:

```bash
aws lambda list-durable-executions-by-function \
    --function-name $MONITOR_ARN \
    --query "DurableExecutions[].{Status:Status,Started:StartTimestamp}" \
    --output table
```

You should see multiple executions — the original completing with `SUCCEEDED` status (it reached the cycle limit and self-invoked) and a new one in `RUNNING` status (the fresh restart):

```
-------------------------------------------
|    ListDurableExecutionsByFunction      |
+-----------+-----------------------------+
|  Status   |          Started            |
+-----------+-----------------------------+
|  RUNNING  |  2026-07-15T09:15:50.000Z   |  ← new execution (continue-as-new)
|  SUCCEEDED|  2026-07-15T09:14:59.000Z   |  ← original (completed 5 cycles)
+-----------+-----------------------------+
```

To confirm the restart happened, check the completed execution's result:

```bash
# Get the ARN of the completed execution
COMPLETED_ARN=$(aws lambda list-durable-executions-by-function \
    --function-name $MONITOR_ARN \
    --query "DurableExecutions[?Status=='SUCCEEDED'].DurableExecutionArn | [0]" \
    --output text)

aws lambda get-durable-execution \
    --durable-execution-arn $COMPLETED_ARN \
    --query "OutputPayload" --output text
```

The output shows `"Reason":"cycle_limit_reached"` confirming it self-restarted:

```json
{"DeviceId":"sensor-restart-test","Reason":"cycle_limit_reached","CompletedCycles":5,"RestartedAt":"..."}
```

Clean up the test device when done:

```bash
# Stop all running executions for the test device
aws lambda list-durable-executions-by-function \
    --function-name $MONITOR_ARN \
    --query "DurableExecutions[?Status=='RUNNING'].DurableExecutionArn" \
    --output text \
    | tr '\t' '\n' \
    | while read -r arn; do
        aws lambda stop-durable-execution --durable-execution-arn "$arn"
    done
```

### Subscribe to alerts (optional)

```bash
TOPIC_ARN=$(aws cloudformation describe-stacks \
    --stack-name $STACK_NAME \
    --query "Stacks[0].Outputs[?OutputKey=='AlertTopicArn'].OutputValue" \
    --output text)

aws sns subscribe \
    --topic-arn $TOPIC_ARN \
    --protocol email \
    --notification-endpoint your@email.com
```

### Stop monitoring a device

To stop an active heartbeat monitor, list the running executions and stop the one for your device:

```bash
# List active executions
aws lambda list-durable-executions-by-function \
    --function-name $MONITOR_ARN \
    --query "DurableExecutions[?Status=='RUNNING'].[DurableExecutionArn]" \
    --output text

# Stop a specific execution
EXECUTION_ARN="<arn-from-above>"
aws lambda stop-durable-execution \
    --durable-execution-arn $EXECUTION_ARN
```

Or stop all running executions for the monitor function:

```bash
aws lambda list-durable-executions-by-function \
    --function-name $MONITOR_ARN \
    --query "DurableExecutions[?Status=='RUNNING'].DurableExecutionArn" \
    --output text \
    | tr '\t' '\n' \
    | while read -r arn; do
        echo "Stopping: $arn"
        aws lambda stop-durable-execution \
            --durable-execution-arn "$arn"
    done
```

---

## How the Eternal Orchestration Pattern Works

```csharp
private async Task<MonitorResult> Workflow(MonitorInput input, IDurableContext ctx)
{
    var cycleCount = 0;

    // Eternal loop — runs until cycle limit
    while (cycleCount < input.MaxCyclesBeforeRestart)
    {
        cycleCount++;

        // Suspend for timeout period (no compute charges)
        await ctx.WaitAsync(timeout, name: $"wait-cycle-{cycleCount}");

        // Check DynamoDB for recent heartbeat
        var lastHeartbeat = await ctx.StepAsync(..., name: $"check-heartbeat-{cycleCount}");

        if (heartbeatReceived)
            // Mark online
        else
            // Mark offline + send SNS alert
    }

    // Continue-as-new: self-invoke with same input, fresh execution history
    await ctx.StepAsync(async (_, ct) =>
    {
        await LambdaClient.InvokeAsync(new InvokeRequest
        {
            FunctionName = $"{functionName}:$LATEST",
            InvocationType = InvocationType.Event,
            Payload = JsonSerializer.Serialize(input)
        }, ct);
    }, name: "continue-as-new");
}
```

**Why continue-as-new?** Each durable execution accumulates checkpoint history. For an eternal workflow, this grows without bound. By self-invoking after N cycles, the new execution starts fresh with zero history while maintaining logical continuity.

---

## Configuration

| Parameter | Default | Description |
|-----------|---------|-------------|
| `HeartbeatTimeoutSeconds` | 60 | How long to wait before checking for a heartbeat |
| `MaxCyclesBeforeRestart` | 100 | Cycles before performing continue-as-new |
| `DeviceId` | (required) | The device identifier to monitor |

---

## Cleanup

```bash
cdk destroy
```

---

## Useful Commands

| Command | Description |
|---------|-------------|
| `dotnet build src/CdkDotnetDurablefunctionIotheartbeat.slnx` | Build the solution |
| `cdk synth` | Synthesize CloudFormation (auto-publishes Lambda) |
| `cdk deploy` | Deploy the stack |
| `cdk destroy` | Tear down all resources |

---

## References

- [Amazon.Lambda.DurableExecution SDK](https://github.com/aws/aws-lambda-dotnet/tree/master/Libraries/src/Amazon.Lambda.DurableExecution)
- [Wait documentation](https://github.com/aws/aws-lambda-dotnet/blob/master/Libraries/src/Amazon.Lambda.DurableExecution/docs/core/wait.md)
- [Steps documentation](https://github.com/aws/aws-lambda-dotnet/blob/master/Libraries/src/Amazon.Lambda.DurableExecution/docs/core/steps.md)
- [AWS CDK .NET Reference](https://docs.aws.amazon.com/cdk/api/v2/dotnet/)
