SNS SQS LAMBDA

This project contains source code and supporting files for a serverless application that you can deploy with the AWS Cloudformation. It includes the following files and folders.

The project creates a SNS Topic and Subscribes a SQS Queue to it. The Subscribed SQS Queue is polled by Lambda Event Source Mapping and invokes the Lambda function with the messages present in the queue. 

Requirements

Create an AWS account if you do not already have one and log in. The IAM user that you use must have sufficient permissions to make necessary AWS service calls and manage AWS resources.

AWS CLI installed and configured

Git Installed

Deployment Instructions
Create a new directory, navigate to that directory in a terminal and clone the GitHub repository:

git clone https://github.com/aws-samples/serverless-patterns
Change directory to the pattern directory:

cd sns-sqs-lambda

From the command line, use AWS CLI  to deploy the AWS resources for the pattern as specified in the main.tf file:

aws cloudformation create-stack --stack-name myteststack --template-body file://SNS_SQS_Lambda.yaml
