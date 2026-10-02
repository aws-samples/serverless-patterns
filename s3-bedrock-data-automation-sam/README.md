# Extract structured data from documents with Amazon Bedrock Data Automation

This pattern turns files uploaded to Amazon Simple Storage Service (Amazon S3) into structured JSON using Amazon Bedrock Data Automation (BDA) and AWS Lambda, with no machine-learning code. Drop a document into the `input/` prefix of the bucket and Bedrock Data Automation writes the extracted result to the `output/` prefix. A one-page sample invoice, `sample-invoice.pdf`, is included so that you can run the pattern end to end straight after deployment.

Learn more about this pattern at Serverless Land Patterns: https://serverlessland.com/patterns/s3-bedrock-data-automation-sam

Important: this application uses various AWS services and there are costs associated with these services after the Free Tier usage - please see the [AWS Pricing page](https://aws.amazon.com/pricing/) for details. You are responsible for any AWS costs incurred. No warranty is implied in this example.

```
  upload file                ObjectCreated              invoke async
  to input/  --> Amazon S3  ------------->  AWS Lambda  ------------>  Bedrock Data Automation
                    ^                       (start job)                (managed extraction)
                    |                                                          |
                    +---------------- structured JSON to output/ --------------+
```

## Requirements

* [Create an AWS account](https://portal.aws.amazon.com/gp/aws/developer/registration/index.html) if you do not already have one and log in. The IAM user that you use must have sufficient permissions to make necessary AWS service calls and manage AWS resources.
* [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html) installed and configured
* [Git Installed](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)
* [AWS Serverless Application Model](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-sam-cli-install.html) (AWS SAM) installed
* Permissions in the deployment account for Amazon S3, AWS Lambda, Amazon CloudWatch Logs, AWS Identity and Access Management (IAM) and Amazon Bedrock Data Automation
* This pattern uses the US geography cross-Region inference profile `us.data-automation-v1`, which Bedrock Data Automation offers in the source Regions `us-east-1`, `us-east-2` and `us-west-2`, so deploy in one of those three Regions. The template contains an AWS CloudFormation `Rules` assertion that stops the deployment in any other Region. For another geography, change the profile and the IAM policy in `template.yaml` as described in [Cross Region support required for Bedrock Data Automation](https://docs.aws.amazon.com/bedrock/latest/userguide/bda-cris.html)

## Deployment Instructions

1. Create a new directory, navigate to that directory in a terminal and clone the GitHub repository:
    ```
    git clone https://github.com/aws-samples/serverless-patterns
    ```
1. Change directory to the pattern directory:
    ```
    cd serverless-patterns/s3-bedrock-data-automation-sam
    ```
1. From the command line, build the function package (the function pins an exact AWS SDK for Python (Boto3) version, see `src/requirements.txt`) and use AWS SAM to deploy the AWS resources for the pattern as specified in the template.yaml file:
    ```
    sam build
    sam deploy --guided
    ```
1. During the prompts:
    * **Stack Name**: enter a stack name, for example `s3-bedrock-data-automation`
    * **AWS Region**: enter `us-east-1`, `us-east-2` or `us-west-2` (see Requirements)
    * **Parameter DataBucketName**: no default, enter a globally unique Amazon S3 bucket name, for example `bda-demo-<your-account-id>`
    * **Confirm changes before deploy**: default `N`, accept the default to deploy without reviewing the change set
    * **Allow SAM CLI IAM role creation**: default `Y`, accept the default so AWS SAM can create the function execution role
    * **Disable rollback**: default `N`, accept the default
    * **Save arguments to configuration file**: default `Y`, accept the default
    * **SAM configuration file**: default `samconfig.toml`, accept the default
    * **SAM configuration environment**: default `default`, accept the default

    Once you have run `sam deploy --guided` mode once and saved arguments to a configuration file (samconfig.toml), you can use `sam deploy` in future to use these defaults.

1. Note the outputs from the SAM deployment process. These contain the resource names and/or ARNs which are used for testing. This pattern uses `DataBucketName` and `LogGroupName`.

## How it works

* A file uploaded to the `input/` prefix of the Amazon S3 bucket raises an `ObjectCreated` event that triggers the AWS Lambda function.
* The function calls the Bedrock Data Automation runtime `InvokeDataAutomationAsync` API with the input file, an output location, and the Bedrock Data Automation project. It is fire-and-forget, so it only starts the job. The function skips folder markers and empty objects, and logs an error line for any record Bedrock Data Automation rejects.
* Bedrock Data Automation reads the file, runs the managed extraction defined by the project, and writes structured JSON to the `output/` prefix.
* The project (`AWS::Bedrock::DataAutomationProject`) is a native AWS CloudFormation resource, so the whole pipeline is infrastructure as code. The included standard output configuration returns each document as Markdown text (including tables) plus a generative summary.
* Bedrock Data Automation requires a cross-Region inference profile. This pattern uses the US geography profile `us.data-automation-v1`, so a job started in a US source Region can be processed in any of `us-east-1`, `us-east-2`, `us-west-1` or `us-west-2`. The function execution role lists exactly those four profile ARNs, as the [Bedrock Data Automation documentation](https://docs.aws.amazon.com/bedrock/latest/userguide/bda-cris.html) prescribes.

## Testing

1. Set a shell variable to the bucket name from the `DataBucketName` output, then upload the sample invoice that ships with this pattern to the `input/` prefix. The upload is what triggers the pipeline. Replace `BUCKET_NAME` with your bucket name:
    ```bash
    BUCKET=BUCKET_NAME
    aws s3 cp ./sample-invoice.pdf s3://$BUCKET/input/sample-invoice.pdf
    ```
    Output:
    ```
    upload: ./sample-invoice.pdf to s3://BUCKET_NAME/input/sample-invoice.pdf
    ```
1. Wait about a minute, then list the output prefix:
    ```bash
    aws s3 ls s3://$BUCKET/output/ --recursive
    ```
    Output (three objects, with your own job id, timestamps and sizes):
    ```
    2026-10-02 23:02:38          0 output/544dcfa2-fbf6-4018-b72c-52a2b552c121/0/.s3_access_check
    2026-10-02 23:02:51       4510 output/544dcfa2-fbf6-4018-b72c-52a2b552c121/0/standard_output/0/result.json
    2026-10-02 23:02:51        404 output/544dcfa2-fbf6-4018-b72c-52a2b552c121/job_metadata.json
    ```
    The path segment immediately after `output/` is the job id, `544dcfa2-fbf6-4018-b72c-52a2b552c121` in the listing above. Bedrock Data Automation writes the zero-byte `.s3_access_check` object as soon as the job starts, so a listing that shows only that object means the extraction is still running; wait and list again. `job_metadata.json` records the job status and where the job wrote its output.
1. Read the structured result. Replace `JOB_ID` with the job id from step 2:
    ```bash
    aws s3 cp s3://$BUCKET/output/JOB_ID/0/standard_output/0/result.json -
    ```
    The command prints the whole result as one line of JSON, which begins:
    ```
    {"metadata": {"asset_id": "0", "logical_subdocument_id": "0", "semantic_modality": "DOCUMENT", "s3_bucket": "BUCKET_NAME", "s3_key": "input/sample-invoice.pdf", "number_of_pages": 1, "start_page_index": 0, "end_page_index": 0, "file_type": "PDF"}, "document": {"representation": {"markdown": "# Northwind Paper Supply\n\n1200 Harbour Road, Suite 400, Springfield, IL 62704 billing@northwind-paper.example\n\n## Invoice INV-2026-0042\n\n ...
    ```
    The top-level keys are `metadata`, `document` and `pages`. The extracted document text is in `document.representation.markdown`, where the invoice line items come back as a Markdown table:
    ```
    | Item                   | Description                            | Qty   | Unit price   | Amount   |
    |------------------------|----------------------------------------|-------|--------------|----------|
    | NW-100                 | A4 premium copy paper, 500 sheets      | 40    | 7.50         | 300.00   |
    | NW-214                 | Recycled kraft envelopes, box of 250   | 12    | 14.25        | 171.00   |
    | NW-330                 | Laser labels, 30 per sheet, 100 sheets | 6     | 22.00        | 132.00   |
    | NW-451                 | Hardcover notebooks, pack of 5         | 15    | 18.60        | 279.00   |
    ```
    The generative summary is in `document.summary`. It is model generated, so the wording varies between runs, but for the sample invoice it reads along these lines:
    ```
    This document is an invoice from Northwind Paper Supply to Lakeside Design Studio. The invoice number is INV-2026-0042, dated March 14, 2026, with a due date of April 13, 2026. The invoice includes items such as A4 premium copy paper, recycled kraft envelopes, laser labels, and hardcover notebooks. The subtotal is $882.00, with a sales tax of 5.5% amounting to $48.51, making the total due $930.51.
    ```
1. The pattern is not limited to the sample file. Bedrock Data Automation processes PDF, TIFF, JPEG, PNG and DOCX documents asynchronously, as listed in [Prerequisites for using Bedrock Data Automation](https://docs.aws.amazon.com/bedrock/latest/userguide/bda-limits.html). Upload any of those to the `input/` prefix to start another job.

## Customizing what is extracted

Edit the `BDAProject` resource in `template.yaml`:

* The project already processes image, video and audio files with the Bedrock Data Automation service defaults. Add `Image`, `Video` or `Audio` blocks to `StandardOutputConfiguration` to control the standard output for those modalities.
* Attach a `CustomOutputConfiguration` (a blueprint) to extract a specific set of fields (for example invoice number, total and line items) as typed JSON.

## Troubleshooting

If no job starts, or `output/` stays empty, the function log group holds the reason. The function logs one line per record: a `Started BDA job ...` line, a `Skipping ...` line for a folder marker or an empty object, or an `ERROR starting BDA job ...` line with the object key and the Bedrock Data Automation error code. Use the `LogGroupName` output from the deployment:

```
aws logs tail LOG_GROUP_NAME --since 10m
```

A record that fails makes the function raise, so AWS Lambda runs the invocation two more times by default before discarding the event (see [How Lambda handles errors and retries with asynchronous invocation](https://docs.aws.amazon.com/lambda/latest/dg/invocation-async-error-handling.html)), and the failure also shows in the function `Errors` metric in Amazon CloudWatch. The most common cause is an unsupported file format (see [Prerequisites for using Bedrock Data Automation](https://docs.aws.amazon.com/bedrock/latest/userguide/bda-limits.html)).

If you deploy in a Region the inference profile does not cover, the stack does not get that far: the `Rules` assertion in the template fails the stack operation with `Parameter validation failed: assertion error: This pattern uses the US geography Amazon Bedrock Data Automation inference profile us.data-automation-v1, which is offered in the source Regions us-east-1, us-east-2 and us-west-2.` and no resources are created.

## Cleanup

1. Empty the Amazon S3 bucket (the bucket must be empty before CloudFormation can delete it). Replace `BUCKET_NAME` with the `DataBucketName` output:
    ```bash
    BUCKET=BUCKET_NAME
    aws s3 rm s3://$BUCKET --recursive
    ```
1. Delete the stack
    ```bash
    sam delete --stack-name STACK_NAME
    ```
1. Confirm the stack has been deleted
    ```bash
    aws cloudformation list-stacks --query "StackSummaries[?contains(StackName,'STACK_NAME')].StackStatus"
    ```

----
Copyright 2026 Amazon.com, Inc. or its affiliates. All Rights Reserved.

SPDX-License-Identifier: MIT-0
