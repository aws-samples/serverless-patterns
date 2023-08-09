# S3 to EventBridge to SNS

Publish events directly from S3 to EventBridge and send notifications to SNS when an object is created. This template creates an S3 bucket that publishes events to Amazon EventBridge. When an object is uploaded to the bucket, the EventBridge is triggered and a SNS notification is sent.

Learn more about this pattern at Serverless Land Patterns:https://serverlessland.com/patterns/s3-eventbridge-sns-sam

Important: this application uses various AWS services and there are costs associated with these services after the Free Tier usage - please see the [AWS Pricing page](https://aws.amazon.com/pricing/) for details. You are responsible for any AWS costs incurred. No warranty is implied in this example.

## Requirements

- [Create an AWS account](https://portal.aws.amazon.com/gp/aws/developer/registration/index.html) if you do not already have one and log in. The IAM user that you use must have sufficient permissions to make necessary AWS service calls and manage AWS resources.
- [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html) installed and configured
- [Git Installed](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)
- [AWS Serverless Application Model](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-sam-cli-install.html) (AWS SAM) installed

## Deployment Instructions

1. Create a new directory, navigate to that directory in a terminal and clone the GitHub repository:
   ```
   git clone https://github.com/aws-samples/serverless-patterns
   ```
1. Change directory to the pattern directory:
   ```
   cd s3-eventbridge-sam
   ```
1. From the command line, use AWS SAM to deploy the AWS resources for the pattern as specified in the template.yml file:
   ```
   sam deploy --guided --capabilities CAPABILITY_NAMED_IAM
   ```
1. You can also use AWS CloudFormation console and paste the template.yml file in the designer and deploy it by passing the below required parameters.

   - Enter a stack name

## How it works

This template creates an S3 bucket that publishes events to Amazon EventBridge, allows you to upload objects to that bucket, and will send you notifications from EventBridge to SNS when an object is created in that bucket.

## Testing

1. Subscribe your email address to the SNS topic:
    ```bash
    aws sns subscribe --topic-arn ENTER_YOUR_TOPIC_ARN --protocol email --notification-endpoint ENTER_YOUR_EMAIL_ADDRESS
    ```
1. Click the confirmation link delivered to your email to verify the endpoint.

1. Upload an object to the S3 bucket created by the deployment. You can also use the below command to upload a file:
    ```bash
    aws s3 cp README.md s3://ENTER_YOUR_S3_BUCKET_NAME
    ```
1. The notification message is delivered to your email address.

## Cleanup

1. Delete all files from the S3 bucket

1. Delete the stack
   ```bash
   sam delete
   ```

---

Copyright 2023 Amazon.com, Inc. or its affiliates. All Rights Reserved.

SPDX-License-Identifier: MIT-0
