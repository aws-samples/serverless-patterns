# AWS Lambda Web Function behind Amazon CloudFront with Origin Access Control

This pattern deploys an AWS Lambda Web Function that is reachable only through an Amazon CloudFront distribution. The function's endpoint uses the `IamAuth` authentication type, so Lambda accepts only requests signed with AWS Signature Version 4. CloudFront signs every origin request through an Origin Access Control (OAC) of type `lambda`, and a resource policy on the function allows invocation only from that one distribution. Direct requests to the function's domain get `403 Forbidden` before they reach your code.

With CloudFront in front, you get edge caching, TLS termination at the edge, compression, a custom domain if you add one, and the option to attach AWS WAF. The application is a plain Node.js `http` server with no dependencies and no authentication code of its own.

Learn more about this pattern at Serverless Land Patterns: https://serverlessland.com/patterns/lambda-web-cloudfront-oac-nodejs-awscli

Important: this application uses various AWS services and there are costs associated with these services after the Free Tier usage - please see the [AWS Pricing page](https://aws.amazon.com/pricing/) for details. You are responsible for any AWS costs incurred. No warranty is implied in this example.

## Requirements

* [Create an AWS account](https://portal.aws.amazon.com/gp/aws/developer/registration/index.html) if you do not already have one and log in. The IAM user that you use must have sufficient permissions to make necessary AWS service calls and manage AWS resources.
* [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html) installed and configured (latest version, with the `aws lambda-web` commands)
* [Git Installed](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)
* [Node.js](https://nodejs.org/) 24 or later installed

## Deployment Instructions

1. Create a new directory, navigate to that directory in a terminal and clone the GitHub repository:
    ```
    git clone https://github.com/aws-samples/serverless-patterns
    ```
1. Change directory to the pattern directory:
    ```
    cd serverless-patterns/lambda-web-cloudfront-oac/nodejs/awscli
    ```
1. Set your Region (the Web Function's home Region; CloudFront itself is global) and run the deploy script:
    ```bash
    export AWS_REGION=us-east-1
    ./deploy.sh
    ```
    The script takes a few minutes, most of it waiting for the distribution to deploy. It prints the CloudFront URL and the origin URL when it finishes. Re-running it is safe: each step checks whether its resource already exists, and a code change becomes a new revision.

The script runs these steps. You can run them one at a time instead:

1. Deploy the Web Function with an `IamAuth` endpoint. The AWS CLI packages the `src` folder, and creates the function, a logs-only execution role, a versioned artifact bucket and an endpoint named `dev`:
    ```bash
    aws lambda-web deploy --name lambda-web-cloudfront-oac --code src --auth-type IamAuth --create
    ```
    From this moment the endpoint rejects unsigned requests. It is never public.
1. Create a cache policy. The managed `CachingOptimized` policy leaves the query string and the `Authorization` header out of the cache key, and CloudFront forwards `Authorization` to the origin only when the cache policy includes it. This policy keeps the `CachingOptimized` TTLs and compression and adds both, so each signed-in viewer gets their own cache entries:
    ```bash
    aws cloudfront create-cache-policy --cache-policy-config '{
      "Name": "lambda-web-cloudfront-oac",
      "MinTTL": 1, "DefaultTTL": 86400, "MaxTTL": 31536000,
      "ParametersInCacheKeyAndForwardedToOrigin": {
        "EnableAcceptEncodingGzip": true,
        "EnableAcceptEncodingBrotli": true,
        "HeadersConfig": { "HeaderBehavior": "whitelist", "Headers": { "Quantity": 1, "Items": ["Authorization"] } },
        "CookiesConfig": { "CookieBehavior": "none" },
        "QueryStringsConfig": { "QueryStringBehavior": "all" }
      }
    }'
    ```
1. Create the Origin Access Control. `OriginAccessControlOriginType` must be `lambda` and `SigningBehavior` must be `always-amz-auth`; CloudFront rejects `always` for Web Function origins:
    ```bash
    aws cloudfront create-origin-access-control --origin-access-control-config '{
      "Name": "lambda-web-cloudfront-oac",
      "SigningProtocol": "sigv4",
      "SigningBehavior": "always-amz-auth",
      "OriginAccessControlOriginType": "lambda"
    }'
    ```
1. Create the distribution with the function's endpoint domain as an HTTPS custom origin and the OAC attached to it. The script uses the cache policy from the previous step and the managed `AllViewerExceptHostHeader` origin request policy, which forwards the viewer's headers and query string but not the `Host` header. Lambda routes on `Host`, so the origin request must carry the endpoint domain, not the viewer's.
1. Attach a resource policy to the function that lets the CloudFront service principal invoke the `dev` endpoint, with an `AWS:SourceArn` condition naming your distribution. The ARNs take the partition and account from your own identity:
    ```bash
    CALLER_ARN=$(aws sts get-caller-identity --query Arn --output text)
    PARTITION=$(echo $CALLER_ARN | cut -d: -f2)
    ACCOUNT_ID=$(echo $CALLER_ARN | cut -d: -f5)
    aws lambda-web put-resource-policy --resource-arn arn:$PARTITION:lambda:$AWS_REGION:$ACCOUNT_ID:web-function/lambda-web-cloudfront-oac --policy '{
      "Version": "2012-10-17",
      "Statement": [{
        "Effect": "Allow",
        "Principal": { "Service": "cloudfront.amazonaws.com" },
        "Action": "lambda:InvokeWebFunctionEndpoint",
        "Resource": "arn:'$PARTITION':lambda:'$AWS_REGION':'$ACCOUNT_ID':web-function/lambda-web-cloudfront-oac/endpoint/dev",
        "Condition": { "StringEquals": { "AWS:SourceArn": "arn:'$PARTITION':cloudfront::'$ACCOUNT_ID':distribution/<distribution-id>" } }
      }]
    }'
    ```
1. Wait for the distribution to deploy:
    ```bash
    aws cloudfront wait distribution-deployed --id <distribution-id>
    ```

## How it works

```
Viewer ──HTTPS──▶ CloudFront ──SigV4-signed HTTPS (OAC)──▶ Web Function endpoint (IamAuth) ──▶ your HTTP server
                                                           ▲
Direct request ──HTTPS (unsigned)──────────────────────────┘ 403 Forbidden
```

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

Set the two URLs the deploy script printed:

```bash
export CLOUDFRONT_URL="https://<distribution-domain>.cloudfront.net"
export ORIGIN_URL="https://<endpoint-domain>.lambda-web.us-east-1.on.aws"
```

Directly at the origin, the request is rejected before it reaches the application:

```bash
curl -s -o /dev/null -w '%{http_code}\n' "$ORIGIN_URL/whoami"
# 403
```

Through CloudFront, the same request reaches the function. `viaCloudFront` is `true`, `authorizationHeaderPresent` is `false`, and the `cloudfront` object lists headers such as your viewer country:

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
#   "generatedAt": "2026-10-14T07:48:17.442Z",
# x-cache: Hit from cloudfront
#   "generatedAt": "2026-10-14T07:48:17.442Z",
# ...
```

To confirm that the policy ties the function to one distribution, create a second distribution with the same origin and OAC and request `/whoami` through it: it returns `403`. Disable and delete that distribution afterwards.

## Cleanup

Use the same `AWS_REGION` as the deploy. CloudFront needs a distribution to be disabled and fully deployed before it can be deleted, so that part takes a few minutes.

1. Disable and delete the distribution, the OAC and the cache policy:
    ```bash
    DIST_ID=$(aws cloudfront list-distributions \
      --query "DistributionList.Items[?Comment=='lambda-web-cloudfront-oac'].Id | [0]" --output text)
    ETAG=$(aws cloudfront get-distribution-config --id $DIST_ID --query ETag --output text)
    aws cloudfront get-distribution-config --id $DIST_ID --query DistributionConfig \
      | sed 's/"Enabled": true/"Enabled": false/' > /tmp/dist.json
    aws cloudfront update-distribution --id $DIST_ID --if-match $ETAG --distribution-config file:///tmp/dist.json > /dev/null
    aws cloudfront wait distribution-deployed --id $DIST_ID
    aws cloudfront delete-distribution --id $DIST_ID \
      --if-match $(aws cloudfront get-distribution-config --id $DIST_ID --query ETag --output text)

    OAC_ID=$(aws cloudfront list-origin-access-controls \
      --query "OriginAccessControlList.Items[?Name=='lambda-web-cloudfront-oac'].Id | [0]" --output text)
    aws cloudfront delete-origin-access-control --id $OAC_ID \
      --if-match $(aws cloudfront get-origin-access-control --id $OAC_ID --query ETag --output text)

    CACHE_POLICY_ID=$(aws cloudfront list-cache-policies --type custom \
      --query "CachePolicyList.Items[?CachePolicy.CachePolicyConfig.Name=='lambda-web-cloudfront-oac'].CachePolicy.Id | [0]" --output text)
    aws cloudfront delete-cache-policy --id $CACHE_POLICY_ID \
      --if-match $(aws cloudfront get-cache-policy --id $CACHE_POLICY_ID --query ETag --output text)
    ```
1. Delete the function. This also removes its endpoint, revisions and resource policy:
    ```bash
    aws lambda-web delete-web-function --function-name lambda-web-cloudfront-oac
    ```
1. Delete the execution role the AWS CLI created, and the log groups:
    ```bash
    aws iam delete-role-policy --role-name awscli-lambdaweb-lambda-web-cloudfront-oac --policy-name awscli-lambdaweb-logs
    aws iam delete-role --role-name awscli-lambdaweb-lambda-web-cloudfront-oac
    aws logs delete-log-group --log-group-name /aws/lambda/web/lambda-web-cloudfront-oac
    aws logs delete-log-group --log-group-name /aws/lambda/web/lambda-web-cloudfront-oac.local
    ```
1. The deploy also provisions a versioned artifact S3 bucket named `awscli-lambdaweb-<account-id>-<region>-<identifier>`. It is shared by all Web Functions you deploy in that Region, so leave it in place unless you have removed every Web Function. In that case, empty and delete it:
    ```bash
    aws s3 rb s3://<bucket-name> --force
    ```

----
Copyright 2026 Amazon.com, Inc. or its affiliates. All Rights Reserved.

SPDX-License-Identifier: MIT-0
