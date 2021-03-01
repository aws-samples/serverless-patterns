# AWS Lambda to Amazon SQS

This pattern creates an SQS queue and a Lambda function. The Lambda function publishes to the SQS queue. 

Learn more about this pattern at Serverless Land Patterns: TBD

Important: this application uses various AWS services and there are costs associated with these services after the Free Tier usage - please see the [AWS Pricing page](https://aws.amazon.com/pricing/) for details. You are responsible for any AWS costs incurred. No warranty is implied in this example.

## Requirements

* AWS CLI already configured with Administrator permission
* [NodeJS 12.x installed](https://nodejs.org/en/download/)

## Installation Instructions

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

## Example payload from SQS

```
{                                                                                                                   
    "Messages": [
        {
            "MessageId": "12345678-876d-41f7-b32c-1234567890",
            "ReceiptHandle": "AQEBZfn1234567890O78Kn0C1234567890/z1+1234567890f2bQYOvD9RL1234567890Srr7+XQ/U1234567890j7nL+uaDVnJL1234567890mASoiwI/yQ1234567890gv/h17BW12345678908Pry0JM1234567890DfHE1g1234567890aMisj1234567890M+rC+ZF21234567890QdQpEwrX01234567890Fw6w2+Po0OA1234567890DkKgGuEmebp1234567890w7nNXujzSnzIXj1234567890CqfDOb2D1234567890kCk841+01234567890OaYzXV1234567890C+ruRXj1234567890AR5+vj8+U1234567890SJplJLjd1234567890YWV8o1234567890gJXb12345678901234567890",
            "MD5OfBody": "1234567890eb64e60d1234567890",
            "Body": "Message at Wed Feb 10 2021 13:47:31 GMT+0000 (Coordinated Universal Time)"
        }
    ]
}

```

## How it works

The AWS SAM template deploys the resources and the IAM permissions required to run the application.

When the Lambda function is invoked, it publishes a message to the SQS topic.

### Testing

Use the [AWS CLI](https://aws.amazon.com/cli/) to invoke the Lambda function. The function name is in the outputs of the AWS SAM deployment (the key is `QueuePublisherFunction`):

1. Invoke the Lambda function to publish a message to the SQS queue:

```bash
aws lambda invoke --function-name ENTER_YOUR_FUNCTION_NAME outfile.txt
```
2. Retrieve the message from the SQS queue, using the queue URL from the AWS SAM deployment outputs:
```bash
aws sqs receive-message --queue-url ENTER_YOUR_QUEUE_URL
```

----
Copyright 2021 Amazon.com, Inc. or its affiliates. All Rights Reserved.

SPDX-License-Identifier: MIT-0
