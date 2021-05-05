# AWS Step Functions Standard Workflow to Amazon SQS, with no callback 

The SAM template deploys a Step Functions Standard workflow that takes in a payload and send it to an Amazon SQS. The SAM template contains the minimum IAM resources required to run the application.

Learn more about this pattern at Serverless Land Patterns: https://serverlessland.com/patterns/sfn-sqs

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
    cd sfn-lambda
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

## How it works

* Start the Step Function execution with the event payload 
* As part of the execution, part of the payload (the `message` attribute of the payload) gets pushed to the queue
* Run the cli command to pull messages from the queue to verify the message got delivered.

## Testing

Run the following AWS CLI command to send a 'start-sync-execution` comand to start the Step Functions workflow. Note, you must edit the {StateMachineExpressSynctoLambda} placeholder with the ARN of the deployed Step Functions workflow. This is provided in the stack outputs.

```bash
aws stepfunctions start-sync-execution  --name "test" --state-machine-arn "{StateMachinetoSQS}" --input "{\"message\": {\"hello\" : \"world\" } }"
```

### Example output:

```bash
{
    "executionArn": "arn:aws:states:eu-west-1:123:express:StateMachineExpressSynctoLambda-ftxlCWos7gZd:1:0d806925-361f-4dbf-af36-05ab6a40a8ec",
    "stateMachineArn": "arn:aws:states:eu-west-1:123:stateMachine:StateMachineExpressSynctoLambda-ftxlCWos7gZd",
    "name": "1",
    "startDate": "2021-02-10T15:06:10.895000+00:00",
    "stopDate": "2021-02-10T15:06:11.265000+00:00",
    "status": "SUCCEEDED",
    "input": "{\"message\":\"hello\"}",
    "inputDetails": {
        "included": true
    },
    "output": "{\"message\":\"hello\",\"ticketId\":\"8pcna9\"}",
    "outputDetails": {
        "included": true
    }
}
```
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
