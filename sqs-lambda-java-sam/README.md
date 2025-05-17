# Process Amazon SQS records with AWS Lambda (Java)

This pattern shows how to process Amazon SQS messages using AWS Lambda. The AWS SAM template deploys an AWS Lambda function, an Amazon SQS queue, a dead-letter SQS queue, and the IAM permissions required to run the application. Lambda polls the SQS queue and invokes the Lambda function when new messages are available.

- Failed messages are automatically returned to the queue for retry using `batchItemFailures`.
- After 3 failed processing attempts, messages are moved to the DLQ.
- You should implement additional functionality to process messages that are sent to the DLQ.
- Processing results are logged to Amazon CloudWatch Logs

Learn more about this pattern at Serverless Land Patterns: [https://serverlessland.com/patterns/sqs-lambda-java-sam](https://serverlessland.com/patterns/sqs-lambda-java-sam)

:heavy_exclamation_mark: Important: this application uses various AWS services and there are costs associated with these services after the Free Tier usage - please see the [AWS Pricing page](https://aws.amazon.com/pricing/) for details. You are responsible for any AWS costs incurred. No warranty is implied in this example.

## Requirements

* [Create an AWS account](https://portal.aws.amazon.com/gp/aws/developer/registration/index.html) if you do not already have one and log in. The IAM user that you use must have sufficient permissions to make necessary AWS service calls and manage AWS resources.
* [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html) installed and configured
* [Git Installed](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)
* [AWS Serverless Application Model](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-sam-cli-install.html) (AWS SAM) installed

## Download Instructions

If you download this pattern as part of the AWS Toolkit for your IDE, the toolkit downloads the files into the directory you specify.

To download the patterns yourself: 
1. Create a new directory, navigate to that directory in a terminal and clone the GitHub repository:
    ``` 
    git clone https://github.com/aws-samples/serverless-patterns
    ```
1. Change directory to the pattern directory:
    ```
    cd sqs-lambda-java-sam
    ```

## Build Instructions

*For additional information on features to help you author, build, debug, test, and deploy Lambda applications more efficiently when using Visual Studio Code, see [Introducing an enhanced local IDE experience for AWS Lambda developers](https://aws.amazon.com/blogs/compute/introducing-an-enhanced-local-ide-experience-for-aws-lambda-developers?trk=2dd77e51-cb93-4970-a61a-5993781e5576&sc_channel=el).*

1. From the command line, use AWS SAM to build the AWS resources for the pattern as specified in the template.yml file:
    ```
    sam build
    ```
* You can also use `--use-container` to build your function inside a Lambda-like Docker container:
    ```
    sam build --guided --use-container
    ```

## Deployment Instructions

1. From the command line, use AWS SAM to deploy the AWS resources for the pattern as specified in the template.yaml file:
    ```
    sam deploy --guided
    ```
1. During the prompts:

1. During the prompts:
    * Enter a stack name
    * Enter the desired AWS Region
    * Allow AWS SAM CLI to create IAM roles with the required permissions.

    Once you have run `sam deploy -guided` mode once and saved arguments to a configuration file `samconfig.toml`, you can use `sam deploy` in future to use these defaults.

1. Note the outputs from the AWS SAM deployment process. These contain the resource names and/or ARNs to use for testing.
   
## Example event payload from SQS to Lambda

```
{
    "Records": [
        {
            "messageId": "059f36b4-87a3-44ab-83d2-661975830a7d",
            "receiptHandle": "AQEBwJnKyrHigUMZj6rYigCgxlaS3SLy0a...",
            "body": "test",
            "attributes": {
                "ApproximateReceiveCount": "1",
                "SentTimestamp": "1545082649183",
                "SenderId": "AIDAIENQZJOLO23YVJ4VO",
                "ApproximateFirstReceiveTimestamp": "1545082649185"
            },
            "messageAttributes": {},
            "md5OfBody": "098f6bcd4621d373cade4e832627b4f6",
            "eventSource": "aws:sqs",
            "eventSourceARN": "arn:aws:sqs:us-east-1:111122223333:my-queue",
            "awsRegion": "us-east-1"
        }
    ]
}

```
There is also a sample file `\events\test-event.json` which contains a sample event payload with 10 items.

### Testing

Use the [AWS CLI](https://aws.amazon.com/cli/) to send a message to the SQS queue and observe the event delivered to the Lambda function:

1. Send 10 messages to the SQS queue:

#### Bash
```bash
for i in {1..10}; do aws sqs send-message --queue-url <<ENTER_YOUR_SQS_QUEUE_URL>> --message-body "{\"message\": \"Test message-$i\"}"; done
```

##### PowerShell
```PowerShell
1..10 | ForEach-Object { aws sqs send-message --queue-url <<ENTER_YOUR_SQS_QUEUE_URL>> --message-body "{`"message`": `"Test message-$_`"}" }
```

2. Retrieve the logs from the Lambda function:
```bash
sam logs -n ENTER_YOUR_CONSUMER_FUNCTION_NAME
```

## Cleanup
 
1. Delete the stack
    ```bash
    sam delete --stack-name STACK_NAME
    ```
1. Confirm the stack has been deleted
    ```bash
    aws cloudformation list-stacks --query "StackSummaries[?contains(StackName,'STACK_NAME')].StackStatus"
    ```
----
Copyright 2025 Amazon.com, Inc. or its affiliates. All Rights Reserved.

SPDX-License-Identifier: MIT-0