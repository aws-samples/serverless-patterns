# Remote MCP server with an IAM-protected backend API on AWS Lambda Web Functions

This pattern deploys a remote [Model Context Protocol](https://modelcontextprotocol.io) (MCP) server and the HTTP API it calls, as two AWS Lambda Web Functions that you deploy and delete together. The API stands in for a service you already run. It has no MCP code, and its endpoint uses `IamAuth`, so only callers that sign requests with AWS Signature Version 4 (SigV4) and hold `lambda:InvokeWebFunctionEndpoint` can reach it. The MCP server signs its requests with its own execution role, so there is no shared secret to store or rotate.

The MCP server exposes two tools:

| Tool | Runs in | Description |
|---|---|---|
| `get_current_time` | MCP server | Returns the current time as ISO 8601 and as a formatted local time in an optional IANA time zone (default `UTC`) |
| `run_cpu_work` | CPU API | Calls the API, which runs 1-20 seconds of SHA-256 hashing and streams a line every second. The MCP server relays each line to the client as a progress update, then returns the total hashes, the hash rate, the elapsed time and the execution environment ids of both functions |

Learn more about this pattern at Serverless Land Patterns: https://serverlessland.com/patterns/lambda-web-mcp-server/nodejs/awscli

> **Warning:** the MCP server endpoint has no authentication. Anyone with its URL can call the tools, including `run_cpu_work`, which runs CPU work that you pay for. The CPU API is protected by IAM, but the MCP server calls it on behalf of any caller. Delete the functions when you finish testing (see [Cleanup](#cleanup)), and add authentication to the MCP server before you use this pattern outside a demo.

Important: this application uses various AWS services and there are costs associated with these services after the Free Tier usage - please see the [AWS Pricing page](https://aws.amazon.com/pricing/) for details. You are responsible for any AWS costs incurred. No warranty is implied in this example.

## Requirements

* [Create an AWS account](https://portal.aws.amazon.com/gp/aws/developer/registration/index.html) if you do not already have one and log in. The IAM user that you use must have sufficient permissions to make necessary AWS service calls and manage AWS resources.
* [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html) installed and configured
* [Git Installed](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)
* [Node.js](https://nodejs.org/) 24 or later installed

## Deployment Instructions

1. Create a new directory, navigate to that directory in a terminal and clone the GitHub repository:
    ```
    git clone https://github.com/aws-samples/serverless-patterns
    ```
1. Change directory to the pattern directory:
    ```
    cd serverless-patterns/lambda-web-mcp-server/nodejs/awscli
    ```
1. Set your Region and account ID, and a name prefix for the pattern's resources. Every function, role and log group below starts with `$STACK`, the way a single SAM or CDK stack would name them, so you can deploy a second copy by changing it:
    ```bash
    export AWS_REGION=us-east-1
    export ACCOUNT_ID=$(aws sts get-caller-identity --query Account --output text)
    export STACK=lambda-web-mcp-server
    ```
1. Deploy the CPU API. The AWS CLI creates the function, a logs-only execution role and an endpoint named `dev`:
    ```bash
    aws lambda-web deploy --name $STACK-cpu-api --code cpu-api --timeout-seconds 60 --create
    ```
1. Switch the CPU API endpoint to `IamAuth`. The endpoint is public between the deploy and this command, so run it straight away:
    ```bash
    aws lambda-web update-web-function-endpoint \
      --function-name $STACK-cpu-api --endpoint-name dev --auth-type IamAuth
    ```
1. Save the CPU API endpoint's ARN and domain:
    ```bash
    API_ARN=$(aws lambda-web get-web-function-endpoint \
      --function-name $STACK-cpu-api --endpoint-name dev --query endpointArn --output text)
    API_DOMAIN=$(aws lambda-web get-web-function-endpoint \
      --function-name $STACK-cpu-api --endpoint-name dev --query domainName --output text)
    ```
1. Create the MCP server's execution role. Its policy allows it to invoke the CPU API's `dev` endpoint and nothing else, and to write its own logs. Both functions are in the same account, so this identity-based policy is enough and the CPU API needs no resource-based policy:
    ```bash
    aws iam create-role --role-name $STACK-mcp-role \
      --assume-role-policy-document '{"Version":"2012-10-17","Statement":[{"Effect":"Allow","Principal":{"Service":"lambda.amazonaws.com"},"Action":"sts:AssumeRole"}]}'

    aws iam put-role-policy --role-name $STACK-mcp-role --policy-name invoke-cpu-api-and-logs \
      --policy-document "{\"Version\":\"2012-10-17\",\"Statement\":[
        {\"Effect\":\"Allow\",\"Action\":\"lambda:InvokeWebFunctionEndpoint\",\"Resource\":\"$API_ARN\"},
        {\"Effect\":\"Allow\",\"Action\":[\"logs:CreateLogGroup\",\"logs:CreateLogStream\",\"logs:PutLogEvents\"],
         \"Resource\":\"arn:aws:logs:$AWS_REGION:$ACCOUNT_ID:log-group:/aws/lambda/web/$STACK-mcp*\"}]}"
    ```
1. Install the MCP server's dependencies and deploy it with that role and the CPU API's URL. Wait about 10 seconds after creating the role so IAM can propagate it:
    ```bash
    (cd mcp-server && npm install)
    aws lambda-web deploy --name $STACK-mcp --code mcp-server --timeout-seconds 120 \
      --execution-role-arn arn:aws:iam::$ACCOUNT_ID:role/$STACK-mcp-role \
      --env BACKEND_URL=https://$API_DOMAIN --create
    ```
    The MCP server's timeout (120 seconds) is longer than the CPU API's (60 seconds), so a slow backend call fails as a tool error instead of the MCP request being cut off.

The second deploy prints the MCP server's URL in the form `https://<domain>.lambda-web.<region>.on.aws`. The MCP endpoint is that URL with `/mcp` appended.

## How it works

The MCP client calls the MCP server over Streamable HTTP. `get_current_time` runs in the MCP server. For `run_cpu_work`, the MCP server sends a signed `POST /work` to the CPU API, reads its streamed response, and turns each line into an MCP progress notification:

```
MCP client ──Streamable HTTP──▶ MCP server ──SigV4-signed HTTPS──▶ CPU API (IamAuth)
           ◀──SSE progress────            ◀──one JSON line per s──
```

### Signing requests to an `IamAuth` endpoint

Lambda Web Functions have no SDK client for invoking an endpoint. You send a normal HTTPS request and sign it with SigV4, using the service name `lambda`. The MCP server creates a signer once, at module scope, with the default credential provider, which picks up the execution role's credentials:

```javascript
const signer = new SignatureV4({
  service: 'lambda',
  region: process.env.AWS_REGION,
  credentials: defaultProvider(),
  sha256: Sha256,
});
```

Each call signs the request, then sends it with `fetch`:

```javascript
const signed = await signer.sign({
  method: 'POST', protocol: 'https:', hostname: url.hostname, path: url.pathname,
  headers: {
    'content-type': 'application/json',
    host: url.hostname,
    'x-amz-content-sha256': crypto.createHash('sha256').update(body).digest('hex'),
  },
  body,
});
const res = await fetch(url, { method: 'POST', headers: signed.headers, body, signal });
```

Lambda Web rejects requests without an `X-Amz-Content-SHA256` header with `403 Forbidden`. The request body here is small, so the MCP server signs its hash. Only the response streams. After Lambda Web validates the signature, it removes the `Authorization` header, so the CPU API code never sees the credentials and does no authentication of its own.

Regional endpoints such as `dev` (`HomeRegion`) use SigV4. A `MultiRegion` endpoint needs SigV4a instead.

### Streaming progress through two functions

The CPU API streams newline-delimited JSON: one progress line per second of work, then one result line. The MCP server reads the response body line by line and sends each progress line to the client as an MCP progress notification, which the SDK delivers over a Server-Sent Events stream. Both connections stay open for the whole call.

The MCP server passes the MCP request's abort signal to `fetch`. When the client cancels, the MCP server closes the connection to the CPU API, and the CPU API stops hashing when it sees the connection close. A non-200 response or a broken stream from the CPU API becomes a tool error (`isError: true`), not a failed MCP request.

### Why split the work into its own function

* **The MCP server stays responsive.** The CPU work runs in the CPU API's environments, not on the MCP server's JavaScript thread, so `get_current_time` answers immediately while `run_cpu_work` calls are running.
* **Each function scales on its own.** The CPU API scales with the work, and the MCP server scales with the number of MCP requests.
* **You pay CPU time where the work runs.** Lambda Web Functions bill for active CPU time, and time spent waiting on an external call isn't billed as active CPU. While the CPU API hashes, the MCP server mostly waits and relays one line per second. In one test, the `platform.invokeSummary` log records showed the MCP server using 400 ms of CPU across 7 requests, including two `run_cpu_work` calls that ran for 9 seconds in total, while the CPU API used 11,049 ms for those two calls.

The MCP server endpoint uses the default `ApplicationManaged` auth type, so it is public. See the warning at the top of this README.

## Testing

### Run locally

Run the two servers in separate terminals. Locally, the MCP server calls the CPU API on `http://127.0.0.1:3001` and sends unsigned requests, because signing applies only to `https` URLs:

```bash
cd cpu-api && npm start
```

```bash
cd mcp-server && npm install && npm start
```

In a third terminal, start the MCP Inspector and connect to `http://127.0.0.1:3000/mcp` with transport type **Streamable HTTP**:

```bash
cd mcp-server && npm run inspect
```

### With curl

Set the MCP server URL printed by the second deploy:

```bash
export YOUR_ENDPOINT="https://<domain>.lambda-web.us-east-1.on.aws"
```

Call `run_cpu_work` with a `progressToken` and watch the progress messages arrive one second apart. `-N` turns off curl's output buffering so each event prints as it arrives:

```bash
curl -sN "$YOUR_ENDPOINT/mcp" \
  -H 'Content-Type: application/json' \
  -H 'Accept: application/json, text/event-stream' \
  -H 'MCP-Protocol-Version: 2025-06-18' \
  -d '{"jsonrpc":"2.0","id":1,"method":"tools/call","params":{"name":"run_cpu_work","arguments":{"seconds":5},"_meta":{"progressToken":1}}}'
```

The stream ends with the result, which names the execution environments of both functions:

```
event: message
data: {"jsonrpc":"2.0","method":"notifications/progress","params":{"progressToken":1,"progress":1,"total":5,"message":"1 of 5 s: 580,400 hashes"}}
...
event: message
data: {"result":{...,"structuredContent":{"requestedSeconds":5,"hashes":2932000,"hashesPerSecond":581280,"elapsedMs":5052,"region":"us-east-1","backendInstanceId":"1023078a","mcpInstanceId":"9a3358e0"}},"jsonrpc":"2.0","id":1}
```

Call `get_current_time`:

```bash
curl -s "$YOUR_ENDPOINT/mcp" \
  -H 'Content-Type: application/json' \
  -H 'Accept: application/json, text/event-stream' \
  -H 'MCP-Protocol-Version: 2025-06-18' \
  -d '{"jsonrpc":"2.0","id":2,"method":"tools/call","params":{"name":"get_current_time","arguments":{"timeZone":"Europe/London"}}}'
```

It returns in well under a second even while a `run_cpu_work` call is running.

Confirm that the CPU API can't be called directly. An unsigned request gets `403 Forbidden`:

```bash
curl -s -o /dev/null -w '%{http_code}\n' -X POST "https://$API_DOMAIN/work" -d '{"seconds":1}'
```

### From an MCP client

Add the MCP server to your client as a remote server over HTTP, using the MCP endpoint `https://<domain>.lambda-web.us-east-1.on.aws/mcp`.

**Kiro.** Add the server to `~/.kiro/settings/mcp.json` (all workspaces) or `.kiro/settings/mcp.json` (one workspace):

```json
{
  "mcpServers": {
    "lambda-web-mcp-server": {
      "url": "https://<domain>.lambda-web.us-east-1.on.aws/mcp"
    }
  }
}
```

Kiro picks up the change automatically. In Kiro IDE the server appears in the MCP Servers panel; from the terminal, run `kiro-cli chat` and check it with `/mcp`.

**Claude Code.** Add the server with one command. `--scope user` makes it available in every project:

```bash
claude mcp add --transport http --scope user lambda-web-mcp-server https://<domain>.lambda-web.us-east-1.on.aws/mcp
```

Run `claude mcp list` to confirm it connects, or `/mcp` inside a Claude Code session.

**Prompts to try:**

* "What time is it in Tokyo?" calls `get_current_time`.
* "Is it working hours in Sydney right now?" calls `get_current_time` with a time zone the agent works out.
* "Run 10 seconds of CPU work and tell me how many hashes it computed." calls `run_cpu_work`, which calls the CPU API.
* "Run two 5-second CPU jobs at the same time and compare the results." The agent makes two `run_cpu_work` calls. Compare `backendInstanceId` and `elapsedMs` to see whether the CPU API served them from one execution environment or two.
* "Start 15 seconds of CPU work, and while it runs, tell me the time in London." `get_current_time` answers straight away, because the hashing runs in the CPU API and not on the MCP server.

Some clients show only the final result of `run_cpu_work`, not the progress updates. Use the MCP Inspector or curl (above) to watch the stream.

To remove the server when you clean up, delete its entry from Kiro's `mcp.json`, or run `claude mcp remove --scope user lambda-web-mcp-server`.

## Cleanup

Delete the resources in the reverse order of deployment, using the same `STACK` value as the deploy.

1. Delete both functions. This also removes their endpoints and revisions:
    ```bash
    aws lambda-web delete-web-function --function-name $STACK-mcp
    aws lambda-web delete-web-function --function-name $STACK-cpu-api
    ```
1. Delete both execution roles. Their inline policies must be removed before the roles can be deleted:
    ```bash
    aws iam delete-role-policy --role-name $STACK-mcp-role --policy-name invoke-cpu-api-and-logs
    aws iam delete-role --role-name $STACK-mcp-role
    aws iam delete-role-policy --role-name awscli-lambdaweb-$STACK-cpu-api --policy-name awscli-lambdaweb-logs
    aws iam delete-role --role-name awscli-lambdaweb-$STACK-cpu-api
    ```
1. Delete the CloudWatch log groups. A group that was never created returns a harmless "does not exist" error:
    ```bash
    for name in $STACK-mcp $STACK-cpu-api; do
      aws logs delete-log-group --log-group-name /aws/lambda/web/$name
      aws logs delete-log-group --log-group-name /aws/lambda/web/$name.local
    done
    ```
1. The deploy also provisions a versioned artifact S3 bucket named `awscli-lambdaweb-<account-id>-<region>-<identifier>`. It is shared by all Web Functions you deploy in that Region, so leave it in place unless you have removed every Web Function. In that case, empty and delete it:
    ```bash
    aws s3 rb s3://<bucket-name> --force
    ```

----
Copyright 2026 Amazon.com, Inc. or its affiliates. All Rights Reserved.

SPDX-License-Identifier: MIT-0
