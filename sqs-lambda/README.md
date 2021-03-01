# Amazon SQS to AWS Lambda

This pattern creates an SQS queue and a Lambda function. The Lambda function is subscribed to the SQS queue. 

Learn more about this pattern at  Serverless Land Patterns: TBD

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

## Example event payload from SQS to Lambda

```
{
    "Records": [
        {
            "messageId": "fa2012345678e816-0a49-4681-ba8f-1234567890",
            "receiptHandle": "1234567890NmjC1234567890qODTr1234567890/XPPk/f0qU4tJtQ1234567890ihWDp8YHKhDr3V1234567890e9amjZhgg1234567890RodR1234567890lwDGpf6oLa8/B/1234567890/Pq+xP/1234567890/1234567890fIV6nFUGs71234567890zsj616CBx912M12345678908rxtUEj1234567890J8d1234567890yDcI9E12345678905mTyYZ41S2cP01NCA1234567890jcalHD1234567890Kio+HFQp1234567890OI7bTs5I7pZJ4pu+BnM8Bcki1234567890aNML5B7S12345678904eYKKcrunp1234567890Qhz7BUWPG41",
            "body": "Test message",
            "attributes": {
                "ApproximateReceiveCount": "1",
                "SentTimestamp": "1612966720445",
                "SenderId": "AIDA3DTKMG1234567890",
                "ApproximateFirstReceiveTimestamp": "1612966720455"
            },
            "messageAttributes": {},
            "md5OfBody": "82dfa5549ebc91234567890ece5f",
            "eventSource": "aws:sqs",
            "eventSourceARN": "arn:aws:sqs:us-east-1:123456789012:patterns-sqs-to-lambda-MySqsQueue-1234567890",
            "awsRegion": "us-east-1"
        }
    ]
}

```
## How it works

The AWS SAM template deploys the resources and the IAM permissions required to run the application.

When messages are sent to the SQS queue, they are delivered as a JSON event payload (see above) to the Lambda function.

### Testing

Use the [AWS CLI](https://aws.amazon.com/cli/) to send a message to the SQS queue and observe the event delivered to the Lambda function:

1. Send the SQS message:
```bash
aws sqs send-message --queue-url ENTER_YOUR_SQS_QUEUE_URL --message-body "Test message"
```
2. Retrieve the logs from the Lambda function:
```bash
sam logs -n ENTER_YOUR_CONSUMER_FUNCTION_NAME
```


----
Copyright 2021 Amazon.com, Inc. or its affiliates. All Rights Reserved.

SPDX-License-Identifier: MIT-0
