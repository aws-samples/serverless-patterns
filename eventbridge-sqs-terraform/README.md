# Amazon EventBridge to Amazon SQS

This template deploys an SQS queue that is triggered by an EventBridge rule. The SQS queue policy provides the permission for EventBridge to send messages to the SQS queue.

In this example, the EventBridge rule specified in `main.tf` filters the events based upon the criteria in the `aws_cloudwatch_event_rule` block. When matching events are sent to EventBridge that trigger the rule, they are delivered as a JSON event payload (see "Example event payload from EventBridge to SQS" in the README) to the SQS queue.

Learn more about this pattern at Serverless Land Patterns: https://serverlessland.com/patterns/eventbridge-sqs.

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
    cd eventbridge-sqs-terraform
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

## Example event payload from EventBridge to SQS
```
{
    "Messages": [
        {
            "Body": "{\"version\":\"0\",\"id\":\"e925d44a-ce79-949c-0cd6-92c826c15fde\",\"detail-type\":\"transaction\",\"source\":\"demo.sqs\",\"account\":\"123456789100\",\"time\":\"2022-03-08T15:18:59Z\",\"region\":\"us-east-1\",\"resources\":[],\"detail\":{\"message\":\"Hello From EventBridge!\"}}", 
            "ReceiptHandle": "AQEB9CHjYQSkKBL+zPmmyMYCQbtUh1NRgoXxE+duCfsf51mSWKu1BqGFLpOYGibvNXil9qGPD/xFQgcVHq9feG1D8E0hlorPQk/qaImSMWjMxQjH9g1cpwgC+a6vey+HkwA42y8v3GxQXjkjncUx6fvGY4PrPvgoUei6/i1jyS8D3esbUFE2JXwX2viIxGQY0Jqpp9VYnDYXqQFi3gjltfNQP3EwbNMFLvR221sGrcrapA4jWu5grQUIApVlWvFeE9nL1thIaMWnMb4aYNtg8nY0lA1IpB/Y0RRHvN+ke56hBDh+QQx3qTl2EQlFREJzZtLqJGD9Eqco79x0YZc+kOTkz4YMA6fdjh85Svu/bNhZ/kOS7CZiJe8VoV6EOSUP09sYCmpWXRulJx7pFLjAZhQQ6NdDAOtpus1Nla03q8t0upI=", 
            "MD5OfBody": "7d822f00ca747wewb66361255c5cf1ee", 
            "MessageId": "af6b7c96-cc77-4c48-9191-01f40900c282"
        }
    ]
}
```

## Testing

Use the [AWS CLI](https://aws.amazon.com/cli/) to send a test event to EventBridge:

1. Send an event to EventBridge:
    ```bash
    aws events put-events --entries file://event.json
    ```
1. Retrieve the message from the SQS queue, using the queue URL from the deployment outputs:
    ```bash
    aws sqs receive-message --queue-url ENTER_YOUR_QUEUE_URL
    ```

## Cleanup
 
1. Change directory to the pattern directory:
    ```
    cd eventbridge-sqs-terraform
    ```
1. Delete all created resources
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
