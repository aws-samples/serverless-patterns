# Amazon EventBridge Schedule to Amazon SQS


This pattern will create an EventBridge schedule to send a message to an Amazon SQS queue every 5 minutes. The pattern is deployed using the AWS Serverless Application Model (SAM).

Important: this application uses various AWS services and there are costs associated with these services after the Free Tier usage - please see the [AWS Pricing page](https://aws.amazon.com/pricing/) for details. You are responsible for any AWS costs incurred. No warranty is implied in this example.

## Requirements

* [Create an AWS account](https://portal.aws.amazon.com/gp/aws/developer/registration/index.html) if you do not already have one
  and log in. The IAM user that you use must have sufficient permissions to make necessary AWS service calls and manage AWS
  resources.
* [Git Installed](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)
* [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html) installed and configured
* [AWS Serverless Application Model](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-sam-cli-install.html) (AWS SAM) installed

## Deployment Instructions

1. Create a new directory, navigate to that directory in a terminal and clone the GitHub repository:
    ``` 
    git clone https://github.com/aws-samples/serverless-patterns
    ```
1. Change directory to the pattern directory:
    ```
    cd eventbridge-schedule-to-sqs-sam
    ```
1. From the command line, build the application along with its dependencies:
    ```
    sam build
    ```
1. From the command line, deploy the AWS resources using SAM and follow the prompts:
    ```
    sam deploy --guided 
    ```

## How it works

An EventBridge Schedule is created to send a message to an Amazon SQS queue every 5 minutes. Along with a schedule and topic, the SAM stack creates an IAM role and policy for EventBridge scheduler to assume and send messages to the SQS queue.

## Testing

After the stack is successfully deployed, you can confirm that EventBridge is publishing messages to SQS by checking the queues "ApproximateNumberOfMessagesVisible" metric in CloudWatch or within the SQS web console. 

## Cleanup
 
1. Change directory to the pattern directory:
    ```
    cd eventbridge-schedule-to-sqs-sam
    ```
1. Delete all created resources and follow prompts:
    ```
    sam delete
    ```
----
Copyright 2023 Amazon.com, Inc. or its affiliates. All Rights Reserved.

SPDX-License-Identifier: MIT-0