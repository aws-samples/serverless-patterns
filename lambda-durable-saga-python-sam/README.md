# Saga Pattern with AWS Lambda Durable Functions in Python

This pattern implements the Saga pattern using AWS Lambda durable functions. It processes a multi-step order through inventory reservation, payment processing, and order confirmation. If any step fails, compensating transactions execute in reverse order to undo all previously completed steps.

Learn more about this pattern at Serverless Land Patterns: [https://serverlessland.com/patterns/lambda-durable-saga-python-sam](https://serverlessland.com/patterns/lambda-durable-saga-python-sam)

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
    cd lambda-durable-saga-python-sam
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

1. **Durable Lambda Function (Saga Orchestrator)**: A Python 3.13 Lambda function that orchestrates three checkpointed steps in sequence and executes compensating transactions on failure.

2. **Orders Table (DynamoDB)**: Tracks order state (CONFIRMED or FAILED).

3. **Payments Table (DynamoDB)**: Tracks payment reservations and their status (RESERVED, CAPTURED, REFUNDED).

4. **Inventory Table (DynamoDB)**: Tracks available and reserved stock per item.

### Saga Execution Flow

**Happy Path (all steps succeed):**
1. **Reserve Inventory** — decrements available stock, increments reserved count
2. **Process Payment** — creates a payment record with status RESERVED
3. **Confirm Order** — writes order as CONFIRMED, updates payment to CAPTURED

**Failure Path (compensating transactions):**
1. **Reserve Inventory** — succeeds ✓
2. **Process Payment** — FAILS (e.g., amount exceeds limit)
3. **Compensate** — runs in reverse order:
   - Cancel payment → status set to REFUNDED
   - Release inventory → available stock restored to original
4. **Record failure** — writes order as FAILED with error message

Each step uses `@durable_step` for automatic checkpointing. If the function is interrupted, it resumes from the last completed step without re-execution.

## Testing

1. Seed inventory data:
    ```bash
    aws dynamodb put-item \
      --table-name lambda-durable-saga-inventory \
      --item '{"item_id": {"S": "ITEM-LAPTOP"}, "available": {"N": "50"}, "reserved": {"N": "0"}}'

    aws dynamodb put-item \
      --table-name lambda-durable-saga-inventory \
      --item '{"item_id": {"S": "ITEM-MOUSE"}, "available": {"N": "100"}, "reserved": {"N": "0"}}'
    ```

2. Test happy path (successful order):
    ```bash
    aws lambda invoke \
      --function-name "lambda-durable-saga-orchestrator:$LATEST" \
      --invocation-type Event \
      --cli-binary-format raw-in-base64-out \
      --payload '{"order_id": "ORD-001", "customer_id": "CUST-100", "items": [{"item_id": "ITEM-LAPTOP", "quantity": 2}, {"item_id": "ITEM-MOUSE", "quantity": 3}], "total_amount": "999.99"}' \
      /tmp/response.json
    ```

    After ~15 seconds, verify:
    ```bash
    aws dynamodb get-item \
      --table-name lambda-durable-saga-orders \
      --key '{"order_id": {"S": "ORD-001"}}'
    ```
    Expected: `"status": "CONFIRMED"`

3. Test failure path (payment declined triggers compensation):
    ```bash
    aws lambda invoke \
      --function-name "lambda-durable-saga-orchestrator:$LATEST" \
      --invocation-type Event \
      --cli-binary-format raw-in-base64-out \
      --payload '{"order_id": "ORD-FAIL", "customer_id": "CUST-200", "items": [{"item_id": "ITEM-LAPTOP", "quantity": 5}], "total_amount": "15000.00"}' \
      /tmp/response.json
    ```

    After ~30 seconds, verify compensation executed:
    ```bash
    # Order should be FAILED
    aws dynamodb get-item \
      --table-name lambda-durable-saga-orders \
      --key '{"order_id": {"S": "ORD-FAIL"}}'

    # Inventory should be restored
    aws dynamodb get-item \
      --table-name lambda-durable-saga-inventory \
      --key '{"item_id": {"S": "ITEM-LAPTOP"}}' \
      --query 'Item.{available: available.N, reserved: reserved.N}'
    ```
    Expected: Order `"status": "FAILED"`, inventory `available: 50, reserved: 0`

## Cleanup

1. Delete the stack:
    ```bash
    sam delete
    ```

----
Copyright 2026 Amazon.com, Inc. or its affiliates. All Rights Reserved.

SPDX-License-Identifier: MIT-0
