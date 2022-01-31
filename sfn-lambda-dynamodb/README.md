# Create a Step Functions workflow that invokes Lambda and DynamoDB

This pattern passes event data from a State Machine to a DynamoDB table after the data is processed by a Lambda function. 

Learn more about this pattern at Serverless Land Patterns: https://serverlessland.com/patterns/sfn-lambda-ddb

Important: this application uses various AWS services and there are costs associated with these services after the Free Tier usage - please see the AWS Pricing page for details. You are responsible for any AWS costs incurred. No warranty is implied in this example.

## Requirements
Create an AWS account if you do not already have one and log in. The IAM user that you use must have sufficient permissions to make necessary AWS service calls and manage AWS resources.
AWS CLI installed and configured
Git Installed
AWS Serverless Application Model (AWS SAM) installed

## Deployment Instructions
1. Create a new directory, navigate to that directory in a terminal and clone the GitHub repository:
```
git clone https://github.com/aws-samples/serverless-patterns
```
2. Change directory to the pattern directory:
```
cd sfn-lambda-dynamodb
```
3. From the command line, use AWS SAM to deploy the AWS resources for the pattern as specified in the template.yml file:
```
sam deploy --guided
```
4. During the prompts:

- Enter a stack name
- Enter the desired AWS Region
- Allow SAM CLI to create IAM roles with the required permissions.
Once you have run `sam deploy --guided` mode once and saved arguments to a configuration file (samconfig.toml), you can use `sam deploy` in future to use these defaults.

5. Note the outputs from the SAM deployment process. These contain the resource names and/or ARNs which are used for testing.

## How it works
The state machine passes it's event data to a lambda function. You could choose to process the data here(using any business logic) and then send the data to be store in a DynamoDB table.

## Testing
The state machine can be executed from the a CLI or from the AWS console. Follows [these](https://docs.aws.amazon.com/cli/latest/reference/stepfunctions/start-execution.html) steps to execute a step function from your terminal. To execute the state machine from the AWS console follow [these](https://docs.aws.amazon.com/step-functions/latest/dg/getting-started.html#start-new-execution) instrusctions.
Whichever way you choose to execute the state machine add the following as input to it:
```
{
    "transaction_id": "44d106bd-c008-6214-1a8b-c6e08c638e60"
}
```
You can choose any value for the `transaction_id` attribute. 

## Cleanup
1. Delete the stack
```
aws cloudformation delete-stack --stack-name STACK_NAME
```
2. Confirm the stack has been deleted
```
aws cloudformation list-stacks --query "StackSummaries[?contains(StackName,'STACK_NAME')].StackStatus"
```
------------------------------------------------
Copyright 2021 Amazon.com, Inc. or its affiliates. All Rights Reserved.

SPDX-License-Identifier: MIT-0
