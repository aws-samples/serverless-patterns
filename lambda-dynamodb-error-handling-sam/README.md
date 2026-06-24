# AWS Lambda to Amazon DynamoDB with SQS Partial Batch Error Handling

This pattern demonstrates best-practice error handling when processing SQS messages with Lambda and writing to DynamoDB. It uses ReportBatchItemFailures to return only failed message IDs so successfully processed messages are not retried, and routes persistently failing messages to a Dead Letter Queue.

Learn more about this pattern at Serverless Land Patterns: [https://serverlessland.com/patterns/lambda-dynamodb-error-handling-sam](https://serverlessland.com/patterns/lambda-dynamodb-error-handling-sam)

Important: this application uses various AWS services and there are costs associated with these services after the Free Tier usage - please see the [AWS Pricing page](https://aws.amazon.com/pricing/) for details. You are responsible for any AWS costs incurred. No warranty is implied in this example.

## Requirements

* [Create an AWS account](https://portal.aws.amazon.com/gp/aws/developer/registration/index.html) if you do not already have one and log in. The IAM user that you use must have sufficient permissions to make necessary AWS service calls and manage AWS resources.
* [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html) installed and configured
* [Git Installed](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)
* [AWS Serverless Application Model](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-sam-cli-install.html) (AWS SAM) installed
* [Python 3.12](https://www.python.org/downloads/) installed and available in your PATH

## Deployment Instructions

1. Create a new directory, navigate to that directory in a terminal and clone the GitHub repository:
    ```
    git clone https://github.com/aws-samples/serverless-patterns
    ```
1. Change directory to the pattern directory:
    ```
    cd lambda-dynamodb-error-handling-sam
    ```
1. From the command line, use AWS SAM to build and deploy the AWS resources for the pattern as specified in the template.yaml file:
    ```
    sam build
    sam deploy --guided
    ```
1. During the prompts:
    * Enter a stack name
    * Enter the desired AWS Region
    * Allow SAM CLI to create IAM roles with the required permissions.

    Once you have run `sam deploy --guided` mode once and saved arguments to a configuration file (samconfig.toml), you can use `sam deploy` in future to use these defaults.

1. Note the outputs from the SAM deployment process. These contain the resource names and/or ARNs which are used for testing.

## How it works

This pattern creates:

1. **Lambda Function (Processor)**: A Python 3.12 Lambda function that processes SQS message batches and writes items to DynamoDB. Uses `ReportBatchItemFailures` to return only failed message IDs.

2. **Source Queue (SQS)**: The queue that triggers the Lambda function with a batch size of 10. Visibility timeout is set to 6x the Lambda timeout (best practice).

3. **Dead Letter Queue (SQS)**: Messages that fail after 3 retries (maxReceiveCount) are automatically routed here for investigation. Retains messages for 14 days.

4. **Items Table (DynamoDB)**: The target table where successfully processed items are stored.

### Error Handling Flow

- **Valid message**: Parsed → written to DynamoDB → acknowledged (removed from queue).
- **Malformed message** (invalid JSON, missing fields): Caught by `json.JSONDecodeError` or `KeyError` → reported as batch item failure → retried up to 3 times → routed to DLQ.
- **DynamoDB error** (throttle, conditional check failure): Caught by `ClientError` → reported as batch item failure → retried (may succeed on retry).
- **Partial batch**: If 8 of 10 messages succeed, only the 2 failures are retried. The 8 successes are never re-processed.

## Testing

1. Send a valid message:
    ```bash
    QUEUE_URL=$(aws cloudformation describe-stacks \
      --stack-name lambda-dynamodb-error-handling \
      --query "Stacks[0].Outputs[?OutputKey=='QueueUrl'].OutputValue" \
      --output text)

    aws sqs send-message \
      --queue-url "$QUEUE_URL" \
      --message-body '{"id": "test-001", "name": "Test Item"}'
    ```

2. Verify item in DynamoDB:
    ```bash
    TABLE_NAME=$(aws cloudformation describe-stacks \
      --stack-name lambda-dynamodb-error-handling \
      --query "Stacks[0].Outputs[?OutputKey=='TableName'].OutputValue" \
      --output text)

    aws dynamodb get-item \
      --table-name "$TABLE_NAME" \
      --key '{"id": {"S": "test-001"}}'
    ```

3. Test error handling (malformed message):
    ```bash
    aws sqs send-message \
      --queue-url "$QUEUE_URL" \
      --message-body 'invalid-json'
    ```

    After 3 retries, check the DLQ:
    ```bash
    DLQ_URL=$(aws cloudformation describe-stacks \
      --stack-name lambda-dynamodb-error-handling \
      --query "Stacks[0].Outputs[?OutputKey=='DeadLetterQueueUrl'].OutputValue" \
      --output text)

    aws sqs receive-message --queue-url "$DLQ_URL"
    ```

## Cleanup

1. Delete the stack:
    ```bash
    sam delete
    ```

----
Copyright 2026 Amazon.com, Inc. or its affiliates. All Rights Reserved.

SPDX-License-Identifier: MIT-0
