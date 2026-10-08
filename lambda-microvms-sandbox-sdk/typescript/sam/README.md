# Code sandboxes on AWS Lambda MicroVMs with a sandbox SDK

This pattern deploys an AWS Lambda MicroVM image that turns each MicroVM into a code sandbox you drive from TypeScript or Python with [Rayito](https://alejandro-cedeno-10.github.io/rayito/), an open-source (Apache-2.0) sandbox SDK. A short TypeScript client creates a sandbox, runs stateful Python code and shell commands, reads and writes files, and terminates it, in seconds and with a few lines of code. The same SDK is published for Python (`pip install rayito`) with matching sync and async APIs. Everything stays in your AWS account: no third-party service and no API key.

An optional part builds a second image with a coding agent (OpenCode) that calls a model in Amazon Bedrock. The model credential, a short-term Bedrock API key in AWS Secrets Manager, reaches Bedrock only through a secrets gateway inside the sandbox, so code in the sandbox can use the key but cannot read it.

Learn more about this pattern at Serverless Land Patterns: << Add the live URL here >>

Important: this application uses various AWS services and there are costs associated with these services after the Free Tier usage - please see the [AWS Pricing page](https://aws.amazon.com/pricing/) for details. You are responsible for any AWS costs incurred. No warranty is implied in this example.

## Requirements

* [Create an AWS account](https://portal.aws.amazon.com/gp/aws/developer/registration/index.html) if you do not already have one and log in. The IAM user that you use must have sufficient permissions to make necessary AWS service calls and manage AWS resources.
* [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html) installed and configured. Use a recent version: the `aws lambda-microvms` commands used in Cleanup are not in older releases.
* [Git Installed](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)
* [AWS Serverless Application Model](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-sam-cli-install.html) (AWS SAM) installed
* [Node.js](https://nodejs.org/) 20 or later, for the client
* Optional, recommended: [cosign](https://docs.sigstore.dev/cosign/system_config/installation/) 2.x or later, to verify the signature of the sandbox image artifact
* An AWS Region where [Lambda MicroVMs](https://docs.aws.amazon.com/lambda/latest/dg/lambda-microvms.html) is available. The commands below use `us-east-1`.
* Optional part only: access to the Amazon Bedrock model you want to use (the client defaults to Anthropic Claude Haiku 4.5 through the `us.` cross-Region inference profile).

## Deployment Instructions

1. Create a new directory, navigate to that directory in a terminal and clone the GitHub repository:
    ```bash
    git clone https://github.com/aws-samples/serverless-patterns
    ```
1. Change directory to the pattern directory:
    ```bash
    cd serverless-patterns/lambda-microvms-sandbox-sdk/typescript/sam
    ```
1. Set the Region, a stack name and a globally unique name for a new S3 bucket. The stack name prefixes every image and IAM resource it creates:
    ```bash
    export AWS_REGION=us-east-1
    export STACK_NAME=sandbox-sdk
    export ARTIFACT_BUCKET=amzn-s3-demo-bucket   # replace with a unique bucket name
    ```
1. Download the sandbox image artifact of the Rayito release, check its signature and checksum, and upload it to a new bucket. The zip holds the in-guest agent (`rayd`) and its Dockerfile; Lambda builds the image from it in your account.
    ```bash
    RAYITO_VERSION=0.10.0
    BASE=https://github.com/alejandro-cedeno-10/rayito/releases/download/rayd-v${RAYITO_VERSION}
    curl -fsSLO "$BASE/rayito-image.zip"
    curl -fsSLO "$BASE/rayito-image.zip.sigstore.json"
    curl -fsSLO "$BASE/SHA256SUMS"

    # Optional, recommended: must print "Verified OK"
    cosign verify-blob --bundle rayito-image.zip.sigstore.json \
      --certificate-identity "https://github.com/alejandro-cedeno-10/rayito/.github/workflows/release.yml@refs/tags/rayd-v${RAYITO_VERSION}" \
      --certificate-oidc-issuer https://token.actions.githubusercontent.com \
      rayito-image.zip
    shasum -a 256 -c --ignore-missing SHA256SUMS   # on Linux: sha256sum -c --ignore-missing SHA256SUMS

    aws s3 mb "s3://${ARTIFACT_BUCKET}" --region "${AWS_REGION}"
    aws s3 cp rayito-image.zip "s3://${ARTIFACT_BUCKET}/rayito/rayito-image.zip"
    ```
    To reuse an existing bucket in the same Region instead, upload the zip under a key that starts with `rayito/` and add `ArtifactKey=<that key>` to `--parameter-overrides` in the next step. The build role can read only `rayito/*` of the bucket.
1. From the command line, use AWS SAM to deploy the AWS resources for the pattern as specified in the template.yaml file. CloudFormation waits until Lambda has built the image, which takes about 5 minutes:
    ```bash
    sam deploy --template-file template.yaml --stack-name "${STACK_NAME}" --region "${AWS_REGION}" \
      --capabilities CAPABILITY_IAM \
      --parameter-overrides ArtifactBucket="${ARTIFACT_BUCKET}"
    ```
    The template has no local artifacts to upload, so this command does not need an S3 bucket for SAM. You can also run `sam deploy --guided` and answer the prompts (stack name, Region, `ArtifactBucket`, and allow SAM CLI to create IAM roles); guided mode creates the SAM managed bucket stack (`aws-sam-cli-managed-default`) if your account does not have it yet.

1. Note the outputs from the SAM deployment process. `SandboxImageName` is the image the client uses, and `SandboxLauncherPolicyArn` is the least-privilege policy for the identity that runs the client:
    ```bash
    aws cloudformation describe-stacks --stack-name "${STACK_NAME}" --query "Stacks[0].Outputs" --output table
    ```

## How it works

The stack creates only AWS resources:

* An `AWS::Lambda::MicrovmImage` built on the AWS managed Amazon Linux 2023 base image (`al2023-1`) from `rayito-image.zip`. The zip contains `rayd`, a small static agent written in Rust that serves the MicroVM lifecycle hooks on port 9000 (`/ready`, `/validate`, `/run`, `/suspend`, `/resume`, `/terminate`) and a gRPC API for processes, files and a Python (Jupyter) kernel. Lambda boots the image, waits for `/ready`, checks it with `/validate`, and snapshots it, so every sandbox starts from a warm snapshot: `Sandbox.create()` returns in under 10 seconds with the Python kernel ready.
* An IAM build role that Lambda assumes to read the artifact and write build logs, and an Amazon CloudWatch Logs log group with 7-day retention for each image.
* `SandboxLauncherPolicy`, a customer managed policy with the runtime actions only: run, get, suspend, resume and terminate MicroVMs of this stack's images, mint their auth tokens, and pass the AWS managed network connectors. It cannot change an image.

The client uses the `rayito` npm package. `Sandbox.create()` calls `RunMicrovm`, mints a MicroVM auth token with `CreateMicrovmAuthToken`, and talks to `rayd` over the MicroVM endpoint with that token and a per-sandbox access token. `runCode()`, `commands.run()` and `files.*` are calls to `rayd`. `kill()` calls `TerminateMicrovm`. Each sandbox is one MicroVM with its own kernel, memory and disk.

With `EnableAgent=true` the stack also builds `<stack>-base-caps`, the same artifact with additional OS capabilities, which `rayd` needs to block Internet access inside the guest, and creates `AgentImageBuilderPolicy`. `src/build-agent-image.ts` composes `<stack>-agent` on top of it with the OpenCode runtime, and `src/agent.ts` runs a coding agent in a sandbox that has no Internet access: its only way out is a gateway in `rayd` that adds the Bedrock API key (read from Secrets Manager by the client) to requests for one allowed model. This part is off by default and adds no resources or cost until you enable it.

## Testing

1. Install the client dependencies:
    ```bash
    cd src
    npm ci
    ```
1. Run the sandbox client. It creates a sandbox, runs Python code twice to show that variables persist, runs a shell command, writes and runs a script, reads its output, lists the directory and terminates the sandbox:
    ```bash
    export RAYITO_TEMPLATE="${STACK_NAME}-base"
    npm run sandbox
    ```
    Expected output (IDs and times vary):
    ```text
    sandbox microvm-00000000-0000-0000-0000-000000000001 ready in 8531 ms
    runCode: 42
    commands.run: 0 Linux aarch64
    files.read: hello from the MicroVM
    files.list: hello.py, out.txt
    done in 10044 ms; terminating microvm-00000000-0000-0000-0000-000000000001
    ```
1. Check that no sandbox is left running (the list must not show a `RUNNING` MicroVM of your images):
    ```bash
    aws lambda-microvms list-microvms --query "items[?state!='TERMINATED'].[microvmId,state,imageArn]" --output table
    ```

### Optional: coding agent with Amazon Bedrock

1. Enable the agent part. CloudFormation builds the `<stack>-base-caps` image (about 5 minutes):
    ```bash
    cd ..
    sam deploy --template-file template.yaml --stack-name "${STACK_NAME}" --region "${AWS_REGION}" \
      --capabilities CAPABILITY_IAM \
      --parameter-overrides ArtifactBucket="${ARTIFACT_BUCKET}" EnableAgent=true
    cd src
    ```
1. Build the agent image (about 5 minutes; it downloads the pinned OpenCode release during the build):
    ```bash
    npm run build-agent-image
    ```
1. Run the agent. The client mints a short-term Bedrock API key with your current credentials, stores it in Secrets Manager as `rayito/<stack>-bedrock-key`, creates a sandbox without Internet access and asks the agent to fix a bug in a small file:
    ```bash
    npm run agent
    ```
    Expected output (the agent's wording varies):
    ```text
    agent: The bug has been fixed. The `add` function was returning `a - b` instead of `a + b`. After the fix, `add(5, 3)` correctly returns `8`.
    steps: 5 tokens: 39959
    app.py now:
    def add(a, b):
        return a + b
    ```
    To use another model, redeploy with `AgentModelId=<inference profile ID>` and export the same `MODEL_ID` before `npm run agent`.

### Permissions for the client

The commands above work with administrator credentials. To run the client with least privilege, attach the stack's customer managed policies to the IAM role or user that runs it:

| Script | Policies (stack outputs) |
|---|---|
| `npm run sandbox` | `SandboxLauncherPolicyArn` |
| `npm run build-agent-image` | `AgentImageBuilderPolicyArn` |
| `npm run agent` | `SandboxLauncherPolicyArn`, `AgentImageBuilderPolicyArn` (stores the key in Secrets Manager) and `ModelInvokePolicyArn` (the short-term Bedrock API key carries the permissions of the identity that mints it) |

A service that only creates sandboxes needs `SandboxLauncherPolicyArn` alone: it can run sandboxes from this stack's images but cannot change an image.

## Cleanup

1. If you ran the optional agent part, delete the agent image (it is not managed by the stack) and the secret:
    ```bash
    AGENT_IMAGE_ARN=$(aws lambda-microvms list-microvm-images --query "items[?name=='${STACK_NAME}-agent'].imageArn" --output text)
    aws lambda-microvms delete-microvm-image --image-identifier "${AGENT_IMAGE_ARN}"
    aws secretsmanager delete-secret --secret-id "rayito/${STACK_NAME}-bedrock-key" --force-delete-without-recovery
    ```
1. Delete the stack. This deletes the images, roles, policies and log groups it created:
    ```bash
    sam delete --stack-name "${STACK_NAME}" --region "${AWS_REGION}" --no-prompts
    ```
    If you deployed without `--guided`, `sam delete` warns that it cannot resolve an S3 bucket: the pattern uploads nothing for SAM, so there is nothing to delete there.
1. Delete the artifact bucket and everything in it (the release zip and, if you built the agent image, its artifact):
    ```bash
    aws s3 rb "s3://${ARTIFACT_BUCKET}" --force
    ```
1. Confirm the stack has been deleted
    ```bash
    aws cloudformation list-stacks --query "StackSummaries[?contains(StackName,'${STACK_NAME}')].StackStatus"
    ```

## Cost

Sandboxes are billed only while they run or are suspended: a 2 GB sandbox costs about $0.13 per hour in us-east-1, so the test run above costs well under one cent. Each image version is billed for snapshot storage, with a minimum of one week per version: about $0.04 for `<stack>-base` and the same for `<stack>-base-caps`, and about $0.06 for `<stack>-agent`. The optional agent part also pays for the Bedrock tokens it uses (a few cents with Claude Haiku 4.5) and for the secret ($0.40 per month, pro-rated). See [AWS Lambda pricing](https://aws.amazon.com/lambda/pricing/).

----
Copyright 2026 Amazon.com, Inc. or its affiliates. All Rights Reserved.

SPDX-License-Identifier: MIT-0
