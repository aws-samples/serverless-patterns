# Amazon EventBridge to Amazon SNS

This pattern creates an EventBridge rule and an SNS topic. The SNS topic is invoked by the EventBridge rule. 

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

## Example event payload from EventBridge to SNS
```
{
  "Type" : "Notification",
  "MessageId" : "12345678-bf85-59ce-8914-12345678012",
  "TopicArn" : "arn:aws:sns:us-east-1:12345678012:patterns-eb-sns-MySnsTopic-12345678012",
  "Message" : "{\"version\":\"0\",\"id\":\"12345678-3eb5-3993-7eee-12345678012\",\"detail-type\":\"transaction\",\"source\":\"demo.cli\",\"account\":\"12345678012\",\"time\":\"2021-02-10T16:19:39Z\",\"region\":\"us-east-1\",\"resources\":[],\"detail\":{\"msg\":\"test\"}}",
  "Timestamp" : "2021-02-10T16:19:39.679Z",
  "SignatureVersion" : "1",
  "Signature" : "gdXXii12345678012iY+jXXY5FRSSa12345678012A1ZxqsC812345678012uP6tssVCNYQ712345678012v+5212345678012gqLwpyzUL12345678012EwTLhv3KJfRa12345678012ilxkYnU12345678012Fw60z12345678012hZonx12345678012/yd7nC12345678012x5Yy23sisMCULq/oqejE12345678012EdtAYnXzWeF9fBE12345678012eHnUYbUlX/jZqK/Vc12345678012UPGLDiWKOS12345678012==",
  "SigningCertURL" : "https://sns.us-east-1.amazonaws.com/SimpleNotificationService-12345678012cd9412345678012.pem",
  "UnsubscribeURL" : "https://sns.us-east-1.amazonaws.com/?Action=Unsubscribe&SubscriptionArn=arn:aws:sns:us-east-1:12345678012:patterns-eb-sns-MySnsTopic-12345678012:12345678-1124-447a-8c2a-12345678012"
}


```

## How it works

The AWS SAM template deploys the resources and the IAM permissions required to run the application.

The EventBridge rule specified in `template.yaml` filters the events based upon the criteria in the `EventPattern` section. When matching events are sent to EventBridge that trigger the rule, they are delivered as a JSON event payload (see above) to the SNS topic.

## Testing

Use the [AWS CLI](https://aws.amazon.com/cli/) to send a test event to EventBridge:

1. Subscribe your email address to the SNS topic:

```bash
aws sns subscribe --topic-arn ENTER_YOUR_TOPIC_ARN --protocol email-json --notification-endpoint ENTER_YOUR_EMAIL_ADDRESS
```

2. Click the confirmation link delivered to your email to verify the endpoint.

3. Send an event to EventBridge:

```bash
aws events put-events --entries file://event.json
```

4. The event is delivered to your email address.

----
Copyright 2021 Amazon.com, Inc. or its affiliates. All Rights Reserved.

SPDX-License-Identifier: MIT-0
