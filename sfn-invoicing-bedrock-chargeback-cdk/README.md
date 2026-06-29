# Multi-BU Invoice Reconciliation with AWS Step Functions, AWS Invoicing APIs, Amazon Bedrock, and Amazon DynamoDB

This pattern deploys an AWS Step Functions state machine that uses a Map state to iterate over AWS Invoice Units (business units), fetches invoice summaries for each unit via AWS Invoicing APIs, runs Amazon Bedrock analysis for chargeback allocation, and stores results in an Amazon DynamoDB ledger.

Learn more about this pattern at Serverless Land Patterns: https://serverlessland.com/patterns/sfn-invoicing-bedrock-chargeback-cdk

Important: this application uses various AWS services and there are costs associated with these services after the Free Tier usage - please see the [AWS Pricing page](https://aws.amazon.com/pricing/) for details. You are responsible for any AWS costs incurred. No warranty is implied in this example.

## Requirements

* [Create an AWS account](https://portal.aws.amazon.com/gp/aws/developer/registration/index.html) if you do not already have one and log in. The IAM user that you use must have sufficient permissions to make necessary AWS service calls and manage AWS resources.
* [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html) installed and configured
* [Git Installed](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)
* [Node.js 20+](https://nodejs.org/en/download/) installed
* [AWS CDK v2](https://docs.aws.amazon.com/cdk/v2/guide/getting-started.html) installed and bootstrapped (`cdk bootstrap`)
* [Amazon Bedrock model access](https://docs.aws.amazon.com/bedrock/latest/userguide/model-access.html) enabled for Anthropic Claude Sonnet in your target region
* At least one [AWS Invoice Unit](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/manage-invoice-units.html) configured in your account

## Architecture

```
┌────────────────────────────────────────────────────────────────────────────┐
│                        AWS Step Functions                                    │
│                                                                            │
│  ┌─────────────────┐    ┌──────────────────────────────────────────────┐  │
│  │  ListUnitsTask   │───▶│  Map State (parallel per Invoice Unit)        │  │
│  │  (AWS Lambda)    │    │                                              │  │
│  │  Invoicing API:  │    │  ┌─────────────────┐  ┌──────────────────┐  │  │
│  │  ListInvoiceUnits│    │  │ FetchInvoicesTask│─▶│  AnalysisTask     │  │  │
│  └─────────────────┘    │  │ (AWS Lambda)     │  │  (AWS Lambda)     │  │  │
│                          │  │ Invoicing API:   │  │  Bedrock Converse │  │  │
│                          │  │ ListInvoice      │  │  + DynamoDB Write │  │  │
│                          │  │ Summaries        │  │                   │  │  │
│                          │  └─────────────────┘  └──────────────────┘  │  │
│                          └──────────────────────────────────────────────┘  │
└────────────────────────────────────────────────────────────────────────────┘
                                                          │
                                                          ▼
                                               ┌──────────────────┐
                                               │ Amazon DynamoDB   │
                                               │ Chargeback Ledger │
                                               └──────────────────┘
```

## How it works

1. **ListUnitsTask** — An AWS Lambda function calls the AWS Invoicing `ListInvoiceUnits` API with pagination to discover all business units in the account.

2. **Map State** — AWS Step Functions iterates over each Invoice Unit in parallel (max concurrency 5), processing them independently.

3. **FetchInvoicesTask** — For each unit, an AWS Lambda function calls `ListInvoiceSummaries` filtered by that unit, retrieving the last 90 days of invoice data.

4. **AnalysisTask** — An AWS Lambda function sends the invoice data to Amazon Bedrock (Claude Sonnet) for FinOps analysis: total spend calculation, month-over-month trend detection, chargeback allocation recommendations, and cost optimization opportunities. Results are written to Amazon DynamoDB.

5. **Amazon DynamoDB Ledger** — Stores chargeback allocations per business unit per period, creating an auditable financial record.

## Deployment Instructions

1. Clone the repository:
    ```bash
    git clone https://github.com/aws-samples/serverless-patterns
    cd serverless-patterns/sfn-invoicing-bedrock-chargeback-cdk/cdk
    ```

2. Install dependencies:
    ```bash
    npm install
    ```

3. Deploy the stack:
    ```bash
    cdk deploy
    ```

4. (Optional) Use a different model:
    ```bash
    cdk deploy --context modelId=us.anthropic.claude-sonnet-4-20250514-v1:0
    ```

## Testing

1. Start a Step Functions execution:
    ```bash
    aws stepfunctions start-execution \
      --state-machine-arn <StateMachineArn from stack outputs> \
      --input '{}'
    ```

2. Monitor the execution:
    ```bash
    aws stepfunctions describe-execution \
      --execution-arn <execution ARN from above>
    ```

3. Once complete (status: SUCCEEDED), check the Amazon DynamoDB chargeback ledger:
    ```bash
    aws dynamodb scan \
      --table-name <ChargebackTableName from stack outputs>
    ```

4. Expected result: One item per Invoice Unit with fields including `unitName`, `invoiceCount`, `analysis` (JSON with totalSpend, trend, chargebackAllocation, optimizations), and `analyzedAt` timestamp.

## Cleanup

```bash
cdk destroy
```

> **Warning:** This deletes the Amazon DynamoDB table and all chargeback history. The table uses `RemovalPolicy.DESTROY` for cleanup convenience. In production, use `RETAIN` or enable point-in-time recovery.

----
Copyright 2026 Amazon.com, Inc. or its affiliates. All Rights Reserved.

SPDX-License-Identifier: MIT-0
