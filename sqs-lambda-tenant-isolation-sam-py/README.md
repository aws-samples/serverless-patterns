# AWS Lambda Tenant Isolation with Amazon SQS

This pattern demonstrates AWS Lambda's tenant isolation feature in Multi-tenant application. It uses single Amazon SQS for multi-tenant application and isolating messages using messagegroupid and invoking isolated lambda enviornments. 

## Key Features

- Tenant isolation at infrastructure level (no custom routing logic)
- Execution environments never shared between tenants
- Asynchronous invocation pattern
- Automatic tenant context propagation

Learn more about this pattern at [Serverless Land Patterns](https://serverlessland.com/patterns/sqs-lambda-tenant-isolation-sam-py)

Important: this application uses various AWS services and there are costs associated with these services after the Free Tier usage - please see the [AWS Pricing page](https://aws.amazon.com/pricing/) for details. You are responsible for any AWS costs incurred. No warranty is implied in this example.

## Requirements

* [Create an AWS account](https://portal.aws.amazon.com/gp/aws/developer/registration/index.html) if you do not already have one and log in. The IAM user that you use must have sufficient permissions to make necessary AWS service calls and manage AWS resources.
* [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html) installed and configured
* [Git Installed](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)
* [AWS Serverless Application Model](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-sam-cli-install.html) (AWS SAM) installed

## How it works

<img width="535" height="183" alt="image" src="https://github.com/user-attachments/assets/b6af3efa-e81b-4a08-80ca-b7536934d490" />

### 1. SQS Processor (`sqs-processor/`)
- Triggered by SQS queue messages
- Invokes tenant-isolated Lambda asynchronously

### 2. Tenant-Isolated Processor (`tenant-isolated-processor/`)
- Configured with tenant isolation mode enabled
- Processes requests in isolated execution environments per tenant using message-group-id

## Message Format

```json
{
  "data": "your payload here"
}
```

## Deployment Instructions

```bash
sam build
sam deploy --guided
```

## Testing

Step 1: 
After deploying infrastructure using SAM, run below command to get SQS Queue URL. Replace <your-stack-name> with your cloudformation stack name.

```bash
aws cloudformation describe-stacks \
  --stack-name <your-stack-name> \
  --query "Stacks[0].Outputs[?OutputKey=='MyQueueUrl'].OutputValue" \
  --output text
```

Step 2:
You send messages to the SQS queue with --message-group-id set to a tenant identifier. Use below CLI command to send-message. Make sure to set --message-group-id as tenant name. Send multiple messages with different tenant name

```bash
aws sqs send-message \
  --queue-url <QUEUE_URL> \
  --message-body '{"data": "test payload"}' \
  --message-group-id "tenant-blue"
```

```bash
aws sqs send-message \
  --queue-url <QUEUE_URL> \
  --message-body '{"data": "test payload"}' \
  --message-group-id "tenant-green"
```

Step 3:
The SQS processor Lambda picks up the message, reads the MessageGroupId from the SQS record attributes, and passes it as the TenantId when invoking the tenant-isolated LambdaAfter dropping the message, review cloudwatch log for Tenant-Isolated Lambda.

aws logs describe-log-streams \
  --log-group-name /aws/lambda/tenant-isolated-processor \
  --order-by LastEventTime \
  --descending

Different log streams should be created for each tenant.

## Cleanup

Delete the stack
```bash
aws cloudformation delete-stack --stack-name STACK_NAME
```
Confirm the stack has been deleted
```bash
aws cloudformation list-stacks --query "StackSummaries[?contains(StackName,'STACK_NAME')].StackStatus"
```
----
Copyright 2026 Amazon.com, Inc. or its affiliates. All Rights Reserved.

SPDX-License-Identifier: MIT-0
