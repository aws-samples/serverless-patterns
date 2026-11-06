# Amazon API Gateway direct integration with Amazon DynamoDB bulk put items

This pattern deploys an Amazon API Gateway REST API that starts and monitors an Amazon DynamoDB bulk put items operation, which loads data files from Amazon S3 into a DynamoDB table. API Gateway calls the DynamoDB API directly through an AWS service integration (`StartBulkPutItems` and `DescribeBulkOperation`) with mapping templates, so no AWS Lambda function is in the request path. Callers sign requests with AWS Identity and Access Management (IAM) credentials (SigV4).

Learn more about this pattern at Serverless Land Patterns: https://serverlessland.com/patterns/apigw-dynamodb-bulk-put-typescript-cdk

Important: this application uses various AWS services and there are costs associated with these services after the Free Tier usage - please see the [AWS Pricing page](https://aws.amazon.com/pricing/) for details. You are responsible for any AWS costs incurred. No warranty is implied in this example.

## Requirements

* [Create an AWS account](https://portal.aws.amazon.com/gp/aws/developer/registration/index.html) if you do not already have one and log in. The IAM user that you use must have sufficient permissions to make necessary AWS service calls and manage AWS resources.
* [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html) installed and configured. The Testing commands use `aws configure export-credentials`, which needs AWS CLI v2. Your principal needs `execute-api:Invoke` on the API, plus the AWS CloudFormation, Amazon S3 and DynamoDB read and write permissions that the Testing commands use.
* [curl](https://curl.se/) 7.75 or later, for the `--aws-sigv4` option, and bash or zsh with `sed` and `gunzip` for the Testing commands
* [Node.js 22 or later](https://nodejs.org/en/download/) installed
* [AWS CDK v2](https://docs.aws.amazon.com/cdk/v2/guide/getting_started.html) and an account and Region [bootstrapped](https://docs.aws.amazon.com/cdk/v2/guide/bootstrapping.html) for it
* [Git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git) installed
* The stack deploys to the Region that the CDK resolves from your environment (`AWS_REGION` or the Region of your AWS CLI profile). Run the Testing commands in that Region, for example `export AWS_REGION=us-west-2` (and `AWS_PROFILE` if you use a named profile).

## Supported Regions

Deployed and tested in us-west-2 only. According to the launch announcement, the Standard tier is available in all commercial AWS Regions and the AWS GovCloud (US) Regions; check the [bulk put items documentation](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/BulkPutItems.HowItWorks.html) and the [launch announcement](https://aws.amazon.com/about-aws/whats-new/2026/11/amazon-dynamodb-now-supports-bulk-put-items/) for the Regions that support it.

## Architecture

```
POST /operations {"prefix": "daily/"}          GET /operations/{operationId}
        |                                               |
        v                                               v
Amazon API Gateway REST API (IAM authorization, resource policy, stage throttling, request validation)
        |  AWS service integration with mapping templates, using the API role
        v
Amazon DynamoDB: StartBulkPutItems / DescribeBulkOperation (one bulk put items operation)
        |
        +-- reads  --> Amazon S3 bucket, input/daily/ (DynamoDB JSON files)
        +-- writes --> Amazon DynamoDB table (the items)
        +-- writes --> Amazon S3 bucket, reports/ (ERROR and CONDITION_CHECK_FAILURE records)
```

## How it works

1. `POST /operations` with `{"prefix": "daily/"}` is validated against a JSON schema model. The mapping template builds the `StartBulkPutItems` request: the table and bucket of this stack, the key prefix `input/daily/`, the `DYNAMODB_JSON` format, no compression, and a report location under `reports/` for `ERROR` and `CONDITION_CHECK_FAILURE` records. The API request id is the client token. The response is reduced to `operationId` and `status`.
2. DynamoDB reads the files under that prefix and writes each item to the table. A record can carry its own `ConditionExpression`; a record whose condition fails is skipped and listed in the `CONDITION_CHECK_FAILURE` report.
3. `GET /operations/{operationId}` calls `DescribeBulkOperation` and returns `status`, `processedItemCount`, `failedItemCount` and `failureCode`.

## Important Notes

* **Not production-ready.** Any caller with `execute-api:Invoke` on the API can start a bulk put from the files under `input/` into this table. The API has IAM authorization, a resource policy that denies other accounts and stage throttling (5 requests per second, burst of 10), but no AWS WAF, no custom domain and no per-caller limit. `GET /operations/{operationId}` can describe any bulk operation of this account in this Region, because the operation id is not known when the role is created. The API has no access logging (that needs the account-wide API Gateway role for Amazon CloudWatch Logs, which this stack does not create) and no alarms. According to the [documentation](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/BulkPutItems.Considerations.html), AWS CloudTrail records the `StartBulkOperation` call, and DynamoDB can write some records a second time after an internal failover, so put a version guard in the condition expression of every record if your application writes the same keys while an operation runs. Add your own authorization model, input checks and monitoring before real use.
* **One operation per table at a time.** Starting a second operation while one was running returned HTTP 400 with `Table has ongoing bulk operations, please wait and try again`. According to the documentation, starts that arrive at nearly the same time can each get an operation id, and one of them later ends `FAILED` with `ResourceInUseException` (not tested). There is no cancel route and the role has no cancel action, so an operation that was started with the wrong prefix runs to the end.
* **Duration.** For the three sample records an operation took between about 45 seconds and 3.5 minutes in four tests, so poll with `GET /operations/{operationId}`. Do not change the input objects while it runs ([documentation](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/BulkPutItems.Requesting.html)).
* **A failed condition is not a failed item.** In the test a record whose condition failed was skipped and listed in the `CONDITION_CHECK_FAILURE` report, and the operation ended `COMPLETED` with `failedItemCount` 0. `processedItemCount` counted the 3 records that were read, while 2 items reached the table. According to the [documentation](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/BulkPutItems.Requesting.html), records that fail for other reasons are counted in `failedItemCount`, listed in the `ERROR` report, and the status is `COMPLETED_WITH_ERRORS` (not exercised in this test).
* **IAM.** The IAM actions are named after the bulk operation, not after the API calls ([IAM permissions](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/BulkPutItems.Considerations.html)): `dynamodb:StartBulkOperation` and `dynamodb:DescribeBulkOperation` on `bulk-operation/*`, `dynamodb:BulkPutItems` on the table, `s3:ListBucket` on the bucket (limited to the `input/*` prefix), `s3:GetObject` on `input/*`, and `s3:PutObject` and `s3:AbortMultipartUpload` on `reports/*`. The role has no cancel or list action because no route uses them. The mapping template adds the `input/` prefix to the caller's prefix, and a request model limits the prefix to letters, digits and `/ _ . = -`.
* **No condition on the role's trust policy.** With an `aws:SourceAccount` condition, API Gateway failed every call with `API Gateway does not have permission to assume the provided role`, so the trust policy names only the service principal (an `aws:SourceArn` condition was not tried).
* **Encryption.** The table uses the AWS managed key for DynamoDB and the bucket uses Amazon S3 managed keys and requires TLS. The operation worked with the AWS managed key without any AWS KMS permission on the role.
* **Client token.** The API request id is the client token, so a client that retries a timed-out call is expected to start a new operation instead of getting the first one back (not tested).
* **No AWS Lambda function in the request path.** The stack still contains the AWS CDK helper function that empties the bucket on `cdk destroy` (`autoDeleteObjects`).
* Input format, quotas and the report layout are in the [bulk put items documentation](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/BulkPutItems.HowItWorks.html). Bulk put items has its own pricing: see the [Amazon DynamoDB pricing page](https://aws.amazon.com/dynamodb/pricing/).

## Deployment Instructions

1. Clone the repository:
    ```bash
    git clone https://github.com/aws-samples/serverless-patterns
    cd serverless-patterns/apigw-dynamodb-bulk-put/typescript/cdk
    ```

2. Install dependencies and build:
    ```bash
    npm install
    npm run build
    ```

3. Bootstrap CDK once per account and Region, then deploy:
    ```bash
    npx cdk bootstrap
    npx cdk deploy
    ```

## Testing

1. Define helpers. Run this block again in any new terminal, and again when the exported credentials expire (`ExpiredToken`); it only defines helpers and starts nothing. `curl --user` puts the secret key on the command line, where other users of the machine can see it, so use a scratch machine or session:
    ```bash
    out() { aws cloudformation describe-stacks --stack-name ApigwDynamodbBulkPutStack --query "Stacks[0].Outputs[?OutputKey=='$1'].OutputValue" --output text; }
    API=$(out ApiUrl); BUCKET=$(out BucketName); TABLE=$(out TableName)
    REGION=${AWS_REGION:-${AWS_DEFAULT_REGION:-$(aws configure get region)}}
    eval "$(aws configure export-credentials --format env)"
    sigv4() { curl -s --aws-sigv4 "aws:amz:${REGION}:execute-api" --user "$AWS_ACCESS_KEY_ID:$AWS_SECRET_ACCESS_KEY" -H "x-amz-security-token: $AWS_SESSION_TOKEN" "$@"; echo; }
    ```

2. Upload the sample input. It has three records: an unconditional put, a put that only inserts (`attribute_not_exists(id)`), and a put whose condition cannot be met on an empty table (`attribute_exists(id)`):
    ```bash
    aws s3 cp events/items.jsonl s3://$BUCKET/input/daily/items.jsonl
    ```

3. Start the operation for the files under `input/daily/`:
    ```bash
    RESP=$(sigv4 -X POST "${API}operations" -H 'content-type: application/json' -d '{"prefix": "daily/"}'); echo "$RESP"
    OP=$(echo "$RESP" | sed -n 's/.*"operationId": "\([^"]*\)".*/\1/p')
    ```
   Expected: `{"operationId": "<id>", "status": "IN_PROGRESS"}`.

4. Wait for the operation to finish, then read its outcome. If `OP` is empty, step 3 did not start an operation (read its output), and in a new terminal set `OP` again to the `operationId` that step 3 printed:
    ```bash
    until [ "$(sigv4 "${API}operations/$OP" | sed -n 's/.*"status": "\([^"]*\)".*/\1/p')" != "IN_PROGRESS" ]; do sleep 10; done
    sigv4 "${API}operations/$OP"
    ```
   Expected: `"status": "COMPLETED"`, `"processedItemCount": 3`, `"failedItemCount": 0` and an empty `failureCode`. This took between 45 seconds and 3.5 minutes in four tests.

5. Read the table. This is an independent read, not the API's answer:
    ```bash
    aws dynamodb scan --table-name $TABLE --query 'Items[].[id.S,name.S,price.N]' --output text
    ```
   Expected, in any order: `item-1`, `Widget A`, `9.99` and `item-2`, `Widget B`, `14.99`. `item-3` is not there because its condition `attribute_exists(id)` was not met.

6. Read the condition check failure report that DynamoDB wrote to the bucket:
    ```bash
    KEY=$(aws s3api list-objects-v2 --bucket $BUCKET --prefix reports/ --query "Contents[?contains(Key,'condition-check-failures')].Key | [0]" --output text)
    aws s3 cp "s3://$BUCKET/$KEY" - | gunzip
    ```
   Expected: one record for `item-3` with `"itemIndex":2` and the message `The conditional request failed`. The step reads the first condition check failure report in the bucket, so run steps 2 to 6 once and in order on a freshly deployed stack.

7. Negative cases: an unsigned request, a body without `prefix`, a prefix with a character that the model does not allow, and an unknown operation id:
    ```bash
    curl -s -w ' HTTP %{http_code}\n' -X POST "${API}operations" -H 'content-type: application/json' -d '{"prefix": "daily/"}'
    sigv4 -w ' HTTP %{http_code}' -X POST "${API}operations" -H 'content-type: application/json' -d '{}'
    sigv4 -w ' HTTP %{http_code}' -X POST "${API}operations" -H 'content-type: application/json' -d '{"prefix": "a\"b"}'
    sigv4 -w ' HTTP %{http_code}' "${API}operations/does-not-exist"
    ```
   Expected, in this order: `{"message":"Missing Authentication Token"} HTTP 403`, two times `{"message": "Invalid request body"} HTTP 400`, and `{"message": "Invalid Request: Bulk operation ARN is invalid."} HTTP 400`.

## Cleanup

1. Delete the stack. This deletes the table with its items and the bucket with its input files and reports:
    ```bash
    npx cdk destroy
    ```

2. The log group of the AWS CDK helper function that empties the bucket (`autoDeleteObjects`) stayed behind after `cdk destroy` in a test. Find it, and delete it if you no longer need it:
    ```bash
    LG=$(aws logs describe-log-groups --log-group-name-prefix /aws/lambda/ApigwDynamodbBulkPutStack-CustomS3AutoDeleteObject --query 'logGroups[0].logGroupName' --output text); echo "$LG"
    aws logs delete-log-group --log-group-name "$LG"
    ```

3. Confirm the stack has been deleted:
    ```bash
    aws cloudformation describe-stacks --stack-name ApigwDynamodbBulkPutStack
    ```
    Expected: an error that the stack does not exist.

----
Copyright 2026 Amazon.com, Inc. or its affiliates. All Rights Reserved.

SPDX-License-Identifier: MIT-0
