# Extract structured data from documents with Amazon Bedrock Data Automation

This pattern turns files uploaded to Amazon S3 into structured JSON using Amazon Bedrock Data Automation (BDA) and AWS Lambda, with no machine-learning code. Drop a document (or image, video, or audio file) into the `input/` prefix and BDA writes the extracted result to the `output/` prefix.

Learn more about this pattern at Serverless Land Patterns: https://serverlessland.com/patterns/s3-bedrock-data-automation-sam

Important: this application uses various AWS services and there are costs associated with these services after the Free Tier usage - please see the [AWS Pricing page](https://aws.amazon.com/pricing/) for details. You are responsible for any AWS costs incurred. No warranty is implied in this example.

## How it works

```
  upload file                ObjectCreated              invoke async
  to input/  --> Amazon S3  ------------->  AWS Lambda  ------------>  Bedrock Data Automation
                    ^                       (start job)                (managed extraction)
                    |                                                          |
                    +---------------- structured JSON to output/ -------------+
```

- A file uploaded to the `input/` prefix raises an S3 `ObjectCreated` event that triggers the Lambda function.
- The function calls the BDA runtime `InvokeDataAutomationAsync` API with the input file, an output location, and the Bedrock Data Automation project. It is fire-and-forget - it only starts the job.
- Bedrock Data Automation reads the file, runs the managed extraction defined by the project, and writes structured JSON to the `output/` prefix.
- The project (`AWS::Bedrock::DataAutomationProject`) is a native CloudFormation resource, so the whole pipeline is infrastructure as code. The included standard configuration returns each document as Markdown text (including tables) plus a generative summary.

## Requirements

- An AWS account with permissions for Amazon S3, AWS Lambda, and Amazon Bedrock Data Automation.
- [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html) v2, recent enough to include the `bedrock-data-automation` and `bedrock-data-automation-runtime` commands.
- [AWS SAM CLI](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-sam-cli-install.html).
- A Region where Amazon Bedrock Data Automation is available (for example, `us-east-1`).

## Deployment

```bash
sam build
sam deploy --guided
#   - Stack Name       : s3-bedrock-data-automation
#   - AWS Region       : us-east-1 (or a Region where BDA is available)
#   - DataBucketName   : a globally-unique bucket name, for example my-bda-demo-<account-id>
#   - Allow SAM CLI IAM role creation : Y
```

Note the `DataBucketName` output after deployment.

## Testing

Upload any supported document (PDF, PNG, JPEG, TIFF) to the `input/` prefix. This triggers the pipeline; the structured result appears under `output/` within seconds.

```bash
BUCKET=<the DataBucketName from the outputs>

# 1. Upload a document to the input/ prefix (triggers the pipeline)
aws s3 cp ./my-document.pdf s3://$BUCKET/input/my-document.pdf

# 2. Wait ~20-30 seconds, then list the output
aws s3 ls s3://$BUCKET/output/ --recursive

# 3. Read the structured result (replace <job-id> with the folder name from step 2)
aws s3 cp s3://$BUCKET/output/<job-id>/0/standard_output/0/result.json -
```

The `result.json` contains the extracted document text as Markdown (including tables) and a generative summary under the `document` and `pages` keys.

## Changing what is extracted

Edit the `BDAProject` resource in `template.yaml`:
- Add `Image`, `Video`, or `Audio` blocks to `StandardOutputConfiguration` to process other media types.
- Attach a `CustomOutputConfiguration` (a blueprint) to extract a specific set of fields (for example invoice number, total, and line items) as typed JSON.

Note: the system profile `us.data-automation-v1` is a cross-region (US geo) profile, so BDA may route the job to any US region. The IAM policy region-wildcards the profile ARN for this reason.

## Cleanup

```bash
aws s3 rm s3://$BUCKET --recursive
sam delete
```

----

Author: Manish S

Copyright 2026 Amazon.com, Inc. or its affiliates. All Rights Reserved. SPDX-License-Identifier: MIT-0
