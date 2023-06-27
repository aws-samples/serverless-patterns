# Amazon Eventbridge to Amazon SNS

This CDK template deploys a SNS topic that is triggered by an EventBridge rule. The SNS topic policy provides the permission for EventBridge to invoke the SNS topic.

Learn more about this pattern at Serverless Land Patterns: https://serverlessland.com/patterns/eventbridge-sns-java-cdk.

Important: this application uses various AWS services and there are costs associated with these services after the Free Tier usage - please see the [AWS Pricing page](https://aws.amazon.com/pricing/) for details. You are responsible for any AWS costs incurred. No warranty is implied in this example.

## Requirements

* [Create an AWS account](https://portal.aws.amazon.com/gp/aws/developer/registration/index.html) if you do not already have one and log in. The IAM user that you use must have sufficient permissions to make necessary AWS service calls and manage AWS resources.
* [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html) installed and configured
* [Git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git) installed and configured
* [AWS CDK](https://docs.aws.amazon.com/cdk/latest/guide/cli.html) installed and configured
* [Maven](https://maven.apache.org/download.cgi) installed and configured

## Deployment Instructions

1. Clone the project to your local working directory
    ```
    git clone https://github.com/aws-samples/serverless-patterns
    ```

2. Change the working directory to this pattern's directory
    ```
    cd eventbridge-sns-java-cdk
    ```

1. From the command line, use Maven to build and package the project
    ```
    mvn clean package
    ```
1. Next, configure the AWS CDK.:
    ```
    cdk bootstrap <ACCOUNT-NUMBER>/<REGION>
   ```
   For example:
   ```cdk bootstrap 1111111111/us-east-1```
   Or,
   ```cdk bootstrap --profile test 1111111111/us-east-1```

1. Deploy the stack (Accept prompt):
    ```
    cdk deploy
    ```

## How it works

The CDK stack deploys the resources and the IAM permissions required to run the application.

The EventBridge rule filters the events based upon the defined criteria. When matching events are sent to EventBridge that trigger the rule, they are published to target SNS topic.

## Testing

Use the [AWS CLI](https://aws.amazon.com/cli/) to send a test event to EventBridge:

1. Subscribe your email address to the SNS topic:
    ```
    aws sns subscribe --topic-arn ENTER_YOUR_TOPIC_ARN --protocol email-json --notification-endpoint ENTER_YOUR_EMAIL_ADDRESS
    ```
2. Click the confirmation link(SubscribeURL) delivered to your email to verify the endpoint.

3. Send an event to EventBridge:
    ```
    aws events put-events --entries file://event.json
    ```
4. The event is delivered to your email address.

## Cleanup
 
1. Run the given command to delete the resources that were created. It might take some time for the CloudFormation stack to get deleted.
    ```
    cdk destroy
    ```

----
Copyright 2022 Amazon.com, Inc. or its affiliates. All Rights Reserved.

SPDX-License-Identifier: MIT-0
