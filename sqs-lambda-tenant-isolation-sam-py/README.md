# Lambda Tenant Isolation with SQS

This pattern demonstrate AWS Lambda's tenant isolation feature in Multi-tenant application. It uses single SQS for multi-tenant applucation and isolating messages using messagegroupid and invoking isolated lambda enviornments. 

## Key Features

- Tenant isolation at infrastructure level (no custom routing logic)
- Execution environments never shared between tenants
- Asynchronous invocation pattern
- Automatic tenant context propagation

Learn more about this pattern at [Serverless Land Patterns](https://serverlessland.com/patterns/sqs-lambda-tenant-isolation)

Important: this application uses various AWS services and there are costs associated with these services after the Free Tier usage - please see the [AWS Pricing page](https://aws.amazon.com/pricing/) for details. You are responsible for any AWS costs incurred. No warranty is implied in this example.

## Requirements

* [Create an AWS account](https://portal.aws.amazon.com/gp/aws/developer/registration/index.html) if you do not already have one and log in. The IAM user that you use must have sufficient permissions to make necessary AWS service calls and manage AWS resources.
* [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html) installed and configured
* [Git Installed](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)
* [AWS Serverless Application Model](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-sam-cli-install.html) (AWS SAM) installed

## Components

### 1. SQS Processor (`sqs-processor/`)
- Triggered by SQS queue messages
- Extracts `customer-id` from message payload
- Invokes tenant-isolated Lambda asynchronously with `TenantId` parameter

### 2. Tenant-Isolated Processor (`tenant-isolated-processor/`)
- Configured with tenant isolation mode enabled
- Processes requests in isolated execution environments per tenant
- Accesses tenant ID via `context.identity.tenant_id`

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

## How it works

```
SQS Queue → SQS Processor Lambda → Tenant-Isolated Lambda
            (reads customer-id)     (processes with tenant isolation)
```

## Testing

Send a message to the SQS queue:

```bash
aws sqs send-message \
  --queue-url <QUEUE_URL> \
  --message-body '{"data": "test payload"}'
```
