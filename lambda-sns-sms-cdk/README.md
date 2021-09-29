# AWS Lambda to Amazon SNS - CDK

The CDK template deploys a Lambda function with IAM permissions configured to publish an SMS message to a US phone number using a 10-digit long code (10DLC). The Lambda function publishes a message to the phone number when invoked. The AWS CDK template deploys the resources and the IAM permissions required to run the application.

Learn more about this pattern at Serverless Land Patterns: https://serverlessland.com/patterns/lambda-sns-sms-cdk.

Important: this application uses various AWS services and there are costs associated with these services after the Free Tier usage - please see the [AWS Pricing page](https://aws.amazon.com/pricing/) for details. You are responsible for any AWS costs incurred. No warranty is implied in this example.

## Requirements

* [Create an AWS account](https://portal.aws.amazon.com/gp/aws/developer/registration/index.html) if you do not already have one and log in. The IAM user that you use must have sufficient permissions to make necessary AWS service calls and manage AWS resources.
* [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html) installed and configured
* [Git Installed](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)
* [AWS Cloud Development Kit](https://docs.aws.amazon.com/cdk/latest/guide/getting_started.html) (AWS CDK) Installed and account bootstrapped
## Deployment Instructions

1. Create a new directory, navigate to that directory in a terminal and clone the GitHub repository:
    ``` 
    git clone https://github.com/aws-samples/serverless-patterns
    ```
2. Change directory to the pattern directory:
    ```
    cd lambda-sns-sms-cdk
    ```
3. Create a virtual environment for python:
    ```
    python3 -m venv .venv
    ```
4. Activate the virtual environment:
    ```
    source .venv/bin/activate
    ```
5. Install python modules:
    ```
    python3 -m pip install -r requirements.txt
    ```
6. From the command line, use CDK to synthesize the CloudFormation template and check for errors:
    ```
    cdk synth
    ```
7. From the command line, use CDK to deploy the stack:
    ```
    cdk deploy --parameters phoneNumber=8088675309 --parameters tenDLC=8088675309
    ```
Note the outputs from the CDK deployment process. This contains the lambda function name used for testing.

## Example payload from SNS

```
{
  "Type" : "Notification",
  "MessageId" : "12345678-2045-5567-8d78-1234567890",
  "Subject" : "New message from publisher",
  "Message" : "Message at Wed Feb 10 2021 13:28:10 GMT+0000 (Coordinated Universal Time)",
  "Timestamp" : "2021-02-10T13:28:11.255Z",
  "SignatureVersion" : "1",
  "Signature" : "ks1BRXk41234567890ZvJWznlw1234567890rjioy/G4Br1234567890ll1JEVF1234567890jjyb/lPxIFg123456789025pbdlD2C1234567890L2L0cq2g1234567890afD5BAkbC1234567890+aHMG1234567890jmiMmhTl1234567890r1L9ENgT1234567890U+ROFyh12345678901WeFD1234567890PqpiR0A43T+6Cz7N1234567890wlzln4m5gAw123456781234567890YN/1234567890/1234567890+f/1234567890==",
  "SigningCertURL" : "https://sns.us-east-1.amazonaws.com/SimpleNotificationService-1234567890636cd94b1234567890.pem",
  "UnsubscribeURL" : "https://sns.us-east-1.amazonaws.com/?Action=Unsubscribe&SubscriptionArn=arn:aws:sns:us-east-1:123456789012:patterns-lambda-to-sns-MySnsTopic-1234567890:1234567890-88ee-4bf8-a788-1234567890"
}

```

### Testing

Use the [AWS CLI](https://aws.amazon.com/cli/) to invoke the Lambda function. The function name is in the outputs of the AWS CDK deployment (the key is `TopicPublisherFunction`):

1. Invoke the Lambda function to publish a message to SNS:

```bash
aws lambda invoke --function-name SMSPublisherFunction response.json
```

## Cleanup
 
1. Delete the stack
    ```bash
    cdk destroy
    ```
1. Confirm the stack has been deleted
    ```bash
    aws cloudformation list-stacks --query "StackSummaries[?contains(StackName,'STACK_NAME')].StackStatus"
    ```
----
Copyright 2021 Amazon.com, Inc. or its affiliates. All Rights Reserved.

SPDX-License-Identifier: MIT-0
