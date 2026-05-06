# Amazon DynamoDB Cross-Account Replication with Global Tables

This pattern deploys a DynamoDB Global Table with cross-account replication and an IAM role for secure cross-account read access.

Learn more about this pattern at Serverless Land Patterns: https://serverlessland.com/patterns/dynamodb-cross-account-replication-cdk

Important: this application uses various AWS services and there are costs associated with these services after the Free Tier usage - please see the [AWS Pricing page](https://aws.amazon.com/pricing/) for details.

## Requirements

* [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html) installed and configured
* [AWS CDK](https://docs.aws.amazon.com/cdk/latest/guide/cli.html) installed
* [Node.js](https://nodejs.org/en/download/) installed
* Two AWS accounts (source and replica)

## Deployment Instructions

1. Clone and navigate to the pattern:
    ```
    cd serverless-patterns/dynamodb-cross-account-replication-cdk
    npm install
    ```
2. Deploy with the replica account ID:
    ```
    cdk deploy --parameters ReplicaAccountId=123456789012 --parameters ReplicaRegion=us-west-2
    ```

## How it works

- A DynamoDB Global Table is created with a replica in the specified region
- DynamoDB automatically replicates all writes to the replica with sub-second latency
- A cross-account IAM role allows the replica account to assume and read from the table
- Point-in-time recovery is enabled for data protection

## Testing

```bash
# Write an item to the source table
aws dynamodb put-item --table-name $(aws cloudformation describe-stacks \
  --stack-name DynamodbCrossAccountReplicationStack \
  --query 'Stacks[0].Outputs[?OutputKey==`TableName`].OutputValue' --output text) \
  --item '{"PK":{"S":"user#123"},"SK":{"S":"profile"},"name":{"S":"test"}}'

# Read from replica region (same account)
aws dynamodb get-item --table-name <TableName> \
  --key '{"PK":{"S":"user#123"},"SK":{"S":"profile"}}' \
  --region us-west-2
```

## Cleanup

```
cdk destroy
```

---

Copyright 2026 Amazon.com, Inc. or its affiliates. All Rights Reserved.

SPDX-License-Identifier: MIT-0
