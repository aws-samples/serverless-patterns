# Amazon GuardDuty Sensitive File Modification with AWS Step Functions Incident Response

This pattern deploys an automated incident response architecture that detects sensitive file modifications on Amazon EC2 instances using Amazon GuardDuty, classifies findings by severity using AWS Step Functions, and automatically isolates compromised instances via AWS Lambda while notifying security teams through Amazon SNS.

Important: This pattern is fundamentally different from the existing `guardduty-malware-s3` pattern, which scans S3 objects for malware and sends notifications. This pattern handles **host-level runtime threat detection** with **automated incident response orchestration** — isolating compromised instances, creating forensic snapshots, and tagging for investigation.

Learn more about this pattern at Serverless Land Patterns: https://serverlessland.com/patterns/guardduty-file-modification-sfn-response-cdk

## Architecture

```
┌──────────────────┐     ┌─────────────────────┐     ┌──────────────────────────────────────────────────────┐
│ Amazon GuardDuty │────▶│ Amazon EventBridge  │────▶│ AWS Step Functions (Incident Response Workflow)       │
│ (Finding)        │     │ (rule)              │     │                                                      │
└──────────────────┘     └─────────────────┘     │  ┌─────────────────┐                                │
                                                  │  │ Classify         │                                │
                                                  │  │ Severity         │                                │
                                                  │  └────────┬────────┘                                │
                                                  │           │                                          │
                                                  │  ┌────────┼────────────────┐                        │
                                                  │  │ HIGH   │ MEDIUM  │ LOW  │                        │
                                                  │  ▼        ▼         ▼      │                        │
                                                  │  Isolate  Notify    Log    │                        │
                                                  │  + Notify  Only     Only   │                        │
                                                  └──────────────────────────────────────────────────────┘
                                                       │          │
                                                       ▼          ▼
                                                  ┌────────────────┐  ┌──────────────┐
                                                  │ AWS Lambda     │  │ Amazon SNS   │
                                                  │ (Isolate)      │  │ (Alerts)     │
                                                  └─────┬──────────┘  └──────────────┘
                                                  └─────┬────┘
                                                        │
                                                        ▼
                                                  ┌──────────────────┐
                                                  │ Amazon EC2 API   │
                                                  │ (Replace SG,     │
                                                  │  Snapshot,       │
                                                  │  Tag)            │
                                                  └──────────────────┘
```

**How it works:**

1. Amazon GuardDuty detects sensitive file modifications or unauthorized access on Amazon EC2 instances
2. Amazon EventBridge captures the finding and triggers the AWS Step Functions workflow
3. AWS Step Functions classifies the finding severity:
   - **HIGH (≥7):** Isolate instance + create forensic snapshot + notify
   - **MEDIUM (4-6):** Notify security team only
   - **LOW (<4):** Log the finding only
4. For HIGH severity: AWS Lambda replaces the instance security group (network isolation), creates EBS snapshots for forensics, and tags the instance for investigation
5. Amazon SNS delivers alerts to the security team

## Requirements

- [AWS CDK v2](https://docs.aws.amazon.com/cdk/v2/guide/getting_started.html) installed and configured
- [Node.js 20+](https://nodejs.org/) with npm
- AWS account [bootstrapped for CDK](https://docs.aws.amazon.com/cdk/v2/guide/bootstrapping.html)
- Python 3.12 (for AWS Lambda functions)
- Amazon GuardDuty: an account has at most one detector per Region. If GuardDuty is **not** already enabled, this stack creates a detector for you. If a detector **already exists**, deployment fails with `A detector already exists for the current account` unless you pass its ID with the `DetectorId` parameter (see Deployment below). Find an existing detector with `aws guardduty list-detectors`.

## Deployment

```bash
cd guardduty-file-modification-sfn-response-cdk/cdk
npm install
npx cdk deploy
```

If a GuardDuty detector already exists in this account and Region, pass its ID so the stack reuses it instead of trying to create a second one:

```bash
npx cdk deploy --parameters DetectorId=$(aws guardduty list-detectors --query 'DetectorIds[0]' --output text)
```

## Testing

### 1. Subscribe to incident alerts first

Subscribe (and confirm the subscription from your inbox) **before** generating a finding, so the alert email is delivered during the test:

```bash
TOPIC_ARN=$(aws cloudformation describe-stacks \
  --stack-name GuarddutyFileModificationSfnResponseStack \
  --query 'Stacks[0].Outputs[?OutputKey==`IncidentTopicArn`].OutputValue' \
  --output text)

aws sns subscribe \
  --topic-arn $TOPIC_ARN \
  --protocol email \
  --notification-endpoint your-security-team@example.com
```

### 2. Simulate a GuardDuty finding (using sample findings)

```bash
# Generate sample findings to test the pipeline
DETECTOR_ID=$(aws cloudformation describe-stacks \
  --stack-name GuarddutyFileModificationSfnResponseStack \
  --query 'Stacks[0].Outputs[?OutputKey==`DetectorIdOutput`].OutputValue' \
  --output text)

aws guardduty create-sample-findings \
  --detector-id $DETECTOR_ID \
  --finding-types "UnauthorizedAccess:EC2/SSHBruteForce"
```

### 3. Verify AWS Step Functions execution

```bash
SFN_ARN=$(aws cloudformation describe-stacks \
  --stack-name GuarddutyFileModificationSfnResponseStack \
  --query 'Stacks[0].Outputs[?OutputKey==`StateMachineArn`].OutputValue' \
  --output text)

aws stepfunctions list-executions \
  --state-machine-arn $SFN_ARN \
  --max-results 5 \
  --query 'executions[].{Status:status,Start:startDate}'
```

## Cleanup

> **Warning:** This will delete the Amazon GuardDuty detector created by this stack. If you passed an existing detector via the `DetectorId` parameter, that detector is left untouched.

```bash
cd guardduty-file-modification-sfn-response-cdk/cdk
npx cdk destroy
```

If the isolation workflow ran during testing, it created resources **outside** the stack that `cdk destroy` does not remove. Delete them manually:

```bash
# Isolation security groups created by the AWS Lambda function
aws ec2 describe-security-groups \
  --filters "Name=tag:Purpose,Values=GuardDuty-Isolation" \
  --query 'SecurityGroups[].GroupId' --output text | \
  xargs -r -n1 aws ec2 delete-security-group --group-id

# Forensic EBS snapshots created by the AWS Lambda function
aws ec2 describe-snapshots --owner-ids self \
  --filters "Name=tag:Purpose,Values=GuardDuty-Forensics" \
  --query 'Snapshots[].SnapshotId' --output text | \
  xargs -r -n1 aws ec2 delete-snapshot --snapshot-id
```

Isolated instances also keep their `GuardDuty:*` tags and the isolation security group as their only group; restore their original security groups (recorded in the `GuardDuty:OriginalSecurityGroups` tag) before terminating or returning them to service.

## Services Used

| Service | Role |
|---------|------|
| Amazon GuardDuty | Detects sensitive file modifications and unauthorized access on Amazon EC2 |
| Amazon EventBridge | Routes GuardDuty findings to the incident response workflow |
| AWS Step Functions | Orchestrates severity classification and response actions |
| AWS Lambda | Isolates compromised instances (replace SG, snapshot, tag) |
| Amazon SNS | Delivers incident alerts to the security team |
| Amazon EC2 | Target of isolation actions (security group replacement, snapshots) |

----
Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
SPDX-License-Identifier: MIT-0
