# AWS Lambda To Amazon DynamoDB - Persist Data to DynamoDB table from a Lambda function

The SAM template deploys a Lambda function, a DynamoDB table and the minimum IAM resources required to run the application. 
Learn more about this pattern at Serverless Land Patterns: TBD

Important: this application uses various AWS services and there are costs associated with these services after the Free Tier usage - please see the [AWS Pricing page](https://aws.amazon.com/pricing/) for details. You are responsible for any AWS costs incurred. No warranty is implied in this example.

## Requirements

* AWS CLI already configured with Administrator permission
* [NodeJS 12.x installed](https://nodejs.org/en/download/)

## Installation Instructions

1. [Create an AWS account](https://portal.aws.amazon.com/gp/aws/developer/registration/index.html) if you do not already have one and login.

1. [Install Git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git) and [install the AWS Serverless Application Model CLI](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-sam-cli-install.html) on your local machine.

1. Create a new directory, navigate to that directory in a terminal and enter ```git clone https://github.com/aws-samples/serverless-patterns/tree/main/lambda-eventbridge```.

1. From the command line, run:
```
sam deploy --guided
```
Choose a stack name, select the desired AWS Region, and allow SAM to create roles with the required permissions. Once you have run guided mode once, you can use `sam deploy` in future to use these defaults.

## How it works

* A Lambda function is invoked by an event integration or CLI command
* The Lambda function "stringifies" the event payload
* The Function uses the AWS SDK to perform a `put` command on a DynamoDB table 
* The name of the DynamoDB table is passed to the Lambda function via an environment variable named `DatabaseTable`
* The Lambda function is granted `PutItem` permissions, defined in the `LambdaExecRole` IAM Role.
==============================================

## Testing

Run the following Lambda CLI invoke command to invoke the function. Note, you must edit the {LambdaPutDynamoDBArn} placeholder with the ARN of the deployed Lambda function. This is provided in the stack outputs.

```bash
aws lambda invoke --function-name {LambdaPutDynamoDBArn} --invocation-type Event \
--payload '{ "Metadata": "Hello" }' \ response.json --cli-binary-format raw-in-base64-out  
```


Copyright 2021 Amazon.com, Inc. or its affiliates. All Rights Reserved.

SPDX-License-Identifier: MIT-0
