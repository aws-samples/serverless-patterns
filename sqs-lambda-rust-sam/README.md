# Amazon SQS to AWS Lambda

The SAM template deploys a Lambda function, an SQS queue and the IAM permissions required to run the application. SQS invokes the Lambda function when new messages are available.

Learn more about this pattern at Serverless Land Patterns: https://serverlessland.com/patterns/sqs-lambda-rust-sam.

Important: this application uses various AWS services and there are costs associated with these services after the Free Tier usage - please see the [AWS Pricing page](https://aws.amazon.com/pricing/) for details. You are responsible for any AWS costs incurred. No warranty is implied in this example.

## Requirements

* [Create an AWS account](https://portal.aws.amazon.com/gp/aws/developer/registration/index.html) if you do not already have one and log in. The IAM user that you use must have sufficient permissions to make necessary AWS service calls and manage AWS resources.
* [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html) installed and configured
* [Git Installed](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)
* [AWS Serverless Application Model](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-sam-cli-install.html) (AWS SAM) installed
* [Rust](https://www.rust-lang.org/) 1.56.0 or higher
* [cargo-zigbuild](https://github.com/messense/cargo-zigbuild) and [Zig](https://ziglang.org/) for cross-compilation

## Deployment Instructions

1. Create a new directory, navigate to that directory in a terminal and clone the GitHub repository:
    ``` 
    git clone https://github.com/aws-samples/serverless-patterns
    ```
2. Change directory to the pattern directory:
    ```
    cd sqs-lambda-rust-sam
    ```
3. Install dependencies and build:
    ```
    make build
    ```
4. From the command line, use AWS SAM to deploy the AWS resources for the pattern as specified in the template.yml file:
    ```
    make deploy
    ```
5. During the prompts:
    * Enter a stack name
    * Enter the desired AWS Region
    * Allow SAM CLI to create IAM roles with the required permissions.

    Once you have run `sam deploy -guided` mode once and saved arguments to a configuration file (samconfig.toml), you can use `sam deploy` in future to use these defaults.

6. Note the outputs from the SAM deployment process. These contain the resource names and/or ARNs which are used for testing.
   
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
            "eventSourceARN": "arn:aws:sqs:us-east-1:xxxxx:sam-app-MySqsQueue-1234567890",
            "awsRegion": "us-east-1"
        }
    ]
}

```
### Testing

Use the [AWS CLI](https://aws.amazon.com/cli/) to send a message to the SQS queue and observe the event delivered to the Lambda function:

1. Send the SQS message:
```bash
aws sqs send-message --queue-url ENTER_YOUR_SQS_QUEUE_URL --message-body "Test message"
```
2. Then check the logs in Cloudwatch logs, you should see something like
```bash
SqsEvent { records: [SqsMessage { message_id: Some("fa2012345678e816-0a49-4681-ba8f-1234567890"), receipt_handle: Some("1234567890NmjC1234567890qODTr1234567890/XPPk/f0qU4tJtQ1234567890ihWDp8YHKhDr3V1234567890e9amjZhgg1234567890RodR1234567890lwDGpf6oLa8/B/1234567890/Pq+xP/1234567890/1234567890fIV6nFUGs71234567890zsj616CBx912M12345678908rxtUEj1234567890J8d1234567890yDcI9E12345678905mTyYZ41S2cP01NCA1234567890jcalHD1234567890Kio+HFQp1234567890OI7bTs5I7pZJ4pu+BnM8Bcki1234567890aNML5B7S12345678904eYKKcrunp1234567890Qhz7BUWPG41"), body: Some("Test message"), md5_of_body: Some("82dfa5549ebc91234567890ece5f"), md5_of_message_attributes: None, attributes: {"SentTimestamp": "1612966720445", "ApproximateFirstReceiveTimestamp": "1612966720455", "SenderId": "AROAYKMZLNCDSKNYVGYUR:botocore-session-1644770178", "ApproximateReceiveCount": "1"}, message_attributes: {}, event_source_arn: Some("arn:aws:sqs:us-east-1:xxxxx:sam-app-MySqsQueue-1234567890"), event_source: Some("aws:sqs"), aws_region: Some("us-east-1") }] }

```


## Cleanup
 
1. Delete the stack
    ```bash
    make delete --stack-name STACK_NAME
    ```
----
Copyright 2021 Amazon.com, Inc. or its affiliates. All Rights Reserved.

SPDX-License-Identifier: MIT-0
