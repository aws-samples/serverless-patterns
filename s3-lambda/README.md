# AWS Amazon S3 to AWS Lambda - Create a Lambda function that resizes images uploaded to S3

This pattern is a Lambda function asynchronously triggered when an object is uploaded to an S3 bucket. 

The SAM template deploys a Lambda function, an S3 bucket and the IAM resources required to run the application. A Lambda function consumes `ObjectCreated` events from an Amazon S3 bucket. The Lambda code checks the uploaded file is an image and creates a thumbail version of the image in the same bucket.

Learn more about this pattern at Serverless Land Patterns: [https://serverlessland.com/patterns/s3-lambda](https://serverlessland.com/patterns/s3-lambda)

Important: this application uses various AWS services and there are costs associated with these services after the Free Tier usage - please see the [AWS Pricing page](https://aws.amazon.com/pricing/) for details. You are responsible for any AWS costs incurred. No warranty is implied in this example.

## Requirements

* AWS CLI already configured with Administrator permission
* [NodeJS 12.x installed](https://nodejs.org/en/download/)

## Installation Instructions

1. [Create an AWS account](https://portal.aws.amazon.com/gp/aws/developer/registration/index.html) if you do not already have one and login.

1. [Install Git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git) and [install the AWS Serverless Application Model CLI](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-sam-cli-install.html) on your local machine.

1. Create a new directory, navigate to that directory in a terminal and enter:
 ```
 git clone https://github.com/aws-samples/serverless-patterns
 cd s3-lambda
 ```

4. From the command line, run:
```
sam build
sam deploy --guided
```
Choose a stack name, select the desired AWS Region, and allow SAM to create roles with the required permissions. Once you have run guided mode once, you can use `sam deploy` in future to use these defaults.

## How it works

* Use the AWS CLI upload an image to S3
* If the object is a .jpg or a .png, the code creates a thumbnail and saves it to the target bucket. 
* The code assumes that the destination bucket exists and its name is a concatenation of the source bucket name followed by the string -resized

==============================================

## Testing

Run the following S3 CLI  command to upload an image to the S3 bucket. Note, you must edit the {SourceBucketName} placeholder with the name of the S3 Bucket. This is provided in the stack outputs.

```bash
aws s3 cp './events/exampleImage.png'  s3://{SourceBucketName}
```

Run the following command to check that a new version of the image has been created in the destination bucket.

```bash
aws s3 ls s3://{DestinationBucketName}
```

## Cleanup

1. Delete the stack

aws cloudformation delete-stack --stack-name STACK_NAME

1. Confirm the stack has been deleted

aws cloudformation list-stacks --query "StackSummaries[?contains(StackName,'STACK_NAME')].StackStatus


Copyright 2021 Amazon.com, Inc. or its affiliates. All Rights Reserved.

SPDX-License-Identifier: MIT-0
