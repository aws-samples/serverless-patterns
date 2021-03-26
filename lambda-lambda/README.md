# AWS Lambda to AWS Lambda - Create a Lambda function that consumes events

This pattern is a Lambda function asynchronously triggered by a Lambda Function. 

The SAM template deploys three Lambda functions. A Producer function invokes a failure handler Lambda function on failure, or on Success handler Lambda function on success using event destinations.

Learn more about this pattern at Serverless Land Patterns: https://serverlessland.com/patterns/lambda-lambda

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

 cd lambda-lambda
 ```

4. From the command line, run:
```
sam deploy --guided
```
Choose a stack name, select the desired AWS Region, and allow SAM to create roles with the required permissions. Once you have run guided mode once, you can use `sam deploy` in future to use these defaults.

## How it works

* Use the AWS CLI to asynchronously invoke the producer function.
* A successfull execution will asynchronously invoke the `successHandlerFunction`
* An unsuccessfull, or failed execution will asynchronously invoke the `failHandlerFunction`
* which you can see in CloudWatch Logs.

==============================================

## Testing

### Success Testing

```bash
aws lambda invoke --function-name producerFunction --invocation-type Event --payload  '{"Success":true}' response.json --cli-binary-format raw-in-base64-out
```

### Failure testing
```bash
aws lambda invoke --function-name producerFunction --invocation-type Event --payload  '{"Success":false}' response.json --cli-binary-format raw-in-base64-out
```


Copyright 2021 Amazon.com, Inc. or its affiliates. All Rights Reserved.

SPDX-License-Identifier: MIT-0
