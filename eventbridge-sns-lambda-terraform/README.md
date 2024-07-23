# Integration of Amazon EventBridge with Amazon SNS and Amazon Lambda

This terraform code deploys an EventBridge rule with target as SNS topic which has a Lambda function as subscription and the IAM permissions required to run the application. Whenever the EventBridge rule gets triggered, the Lambda function is invoked by the SNS topic. It also deploys the resources and the IAM permissions required to run the application.

In this example, the EventBridge rule specified in `main.tf` filters the events based upon the criteria in the `aws_cloudwatch_event_rule` block. When matching events are sent to EventBridge that trigger the rule, they are delivered as a JSON event payload (see Example event payload from EventBridge to SNS in the README) to the SNS topic. SNS topic further invokes and delivers the message payload to subscribed  lambda function defined in `aws_lambda_function` block.

Learn more about this pattern at Serverless Land Patterns: https://serverlessland.com/patterns/eventbridge-lambda-sns-terraform.

Important: this application uses various AWS services and there are costs associated with these services after the Free Tier usage - please see the [AWS Pricing page](https://aws.amazon.com/pricing/) for details. You are responsible for any AWS costs incurred. No warranty is implied in this example.

## Requirements

* [Create an AWS account](https://portal.aws.amazon.com/gp/aws/developer/registration/index.html) if you do not already have one and log in. The IAM user that you use must have sufficient permissions to make necessary AWS service calls and manage AWS resources.
* [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html) installed and configured
* [Git Installed](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)
* [Terraform](https://learn.hashicorp.com/tutorials/terraform/install-cli?in=terraform/aws-get-started) installed

## Deployment Instructions

1. Create a new directory, navigate to that directory in a terminal and clone the GitHub repository:
    ``` 
    git clone https://github.com/aws-samples/serverless-patterns
    ```
1. Change directory to the pattern directory:
    ```
    cd eventbridge-sns-lambda-terraform
    ```
1. From the command line, initialize terraform to  to downloads and installs the providers defined in the configuration:
    ```
    terraform init
    ```
1. From the command line, apply the configuration in the main.tf file:
    ```
    terraform apply
    ```
1. During the prompts:
    * Enter yes
1. Note the outputs from the deployment process. These contain the resource names and/or ARNs which are used for testing.

## Example event payload from EventBridge to SNS
```
{
  "Type" : "Notification",
  "MessageId" : "7e758714-7388-5c63-95c5-ddb5001df8a8",
  "TopicArn" : "arn:aws:sns:us-east-1:123456789100:terraform-20220308150620204300000003",
  "Message" : "{\"version\":\"0\",\"id\":\"46e35dca-79f2-8d9c-f4e0-16a5369ec9d4\",\"detail-type\":\"message\",\"source\":\"demo.sns\",\"account\":\"123456789100\",\"time\":\"2022-03-08T15:08:05Z\",\"region\":\"us-east-1\",\"resources\":[],\"detail\":{\"message\":\"Hello From EventBridge!\"}}",
  "Timestamp" : "2022-03-08T15:08:05.888Z",
  "SignatureVersion" : "1",
  "Signature" : "ejxFtHXIp/ujJHrgouzg++Scym+ESe25DGQ61K6SwSsdzq88VBNsyzY/VRA7ErEvDmzX545lu9Ah4zTmoPGZMT19PH3ovksARkrfIwNKqxhRN2ueDYaboYLB63k7WyPEHqH57X/rmDHtakGXksdbAse7MqqVXl2HyrhYZIvUNbwugH0ZtMlfgBOdftcCTVu6WAN+Mq9hSHvOocuGAz4lJ6iKDrs0jrqBDvQvg/k+t9+Q3pQps26dNVbse6sD9iXA92VSy+bACE6Wy325sPvDiQoBtW7C/wgrRutgRmSaJz4clNsFF6TWIGxwpP2fHkD6XUI92AhmVt9ydo37+ISccA==",
  "SigningCertURL" : "https://sns.us-east-1.amazonaws.com/SimpleNotificationService-7ff5318490ec883fbaddaa2a969abfda.pem",
  "UnsubscribeURL" : "https://sns.us-east-1.amazonaws.com/?Action=Unsubscribe&SubscriptionArn=arn:aws:sns:us-east-1:123456789100:terraform-20220308150620204300000003:07d1fa96-6759-472f-a0a7-ccb3e8ba8978"
}
```

## Testing

Use the [AWS CLI](https://aws.amazon.com/cli/) to send a test event to EventBridge:

   
1. Send an event to EventBridge:
    ```bash
    aws events put-events --entries file://event.json
    ```
2. The event is delivered to your lambda function.

## Cleanup
 
1. Change directory to the pattern directory:
    ```
    cd eventbridge-sns-lambda-terraform
    ```
1. Delete the all created resources
    ```bash
    terraform destroy
    ```
1. During the prompts:
    * Enter yes
1. Confirm all created resources has been deleted
    ```bash
    terraform show
    ```
----
Copyright 2022 Amazon.com, Inc. or its affiliates. All Rights Reserved.

SPDX-License-Identifier: MIT-0
