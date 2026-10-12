# Express.js CRUD API on AWS Lambda Web Functions with DynamoDB (SAM)

This pattern deploys an unmodified Express.js 5 REST API as an AWS Lambda Web Function, backed by an Amazon DynamoDB table. Lambda Web Functions run a long-lived HTTP server and forward requests to it directly, so there is no adapter, no Lambda handler and no event-to-request mapping. The same `index.js` runs locally with `node index.js` and on AWS.

The API exposes `POST /items`, `GET /items/{id}`, `PUT /items/{id}` and `GET /items` (paginated), with 400/404/409 handling. A single `AWS::Serverless::WebFunction` resource creates the function, an immutable revision and a public HTTPS endpoint.

Learn more about this pattern at Serverless Land Patterns: << Add the live URL here >>

Important: this application uses various AWS services and there are costs associated with these services after the Free Tier usage - please see the [AWS Pricing page](https://aws.amazon.com/pricing/) for details. You are responsible for any AWS costs incurred. No warranty is implied in this example.

## Requirements

* [Create an AWS account](https://portal.aws.amazon.com/gp/aws/developer/registration/index.html) if you do not already have one and log in. The IAM user that you use must have sufficient permissions to make necessary AWS service calls and manage AWS resources.
* Latest [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html) installed and configured
* [Git Installed](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)
* [Node.js](https://nodejs.org/en/download/) 24 (matches the `nodejs24.x` runtime)
* [AWS Serverless Application Model](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-sam-cli-install.html) (AWS SAM) installed

## Deployment Instructions

1. Create a new directory, navigate to that directory in a terminal and clone the GitHub repository:
    ```
    git clone https://github.com/aws-samples/serverless-patterns
    ```
1. Change directory to the pattern directory:
    ```
    cd lambda-web-dynamodb-api/nodejs/sam
    ```
1. Create the code bucket (one time per account and Region). `AWS::Lambda::WebFunctionRevision` requires a **versioning-enabled** bucket, and the bucket policy must let the Lambda service read the code:
    ```bash
    export AWS_REGION=<< AWS Region >>
    export ACCOUNT_ID=$(aws sts get-caller-identity --query Account --output text)
    export BUCKET=lambda-web-sam-$ACCOUNT_ID-$AWS_REGION

    aws s3 mb s3://$BUCKET --region $AWS_REGION
    aws s3api put-bucket-versioning --bucket $BUCKET \
      --versioning-configuration Status=Enabled --region $AWS_REGION
    aws s3api put-bucket-policy --bucket $BUCKET --region $AWS_REGION --policy "{
      \"Version\": \"2012-10-17\",
      \"Statement\": [{
        \"Effect\": \"Allow\",
        \"Principal\": {\"Service\": \"lambda.amazonaws.com\"},
        \"Action\": [\"s3:GetObject\", \"s3:GetObjectVersion\"],
        \"Resource\": \"arn:aws:s3:::$BUCKET/*\",
        \"Condition\": {\"StringEquals\": {\"aws:SourceAccount\": \"$ACCOUNT_ID\"}}
      }]
    }"
    ```
1. Install production dependencies, package the application and upload it. `node_modules` must be inside the zip because there is no build step at deploy time:
    ```bash
    (cd src && npm install --omit=dev && zip -qr ../function.zip index.js package.json node_modules)
    aws s3 cp function.zip s3://$BUCKET/lambda-web-dynamodb-api-sam/function.zip --region $AWS_REGION
    ```
1. Deploy the stack, passing the bucket and key of the uploaded code:
    ```bash
    sam deploy \
      --stack-name lambda-web-dynamodb-api-sam \
      --capabilities CAPABILITY_IAM \
      --region $AWS_REGION \
      --resolve-s3 \
      --parameter-overrides \
        CodeBucket=$BUCKET \
        CodeKey=lambda-web-dynamodb-api-sam/function.zip
    ```
    Once you have run `sam deploy` once and saved arguments to a configuration file (`samconfig.toml`), you can use `sam deploy` in future to use these defaults.
1. Note the `EndpointDomainName` and `TableName` outputs. The endpoint can take a couple of minutes to become `Active` on a first deploy.

## How it works

* `src/index.js` is a plain Express 5 app wrapped in `http.createServer`. It listens on the address in the `AWS_LAMBDA_HTTP_ENDPOINT` environment variable, which the runtime sets to `0.0.0.0:3000` and probes for readiness; when the variable is absent (local development) it falls back to the same value.
* The DynamoDB `DocumentClient` is created once per sandbox and reused across the many concurrent requests one sandbox serves. Credentials come from the function's execution role; no keys are configured in code.
* Routes:
  * `POST /items` writes the item with `attribute_not_exists(id)`, so a duplicate `id` returns **409**; missing `id` or `name` returns **400**.
  * `GET /items/{id}` returns the item or **404**.
  * `PUT /items/{id}` updates `name`, `description` and/or `metadata` with `attribute_exists(id)`, so an unknown id returns **404**.
  * `GET /items?limit=20&lastKey=<url-encoded JSON>` scans the table with cursor pagination (`limit` is capped at 100).
  * Every response includes the Region that served it (`servedFrom`, `createdIn`, `updatedIn`). Deploy the same code behind a `MultiRegion` endpoint with a DynamoDB global table and these fields show which Region handled each call.
* `template.yaml`:
  * `ItemsTable` is an on-demand DynamoDB table keyed by `id`. Its generated name is passed to the app as `TABLE_NAME`.
  * `WebFunctionRole` is defined explicitly so it can carry `AWSLambdaBasicExecutionRole` (CloudWatch Logs) plus `GetItem`, `PutItem`, `UpdateItem` and `Scan` scoped to the table ARN.
  * The single `AWS::Serverless::WebFunction` expands into `AWS::Lambda::WebFunction`, `AWS::Lambda::WebFunctionRevision` (immutable code + configuration) and `AWS::Lambda::WebFunctionEndpoint` (HTTPS endpoint routed 100% to that revision).
* `AuthType: ApplicationManaged` means the endpoint is **public: anyone with the URL can reach it**. This sample has no authentication of its own; add it before exposing real data, or change to `AuthType: IamAuth` to accept only SigV4-signed requests (sign with service name `lambda`).

Key runtime constraints:

* Runtime is `nodejs24.x`; the code uses ESM (`"type": "module"` in `package.json`).
* The entry point is `index.js` at the zip root, with `node_modules` next to it.
* Bind the host and port from `AWS_LAMBDA_HTTP_ENDPOINT`. A hardcoded port that does not match it fails the readiness probe.

To deploy a code change, upload the zip under a **new key** (for example `function-v2.zip`) and deploy again with the new `CodeKey`. CloudFormation only creates a new revision when the revision's properties change, so re-deploying with an unchanged key reports "No changes to deploy".

## Testing

Run the app locally first against the deployed table. The same code runs unchanged on AWS:

```bash
cd src && npm install
export TABLE_NAME=$(aws cloudformation describe-stacks \
  --stack-name lambda-web-dynamodb-api-sam --region $AWS_REGION \
  --query "Stacks[0].Outputs[?OutputKey=='TableName'].OutputValue" --output text)
node index.js
# Express API listening on 0.0.0.0:3000 (table: ..., region: ...)
```

After deployment, exercise the API through the endpoint:

```bash
ENDPOINT=$(aws cloudformation describe-stacks \
  --stack-name lambda-web-dynamodb-api-sam \
  --region $AWS_REGION \
  --query "Stacks[0].Outputs[?OutputKey=='EndpointDomainName'].OutputValue" \
  --output text)

# Create -> 201
curl -s -X POST https://$ENDPOINT/items \
  -H 'Content-Type: application/json' \
  -d '{"id":"item-1","name":"First item","description":"created via the pattern"}'
# {"item":{"id":"item-1","name":"First item","description":"created via the pattern","metadata":{},"createdAt":"...","updatedAt":"...","createdInRegion":"us-east-1"},"createdIn":"us-east-1"}

# Duplicate -> 409
curl -s -X POST https://$ENDPOINT/items -H 'Content-Type: application/json' -d '{"id":"item-1","name":"x"}'
# {"error":"Item already exists","id":"item-1"}

# Read -> 200
curl -s https://$ENDPOINT/items/item-1

# Update -> 200
curl -s -X PUT https://$ENDPOINT/items/item-1 -H 'Content-Type: application/json' -d '{"description":"updated"}'

# List -> 200 (paginated)
curl -s "https://$ENDPOINT/items?limit=5"
# {"items":[...],"count":1,"servedFrom":"us-east-1"}

# Unknown id -> 404
curl -s https://$ENDPOINT/items/missing
# {"error":"Item not found","id":"missing"}
```

View the request log written by the sandboxes:

```bash
aws logs tail /aws/lambda/web/lambda-web-dynamodb-api-sam --region $AWS_REGION --follow
# POST /items 201 978ms
# GET /items/item-1 200 117ms
```

## Cleanup

1. Delete the stack. This also deletes the DynamoDB table **and all items in it**:
    ```bash
    sam delete --stack-name lambda-web-dynamodb-api-sam --region $AWS_REGION
    ```
1. Empty and delete the code bucket. Versioning is enabled, so every object version and delete marker must be removed first:
    ```bash
    aws s3api list-object-versions --bucket $BUCKET --region $AWS_REGION \
      --query '[Versions,DeleteMarkers][][].[Key,VersionId]' --output text \
      | while read -r key version; do
          aws s3api delete-object --bucket $BUCKET --region $AWS_REGION \
            --key "$key" --version-id "$version"
        done
    aws s3 rb s3://$BUCKET --region $AWS_REGION
    ```

----
Copyright 2026 Amazon.com, Inc. or its affiliates. All Rights Reserved.

SPDX-License-Identifier: MIT-0
