# AWS Security Hub Auto-Remediation with AWS Step Functions

This pattern deploys an automated remediation pipeline for AWS Security Hub findings. When HIGH or CRITICAL findings are detected, Amazon EventBridge routes them to an AWS Step Functions workflow that classifies the finding type and executes targeted remediation via AWS Lambda — closing open security groups, blocking public S3 bucket access, and marking findings as resolved.

Learn more about this pattern at Serverless Land Patterns: https://serverlessland.com/patterns/securityhub-finding-sfn-remediation-cdk

## Architecture

```
┌───────────────────┐     ┌────────────────────┐     ┌────────────────────────────────────┐
│ AWS Security Hub  │────▶│ Amazon EventBridge  │────▶│ AWS Step Functions                  │
│ (HIGH/CRITICAL)   │     │ (Finding Rule)      │     │ (Classify + Route)                  │
└───────────────────┘     └────────────────────┘     └─────────────┬──────────────────────┘
                                                                   │
                                                    ┌──────────────┼──────────────┐
                                                    ▼              ▼              ▼
                                              ┌──────────┐  ┌──────────┐  ┌────────────┐
                                              │ Open SG  │  │ Public   │  │ Unsupported│
                                              │ → Revoke │  │ Bucket   │  │ → Skip     │
                                              │ ingress  │  │ → Block  │  └────────────┘
                                              └────┬─────┘  └────┬─────┘
                                                   │              │
                                                   ▼              ▼
                                              ┌──────────────────────────┐
                                              │ Amazon SNS (Alert)       │
                                              │ + Update Finding Status  │
                                              └──────────────────────────┘
```

**How it works:**

1. AWS Security Hub detects a HIGH or CRITICAL finding (e.g., open security group, public Amazon S3 bucket)
2. Amazon EventBridge matches the finding and triggers the AWS Step Functions workflow
3. AWS Step Functions classifies the finding type and routes to the appropriate remediation path
4. AWS Lambda executes the remediation:
   - **Open Security Group:** Revokes 0.0.0.0/0 ingress rules and tags the resource
   - **Public Amazon S3 Bucket:** Enables full public access block
5. AWS Lambda updates the finding status to RESOLVED in AWS Security Hub
6. Amazon SNS delivers a notification to the security team with remediation details

## Requirements

- [AWS CDK v2](https://docs.aws.amazon.com/cdk/v2/guide/getting_started.html) installed and configured
- [Node.js 20+](https://nodejs.org/) with npm
- AWS account [bootstrapped for CDK](https://docs.aws.amazon.com/cdk/v2/guide/bootstrapping.html)
- AWS Security Hub enabled in your account
- Python 3.12 (for AWS Lambda functions)

## Deployment

> **Prerequisite:** AWS Security Hub must be enabled in the target account and Region before deploying. Enable it with `aws securityhub enable-security-hub` (or via the console). Without it, no findings are generated and the workflow is never triggered.

```bash
cd securityhub-finding-sfn-remediation-cdk/cdk
npm install
cdk deploy
```

## Testing

### Option 1: Fast test with a sample finding event (recommended)

You can exercise the workflow directly without waiting for AWS Security Hub to
generate a finding. This starts an execution with a sample "open security group"
finding and confirms the Choice state routes to remediation.

```bash
SFN_ARN=$(aws cloudformation describe-stacks \
  --stack-name SecurityhubFindingSfnRemediationStack \
  --query "Stacks[0].Outputs[?OutputKey=='StateMachineArn'].OutputValue" \
  --output text)

aws stepfunctions start-execution \
  --state-machine-arn "$SFN_ARN" \
  --input '{
    "detail": {
      "findings": [
        {
          "Id": "test-finding-001",
          "Type": "Software and Configuration Checks/AWS Security Best Practices/EC2.2",
          "ProductArn": "arn:aws:securityhub:us-east-1::product/aws/securityhub",
          "Severity": { "Label": "HIGH" },
          "Resources": [{ "Id": "arn:aws:ec2:us-east-1:111122223333:security-group/sg-example" }]
        }
      ]
    }
  }'

# Confirm the execution reached the remediation path (SUCCEEDED)
aws stepfunctions list-executions \
  --state-machine-arn "$SFN_ARN" --max-results 1 \
  --query "executions[0].{Status:status,Name:name}"
```

The sample `sg-example` will not exist in your account, so the AWS Lambda function records a
`NO_SG_FOUND` result. The execution still SUCCEEDS, confirming the Choice state,
AWS Lambda invocation, and Amazon SNS notification wiring all work end to end.

### Option 2: Generate a real Security Hub finding

```bash
# Create a deliberately open security group to trigger a finding
SG_ID=$(aws ec2 create-security-group \
  --group-name test-open-sg \
  --description "Test open SG for remediation" \
  --query 'GroupId' --output text)

aws ec2 authorize-security-group-ingress \
  --group-id $SG_ID \
  --protocol tcp --port 22 --cidr 0.0.0.0/0

echo "Created open SG: $SG_ID. AWS Security Hub will detect this within 15 minutes"
```

### Verify remediation after Security Hub detects the finding

```bash
# Check Step Functions executions
SFN_ARN=$(aws cloudformation describe-stacks \
  --stack-name SecurityhubFindingSfnRemediationStack \
  --query "Stacks[0].Outputs[?OutputKey=='StateMachineArn'].OutputValue" \
  --output text)

aws stepfunctions list-executions \
  --state-machine-arn $SFN_ARN --max-results 5 \
  --query 'executions[].{Status:status,Start:startDate}'

# Verify the security group was closed
aws ec2 describe-security-groups --group-ids $SG_ID \
  --query 'SecurityGroups[0].IpPermissions'
```

### Subscribe to alerts

```bash
TOPIC_ARN=$(aws cloudformation describe-stacks \
  --stack-name SecurityhubFindingSfnRemediationStack \
  --query 'Stacks[0].Outputs[?OutputKey==`AlertTopicArn`].OutputValue' \
  --output text)

aws sns subscribe --topic-arn $TOPIC_ARN --protocol email \
  --notification-endpoint security-team@example.com
```

## Cleanup

> **Warning:** After destroying this stack, Security Hub findings will no longer be auto-remediated.

```bash
cd securityhub-finding-sfn-remediation-cdk/cdk
cdk destroy
```

## Services Used

| Service | Role |
|---------|------|
| AWS Security Hub | Detects misconfigurations and compliance violations |
| Amazon EventBridge | Routes HIGH/CRITICAL findings to the remediation workflow |
| AWS Step Functions | Classifies finding type and orchestrates remediation |
| AWS Lambda | Executes remediation actions (revoke SG rules, block S3 access) |
| Amazon SNS | Delivers remediation alerts to the security team |

----
Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
SPDX-License-Identifier: MIT-0
