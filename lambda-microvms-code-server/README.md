# VS Code Server (code-server) on AWS Lambda MicroVMs

This pattern deploys **VS Code Server (code-server)** inside an AWS Lambda MicroVMs. It gives you a full VS Code IDE accessible from your browser, running in a Firecracker-isolated sandbox with Python, AWS CLI, and project persistence.

The Lambda MicroVM image is built declaratively via CloudFormation using the `AWS::Lambda::MicrovmImage` resource with full lifecycle hook management (ready, run, suspend, resume, terminate).

Learn more about this pattern at Serverless Land Patterns: https://serverlessland.com/patterns/lambda-microvms-code-server

Important: this application uses various AWS services and there are costs associated with these services after the Free Tier usage - please see the [AWS Pricing page](https://aws.amazon.com/pricing/) for details. You are responsible for any AWS costs incurred. No warranty is implied in this example.

## How it works

1. **Image Build**: CloudFormation creates the `AWS::Lambda::MicrovmImage` resource. Lambda downloads the zip from S3, executes the Dockerfile (installs code-server, Python, AWS CLI), starts the lifecycle hooks handler on port 9000, and waits for `/ready`. Once ready, Lambda takes a snapshot.
2. **Run**: The Lambda MicroVM resumes from snapshot in under a second. The `/run` hook fires with the `microVmId`.
3. **Connect**: You generate an auth token and use the local proxy (`proxy.py`) to access code-server through your browser.
4. **Suspend/Resume**: After idle, the VM suspends (the `/suspend` hook fires). On the next request it resumes (the `/resume` hook fires). State is preserved across cycles.
5. **Terminate**: When the VM is terminated, the `/terminate` hook fires for graceful cleanup.


## Prerequisites

- Updated [AWS CLI v2](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-getting-started.html) (with `lambda-microvms` subcommand available)
- [Git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)
- Python 3.14+ — for the local proxy
- `aiohttp` — for the WebSocket-capable proxy

### Install proxy dependencies

```bash
pip3 install aiohttp
```

## Deployment

### Quick Start (deploy.sh)

`deploy.sh` automates the entire deployment (bucket creation, packaging, CloudFormation deploy, and running the MicroVM):

```bash
export ACCOUNT_ID="YOUR-ACCOUNT-ID"
export AWS_REGION="us-east-2"          # optional, defaults to us-east-2
chmod +x deploy.sh
./deploy.sh
```

The script prints the MicroVM ID and endpoint when complete. Then get a token and connect:

```bash
MICROVM_ID="<from deploy output>"
ENDPOINT="<from deploy output>"

TOKEN=$(aws lambda-microvms create-microvm-auth-token \
  --microvm-identifier "${MICROVM_ID}" \
  --expiration-in-minutes 60 \
  --allowed-ports allPorts={} \
  --region "${AWS_REGION}" \
  --query 'authToken."X-aws-proxy-auth"' --output text)

python3 proxy.py "https://${ENDPOINT}" "${TOKEN}"
```

### Manual Step-by-Step

If you prefer to run each step individually:

#### Step 1: Set configuration

```bash
export ACCOUNT_ID="YOUR-ACCOUNT-ID"
export AWS_REGION="us-east-2"
export S3_BUCKET="microvm-artifacts-${ACCOUNT_ID}"
```

#### Step 2: Create S3 bucket

The image build pulls the code artifact from S3.

```bash
aws s3 mb "s3://${S3_BUCKET}" --region "${AWS_REGION}"
```

#### Step 3: Package and upload

Zip the `src/` directory (Dockerfile + app.py + start.sh) and upload to S3.

```bash
cd src && zip -r /tmp/app.zip . && cd -
aws s3 cp /tmp/app.zip "s3://${S3_BUCKET}/deployments/code-server.zip" --region "${AWS_REGION}"
```

#### Step 4: Deploy infrastructure (CloudFormation)

The template creates two IAM roles (build + execution) and builds the MicroVM image with full lifecycle hooks. The image build takes 3–5 minutes (installs code-server, Python, AWS CLI).

```bash
aws cloudformation deploy \
  --template-file template.yaml \
  --stack-name lambda-microvm-code-server \
  --parameter-overrides \
      S3Bucket="${S3_BUCKET}" \
      S3Key="deployments/code-server.zip" \
      ImageName="code-server" \
  --capabilities CAPABILITY_NAMED_IAM \
  --region "${AWS_REGION}"
```

#### Step 5: Run the MicroVM

Start the Lambda MicroVM with the `HTTP_INGRESS` connector for browser access.

```bash
IMAGE_ARN=$(aws cloudformation describe-stacks \
  --stack-name microvm-code-server --region "${AWS_REGION}" \
  --query 'Stacks[0].Outputs[?OutputKey==`ImageArn`].OutputValue' --output text)

EXEC_ROLE_ARN=$(aws cloudformation describe-stacks \
  --stack-name microvm-code-server --region "${AWS_REGION}" \
  --query 'Stacks[0].Outputs[?OutputKey==`ExecutionRoleArn`].OutputValue' --output text)

LAUNCH=$(aws lambda-microvms run-microvm \
  --image-identifier "${IMAGE_ARN}" \
  --execution-role-arn "${EXEC_ROLE_ARN}" \
  --ingress-network-connectors '["arn:aws:lambda:'"${AWS_REGION}"':aws:network-connector:aws-network-connector:HTTP_INGRESS"]' \
  --egress-network-connectors '["arn:aws:lambda:'"${AWS_REGION}"':aws:network-connector:aws-network-connector:INTERNET_EGRESS"]' \
  --idle-policy '{"maxIdleDurationSeconds":3600,"suspendedDurationSeconds":1800,"autoResumeEnabled":true}' \
  --logging '{"cloudWatch":{"logGroup":"/aws/lambda-microvms/code-server"}}' \
  --region "${AWS_REGION}")

echo "${LAUNCH}" | python3 -c "import sys,json; d=json.load(sys.stdin); print(f'MicroVM ID: {d[\"microvmId\"]}'); print(f'Endpoint: https://{d[\"endpoint\"]}')"
```

Note the `microvmId` and `endpoint` from the output.

#### Step 6: Connect via proxy

```bash
# Get an auth token (60-minute TTL)
TOKEN=$(aws lambda-microvms create-microvm-auth-token \
  --microvm-identifier "${MICROVM_ID}" \
  --expiration-in-minutes 60 \
  --allowed-ports allPorts={} \
  --region "${AWS_REGION}" \
  --query 'authToken."X-aws-proxy-auth"' --output text)

# Open code-server in your browser via local proxy
python3 proxy.py "https://${ENDPOINT}" "${TOKEN}"
```

The proxy opens `http://127.0.0.1:8080` in your browser with VS Code ready.

## Lifecycle Hooks

The CloudFormation template configures all lifecycle hooks on port 9000:

| Hook | Purpose | Timeout |
|------|---------|---------|
| `/ready` | Signals image build is complete, snapshot taken | 300s |
| `/run` | Fires when MicroVM starts, provides `microVmId` | 5s |
| `/suspend` | Fires before suspension — flush state | 5s |
| `/resume` | Fires after resumption — restore connections | 5s |
| `/terminate` | Fires before termination — graceful shutdown | 5s |

The `app.py` handler responds to these hooks and logs each transition for observability.

## Project Structure

```
├── README.md                       # This file
├── template.yaml                   # CloudFormation (IAM + MicrovmImage with hooks)
├── deploy.sh                       # Full deployment script
├── proxy.py                        # Local HTTP+WebSocket proxy for browser access
├── example-pattern.json            # Serverless Land pattern metadata
└── src/
    ├── Dockerfile                  # code-server container image
    ├── app.py                      # Lifecycle hooks + health endpoint
    └── start.sh                    # Entrypoint: hooks + code-server
```

## Testing

1. Deploy the stack and run a MicroVM (see above).

2. Get a token and start the proxy:
   ```bash
   python3 proxy.py "https://${ENDPOINT}" "${TOKEN}"
   ```

3. Open `http://127.0.0.1:8080` — you should see VS Code.

4. Open a terminal inside VS Code and verify:
   ```bash
   python3 --version
   aws --version
   ```

5. Test health endpoint:
   ```bash
   curl "https://${ENDPOINT}/healthz" -H "X-aws-proxy-auth: ${TOKEN}"
   ```

## Cleanup

```bash
# 1. Terminate the running MicroVM
aws lambda-microvms terminate-microvm \
  --microvm-identifier "${MICROVM_ID}" \
  --region us-east-2

# 2. Delete the CloudFormation stack (removes IAM roles + image)
aws cloudformation delete-stack --stack-name microvm-code-server --region us-east-2

# 3. Delete S3 artifacts
aws s3 rm "s3://${S3_BUCKET}/deployments/" --recursive
```

---

Copyright 2026 Amazon.com, Inc. or its affiliates. All Rights Reserved.

SPDX-License-Identifier: MIT-0
