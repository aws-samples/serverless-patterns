# Amazon API Gateway to AWS Step Functions Express to Amazon Athena (synchronous, no AWS Lambda in the request path)

Run an Amazon Athena query and return its rows in a single synchronous Amazon API Gateway request through an AWS Step Functions Express Workflow, with no AWS Lambda functions in the request path.

This pattern is implemented with the AWS Cloud Development Kit (AWS CDK) in TypeScript.

Learn more about this pattern at Serverless Land Patterns: https://serverlessland.com/patterns/apigw-sfn-express-athena-cdk

Important: this application uses various AWS services and there are costs associated with these services after the Free Tier usage - please see the [AWS Pricing page](https://aws.amazon.com/pricing/) for details. You are responsible for any AWS costs incurred. No warranty is implied in this example.

## Architecture

A client sends an HTTP `POST` to an Amazon API Gateway REST API with a JSON body containing an Amazon Athena SQL `queryString`. Amazon API Gateway invokes an AWS Step Functions Express Workflow with `StartSyncExecution`, so the HTTP call blocks until the workflow completes and returns its output in the same response.

The Express Workflow uses only native AWS Step Functions service integrations (no AWS Lambda in the request path). Because Express Workflows do not support the `.sync` (RUN_JOB) integration pattern, the workflow starts the query and then polls it to completion:

1. `AthenaStartQueryExecution` with the `REQUEST_RESPONSE` integration pattern starts the query against an AWS Glue database and table and returns immediately with a query execution ID.
2. A `Wait` state pauses, then `GetQueryExecution` reads the query status and a `Choice` state loops back to `Wait` until the query reaches `SUCCEEDED`. If the query reports `FAILED` or `CANCELLED`, the workflow ends in a `Fail` state.
3. `AthenaGetQueryResults` reads the completed query's result rows.

A final `Pass` state shapes the response down to the Amazon Athena result rows, which flow back through AWS Step Functions and Amazon API Gateway to the caller.

If the query fails or is cancelled, or if any of the three Amazon Athena tasks fails, the workflow ends in a `Fail` state. A request that Amazon Athena rejects as invalid, such as a SQL syntax error, is not retried; other task errors are retried up to three times first. A request body without `queryString` also fails the execution (`States.Runtime`). The execution status is then `FAILED`, and the response template that `StepFunctionsRestApi` generates returns HTTP 500 with `error` and `cause` fields. The generated template inserts those two values into the body as they are, without JSON escaping, so a `cause` that contains double quotes or line breaks (for example an Amazon Athena error message) can make the 500 body invalid JSON. Treat the 500 body as diagnostic text rather than parsing it as JSON, or customize the integration response if your clients need strict JSON.

Amazon Athena reads a sample CSV dataset stored in Amazon S3 (`data/` prefix) via an AWS Glue external table whose schema is declared in AWS CDK, and writes query results to a separate `athena-results/` prefix in the same Amazon S3 bucket. An Amazon Athena workgroup pins the result location and enforces server-side encryption.

```
Client
  |  POST { "queryString": "SELECT ..." }
  v
Amazon API Gateway (REST)
  |  states:StartSyncExecution
  v
AWS Step Functions Express Workflow
  |  AthenaStartQueryExecution (REQUEST_RESPONSE)
  |    --> Wait --> GetQueryExecution --> Choice(status) --loop until SUCCEEDED-->
  |    --> AthenaGetQueryResults --> FormatResponse
  |  (query FAILED or CANCELLED, or an Athena task error --> Fail state --> HTTP 500)
  v
Amazon Athena  --(AWS Glue table)-->  Amazon S3  (data/ read, athena-results/ write)
  |
  v
Rows returned synchronously to the client
```

Because every Amazon Athena call is a native AWS Step Functions service integration, there are no AWS Lambda functions in the request path. (The stack does deploy two small AWS CDK helper functions at deploy time: one behind the `AwsCustomResource` that seeds the sample CSV, and one that empties the bucket on `cdk destroy`.)

### Access control

The Amazon API Gateway method uses AWS IAM authorization, so requests must be signed with AWS Signature Version 4 by a principal that is allowed `execute-api:Invoke` on the API. The caller's `queryString` is passed straight to Amazon Athena, so an open endpoint would let anyone with the URL run queries and drive scan cost. The `prod` stage also applies stage-level throttling (5 requests per second, burst of 10) to all methods. Adjust both for your own workload.

### Limits

* **29 second timeout.** The API is edge-optimized (the `RestApi` default), where the integration timeout is 29 seconds and cannot be raised ([API Gateway quotas](https://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-execution-service-limits-table.html)). A query has to finish inside that window; the sample dataset does. If it takes longer, the caller receives a 504 while the workflow keeps running (its own timeout is 60 seconds) and the Amazon Athena query is not stopped.
* **Result size.** Rows travel back in the execution output and the `StartSyncExecution` response, which are capped at 256 KiB ([Step Functions quotas](https://docs.aws.amazon.com/step-functions/latest/dg/service-quotas.html)), and `GetQueryResults` returns at most 1000 rows per call ([GetQueryResults](https://docs.aws.amazon.com/athena/latest/APIReference/API_GetQueryResults.html)). This pattern does not paginate, so a larger result set is truncated to the first page or fails with `States.DataLimitExceeded`, which a `States.ALL` catcher cannot catch ([error handling](https://docs.aws.amazon.com/step-functions/latest/dg/concepts-error-handling.html)). To handle large results, return the result file location (`$.queryStatus.QueryExecution.ResultConfiguration.OutputLocation`) instead of the rows.
* **Logging.** The state machine logs at level `ALL` with execution data included, so the caller's SQL and the result rows are written to Amazon CloudWatch Logs on every request. Turn `includeExecutionData` off if you copy this pattern for sensitive data.

## Requirements

* [Create an AWS account](https://portal.aws.amazon.com/gp/aws/developer/registration/index.html) if you do not already have one and log in. The IAM user that you use must have sufficient permissions to make necessary AWS service calls and manage AWS resources.
* [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html) version 2 installed and configured
* [curl](https://curl.se/) 7.75.0 or newer, used to send the SigV4-signed test request
* [Git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git) installed
* [Node.js 18+](https://nodejs.org/en/download/) installed
* [AWS Cloud Development Kit (AWS CDK) v2](https://docs.aws.amazon.com/cdk/v2/guide/getting_started.html) installed
* An AWS account bootstrapped for the AWS CDK (`cdk bootstrap`)

## Deployment Instructions

1. Create a new directory, navigate to that directory in a terminal and clone the GitHub repository:
    ```
    git clone https://github.com/aws-samples/serverless-patterns
    ```
2. Change directory to the pattern directory:
    ```
    cd apigw-sfn-express-athena-cdk/cdk
    ```
3. Install dependencies:
    ```
    npm install
    ```
4. Deploy the stack to your default AWS account and region:
    ```
    npx cdk deploy
    ```
5. Note the `ApiEndpoint` value from the stack outputs. You will use it for testing. The stack also outputs `DataBucketName`, `AthenaWorkgroupName` and `GlueDatabaseName`, which are useful for looking at the sample data and query results in the Amazon Athena console.

## Testing

The headline of this pattern is that a single synchronous HTTP call returns Amazon Athena result rows, with no AWS Lambda in the request path.

After deployment, send a SigV4-signed `POST` to the `ApiEndpoint` output with an Amazon Athena SQL query in the body. The method uses AWS IAM authorization, so an unsigned request is rejected.

`curl --aws-sigv4` needs curl 7.75.0 or newer. Load temporary credentials from your configured AWS CLI profile into environment variables of the current shell (this does not print them), then replace `<ApiEndpoint>` with your stack output and `<region>` with the Region you deployed to:

```
eval "$(aws configure export-credentials --format env)"

curl -X POST '<ApiEndpoint>' \
  --aws-sigv4 'aws:amz:<region>:execute-api' \
  --user "$AWS_ACCESS_KEY_ID:$AWS_SECRET_ACCESS_KEY" \
  -H "x-amz-security-token: $AWS_SESSION_TOKEN" \
  -H 'Content-Type: application/json' \
  -d '{"queryString": "SELECT customer, SUM(amount) AS total FROM orders GROUP BY customer ORDER BY total DESC LIMIT 2"}'
```

If your credentials are long-term access keys without a session token, omit the `x-amz-security-token` header.

The response returns synchronously in the same call and contains the Amazon Athena result rows, for example:

```json
{
  "rows": [
    { "Data": [ { "VarCharValue": "customer" }, { "VarCharValue": "total" } ] },
    { "Data": [ { "VarCharValue": "Initech" }, { "VarCharValue": "499.75" } ] },
    { "Data": [ { "VarCharValue": "Umbrella" }, { "VarCharValue": "359.88" } ] }
  ]
}
```

The first row is the column header. This proves the full Amazon API Gateway -> AWS Step Functions Express -> Amazon Athena query-and-return round trip completed in one request/response.

You can query any column of the sample `orders` table (`order_id`, `customer`, `product`, `quantity`, `amount`, `order_date`).

If a query fails (for example a syntax error or an unknown table), the call returns HTTP 500 with `error` and `cause` fields (passed through as is and not JSON-escaped, so the body may not be valid JSON). To investigate a failed query or an error response, open the Amazon CloudWatch Logs log group that the stack creates for the state machine (its name contains `StateMachineLogGroup`). It logs every execution at level `ALL` with execution data, including the Amazon Athena query status and the failure reason.

## Cleanup

1. Delete the stack:
    ```
    cd apigw-sfn-express-athena-cdk/cdk
    npx cdk destroy
    ```

   Warning: `cdk destroy` deletes the Amazon S3 bucket and ALL of its contents, including the sample dataset and every Amazon Athena query result written during testing. The bucket is configured with `RemovalPolicy.DESTROY` and auto-delete so the pattern cleans up fully. Do not store data you want to keep in this bucket.

----
Copyright 2026 Amazon.com, Inc. or its affiliates. All Rights Reserved.

SPDX-License-Identifier: MIT-0
