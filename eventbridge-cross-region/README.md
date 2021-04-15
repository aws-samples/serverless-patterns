# Cross-region event bus routing with Amazon EventBridge

This pattern shows how to route events in one Region's event bus to an event bus in another region. The template shows how to configure an event rule to send matching events to target event buses in another region. It includes the necessary IAM permissions to allow the rule to invoke the target in another region.

Learn more about this pattern at Serverless Land Patterns: https://aws.amazon.com/blogs/compute/introducing-cross-region-event-routing-with-amazon-eventbridge/

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
1.  There are two parts to this pattern. The first is the destination event bus where the event should be routed to. You are going to deploy this to three regions.
1. Change directory to the event destination template in the pattern directory:
    ```
    cd eventbridge-cross-region/event-destination
    ```
1.  Run the following command three times, using one of these regions for each deployment: `us-east-1`, `us-west-2`, `eu-west-1`.
    ```
    sam deploy --guided
    ```
1. After deployment the destination template is deployed in three regions and you have three target event buses to receive events. The template also includes a Lambda logger function to log out anything received in the custom event buses in these regions.
1.  Next, deploy the source event bus and rule. This template also deploys an API Gateway webhook to help with testing:
    ```
    cd ../eventbus-source
    sam deploy --guided
    ```
1. During the prompts:
    * Enter a stack name
    * Enter the desired AWS Region - ensure that your source region is not us-east-1, us-west-2 or eu-west-1 since these are used as target regions in this example.
    * Allow SAM CLI to create IAM roles with the required permissions.
1. Note the output from the SAM deployment process. This contain the API endpoint created, which is used for testing.

## Testing

Using curl or [Postman](https://postman.com), invoke the API Gateway endpoint, using a *region* query parameter to determine where the event should be routed. For example:

* https://yourendpoint.execute-api.yourregion.amazonaws.com/Prod?region=us-east-1 - routes the event to us-east-1 (N Virginia, US).
* https://yourendpoint.execute-api.yourregion.amazonaws.com/Prod?region=us-west-2 - routes the event to us-west-2 (Oregon, US).
* https://yourendpoint.execute-api.yourregion.amazonaws.com/Prod?region=eu-west-1 - routes the event to eu-west-1 (Ireland).

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
