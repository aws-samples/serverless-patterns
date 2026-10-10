# Amazon DynamoDB Global Tables with Cross-Account Read Access

This pattern deploys an Amazon DynamoDB Global Table (same-account, multi-region) and an AWS Identity and Access Management (IAM) role that grants a separate AWS account read-only access to the table in both regions.

Learn more about this pattern at Serverless Land Patterns: https://serverlessland.com/patterns/dynamodb-cross-account-replication-cdk

Important: this application uses various AWS services and there are costs associated with these services after the Free Tier usage - please see the [AWS Pricing page](https://aws.amazon.com/pricing/) for details.

## Requirements

* [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html) installed and configured
* [AWS CDK](https://docs.aws.amazon.com/cdk/latest/guide/cli.html) installed
* [Node.js](https://nodejs.org/en/download/) 20.x or later
* Two AWS accounts (one owns the table, the other reads from it)
* CDK bootstrapped in the deployment account/region (`cdk bootstrap`)

## How it works

```
┌─────────────────────────────────────────────────────────────────┐
│  Owner Account                                                   │
│                                                                   │
│  ┌─────────────────┐   Global Tables    ┌─────────────────┐     │
│  │ DynamoDB Table   │ ─────────────────▶ │ DynamoDB Replica │     │
│  │ (us-east-1)      │   auto-replicate   │ (us-west-2)      │     │
│  └─────────────────┘                    └─────────────────┘     │
│           │                                       │              │
│           └───────────── IAM Role ───────────────┘              │
│                              │                                    │
└──────────────────────────────┼────────────────────────────────────┘
                               │ AssumeRole
┌──────────────────────────────┼────────────────────────────────────┐
│  Reader Account              ▼                                    │
│              GetItem / Query / BatchGetItem                       │
└───────────────────────────────────────────────────────────────────┘
```

- A DynamoDB Global Table is created with a replica in the specified region (same account)
- An IAM role is created that the reader account can assume only when it passes the external ID you set at deploy time
- The role grants read-only access (`GetItem`, `Query`, `BatchGetItem`) to the table in **both** regions
- DynamoDB handles replication automatically with sub-second latency

**Note:** This is same-account multi-region replication (Global Tables) with cross-account read access via IAM. For true cross-account Global Tables replication, use `TableV2MultiAccountReplica` in a separate stack deployed to the replica account.

**Trust policy:** the role trusts the reader account and requires the `sts:ExternalId` you pass in `ExternalId`. Share that value only with the team that runs the reader workload. To limit the trust to one role or user in the reader account, add a condition on `aws:PrincipalArn` to the trust policy.

**Encryption:** the table uses the default AWS-owned key, so no key policy changes are needed. If you switch to a customer-managed KMS key, make sure the key policy or the role's IAM policy lets the cross-account role use the key (for example `kms:Decrypt`) in each Region it reads from. See [DynamoDB encryption at rest usage notes](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/encryption.usagenotes.html) for the permissions DynamoDB requires on a customer managed key.

## Deployment Instructions

1. Clone and navigate to the pattern:
    ```bash
    cd serverless-patterns/dynamodb-cross-account-replication-cdk
    npm install
    ```
2. Deploy with the reader account ID, an external ID of your choice (at least 8 characters), and the replica region:
    ```bash
    cdk deploy --parameters ReplicaAccountId=<READER_ACCOUNT_ID> --parameters ExternalId=<EXTERNAL_ID> -c replicaRegion=us-west-2
    ```

## Testing

```bash
# Write an item to the source table
aws dynamodb put-item --table-name $(aws cloudformation describe-stacks \
  --stack-name DynamodbCrossAccountReplicationStack \
  --query 'Stacks[0].Outputs[?OutputKey==`TableName`].OutputValue' --output text) \
  --item '{"PK":{"S":"user#123"},"SK":{"S":"profile"},"name":{"S":"test"}}'

# Read from replica region (same account, verifies replication)
aws dynamodb get-item --table-name <TableName> \
  --key '{"PK":{"S":"user#123"},"SK":{"S":"profile"}}' \
  --region us-west-2

# Cross-account read (from reader account, assuming the role)
aws sts assume-role --role-arn <CrossAccountRoleArn> \
  --role-session-name reader-test --external-id <EXTERNAL_ID>

# Export the temporary credentials
export AWS_ACCESS_KEY_ID=<AccessKeyId from above>
export AWS_SECRET_ACCESS_KEY=<SecretAccessKey from above>
export AWS_SESSION_TOKEN=<SessionToken from above>

# Read from the replica region using the cross-account role
aws dynamodb get-item --table-name <TableName> \
  --key '{"PK":{"S":"user#123"},"SK":{"S":"profile"}}' \
  --region us-west-2
```

## Cleanup

> **⚠️ Warning:** `cdk destroy` with `RemovalPolicy.DESTROY` will permanently delete the table and all its data. Back up any important data before destroying.

```bash
cdk destroy
```

---

Copyright 2026 Amazon.com, Inc. or its affiliates. All Rights Reserved.

SPDX-License-Identifier: MIT-0
