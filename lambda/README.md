# AWS Lambda to AWS Lambda - Create a Lambda function that consumes events

This pattern is a simple Lambda function. 

The SAM template deploys A single Lambda function. The Lambda function concatenates `event.name` to a string and outputs the result.

Important: this application uses various AWS services and there are costs associated with these services after the Free Tier usage - please see the [AWS Pricing page](https://aws.amazon.com/pricing/) for details. You are responsible for any AWS costs incurred. No warranty is implied in this example.

## Requirements

* AWS CLI already configured with Administrator permission
* [NodeJS 12.x installed](https://nodejs.org/en/download/)

## Installation Instructions

1. [Create an AWS account](https://portal.aws.amazon.com/gp/aws/developer/registration/index.html) if you do not already have one and login.

1. [Install Git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git) and [install the AWS Serverless Application Model CLI](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-sam-cli-install.html) on your local machine.

1. Create a new directory, navigate to that directory in a terminal and enter ```git clone https://github.com/aws-samples/serverless-patterns```.

1. From the command line, run:
```
cd lambda
sam deploy --guided
```
Choose a stack name, select the desired AWS Region, and allow SAM to create roles with the required permissions. Once you have run guided mode once, you can use `sam deploy` in future to use these defaults.

## How it works

* Use the AWS CLI to asynchronously invoke the Lambda function.
* View the output in CloudWatch Logs.

==============================================

## Testing

### Success Testing

```bash
aws lambda invoke --function-name simpleFunction --invocation-type Event --payload  '{"name":"Ben"}' response.json --cli-binary-format raw-in-base64-out
```

### Failure testing
```bash
aws lambda invoke --function-name simpleFunction --invocation-type Event  response.json --cli-binary-format raw-in-base64-out
```


Copyright 2021 Amazon.com, Inc. or its affiliates. All Rights Reserved.

SPDX-License-Identifier: MIT-0
