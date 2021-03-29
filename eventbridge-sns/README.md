# Amazon EventBridge to Amazon SNS

The AWS SAM template deploys an SNS topic that is triggered by an EventBridge rule. The SNS topic policy provides the permission for EventBridge to invoke the SNS topic.

In this example, the EventBridge rule specified in `template.yaml` filters the events based upon the criteria in the `EventPattern` section. When matching events are sent to EventBridge that trigger the rule, they are delivered as a JSON event payload (see Example event payload from EventBridge to SNS in the README) to the SNS topic.

Learn more about this pattern at Serverless Land Patterns: https://serverlessland.com/patterns/eventbridge-sns.

Important: this application uses various AWS services and there are costs associated with these services after the Free Tier usage - please see the [AWS Pricing page](https://aws.amazon.com/pricing/) for details. You are responsible for any AWS costs incurred. No warranty is implied in this example.

## Requirements

* [Create an AWS account](https://portal.aws.amazon.com/gp/aws/developer/registration/index.html) if you do not already have one and log in. The IAM user that you use must have sufficient permissions to make necessary AWS service calls and manage AWS resources.
* [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html) installed and configured
* [Git Installed](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)
* [AWS Serverless Application Model](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-sam-cli-install.html) (AWS SAM) installed

## Deployment Instructions

1. Create a new directory, navigate to that directory in a terminal and clone the GitHub repository:
    ``` 
    git clone https://github.com/aws-samples/serverless-patterns
    ```
1. Change directory to the pattern directory:
    ```
    cd eventbridge-sns
    ```
1. From the command line, use AWS SAM to deploy the AWS resources for the pattern as specified in the template.yml file:
    ```
    sam deploy --guided
    ```
1. During the prompts:
    * Enter a stack name
    * Enter the desired AWS Region
    * Allow SAM CLI to create IAM roles with the required permissions.

    Once you have run `sam deploy -guided` mode once and saved arguments to a configuration file (samconfig.toml), you can use `sam deploy` in future to use these defaults.

1. Note the outputs from the SAM deployment process. These contain the resource names and/or ARNs which are used for testing.

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

## Testing

Use the [AWS CLI](https://aws.amazon.com/cli/) to send a test event to EventBridge:

1. Subscribe your email address to the SNS topic:
    ```bash
    aws sns subscribe --topic-arn ENTER_YOUR_TOPIC_ARN --protocol email-json --notification-endpoint ENTER_YOUR_EMAIL_ADDRESS
    ```
1. Click the confirmation link delivered to your email to verify the endpoint.
1. Send an event to EventBridge:
    ```bash
    aws events put-events --entries file://event.json
    ```
1. The event is delivered to your email address.

## Cleanup
 
1. Delete the stack
    ```bash
    aws cloudformation delete-stack --stack-name STACK_NAME
    ```
1. Confirm the stack has been deleted
    ```bash
    aws cloudformation list-stacks --query "StackSummaries[?contains(StackName,'STACK_NAME')].StackStatus"
    ```
----
Copyright 2021 Amazon.com, Inc. or its affiliates. All Rights Reserved.

SPDX-License-Identifier: MIT-0
