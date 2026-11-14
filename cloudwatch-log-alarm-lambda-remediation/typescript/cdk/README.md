# Amazon CloudWatch Log Alarm with AWS Lambda Auto-Remediation

This pattern deploys a self-healing architecture using the Amazon CloudWatch Log Alarm resource (`AWS::CloudWatch::LogAlarm`) to monitor application logs with CloudWatch Logs Insights queries and automatically trigger remediation through AWS Lambda and AWS Systems Manager when error thresholds are breached.

Learn more about this pattern at Serverless Land Patterns: https://serverlessland.com/patterns/cloudwatch-log-alarm-lambda-remediation-cdk

## Architecture

```
┌─────────────────────┐     ┌──────────────────────────┐     ┌─────────────┐     ┌──────────────┐     ┌──────────────────┐
│ Amazon CloudWatch   │────▶│ Amazon CloudWatch         │────▶│ Amazon SNS  │────▶│ AWS Lambda   │────▶│ AWS Systems      │
│ Logs                │     │ Log Alarm                 │     │             │     │ (Remediation)│     │ Manager          │
│ (Application Logs)  │     │ (Logs Insights Query)     │     │             │     │              │     │ (RunCommand)     │
└─────────────────────┘     └──────────────────────────┘     └─────────────┘     └──────────────┘     └──────────────────┘
```

**How it works:**

1. Application logs are written to Amazon CloudWatch Logs
2. The Amazon CloudWatch Log Alarm runs a CloudWatch Logs Insights query every 5 minutes to count ERROR messages
3. When error count ≥ 5 in a single evaluation window, the alarm transitions to ALARM state
4. The alarm publishes to Amazon SNS, which invokes the AWS Lambda remediation function
5. AWS Lambda sends a command via AWS Systems Manager to restart the application service on tagged Amazon EC2 instances

The `AWS::CloudWatch::LogAlarm` resource eliminates the need for metric filters. Previously, monitoring log content required creating a CloudWatch Metric Filter, waiting for metric data points, then creating a standard alarm on that metric. Log Alarms run Logs Insights queries directly on schedule and evaluate results against thresholds.

## Requirements

- [AWS CDK v2](https://docs.aws.amazon.com/cdk/v2/guide/getting_started.html) installed and configured
- [Node.js 20+](https://nodejs.org/) with npm
- AWS account [bootstrapped for CDK](https://docs.aws.amazon.com/cdk/v2/guide/bootstrapping.html)
- Python 3.12 (for AWS Lambda functions)
- (Optional) Amazon EC2 instances tagged with `AutoRemediate=true` for SSM remediation

## Deployment

### Step 1: Install dependencies and synthesize

```bash
cd cloudwatch-log-alarm-lambda-remediation-cdk/cdk
npm install
npx cdk synth
```

### Step 2: Deploy the stack

```bash
npx cdk deploy
```

## Testing

### 1. Generate error logs to trigger the alarm

```bash
LOG_GROUP="/app/monitored-service"

# Write ERROR messages to trigger the alarm (threshold = 5)
for i in $(seq 1 6); do
  aws logs put-log-events \
    --log-group-name "$LOG_GROUP" \
    --log-stream-name "test-stream" \
    --log-events "[{\"timestamp\":$(date +%s000),\"message\":\"ERROR: Connection timeout to database (attempt $i)\"}]" \
    --sequence-token "$(aws logs describe-log-streams --log-group-name $LOG_GROUP --log-stream-name-prefix test --query 'logStreams[0].uploadSequenceToken' --output text 2>/dev/null)"
  sleep 1
done

echo "Wrote 6 ERROR messages. Alarm will evaluate in ~5 minutes."
```

### 2. Check alarm state (after 5 minutes)

```bash
aws cloudwatch describe-alarms \
  --alarm-names "app-error-rate-alarm" \
  --alarm-types "LogAlarm" \
  --query 'LogAlarms[0].{State:StateValue,Reason:StateReason}'
```

### 3. Verify the AWS Lambda function was invoked

```bash
aws logs filter-log-events \
  --log-group-name "/aws/lambda/CloudwatchLogAlarmLambdaRem-RemediationFn*" \
  --filter-pattern "Executing remediation" \
  --query 'events[].message'
```

### 4. Check AWS Systems Manager command history

```bash
aws ssm list-commands \
  --filters "key=DocumentName,value=AWS-RunShellScript" \
  --max-results 5 \
  --query 'Commands[].{Id:CommandId,Status:Status,Comment:Comment}'
```

## Cleanup

> **Warning:** This will delete the log group and all log data. The Amazon CloudWatch Log Alarm and all associated resources will be removed.

```bash
cd cloudwatch-log-alarm-lambda-remediation-cdk/cdk
npx cdk destroy
```

## Services Used

| Service | Role |
|---------|------|
| Amazon CloudWatch Logs | Application log storage and query target |
| Amazon CloudWatch Log Alarm | Scheduled Logs Insights query with threshold evaluation |
| Amazon SNS | Alarm notification delivery to subscribers |
| AWS Lambda | Auto-remediation logic (classify alarm, invoke SSM) |
| AWS Systems Manager | Execute commands on tagged Amazon EC2 instances |

----
Copyright 2026 Amazon.com, Inc. or its affiliates. All Rights Reserved.
SPDX-License-Identifier: MIT-0
