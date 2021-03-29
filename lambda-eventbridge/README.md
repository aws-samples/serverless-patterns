# AWS Lambda to Amazon EventBridge

This pattern creates a Lambda function that publishes to EventBridge. 

Learn more about this pattern at Serverless Land Patterns: TBD

Important: this application uses various AWS services and there are costs associated with these services after the Free Tier usage - please see the [AWS Pricing page](https://aws.amazon.com/pricing/) for details. You are responsible for any AWS costs incurred. No warranty is implied in this example.

## Requirements

* AWS CLI already configured with Administrator permission
* [NodeJS 12.x installed](https://nodejs.org/en/download/)

## Deployment Instructions

1. [Create an AWS account](https://portal.aws.amazon.com/gp/aws/developer/registration/index.html) if you do not already have one and login.

1. [Install Git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git) and [install the AWS Serverless Application Model CLI](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-sam-cli-install.html) on your local machine.

1. Create a new directory, navigate to that directory in a terminal and enter ```git clone https://github.com/aws-samples/serverless-patterns/tree/main/lambda-eventbridge```.

1. Change directory to this pattern.

1. From the command line, run:
```
sam deploy --guided
```
Choose a stack name, select the desired AWS Region, and allow SAM to create roles with the required permissions. Once you have run guided mode once, you can use `sam deploy` in future to use these defaults.

1. Note the outputs from the SAM deployment process. These contain the resource names and ARNs.

## How it works

The AWS SAM template deploys the resources and the IAM permissions required to run the application. When the Lambda function is invoked, it publishes a test event to the default event bus in EventBridge.

## Testing

Use the [AWS CLI](https://aws.amazon.com/cli/) to send a test event to EventBridge and observe the Lambda function logs:

1. Send an event to EventBridge:

```bash
aws lambda invoke --function-name ENTER_YOUR_PUBLISHER_FUNCTION_NAME outfile.txt
```

2. Retrieve the logs from the Lambda function:
```bash
sam logs -n ENTER_YOUR_PUBLISHER_FUNCTION_NAME
```


----
Copyright 2021 Amazon.com, Inc. or its affiliates. All Rights Reserved.

SPDX-License-Identifier: MIT-0
