# AWS Step Functions Standard Workflow to AWS Lambda functions with Amazon Cloudwatch Logs enabled 

The Step Functions Standard Workflow can be started using the AWS CLI or from another service (e.g. API Gateway) to run an standard workflow and return the result.

The SAM template deploys a Step Functions Standard workflow that invokes a Lambda function and cascades the output returned to another Lambda function, which finally returns a response. The SAM template contains the minimum IAM resources required to run the application with logging enabled.

Learn more about this pattern at Serverless Land Patterns: https://serverlessland.com/patterns/sfn-lambda-lambda

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
    cd sfn-lambda-lambda
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

* Start the Standard Workflow using the `start-execution` api command with a "message" string in the input payload.
* The Standard Workflow invokes a Lambda function.
* This Lambda function then returns a response which is used as an event to trigger another function that finally returns a response.
* If the Lambda function fails, the Step Functions workflow will retry up to 5 times before exiting with a `status:FAILED` response.

## Testing

Run the following AWS CLI command to send a 'start-execution` comand to start the Step Functions workflow. Note, you must replace the below test ARN of the deployed Step Functions workflow with your deployed. This is provided in the stack outputs.

```bash
aws stepfunctions start-execution  --name "test" --state-machine-arn "arn:aws:states:us-east-1:111111111:execution:YourStateMachine" 
--input "{\"message\":\"hello\"}"
```

### Example output:

```bash
{
    "startDate": 1658502748.259,
    "executionArn": "arn:aws:states:us-east-1:111111111:execution:YourStateMachine:test"
}
```
## Cleanup

 1. For deleting the stack you can use sam delete from SAM CLI -
    ```
    sam delete
    ```

----
Copyright 2021 Amazon.com, Inc. or its affiliates. All Rights Reserved.

SPDX-License-Identifier: MIT-0
