# AWS Lambda with Amazon ElastiCache Serverless (Valkey)

This pattern deploys a Lambda function connected to Amazon ElastiCache Serverless running the Valkey engine for sub-millisecond key-value caching.

Learn more about this pattern at Serverless Land Patterns: https://serverlessland.com/patterns/lambda-elasticache-valkey-cdk

Important: this application uses various AWS services and there are costs associated with these services after the Free Tier usage - please see the [AWS Pricing page](https://aws.amazon.com/pricing/) for details.

## Requirements

* [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html) installed and configured
* [Node.js 22+](https://nodejs.org/en/download/) installed
* [AWS CDK v2](https://docs.aws.amazon.com/cdk/v2/guide/getting-started.html) installed
* A VPC with private subnets (or NAT gateway for public subnets)

## Architecture

```
┌──────────┐     ┌──────────────────┐     ┌─────────────────────────┐
│  Client  │────▶│  AWS Lambda      │────▶│  ElastiCache Serverless │
│          │     │  (VPC)           │     │  (Valkey 8)             │
└──────────┘     └──────────────────┘     └─────────────────────────┘
```

## How it works

1. Lambda connects to ElastiCache Serverless (Valkey engine) via VPC networking.
2. The function performs SET/GET/DEL operations using the RESP protocol.
3. ElastiCache Serverless auto-scales based on demand — no capacity planning needed.
4. Valkey 8 provides Redis-compatible commands with open-source licensing.

## Deployment

```bash
npm install
cdk deploy
```

Note: Lambda must be in subnets with connectivity to the ElastiCache endpoint (private subnets recommended).

## Testing

```bash
# Set a session key with 5-minute TTL
aws lambda invoke --function-name <FunctionName> \
  --payload '{"body":"{\"action\":\"set\",\"key\":\"session:user1\",\"value\":\"active\",\"ttl\":300}"}' \
  --cli-binary-format raw-in-base64-out output.json

# Get the key
aws lambda invoke --function-name <FunctionName> \
  --payload '{"body":"{\"action\":\"get\",\"key\":\"session:user1\"}"}' \
  --cli-binary-format raw-in-base64-out output.json
```

## Cleanup

```bash
cdk destroy
```
