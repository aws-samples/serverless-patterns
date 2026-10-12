# Server-Sent Events dashboard on AWS Lambda Web Functions (SAM)

This pattern deploys a real-time metrics dashboard that streams updates to browsers over Server-Sent Events (SSE) from an AWS Lambda Web Function. With the Lambda invocation model, a function returns one response per invocation and the execution environment is frozen afterwards, so it cannot hold a long-lived HTTP connection. Lambda Web Functions run a persistent HTTP server that keeps serving while connections stay open, so this zero-dependency Node.js app (`http`, `fs`, `path` only) runs unchanged locally and on AWS.

`GET /api/events` keeps the response open and receives a metrics broadcast every 2 seconds; `POST /api/metrics` pushes a custom event to every connected client; `GET /` serves a Chart.js dashboard that plots the stream. A single `AWS::Serverless::WebFunction` resource creates the function, an immutable revision and a public HTTPS endpoint.

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
    cd lambda-web-sse-dashboard/nodejs/sam
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
1. Package the application and upload it. The app has no dependencies; the zip contains the server and the static dashboard:
    ```bash
    (cd src && zip -qr ../function.zip index.js package.json public)
    aws s3 cp function.zip s3://$BUCKET/lambda-web-sse-dashboard-sam/function.zip --region $AWS_REGION
    ```
1. Deploy the stack, passing the bucket and key of the uploaded code:
    ```bash
    sam deploy \
      --stack-name lambda-web-sse-dashboard-sam \
      --capabilities CAPABILITY_IAM \
      --region $AWS_REGION \
      --resolve-s3 \
      --parameter-overrides \
        CodeBucket=$BUCKET \
        CodeKey=lambda-web-sse-dashboard-sam/function.zip
    ```
    Once you have run `sam deploy` once and saved arguments to a configuration file (`samconfig.toml`), you can use `sam deploy` in future to use these defaults.
1. Note the `EndpointDomainName` output. The endpoint can take a couple of minutes to become `Active` on a first deploy.

## How it works

* `src/index.js` creates the server with `http.createServer` and listens on the address in the `AWS_LAMBDA_HTTP_ENDPOINT` environment variable. The runtime sets it to `0.0.0.0:3000` and probes it for readiness; when the variable is absent (local development) the app falls back to the same value.
* Routes:
  * `GET /api/events` answers `200` with `Content-Type: text/event-stream` and **never ends the response**. The response object is added to a `Set` of clients, receives an initial snapshot immediately, and is removed when the request closes.
  * A `setInterval` generates a metrics snapshot every 2 seconds and writes it to every client as a `data: {...}\n\n` line. The metrics are synthetic sine waves plus the real per-sandbox counters (`activeConnections`, `peakConnections`, `totalRequests`, `uptime`).
  * `POST /api/metrics` accepts any JSON body and broadcasts it right away to all connected clients as a `custom` field. Invalid JSON returns **400**.
  * `GET /api/status` returns one snapshot; `GET /` and other paths serve files from `public/` (path traversal outside `public/` returns 404).
* **Scope of the connection set.** Clients and counters live in the sandbox's memory. One sandbox serves many concurrent connections; when traffic grows the service adds sandboxes, and a broadcast only reaches the clients connected to the sandbox that emits it. That is the right scope for per-instance dashboards, progress feeds or notifications about work the sandbox itself is doing. For fan-out that must reach every client regardless of sandbox, publish events through a shared channel (DynamoDB Streams, SNS, EventBridge) and let each sandbox subscribe and relay.
* `template.yaml` sets `Timeout: 900` (the maximum) because an SSE response lasts as long as the request timeout. When the timeout closes the stream, the browser `EventSource` reconnects on its own. The single `AWS::Serverless::WebFunction` expands into `AWS::Lambda::WebFunction`, `AWS::Lambda::WebFunctionRevision` (immutable code + configuration) and `AWS::Lambda::WebFunctionEndpoint` (HTTPS endpoint routed 100% to that revision); SAM generates the execution role with `AWSLambdaBasicExecutionRole`.
* `AuthType: ApplicationManaged` means the endpoint is **public: anyone with the URL can reach it**. Protect `POST /api/metrics` before real use, or change to `AuthType: IamAuth` to accept only SigV4-signed requests.
* On `SIGTERM` the interval is cleared, every open SSE response is ended and the server closes.

Key runtime constraints:

* Runtime is `nodejs24.x`; the code uses ESM (`"type": "module"` in `package.json`).
* The entry point is `index.js` at the zip root, with `public/` next to it.
* Bind the host and port from `AWS_LAMBDA_HTTP_ENDPOINT`. A hardcoded port that does not match it fails the readiness probe.

To deploy a code change, upload the zip under a **new key** (for example `function-v2.zip`) and deploy again with the new `CodeKey`. CloudFormation only creates a new revision when the revision's properties change, so re-deploying with an unchanged key reports "No changes to deploy".

## Testing

Run the app locally first. The same code runs unchanged on AWS:

```bash
cd src
node index.js
# SSE Dashboard listening on 0.0.0.0:3000
```

Open `http://localhost:3000/` in a browser to see the dashboard, or use curl:

```bash
# Hold an SSE connection open for 10 seconds: one "data:" line every 2 seconds
curl -N --max-time 10 http://localhost:3000/api/events
```

After deployment, read the endpoint domain and repeat against AWS:

```bash
ENDPOINT=$(aws cloudformation describe-stacks \
  --stack-name lambda-web-sse-dashboard-sam \
  --region $AWS_REGION \
  --query "Stacks[0].Outputs[?OutputKey=='EndpointDomainName'].OutputValue" \
  --output text)

# Dashboard
open https://$ENDPOINT/      # or paste the URL in a browser

# Three concurrent SSE clients on the same endpoint for 7 seconds
for i in 1 2 3; do curl -sN --max-time 7 https://$ENDPOINT/api/events > /tmp/sse-$i.txt & done
sleep 2

# Push a custom event: it reaches every client connected to the same sandbox
curl -s -X POST https://$ENDPOINT/api/metrics -H 'Content-Type: application/json' -d '{"deploy":"v2"}'
# {"success":true,"broadcastTo":3}
wait

grep -c '^data:' /tmp/sse-1.txt          # ~4 snapshots + the custom event
grep -o '"activeConnections":[0-9]*' /tmp/sse-1.txt | sort | uniq -c
#   4 "activeConnections":3
grep -o '"custom":{[^}]*}' /tmp/sse-1.txt
# "custom":{"deploy":"v2"}

# One-shot snapshot
curl -s https://$ENDPOINT/api/status
# {"timestamp":"...","region":"us-east-1","uptime":42,"activeConnections":0,"peakConnections":3,"totalRequests":9,...}
```

If `broadcastTo` is smaller than the number of clients you opened, the clients landed on different sandboxes; see "Scope of the connection set" above.

View the logs written by the sandboxes:

```bash
aws logs tail /aws/lambda/web/lambda-web-sse-dashboard-sam --region $AWS_REGION --follow
```

## Cleanup

1. Delete the stack:
    ```bash
    sam delete --stack-name lambda-web-sse-dashboard-sam --region $AWS_REGION
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
