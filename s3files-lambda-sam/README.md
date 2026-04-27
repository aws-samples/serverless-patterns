# Mount an Amazon S3 Bucket as a File System on AWS Lambda using Amazon S3 Files

This pattern mounts an Amazon S3 bucket as a file system on an AWS Lambda function using **Amazon S3 Files**, then reads CSV files with **pandas** using standard Python file I/O.

Learn more about this pattern at Serverless Land Patterns: https://serverlessland.com/patterns/s3files-lambda-sam

Important: this application uses various AWS services and there are costs associated with these services after the Free Tier usage - please see the [AWS Pricing page](https://aws.amazon.com/pricing/) for details. You are responsible for any AWS costs incurred. No warranty is implied in this example.

## Requirements

* [Create an AWS account](https://portal.aws.amazon.com/gp/aws/developer/registration/index.html) if you do not already have one and log in. The IAM user that you use must have sufficient permissions to make necessary AWS service calls and manage AWS resources.
* [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html) installed and configured
* [Git Installed](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)
* [AWS Serverless Application Model](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-sam-cli-install.html) (AWS SAM) installed
* [Python 3.13](https://www.python.org/downloads/) installed

## How it works

1. An S3 bucket is linked to an **S3 file system** (Amazon S3 Files), providing full POSIX file system semantics over S3 data.
2. A **mount target** is created in a private subnet, giving the Lambda function NFS access to the file system.
3. The Lambda function is configured with `FileSystemConfigs` pointing to the access point, mounting the S3 bucket at `/mnt/s3data`.
4. When invoked, Lambda reads a CSV file from `/mnt/s3data/input/` using `pandas.read_csv()` — a standard file path, no boto3 required.
5. It returns the row count, column names, and a preview of the first 5 rows as JSON.

## Build Instructions

Build the pandas Lambda layer targeting Linux x86_64 (Lambda's runtime), then remove pyarrow to stay within Lambda's 250MB unzipped layer limit:

```bash
pip install pandas \
  --platform manylinux2014_x86_64 \
  --target layer/python/ \
  --implementation cp \
  --python-version 3.13 \
  --only-binary=:all:

# Remove pyarrow if present (not needed for CSV reads, exceeds layer size limit)
rm -rf layer/python/pyarrow

sam build
```

> The `--platform` flag ensures Linux-compatible wheels are downloaded regardless of your local OS (macOS, Windows, or Linux).

## Deployment Instructions

1. Clone the repository:
    ```bash
    git clone https://github.com/aws-samples/serverless-patterns
    ```

2. Change to the pattern directory:
    ```bash
    cd s3files-lambda-sam
    ```

3. Build (see Build Instructions above).

4. Deploy:
    ```bash
    sam deploy --guided
    ```

5. During the prompts:
    * Enter a stack name
    * Enter the desired AWS Region
    * Accept the default parameter values or adjust VPC CIDRs if needed
    * Allow SAM CLI to create IAM roles with the required permissions

    Once you have run `sam deploy --guided` once and saved arguments to `samconfig.toml`, you can use `sam deploy` for future deployments.

6. Note the outputs — you will need `DataBucketName` and `S3FilesReaderFunctionName` for testing.

## Testing

### Unit tests (no AWS required)

```bash
python3 -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install pytest pandas
pytest src/tests/ -v
```

### Integration test against a deployed stack

#### 1. Upload the sample CSV

```bash
BUCKET=$(aws cloudformation describe-stacks \
  --stack-name <your-stack-name> \
  --query "Stacks[0].Outputs[?OutputKey=='DataBucketName'].OutputValue" \
  --output text)

aws s3 cp src/tests/sample_sales.csv s3://$BUCKET/lambda/input/sample_sales.csv
```

#### 2. Invoke the Lambda function

```bash
FUNCTION=$(aws cloudformation describe-stacks \
  --stack-name <your-stack-name> \
  --query "Stacks[0].Outputs[?OutputKey=='S3FilesReaderFunctionName'].OutputValue" \
  --output text)

aws lambda invoke \
  --function-name $FUNCTION \
  --payload '{"file": "input/sample_sales.csv"}' \
  --cli-binary-format raw-in-base64-out \
  response.json

cat response.json
```

Expected response:

```json
{
  "statusCode": 200,
  "body": {
    "file": "/mnt/s3data/input/sample_sales.csv",
    "rows": 10,
    "columns": ["region", "revenue", "units"],
    "preview": [...]
  }
}
```

#### 3. Check Lambda logs

```bash
sam logs --stack-name <your-stack-name> --tail
```

## Cleanup

1. Delete the stack:
    ```bash
    aws cloudformation delete-stack --stack-name STACK_NAME
    ```

2. Confirm the stack has been deleted:
    ```bash
    aws cloudformation list-stacks --query "StackSummaries[?contains(StackName,'STACK_NAME')].StackStatus"
    ```

----
Copyright 2026 Amazon.com, Inc. or its affiliates. All Rights Reserved.

SPDX-License-Identifier: MIT-0
