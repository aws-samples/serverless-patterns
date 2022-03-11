# Amazon SQS to AWS Lambda with Terraform

This pattern contains a Lambda function, an SQS queue, a CloudWatch Log group and the IAM permissions required to run the application. SQS invokes the Lambda function when new messages are available.

Learn more about this pattern at Serverless Land Patterns: [serverlessland.com/patterns/sqs-lambda](https://serverlessland.com/patterns/sqs-lambda)

Important: this application uses various AWS services and there are costs associated with these services after the Free Tier usage - please see the [AWS Pricing page](https://aws.amazon.com/pricing/) for details. You are responsible for any AWS costs incurred. No warranty is implied in this example.

## Requirements

* [Create an AWS account](https://portal.aws.amazon.com/gp/aws/developer/registration/index.html) if you do not already have one and log in. The IAM user that you use must have sufficient permissions to make necessary AWS service calls and manage AWS resources.
* [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html) installed and configured
* [Git Installed](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)
* [Terraform](https://learn.hashicorp.com/tutorials/terraform/install-cli) with version 1.x installed (this pattern has been tested with version 1.1.7)

## Deployment Instructions

1. Create a new directory, navigate to that directory in a terminal and clone the GitHub repository:
    ```
    git clone https://github.com/aws-samples/serverless-patterns
    ```
1. Change directory to the pattern directory:
    ```
    cd sqs-lambda-terraform-python
    ```
1. From the command line, use Terraform to deploy the AWS resources for the pattern as specified in the main.tf file:
    ```
    terraform init
    terraform apply --auto-approve
    ```

2. Note the outputs from the Terraform deployment process. These contain the resource names and/or ARNs which are used for testing.

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
                "SenderId": "AIDACKCEVSQ6C2EXAMPLE",
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

When a message is received by the SQS queue, the Lambda function is triggered to read and parse the message. For the sake of the pattern, the Lambda function pushes the message body in CloudWatchLogs.

## Testing

Use the [AWS CLI](https://aws.amazon.com/cli/) to send a message to the SQS queue and observe the event delivered to the Lambda function:

1. Send the SQS message:
```bash
aws sqs send-message --queue-url ENTER_YOUR_SQS_QUEUE_URL --message-body "Test message"
```
2. Retrieve the logs from the Lambda function:
```bash
aws logs filter-log-events --log-group-name ENTER_YOUR_LOG_GROUP_NAME
```


## Cleanup

1. Delete the stack
    ```bash
    terraform destroy --auto-approve
    ```
----
Copyright 2022 Amazon.com, Inc. or its affiliates. All Rights Reserved.

SPDX-License-Identifier: MIT-0
