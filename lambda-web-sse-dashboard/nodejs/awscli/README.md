# Real-time metrics dashboard with Server-Sent Events on AWS Lambda Web Functions

This pattern deploys a zero-dependency Node.js HTTP server as an AWS Lambda Web Function that streams live metrics to the browser over Server-Sent Events (SSE). It uses a plain Node.js HTTP server rather than a framework, so there are no dependencies and no build step. The dashboard makes the behaviours that distinguish Web Functions from the Lambda event model visible: long-lived HTTP connections, active-CPU time versus wall-clock uptime, many concurrent requests per execution environment with scale-out, and — optionally — latency-based routing across Regions.

Learn more about this pattern at Serverless Land Patterns: https://serverlessland.com/patterns/lambda-web-sse-dashboard/nodejs/awscli

Important: this application uses various AWS services and there are costs associated with these services after the Free Tier usage - please see the [AWS Pricing page](https://aws.amazon.com/pricing/) for details. You are responsible for any AWS costs incurred. No warranty is implied in this example.

## Requirements

* [Create an AWS account](https://portal.aws.amazon.com/gp/aws/developer/registration/index.html) if you do not already have one and log in. The IAM user that you use must have sufficient permissions to make necessary AWS service calls and manage AWS resources.
* [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html) installed and configured
* [Git Installed](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)
* [Node.js](https://nodejs.org/) installed

## Deployment Instructions

1. Create a new directory, navigate to that directory in a terminal and clone the GitHub repository:
    ```
    git clone https://github.com/aws-samples/serverless-patterns
    ```
1. Change directory to the pattern directory:
    ```
    cd serverless-patterns/lambda-web-sse-dashboard/nodejs/awscli
    ```
1. Install dependencies (this app has none, so the step completes immediately):
    ```
    npm install
    ```
1. Deploy the web function with a single command:
    ```
    aws lambda-web deploy --name lambda-web-sse-dashboard --code . --timeout-seconds 900
    ```
    You can also run `npm run deploy`, which wraps the same command. The AWS CLI bundles your code, provisions a versioned artifact bucket and an execution role if you don't already have them, creates the function and its endpoint, and returns a live HTTPS URL.
1. Press ENTER when prompted to create the resources.

The AWS CLI prints the endpoint URL in the form `https://<domain>.lambda-web.<region>.on.aws`. Browse to it and the dashboard loads, already streaming.

## How it works

The dashboard is a single Node.js HTTP server (`index.js`) that reports what it measures about itself: how long the execution environment has been alive, how much CPU it has used, how many streaming connections it is holding open, and which Region is serving the request. Every value is measured from the running process — none of it is synthetic.

A Web Function runs a real server process, so the runtime provides the address to listen on in the `AWS_LAMBDA_HTTP_ENDPOINT` environment variable (in `host:port` form). The server reads it and starts listening, exactly as it would anywhere else:

```javascript
const [host, port] = (process.env.AWS_LAMBDA_HTTP_ENDPOINT || "0.0.0.0:3000").split(":");
server.listen(Number(port), host);
```

The runtime is `nodejs24.x`, and it loads `index.js` at the package root by default. To use a different entry file, set `AWS_LAMBDA_NODEJS_ENTRYPOINT` to its path.

The server exposes these routes:

| Method | Path | Description |
|---|---|---|
| `GET` | `/` | Dashboard UI (static HTML/CSS/JS, Chart.js from CDN) |
| `GET` | `/api/events` | SSE stream — holds the connection open and pushes a metrics snapshot every 2 seconds |
| `GET` | `/api/work?ms=1500` | Performs genuine CPU work (repeated SHA-256 hashing) for the requested duration |
| `GET` | `/api/ping` | Tiny response the browser times to measure round-trip latency to the serving Region |
| `GET` | `/api/status` | Current metrics snapshot as JSON |

The dashboard updates every two seconds over a single HTTP connection that stays open. Because a Web Function environment is a long-lived process, it keeps the connection open and keeps pushing data to the browser — and can run background tasks outside the main request path, such as emitting telemetry. The Lambda event model handles one request per invocation and then freezes the environment until the next one; a frozen environment runs no code, so it cannot hold a connection open.

## Testing

### Run locally

Start the server locally and browse to `http://localhost:3000/` to see the dashboard streaming from the local process:

```bash
npm start
```

### On the deployed endpoint

Set the endpoint URL printed by `aws lambda-web deploy`:

```bash
export YOUR_ENDPOINT="https://<domain>.lambda-web.us-east-1.on.aws"
```

**Active-CPU time vs. uptime.** Compare the **Environment uptime** and **CPU time consumed** cards. The environment stays alive for minutes but uses only a fraction of a second of CPU — you pay for the CPU time your code uses (plus memory and requests), not for wall-clock time spent waiting. Select **Generate CPU load** and the app runs a cryptographic hashing loop for about 1.5 seconds; the CPU line climbs, then falls back to near zero when the work stops. For a web app that spends a request waiting on a database, downstream API, or AI inference, that waiting is not billed as CPU. See the [AWS Lambda pricing page](https://aws.amazon.com/lambda/pricing/) for details.

You can also drive the work from the command line:

```bash
curl "$YOUR_ENDPOINT/api/work?ms=1500"
```

**Concurrency and scale-out.** Each execution environment handles many requests at once, not one at a time. As environments approach their concurrency limit, Lambda adds more, and removes them again when traffic falls, scaling back to zero. Generate load by sending 300 streaming requests to the `/api/events` endpoint rather than a burst of quick responses. curl keeps 200 connections open at once, each for 90 seconds, and starts the remaining 100 as the first ones finish, so the test takes about 3 minutes:

```bash
curl -sN --parallel --parallel-immediate --parallel-max 200 --max-time 90 \
  "$YOUR_ENDPOINT/api/events?[1-300]"
```

The dashboard reflects the active SSE connections and peak for the currently connected environment. Each environment reports only its own connections, because Lambda routes each request independently with no session affinity.

You can control how a Web Function scales: `maxConcurrencyPerEnvironment` sets how many requests each environment handles at once (up to 128, default 64); on the endpoint, `maxEnvironments` caps the number of environments and `rateLimit` caps requests per second — useful for protecting downstream dependencies.

The runtime writes a per-environment summary record to Amazon CloudWatch Logs every minute (instance id, request count, peak concurrency, CPU time). Aggregate them across the fleet with a CloudWatch Logs Insights query:

```bash
QID=$(aws logs start-query \
  --log-group-name /aws/lambda/web/lambda-web-sse-dashboard \
  --start-time $(($(date +%s)-300)) --end-time $(date +%s) \
  --query-string 'filter type="platform.invokeSummary" | stats count_distinct(record.instanceId) as environments, sum(record.metrics.requests) as totalRequests, max(record.metrics.concurrentRequests) as peakConcurrency, sum(record.metrics.cpuTimeMs)/1000 as totalCpuSeconds' \
  --query queryId --output text) && sleep 6 && aws logs get-query-results --query-id "$QID"
```

In a sample run, the streams landed on 6 execution environments: three held 64 connections each (the default limit), and the others held 47, 35 and 26. The query reported 355 requests, a peak concurrency of 64, and about 4.3 seconds of CPU across the whole fleet for over 3 minutes of streaming. The query can count a few more environments than the streams used, because environments from earlier traffic stay alive for a while and still write summary records.

### Going global (optional)

The same app can serve requests from the Region nearest the caller. An endpoint's type and Regions are fixed when it is created, so going global means adding a new endpoint rather than changing the existing one:

```bash
aws lambda-web deploy --name lambda-web-sse-dashboard --code . --timeout-seconds 900 \
  --endpoint-name global --endpoint-type MultiRegion --regions us-east-1,eu-west-2
```

You can also run `npm run deploy:global`. Lambda replicates the code to each Region and returns a single global domain URL in the form `https://<domain>.lambda-web.global.on.aws`, using Amazon Route 53 latency-based routing to send each request to the closest Region. Browse to the global URL and the **Served from** card shows the Region actually serving you — with no load balancer and no routing to configure.

### About the log groups

Lambda writes logs to two groups per Region: `/aws/lambda/web/lambda-web-sse-dashboard` is the centralized group you read from (created lazily on the first request, after a short delay), and `/aws/lambda/web/lambda-web-sse-dashboard.local` is a temporary in-Region staging group — don't build queries or filters on it. With a global endpoint, both exist in each Region the function runs (for example `eu-west-2`), so cleanup deletes them per Region.

## Cleanup

1. Delete the function. This also removes all of its endpoints (both `dev` and `global`) and revisions — you don't need to delete them separately:
    ```bash
    aws lambda-web delete-web-function --function-name lambda-web-sse-dashboard
    ```
1. Delete the dedicated execution role. Its inline policy must be removed before the role can be deleted:
    ```bash
    aws iam delete-role-policy --role-name awscli-lambdaweb-lambda-web-sse-dashboard --policy-name awscli-lambdaweb-logs
    aws iam delete-role --role-name awscli-lambdaweb-lambda-web-sse-dashboard
    ```
1. Delete the CloudWatch log groups in the home Region (`us-east-1`). A group that was never created returns a harmless "does not exist" error:
    ```bash
    aws logs delete-log-group --log-group-name /aws/lambda/web/lambda-web-sse-dashboard --region us-east-1
    aws logs delete-log-group --log-group-name /aws/lambda/web/lambda-web-sse-dashboard.local --region us-east-1
    ```
1. If you created the global endpoint, also delete the log groups in each replica Region (for example `eu-west-2`):
    ```bash
    aws logs delete-log-group --log-group-name /aws/lambda/web/lambda-web-sse-dashboard --region eu-west-2
    aws logs delete-log-group --log-group-name /aws/lambda/web/lambda-web-sse-dashboard.local --region eu-west-2
    ```
1. The deploy also provisions a versioned artifact S3 bucket named `awscli-lambdaweb-<account-id>-<region>-<identifier>`. This bucket is shared by all Web Functions you deploy in that Region, so leave it in place unless you have removed every Web Function — in which case empty and delete it (versioning is enabled, so `--force` is required to empty it first):
    ```bash
    aws s3 rb s3://<bucket-name> --force
    ```

----
Copyright 2026 Amazon.com, Inc. or its affiliates. All Rights Reserved.

SPDX-License-Identifier: MIT-0
