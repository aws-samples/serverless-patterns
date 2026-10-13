# Real-time metrics dashboard with Server-Sent Events on AWS Lambda Web Functions (SAM)

This pattern deploys a zero-dependency Node.js HTTP server as an AWS Lambda Web Function that streams live metrics to the browser over Server-Sent Events (SSE). It uses a plain Node.js HTTP server rather than a framework, so there are no dependencies and no build step. The dashboard makes the behaviours that distinguish Web Functions from the Lambda event model visible: long-lived HTTP connections, active-CPU time versus wall-clock uptime, and many concurrent requests per execution environment with scale-out.

A single `AWS::Serverless::WebFunction` resource creates the function, an immutable revision and a public HTTPS endpoint. The app is the same as the [AWS CLI variant](../awscli/) of this pattern; only the deployment differs.

Learn more about this pattern at Serverless Land Patterns: https://serverlessland.com/patterns/lambda-web-sse-dashboard-nodejs-sam

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

The dashboard is a single Node.js HTTP server (`src/index.js`) that reports what it measures about itself: how long the execution environment has been alive, how much CPU it has used, how many streaming connections it is holding open, and which Region is serving the request. Every value is measured from the running process; none of it is synthetic.

A Web Function runs a real server process, so the runtime provides the address to listen on in the `AWS_LAMBDA_HTTP_ENDPOINT` environment variable (in `host:port` form). The server reads it and starts listening, exactly as it would anywhere else:

```javascript
const [HOST, PORT_STR] = (process.env.AWS_LAMBDA_HTTP_ENDPOINT ?? `0.0.0.0:${process.env.PORT || 3000}`).split(':');
server.listen(Number(PORT_STR) || 3000, HOST);
```

The server exposes these routes:

| Method | Path | Description |
|---|---|---|
| `GET` | `/` | Dashboard UI (static HTML/CSS/JS, Chart.js from CDN) |
| `GET` | `/api/events` | SSE stream: holds the connection open and pushes a metrics snapshot every 2 seconds |
| `GET` | `/api/work?ms=1500` | Performs genuine CPU work (repeated SHA-256 hashing) for the requested duration (50 to 5000 ms) |
| `GET` | `/api/ping` | Tiny response the browser times to measure round-trip latency to the serving Region |
| `GET` | `/api/status` | Current metrics snapshot as JSON |

The dashboard updates every two seconds over a single HTTP connection that stays open. Because a Web Function environment is a long-lived process, it keeps the connection open and keeps pushing data to the browser. The Lambda event model handles one request per invocation and then freezes the environment until the next one; a frozen environment runs no code, so it cannot hold a connection open.

Template notes:

* `Timeout: 900` (the maximum), because an SSE response lasts as long as the request timeout. When the timeout closes the stream, the browser `EventSource` reconnects on its own.
* The single `AWS::Serverless::WebFunction` expands into `AWS::Lambda::WebFunction`, `AWS::Lambda::WebFunctionRevision` (immutable code and configuration) and `AWS::Lambda::WebFunctionEndpoint` (HTTPS endpoint routed 100% to that revision). SAM generates the execution role with `AWSLambdaBasicExecutionRole`.
* `AuthType: ApplicationManaged` means the endpoint is **public: anyone with the URL can reach it**, including `/api/work`, which runs CPU work that you pay for. Use `AuthType: IamAuth` to accept only SigV4-signed requests.
* Runtime is `nodejs24.x` with ESM (`"type": "module"`); the entry point is `index.js` at the zip root, with `public/` next to it.

To deploy a code change, upload the zip under a **new key** (for example `function-v2.zip`) and deploy again with the new `CodeKey`. CloudFormation only creates a new revision when the revision's properties change, so re-deploying with an unchanged key reports "No changes to deploy".

## Testing

### Run locally

Start the server locally and browse to `http://localhost:3000/` to see the dashboard streaming from the local process:

```bash
cd src && npm start
```

### On the deployed endpoint

Read the endpoint domain from the stack outputs:

```bash
export YOUR_ENDPOINT="https://$(aws cloudformation describe-stacks \
  --stack-name lambda-web-sse-dashboard-sam --region $AWS_REGION \
  --query "Stacks[0].Outputs[?OutputKey=='EndpointDomainName'].OutputValue" --output text)"
```

**Active-CPU time vs. uptime.** Browse to `$YOUR_ENDPOINT` and compare the **Environment uptime** and **CPU time consumed** cards. The environment stays alive for minutes but uses only a fraction of a second of CPU: you pay for the CPU time your code uses (plus memory and requests), not for wall-clock time spent waiting. Select **Generate CPU load** and the app runs a cryptographic hashing loop for about 1.5 seconds; the CPU line climbs, then falls back to near zero when the work stops. See the [AWS Lambda pricing page](https://aws.amazon.com/lambda/pricing/) for details.

You can also drive the work from the command line:

```bash
curl "$YOUR_ENDPOINT/api/work?ms=1500"
```

**Concurrency and scale-out.** Each execution environment handles many requests at once, not one at a time. As environments approach their concurrency limit, Lambda adds more, and removes them again when traffic falls, scaling back to zero. Generate load by sending 300 streaming requests to the `/api/events` endpoint rather than a burst of quick responses. curl keeps 200 connections open at once, each for 90 seconds, and starts the remaining 100 as the first ones finish, so the test takes about 3 minutes:

```bash
curl -sN --parallel --parallel-immediate --parallel-max 200 --max-time 90 \
  "$YOUR_ENDPOINT/api/events?[1-300]" > /dev/null
```

The dashboard reflects the active SSE connections and peak for the currently connected environment. Each environment reports only its own connections, because Lambda routes each request independently with no session affinity.

The runtime writes a per-environment summary record to Amazon CloudWatch Logs every minute (instance id, request count, peak concurrency, CPU time). Aggregate them across the fleet with a CloudWatch Logs Insights query on the stack's log group:

```bash
QID=$(aws logs start-query --region $AWS_REGION \
  --log-group-name /aws/lambda/web/lambda-web-sse-dashboard-sam \
  --start-time $(($(date +%s)-300)) --end-time $(date +%s) \
  --query-string 'filter type="platform.invokeSummary" | stats count_distinct(record.instanceId) as environments, sum(record.metrics.requests) as totalRequests, max(record.metrics.concurrentRequests) as peakConcurrency, sum(record.metrics.cpuTimeMs)/1000 as totalCpuSeconds' \
  --query queryId --output text) && sleep 6 && aws logs get-query-results --region $AWS_REGION --query-id "$QID"
```

In a sample run in `us-east-2`, Lambda spread the 300 streams across about 100 execution environments: most held 2 connections, and a few held 13 or 14. Lambda decides placement, so your numbers will differ from run to run. The query can count more environments than the streams used, because environments from earlier traffic stay alive for a while and still write summary records. Run it again a minute or two after the test to include the last summary records.

View the logs written by the environments:

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
