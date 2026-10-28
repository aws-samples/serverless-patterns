# Express in-process job runner to Amazon SQS and AWS Lambda

This pattern demonstrates moving an Express service's background work out of the web process and onto Amazon SQS with an AWS Lambda consumer, without changing the API's public contract. The `before/` folder is an Express app that runs each job in the request process and records progress in an Amazon DynamoDB jobs table. The `after/` folder keeps the same routes, job ids and status endpoint, but the API now enqueues each job to an SQS queue and a separate Lambda runs the identical step code, so the work survives deploys, scales independently, and dead-letters poison messages instead of looping forever.

Learn more about this pattern at Serverless Land Patterns: https://serverlessland.com/patterns/lambda-sqs-fastapi-typescript-sam

Important: this application uses various AWS services and there are costs associated with these services after the Free Tier usage - please see the [AWS Pricing page](https://aws.amazon.com/pricing/) for details. You are responsible for any AWS costs incurred. No warranty is implied in this example.

## Requirements

* [Create an AWS account](https://portal.aws.amazon.com/gp/aws/developer/registration/index.html) if you do not already have one and log in. The IAM user that you use must have sufficient permissions to make necessary AWS service calls and manage AWS resources.
* [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html) installed and configured
* [Git Installed](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)
* [AWS Serverless Application Model](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-sam-cli-install.html) (AWS SAM) installed
* [awscurl](https://github.com/okigan/awscurl) installed (`pip install awscurl`) to call the IAM-protected API
* [Node.js 24](https://nodejs.org/en/download/) installed (matches the nodejs24.x runtime; the tests and sam build use it)

## Deployment Instructions

1. Create a new directory, navigate to that directory in a terminal and clone the GitHub repository:
    ```
    git clone https://github.com/aws-samples/serverless-patterns
    ```
1. Change directory to the pattern directory:
    ```
    cd lambda-sqs-fastapi/typescript/sam
    ```
1. Install dependencies (the build and the tests need them):
    ```
    npm install
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

The API Lambda runs the Express app behind Amazon API Gateway (serverless-http adapts the app to the proxy event). A `POST /v1/jobs` writes a `PENDING` row to the DynamoDB jobs table, sends one message to the SQS queue, and returns `202` with the job id - it does not run the work. The worker Lambda is triggered by the queue, runs the three job steps (fetch, transform, publish), and updates the same row to `DONE` or `FAILED`. `GET /v1/jobs/{job_id}` reads the row, so the status endpoint is unchanged from the in-process version.

The queue is what the in-process worker could not give you: an unacknowledged message is redelivered after the visibility timeout, so a crash mid-job retries instead of stranding the row; a message that fails `maxReceiveCount` times is parked in a dead-letter queue; and the worker returns partial batch failures so only failed messages are redelivered. The API and the worker scale on their own.

The `before/` folder is the starting point to compare against - the same Express app running the steps on the request process. It is included as reference and is not deployed by this template.

Note: SQS delivers at least once, so a redelivered message runs the steps again from the top. The demo steps have no external effect, so that is safe; a real `publishResult` writing to a non-idempotent sink needs an idempotency key or a per-step checkpoint. The `POST` writes the row and sends the message as two calls, not one transaction: if the send fails after the row is written, the API deletes the `PENDING` row it just wrote and returns `503`, so the client's retry creates and enqueues the job afresh instead of finding a job no worker will ever see. Every worker update is conditional on the row still existing, so a message redelivered after the row's TTL is dropped rather than recreating the row.

Both functions use [Powertools for AWS Lambda (TypeScript)](https://docs.powertools.aws.dev/lambda/typescript/latest/): structured JSON logs with the invocation context, X-Ray subsegments for each DynamoDB and SQS call, `JobsEnqueued` / `JobsDone` / `JobsFailed` metrics in a namespace named after the stack, and the SQS batch processor for the partial batch response. API Gateway writes access logs to a log group with 14-day retention and throttles the stage at 50 requests per second (burst 100); access logging uses the one account-level API Gateway CloudWatch role per Region, which this template sets via `AWS::ApiGateway::Account`. The event source mapping caps the worker at 10 concurrent invocations; set `ReservedConcurrentExecutions: 0` on `JobWorkerFunction` to pause consumption entirely (messages wait in the queue) and raise it to resume. CloudWatch alarms on dead-letter queue depth and on each function's errors and throttles are created without actions - add your own `AlarmActions` to be notified.

## Testing

The API uses the `AWS_IAM` authorizer, so every call must be signed with SigV4. The examples use [awscurl](https://github.com/okigan/awscurl), which signs with the same AWS credentials you deployed with; an unsigned `curl` gets `403`. After deploying, note the `ApiUrl` output, then set it in your shell:

```bash
API=<ApiUrl output>
```

Submit a job and poll its status (use a fresh id each run):

```bash
RUN=$(date +%s)
awscurl --service execute-api -X POST $API/v1/jobs -d "{\"job_id\":\"ok-$RUN\",\"input\":\"hello\"}"
# wait a few seconds, then:
awscurl --service execute-api $API/v1/jobs/ok-$RUN
```

The status moves from `PENDING` to `DONE` with a `result`. A duplicate `POST` with the same `job_id` returns the existing job and does not enqueue it again.

Run the handler tests locally with no AWS account:

```bash
npm test
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
