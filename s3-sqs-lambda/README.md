# AWS Amazon S3 to SQS to AWS Lambda - Create a Lambda function that resizes images uploaded to S3 using SQS as a notification target

The SAM template deploys a Lambda function, an SQS queue, 2 S3 buckets and the IAM resources required to run the application. An SQS Queue consumes <code>ObjectCreated</code> events from an Amazon S3 bucket if the file has .jpg extension. The SQS triggers a Lambda function. The Lambda code checks the uploaded file is an image and creates a thumbnail version of the image in another bucket.

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
1. Install dependencies
   ```bash
   npm --prefix ./src install ./src
   ```
1. From the command line, use AWS SAM to build and deploy the AWS resources for the pattern as specified in the template.yml file:
    ```bash
    sam build
    sam deploy --guided
    ```
1. During the prompts:
   * Enter a stack name
   * Enter a source bucket name
   * Enter a destination bucket name
   * Enter a queue name
   * Enter the desired AWS Region
   * Allow SAM CLI to create IAM roles with the required permissions.

   Once you have run `sam deploy -guided` mode once and saved arguments to a configuration file (samconfig.toml), you can use `sam deploy` in future to use these defaults.

1. Note the outputs from the SAM deployment process. These contain the resource names and/or ARNs which are used for testing.

## How it works

* Use the AWS CLI or AWS console to upload an image to the source S3 Bucket
* If the object is a .jpg the code creates a thumbnail and saves it to the target bucket.
* The code assumes that the destination bucket exists and its name is a concatenation of the source bucket name followed by the string -resized

==============================================

## Testing

Run the following S3 CLI  command to upload an image to the S3 bucket. Note, you must edit the {SourceBucketName} placeholder with the name of the source S3 Bucket. This is provided in the stack outputs.

```bash
aws s3 cp './events/exampleImage.png'  s3://{SourceBucketName}
```

Run the following command to check that a new version of the image has been created in the destination bucket.

```bash
aws s3 ls s3://{DestinationBucketName}
```

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
Copyright 2021 Amazon.com, Inc. or its affiliates. All Rights Reserved.

SPDX-License-Identifier: MIT-0
