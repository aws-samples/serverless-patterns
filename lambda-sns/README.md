# AWS Lambda to Amazon SNS

This pattern creates an SNS topic and a Lambda function. The Lambda function publishes to the SNS topic. 

Learn more about this pattern at Serverless Land Patterns: TBD

Important: this application uses various AWS services and there are costs associated with these services after the Free Tier usage - please see the [AWS Pricing page](https://aws.amazon.com/pricing/) for details. You are responsible for any AWS costs incurred. No warranty is implied in this example.

## Requirements

* AWS CLI already configured with Administrator permission
* [NodeJS 12.x installed](https://nodejs.org/en/download/)

## Installation Instructions

1. [Create an AWS account](https://portal.aws.amazon.com/gp/aws/developer/registration/index.html) if you do not already have one and login.

1. [Install Git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git) and [install the AWS Serverless Application Model CLI](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-sam-cli-install.html) on your local machine.

1. Create a new directory, navigate to that directory in a terminal and enter ```git clone this-repo-name```.

1. Change directory to this pattern.

1. From the command line, run:
```
sam deploy --guided
```
Choose a stack name, select the desired AWS Region, and allow SAM to create roles with the required permissions. Once you have run guided mode once, you can use `sam deploy` in future to use these defaults.

1. Note the outputs from the SAM deployment process. These contain the resource names and ARNs.

## Example payload from SNS

```
{
  "Type" : "Notification",
  "MessageId" : "12345678-2045-5567-8d78-1234567890",
  "TopicArn" : "arn:aws:sns:us-east-1:123456789012:patterns-lambda-to-sns-MySnsTopic-1234567890",
  "Subject" : "New message from publisher",
  "Message" : "Message at Wed Feb 10 2021 13:28:10 GMT+0000 (Coordinated Universal Time)",
  "Timestamp" : "2021-02-10T13:28:11.255Z",
  "SignatureVersion" : "1",
  "Signature" : "ks1BRXk41234567890ZvJWznlw1234567890rjioy/G4Br1234567890ll1JEVF1234567890jjyb/lPxIFg123456789025pbdlD2C1234567890L2L0cq2g1234567890afD5BAkbC1234567890+aHMG1234567890jmiMmhTl1234567890r1L9ENgT1234567890U+ROFyh12345678901WeFD1234567890PqpiR0A43T+6Cz7N1234567890wlzln4m5gAw123456781234567890YN/1234567890/1234567890+f/1234567890==",
  "SigningCertURL" : "https://sns.us-east-1.amazonaws.com/SimpleNotificationService-1234567890636cd94b1234567890.pem",
  "UnsubscribeURL" : "https://sns.us-east-1.amazonaws.com/?Action=Unsubscribe&SubscriptionArn=arn:aws:sns:us-east-1:123456789012:patterns-lambda-to-sns-MySnsTopic-1234567890:1234567890-88ee-4bf8-a788-1234567890"
}

```

## How it works

The AWS SAM template deploys the resources and the IAM permissions required to run the application.

When the Lambda function is invoked, it publishes a messages to the SNS topic.

### Testing

Use the [AWS CLI](https://aws.amazon.com/cli/) to invoke the Lambda function. The function name is in the outputs of the AWS SAM deployment (the key is `TopicPublisherFunction`):

Invoke the Lambda function to publish a message to SNS:

```bash
aws lambda invoke --function-name ENTER_YOUR_FUNCTION_NAME outfile.txt
```

----
Copyright 2021 Amazon.com, Inc. or its affiliates. All Rights Reserved.

SPDX-License-Identifier: MIT-0
