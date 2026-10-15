# AWS Lambda Web Function behind Amazon CloudFront with Origin Access Control (SAM)

This pattern deploys an AWS Lambda Web Function that is reachable only through an Amazon CloudFront distribution, all from one AWS SAM template. The function's endpoint uses the `IamAuth` authentication type, so Lambda accepts only requests signed with AWS Signature Version 4. CloudFront signs every origin request through an Origin Access Control (OAC) of type `lambda`, and a resource policy on the function allows invocation only from that one distribution. Direct requests to the function's domain get `403 Forbidden` before they reach your code.

With CloudFront in front, you get edge caching, TLS termination at the edge, compression, a custom domain if you add one, and the option to attach AWS WAF. The application is a plain Node.js `http` server with no dependencies and no authentication code of its own.

Learn more about this pattern at Serverless Land Patterns: https://serverlessland.com/patterns/lambda-web-cloudfront-oac-nodejs-sam

Important: this application uses various AWS services and there are costs associated with these services after the Free Tier usage - please see the [AWS Pricing page](https://aws.amazon.com/pricing/) for details. You are responsible for any AWS costs incurred. No warranty is implied in this example.

## Requirements

* [Create an AWS account](https://portal.aws.amazon.com/gp/aws/developer/registration/index.html) if you do not already have one and log in. The IAM user that you use must have sufficient permissions to make necessary AWS service calls and manage AWS resources.
* Latest [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html) installed and configured
* [Git Installed](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)
* [Node.js](https://nodejs.org/) 24 or later installed (matches the `nodejs24.x` runtime)
* [AWS Serverless Application Model](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-sam-cli-install.html) (AWS SAM) installed

## Deployment Instructions

1. Create a new directory, navigate to that directory in a terminal and clone the GitHub repository:
    ```
    git clone https://github.com/aws-samples/serverless-patterns
    ```
1. Change directory to the pattern directory:
    ```
    cd serverless-patterns/lambda-web-cloudfront-oac/nodejs/sam
    ```
1. Create the code bucket (one time per account and Region). `AWS::Lambda::WebFunctionRevision` requires a **versioning-enabled** bucket, and the bucket policy must let the Lambda service read the code:
    ```bash
    export AWS_REGION=us-east-1
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
    aws s3 cp function.zip s3://$BUCKET/lambda-web-cloudfront-oac-sam/function.zip --region $AWS_REGION
    ```
1. Deploy the stack, passing the bucket and key of the uploaded code. The same bucket also holds the packaged template, so SAM does not need to create a managed bucket of its own:
    ```bash
    sam deploy \
      --stack-name lambda-web-cloudfront-oac-sam \
      --capabilities CAPABILITY_IAM \
      --region $AWS_REGION \
      --s3-bucket $BUCKET \
      --s3-prefix lambda-web-cloudfront-oac-sam/sam-artifacts \
      --parameter-overrides \
        CodeBucket=$BUCKET \
        CodeKey=lambda-web-cloudfront-oac-sam/function.zip
    ```
    The stack takes about 4 minutes, most of it waiting for the CloudFront distribution to deploy. Once you have run `sam deploy` once and saved arguments to a configuration file (`samconfig.toml`), you can use `sam deploy` in future to use these defaults.
1. Note the `CloudFrontUrl` and `OriginUrl` outputs. From the moment the endpoint exists it only accepts signed requests; it is never public.

To deploy a code change, upload the zip under a **new key** (for example `function-v2.zip`) and deploy again with the new `CodeKey`. CloudFormation creates a new revision, moves the endpoint to it and deletes the old one; the endpoint keeps its domain, its `IamAuth` setting and its resource policy, so nothing changes on the CloudFront side.

## How it works

```
Viewer ──HTTPS──▶ CloudFront ──SigV4-signed HTTPS (OAC)──▶ Web Function endpoint (IamAuth) ──▶ your HTTP server
                                                           ▲
Direct request ──HTTPS (unsigned)──────────────────────────┘ 403 Forbidden
```

`template.yaml` declares five resources:

* **`WebFunction`** (`AWS::Serverless::WebFunction`) with `AuthType: IamAuth`, `EndpointType: HomeRegion` and `EndpointName: dev`. SAM expands it into `AWS::Lambda::WebFunction`, an immutable `AWS::Lambda::WebFunctionRevision` (code + configuration) and an `AWS::Lambda::WebFunctionEndpoint` routed 100% to that revision, plus a logs-only execution role (`WebFunctionRole`) because `ExecutionRoleArn` is not set. The generated logical IDs are `WebFunctionRevision` and `WebFunctionEndpoint`, which is how the other resources reference the endpoint's `DomainName` and `EndpointArn`.
* **`OriginAccessControl`** (`AWS::CloudFront::OriginAccessControl`) with `OriginAccessControlOriginType: lambda`, `SigningProtocol: sigv4` and `SigningBehavior: always-amz-auth`. CloudFront rejects `always` for Web Function origins.
* **`CachePolicy`** (`AWS::CloudFront::CachePolicy`) with the path, the query string and the viewer's `Authorization` header in the cache key. The managed `CachingOptimized` policy leaves the last two out, and CloudFront forwards `Authorization` to the origin only when the cache policy includes it. It keeps the `CachingOptimized` TTLs and compression, so CloudFront still honours the origin's `Cache-Control` headers, and each signed-in viewer gets their own cache entries.
* **`Distribution`** (`AWS::CloudFront::Distribution`) with the endpoint domain as an HTTPS-only custom origin and the OAC attached to it. It uses the cache policy above and the managed `AllViewerExceptHostHeader` origin request policy, which forwards the viewer's headers and query string but not the `Host` header. Lambda routes on `Host`, so the origin request must carry the endpoint domain, not the viewer's. CloudFront is a global service, but the distribution is created from the stack's Region like any other resource.
* **`EndpointResourcePolicy`** (`AWS::Lambda::ResourcePolicy`) attached to the function (`ResourceArn` is the web-function ARN). It allows `lambda:InvokeWebFunctionEndpoint` on the `dev` endpoint for the `cloudfront.amazonaws.com` service principal, with an `AWS:SourceArn` condition naming this stack's distribution.

Three settings work together:

* **`IamAuth` on the endpoint.** Lambda validates a SigV4 signature on every request and returns `403` when it is missing or invalid. Your code never runs for those requests.
* **OAC of type `lambda` with `always-amz-auth`.** CloudFront signs each origin request with its own service credentials. The viewer's own `Authorization` header, if any, is preserved and forwarded to your application, because the cache policy includes it, so existing sign-in flows keep working.
* **Resource policy with `AWS:SourceArn`.** The signature proves the caller is CloudFront; the policy decides which CloudFront distribution is allowed. Another distribution in any account, even one using the same OAC configuration, gets `403`.

After validating the signature, Lambda removes the `Authorization` header it used, so the application sees the request without CloudFront's credentials. The application exposes two routes:

| Path | Cache-Control | Purpose |
|---|---|---|
| `/` and `/cached` | `public, max-age=60` | Shows edge caching: repeat requests within 60 s are served by CloudFront without reaching the function |
| `/whoami` | `no-store` | Returns the serving Region, the execution environment id, whether the request came through CloudFront and the `CloudFront-*` headers CloudFront added |

The server reads its listen address from the `AWS_LAMBDA_HTTP_ENDPOINT` environment variable that the runtime sets (`0.0.0.0:3000`). When the variable is absent, it binds `127.0.0.1` for local development.

Two things this pattern does not do: it does not make the endpoint private at the network layer (the endpoint domain is still resolvable; it just denies unsigned requests), and it does not add a custom domain or AWS WAF. Both attach to the distribution in the usual way.

## Testing

### Run locally

```bash
cd src
npm start
curl http://127.0.0.1:3000/whoami
```

### On the deployed endpoints

Read the two URLs from the stack outputs:

```bash
export CLOUDFRONT_URL=$(aws cloudformation describe-stacks --stack-name lambda-web-cloudfront-oac-sam \
  --region $AWS_REGION --query "Stacks[0].Outputs[?OutputKey=='CloudFrontUrl'].OutputValue" --output text)
export ORIGIN_URL=$(aws cloudformation describe-stacks --stack-name lambda-web-cloudfront-oac-sam \
  --region $AWS_REGION --query "Stacks[0].Outputs[?OutputKey=='OriginUrl'].OutputValue" --output text)
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

```json
{
  "generatedAt": "2026-10-14T08:19:31.074Z",
  "region": "us-east-1",
  "instanceId": "62cc1f75",
  "viaCloudFront": true,
  "authorizationHeaderPresent": false,
  "cloudfront": {
    "cloudfront-viewer-country": "NL",
    "cloudfront-viewer-city": "Amsterdam",
    "cloudfront-is-mobile-viewer": "false",
    "cloudfront-is-desktop-viewer": "true",
    "cloudfront-forwarded-proto": "https",
    "via": "2.0 e2b2960acb3b050648b3477a3e78810e.cloudfront.net (CloudFront)",
    "x-amz-cf-id": "V0WgrFhIBruF08hcIXhQJpZNKjPpml0qTQ9g3MTxPKHdN2C2k9V3lQ=="
  }
}
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
#   "generatedAt": "2026-10-14T08:19:38.524Z",
# x-cache: Hit from cloudfront
#   "generatedAt": "2026-10-14T08:19:38.524Z",
# ...
```

To confirm that the policy ties the function to one distribution, create a second distribution with the same origin and OAC and request `/whoami` through it: it returns `403`. Disable and delete that distribution afterwards.

View the logs written by the execution environments:

```bash
aws logs tail /aws/lambda/web/lambda-web-cloudfront-oac-sam --region $AWS_REGION --follow
```

## Cleanup

1. Delete the stack. CloudFormation disables the distribution, waits for it to deploy and then deletes it, so this takes a few minutes. The function, its endpoint, revision and resource policy, the OAC and the execution role go with it:
    ```bash
    sam delete --stack-name lambda-web-cloudfront-oac-sam --region $AWS_REGION --no-prompts
    ```
1. Delete the log groups the runtime created:
    ```bash
    aws logs delete-log-group --log-group-name /aws/lambda/web/lambda-web-cloudfront-oac-sam --region $AWS_REGION
    aws logs delete-log-group --log-group-name /aws/lambda/web/lambda-web-cloudfront-oac-sam.local --region $AWS_REGION
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
