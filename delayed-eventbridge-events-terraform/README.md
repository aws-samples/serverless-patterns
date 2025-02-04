# Delayed Amazon EventBridge events with Amazon EventBridge Scheduler

This pattern listens for EventBridge events, processes them and creates schedules for every user. 24 hours after user has been created a schedule is run that publishes events directly into EventBridge. The pattern is deployed using Terraform.

Learn more about this pattern at Serverless Land Patterns: https://serverlessland.com/patterns/delayed-eventbridge-events-terraform.

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
    cd delayed-eventbridge-events-terraform
    ```
1. From the command line, initialize Terraform:
    ```
    terraform init
    ```
1. From the commend line, apply the configuration in the main.tf file and follow the prompts:
    ```
    terraform apply
    ```

## How it works

We assume we have a business requirement to email a customer 24 hours after they have signed up.

1. `UserCreated` event is triggered. In this example we assume a `UserCreated` event is triggered into our event bus.
2. EventBridge Rule setup to listen to the `UserCreated` event.
3. Lambda function listens to `UserCreated` event and creates an Amazon EventBridge Schedule for 24 hours in the future (2 mins for development mode).
4. 24 hours pass, and schedule is triggered and raises `UserCreated24HoursAgo` event directly into EventBridge..
5. Consumers listen for event and process it. An example would be email a welcome message to customers or an offer etc.

## Testing

Use the [AWS CLI](https://aws.amazon.com/cli/) to send a test event to EventBridge:

1. Send an event to EventBridge:
    ```bash
    aws events put-events --entries "Source='myapp.users',DetailType='UserCreated',Detail='{\"id\": \"test-customer-id\", \"firstName\": \"FirstName\", \"lastName\": \"LastName\"}',EventBusName='<custom-event-bus-ARN>'"
    ```

2. Check the CloudWatch metrics of `UserCreatedRule` and `UserCreated24HoursAgoRule` EventBridge rule and `SchedulesForUsers24HoursAfterCreation` EventBridge Scheduler Group. Also, check the CloudWatch Logs of Lambda Functions which are targets of corresponding `UserCreatedRule` and `UserCreated24HoursAgoRule` EventBridge rules within CloudWatch Logs Console or via `aws logs start-live-tail --log-group-identifiers <Lambda Function LogGroup ARN>` CLI command.

## Cleanup
 
1. Delete all created resources and follow prompts:
    ```
    terraform destroy
    ```
----
Copyright 2023 Amazon.com, Inc. or its affiliates. All Rights Reserved.

SPDX-License-Identifier: MIT-0