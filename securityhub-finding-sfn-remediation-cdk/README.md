# AWS Security Hub Auto-Remediation with AWS Step Functions

This pattern deploys an automated remediation pipeline for AWS Security Hub findings. When HIGH or CRITICAL findings are detected, Amazon EventBridge routes them to an AWS Step Functions workflow that classifies the finding type and executes targeted remediation via AWS Lambda — closing open security groups, blocking public S3 bucket access, and marking findings as resolved.

Important: This is the first AWS Security Hub pattern in the serverless-patterns repo. Every AWS account with Security Hub enabled accumulates findings that require manual triage. This pattern automates the response for common CIS benchmark violations.

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

```bash
cd securityhub-finding-sfn-remediation-cdk/cdk
npm install
npx cdk deploy
```

## Testing

### Generate a sample Security Hub finding

```bash
# Create a deliberately open security group to trigger a finding
SG_ID=$(aws ec2 create-security-group \
  --group-name test-open-sg \
  --description "Test open SG for remediation" \
  --query 'GroupId' --output text)

aws ec2 authorize-security-group-ingress \
  --group-id $SG_ID \
  --protocol tcp --port 22 --cidr 0.0.0.0/0

echo "Created open SG: $SG_ID — Security Hub will detect this within 15 minutes"
```

### Verify remediation after Security Hub detects the finding

```bash
# Check Step Functions executions
SFN_ARN=$(aws cloudformation describe-stacks \
  --stack-name SecurityhubFindingSfnRemediationStack \
  --query 'Stacks[0].Outputs[?OutputKey==`StateMachineArn`].OutputValue' \
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
npx cdk destroy
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
