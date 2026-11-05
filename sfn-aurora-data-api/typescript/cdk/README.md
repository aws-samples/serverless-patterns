# AWS Step Functions to Amazon Aurora Serverless v2 with Amazon RDS Data API transactions

This pattern deploys an AWS Step Functions state machine that runs one SQL unit of work (an order row, a guarded stock decrement and an audit row) as a single transaction on Amazon Aurora Serverless v2 (PostgreSQL) through the Amazon RDS Data API: BeginTransaction, three ExecuteStatement calls, then CommitTransaction, or RollbackTransaction when a step fails. No AWS Lambda function is in the request path.

Learn more about this pattern at Serverless Land Patterns: https://serverlessland.com/patterns/sfn-aurora-data-api-typescript-cdk

Important: this application uses various AWS services and there are costs associated with these services after the Free Tier usage - please see the [AWS Pricing page](https://aws.amazon.com/pricing/) for details. You are responsible for any AWS costs incurred. No warranty is implied in this example.

## Requirements

* [Create an AWS account](https://portal.aws.amazon.com/gp/aws/developer/registration/index.html) if you do not already have one and log in. The IAM user that you use must have sufficient permissions to make necessary AWS service calls and manage AWS resources.
* [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html) installed and configured. The Testing commands were written for AWS CLI 2.31.3. Your principal also needs `rds-data:ExecuteStatement` on the cluster and `secretsmanager:GetSecretValue` on the secret to run the SQL checks.
* [Node.js 22 or later](https://nodejs.org/en/download/) installed
* [AWS CDK v2](https://docs.aws.amazon.com/cdk/v2/guide/getting_started.html) and an account and Region [bootstrapped](https://docs.aws.amazon.com/cdk/v2/guide/bootstrapping.html) for it
* [Git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git) installed
* The stack deploys to the Region that the CDK resolves from your environment (`AWS_REGION` or the Region of your AWS CLI profile). Run the Testing commands in that Region, for example `export AWS_REGION=us-west-2` (and `AWS_PROFILE` if you use a named profile).

## Supported Regions

Deployed and tested in us-west-2 only. The [Data API Regions page](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/Concepts.Aurora_Fea_Regions_DB-eng.Feature.Data_API.html) lists the Regions and engine versions that support the Data API (check it for yours), and scale to 0 ACUs needs Aurora PostgreSQL 17.4 or higher ([capacity table](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/aurora-serverless-v2.how-it-works.html#aurora-serverless-v2.how-it-works.capacity)). The stack uses engine version 17.7 (offered in us-west-2 with a minimum of 0 ACUs, according to `aws rds describe-db-engine-versions`) and contains no Region-specific value; check that the version is offered in your Region before you deploy there.

## Architecture

```
Execution input {"sku": "SKU-100", "quantity": 2}
      |
      v
AWS Step Functions (Standard, JSONata)
  EnsureSchema -> BeginTransaction -> InsertOrder -> DecrementStock -> StockReserved? -> InsertAudit -> CommitTransaction -> OrderCommitted
  (any error in InsertOrder, DecrementStock, InsertAudit or CommitTransaction, or no stock, goes to:)
  RollbackTransaction -> OrderRolledBack (Fail state with error and cause)
      |
      | AWS SDK integration (IAM)
      v
Amazon RDS Data API --> Amazon Aurora Serverless v2 PostgreSQL (private isolated subnets, no inbound rules)
                    --> AWS Secrets Manager (cluster secret, read with the caller's permissions)
```

## How it works

1. EnsureSchema runs four idempotent statements outside the transaction (three `CREATE TABLE IF NOT EXISTS` and one seed row, `SKU-100` with 5 units) and keeps the order id, SKU and quantity in workflow variables.
2. BeginTransaction returns a transaction id, stored in a workflow variable.
3. InsertOrder, DecrementStock and InsertAudit pass that id and use named SQL parameters. DecrementStock only updates a row when `stock >= quantity`; StockReserved reads the update count and treats zero rows as "not enough stock".
4. CommitTransaction ends the execution in OrderCommitted.
5. A statement error, or zero updated rows, goes to RollbackTransaction with the same transaction id and ends in the OrderRolledBack Fail state with the error and cause.

## Important Notes

* The Data API ends a transaction that no call uses for three minutes and caps it at one hour, according to the [BeginTransaction](https://docs.aws.amazon.com/rdsdataservice/latest/APIReference/API_BeginTransaction.html) reference (not tested here). The state machine does not roll back when an execution is stopped or times out outside a Catch; the Data API does it after the idle period, and row locks stay held until then.
* The cluster scales to 0 ACUs and pauses after 5 minutes without connections. AWS documents about 15 seconds to resume, longer after a day paused ([auto-pause](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/aurora-serverless-v2-auto-pause.html)). The first call after a pause fails with `RdsData.DatabaseResumingException` ("is resuming after being auto-paused"), so the first database calls retry that error up to 6 times; in a test the first execution after a pause succeeded after the retry and took 17 seconds, and later executions took about 1.5 seconds. Failed statements are never retried.
* The stock check reads `NumberOfRecordsUpdated` with `$exists`, so a response without that field counts as zero rows. If RollbackTransaction itself fails (for example the transaction already expired, or a Commit that succeeded only lost its response), the execution fails with that error instead of the original one, and you should check the table state (by design; a failing CommitTransaction was not tested). After a failed PostgreSQL statement (Testing step 4) the Data API still accepted the rollback, so `error` and `cause` hold the database error.
* The cluster has the Data API HTTP endpoint enabled, and its security group has no inbound rule. Access to the database goes through IAM (`rds-data` actions plus `secretsmanager:GetSecretValue`), not through the network. The state machine connects as the master user `postgres`, whose generated credentials are in the secret and are not rotated; use a scoped database user and rotation for anything real.
* The workflow does not validate its input: send `sku` (a string) and `quantity` (an integer) as in the Testing examples. The order id is the execution name, which is a UUID unless you pass `--name`.
* EnsureSchema runs on every execution so that nobody runs DDL by hand. That is acceptable for a demo that runs one execution at a time; use a migration tool for a real schema.
* Every SDK call has a 60 second `TimeoutSeconds`, because SDK integrations have none by default. The Data API response limit is 1 MiB.
* IAM: the state machine role gets the four `rds-data` transaction actions on this cluster and `secretsmanager:GetSecretValue` on this secret, because the Data API reads the secret with the caller's permissions. CDK derives the wrong IAM prefix for `rdsdata`, so the stack passes `iamAction` explicitly.
* Execution input and output are not written to the state machine log group (`ERROR` level) because they hold order values and SQL parameters. Error messages are, and a database error message can quote values. Use the execution history as in Testing.
* Use a single statement or a stored procedure instead when all statements fit in one call; a Data API transaction only exists across separate calls, which is what the state machine holds together.

## Deployment Instructions

1. Clone the repository:
    ```bash
    git clone https://github.com/aws-samples/serverless-patterns
    cd serverless-patterns/sfn-aurora-data-api/typescript/cdk
    ```

2. Install dependencies and build:
    ```bash
    npm install
    npm run build
    ```

3. Bootstrap CDK once per account and Region, then deploy (creating the Aurora cluster takes several minutes):
    ```bash
    npx cdk bootstrap
    npx cdk deploy
    ```

## Testing

1. Define helpers. Run this block again in any new terminal; it only defines helpers and starts nothing:
    ```bash
    out() { aws cloudformation describe-stacks --stack-name SfnAuroraDataApiStack --query "Stacks[0].Outputs[?OutputKey=='$1'].OutputValue" --output text; }
    SM=$(out StateMachineArn); CLUSTER=$(out ClusterArn); SECRET=$(out SecretArn); DB=$(out DatabaseName)
    run() { ARN=$(aws stepfunctions start-execution --state-machine-arn "$SM" --input "$1" --query executionArn --output text)
      while [ "$(aws stepfunctions describe-execution --execution-arn "$ARN" --query status --output text)" = "RUNNING" ]; do sleep 3; done
      aws stepfunctions describe-execution --execution-arn "$ARN" --query '{status:status,output:output,error:error,cause:cause}'; }
    state() { aws rds-data execute-statement --resource-arn "$CLUSTER" --secret-arn "$SECRET" --database "$DB" --format-records-as JSON --output text --query formattedRecords \
      --sql "SELECT (SELECT stock FROM inventory WHERE sku = 'SKU-100') AS stock, (SELECT count(*) FROM orders) AS orders, (SELECT count(*) FROM audit) AS audit"; }
    ```

2. Commit path. Order 2 of 5 units. The counts below are for a freshly deployed stack, so run steps 2 to 4 once and in order:
    ```bash
    run '{"sku": "SKU-100", "quantity": 2}'
    state
    ```
   Expected: status `SUCCEEDED` and an output like `{"orderId":"<uuid>","status":"COMMITTED"}`, then `[{"stock":3,"orders":1,"audit":1}]`. If the cluster had paused, this first run takes about 17 seconds (see Important Notes).

3. Rollback path. Order 10 when 3 are left:
    ```bash
    run '{"sku": "SKU-100", "quantity": 10}'
    aws stepfunctions get-execution-history --execution-arn "$ARN" --query "events[?ends_with(type,'StateEntered')].stateEnteredEventDetails.name" --output text | tr '\t' '\n'
    state
    ```
   Expected: status `FAILED`, error `InsufficientStock` and the cause `No row updated: SKU SKU-100 is unknown or has fewer than 10 units`. The history lists EnsureSchema, four RunDdlStatement entries, BeginTransaction, InsertOrder, DecrementStock, StockReserved, StockUnavailable, RollbackTransaction and OrderRolledBack, and no InsertAudit or CommitTransaction. The counts are still `[{"stock":3,"orders":1,"audit":1}]`, which means the order row that InsertOrder inserted inside the transaction was rolled back.

4. Database error path (the Catch). A quantity of 0 breaks the `CHECK (quantity > 0)` on `orders`, an unknown SKU breaks its foreign key:
    ```bash
    run '{"sku": "SKU-100", "quantity": 0}'
    run '{"sku": "SKU-999", "quantity": 1}'
    state
    ```
   Expected: both `FAILED` with error `RdsData.DatabaseErrorException`, and the counts unchanged. The causes are `ERROR: new row for relation "orders" violates check constraint "orders_quantity_check"; SQLState: 23514 ...` and `ERROR: insert or update on table "orders" violates foreign key constraint "orders_sku_fkey"; SQLState: 23503 ...`.

5. If an execution fails before any of the above (for example an IAM error), read the log group named by the `StateMachineLogGroupName` output:
    ```bash
    aws logs tail "$(out StateMachineLogGroupName)" --since 30m
    ```

## Cleanup

1. Delete the stack. This deletes the Aurora cluster without a final snapshot, the tables and all data in them, the log group and the secret:
    ```bash
    npx cdk destroy
    ```
2. Nothing is created outside the stack. In a test, `aws secretsmanager list-secrets --include-planned-deletion` showed no secret from the stack after `cdk destroy`; check it in your account.

----
Copyright 2026 Amazon.com, Inc. or its affiliates. All Rights Reserved.

SPDX-License-Identifier: MIT-0
