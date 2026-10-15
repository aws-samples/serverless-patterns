# AWS Lambda Web Function behind Amazon CloudFront with Origin Access Control (CDK)

This pattern deploys an AWS Lambda Web Function that is reachable only through an Amazon CloudFront distribution, using the AWS Cloud Development Kit (AWS CDK) in TypeScript. The function's endpoint uses the `IamAuth` authentication type, so Lambda accepts only requests signed with AWS Signature Version 4. CloudFront signs every origin request through an Origin Access Control (OAC) of type `lambda`, and a resource policy on the function allows invocation only from that one distribution. Direct requests to the function's domain get `403 Forbidden` before they reach your code.

With CloudFront in front, you get edge caching, TLS termination at the edge, compression, a custom domain if you add one, and the option to attach AWS WAF. The application is a plain Node.js `http` server with no dependencies and no authentication code of its own.

Learn more about this pattern at Serverless Land Patterns: https://serverlessland.com/patterns/lambda-web-cloudfront-oac-nodejs-cdk

Important: this application uses various AWS services and there are costs associated with these services after the Free Tier usage - please see the [AWS Pricing page](https://aws.amazon.com/pricing/) for details. You are responsible for any AWS costs incurred. No warranty is implied in this example.

## Requirements

* [Create an AWS account](https://portal.aws.amazon.com/gp/aws/developer/registration/index.html) if you do not already have one and log in. The IAM user that you use must have sufficient permissions to make necessary AWS service calls and manage AWS resources.
* [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html) installed and configured
* [Git Installed](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)
* [Node.js](https://nodejs.org/) 24 or later installed
* [AWS CDK](https://docs.aws.amazon.com/cdk/v2/guide/getting_started.html) v2 CLI installed (`npm install -g aws-cdk`) and the target account and Region [bootstrapped](https://docs.aws.amazon.com/cdk/v2/guide/bootstrapping.html)

## Deployment Instructions

1. Create a new directory, navigate to that directory in a terminal and clone the GitHub repository:
    ```
    git clone https://github.com/aws-samples/serverless-patterns
    ```
1. Change directory to the pattern directory:
    ```
    cd serverless-patterns/lambda-web-cloudfront-oac/nodejs/cdk
    ```
1. Install the CDK app's dependencies:
    ```bash
    npm install
    ```
1. Bootstrap the account and Region if you have not used the CDK there before (one time):
    ```bash
    cdk bootstrap aws://<account-id>/us-east-1
    ```
1. Deploy the stack. The Region you deploy to is the Web Function's home Region; CloudFront itself is global:
    ```bash
    export AWS_REGION=us-east-1
    cdk deploy
    ```
    `cdk synth` and `cdk deploy` print warnings such as `Unknown resource type 'AWS::Lambda::WebFunction'` for the three Web Function resources. The CDK CLI's bundled validation rules are behind the CloudFormation registry; the deployment is not affected.

    The first deployment takes about five minutes, most of it waiting for the CloudFront distribution. The outputs include `CloudFrontUrl` (where to send requests) and `OriginUrl` (the function's own domain, which returns `403`). Later deployments that only change the application code take about one minute: CDK uploads a new zip, CloudFormation creates a new revision, moves the endpoint to it and deletes the old one.

### What the stack creates

`lib/lambda-web-cloudfront-oac-stack.ts` defines everything. There are no L2 constructs for Web Functions yet, so the function, revision, endpoint and resource policy use the generated L1 classes from `aws-cdk-lib/aws-lambda`:

| Construct | CloudFormation type | Purpose |
|---|---|---|
| `s3.Bucket` + `BucketDeployment` | `AWS::S3::Bucket`, `Custom::CDKBucketDeployment` | Versioning-enabled code bucket with a policy that lets `lambda.amazonaws.com` read objects; `src/` is uploaded as a single zip (`extract: false`) |
| `iam.Role` | `AWS::IAM::Role` | Execution role with `AWSLambdaBasicExecutionRole` (CloudWatch Logs only) |
| `logs.LogGroup` | `AWS::Logs::LogGroup` | `/aws/lambda/web/<stack-name>`, 1-week retention, deleted with the stack |
| `lambda.CfnWebFunction` | `AWS::Lambda::WebFunction` | The function |
| `lambda.CfnWebFunctionRevision` | `AWS::Lambda::WebFunctionRevision` | Immutable code + configuration (`nodejs24.x`, 30 s request timeout, bucket/key/version of the zip) |
| `lambda.CfnWebFunctionEndpoint` | `AWS::Lambda::WebFunctionEndpoint` | `IamAuth`, `HomeRegion`, 100% of traffic to the revision above |
| `cloudfront.CfnOriginAccessControl` | `AWS::CloudFront::OriginAccessControl` | Type `lambda`, SigV4, `always-amz-auth` |
| `cloudfront.CachePolicy` | `AWS::CloudFront::CachePolicy` | Path, query string and the viewer's `Authorization` header in the cache key, with the `CachingOptimized` TTLs and compression |
| `cloudfront.Distribution` + `HttpOrigin` | `AWS::CloudFront::Distribution` | The endpoint domain as an HTTPS-only custom origin with the OAC attached; the cache policy above and the managed `AllViewerExceptHostHeader` origin request policy |
| `lambda.CfnResourcePolicy` | `AWS::Lambda::ResourcePolicy` | Allows `lambda:InvokeWebFunctionEndpoint` for `cloudfront.amazonaws.com` when `AWS:SourceArn` is this distribution |

The endpoint is created as `IamAuth`, so there is no moment at which it is public. The resource policy references the distribution ID and the distribution references the endpoint domain, so CloudFormation orders them correctly without explicit dependencies.

## How it works

```
Viewer ──HTTPS──▶ CloudFront ──SigV4-signed HTTPS (OAC)──▶ Web Function endpoint (IamAuth) ──▶ your HTTP server
                                                           ▲
Direct request ──HTTPS (unsigned)──────────────────────────┘ 403 Forbidden
```

Three settings work together:

* **`IamAuth` on the endpoint.** Lambda validates a SigV4 signature on every request and returns `403` when it is missing or invalid. Your code never runs for those requests.
* **OAC of type `lambda` with `always-amz-auth`.** CloudFront signs each origin request with its own service credentials. The viewer's own `Authorization` header, if any, is preserved and forwarded to your application, because the cache policy includes it, so existing sign-in flows keep working. CloudFront rejects `SigningBehavior: always` for Web Function origins.
* **Resource policy with `AWS:SourceArn`.** The signature proves the caller is CloudFront; the policy decides which CloudFront distribution is allowed. Another distribution in any account, even one using the same OAC configuration, gets `403`.

After validating the signature, Lambda removes the `Authorization` header it used, so the application sees the request without CloudFront's credentials. The application exposes two routes:

| Path | Cache-Control | Purpose |
|---|---|---|
| `/` and `/cached` | `public, max-age=60` | Shows edge caching: repeat requests within 60 s are served by CloudFront without reaching the function |
| `/whoami` | `no-store` | Returns the serving Region, the execution environment id, whether the request came through CloudFront and the `CloudFront-*` headers CloudFront added |

The server reads its listen address from the `AWS_LAMBDA_HTTP_ENDPOINT` environment variable that the runtime sets (`0.0.0.0:3000`). When the variable is absent, it binds `127.0.0.1` for local development.

The distribution uses its own cache policy and the managed `AllViewerExceptHostHeader` origin request policy. The managed `CachingOptimized` cache policy leaves the query string and the `Authorization` header out of the cache key, and CloudFront forwards `Authorization` to the origin only when the cache policy includes it. The stack's cache policy keeps the `CachingOptimized` TTLs and compression, so CloudFront still honours the origin's `Cache-Control` headers, and adds both, so each signed-in viewer gets their own cache entries. `AllViewerExceptHostHeader` forwards the viewer's headers and query string but not the `Host` header. Lambda routes on `Host`, so the origin request must carry the endpoint domain, not the viewer's.

Code updates work through CloudFormation's replacement semantics. `BucketDeployment` names the zip after its content hash, so a code change produces a new S3 key and version ID. Every property of `AWS::Lambda::WebFunctionRevision` is create-only, so CloudFormation creates a new revision, updates the endpoint's `RevisionWeights` to point at it, and deletes the old revision once the update succeeds.

Two things this pattern does not do: it does not make the endpoint private at the network layer (the endpoint domain is still resolvable; it just denies unsigned requests), and it does not add a custom domain or AWS WAF. Both attach to the distribution in the usual way.

## Testing

### Run locally

```bash
cd src
npm start
curl http://127.0.0.1:3000/whoami
```

### On the deployed endpoints

Set the two URLs from the stack outputs:

```bash
export CLOUDFRONT_URL=$(aws cloudformation describe-stacks --stack-name lambda-web-cloudfront-oac-cdk \
  --query "Stacks[0].Outputs[?OutputKey=='CloudFrontUrl'].OutputValue" --output text)
export ORIGIN_URL=$(aws cloudformation describe-stacks --stack-name lambda-web-cloudfront-oac-cdk \
  --query "Stacks[0].Outputs[?OutputKey=='OriginUrl'].OutputValue" --output text)
```

Directly at the origin, the request is rejected before it reaches the application:

```bash
curl -s -o /dev/null -w '%{http_code}\n' "$ORIGIN_URL/whoami"
# 403
```

Through CloudFront, the request reaches the function. `viaCloudFront` is `true`, `authorizationHeaderPresent` is `false`, and the `cloudfront` object lists headers such as your viewer country:

```bash
curl -s "$CLOUDFRONT_URL/whoami"
```

Send your own `Authorization` header and the application receives it, while CloudFront's signature is still removed:

```bash
curl -s -H 'Authorization: Bearer example-token' "$CLOUDFRONT_URL/whoami" | grep authorizationHeaderPresent
#   "authorizationHeaderPresent": true,
```

Edge caching: the first request is a miss and later ones within 60 seconds are hits with the same `generatedAt` value:

```bash
for i in 1 2 3; do curl -si "$CLOUDFRONT_URL/cached" | grep -i 'x-cache\|generatedAt'; done
# x-cache: Miss from cloudfront
#   "generatedAt": "2026-10-14T08:25:05.983Z",
# x-cache: Hit from cloudfront
#   "generatedAt": "2026-10-14T08:25:05.983Z",
# ...
```

To see a code update roll out, edit the `message` string in `src/index.js` and run `cdk deploy` again. The endpoint keeps its domain and its `IamAuth` setting, the origin still returns `403`, and `curl "$CLOUDFRONT_URL/cached?v=2"` shows the new message, because the query string is part of the cache key.

To confirm that the policy ties the function to one distribution, create a second distribution with the same origin and OAC and request `/whoami` through it: it returns `403`. Disable and delete that distribution afterwards.

## Cleanup

1. Delete the stack. CloudFront needs the distribution disabled and fully deployed before it can be deleted, so this takes a few minutes. The code bucket is emptied (all object versions) and deleted automatically, and the stack's log group is deleted with it:
    ```bash
    cdk destroy
    ```
1. Delete the staging log group the service creates next to the stack's one. It is not part of the stack:
    ```bash
    aws logs delete-log-group --log-group-name /aws/lambda/web/lambda-web-cloudfront-oac-cdk.local
    ```

----
Copyright 2026 Amazon.com, Inc. or its affiliates. All Rights Reserved.

SPDX-License-Identifier: MIT-0
