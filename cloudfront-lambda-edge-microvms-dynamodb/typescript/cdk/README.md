# Session routing to AWS Lambda MicroVMs with Amazon CloudFront, Lambda@Edge and Amazon DynamoDB

Give every session its own AWS Lambda MicroVM behind a single Amazon CloudFront URL. A session id in the request path (`/s/{sessionId}/...`) or query string (`?session={sessionId}`) selects the VM. An Amazon DynamoDB table maps session id → MicroVM. A Lambda@Edge origin-request function does the routing; a regional control-plane AWS Lambda function launches the MicroVM on demand. The app inside each MicroVM is a Node.js hello-world that returns its own session id, so `/s/A` and `/s/B` land on two different MicroVMs.

Learn more about this pattern at Serverless Land Patterns: << Add the live URL here >>

Important: this application uses various AWS services and there are costs associated with these services after the Free Tier usage - please see the [AWS Pricing page](https://aws.amazon.com/pricing/) for details. You are responsible for any AWS costs incurred. No warranty is implied in this example.

## Requirements

* [Create an AWS account](https://portal.aws.amazon.com/gp/aws/developer/registration/index.html) if you do not already have one and log in. The IAM user that you use must have sufficient permissions to make necessary AWS service calls and manage AWS resources.
* [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html) installed and configured
* [Git Installed](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)
* [Node.js 22+](https://nodejs.org/en/download). The AWS CDK CLI is a dev dependency, so `npx cdk` works without a global install. No local Docker is needed: the MicroVM image is built by the service.
* [AWS Lambda MicroVMs](https://docs.aws.amazon.com/lambda/latest/dg/lambda-microvms-guide.html) available in your account in `us-east-1`. The stack deploys entirely in `us-east-1` because Lambda@Edge functions can only be created there.

## Deployment Instructions

1. Create a new directory, navigate to that directory in a terminal and clone the GitHub repository:
    ```
    git clone https://github.com/aws-samples/serverless-patterns
    ```
1. Change directory to the pattern directory:
    ```
    cd serverless-patterns/cloudfront-lambda-edge-microvms-dynamodb/typescript/cdk
    ```
1. Install dependencies:
    ```
    npm install
    ```
1. If this is your first CDK deployment in the account and `us-east-1`, bootstrap it:
    ```
    npx cdk bootstrap
    ```
1. Deploy the stack:
    ```
    npx cdk deploy
    ```
1. Note the `DistributionUrl` output. You need it for testing.

The first deployment builds the MicroVM image and creates the CloudFront distribution, so it takes several minutes.

## How it works

For an interactive, step-by-step walkthrough, open [`explainer.html`](explainer.html) from your clone in a browser (GitHub shows its source rather than rendering it).

```mermaid
flowchart TD
    V[Viewer] -->|"/s/{id}/..."| CF[Amazon CloudFront]
    CF -->|default behavior: origin-request| E[Lambda@Edge router]
    E -->|GetItem session| D[(Amazon DynamoDB)]
    E -->|usable: rewrite origin + Host + token| M[Per-session Lambda MicroVM :8080]
    E -->|not usable: 307 to /_control| CF
    CF -->|"/_control* via Function URL + OAC"| C[Control-plane Lambda]
    C -->|conditional put = launch claim| D
    C -->|RunMicrovm / CreateMicrovmAuthToken| M
    C -->|307 back with _attempt=1| CF
```

1. A viewer requests `https://<distribution>/s/{sessionId}/...` (or `...?session={sessionId}`).
2. CloudFront runs the **Lambda@Edge** origin-request function. It validates the session id (`^[A-Za-z0-9_-]{1,64}$`, otherwise `400`) and reads the session from DynamoDB. Lambda@Edge has no environment variables, so the table name and Region reach the function as custom headers on the CloudFront origin.
3. **If the session has a valid token**, the function points the request at the MicroVM endpoint, sets the `Host` header to match, adds the `x-aws-proxy-auth` token and `x-aws-proxy-port: 8080`, and strips the `/s/{id}` prefix.
4. **Otherwise** it 307-redirects to `/_control?session=...&return=...`. CloudFront sends `/_control*` to the **control-plane Lambda** through an IAM-auth **Function URL** protected by **Origin Access Control**. The control plane attaches to the session's MicroVM or launches one, mints a token, stores it, and 307-redirects back with `_attempt=1`. It only redirects to relative paths, so it can't be used as an open redirect.
5. If the session still isn't usable on the `_attempt=1` retry, the edge returns `503` instead of redirecting again.

A conditional DynamoDB put is the launch lock: when two requests for a new session arrive together, only one launches a MicroVM; the other gets a `503 launch in progress` and succeeds on retry.

## Testing

After `npx cdk deploy`, set `URL` to the `DistributionUrl` output:

```bash
URL=https://<distribution-id>.cloudfront.net
```

1. Open two sessions. The first request to each follows a redirect chain while its MicroVM launches (a few seconds):
    ```bash
    curl -sL "$URL/s/session-a/"
    curl -sL "$URL/s/session-b/"
    ```
    Each response is JSON from that session's own MicroVM, so the two `microvmId` values differ:
    ```json
    { "message": "Hello from session session-a", "sessionId": "session-a", "microvmId": "microvm-...", "path": "/", "startedAt": "...", "hits": 1 }
    ```
1. Request session-a again, this time with the query-string form. It reaches the same MicroVM directly, without a redirect, and `hits` goes up:
    ```bash
    curl -sL "$URL/?session=session-a"
    ```
1. Watch the redirect chain for a new session: a `307` to `/_control`, a `307` back, then `200`:
    ```bash
    curl -sIL "$URL/s/session-c/" | grep -iE "^HTTP|^location"
    ```

The control plane waits up to 20 seconds for a new MicroVM to boot. If a first request returns `500` (still booting) or `503` (another request is launching it), repeat it: the next request attaches to the MicroVM that is already booting.

## Cleanup

1. Terminate the MicroVMs you started. The `x-amz-content-sha256` header (the SHA-256 of an empty body) is required because CloudFront Origin Access Control needs the payload hash on `POST` requests to a Lambda Function URL:
    ```bash
    for s in session-a session-b session-c; do
      curl -s -X POST -H "x-amz-content-sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855" \
        "$URL/_control/terminate?session=$s"; echo
    done
    ```
    Otherwise the idle policy suspends a MicroVM after 15 idle minutes and terminates it after a further 30. To check for MicroVMs still running from this stack:
    ```bash
    aws lambda-microvms list-microvms --region us-east-1 \
      --image-identifier "arn:aws:lambda:us-east-1:$(aws sts get-caller-identity --query Account --output text):microvm-image:MicrovmEdgeSessionsStack-image" \
      --query "items[?state!='TERMINATED'].[microvmId,state]" --output text
    ```
1. Delete the stack:
    ```bash
    npx cdk destroy
    ```
1. CloudFront takes a few hours to delete the Lambda@Edge replicas, so the first `cdk destroy` usually ends in `DELETE_FAILED` on the edge function. Wait a few hours and run `npx cdk destroy` again.
1. Lambda@Edge writes logs to a `/aws/lambda/us-east-1.MicrovmEdgeSessionsStack-EdgeRouter...` log group in each Region where it ran. These aren't part of the stack; delete them in the CloudWatch console if you want.

## Limitations

* **No authentication.** The session id is the only key: anyone who knows a session id reaches that MicroVM. Add authentication before adapting this pattern.
* **Single-Region session table.** Edge locations far from `us-east-1` add latency to every lookup. For production, consider a [DynamoDB global table](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/GlobalTables.html).
* **First request must be a `GET`.** A first request redirects to the control plane with a 307, which keeps the method. A `POST` would reach the control plane's Function URL without the payload hash that Origin Access Control requires, and fail with `403`.
* **Path-prefix routing.** Stripping `/s/{id}` works for apps that use relative asset paths. For apps with absolute paths (`/assets/...`), route by subdomain instead.

## Gotchas

* **Rewrite the `Host` header, not just the origin.** When Lambda@Edge changes the origin, `Host` stays the viewer's host. The MicroVM endpoint is virtual-hosted, so a mismatched `Host` fails with *"Token authentication failed"*.
* **Hooks on port 9000, bound to `0.0.0.0`.** The service's `/ready` poller can't reach port 8081, and a bare `listen(port)` can bind IPv6-only. Either causes *"Ready hook invocation timed out"* and a `CREATE_FAILED` image. The app also answers `/ready` on port 8080, as a precaution in case the service polls the app port.
* **Base image versions expire.** The stack pins `baseImageVersion: "2"` of the managed AL2023 base. If image creation fails because that version is deprecated or expired, list the current versions and update the stack:
    ```bash
    aws lambda-microvms list-managed-microvm-image-versions --image-identifier arn:aws:lambda:us-east-1:aws:microvm-image:al2023-1 --region us-east-1
    ```
* **MicroVM IAM actions use the `lambda:` prefix** (`lambda:RunMicrovm`), not `lambda-microvms:`, and `RunMicrovm` also needs `lambda:PassNetworkConnector`.

----
Copyright 2026 Amazon.com, Inc. or its affiliates. All Rights Reserved.

SPDX-License-Identifier: MIT-0
