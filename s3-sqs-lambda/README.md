# AWS Amazon S3 to SQS to AWS Lambda - Create a Lambda function that resizes images uploaded to S3 using SQS as a notification target

The SAM template deploys a Lambda function, an SQS queue, 2 S3 buckets and the IAM resources required to run the application. The source bucket sends an <code>ObjectCreated</code> event to the SQS queue for each uploaded .jpg file. The queue triggers the Lambda function, which resizes the image with [sharp](https://sharp.pixelplumbing.com/) and saves it in the destination bucket. Both buckets block public access and use S3-managed encryption, so the resized images stay private.

Learn more about this pattern at Serverless Land Patterns: [https://serverlessland.com/patterns/s3-sqs-lambda](https://serverlessland.com/patterns/s3-sqs-lambda)

Important: this application uses various AWS services and there are costs associated with these services after the Free Tier usage - please see the [AWS Pricing page](https://aws.amazon.com/pricing/) for details. You are responsible for any AWS costs incurred. No warranty is implied in this example.

## Requirements

* [Create an AWS account](https://portal.aws.amazon.com/gp/aws/developer/registration/index.html) if you do not already have one and log in. The IAM user that you use must have sufficient permissions to make necessary AWS service calls and manage AWS resources.
* [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html) installed and configured
* [Git Installed](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)
* [AWS Serverless Application Model](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-sam-cli-install.html) (AWS SAM) installed

## Deployment Instructions

1. Create a new directory, navigate to that directory in a terminal and clone the GitHub repository:
    ```bash
    git clone https://github.com/aws-samples/serverless-patterns
    ```
1. Change directory to the pattern directory:
    ```bash
    cd s3-sqs-lambda
    ```
1. From the command line, use AWS SAM to build and deploy the AWS resources for the pattern as specified in the template.yaml file:
    ```bash
    sam build
    sam deploy --guided
    ```
    `sam build` runs `npm install` in `src` with the settings in `src/.npmrc` (`os=linux`, `cpu=arm64`, `libc=glibc`). This installs the Linux arm64 build of sharp that the function needs, even when you build on macOS or Windows, so you don't need Docker. If you change `Architectures` in template.yaml to `x86_64`, set `cpu=x64` in `src/.npmrc`. You can also build in a Lambda-like container with `sam build --use-container`.

1. During the prompts:
   * Enter a stack name
   * Enter a source bucket name
   * Enter a destination bucket name. It must be a different bucket from the source, otherwise the resized images would trigger the function again. The template refuses to deploy if they're the same.
   * Enter a queue name
   * Enter the desired AWS Region
   * Allow SAM CLI to create IAM roles with the required permissions.

   Once you have run `sam deploy -guided` mode once and saved arguments to a configuration file (samconfig.toml), you can use `sam deploy` in future to use these defaults.

1. Note the outputs from the SAM deployment process. These contain the resource names and/or ARNs which are used for testing.

## How it works

* You upload a .jpg image to the source S3 bucket.
* S3 sends an `ObjectCreated` event to the SQS queue. The Lambda function reads up to 10 messages at a time.
* For each message, the function gets the image, resizes it to fit inside 480 x 480 pixels with sharp, and writes it as a JPEG to the destination bucket with the same key. The function's role can only read objects from the source bucket and write objects to the destination bucket.
* The function reports failed messages with `ReportBatchItemFailures`, so one bad image doesn't make Lambda retry the whole batch.
* The resized image is private. The destination bucket blocks public access and disables ACLs, so the function doesn't set an ACL.

## Testing

1. Upload an image to the source bucket. Replace `{SourceBucketName}` with the name from the stack outputs.

    ```bash
    aws s3 cp ./my-image.jpg s3://{SourceBucketName}/my-image.jpg
    ```

1. After a few seconds, check that the resized image is in the destination bucket:

    ```bash
    aws s3 ls s3://{DestinationBucketName}/
    aws s3 cp s3://{DestinationBucketName}/my-image.jpg ./my-image-resized.jpg
    ```

1. Check that the image is private. A request without credentials returns `403 Forbidden`:

    ```bash
    curl -I https://{DestinationBucketName}.s3.amazonaws.com/my-image.jpg
    ```

If no image appears, check the function's logs:

```bash
sam logs --stack-name STACK_NAME --name ResizerFunction
```

## Cleanup

1. Empty both buckets, then delete the stack
    ```bash
    aws s3 rm s3://{SourceBucketName} --recursive
    aws s3 rm s3://{DestinationBucketName} --recursive
    sam delete --stack-name STACK_NAME
    ```
1. Confirm the stack has been deleted
    ```bash
    aws cloudformation list-stacks --query "StackSummaries[?contains(StackName,'STACK_NAME')].StackStatus"
    ```
----
Copyright 2021 Amazon.com, Inc. or its affiliates. All Rights Reserved.

SPDX-License-Identifier: MIT-0
