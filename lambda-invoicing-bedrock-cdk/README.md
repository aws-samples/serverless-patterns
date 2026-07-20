# Automated AWS Invoice Retrieval and Analysis with Amazon Bedrock

This pattern deploys an AWS Lambda function that automatically retrieves AWS invoices using the new programmatic Invoicing APIs, archives invoice PDFs to Amazon S3, and generates cost analysis summaries using Amazon Bedrock.

Learn more about this pattern at Serverless Land Patterns: https://serverlessland.com/patterns/lambda-invoicing-bedrock-cdk

Important: this application uses various AWS services and there are costs associated with these services after the Free Tier usage - please see the [AWS Pricing page](https://aws.amazon.com/pricing/) for details. You are responsible for any AWS costs incurred. No warranty is implied in this example.

## Requirements

* [Create an AWS account](https://portal.aws.amazon.com/gp/aws/developer/registration/index.html) if you do not already have one and log in. The IAM user that you use must have sufficient permissions to make necessary AWS service calls and manage AWS resources.
* [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html) installed and configured
* [Node.js 20+](https://nodejs.org/en/download/) installed
* [AWS CDK v2](https://docs.aws.amazon.com/cdk/v2/guide/getting_started.html) installed (`npm install -g aws-cdk`)
* [Git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git) installed

## Deployment Instructions

1. Create a new directory, navigate to that directory in a terminal and clone the GitHub repository:
    ```bash
    git clone https://github.com/aws-samples/serverless-patterns
    ```
2. Change directory to the pattern directory:
    ```bash
    cd serverless-patterns/lambda-invoicing-bedrock-cdk
    ```
3. Install dependencies:
    ```bash
    npm install
    ```
4. Bootstrap CDK (if not already done):
    ```bash
    cdk bootstrap
    ```
5. Deploy the stack:
    ```bash
    cdk deploy
    ```

    To use a different Amazon Bedrock model or deploy in a different region, pass the model ID as context:
    ```bash
    cdk deploy --context modelId=eu.anthropic.claude-sonnet-4-6
    ```

## How it works

This pattern uses four AWS services in composition:

1. **Amazon EventBridge** triggers the Lambda function on the 2nd of each month (after invoices become available).
2. **AWS Lambda** orchestrates the workflow: calls the AWS Invoicing API to list invoices and download PDFs.
3. **Amazon S3** stores the invoice PDFs with date-partitioned keys and lifecycle transitions to Infrequent Access after 90 days.
4. **Amazon Bedrock** (Claude Sonnet) analyzes the invoice data and generates an executive summary with spend breakdown, tax analysis, and cost optimization recommendations.

The pattern leverages the new `ListInvoiceSummaries` and `GetInvoicePDF` APIs (launched June 2026) to programmatically access invoices that previously required manual console downloads.

### Architecture

```
Amazon EventBridge (monthly) → AWS Lambda → Invoicing APIs → Amazon S3 (PDF archive)
                                                             → Amazon Bedrock (analysis) → Amazon S3 (summary)
```

## Testing

Invoke the AWS Lambda function manually:

```bash
aws lambda invoke \
  --function-name $(aws cloudformation describe-stacks \
    --stack-name LambdaInvoicingBedrockStack \
    --query 'Stacks[0].Outputs[?OutputKey==`FunctionName`].OutputValue' \
    --output text) \
  --payload '{}' \
  response.json && cat response.json
```

Expected output shows invoices retrieved, PDFs archived, and Bedrock analysis:

```json
{
  "statusCode": 200,
  "body": "{\"message\": \"Processed 1 invoice(s)\", \"period\": \"2026-05\", \"totalInvoices\": 1, \"analysisKey\": \"analysis/2026/05/summary.json\", \"analysis\": \"...\"}"
}
```

Check the Amazon S3 bucket for archived PDFs and analysis:

```bash
aws s3 ls s3://$(aws cloudformation describe-stacks \
  --stack-name LambdaInvoicingBedrockStack \
  --query 'Stacks[0].Outputs[?OutputKey==`InvoiceBucketName`].OutputValue' \
  --output text) --recursive
```

## Cleanup

> **Warning:** Running `cdk destroy` will delete the Amazon S3 bucket and all archived invoice PDFs. Download any needed invoices before destroying.

```bash
cdk destroy
```

----
Copyright 2026 Amazon.com, Inc. or its affiliates. All Rights Reserved.

SPDX-License-Identifier: MIT-0
