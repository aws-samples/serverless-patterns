# AWS Serverless Patterns Collection

This repo contains serverless patterns showing how to integrate services using infrastructure-as-code (IaC). You can use these patterns to help develop your own projects quickly.

- Learn more about these patterns at https://serverlessland.com/patterns.
- To learn more about submitting a pattern, read the [publishing guidelines page](https://github.com/aws-samples/serverless-patterns/blob/main/PUBLISHING.md).

## Patterns by job

Looking for a pattern by the job you need to run? Start here. Each list links to patterns that run that job on AWS Lambda.

### Background jobs
Run background jobs and queue workers without managing worker hosts or process supervisors.
- Amazon SQS to AWS Lambda:
  - Node.js: [AWS SAM](./sqs-lambda), [AWS CDK](./sqs-lambda-cdk)
  - Python: [AWS CDK](./sqs-lambda-cdk-python), [Terraform](./sqs-lambda-terraform-python)
  - Rust: [AWS SAM](./sqs-lambda-rust-sam)
- Process Amazon SQS messages with AWS Lambda: [Python](./sqs-lambda-python-sam), [Node.js](./sqs-lambda-nodejs-sam), [Java](./sqs-lambda-java-sam), [.NET](./sqs-lambda-dotnet-sam)
- Amazon API Gateway to Amazon SQS to AWS Lambda: [Python](./apigw-http-api-sqs-lambda-cdk), [TypeScript](./apigw-http-api-sqs-lambda-sls)
- Amazon API Gateway to Amazon SQS to AWS Lambda to Amazon DynamoDB: [Python with AWS CDK](./apigw-sqs-lambda-ddb-cdk), [Python with AWS SAM](./apigw-sqs-lambda-ddb)

### Webhooks
Receive webhooks, verify and process each event, and retry safely.
- [Webhook ingestion on AWS Lambda Web Functions with Amazon DynamoDB](./lambda-web-webhooks/nodejs/sam)
- [Shopify webhook integration with Amazon EventBridge to AWS Lambda](./shopify-eventbridge-lambda)
- Webhook receiver with AWS Lambda durable functions: [Python](./lambda-durable-webhook-sam-python), [Node.js](./lambda-durable-webhook-sam-nodejs)

### Scheduled tasks
Run recurring tasks and cron jobs on a schedule.
- Amazon EventBridge Scheduler to AWS Lambda every 5 minutes:
  - TypeScript: [AWS SAM](./eventbridge-schedule-to-lambda), [AWS CDK](./eventbridge-schedule-to-lambda-cdk), [Terraform](./eventbridge-schedule-to-lambda-terraform-typescript)
  - Java: [AWS SAM](./eventbridge-schedule-to-lambda-sam-java), [AWS CDK](./eventbridge-schedule-to-lambda-cdk-java), [Terraform](./eventbridge-schedule-to-lambda-terraform-java)
  - Go: [AWS SAM](./eventbridge-schedule-to-lambda-sam-go), [AWS CDK](./eventbridge-schedule-to-lambda-cdk-go), [Terraform](./eventbridge-schedule-to-lambda-terraform-go)
  - Python: [Terraform](./eventbridge-schedule-to-lambda-terraform-python)
- [Amazon EventBridge Scheduler to AWS Lambda with dead-letter queues](./eventbridge-schedule-to-lambda-dlq-sam-python)
- [Multi-day scheduled tasks with AWS Lambda durable functions](./lambda-durable-scheduled-tasks-sam)

### Durable workflows
Run long-running, multi-step workflows with checkpoints, human approvals, parallel branches and compensation, using AWS Step Functions or AWS Lambda durable functions.
- [AWS Step Functions to AWS Lambda](./sfn-lambda)
- [AWS Step Functions to AWS Lambda durable functions](./cdk-stepfunction-durable-lambda-function)
- [Human approval workflow with AWS Lambda durable functions](./lambda-durable-human-approval-sam)
- Saga pattern with compensation using AWS Lambda durable functions: [Python](./lambda-durable-saga-python-sam), [Python with AWS CDK](./saga-pattern-lambda-durable-functions), [Node.js](./lambda-durable-functions-nodejs-saga-pattern)
- [Parallel processing with AWS Lambda durable functions](./lambda-durable-parallel-processing-sam)
- Function chaining with AWS Lambda durable functions: [Python](./lambda-durable-function-chaining-sam), [Python with Terraform](./lambda-durable-function-chaining-terraform)

### File processing
Process files when they are uploaded: resize images, make thumbnails, parse CSV files.
- Resize images uploaded to Amazon S3 with AWS Lambda:
  - Python: [AWS SAM](./s3-lambda-resizing-python)
  - Node.js: [AWS SAM](./s3-lambda-resizing-node), [AWS CDK](./s3-lambda-cdk)
  - Java: [AWS SAM](./s3-lambda-resizing-java)
  - .NET: [AWS SAM](./s3-lambda-resizing-dotnet)
- [Process CSV files uploaded to Amazon S3 with Amazon SQS and AWS Lambda](./cdk-s3-sqs-lambda-dynamodb)
- [Upload files up to 5 GB to Amazon S3 with a presigned URL](./apigw-lambda-s3-sam-java)

### Event-driven
Route and filter events so each handler runs only for the events it needs.
- Process Amazon SNS messages with AWS Lambda: [Python](./sns-lambda-python-sam), [Node.js](./sns-lambda-nodejs-sam), [Java](./sns-lambda-java-sam), [.NET](./sns-lambda-dotnet-sam)
- Amazon DynamoDB changes to AWS Lambda to Amazon EventBridge: [Node.js](./dynamodb-eventbridge), [Java](./dynamodb-eventbridge-java)
- [Auth0 events to AWS Lambda with Amazon EventBridge](./auth0-eventbridge-lambda)
- [Amazon SNS filter policy to AWS Lambda](./apigw-sns-filter-policy-lambda-sls-py)

### Web apps and APIs on Lambda
Host a web app or API backend on AWS Lambda with Amazon API Gateway or Lambda Web Functions.
- Amazon API Gateway REST API with AWS Lambda: [Python](./apigw-rest-api-lambda-python), [Node.js](./apigw-rest-api-lambda-node), [Java](./apigw-rest-api-lambda-java), [.NET](./apigw-rest-api-lambda-dotnet)
- [Node.js HTTP server on AWS Lambda Web Functions](./lambda-web-http-server/nodejs/sam)
- [Express.js CRUD API on AWS Lambda Web Functions with Amazon DynamoDB](./lambda-web-dynamodb-api/nodejs/sam)
- AWS Lambda Web Function behind Amazon CloudFront: [AWS SAM](./lambda-web-cloudfront-oac/nodejs/sam), [AWS CDK](./lambda-web-cloudfront-oac/nodejs/cdk), [AWS CLI](./lambda-web-cloudfront-oac/nodejs/awscli)
- Real-time dashboard with server-sent events on AWS Lambda Web Functions: [AWS SAM](./lambda-web-sse-dashboard/nodejs/sam), [AWS CLI](./lambda-web-sse-dashboard/nodejs/awscli)
- [Remote MCP server on AWS Lambda Web Functions](./lambda-web-mcp-server/nodejs/awscli)
- [Amazon API Gateway REST API with AWS Lambda proxy integration and CORS](./apigw-cors-proxy)
- AWS Lambda function URL: [Node.js](./lambda-function-url), [TypeScript](./lambda-function-url-cdk)
- Amazon CloudFront in front of AWS Lambda function URLs: [TypeScript](./cloudfront-lambda-url-cdk-ts), [Java](./cloudfront-lambda-url-java)

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
