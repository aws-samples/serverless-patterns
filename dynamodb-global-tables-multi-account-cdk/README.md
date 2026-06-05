# Amazon DynamoDB Global Tables — True Multi-Account Replication

This pattern deploys a DynamoDB Global Table that replicates data across two separate AWS accounts using `TableV2MultiAccountReplica`. Writes in Account A are automatically replicated to Account B with sub-second latency.

Learn more about this pattern at Serverless Land Patterns: https://serverlessland.com/patterns/dynamodb-global-tables-multi-account-cdk

Important: this application uses various AWS services and there are costs associated with these services after the Free Tier usage - please see the [AWS Pricing page](https://aws.amazon.com/pricing/) for details.

## Requirements

* [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html) installed and configured
* [AWS CDK](https://docs.aws.amazon.com/cdk/latest/guide/cli.html) installed (v2.252.0+)
* [Node.js](https://nodejs.org/en/download/) 20.x or later
* Two AWS accounts with credentials configured
* CDK bootstrapped in both accounts/regions

## Architecture

```
┌─────────────────────────────────┐         ┌─────────────────────────────────┐
│  Account A (742460038667)        │         │  Account B (843577947854)        │
│  us-east-1                       │         │  us-west-2                       │
│                                  │         │                                  │
│  ┌───────────────────────────┐  │  auto   │  ┌───────────────────────────┐  │
│  │ DynamoDB GlobalTable       │──┼────────▶│  │ DynamoDB Replica (CFN)     │  │
│  │ MultiAccountGlobalTable    │  │ replicate │ MultiAccountGlobalTable    │  │
│  └───────────────────────────┘  │         │  └───────────────────────────┘  │
│                                  │         │                                  │
│  Source Stack                    │         │  Replica Stack                   │
└─────────────────────────────────┘         └─────────────────────────────────┘
```

## How it works

1. **Source Stack** (Account A): Creates a DynamoDB Global Table with on-demand billing and point-in-time recovery
2. **Replica Stack** (Account B): Uses `TableV2MultiAccountReplica` to join the Global Table as a replica in a different account and region
3. DynamoDB automatically handles replication — writes in either account propagate to the other with sub-second latency
4. CDK automatically configures the resource policies needed for cross-account replication

**Note:** The replica must be in a different region from the source. This is a DynamoDB Global Tables requirement.

## Deployment Instructions

1. Clone and install:
    ```bash
    cd serverless-patterns/dynamodb-global-tables-multi-account-cdk
    npm install
    ```

2. Bootstrap CDK in both accounts (if not already done):
    ```bash
    npx cdk bootstrap aws://ACCOUNT_A/us-east-1 --profile source-profile
    npx cdk bootstrap aws://ACCOUNT_B/us-west-2 --profile replica-profile
    ```

3. Deploy the source stack first:
    ```bash
    npx cdk deploy DynamoDbMultiAccountSourceStack \
      -c sourceAccount=ACCOUNT_A \
      -c sourceRegion=us-east-1 \
      -c replicaAccount=ACCOUNT_B \
      -c replicaRegion=us-west-2 \
      --profile source-profile
    ```

4. Deploy the replica stack:
    ```bash
    npx cdk deploy DynamoDbMultiAccountReplicaStack \
      -c sourceAccount=ACCOUNT_A \
      -c sourceRegion=us-east-1 \
      -c replicaAccount=ACCOUNT_B \
      -c replicaRegion=us-west-2 \
      --profile replica-profile
    ```

## Testing

```bash
# Write an item in Account A (source)
aws dynamodb put-item \
  --table-name MultiAccountGlobalTable \
  --item '{"PK":{"S":"user#123"},"SK":{"S":"profile"},"name":{"S":"test"}}' \
  --region us-east-1 --profile source-profile

# Read the item from Account B (replica) — should appear within ~1 second
aws dynamodb get-item \
  --table-name MultiAccountGlobalTable \
  --key '{"PK":{"S":"user#123"},"SK":{"S":"profile"}}' \
  --region us-west-2 --profile replica-profile
```

## Cleanup

Destroy in reverse order:
```bash
npx cdk destroy DynamoDbMultiAccountReplicaStack \
  -c sourceAccount=ACCOUNT_A -c sourceRegion=us-east-1 \
  -c replicaAccount=ACCOUNT_B -c replicaRegion=us-west-2 \
  --profile replica-profile

npx cdk destroy DynamoDbMultiAccountSourceStack \
  -c sourceAccount=ACCOUNT_A -c sourceRegion=us-east-1 \
  -c replicaAccount=ACCOUNT_B -c replicaRegion=us-west-2 \
  --profile source-profile
```

---

Copyright 2026 Amazon.com, Inc. or its affiliates. All Rights Reserved.

SPDX-License-Identifier: MIT-0
