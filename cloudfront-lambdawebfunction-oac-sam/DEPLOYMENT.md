# Deployment Guide — cloudfront-lambdawebfunction-oac-sam

Exact commands to package, deploy, test, and tear down this pattern. For the architecture overview and how it works, see [README.md](README.md).

> **Shortcut:** `./deploy.sh` from the solution directory automates everything in steps 1–3 below (region resolution, bucket creation, zip + upload + version capture, `sam build`, and `sam deploy`). The steps here are the manual equivalent, useful when you want to run each stage yourself or understand what the script does.

## Prerequisites

- An AWS account with permissions to manage Lambda Web Functions, CloudFront, IAM, and S3.
- [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html) installed and configured.
- [AWS SAM CLI](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-sam-cli-install.html) installed.
- `zip` on your PATH (used to package `src/` into the deployment archive).
- Permissions for the deploying identity to create the IAM execution role (`iam:PassRole`).
- A deployment Region where Lambda Web Functions is available (see the AWS Lambda Web Functions documentation for the current Region list).
- (Manual path only) An Amazon S3 bucket with **versioning enabled (required by Lambda)** for the Web Function `.zip` deployment package. The Quick start `deploy.sh` creates a versioning-enabled bucket for you.

Set some shell variables used throughout this guide:

    export AWS_REGION=us-east-1
    export STACK_NAME=cloudfront-lambdawebfunction-oac
    export CODE_BUCKET=amzn-s3-demo-bucket          # your existing S3 bucket
    export CODE_KEY=web-function/app.zip

## 1. Package the Web Function code and upload to Amazon S3

Lambda Web Functions are deployed **only** from an S3 object — there is no inline code path. Zip the contents of `src/` with the entry file (`index.js`) at the root of the archive, then upload:

    cd src
    zip -r ../app.zip .
    cd ..
    aws s3 cp app.zip "s3://${CODE_BUCKET}/${CODE_KEY}" --region "${AWS_REGION}"

The code bucket must have versioning enabled (Lambda requires it). Capture the uploaded object's version ID so you can pin the revision to it:

    export CODE_VERSION_ID=$(aws s3api head-object \
      --bucket "${CODE_BUCKET}" \
      --key "${CODE_KEY}" \
      --region "${AWS_REGION}" \
      --query VersionId --output text)
    echo "Uploaded version: ${CODE_VERSION_ID}"

## 2. Build

    sam build

## 3. Deploy

> **Before you deploy:** Web Functions deploy code only from an S3 object. `sam deploy` does **not** package or upload your code — you must complete Step 1 (zip + upload to `s3://${CODE_BUCKET}/${CODE_KEY}`) first, or the stack fails with *"The specified S3 object does not exist"*. (The Quick start `./deploy.sh` does the upload for you.)

### Guided (first deploy)

    sam deploy --guided

Answer the prompts:

| Prompt | Value |
|---|---|
| Stack Name | `${STACK_NAME}` |
| AWS Region | `${AWS_REGION}` (a Web Functions Region, see Prerequisites) |
| Parameter CodeBucket | `${CODE_BUCKET}` |
| Parameter CodeKey | `${CODE_KEY}` |
| Parameter CodeVersionId | `${CODE_VERSION_ID}` (optional; leave blank to use the latest object version) |
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
        CodeVersionId="${CODE_VERSION_ID}"

> This template creates an IAM execution role **without** an explicit role name, so `CAPABILITY_IAM` is sufficient — `CAPABILITY_NAMED_IAM` is not required.

## 4. Get the stack outputs

    aws cloudformation describe-stacks \
      --stack-name "${STACK_NAME}" \
      --region "${AWS_REGION}" \
      --query "Stacks[0].Outputs" --output table

Key outputs:

- **CloudFrontDomainName** — the URL to reach your app.
- **WebFunctionEndpointDomain** — the endpoint's own domain (direct access is denied by `IamAuth`).

## 5. Test

Direct access to the endpoint domain is denied (unsigned request against an `IamAuth` endpoint):

    curl -i "https://<WebFunctionEndpointDomain>/"      # expect 403 Forbidden

Access through CloudFront succeeds (CloudFront signs the origin request via OAC):

    curl -i "https://<CloudFrontDomainName>/"           # expect 200, "Hello from AWS !!! ..."

See the README's **Observing multi-concurrency** section for a parallel-request burst that shows a single execution environment handling many concurrent requests.

## 6. Deploy new code (new revisions)

Revisions are immutable. To ship new code, upload a new `.zip` and redeploy — a new revision is created because the revision's code location/configuration are create-only:

    cd src && zip -r ../app.zip . && cd ..
    aws s3 cp app.zip "s3://${CODE_BUCKET}/${CODE_KEY}" --region "${AWS_REGION}"
    # re-capture CODE_VERSION_ID (step 1) if versioning, then redeploy (step 3)

## 7. Clean up

    sam delete --stack-name "${STACK_NAME}" --region "${AWS_REGION}"

Confirm deletion:

    aws cloudformation list-stacks \
      --region "${AWS_REGION}" \
      --query "StackSummaries[?contains(StackName,'${STACK_NAME}')].StackStatus"

The deployment package object(s) in S3 are not removed by `sam delete`. Delete them separately if no longer needed:

    aws s3 rm "s3://${CODE_BUCKET}/${CODE_KEY}" --region "${AWS_REGION}"
