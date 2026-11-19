# AWS AppSync to Amazon Aurora Serverless v2 via the RDS Data API (zero AWS Lambda)

This pattern deploys an AWS AppSync GraphQL API that reads and writes an Amazon Aurora Serverless v2 (PostgreSQL) database directly through the RDS Data API, with no AWS Lambda functions in the request path. AWS AppSync runs JavaScript (APPSYNC_JS) resolvers that issue parameterised SQL over the RDS Data API's HTTPS endpoint, so there is no VPC-attached compute layer to manage.

Learn more about this pattern at Serverless Land Patterns: https://serverlessland.com/patterns/appsync-aurora-serverless-v2-rds-data-api-cdk

Important: this application uses various AWS services and there are costs associated with these services after the Free Tier usage - please see the [AWS Pricing page](https://aws.amazon.com/pricing/) for details. You are responsible for any AWS costs incurred. No warranty is implied in this example.

## Requirements

* [Create an AWS account](https://portal.aws.amazon.com/gp/aws/developer/registration/index.html) if you do not already have one and log in. The IAM user that you use must have sufficient permissions to make necessary AWS service calls and manage AWS resources.
* [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html) installed and configured
* [Git installed](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)
* [Node.js 20+](https://nodejs.org/en/download/) installed
* [AWS Cloud Development Kit](https://docs.aws.amazon.com/cdk/v2/guide/getting_started.html) (AWS CDK) v2 installed
* An AWS account [bootstrapped for AWS CDK](https://docs.aws.amazon.com/cdk/v2/guide/bootstrapping.html)

## Deployment Instructions

1. Create a new directory, navigate to that directory in a terminal and clone the GitHub repository:
    ```
    git clone https://github.com/aws-samples/serverless-patterns
    ```
2. Change directory to the pattern directory:
    ```
    cd serverless-patterns/appsync-aurora-serverless-v2-rds-data-api-cdk/cdk
    ```
3. Install dependencies:
    ```
    npm install
    ```
4. Deploy the stack to your default AWS account and region:
    ```
    npx cdk deploy
    ```
5. Note the outputs from the AWS CDK deployment process. They contain the GraphQL endpoint URL, the API key, the API ID, and the Amazon Aurora Serverless v2 cluster and secret ARNs used for testing.

## How it works

AWS AppSync exposes a GraphQL schema with a `listTodos` query and a `createTodo` mutation. Both fields are wired to an RDS Data API data source rather than to an AWS Lambda function. When a request arrives, AWS AppSync runs a JavaScript resolver that builds a parameterised SQL statement and sends it to the Amazon Aurora Serverless v2 cluster over the RDS Data API. The Data API authenticates using a generated credential in AWS Secrets Manager and returns the result set, which the resolver maps back into the GraphQL response shape.

Each service is load-bearing. AWS AppSync terminates the GraphQL request and runs the resolver. The RDS Data API turns that resolver into an HTTPS SQL call, which is what removes the need for an AWS Lambda function or a VPC-attached compute layer. Amazon Aurora Serverless v2 is the relational store that scales capacity down when idle and holds the data the resolvers query. Removing any one of the three breaks the architecture.

## Architecture

```
GraphQL client
      |
      v
AWS AppSync GraphQL API  (API key auth, APPSYNC_JS resolvers)
      |
      | RDS Data API data source (HTTPS, no AWS Lambda, no VPC compute)
      v
Amazon Aurora Serverless v2  (PostgreSQL, Data API enabled, encrypted at rest)
      ^
      |  admin credential
AWS Secrets Manager
```

## Testing

The database starts empty. Before the first query, create the `todos` table using the RDS Data API from your terminal (this uses the cluster and secret ARNs shown in the stack outputs). Replace `<ClusterArn>` and `<ClusterSecretArn>` with the deployment output values and set your region:

```
aws rds-data execute-statement \
  --resource-arn "<ClusterArn>" \
  --secret-arn "<ClusterSecretArn>" \
  --database "appsyncdemo" \
  --sql "CREATE TABLE IF NOT EXISTS todos (id SERIAL PRIMARY KEY, title TEXT NOT NULL, completed BOOLEAN NOT NULL DEFAULT false);" \
  --region "<region>"
```

1. Create a todo through the GraphQL API. Replace `<GraphQLApiUrl>` and `<GraphQLApiKey>` with the stack output values:

    ```
    curl -X POST "<GraphQLApiUrl>" \
      -H "Content-Type: application/json" \
      -H "x-api-key: <GraphQLApiKey>" \
      -d '{"query":"mutation { createTodo(title: \"Try the RDS Data API\") { id title completed } }"}'
    ```

    Expected response (the `id` will vary):

    ```json
    {"data":{"createTodo":{"id":"1","title":"Try the RDS Data API","completed":false}}}
    ```

2. List todos through the GraphQL API to confirm the row round-tripped from Amazon Aurora Serverless v2:

    ```
    curl -X POST "<GraphQLApiUrl>" \
      -H "Content-Type: application/json" \
      -H "x-api-key: <GraphQLApiKey>" \
      -d '{"query":"query { listTodos { id title completed } }"}'
    ```

    Expected response:

    ```json
    {"data":{"listTodos":[{"id":"1","title":"Try the RDS Data API","completed":false}]}}
    ```

The round trip proves the headline behaviour: a GraphQL request served straight from a relational database through the RDS Data API, with no AWS Lambda function involved.

## Cleanup

1. Delete the stack from the `cdk` directory:
    ```
    npx cdk destroy
    ```
2. Confirm the stack has been deleted:
    ```
    aws cloudformation list-stacks --query "StackSummaries[?contains(StackName,'AppSyncAuroraServerlessStack')].StackStatus"
    ```

Warning: `npx cdk destroy` removes the Amazon Aurora Serverless v2 cluster and all data it contains. The cluster is configured with `RemovalPolicy.DESTROY` for this sample so cleanup leaves nothing behind and stops incurring charges. Do not use this removal policy for production data.

----
Copyright 2026 Amazon.com, Inc. or its affiliates. All Rights Reserved.

SPDX-License-Identifier: MIT-0
