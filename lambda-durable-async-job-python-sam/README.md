# Async Job Processing with AWS Lambda Durable Functions

This pattern implements an async job API using Lambda durable functions. Submit a job via HTTP POST, get a job ID back immediately, then poll for status via HTTP GET. The durable function processes the job through checkpointed steps, updating progress in DynamoDB as it goes.

Learn more about this pattern at Serverless Land Patterns: [https://serverlessland.com/patterns/lambda-durable-async-job-python-sam](https://serverlessland.com/patterns/lambda-durable-async-job-python-sam)

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
    cd lambda-durable-async-job-python-sam
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

1. **Durable Lambda Function (Processor)**: A Python 3.13 Lambda function that uses the durable execution SDK to process jobs through three checkpointed steps: validate, process, and finalize. Each step updates progress in DynamoDB.

2. **API Lambda Function**: A standard Lambda function that handles HTTP requests — POST /jobs to submit work and GET /jobs/{id} to poll for status.

3. **HTTP API (API Gateway)**: An Amazon API Gateway HTTP API with two routes for job submission and status polling.

4. **DynamoDB Table**: A table that tracks job status, progress percentage, and results.

### Durable Execution Flow

- **POST /jobs**: API function creates a job record (SUBMITTED), invokes the durable processor asynchronously, returns job ID with HTTP 202.
- **Processor Step 1 (Validate)**: Validates input data, updates progress to 25%.
- **context.wait()**: Brief pause between steps (checkpointed, no compute charges).
- **Processor Step 2 (Process)**: Processes the data, updates progress to 50%.
- **Processor Step 3 (Finalize)**: Finalizes results, updates progress to 75%, then marks COMPLETED at 100%.
- **GET /jobs/{id}**: Returns current status and progress from DynamoDB at any point.

If the durable function is interrupted at any step, it resumes from the last checkpoint without re-executing completed work.

**Before durable functions, this pattern required**: SQS queue + consumer Lambda + Step Functions + custom polling logic. With durable functions, the entire workflow lives in a single function.

## Testing

1. Get the API endpoint from the stack outputs:
    ```bash
    API_URL=$(aws cloudformation describe-stacks \
      --stack-name lambda-durable-async-job \
      --query "Stacks[0].Outputs[?OutputKey=='ApiEndpoint'].OutputValue" \
      --output text)
    ```

2. Submit a job:
    ```bash
    curl -s -X POST "$API_URL/jobs" \
      -H "Content-Type: application/json" \
      -d '{"data": "Process this document", "priority": "high"}'
    ```

    Expected response (HTTP 202):
    ```json
    {"job_id": "abc-123-...", "status": "SUBMITTED"}
    ```

3. Poll for status (every few seconds):
    ```bash
    curl -s "$API_URL/jobs/<JOB_ID>"
    ```

    Status progresses: SUBMITTED → IN_PROGRESS → VALIDATING → PROCESSING → FINALIZING → COMPLETED

4. Test error handling (empty data):
    ```bash
    curl -s -X POST "$API_URL/jobs" \
      -H "Content-Type: application/json" \
      -d '{"priority": "low"}'
    ```

    The job completes with status FAILED and an error message.

## Cleanup

1. Delete the stack:
    ```bash
    sam delete
    ```

----
Copyright 2026 Amazon.com, Inc. or its affiliates. All Rights Reserved.

SPDX-License-Identifier: MIT-0
