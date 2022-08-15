# AWS Amazon S3 to Lambda - Creates a Lambda function which uses Amazon SES to send notifications when an object is uploaded to the S3 bucket.

This Terraform template deployes a AWS Lambda Function and an AWS S3 bucket.

Learn more about this pattern at Serverless Land Patterns: https://serverlessland.com/patterns/s3-lambda

Important: this application uses various AWS services and there are costs associated with these services after the Free Tier usage - please see the AWS Pricing page for details. You are responsible for any AWS costs incurred. No warranty is implied in this example.

## Requirements

- Create an AWS account if you do not already have one and log in. The IAM user that you use must have sufficient permissions to make necessary AWS service calls and manage AWS resources.
- AWS CLI installed and configured
- Git Installed
- Terraform Installed

## Deployment Instructions

1. Create a new directory, navigate to that directory in a terminal and clone the GitHub repository:

`git clone https://github.com/aws-samples/serverless-patterns`

2. Change directory to the pattern directory:

`cd serverless-patterns/s3-lambda-ses-terraform`

3. From the command line, initialize terraform to download and install the providers defined in the configuration:

`terraform init`

4. From the command line, apply the configuration in the main.tf file:

`terraform apply`

5. During the prompts:
 > Enter yes

6. Note the outputs from the deployment process, these contain the resource names and/or ARNs which are used for testing.

## How it works 

This template deploys a AWS Lambda Function and Amazon S3 bucket with the required IAM resources to run the application. The Lambda Function consumes **ObjectCreated** events from an Amazon S3 bucket. Further, Lambda code checks the object size if the uploded file size is <= 25MB then the object will be attached to the email for higher payloads Lambda generates a presigned URL and generates short URL which will be attached to the email.

*** Kindly provide SES verfied email and sender email ID values over the terraform temaplte in-order to send the notifications ***

- Once the terraform stack is succesfully deployed, use the AWS CLI or AWS console to upload an object to the created S3 bucket.
- S3 bucket will trigger the Lambda Function and Lambda code checks the uploaded object and based on the above logic, Lambda sends the notification.
- Customize the email payload section as per your requirements.

## Testing

Run the following S3 CLI command to upload an test file to the S3 bucket. Note, you must edit the  placeholder with the name of the S3 Bucket. This is provided in the stack outputs.

`aws s3 cp './src/example.txt'  s3://{SourceBucketName}`

Wait for few seconds hopefully you should receive an notification over your email :crossed_fingers:

## Cleanup

1. Change directory to the pattern directory:

`cd serverless-patterns/apigw-http-api-lambda-terraform`

2. Delete all created resources

`terraform destroy`

> While destroying no need to provide sender and receiver email values.

3. During the prompts:

> Enter yes

4. Confirm all created resources has been deleted

`terraform show`


Copyright 2022 Amazon.com, Inc. or its affiliates. All Rights Reserved.

SPDX-License-Identifier: MIT-0