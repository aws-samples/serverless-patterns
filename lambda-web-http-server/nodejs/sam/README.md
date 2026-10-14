# Node.js HTTP server on AWS Lambda Web Functions (SAM)

This pattern deploys the smallest possible Lambda Web Function: a Node.js server built with the standard `http` module and no dependencies, exposed through a public HTTPS endpoint. Lambda Web Functions run a long-lived HTTP server (Express, Hono, Next.js, or plain `http.createServer`) and forward requests to it directly. There is no handler, no event object and no response mapping: the same `index.js` runs locally with `node index.js` and on AWS without changes.

The app tracks how many requests each execution environment is serving at the same time and returns those counters in every response, which makes the multi-request concurrency model visible.

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
    cd lambda-web-http-server/nodejs/sam
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
1. Package the application and upload it. The runtime loads `index.js` from the root of the zip; this app has no dependencies, so there is no `node_modules` to bundle:
    ```bash
    (cd src && zip -r ../function.zip index.js package.json)
    aws s3 cp function.zip s3://$BUCKET/lambda-web-http-server-sam/function.zip --region $AWS_REGION
    ```
1. Deploy the stack, passing the bucket and key of the uploaded code:
    ```bash
    sam deploy \
      --stack-name lambda-web-http-server-sam \
      --capabilities CAPABILITY_IAM \
      --region $AWS_REGION \
      --resolve-s3 \
      --parameter-overrides \
        CodeBucket=$BUCKET \
        CodeKey=lambda-web-http-server-sam/function.zip
    ```
    Once you have run `sam deploy` once and saved arguments to a configuration file (`samconfig.toml`), you can use `sam deploy` in future to use these defaults.
1. Note the `EndpointDomainName` output. The endpoint can take a couple of minutes to become `Active` on a first deploy.

## How it works

* `src/index.js` creates a server with `http.createServer` and listens on the address in the `AWS_LAMBDA_HTTP_ENDPOINT` environment variable. The Lambda Web Functions runtime sets it to `0.0.0.0:3000` and probes that address for readiness; when the variable is absent (local development) the app falls back to the same value. `PORT` and `HOSTNAME` are **not** set by the runtime.
* Each execution environment handles many concurrent requests on one Node.js process. The app keeps three in-memory counters (`currentConcurrency`, `peakConcurrency`, `totalRequests`) and adds a 100 ms artificial delay so that parallel requests overlap and the counters grow. Counters are per execution environment: a second execution environment starts from zero.
* The single `AWS::Serverless::WebFunction` in `template.yaml` expands into three CloudFormation resources:
  * `AWS::Lambda::WebFunction`: the function itself
  * `AWS::Lambda::WebFunctionRevision`: an immutable snapshot of code + configuration
  * `AWS::Lambda::WebFunctionEndpoint`: the HTTPS endpoint, routed 100% to that revision
* `ExecutionRoleArn` is omitted, so SAM generates an execution role with `AWSLambdaBasicExecutionRole` (CloudWatch Logs). `LoggingConfig.LogGroup` names the log group the execution environments write to.
* `AuthType: ApplicationManaged` means the endpoint is **public: anyone with the URL can reach it**. The application must implement its own authentication, input validation and rate limiting. Change to `AuthType: IamAuth` to accept only SigV4-signed requests (sign with service name `lambda`).
* `AutoDeploymentMode: LatestRevision` routes traffic to the newest revision automatically. For manual, weighted routing between two revisions set `AutoDeploymentMode: Disabled` and `RevisionWeights`.
* On `SIGTERM` the server stops accepting connections and exits once in-flight requests finish.

Key runtime constraints:

* Runtime is `nodejs24.x`; the code uses ESM (`"type": "module"` in `package.json`).
* The entry point is `index.js` at the zip root. To use another file (for example `server.ts`, which Node 24 runs directly) set the `EntryPoint` property on the SAM resource.
* Bind the host and port from `AWS_LAMBDA_HTTP_ENDPOINT`. A hardcoded port that does not match it fails the readiness probe and the revision never becomes `Active`.

To deploy a code change, upload the zip under a **new key** (for example `function-v2.zip`) and deploy again with the new `CodeKey`. CloudFormation only creates a new revision when the revision's properties change, so re-deploying with an unchanged key reports "No changes to deploy".

## Testing

Run the app locally first. The same code runs unchanged on AWS:

```bash
cd src
node index.js
# Lambda function listening on 0.0.0.0:3000
curl -s http://localhost:3000/ | head -20
```

After deployment, read the endpoint domain from the stack outputs and send a request:

```bash
ENDPOINT=$(aws cloudformation describe-stacks \
  --stack-name lambda-web-http-server-sam \
  --region $AWS_REGION \
  --query "Stacks[0].Outputs[?OutputKey=='EndpointDomainName'].OutputValue" \
  --output text)

curl -s https://$ENDPOINT/hello
```

Expected response (values vary):

```json
{
  "message": "Answered at 2026-09-29T15:15:08.150Z",
  "timestamp": "2026-09-29T15:15:08.150Z",
  "requestMethod": "GET",
  "requestUrl": "/hello",
  "requestUserAgent": "curl/8.7.1",
  "requestBodyLength": 0,
  "workingDirectory": "/var/task",
  "concurrencyMetrics": {
    "currentConcurrency": 1,
    "peakConcurrency": 1,
    "activeAtResponse": 0,
    "totalRequests": 1,
    "processingTimeMs": 101
  }
}
```

Send 20 requests in parallel and watch `peakConcurrency` rise, which shows several requests being served by the same execution environment at once:

```bash
seq 20 | xargs -P 20 -I{} curl -s https://$ENDPOINT/ -o /dev/null
curl -s https://$ENDPOINT/ | grep -E 'peakConcurrency|totalRequests'
```

View the logs written by the execution environments:

```bash
aws logs tail /aws/lambda/web/lambda-web-http-server-sam --region $AWS_REGION --follow
```

## Cleanup

1. Delete the stack:
    ```bash
    sam delete --stack-name lambda-web-http-server-sam --region $AWS_REGION
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
