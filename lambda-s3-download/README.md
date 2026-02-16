# Lambda S3 Download

This pattern deploys a Lambda function that downloads a file from a URL and uploads it to an S3 bucket using multipart upload. It streams the file in configurable chunks through `/tmp`, making it capable of handling files larger than Lambda's memory and storage limits.

Important: this application uses various AWS services and there are costs associated with these services after the Free Tier usage - please see the [AWS Pricing page](https://aws.amazon.com/pricing/) for details. You are responsible for any AWS costs incurred. No warranty is implied in this example.

## Requirements

* [Create an AWS account](https://portal.aws.amazon.com/gp/aws/developer/registration/index.html) if you do not already have one and log in. The IAM user that you use must have sufficient permissions to make necessary AWS service calls and manage AWS resources.
* [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html) installed and configured
* [Git Installed](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)
* [AWS Serverless Application Model](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-sam-cli-install.html) (AWS SAM) installed

## Deployment Instructions

1. Create a new directory, navigate to that directory in a terminal and clone the GitHub repository:
    ```
    git clone https://github.com/aws-samples/serverless-patterns
    ```
1. Change directory to the pattern directory:
    ```
    cd serverless-patterns/lambda-s3-download
    ```
1. Build the application:
    ```
    sam build
    ```
1. Deploy the application:
    ```
    sam deploy --guided
    ```
1. During the prompts:
    * Enter a stack name
    * Enter the desired AWS Region
    * Enter the target S3 bucket name (the bucket must already exist)
    * Allow SAM CLI to create IAM roles with the required permissions

    Once you have run `sam deploy --guided` mode once and saved arguments to a configuration file (samconfig.toml), you can use `sam deploy` in future to use these defaults.

1. Note the outputs from the SAM deployment process. These contain the resource names and/or ARNs which are used for testing.

## How it works

The Lambda function:

1. Receives a download URL and filename via the event payload
2. Initiates an S3 multipart upload with SHA256 checksums
3. Streams the file from the URL in chunks (default 128 MB), writing each chunk to `/tmp` and uploading it as a multipart part
4. Cleans up each chunk from `/tmp` after uploading to stay within the 10 GB ephemeral storage limit
5. Completes the multipart upload and returns the S3 object checksum
6. If any step fails, aborts the multipart upload to avoid orphaned parts

The function is configured with a 15-minute timeout, 1 GB memory, and 10 GB ephemeral storage.

## Testing

Invoke the Lambda function with a test event:

```bash
aws lambda invoke \
  --function-name FUNCTION_NAME \
  --cli-binary-format raw-in-base64-out \
  --payload '{
    "download_url": "https://example.com/file.zip",
    "download_filename": "file.zip"
  }' \
  response.json
```

Optional event parameters:

| Parameter | Description | Default |
|---|---|---|
| `target_bucket` | S3 bucket name (overrides the deployed parameter) | Value from template parameter |
| `target_bucket_region` | S3 bucket region | Lambda's region |
| `chunk_size_mb` | Size of each download chunk in MB (clamped between 5 and 5120) | 128 |

## Known Limitations

- The Lambda function has a 15-minute maximum timeout. If the download and upload combined take longer than that, the function will be killed mid-stream and the multipart upload will be left incomplete. Consider setting an [S3 lifecycle rule](https://docs.aws.amazon.com/AmazonS3/latest/userguide/mpu-abort-incomplete-mpu-lifecycle-config.html) on the target bucket to auto-clean incomplete multipart uploads.
- The `download_filename` should be a flat filename (e.g. `file.zip`). If it contains slashes (e.g. `path/to/file.zip`), the temporary file path in `/tmp` will include subdirectories that may not exist, causing a write failure.

## Cleanup

1. Delete the stack
    ```bash
    aws cloudformation delete-stack --stack-name STACK_NAME
    ```
1. Confirm the stack has been deleted
    ```bash
    aws cloudformation list-stacks --query "StackSummaries[?contains(StackName,'STACK_NAME')].StackStatus"
    ```
----
Copyright 2025 Amazon.com, Inc. or its affiliates. All Rights Reserved.

SPDX-License-Identifier: MIT-0
