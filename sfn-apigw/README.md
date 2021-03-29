# AWS Step Functions Standard Workflow to Amazon API Gateway REST API, with Amazon Cloudwatch Logs enabled.

The Step Functions Standard Workflow can be started using the AWS CLI or from another service.

The SAM template deploys a Step Functions Standard workflow that makes a call to a API Gateway REST endpoint. This endpoint asyncronously invokes a Lambda function. The SAM template contains the minimum IAM resources required to run the application with logging enabled.

Learn more about this pattern at Serverless Land Patterns: https://serverlessland.com/patterns/sfn-apigw

Important: this application uses various AWS services and there are costs associated with these services after the Free Tier usage - please see the [AWS Pricing page](https://aws.amazon.com/pricing/) for details. You are responsible for any AWS costs incurred. No warranty is implied in this example.

## Requirements

* AWS CLI already configured with Administrator permission
* [NodeJS 12.x installed](https://nodejs.org/en/download/)

## Installation Instructions

1. [Create an AWS account](https://portal.aws.amazon.com/gp/aws/developer/registration/index.html) if you do not already have one and login.

1. [Install Git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git) and [install the AWS Serverless Application Model CLI](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-sam-cli-install.html) on your local machine.

1. Create a new directory, navigate to that directory in a terminal and enter:
```
git clone https://github.com/aws-samples/serverless-patterns
cd sfn-apigw
```

4. From the command line, run:
```
sam deploy --guided
```
Choose a stack name, select the desired AWS Region, and allow SAM to create roles with the required permissions. Once you have run guided mode once, you can use `sam deploy` in future to use these defaults.

## How it works

* Start the Express Workflow using the `start-execution` api command.
* The Standard workflow makes a `GET` request to the API Gateway API REST endpoint.
* The API Gateway API REST endpoint invokes a Lambda function.
* The Lambda function generates a random ID.
* If the function does not fail, the Step Functions Execution ARN is returned.
* If the Lambda function fails, the Step Functions workflow will retry up to 5 times before exiting with a `status:FAILED` response.

## Testing

Run the following AWS CLI command to send a 'start-execution` comand to start the Step Functions workflow. Note, you must edit the {StateMachinetoAPIGW} placeholder with the ARN of the deployed Step Functions workflow. This is provided in the stack outputs.

```bash
aws stepfunctions start-execution  --name "test" --state-machine-arn "{StateMachinetoAPIGW}" --input "{\"message\":\"hello\"}"
```

### Example output:

```bash
{
    "executionArn": "arn:aws:states:eu-west-1:123456:execution:StateMachinetoAPIGW-hwTnEeeEGdgy:test",
    "startDate": "2021-02-10T17:02:33.009000+00:00"
}
```
Copyright 2021 Amazon.com, Inc. or its affiliates. All Rights Reserved.

SPDX-License-Identifier: MIT-0
