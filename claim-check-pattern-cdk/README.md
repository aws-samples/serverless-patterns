# Implementing the claim check pattern using EventBridge Pipes

To reduce the size of the events in your event-driven application, you can temporarily remove attributes. This approach is known as the [claim check pattern](https://www.enterpriseintegrationpatterns.com/patterns/messaging/StoreInLibrary.html).

This pattern demonstrates the claim check pattern using EventBridge Pipes. Attributes that are removed from an event are stored in DynamoDB and retrieved from there when needed. This is done inside Pipes, using enrichment via AWS Lambda.

Learn more about this pattern at Serverless Land Patterns: https://serverlessland.com/patterns/claim-check-pattern-cdk

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
    cd serverless-patterns/claim-check-pattern-cdk/src
    ```
1. Install dependencies:
    ```
    npm install
    ```
1. From the command line, configure AWS CDK:
   ```
    cdk bootstrap ACCOUNT-NUMBER/REGION # e.g.
    cdk bootstrap 1111111111/us-east-1
    cdk bootstrap --profile test 1111111111/us-east-1
   ```
1. From the command line, use AWS CDK to deploy the AWS resources for the pattern:
    ```
    npm run build && cdk deploy 
    ```
1. During the prompts:
    * Enter the desired AWS Region
    

## How it works

This template demonstrates how EventBridge Pipes can remove unneded attributes temporarily by storing them in DynamoDB, then retrieve them when needed. Use the AWS Lambda function as described below to generate sample events.

## Testing

Step-by-step instructions to understand the implementation for the pattern:

1. Deploy the ClaimCheckStack
2. Check the "ClaimCheckTable" in Amazon DynamoDB to see it is empty.
2. Trigger the ClaimCheckSampleDataCreatorLambda to generate a sample event.
3. Check the "ClaimCheckTable" again to see the event has been persistet in the database
4. Check the Amazon CloudWatch Log group '/aws/events/claimTargetLog' to see that only the claim check is passed to EventBridge
5. Check the ClaimCheckTargetWorkflow execution to see the enriched object in the target workflow.

## Cleanup
 
Delete the stack
    ```cdk destroy```

----
Copyright 2023 Amazon.com, Inc. or its affiliates. All Rights Reserved.

SPDX-License-Identifier: MIT-0
