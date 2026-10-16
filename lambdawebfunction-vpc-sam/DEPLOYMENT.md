# Deployment Guide — lambdawebfunction-vpc-sam

Exact commands to package, deploy, test, and tear down this pattern. For the architecture overview and how it works, see [README.md](README.md).

> **Shortcut:** `./deploy.sh --vpc-id vpc-aaa --subnets subnet-aaa,subnet-bbb` from the solution directory automates everything in steps 1–3 below (region resolution, bucket creation, zip + upload + version capture, `sam build`, and `sam deploy` with the VPC parameters). `--security-groups` is optional — omit it to have the stack create an egress-only security group. The steps here are the manual equivalent, useful when you want to run each stage yourself or understand what the script does.

## Prerequisites

- An AWS account with permissions to manage Lambda Web Functions, Lambda network connectors, IAM, EC2 (ENIs), and S3.
- [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html) installed and configured.
- [AWS SAM CLI](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-sam-cli-install.html) installed.
- A way to send a SigV4-signed HTTP request to the `IamAuth` endpoint for testing (Step 5). The approach shown there uses `python3` with `botocore` (the AWS SDK), which is already available in AWS CloudShell and on any machine with the AWS CLI installed — no extra tooling required.
- A deployment Region where Lambda Web Functions is available: `us-east-1`, `us-east-2`, `us-west-2`, `ap-northeast-1`, or `eu-west-1`.
- An existing VPC with:
  - One or more **private subnets** (two or more in different Availability Zones recommended for resilience).
  - **Egress** to any AWS services your app calls (e.g. Amazon S3) via a **NAT gateway** or **VPC interface/gateway endpoints**.
  - Optionally, a **security group** permitting the outbound traffic your app needs (one is typical; attach more only if you compose SGs). If you don't provide any, the stack creates an egress-only security group for you.
- An Amazon S3 bucket (versioning recommended) for the Web Function `.zip` deployment package.

Set shell variables used throughout:

    export AWS_REGION=us-east-1
    export STACK_NAME=lambdawebfunction-vpc
    export CODE_BUCKET=amzn-s3-demo-bucket          # your existing S3 bucket
    export CODE_KEY=web-function/app.zip
    export VPC_ID="vpc-aaaaaaaa"                               # the VPC your subnets belong to
    export SUBNET_IDS="subnet-aaaaaaaa,subnet-bbbbbbbb"        # private subnets, different AZs
    export SG_IDS=""                                          # optional; blank = stack creates an egress-only SG
    export NETWORK_PROTOCOL=IPv4                               # or DualStack

## 1. Package the Web Function code and upload to Amazon S3

Lambda Web Functions are deployed **only** from an S3 object. Zip the contents of `src/` with the entry file (`index.js`) at the root of the archive, then upload:

    cd src
    zip -r ../app.zip .
    cd ..
    aws s3 cp app.zip "s3://${CODE_BUCKET}/${CODE_KEY}" --region "${AWS_REGION}"

If your bucket has versioning enabled, capture the uploaded object's version ID so you can pin the revision to it:

    export CODE_VERSION_ID=$(aws s3api head-object \
      --bucket "${CODE_BUCKET}" \
      --key "${CODE_KEY}" \
      --region "${AWS_REGION}" \
      --query VersionId --output text)
    echo "Uploaded version: ${CODE_VERSION_ID}"

## 2. Build

    sam build

## 3. Deploy

### Guided (first deploy)

    sam deploy --guided

Answer the prompts:

| Prompt | Value |
|---|---|
| Stack Name | `${STACK_NAME}` |
| AWS Region | `${AWS_REGION}` (a Web Functions Region, see Prerequisites) |
| Parameter CodeBucket | `${CODE_BUCKET}` |
| Parameter CodeKey | `${CODE_KEY}` |
| Parameter CodeVersionId | `${CODE_VERSION_ID}` (optional; leave blank if not versioning) |
| Parameter VpcId | `${VPC_ID}` |
| Parameter VpcSubnetIds | `${SUBNET_IDS}` |
| Parameter VpcSecurityGroupIds | `${SG_IDS}` (optional; leave blank to auto-create an egress-only SG) |
| Parameter NetworkProtocol | `${NETWORK_PROTOCOL}` |
| Confirm changes before deploy | Y |
| Allow SAM CLI IAM role creation | Y |
| Disable rollback | N |
| Save arguments to configuration file | Y |

### Non-interactive (CI / repeat deploys)

    sam deploy \
      --stack-name "${STACK_NAME}" \
      --region "${AWS_REGION}" \
      --capabilities CAPABILITY_IAM \
      --resolve-s3 \
      --no-confirm-changeset \
      --parameter-overrides \
        CodeBucket="${CODE_BUCKET}" \
        CodeKey="${CODE_KEY}" \
        CodeVersionId="${CODE_VERSION_ID}" \
        VpcId="${VPC_ID}" \
        VpcSubnetIds="${SUBNET_IDS}" \
        VpcSecurityGroupIds="${SG_IDS}" \
        NetworkProtocol="${NETWORK_PROTOCOL}"

> The template uses auto-named IAM roles, so `CAPABILITY_IAM` is sufficient — `CAPABILITY_NAMED_IAM` is not required.
>
> `VpcSubnetIds` and `VpcSecurityGroupIds` take **comma-separated** values (no spaces) in `--parameter-overrides`. Leave `VpcSecurityGroupIds` blank to have the stack create an egress-only security group in `VpcId`.

## 4. Get the stack outputs

    aws cloudformation describe-stacks \
      --stack-name "${STACK_NAME}" \
      --region "${AWS_REGION}" \
      --query "Stacks[0].Outputs" --output table

Key outputs:

- **WebFunctionEndpointDomain** — the endpoint domain (requests must be SigV4-signed; it is `IamAuth`).
- **NetworkConnectorLatestVersionArn** — the version-qualified connector ARN the revision pins to.

## 5. Test the VPC egress path

Point the sample at a private endpoint reachable only inside your VPC (for example an internal ALB, or a small HTTP server on EC2/ECS). The easiest way is the `--internal-target-url` flag on the deploy script, which sets `INTERNAL_TARGET_URL` on the new revision:

    ./deploy.sh --vpc-id "${VPC_ID}" --subnets "${SUBNET_IDS}" \
      --internal-target-url "http://<private-ip-or-internal-dns>/"

(With the manual `sam deploy`, add `InternalTargetUrl=http://.../` to `--parameter-overrides` instead.) Leave it unset and the page shows **Not configured**.

Then invoke the endpoint. Because it is `IamAuth`, the request must be **SigV4-signed with the service name `lambda`**. Invoke from inside the account (CloudShell, or EC2 with an instance role) so credentials are picked up and signed correctly. Replace `<WebFunctionEndpointDomain>` below with your endpoint domain from the stack outputs (`WebFunctionEndpointDomain`):

    python3 - <<'EOF'
    import urllib.request, hashlib
    import botocore.session
    from botocore.auth import SigV4Auth
    from botocore.awsrequest import AWSRequest
    url = "https://<WebFunctionEndpointDomain>/"
    creds = botocore.session.Session().get_credentials().get_frozen_credentials()
    req = AWSRequest(method="GET", url=url)
    req.headers["X-Amz-Content-SHA256"] = hashlib.sha256(b"").hexdigest()  # required empty-body hash
    SigV4Auth(creds, "lambda", "us-east-1").add_auth(req)
    resp = urllib.request.urlopen(urllib.request.Request(url, headers=dict(req.headers)))
    body = resp.read().decode()
    print()  # blank line so the output is separated from the command above
    print("=" * 60)
    print(f"HTTP {resp.status}  |  {len(body)} bytes")
    print("=" * 60)
    print(body)
    EOF

The in-account invoke script prints a header (`HTTP 200 | <N> bytes`) before the HTML so the
response stands out in the terminal. The returned page reports one of three egress states:

| State | When | What the page shows |
|---|---|---|
| **Not configured** | `InternalTargetUrl` / `--internal-target-url` not set | Amber "Not configured" with a prompt to set the target. The endpoint works; the probe just didn't run. |
| **Reachable** | Target set and responded | Green "Reachable" plus a **Response from private target** panel: HTTP status, latency, content-type, size, and a snippet of the actual response body. End-to-end egress proof. |
| **Unreachable** | Target set but the call failed | Red "Unreachable" with the reason (e.g. `timeout (check routing / security groups)`). Check subnet routing and that the target's security group allows inbound from the connector's security group. |

## 6. Deploy new code (new revisions)

Revisions are immutable. Upload a new `.zip` and redeploy to create a new revision:

    cd src && zip -r ../app.zip . && cd ..
    aws s3 cp app.zip "s3://${CODE_BUCKET}/${CODE_KEY}" --region "${AWS_REGION}"
    # re-capture CODE_VERSION_ID (step 1) if versioning, then redeploy (step 3)

## 7. Production hardening

This template ships a working baseline with conservative endpoint caps already set — `ThrottleConfig.RateLimit: 100` and `ScalingConfig.MaxEnvironments: 10` on `MyWebFunctionEndpoint` (with `MaxConcurrencyPerEnvironment: 64`, a 640 concurrent-request ceiling). Before production, also consider:

- **Tune the endpoint caps** to your expected peak RPS and concurrency (`RateLimit` accepts 0, 100–1000 in steps of 100, or 2000–10000 in steps of 1000).
- **Scope the connector's security group egress** — the auto-created group allows all outbound (`0.0.0.0/0`); restrict it to the destinations your function actually calls, or bring your own via `VpcSecurityGroupIds`.
- **Set CloudWatch Logs retention** on the auto-created log group(s) (no expiration by default).
- **Handle `SIGTERM`** in your app to drain in-flight work before shutdown.
- **Supply a customer-managed KMS key** via the revision's `KmsKeyArn` for compliance-driven workloads.

See the "Production hardening" section in [README.md](README.md) for the full rationale on each.

## 8. Clean up

    sam delete --stack-name "${STACK_NAME}" --region "${AWS_REGION}"

Deleting the stack removes the Web Function, its revisions and endpoint, and the network connector (including all its versions). The deployment package object(s) in S3 are not removed; delete them separately if no longer needed:

    aws s3 rm "s3://${CODE_BUCKET}/${CODE_KEY}" --region "${AWS_REGION}"
