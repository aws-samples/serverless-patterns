# Code execution sandbox on AWS Lambda MicroVMs with a TypeScript SDK

This variant of the [code execution sandbox pattern](../../README.md) builds the same kind of sandbox, an AWS Lambda MicroVM that runs untrusted code in its own VM, but replaces the hand-written HTTP service and `curl` calls with an SDK. The MicroVM runs `rayd`, the agent of [Rayito](https://alejandro-cedeno-10.github.io/rayito/), an open-source (Apache-2.0) sandbox SDK. The author of this variant also maintains Rayito. A short TypeScript client creates sandboxes, runs code, runs shell commands, reads and writes files, pauses and resumes them, and keeps warm sandboxes in a pool. The SDK calls only AWS APIs, with your credentials, and needs no API key. `rayd` and the SDK are third-party code from the Rayito project, so review them as you would any dependency.

Learn more about this pattern at Serverless Land Patterns: << Add the live URL here >>

Important: this application uses various AWS services and there are costs associated with these services after the Free Tier usage - please see the [AWS Pricing page](https://aws.amazon.com/pricing/) for details. You are responsible for any AWS costs incurred. No warranty is implied in this example.

## What this variant adds

The [CloudFormation and Python pattern](../../README.md) in the parent folder ships its own Python HTTP service (`POST /execute`) in the image and you call it with `curl` and an auth token. This variant keeps the same building blocks (an `AWS::Lambda::MicrovmImage` built from a code artifact in Amazon S3, an IAM build role, the lifecycle hooks) and changes what runs inside and how you call it:

| | CloudFormation and Python | This variant |
|---|---|---|
| Template | CloudFormation | AWS SAM |
| In the MicroVM | A Python HTTP service that runs code in a subprocess | `rayd`, a static Rust agent from the Rayito release |
| Client | `curl` with a token from `create-microvm-auth-token` | The `rayito` npm package, in TypeScript |
| Running code | One request per snippet, stateless | A Python kernel: variables survive between `runCode` calls |
| Other operations | None | Shell commands, files, pause and resume, a pool of warm sandboxes |
| API shape | Custom | Rayito API, plus an entry point that implements a subset of the E2B API (`rayito/e2b`) |

The Python version is simpler and has nothing to download. Choose this variant if you want to drive sandboxes from application code through an SDK.

## Requirements

* [Create an AWS account](https://portal.aws.amazon.com/gp/aws/developer/registration/index.html) if you do not already have one and log in. The IAM user that you use must have sufficient permissions to make necessary AWS service calls and manage AWS resources.
* [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html) installed and configured. Use a recent version: the `aws lambda-microvms` commands used in Cleanup are not in older releases.
* [Git Installed](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)
* [AWS Serverless Application Model](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-sam-cli-install.html) (AWS SAM) installed
* [Node.js](https://nodejs.org/) 20 or later and a recent version of [pnpm](https://pnpm.io/installation)
* [cosign](https://docs.sigstore.dev/cosign/system_signing/installation/) to verify the signature of the release artifact
* A Region where [AWS Lambda MicroVMs](https://docs.aws.amazon.com/lambda/latest/dg/lambda-microvms.html) are available

## Deployment Instructions

1. Create a new directory, navigate to that directory in a terminal and clone the GitHub repository:
    ```bash
    git clone https://github.com/aws-samples/serverless-patterns
    ```
1. Change directory to the pattern directory:
    ```bash
    cd serverless-patterns/lambda-microvms-code-execution-sandbox/typescript/sam
    ```
1. Set the Region, a stack name and the name of the S3 bucket for the artifact. The stack name prefixes the image and the IAM resources the stack creates:
    ```bash
    export AWS_REGION="${AWS_REGION:-$(aws configure get region)}"   # a Region where Lambda MicroVMs are available
    export STACK_NAME=sandbox-sdk
    export ARTIFACT_BUCKET=amzn-s3-demo-bucket   # a new unique name, or an existing bucket you reuse
    ```
1. Download the sandbox image artifact of the Rayito release, verify it, and upload it to S3. The zip holds `rayd` and the Dockerfile; Lambda builds the image from it in your account, so verify it before you upload it. The `cosign verify-blob` command is a required step: the signature is what authenticates the file. `SHA256SUMS` from the same release only detects a corrupted download (you can also verify its signature with `SHA256SUMS.sigstore.json`, as in [Verify a release](https://alejandro-cedeno-10.github.io/rayito/verify/)), because whoever could replace the zip could replace that file too; the pinned hash below is the one listed in the `SHA256SUMS` of the `rayd-v0.17.1` release, whose signature was verified.
    ```bash
    RAYITO_VERSION=0.17.1
    BASE=https://github.com/alejandro-cedeno-10/rayito/releases/download/rayd-v${RAYITO_VERSION}
    curl -fsSLO "$BASE/rayito-image.zip"
    curl -fsSLO "$BASE/rayito-image.zip.sigstore.json"

    # Required: must print "Verified OK"
    cosign verify-blob --bundle rayito-image.zip.sigstore.json \
      --certificate-identity "https://github.com/alejandro-cedeno-10/rayito/.github/workflows/release.yml@refs/tags/rayd-v${RAYITO_VERSION}" \
      --certificate-oidc-issuer https://token.actions.githubusercontent.com \
      rayito-image.zip

    # Pinned SHA-256 of rayito-image.zip for 0.17.1 (change it together with RAYITO_VERSION); must print "rayito-image.zip: OK"
    echo "4e57d7db76007ae5517117c19b960d41a17662687c868840a8419292e6bfa89b  rayito-image.zip" | shasum -a 256 -c -   # on Linux: sha256sum -c -
    ```
    Upload the artifact. Choose one of the two options and remember which one you used, because Cleanup differs:
    * Create a new bucket (cleanup deletes it). The check stops you if the name is a bucket you already own, because Cleanup would then delete it; in that case use the next option:
        ```bash
        if ! aws sts get-caller-identity >/dev/null 2>&1; then
          echo "AWS credentials are not valid: stop here and fix them first"
        elif aws s3api head-bucket --bucket "${ARTIFACT_BUCKET}" 2>/dev/null; then
          echo "Bucket already exists: use the reuse option instead"
        else
          aws s3 mb "s3://${ARTIFACT_BUCKET}" --region "${AWS_REGION}" &&
          aws s3 cp rayito-image.zip "s3://${ARTIFACT_BUCKET}/rayito/rayito-image.zip" &&
          export ARTIFACT_KEY=rayito/rayito-image.zip
        fi
        ```
    * Reuse an existing bucket in the same Region (cleanup deletes only the object, never the bucket). Set `ARTIFACT_BUCKET` to that bucket and upload the zip under a key that starts with `rayito/`; the build role can read only `rayito/*` of the bucket:
        ```bash
        export ARTIFACT_KEY=rayito/sandbox-sdk/rayito-image.zip
        aws s3 cp rayito-image.zip "s3://${ARTIFACT_BUCKET}/${ARTIFACT_KEY}"
        ```
    Rayito documents the release verification in [Verify a release](https://alejandro-cedeno-10.github.io/rayito/verify/) and its threat model in [Security](https://alejandro-cedeno-10.github.io/rayito/security/). `rayd` runs as an agent inside every sandbox, so treat this artifact like any other code you deploy.
1. From the command line, use AWS SAM to deploy the AWS resources for the pattern as specified in the template.yaml file. CloudFormation waits until Lambda has built the image. The template has no local artifacts, so SAM does not need a bucket of its own:
    ```bash
    sam deploy --template-file template.yaml --stack-name "${STACK_NAME}" --region "${AWS_REGION}" \
      --capabilities CAPABILITY_IAM \
      --parameter-overrides ArtifactBucket="${ARTIFACT_BUCKET}" ArtifactKey="${ARTIFACT_KEY}"
    ```
    You can also run `sam deploy --guided` and answer the prompts (stack name, Region, `ArtifactBucket`, `ArtifactKey`, and allow SAM CLI to create IAM roles). Guided mode writes a `samconfig.toml`; do not commit it.
1. Note the outputs from the SAM deployment process. `SandboxImageName` is the image the client uses, and `SandboxLauncherPolicyArn` is a policy with the runtime actions for the identity that runs the client:
    ```bash
    aws cloudformation describe-stacks --stack-name "${STACK_NAME}" --region "${AWS_REGION}" \
      --query "Stacks[0].Outputs" --output table
    ```

## How it works

The stack creates AWS resources only:

* An `AWS::Lambda::MicrovmImage` built on the AWS managed Amazon Linux 2023 base image (`al2023-1`) from `rayito-image.zip`. The zip contains `rayd`, a small agent that serves the MicroVM lifecycle hooks on port 9000 (`/ready`, `/validate`, `/run`, `/suspend`, `/resume`, `/terminate`) and an API for processes, files and a Python (Jupyter) kernel. Lambda runs the Dockerfile in the zip, waits for the ready hook, runs the validate hook and takes a snapshot; every sandbox then starts from that snapshot.
* An IAM build role that Lambda assumes to read the artifact and write the build logs, and an Amazon CloudWatch Logs log group with 7-day retention.
* `SandboxLauncherPolicy`, a customer managed policy, a least-privilege starting point scoped to this stack's image, with the runtime actions only: run, get, suspend, resume and terminate MicroVMs of this stack's image, create their auth tokens, and pass the AWS managed network connectors. It cannot create or change an image.

The client uses the `rayito` npm package. `Sandbox.create()` calls `RunMicrovm`, creates a MicroVM auth token with `CreateMicrovmAuthToken`, and talks to `rayd` through the MicroVM endpoint. `runCode()`, `commands.run()` and `files.*` are calls to `rayd`; `pause()` and `resume()` call `SuspendMicrovm` and `ResumeMicrovm`; terminating calls `TerminateMicrovm`. Each sandbox is one MicroVM, with its own kernel, memory and disk.

`SandboxPool` keeps a number of sandboxes suspended and already warm, so `take()` resumes one instead of creating a new MicroVM.

## Network access

The sandbox image in this template has no additional OS capabilities, and a sandbox started from it can reach the internet: according to the Rayito [network documentation](https://alejandro-cedeno-10.github.io/rayito/network/), omitting an egress connector (`EgressNetworkConnectors: []`) does not close the network, because a MicroVM inherits the managed internet egress connector. `PassManagedConnectors` in the launcher policy lets the caller pass the AWS managed network connectors, which `RunMicrovm` requires even when none is named. Do not run code you do not trust in a sandbox without first deciding what it may reach.

Rayito restricts outbound traffic from inside the guest, which needs an image built with additional OS capabilities (`AdditionalOsCapabilities: [ALL]`, a copy of the image resource in the template). With such an image the client can pass a `network` option (`denyOut`, `allowOut`) or `allowInternetAccess: false`; on an image without the capabilities, the SDK refuses to hand you a sandbox instead of leaving the network open. See the Rayito documentation for the exact semantics and limits. Because the guest enforces it, treat it as one layer: for control outside the guest, use a VPC network connector.

## Testing

1. Install the client dependencies:
    ```bash
    cd src
    pnpm install --frozen-lockfile
    ```
1. Point the client at the image the stack built. The client uses the default AWS credential chain and `AWS_REGION`:
    ```bash
    export RAYITO_TEMPLATE="${STACK_NAME}-base"
    ```
1. Run the sandbox client. It creates a sandbox, runs Python code twice to show that variables persist, runs a shell command, writes and runs a script, reads its output, lists the directory, pauses and resumes the sandbox, checks that the variable is still there, and terminates the sandbox:
    ```bash
    pnpm sandbox
    ```
    Expected output (times vary):
    ```text
    sandbox created in 7236 ms
    runCode: 42
    commands.run: 0 Linux aarch64
    files.read: hello from the MicroVM
    files.list: hello.py, out.txt
    after pause/resume: 42
    done in 9933 ms; terminating the sandbox
    ```
1. Run the pool client. It starts a pool of one sandbox, waits for it to be warm and parked, takes it, runs code and closes the pool. The first `take()` includes the time the pool needs to warm its slot:
    ```bash
    pnpm pool
    ```
    Expected output (times vary):
    ```text
    take() returned a usable sandbox after 9177 ms
    runCode: 45
    stats: {"takes":1,"hits":1,"misses":0}
    ```
1. Run the E2B entry point client. The same kind of sandbox through `rayito/e2b`, which implements a subset of the E2B JavaScript SDK API:
    ```bash
    pnpm e2b
    ```
    Expected output:
    ```text
    runCode: 2
    files.read: hello
    ```
1. Check that no sandbox is left running (the list must be empty, or show only MicroVMs that are not yours):
    ```bash
    aws lambda-microvms list-microvms --region "${AWS_REGION}" \
      --query "items[?state!='TERMINATED'].[microvmId,state,imageArn]" --output table
    ```

### Permissions for the client

The stack's `SandboxLauncherPolicyArn` managed policy is a least-privilege starting point scoped to this stack's image. It lists the runtime actions the client calls (run, get, suspend, resume, terminate, create an auth token) and no action that changes an image. The list actions do not support resource-level permissions, so they use `Resource: "*"`. Use it as the starting point for the IAM role or user that runs the client in your application, and adjust it to the features you use.

## Cleanup

If you opened a new terminal, set `AWS_REGION`, `STACK_NAME`, `ARTIFACT_BUCKET` and `ARTIFACT_KEY` again first. `ARTIFACT_KEY` is `rayito/rayito-image.zip` if you created the bucket, or the key you chose if you reused one. If you are not sure which option you used, use the `aws s3 rm` option, which never deletes a bucket. If an earlier attempt of yours created the bucket but the upload failed, delete that empty bucket by hand with `aws s3 rb "s3://${ARTIFACT_BUCKET}"` (without `--force`).

1. Delete the stack. This deletes the image, the roles, the policy and the log group:
    ```bash
    sam delete --stack-name "${STACK_NAME}" --region "${AWS_REGION}" --no-prompts
    ```
1. Delete the artifact, according to the option you chose when you uploaded it:
    * If this run created the bucket (the guard above did not stop you), delete the bucket and everything in it:
        ```bash
        aws s3 rb "s3://${ARTIFACT_BUCKET}" --force
        ```
    * If you reused an existing bucket, delete only the object you uploaded. Never delete the bucket:
        ```bash
        aws s3 rm "s3://${ARTIFACT_BUCKET}/${ARTIFACT_KEY}"
        ```
1. Confirm the stack has been deleted
    ```bash
    aws cloudformation list-stacks --region "${AWS_REGION}" \
      --query "StackSummaries[?contains(StackName,'${STACK_NAME}')].StackStatus"
    ```

## Cost

Sandboxes are billed while they run or are suspended, and each image version is billed for its snapshot storage. A pool keeps its MicroVMs suspended, which is billed too. The test run above creates a few short-lived sandboxes. See [AWS Lambda pricing](https://aws.amazon.com/lambda/pricing/) for the current rates.

## Resources

* [AWS Lambda MicroVMs documentation](https://docs.aws.amazon.com/lambda/latest/dg/lambda-microvms.html)
* [Rayito documentation](https://alejandro-cedeno-10.github.io/rayito/)
* [Rayito source code](https://github.com/alejandro-cedeno-10/rayito)

----
Copyright 2026 Amazon.com, Inc. or its affiliates. All Rights Reserved.

SPDX-License-Identifier: MIT-0
