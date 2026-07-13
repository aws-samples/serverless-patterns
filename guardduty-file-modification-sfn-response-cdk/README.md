# Amazon GuardDuty Sensitive File Modification with AWS Step Functions Incident Response

This pattern deploys an automated incident response architecture that detects sensitive file modifications on Amazon EC2 instances using Amazon GuardDuty, classifies findings by severity using AWS Step Functions, and automatically isolates compromised instances via AWS Lambda while notifying security teams through Amazon SNS.

Important: This pattern is fundamentally different from the existing `guardduty-malware-s3` pattern, which scans S3 objects for malware and sends notifications. This pattern handles **host-level runtime threat detection** with **automated incident response orchestration** — isolating compromised instances, creating forensic snapshots, and tagging for investigation.

Learn more about this pattern at Serverless Land Patterns: https://serverlessland.com/patterns/guardduty-file-modification-sfn-response-cdk

## Architecture

```
┌──────────────────┐     ┌─────────────────┐     ┌──────────────────────────────────────────────────────┐
│ Amazon GuardDuty │────▶│ Amazon           │────▶│ AWS Step Functions (Incident Response Workflow)       │
│ (Finding)        │     │ Amazon EventBridge│     │                                                      │
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
- Amazon GuardDuty enabled in your account (the stack enables a detector)

## Deployment

```bash
cd guardduty-file-modification-sfn-response-cdk/cdk
npm install
npx cdk deploy
```

## Testing

### Simulate a GuardDuty finding (using sample findings)

```bash
# Generate sample findings to test the pipeline
DETECTOR_ID=$(aws cloudformation describe-stacks \
  --stack-name GuarddutyFileModificationSfnResponseStack \
  --query 'Stacks[0].Outputs[?OutputKey==`DetectorId`].OutputValue' \
  --output text)

aws guardduty create-sample-findings \
  --detector-id $DETECTOR_ID \
  --finding-types "UnauthorizedAccess:EC2/SSHBruteForce"
```

### Verify AWS Step Functions execution

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

### Subscribe to incident alerts

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

## Cleanup

> **Warning:** This will delete the Amazon GuardDuty detector. If you have other GuardDuty configurations, remove the detector resource from the stack before deploying.

```bash
cd guardduty-file-modification-sfn-response-cdk/cdk
npx cdk destroy
```

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
