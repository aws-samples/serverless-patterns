# Amazon EventBridge to Amazon SQS

The AWS SAM template deploys a global endpoint for Amazon EventBridge with an SQS queue triggered by an EventBridge rule.
For more information about global endpoints for Amazon EventBridge, read more at https://aws.amazon.com/blogs/compute/introducing-global-endpoints-for-amazon-eventbridge/.


Learn more about this pattern at Serverless Land Patterns: https://serverlessland.com/patterns/eventbridge-globalendpoint-sqs.

Necessary: This application uses various AWS services, and there are costs associated with these services after the Free Tier usage - please see the [AWS Pricing page](https://aws.amazon.com/pricing/) for details. You are responsible for any AWS costs incurred. No warranty is implied in this example.

## Requirements

* [Create an AWS account](https://portal.aws.amazon.com/gp/aws/developer/registration/index.html). If you do not already have one, log in. The IAM user that you use must have sufficient permissions to make necessary AWS service calls and manage AWS resources.
* [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html) installed and configured
* [Git Installed](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)
* [AWS Serverless Application Model](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-sam-cli-install.html) (AWS SAM) installed

## Deployment Instructions

1. Create a new directory, navigate to that directory in a terminal and clone the GitHub repository:
    ``` 
    git clone https://github.com/aws-samples/serverless-patterns
    ```
2. Change the directory to the pattern directory:
    ```
    cd eventbridge-globalendpoint-sqs
    ```
3. From the command line, REPEAT this step twice and use AWS SAM to deploy the SQS in TWO different regions:
    ```
    sam deploy --guided --template-file template-sqs.yml
    ```
4. From the command line,  REPEAT this step twice and use AWS SAM to deploy the Event Bridge bus in the same region of the SQS:
    ```
    sam deploy --guided --template-file template-bus.yml
    ```
5. From the command line, use AWS SAM to deploy the Global Endpoint setting up the PrimaryRegion and SecondaryRegion parameters where the bus and sqs are deployed
    ```
    sam deploy --guided --template-file template-eb-globalendpoint.yml --capabilities CAPABILITY_NAMED_IAM
    ```

6. Note the outputs from the SAM deployment process. These contain the resource names and/or ARNs used for testing.

In the end, you should have deployed in two different regions:

* 1 SQS
* 1 Event Bridge Bus
* 1 Global endpoint in the primary region
```

## Testing

Use the [AWS CLI](https://aws.amazon.com/cli/) to send a test event to EventBridge:

1. Send an event to EventBridge:
    ```bash
    aws events put-events --entries file://event.json --endpoint-id <GLOBAL ENDPOINT ID>
    ```

## Cleanup
 
1. Repeat this step for each stack:
    ```bash
    aws cloudformation delete-stack --stack-name STACK_NAME
    ```
1. Confirm the stack has been deleted
    ```bash
    aws cloudformation list-stacks --query "StackSummaries[?contains(StackName,'STACK_NAME')].StackStatus"
    ```
----
Copyright 2022 Amazon.com, Inc. or its affiliates. All Rights Reserved.

SPDX-License-Identifier: MIT-0
