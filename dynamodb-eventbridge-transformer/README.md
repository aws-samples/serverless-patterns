# Amazon DynamoDB to Amazon EventBridge using Amazon Eventbridge Pipes

This pattern takes a change data capture event from DynamoDB, removes the data type descriptors and sends the simplified event to an EventBridge bus.

The key components of this architecture are DynamoDB as source and EventBridge as target, connected by a pipe.

To demonstrate the end-to-end message flow, the Lambda function writes sample data to the DynamoDB table.

The pattern uses an input transformer to change the event's structure from DynamoDB's response format, which includes data type descriptors, to a simpler JSON structure. The input transformer also allows us to transform the list using the following notation: `<$.dynamodb.NewImage.Items.L[*].S>`

Learn more about this pattern at Serverless Land Patterns: https://serverlessland.com/patterns/claim-check-pattern-cdk

Important: this application uses various AWS services and there are costs associated with these services after the Free Tier usage - please see the [AWS Pricing page](https://aws.amazon.com/pricing/) for details. You are responsible for any AWS costs incurred. No warranty is implied in this example.

## Requirements

* [Create an AWS account](https://portal.aws.amazon.com/gp/aws/developer/registration/index.html) if you do not already have one and log in. The IAM user that you use must have sufficient permissions to make necessary AWS service calls and manage AWS resources.
* [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html) installed and configured
* [Git Installed](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)
* [AWS CDK](https://docs.aws.amazon.com/cdk/v2/guide/getting_started.html) installed

## Deployment Instructions

1. Create a new directory, navigate to that directory in a terminal and clone the GitHub repository:
    ``` 
    git clone https://github.com/aws-samples/serverless-patterns
    ```
1. Change directory to the pattern directory:
    ```
    cd serverless-patterns/dynamodb-eventbridge-transformer/src
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
    

## Testing

Step-by-step instructions to understand the implementation for the pattern:

1. Deploy the Stack
2. Trigger the writeDemoData Lambda function to generate three sample events.
3. Check the "targetLog" to see the events as they were sent to the EventBridge bus.

## Cleanup
 
Delete the stack
    ```cdk destroy```

----
Copyright 2023 Amazon.com, Inc. or its affiliates. All Rights Reserved.

SPDX-License-Identifier: MIT-0
