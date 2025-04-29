# Lambda SQS Best Practices with AWS CDK

This pattern demonstrates how to implement AWS Lambda with Amazon SQS using best practices, including AWS Lambda Powertools for structured logging, metrics, and tracing. The pattern includes proper error handling, dead-letter queue configuration, and comprehensive operational monitoring.

<img src="./resources/Lambda-SQS-Best-Practice.png" alt="Architecture" width="100%"/>

Important: this application uses various AWS services and there are costs associated with these services after the Free Tier usage - please see the [AWS Pricing page](https://aws.amazon.com/pricing/) for details. You are responsible for any AWS costs incurred. No warranty is implied in this example.

## Requirements

* [Create an AWS account](https://portal.aws.amazon.com/gp/aws/developer/registration/index.html) if you do not already have one and log in. The IAM user that you use must have sufficient permissions to make necessary AWS service calls and manage AWS resources.
* [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html) installed and configured
* [Git Installed](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)
* [Node.js 20 or greater](https://nodejs.org/en/download/) installed
* [AWS CDK](https://docs.aws.amazon.com/cdk/v2/guide/getting_started.html) installed

## Deployment Instructions

1. Create a new directory, navigate to that directory in a terminal and clone the GitHub repository:
    ``` 
    git clone https://github.com/aws-samples/serverless-patterns
    ```
1. Change directory to the pattern directory:
    ```
    cd serverless-patterns/lambda-sqs-best-practices-cdk
    ```

1. Install cdk dependencies
   ```
   npm install
   ```

1. Install lambda dependencies
   ```
   cd lambda
   npm install
   ```

1. Deploy cdk stack
    ```
    cd ..
    cdk deploy

    ```

Note: If you are using CDK for the first time then bootstrap CDK in your account by using below command:

```
cdk bootstrap aws://ACCOUNT-NUMBER-1/REGION-1

```

## How it works

This pattern sets up:

1. An SQS queue with a Dead Letter Queue (DLQ) for failed message handling
2. A Lambda function with:
   - AWS Lambda Powertools integration
   - Structured logging
   - Custom metrics
   - X-Ray tracing
3. A CloudWatch Dashboard for operational monitoring
4. Least priviledge permissions implemented on roles and policies

The Lambda function:
- Processes messages in batches
- Validates message format
- Handles errors gracefully
- Reports metrics and traces
- Uses structured logging

Failed messages are:
- Logged with error details
- Sent to DLQ after 3 retries
- Monitored via CloudWatch metrics

## Testing

The pattern includes a load testing script to verify functionality:

1. Set the Queue URL environment variable:
```bash
export QUEUE_URL=$(aws cloudformation describe-stacks --stack-name LambdaSqsBestPracticesCdkStack --query 'Stacks[0].Outputs[?OutputKey==`QueueUrl`].OutputValue' --output text)
export AWS_REGION=us-east-1  # or your AWS region
