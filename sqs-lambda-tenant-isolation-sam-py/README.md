# Lambda Tenant Isolation with SQS

This pattern demonstrate AWS Lambda's tenant isolation feature in Multi-tenant application.

## Key Features

- Tenant isolation at infrastructure level (no custom routing logic)
- Execution environments never shared between tenants
- Asynchronous invocation pattern
- Automatic tenant context propagation

Learn more about this pattern at [Serverless Land Patterns](https://serverlessland.com/patterns/sqs-lambda-tenant-isolation)

Important: this application uses various AWS services and there are costs associated with these services after the Free Tier usage - please see the [AWS Pricing page](https://aws.amazon.com/pricing/) for details. You are responsible for any AWS costs incurred. No warranty is implied in this example.


## Architecture

```
SQS Queue → SQS Processor Lambda → Tenant-Isolated Lambda
            (reads customer-id)     (processes with tenant isolation)
```

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
  "customer-id": "tenant-123",
  "data": "your payload here"
}
```

## Deployment

```bash
sam build
sam deploy --guided
```

## Testing

Send a message to the SQS queue:

```bash
aws sqs send-message \
  --queue-url <QUEUE_URL> \
  --message-body '{"customer-id": "tenant-123", "data": "test payload"}'
```


