# Amazon API Gateway to AWS Step Functions Express to Amazon Athena (synchronous, zero AWS Lambda)

Run an Amazon Athena query and return its rows in a single synchronous Amazon API Gateway request through an AWS Step Functions Express Workflow, using zero AWS Lambda functions.

This pattern is implemented with the AWS Cloud Development Kit (AWS CDK) in TypeScript.

Learn more about this pattern at Serverless Land Patterns: https://serverlessland.com/patterns/apigw-sfn-express-athena-cdk

Important: this application uses various AWS services and there are costs associated with these services after the Free Tier usage - please see the [AWS Pricing page](https://aws.amazon.com/pricing/) for details. You are responsible for any AWS costs incurred. No warranty is implied in this example.

## Architecture

A client sends an HTTP `POST` to an Amazon API Gateway REST API with a JSON body containing an Amazon Athena SQL `queryString`. Amazon API Gateway invokes an AWS Step Functions Express Workflow with `StartSyncExecution`, so the HTTP call blocks until the workflow completes and returns its output in the same response.

The Express Workflow uses only native AWS Step Functions service integrations (no AWS Lambda). Because Express Workflows do not support the `.sync` (RUN_JOB) integration pattern, the workflow starts the query and then polls it to completion:

1. `AthenaStartQueryExecution` with the `REQUEST_RESPONSE` integration pattern starts the query against an AWS Glue database and table and returns immediately with a query execution ID.
2. A `Wait` state pauses, then `GetQueryExecution` reads the query status and a `Choice` state loops back to `Wait` until the query reaches `SUCCEEDED` (or fails).
3. `AthenaGetQueryResults` reads the completed query's result rows.

A final `Pass` state shapes the response down to the Amazon Athena result rows, which flow back through AWS Step Functions and Amazon API Gateway to the caller.

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
  v
Amazon Athena  --(AWS Glue table)-->  Amazon S3  (data/ read, athena-results/ write)
  |
  v
Rows returned synchronously to the client
```

Because every Amazon Athena call is a native AWS Step Functions service integration, there are no AWS Lambda functions anywhere in this pattern.

## Requirements

* [Create an AWS account](https://portal.aws.amazon.com/gp/aws/developer/registration/index.html) if you do not already have one and log in. The IAM user that you use must have sufficient permissions to make necessary AWS service calls and manage AWS resources.
* [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html) installed and configured
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
5. Note the `ApiEndpoint` value from the stack outputs. You will use it for testing.

## Testing

The headline of this pattern is that a single synchronous HTTP call returns Amazon Athena result rows, with no AWS Lambda in the path.

After deployment, send a `POST` to the `ApiEndpoint` output with an Amazon Athena SQL query in the body. Replace `<ApiEndpoint>` with your stack output:

```
curl -X POST '<ApiEndpoint>' \
  -H 'Content-Type: application/json' \
  -d '{"queryString": "SELECT customer, SUM(amount) AS total FROM orders GROUP BY customer ORDER BY total DESC"}'
```

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
