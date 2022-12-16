# S3 upload pre-signed URL

In web and mobile applications, it's common to provide the ability to upload data (documents, images, ...). It can be challenging to upload files to a web server and AWS generally recommends to upload files directly to Amazon S3. If you want to give your users this ability, but you don't want them to have AWS security credentials or permissions, you can use [pre-signed URLs](https://docs.aws.amazon.com/AmazonS3/latest/userguide/PresignedUrlUploadObject.html).

This pattern provides the CDK code to deploy a REST API that will expose a Lambda function in charge of generating the pre-signed URL.

Important: this application uses various AWS services and there are costs associated with these services after the Free Tier usage - please see the [AWS Pricing page](https://aws.amazon.com/pricing/) for details. You are responsible for any AWS costs incurred. No warranty is implied in this example.

## Requirements

* [Create an AWS account](https://portal.aws.amazon.com/gp/aws/developer/registration/index.html) if you do not already have one and log in. The IAM user that you use must have sufficient permissions to make necessary AWS service calls and manage AWS resources.
* [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html) installed and configured
* [Git Installed](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)
* [AWS CDK] (https://docs.aws.amazon.com/cdk/api/latest/)

## Deployment Instructions

1. Create a new directory, navigate to that directory in a terminal and clone the GitHub repository:
    ```
    git clone https://github.com/aws-samples/serverless-patterns
    ```
1. Change directory to the pattern directory:
    ```
    cd s3-upload-presignedurl-api-cdk-ts
    ```
1. From the command line, use CDK to deploy the AWS resources for the pattern as specified in eventbridge-scheduled-lambda-cdk.ts file:
    ```
    cdk deploy
    ```
1. During the prompts:
    * Do you wish to deploy these changes (y/n)?
    answer: y <enter>

## How it works

This pattern leverage a high level CDK Construct [`cdk-s3-upload-presignedurl-api`](https://constructs.dev/packages/cdk-s3-upload-presignedurl-api) that will generate the following components:

![architecture](https://raw.githubusercontent.com/jeromevdl/cdk-s3-upload-presignedurl-api/HEAD/images/architecture.png)

1. The client makes a call to the API, specifying the "contentType" of the file to upload in request parameters (eg. `?contentType=image/png` in the URL)
2. API Gateway handles the request and execute the Lambda function.
3. The Lambda function makes a call to the [`getSignedUrl`](https://docs.aws.amazon.com/AWSJavaScriptSDK/latest/AWS/S3.html) api for a `putObject` operation.
4. The Lambda function returns the generated URL and the key of the object in S3 to API Gateway.
5. The API returns the generated URL and the key of the object in S3 to the client.
6. The client can now use this URL to upload a file, directly to S3.

## Testing
- Create a user in Cognito User Pool (through the console).
- Leverage the [frontend](https://github.com/jeromevdl/cdk-s3-upload-presignedurl-api/tree/main/frontend) example provided in the Construct repository
  - Update the _src/aws-exports.js_ file with the correct values for the `userPoolId`, `userPoolWebClientId`, `region` and `endpoint` (these values are provided in output of the CDK stack).
  - Run `npm install` to install the dependencies
  - Run `npm run start` to start the frontend locally (generally http://localhost:3000)
  - You will have to change your password on the first connection.
  - You can then try to upload files in the UI (open the developer tools / network to observe the API calls).

## Cleanup

1. Delete the stack
    ```bash
    aws cloudformation delete-stack --stack-name STACK_NAME
    ```
1. Confirm the stack has been deleted
    ```bash
    aws cloudformation list-stacks --query "StackSummaries[?contains(StackName,'STACK_NAME')].StackStatus"
    ```
1. or delete the stack using the AWS Cloudformation console
----
Copyright 2021 Amazon.com, Inc. or its affiliates. All Rights Reserved.

SPDX-License-Identifier: MIT-0
