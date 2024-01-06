# Remove completed Amazon EventBridge Schedules and sent notification using Amazon SNS 

This pattern will create an Amazon EventBridge Scheduler and will run every five minutes and will use AWS Lambda  to identify expired and completed Amazon Evenbridge Scheduler tasks that are expired 7 days or more and will send an SNS notification once the activity is completed. The pattern is deployed using the AWS Cloud Development Kit (AWS CDK) for Python. 

Important: this application uses various AWS services and there are costs associated with these services after the Free Tier usage - please see the [AWS Pricing page](https://aws.amazon.com/pricing/) for details. You are responsible for any AWS costs incurred. No warranty is implied in this example.

## Requirements

* [Create an AWS account](https://portal.aws.amazon.com/gp/aws/developer/registration/index.html) if you do not already have one
  and log in. The IAM user that you use must have sufficient permissions to make necessary AWS service calls and manage AWS
  resources.
* [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html) installed and configured
* [Git Installed](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)
* [AWS CDK Toolkit](https://docs.aws.amazon.com/cdk/latest/guide/cli.html) installed and configured
* [Python 3.9+](https://www.python.org/downloads/) installed

## Deployment Instructions

1. Create a new directory, navigate to that directory in a terminal and clone the GitHub repository:
    ``` 
    git clone https://github.com/aws-samples/serverless-patterns
    ```
2. Change directory to the pattern directory:
    ```
    cd eventbridge-schedule-remove-one-time-schedules-cdk-python
    ```
3. From the command line, bootstrap the CDK if you haven't already done so. 
    ```
    cdk bootstrap 
    ```
4. Install the Python required dependencies:
    ```
    pip install -r requirements.txt
    ```
5. Deploy the CDK stack to your default AWS account and region. 
    ```
    cdk deploy
    ```
6. Add your email as subscription to SNS after replacing "YOURSNSTOPICARN" and "YOUREMAIL" in the command below
    ```
    aws sns subscribe --topic-arn YOURSNSTOPICARN --protocol email --notification-endpoint YOUREMAIL
    ```
## How it works

An Amazon EventBridge Scheduler job runs every five minutes and will use AWS lambda to identify and delete one time Amazon EventBridge Scheduler jobs expired more than 7 days.Scheduler job also sends a SNS notifications to confirm the activity is completed.
Along with a schedule and topic, the CDK stack creates an IAM role and policy for Amazon EventBridge Scheduler to assume and send messages. 

## Testing
After the stack has been deployed, you can verify Amazon EventBridge is successfully publishing to the topic by viewing the topics "NumberOfMessagesPublished" metric in CloudWatch and verifying positive data points. 

You can also add a subscription to the SNS topic such as an email address or phone number to verify messages are being published successfully.

## Cleanup
 
1. Delete the stack
    ```bash
    cdk destroy
    ```
----
Copyright 2023 Amazon.com, Inc. or its affiliates. All Rights Reserved.

SPDX-License-Identifier: MIT-0