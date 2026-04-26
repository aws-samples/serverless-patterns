# Lambda SnapStart with Amazon Bedrock

This pattern deploys a Python Lambda function with **SnapStart** enabled that invokes Amazon Bedrock (Claude Sonnet) for text generation, using AWS CDK.

Learn more about this pattern at Serverless Land Patterns: https://serverlessland.com/patterns/lambda-snapstart-bedrock-cdk

Important: this application uses various AWS services and there are costs associated with these services after the Free Tier usage - please see the [AWS Pricing page](https://aws.amazon.com/pricing/) for details. You are responsible for any AWS costs incurred. No warranty is implied in this example.

## Requirements

- [Create an AWS account](https://portal.aws.amazon.com/gp/aws/developer/registration/index.html) if you do not already have one and log in. The IAM user that you use must have sufficient permissions to make necessary AWS service calls and manage AWS resources.
- [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html) installed and configured
- [AWS CDK](https://docs.aws.amazon.com/cdk/latest/guide/cli.html) installed
- [Node.js](https://nodejs.org/) 18.x or later
- [Amazon Bedrock model access](https://docs.aws.amazon.com/bedrock/latest/userguide/model-access.html) enabled for Anthropic Claude Sonnet in your AWS account

## How it works

Lambda SnapStart reduces cold start latency by up to 10x by pre-initializing the execution environment and caching a snapshot of the initialized state. When a new execution environment is needed, Lambda restores from the cached snapshot instead of running full initialization.

**Key points:**
- SnapStart is enabled via `snapStart: lambda.SnapStartConf.ON_PUBLISHED_VERSIONS` in CDK
- SnapStart only applies to **published versions**, not `$LATEST` — the pattern creates a version and alias automatically
- Supported runtimes: Java 11/17/21, Python 3.12/3.13, .NET 8
- The Bedrock client is initialized at module level (outside the handler) so it gets captured in the SnapStart snapshot

```
┌──────────────────────┐         ┌──────────────────────┐
│                      │         │                      │
│  Lambda (SnapStart)  │────────▶│   Amazon Bedrock     │
│  Python 3.13         │         │   Claude Sonnet      │
│                      │◀────────│                      │
└──────────────────────┘         └──────────────────────┘
```

## Deployment

1. Install dependencies:
   ```bash
   cd lambda-snapstart-bedrock-cdk
   npm install
   ```

2. Deploy the stack:
   ```bash
   cdk deploy
   ```

## Testing

Invoke the function via the **alias** (SnapStart only applies to published versions):

```bash
aws lambda invoke \
  --function-name snapstart-bedrock-cdk:live \
  --payload '{"prompt": "Explain Lambda SnapStart in one paragraph"}' \
  --cli-binary-format raw-in-base64-out \
  output.json

cat output.json | python3 -m json.tool
```

To compare cold start times, invoke `$LATEST` (no SnapStart) vs the alias (with SnapStart):

```bash
# Without SnapStart ($LATEST)
aws lambda invoke --function-name snapstart-bedrock-cdk \
  --payload '{"prompt": "Hello"}' --cli-binary-format raw-in-base64-out /dev/null

# With SnapStart (alias)
aws lambda invoke --function-name snapstart-bedrock-cdk:live \
  --payload '{"prompt": "Hello"}' --cli-binary-format raw-in-base64-out /dev/null
```

Check the `Init Duration` in CloudWatch Logs — SnapStart-optimized invocations show `Restore Duration` instead, which is significantly lower.

## Cleanup

```bash
cdk destroy
```

---

Copyright 2025 Amazon.com, Inc. or its affiliates. All Rights Reserved.

SPDX-License-Identifier: MIT-0
