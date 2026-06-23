# Active-Active Multi-Region Serverless PostgreSQL with Amazon Aurora DSQL and AWS Lambda (CDK)

This pattern deploys Amazon Aurora DSQL linked clusters across two AWS regions with an AWS Lambda function that demonstrates active-active reads and writes using IAM authentication.

Learn more about this pattern at Serverless Land Patterns: https://serverlessland.com/patterns/lambda-dsql-multi-region-cdk

Important: this application uses various AWS services and there are costs associated with these services after the Free Tier usage - please see the [AWS Pricing page](https://aws.amazon.com/pricing/) for details.

## Why this pattern is different

Unlike the existing `apigw-lambda-dsql` pattern (which deploys a single-region cluster with SAM), this pattern demonstrates:

1. **Multi-region active-active replication** — Writes in us-east-1 are instantly readable in us-west-2 and vice versa
2. **IAM authentication** — No passwords, no Secrets Manager, no credential rotation needed
3. **No VPC required** — Amazon Aurora DSQL connects over the public internet with TLS, eliminating VPC/subnet/NAT Gateway complexity
4. **No connection pooling** — Unlike Amazon RDS, Amazon Aurora DSQL handles connection scaling natively (no Amazon RDS Proxy needed)
5. **CDK infrastructure as code** — Full `AWS::DSQL::Cluster` with `MultiRegionProperties`

## Requirements

* [Create an AWS account](https://portal.aws.amazon.com/gp/aws/developer/registration/index.html) if you do not already have one and log in.
* [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html) installed and configured
* [Node.js 20+](https://nodejs.org/en/download/) installed
* [AWS CDK v2](https://docs.aws.amazon.com/cdk/v2/guide/getting_started.html) installed (`npm install -g aws-cdk`)
* CDK bootstrapped in your account/region (`cdk bootstrap`)
* Amazon Aurora DSQL available in your regions (us-east-1, us-west-2)

## Deployment Instructions

1. Navigate to the pattern directory:
    ```bash
    cd lambda-dsql-multi-region-cdk
    ```

2. Install dependencies:
    ```bash
    npm install
    ```

3. Deploy (default: us-east-1 primary, us-west-2 peer):
    ```bash
    npx cdk deploy
    ```

    To customize the peer region:
    ```bash
    npx cdk deploy -c peerRegion=eu-west-1
    ```

## How it works

Amazon Aurora DSQL is a serverless, distributed SQL database that provides:

- **Active-active multi-region**: Both linked clusters accept reads AND writes simultaneously
- **Strong consistency**: Writes are durably committed across regions before acknowledgment
- **Serverless scaling**: No capacity planning, no instance types, no storage provisioning
- **PostgreSQL compatibility**: Standard psycopg2/JDBC/node-postgres drivers work unchanged
- **IAM authentication**: `dsql:DbConnect` permission + auth token generation replaces passwords entirely

The AWS Lambda function demonstrates three operations:
1. **setup** — Creates the `messages` table (runs once)
2. **write** — Inserts a message with the originating region
3. **read** — Lists recent messages showing which region wrote each one

## Testing

### Step 1: Create the table
```bash
aws lambda invoke --function-name FUNCTION_NAME \
  --payload '{"action": "setup"}' \
  --cli-binary-format raw-in-base64-out output.json && cat output.json
```

### Step 2: Write a message
```bash
aws lambda invoke --function-name FUNCTION_NAME \
  --payload '{"action": "write", "content": "Hello from us-east-1"}' \
  --cli-binary-format raw-in-base64-out output.json && cat output.json
```

### Step 3: Read messages (shows data from both regions)
```bash
aws lambda invoke --function-name FUNCTION_NAME \
  --payload '{"action": "read"}' \
  --cli-binary-format raw-in-base64-out output.json && cat output.json
```

### Step 4: Verify multi-region replication

Deploy a second copy in us-west-2, write there, then read from us-east-1 — you'll see messages from both regions, proving active-active replication.

## Cleanup

```bash
npx cdk destroy
```

---

Copyright 2026 Amazon.com, Inc. or its affiliates. All Rights Reserved.

SPDX-License-Identifier: MIT-0
