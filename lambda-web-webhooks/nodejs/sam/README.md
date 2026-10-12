# Webhook ingestion on AWS Lambda Web Functions with DynamoDB (SAM)

This pattern deploys a webhook receiver as an AWS Lambda Web Function backed by an Amazon DynamoDB table. Providers such as Stripe or GitHub POST straight to the function's HTTPS endpoint, so one Express server replaces the usual API Gateway plus Lambda pair. The app verifies each provider's HMAC-SHA256 signature over the raw body with a timing-safe comparison, then stores the event once with a conditional write, which makes provider retries idempotent. Events expire through a DynamoDB TTL.

An opt-in `POST /test/fire` helper (`EnableTestEndpoint=true`, off by default) produces a correctly signed sample request so the flow can be tested without an external account. A single `AWS::Serverless::WebFunction` resource creates the function, an immutable revision and the public HTTPS endpoint.

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
    cd lambda-web-webhooks/nodejs/sam
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
    (cd src && npm install --omit=dev && zip -qr ../function.zip index.js lib package.json node_modules)
    aws s3 cp function.zip s3://$BUCKET/lambda-web-webhooks-sam/function.zip --region $AWS_REGION
    ```
1. Generate the webhook secrets. The template has no defaults and requires at least 16 characters; for Stripe, use the `whsec_...` value the Stripe dashboard shows once you register the endpoint (a generated one is fine for the test walkthrough):
    ```bash
    export STRIPE_WEBHOOK_SECRET=$(openssl rand -hex 32)
    export GITHUB_WEBHOOK_SECRET=$(openssl rand -hex 32)
    export GENERIC_WEBHOOK_SECRET=$(openssl rand -hex 32)
    ```
1. Deploy the stack. `EnableTestEndpoint` defaults to `false`; pass `EnableTestEndpoint=true` only to follow the [Testing](#testing) walkthrough, and redeploy without it before pointing real providers at the URL:
    ```bash
    sam deploy \
      --stack-name lambda-web-webhooks-sam \
      --capabilities CAPABILITY_IAM \
      --region $AWS_REGION \
      --resolve-s3 \
      --parameter-overrides \
        CodeBucket=$BUCKET \
        CodeKey=lambda-web-webhooks-sam/function.zip \
        StripeWebhookSecret=$STRIPE_WEBHOOK_SECRET \
        GitHubWebhookSecret=$GITHUB_WEBHOOK_SECRET \
        GenericWebhookSecret=$GENERIC_WEBHOOK_SECRET \
        EnableTestEndpoint=true
    ```
    Once you have run `sam deploy` once and saved arguments to a configuration file (`samconfig.toml`), you can use `sam deploy` in future to use these defaults.
1. Note the `EndpointDomainName` output. Configure your provider's webhook URL as `https://<EndpointDomainName>/webhooks/stripe` (or `/github`, `/generic`).

## How it works

* `src/index.js` is an Express 5 app wrapped in `http.createServer`, listening on the address in `AWS_LAMBDA_HTTP_ENDPOINT` (set by the runtime to `0.0.0.0:3000`, same fallback locally).
* The `/webhooks` router uses `express.raw()` so the handler sees the **exact bytes** the provider sent. Signatures are computed over those bytes; re-serialised JSON would not match.
* `POST /webhooks/{provider}` in four steps:
  1. **Verify** with the provider's scheme (`src/lib/verify.js`): Stripe `stripe-signature: t=<ts>,v1=<hmac>` over `"<ts>.<body>"`; GitHub `x-hub-signature-256: sha256=<hmac>`; generic `x-webhook-signature: <hex hmac>`. All comparisons use `crypto.timingSafeEqual`. A missing or wrong signature returns **401** before the body is parsed.
  2. **Parse** the JSON body (**400** if invalid).
  3. **Derive a stable event id**: GitHub's `x-github-delivery` header, otherwise the payload `id`, stored as `<provider>:<id>`.
  4. **Store once** with `ConditionExpression: attribute_not_exists(eventId)`. The first delivery returns `200`; a redelivery of the same event returns `200` with `duplicate: true`, so the provider stops retrying and nothing is processed twice.
* Each item carries a `ttl` epoch attribute (30 days by default, `EVENT_TTL_DAYS`) and the table has TTL enabled, so old events disappear without a cleanup job.
* `POST /test/fire` returns the headers and body of a correctly signed request for a provider. It signs with the **real** secret, so it only exists when `ENABLE_TEST_ENDPOINT=true` and must be off wherever real webhooks are accepted.
* `template.yaml`: secrets are `NoEcho` parameters with no default and `MinLength: 16`, mapped to environment variables (in production read them from AWS Secrets Manager or SSM Parameter Store at startup instead); `EventsTable` is on-demand with TTL on `ttl`; `WebFunctionRole` grants `PutItem`, `GetItem` and `Scan` on the table plus CloudWatch Logs; the single `AWS::Serverless::WebFunction` expands into `AWS::Lambda::WebFunction`, `AWS::Lambda::WebFunctionRevision` and `AWS::Lambda::WebFunctionEndpoint`.
* `AuthType: ApplicationManaged` is required here: webhook providers cannot SigV4-sign their calls, so the endpoint is public and the HMAC signature is the authentication. `GET /events` and `GET /events/{eventId}` are unauthenticated read-back routes for the demo; protect or remove them before real use.

Key runtime constraints:

* Runtime is `nodejs24.x`; the code uses ESM (`"type": "module"` in `package.json`).
* The entry point is `index.js` at the zip root, with `lib/` and `node_modules` next to it.
* Bind the host and port from `AWS_LAMBDA_HTTP_ENDPOINT`. A hardcoded port that does not match it fails the readiness probe.

To deploy a code change, upload the zip under a **new key** (for example `function-v2.zip`) and deploy again with the new `CodeKey`. CloudFormation only creates a new revision when the revision's properties change, so re-deploying with an unchanged key reports "No changes to deploy".

## Testing

Run the app locally first against the deployed table. The same code runs unchanged on AWS:

```bash
cd src && npm install
export TABLE_NAME=$(aws cloudformation describe-stacks \
  --stack-name lambda-web-webhooks-sam --region $AWS_REGION \
  --query "Stacks[0].Outputs[?OutputKey=='TableName'].OutputValue" --output text)
ENABLE_TEST_ENDPOINT=true node index.js   # uses the *_WEBHOOK_SECRET variables exported above
```

After deploying with `EnableTestEndpoint=true`, use the test helper to obtain a signed request and deliver it. The body must be sent byte for byte as returned (compact JSON), which the `python3` one-liner below guarantees:

```bash
ENDPOINT=$(aws cloudformation describe-stacks \
  --stack-name lambda-web-webhooks-sam \
  --region $AWS_REGION \
  --query "Stacks[0].Outputs[?OutputKey=='EndpointDomainName'].OutputValue" \
  --output text)

# 1. Ask for a signed Stripe-style request
FIRE=$(curl -s -X POST https://$ENDPOINT/test/fire -H 'Content-Type: application/json' \
  -d '{"provider":"stripe","eventType":"payment.succeeded"}')
echo "$FIRE"
# {"instruction":"POST /webhooks/stripe","headers":{"Content-Type":"application/json","stripe-signature":"t=1790695700,v1=271f97..."},"body":{"id":"2f44eaca-...","type":"payment.succeeded","data":{...}}}

SIG=$(echo "$FIRE" | python3 -c "import json,sys;print(json.load(sys.stdin)['headers']['stripe-signature'])")
BODY=$(echo "$FIRE" | python3 -c "import json,sys;print(json.dumps(json.load(sys.stdin)['body'],separators=(',',':')))")

# 2. Deliver it -> 200, stored
curl -s -X POST https://$ENDPOINT/webhooks/stripe -H 'Content-Type: application/json' \
  -H "stripe-signature: $SIG" --data-binary "$BODY"
# {"success":true,"eventId":"stripe:2f44eaca-...","provider":"stripe","eventType":"payment.succeeded","receivedAt":"..."}

# 3. Deliver the same event again -> 200, duplicate (idempotent)
curl -s -X POST https://$ENDPOINT/webhooks/stripe -H 'Content-Type: application/json' \
  -H "stripe-signature: $SIG" --data-binary "$BODY"
# {"success":true,"eventId":"stripe:2f44eaca-...","duplicate":true,"message":"Event already processed"}

# 4. Tamper with the body -> 401
curl -s -X POST https://$ENDPOINT/webhooks/stripe -H 'Content-Type: application/json' \
  -H "stripe-signature: $SIG" --data-binary "${BODY%\}},\"amount\":1}"
# {"error":"Invalid signature","provider":"stripe","detail":"Signature mismatch"}

# 5. No signature -> 401; unknown provider -> 400
curl -s -X POST https://$ENDPOINT/webhooks/generic -H 'Content-Type: application/json' -d '{"id":"1"}'
# {"error":"Invalid signature","provider":"generic","detail":"Missing x-webhook-signature header"}
curl -s -X POST https://$ENDPOINT/webhooks/slack -d '{}'
# {"error":"Unknown provider: slack","supported":["stripe","github","generic"]}

# 6. Read back
curl -s "https://$ENDPOINT/events?limit=10"
```

Repeat steps 1 to 4 with `"provider":"github"` (header `x-hub-signature-256`) and `"provider":"generic"` (header `x-webhook-signature`).

To receive real Stripe events, register `https://<EndpointDomainName>/webhooks/stripe` in the Stripe dashboard, redeploy with `StripeWebhookSecret=<the whsec_... shown by Stripe>` and `EnableTestEndpoint=false` (the default).

View the logs written by the sandboxes:

```bash
aws logs tail /aws/lambda/web/lambda-web-webhooks-sam --region $AWS_REGION --follow
```

## Cleanup

1. Delete the stack. This also deletes the DynamoDB table **and all stored events**:
    ```bash
    sam delete --stack-name lambda-web-webhooks-sam --region $AWS_REGION
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
