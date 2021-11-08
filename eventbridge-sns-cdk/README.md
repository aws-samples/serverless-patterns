# Amazon Eventbridge to Amazon SNS

This CDK template deploys a SNS topic that is triggered by an EventBridge rule. The SNS topic policy provides the permission for EventBridge to invoke the SNS topic.



Learn more about this pattern at Serverless Land Patterns: https://serverlessland.com/patterns/eventbridge-sns-cdk

Important: this application uses various AWS services and there are costs associated with these services after the Free Tier usage - please see the [AWS Pricing page](https://aws.amazon.com/pricing/) for details. You are responsible for any AWS costs incurred. No warranty is implied in this example.

## Requirements

* [Create an AWS account](https://portal.aws.amazon.com/gp/aws/developer/registration/index.html) if you do not already have one and log in. The IAM user that you use must have sufficient permissions to make necessary AWS service calls and manage AWS resources.
* [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html) installed and configured
* [Git Installed](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)
* [AWS Cloud Development Kit](https://docs.aws.amazon.com/cdk/latest/guide/getting_started.html) (AWS CDK >= 1.124.0) Installed

## Deployment Instructions

1. Create a new directory, navigate to that directory in a terminal and clone the GitHub repository:
    ```bash 
    git clone https://github.com/aws-samples/serverless-patterns
    ```
1. Change directory to the pattern directory:
    ```bash
    cd eventbridge-sns-cdk
    ```
1. Create a virtual environment for python:
    ```bash
    python3 -m venv .venv
    ```
1. Activate the virtual environment:
    ```bash
    source .venv/bin/activate
    ```
1. Install python modules:
    ```bash
    python3 -m pip install -r requirements.txt
    ```
1. From the command line, use CDK to synthesize the CloudFormation template and check for errors:
    ```bash
    cdk synth
    ```
1. From the command line, use CDK to deploy the stack:
    ```bash
    cdk deploy
    ```
1. Note the outputs from the CDK deployment process. These contain the resource names and/or ARNs which are used for testing.

## How it works

The CDK stack deploys the resources and the IAM permissions required to run the application.

The EventBridge Rule specified in app.py which filters the events based upon the criteria in the rule.add_event_pattern method. When matching events are sent to the custom EventBridge Bus that trigger the Rule, they are published to target SNS topic.

## Example event payload from EventBridge to SNS
Note - Account Number and SigningCertURL are masked in the example paylod.
```
{
  "Type" : "Notification",
  "MessageId" : "ecc4f3ed-47eb-5374-b5a4-aa16ec96b0a1",
  "TopicArn" : "arn:aws:sns:us-east-1:<*AccountNumber*>:EventbridgeSnsCdkStack-MySnsTopicCB85459E-1VN8RJK7ZDOSB",
  "Message" : "{\"version\":\"0\",\"id\":\"3a91138a-dc4b-8fff-0325-5e18f7247415\",\"detail-type\":\"message\",\"source\":\"my-application\",\"account\":\"<*AccountNumber*>\",\"time\":\"2021-11-02T21:10:21Z\",\"region\":\"us-east-1\",\"resources\":[],\"detail\":{\"message\":\"Hello from EventBridge to SNS Topic!\"}}",
  "Timestamp" : "2021-11-02T21:10:21.802Z",
  "SignatureVersion" : "1",
  "Signature" : "OQBlVrpA8e4sFu211RkLjn2SPWVv1cThCXfG7YBaFkoulyNM+8SvlApbHLR/t+BtLyzmU8DIh7MOb8zyR4rpBhKCkjEvqNpX1AO+Da294onD+NHGrqjnRMkMyjcDzxe7poTKSEwwYBp16jjDNBBXRZmM6YX5XiL1zY41NrfJiUXro76xJr1nqr7BoxNJ1a3ACzh2cv6lyoGS0oxTgXztevUvUmfvxqtbfiFAapEjxde6IWPT6pellzy6HGfls8z7UI1NndBqfCAo4z8dCAxrczDM4Yozc+KvoquSbttKPcMkApe184teOWp0ZOT5dhO6mOV4hgCPoe9hUipoFq4Acw==",
  "SigningCertURL" : "******",
  "UnsubscribeURL" : "https://sns.us-east-1.amazonaws.com/?Action=Unsubscribe&SubscriptionArn=arn:aws:sns:us-east-1:<AccountNumber>:EventbridgeSnsCdkStack-MySnsTopicCB85459E-1VN8RJK7ZDOSB:175aa034-1d2d-4a83-a0e4-dbd830fce265"
}
```

## Testing

Use the [AWS CLI](https://aws.amazon.com/cli/) to send a test event to EventBridge:

1. Subscribe your email address to the SNS topic:
    ```bash
    aws sns subscribe --topic-arn ENTER_YOUR_TOPIC_ARN --protocol email-json --notification-endpoint ENTER_YOUR_EMAIL_ADDRESS
    ```
1. Click the confirmation link(SubscribeURL) delivered to your email to verify the endpoint.

1. Send an event to EventBridge:
    ```bash
    aws events put-events --entries file://event.json
    ```
1. The event is delivered to your email address.

## Cleanup
 
1. Run the given command to delete the resources that were created. It might take some time for the CloudFormation stack to get deleted.
    ```bash
    cdk destroy
    ```
1. Deactivate the virtual environment:
    ```bash
    deactivate
    ```
----
Copyright 2021 Amazon.com, Inc. or its affiliates. All Rights Reserved.

SPDX-License-Identifier: MIT-0
