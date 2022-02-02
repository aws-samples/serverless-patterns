# Amazon DynamoDB Streams to AWS Lambda with Event filtering

This event pattern demonstrates how DynamoDB Streams with event-based filtering on `dynamodb:put` and `dynamodb:delete` operations trigger Lambda functions. 

## Deploy the sample application

The AWS SAM CLI is an extension of the AWS CLI that adds functionality for building and testing Lambda applications. It uses Docker to run your functions in an Amazon Linux environment that matches Lambda. It can also emulate your application's build environment and API.

To use the AWS SAM CLI, you need the following tools:

* AWS SAM CLI - [Install the AWS SAM CLI](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-sam-cli-install.html).
* Node.js - [Install Node.js 14](https://nodejs.org/en/), including the npm package management tool.
* Docker - [Install Docker community edition](https://hub.docker.com/search/?type=edition&offering=community).

To build and deploy your application for the first time, run the following in your shell:

```bash
sam build
sam deploy --guided
```

## Cleanup

To delete the sample application that you created, use the AWS CLI. Assuming you used your project name for the stack name, you can run the following:

```bash
sam delete --stack-name event-filtering
```

## Resources
- [AWS announcement blog](https://aws.amazon.com/about-aws/whats-new/2021/11/aws-lambda-event-filtering-amazon-sqs-dynamodb-kinesis-sources/)
- [Trigger Lambda Functions with event filtering](https://dev.to/aws-builders/trigger-lambda-functions-with-event-filtering-2pnb)
- [Deep dive into Lambda event-filters for DyanmoDB](https://dev.to/aws-builders/deep-dive-into-lambda-event-filters-for-dyanmodb-320)
