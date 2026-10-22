# AWS Serverless Patterns Collection

This repo contains serverless patterns showing how to integrate services using infrastructure-as-code (IaC). You can use these patterns to help develop your own projects quickly.

- Learn more about these patterns at https://serverlessland.com/patterns.
- To learn more about submitting a pattern, read the [publishing guidelines page](https://github.com/aws-samples/serverless-patterns/blob/main/PUBLISHING.md).

## Patterns by job

Looking for a pattern by the job you need to run? Start here. Each list links to patterns that run that job on AWS Lambda.

### Background jobs
Run background jobs and queue workers without managing worker hosts or process supervisors.
- [Amazon SQS to AWS Lambda](./sqs-lambda)
- [Amazon API Gateway to Amazon SQS to AWS Lambda](./apigw-http-api-sqs-lambda-cdk)
- [Amazon API Gateway to Amazon SQS to AWS Lambda to Amazon DynamoDB](./apigw-sqs-lambda-ddb-cdk)

### Webhooks
Receive webhooks, verify and process each event, and retry safely.
- [Webhook receiver with AWS Lambda durable functions (Python)](./lambda-durable-webhook-sam-python)
- [Webhook receiver with AWS Lambda durable functions (Node.js)](./lambda-durable-webhook-sam-nodejs)
- [Shopify webhook integration with Amazon EventBridge to AWS Lambda](./shopify-eventbridge-lambda)

### Scheduled tasks
Run recurring tasks and cron jobs on a schedule.
- [Amazon EventBridge Scheduler to AWS Lambda every 5 minutes](./eventbridge-schedule-to-lambda-cdk)
- [Amazon EventBridge Scheduler to AWS Lambda with dead-letter queues](./eventbridge-schedule-to-lambda-dlq-sam-python)
- [Multi-day scheduled tasks with AWS Lambda durable functions](./lambda-durable-scheduled-tasks-sam)

### Durable workflows
Run long-running, multi-step workflows with checkpoints, human approvals, parallel branches and compensation.
- [Human approval workflow with AWS Lambda durable functions](./lambda-durable-human-approval-sam)
- [Saga pattern with compensation using AWS Lambda durable functions](./lambda-durable-saga-python-sam)
- [Parallel processing with AWS Lambda durable functions](./lambda-durable-parallel-processing-sam)
- [Function chaining with AWS Lambda durable functions](./lambda-durable-function-chaining-sam)

### File processing
Process files when they are uploaded: resize images, make thumbnails, parse CSV files.
- [Resize images uploaded to Amazon S3 with AWS Lambda](./s3-lambda-cdk)
- [Process CSV files uploaded to Amazon S3 with Amazon SQS and AWS Lambda](./cdk-s3-sqs-lambda-dynamodb)
- [Upload files up to 5 GB to Amazon S3 with a presigned URL](./apigw-lambda-s3-sam-java)

### Event-driven
Route and filter events so each handler runs only for the events it needs.
- [Amazon DynamoDB changes to AWS Lambda to Amazon EventBridge](./dynamodb-eventbridge)
- [Auth0 events to AWS Lambda with Amazon EventBridge](./auth0-eventbridge-lambda)
- [Amazon SNS filter policy to AWS Lambda](./apigw-sns-filter-policy-lambda-sls-py)

### Web apps and APIs on Lambda
Host a web app or API backend on AWS Lambda.
- [AWS Lambda function URL](./lambda-function-url)
- [Amazon CloudFront in front of AWS Lambda function URLs](./cloudfront-lambda-url-cdk-ts)
- [Amazon API Gateway REST API with AWS Lambda proxy integration](./apigw-cors-proxy)

Browse every pattern at [serverlessland.com/patterns](https://serverlessland.com/patterns).

Important: this application uses various AWS services and there are costs associated with these services after the Free Tier usage - please see the [AWS Pricing page](https://aws.amazon.com/pricing/) for details. You are responsible for any AWS costs incurred. No warranty is implied in this example.

## Deployment Instructions

1. [Create an AWS account](https://portal.aws.amazon.com/gp/aws/developer/registration/index.html) if you do not already have one and login.

1. [Install Git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git) and [install the AWS Serverless Application Model CLI](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-sam-cli-install.html) on your local machine.

1. Create a new directory and navigate to that directory in a terminal.

1. Clone this repo

```
git clone https://github.com/aws-samples/serverless-patterns
```

Each subdirectory contains additional installation and usage instructions.

## Ownership

This project is owned, managed, and maintained by the **AWS Sererless Developer Advocacy team**.

----
Copyright 2025 Amazon.com, Inc. or its affiliates. All Rights Reserved.

SPDX-License-Identifier: MIT-0
