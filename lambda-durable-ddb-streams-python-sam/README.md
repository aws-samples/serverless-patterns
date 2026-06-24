# Amazon DynamoDB Streams to AWS Lambda Durable Function

This pattern implements a change data capture (CDC) pipeline using DynamoDB Streams and Lambda durable functions. When items are written to the source table, the stream triggers a multi-step processing pipeline with automatic checkpointing at each step.

Learn more about this pattern at Serverless Land Patterns: [https://serverlessland.com/patterns/lambda-durable-ddb-streams-python-sam](https://serverlessland.com/patterns/lambda-durable-ddb-streams-python-sam)

Important: this application uses various AWS services and there are costs associated with these services after the Free Tier usage - please see the [AWS Pricing page](https://aws.amazon.com/pricing/) for details. You are responsible for any AWS costs incurred. No warranty is implied in this example.

## Requirements

* [Create an AWS account](https://portal.aws.amazon.com/gp/aws/developer/registration/index.html) if you do not already have one and log in. The IAM user that you use must have sufficient permissions to make necessary AWS service calls and manage AWS resources.
* [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html) installed and configured
* [Git Installed](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)
* [AWS Serverless Application Model](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-sam-cli-install.html) (AWS SAM) installed
* [Python 3.13](https://www.python.org/downloads/) installed and available in your PATH

## Deployment Instructions

1. Create a new directory, navigate to that directory in a terminal and clone the GitHub repository:
    ```
    git clone https://github.com/aws-samples/serverless-patterns
    ```
1. Change directory to the pattern directory:
    ```
    cd lambda-durable-ddb-streams-python-sam
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

1. **Durable Lambda Function (Stream Processor)**: A Python 3.13 Lambda function that processes DynamoDB stream events through three checkpointed steps: validate, enrich, and notify.

2. **Source Table (DynamoDB with Streams)**: The table where items are written. DynamoDB Streams captures INSERT, MODIFY, and REMOVE events with NEW_AND_OLD_IMAGES.

3. **Processed Table (DynamoDB)**: Stores enriched records with computed metadata (event type, timestamps, flags).

4. **Notifications Table (DynamoDB)**: Audit trail of notification records for each processed event.

### Durable Execution Flow

1. An item is written to the source table, generating a stream event.
2. The durable function receives a batch of stream records.
3. For each record:
   - **Step 1 (Validate)**: Checks record integrity and required fields. REMOVE events are validated but skip further processing.
   - **Step 2 (Enrich)**: Adds computed fields (category, timestamps, name length, description flag) and writes to the processed table.
   - **Step 3 (Notify)**: Creates an audit notification record in the notifications table.
4. Each step is checkpointed. If the function replays, completed steps return cached results without re-executing.
5. Uses `ReportBatchItemFailures` so only failed records are retried — successfully processed records are not re-sent.

**Important**: This pattern uses `AutoPublishAlias: live` because DynamoDB Streams event source mappings with durable functions require a qualified ARN (published version or alias). The `ExecutionTimeout` is set to 900 seconds (maximum allowed for event source mappings).

## Testing

1. Write an item to the source table (INSERT event):
    ```bash
    aws dynamodb put-item \
      --table-name lambda-durable-ddb-streams-source \
      --item '{
        "pk": {"S": "PRODUCT-001"},
        "name": {"S": "Wireless Headphones"},
        "category": {"S": "Electronics"},
        "description": {"S": "Premium noise-cancelling headphones"}
      }'
    ```

2. After 10-30 seconds, verify the processed record:
    ```bash
    aws dynamodb scan --table-name lambda-durable-ddb-streams-processed
    ```

    Expected: enriched record with `event_type: INSERT`, `processed_at`, `name_length`, `has_description: true`.

3. Verify the notification:
    ```bash
    aws dynamodb scan --table-name lambda-durable-ddb-streams-notifications
    ```

    Expected: notification record with `event_type`, `message`, `created_at`.

4. Test MODIFY event:
    ```bash
    aws dynamodb put-item \
      --table-name lambda-durable-ddb-streams-source \
      --item '{
        "pk": {"S": "PRODUCT-001"},
        "name": {"S": "Wireless Headphones Pro"},
        "category": {"S": "Electronics"}
      }'
    ```

## Cleanup

1. Delete the stack:
    ```bash
    sam delete
    ```

----
Copyright 2026 Amazon.com, Inc. or its affiliates. All Rights Reserved.

SPDX-License-Identifier: MIT-0
