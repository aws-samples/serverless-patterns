# Filter and Transform Amazon SQS messages with Amazon EventBridge Pipes 

This pattern will use Amazon EventBridge Pipe connecting an Amazon SQS queue with an Amazon CloudWatch Log group. The pipe will apply a filter and transformation before sending the message to the CloudWatch Log group.
This pattern is implemented with AWS Serverless Application Model (AWS SAM).

Learn more about this pattern at Serverless Land Patterns: https://serverlessland.com/patterns/eventbridge-pipes-sqs-to-cwlog

Important: this application uses various AWS services and there are costs associated with these services after the Free Tier usage - please see the [AWS Pricing page](https://aws.amazon.com/pricing/) for details. You are responsible for any AWS costs incurred. No warranty is implied in this example.

## Requirements

- [Create an AWS account](https://portal.aws.amazon.com/gp/aws/developer/registration/index.html) if you do not already have one and log in. The IAM user that you use must have sufficient permissions to make necessary AWS service calls and manage AWS resources.
- [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html) installed and configured
- [Git Installed](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)
- [AWS SAM](https://docs.aws.amazon.com/cdk/latest/guide/cli.html) installed and configured

## Deployment Instructions

1. Create a new directory, navigate to that directory in a terminal and clone the GitHub repository:
   ```
   git clone https://github.com/aws-samples/serverless-patterns
   ```
2. Change directory to the pattern directory:
   ```
   cd serverless-patterns/eventbridge-pipes-sqs-to-cwlog/
   ```
3. From the command line, use AWS SAM to deploy the AWS resources for the pattern as specified in the template.yaml file:
    ```
    sam deploy --guided
    ```
4. During the prompts:
    * Enter a stack name
    * Enter `us-east-1` or any other AWS Region. 
    * Allow SAM CLI to create IAM roles with the required permissions. Please keep all other options to default.
5. Make a note of the output, which will be used during testing.

## How it works

* The template creates an SQS queue `source-queue`, a CloudWatch Log group `target-cw-log-group`, and EventBridge Pipe.
* The Amazon EventBridge pipe copies messages from `source-queue` to `target-cw-log-group` only if message payload (JSON) contains a `status` attribute with values `REJECTED` or `RETURNED`. The Amazon EventBridge Pipe will filter and transform the messages before sending it to `target-cw-log-group`.

Replace the "SQS_URL" with your SQS URL in the below command to send message to SQS:

```
 aws sqs send-message \
 --queue-url=SQS_URL \
 --message-body '{"id":"123", "status": "COMPLETED"}'

 aws sqs send-message \
 --queue-url=SQS_URL \
 --message-body '{"id":"456", "status": "RETURNED"}'

 aws sqs send-message \
 --queue-url=SQS_URL \
 --message-body '{"id":"789", "status": "REJECTED"}'

 aws sqs send-message \
 --queue-url=SQS_URL \
 --message-body '{"id":"110", "status": "DELIVERED"}'

Validate the result by reviewing the target CloudWatch Log group.
Amazon EventBridge Pipe filter will allow only messages with a status = "REJECTED" or "RETURNED".
The CloudWatch log group contains the following transformed messages. 
    Order ID 456 requires immediate attention. Order status RETURNED
    Order ID 789 requires immediate attention. Order status REJECTED
```

## Delete stack

```
sam delete
```

---

Copyright 2023 Amazon.com, Inc. or its affiliates. All Rights Reserved.

SPDX-License-Identifier: MIT-0
