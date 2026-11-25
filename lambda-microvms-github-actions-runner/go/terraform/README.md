# Ephemeral GitHub Actions runners on AWS Lambda MicroVMs

This pattern runs every GitHub Actions job on its own single-use AWS Lambda MicroVM. A GitHub `workflow_job` webhook reaches an Amazon API Gateway REST API, and an AWS Lambda function verifies it, mints a just-in-time (JIT) runner configuration, and launches a MicroVM from a pre-built snapshot. A small Go supervisor inside the MicroVM runs exactly one job and then terminates its own MicroVM. Nothing runs between jobs, and container images are built with buildah instead of a Docker daemon.

Learn more about this pattern at Serverless Land Patterns: https://serverlessland.com/patterns/lambda-microvms-github-actions-runner-terraform

Important: this application uses various AWS services and there are costs associated with these services after the Free Tier usage - please see the [AWS Pricing page](https://aws.amazon.com/pricing/) for details. You are responsible for any AWS costs incurred. No warranty is implied in this example.

## Requirements

* [Create an AWS account](https://portal.aws.amazon.com/gp/aws/developer/registration/index.html) if you do not already have one and log in. The IAM user that you use must have sufficient permissions to make necessary AWS service calls and manage AWS resources.
* [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html) v2 installed and configured, with `lambda-microvms` support (AWS CLI v2 2.35.10 or later)
* [Git Installed](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)
* [Terraform](https://developer.hashicorp.com/terraform/install) installed
* [Go](https://go.dev/doc/install) and `zip`, used by `build.sh` to compile the supervisor
* `pip3` with internet access. Terraform vendors a current boto3 into the webhook package, because the Lambda runtime's bundled boto3 has no `lambda-microvms` client.
* An AWS Region where Lambda MicroVMs is available
* A **private** GitHub repository
* A GitHub [fine-grained personal access token](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/managing-your-personal-access-tokens) (PAT):
  * Repository access → **Only select repositories** → the target repository
  * Repository permissions → **Administration: Read and write**
  * For organization-level runners (`runner_scope = "org"`), grant Organization permissions → **Self-hosted runners: Read and write** instead.

## Deployment Instructions

1. Create a new directory, navigate to that directory in a terminal and clone the GitHub repository:
    ```
    git clone https://github.com/aws-samples/serverless-patterns
    ```
1. Change directory to the pattern directory:
    ```
    cd serverless-patterns/lambda-microvms-github-actions-runner/go/terraform
    ```
1. Copy the example variables file and set your target repository (`terraform.tfvars` is gitignored):
    ```
    cp terraform.tfvars.example terraform.tfvars
    ```
    Then replace `<owner>` and `<repo>`. For organization-level runners, set `runner_scope = "org"` and `github_org = "<org>"` instead (both are in the file, commented out). See [Variables](#variables) for the other settings.
1. Build the MicroVM code artifact. This cross-compiles the supervisor for linux/arm64 and zips it with the Dockerfile into `src/microvm-runner/dist/supervisor.zip`. It does not call AWS:
    ```
    ./src/microvm-runner/build.sh
    ```
1. Deploy. The apply waits a few minutes for the MicroVM image build:
    ```
    terraform init
    terraform apply
    ```
1. Store the GitHub PAT and a webhook secret (any random string, for example from `openssl rand -hex 32`). Each value is read from a prompt and piped in, so it doesn't appear in shell history or the process list:
    ```bash
    read -rsp 'GitHub PAT: ' PAT; echo
    printf %s "$PAT" | aws secretsmanager put-secret-value --secret-string file:///dev/stdin \
      --secret-id "$(terraform output -raw pat_secret_arn)" \
      --region "$(terraform output -raw region)"

    read -rsp 'Webhook secret: ' WEBHOOK_SECRET; echo
    printf %s "$WEBHOOK_SECRET" | aws secretsmanager put-secret-value --secret-string file:///dev/stdin \
      --secret-id "$(terraform output -raw webhook_secret_arn)" \
      --region "$(terraform output -raw region)"

    unset PAT WEBHOOK_SECRET
    ```
1. In the **private** GitHub repository, go to Settings → Webhooks → Add webhook:
    * Payload URL: the output of `terraform output -raw webhook_url` (it ends in `/v1/webhook`)
    * Content type: `application/json`
    * Secret: the webhook secret from the previous step
    * Which events: "Let me select individual events" → **Workflow jobs** only
1. Copy a workflow from this pattern's `example-workflows/` folder into the repository's `.github/workflows/` folder and commit it to the default branch. GitHub only offers `workflow_dispatch` for workflows on the default branch. The workflows target `runs-on: [self-hosted, lambda]`, the default `runner_labels`; change both together.

## How it works

```
 GitHub (workflow_job "queued")
   │  POST, X-Hub-Signature-256
   ▼
 Amazon API Gateway  REST API, stage v1, POST /webhook
   │  Lambda proxy integration
   ▼
 AWS Lambda  webhook function (src/webhook/handler.py)
   │  1. verify the HMAC signature with the webhook secret (AWS Secrets Manager)
   │  2. act only on queued jobs whose labels include all runner_labels
   │  3. call GitHub generate-jitconfig with the PAT (AWS Secrets Manager)
   │  4. write the JIT config to Amazon S3 (jit/ prefix), presign a 60 s GET URL
   │  5. RunMicrovm: runner image, execution role, NO_INGRESS + INTERNET_EGRESS,
   │     maximumDurationInSeconds, run-hook payload = presigned URL
   ▼
 Lambda MicroVM  restored from the image snapshot, single use
   │  6. Lambda calls the supervisor's /run hook with the MicroVM ID + payload
   │  7. the supervisor fetches the JIT config over HTTPS from the presigned URL
   │  8. ./run.sh --jitconfig: the runner connects to GitHub and runs ONE job
   │     (output streams to Amazon CloudWatch Logs)
   │  9. TerminateMicrovm on its own MicroVM
   ▼
 nothing left running
```

The runner image is built once by `terraform apply`, and again whenever its zip changes:

1. `build.sh` cross-compiles the Go supervisor (`src/microvm-runner/supervisor/`) and zips it with `src/microvm-runner/Dockerfile`.
1. Terraform uploads the zip to the S3 bucket under a content-addressed key (`supervisor-runner-<md5>.zip`).
1. Terraform creates a one-resource AWS CloudFormation stack holding an `AWS::Lambda::MicrovmImage`, because the Terraform AWS provider's image resource can't configure lifecycle hooks. The image uses the AL2023 managed base image, `ARM_64`, the standard OS capabilities (`AdditionalOsCapabilities: []`), the `INTERNET_EGRESS` connector, and the `/ready` and `/run` hooks on port 8080. Lambda runs the Dockerfile on the base image, starts the supervisor, waits for `/ready`, and snapshots the MicroVM. The Dockerfile bakes in the GitHub Actions runner (checked against a pinned SHA-256) and buildah, preconfigured with the `vfs` storage driver and chroot isolation.
1. A changed zip builds a new image version under the same ARN. `RunMicrovm` always launches the latest active version, so the webhook needs no change. If a build fails, CloudFormation rolls back and the previous version stays active.

The stack has three IAM roles. The **webhook role** can read the two secrets, write and presign objects under `jit/`, call `RunMicrovm` on the runner image, pass the execution role and the two network connectors, and write its own logs. The **execution role** (attached to each MicroVM) can call `TerminateMicrovm` on the runner image and write runtime logs. The **build role** can read the `supervisor-runner-*` zip and write the image build logs.

### Security

* **Private repositories only.** On a public repository anyone who opens a pull request could run code on your runners.
* **The PAT never enters the MicroVM.** The VM receives only the single-use JIT config, through a presigned URL that expires after 60 seconds. The execution role has no S3 or Secrets Manager access.
* **Use a GitHub App in production.** A GitHub App lets the webhook mint short-lived installation tokens instead of holding a long-lived PAT.
* **The API Gateway endpoint is public; the HMAC signature is the authentication.** The webhook function rejects every request without a valid `X-Hub-Signature-256`. In production, attach AWS WAF to the API stage for an IP allowlist of GitHub's webhook ranges and rate limiting.
* **CI job code can use the execution role.** Jobs run as root in the MicroVM, so they can call `TerminateMicrovm` on MicroVMs launched from the runner image and write to the runtime log group, and nothing else.
* The webhook never logs secrets, headers, request bodies, or the presigned URL. Secrets are cached for 5 minutes so a rotated value takes effect without a redeploy.

### Limitations

* **ARM64 (AWS Graviton) only.** The supervisor, the runner package and the image are built for `ARM_64`.
* **No Docker daemon.** `dockerd` can't run in the MicroVM with the standard OS capabilities. Use buildah, which the image presets for `vfs` storage and chroot isolation (see `example-workflows/buildah-build.yml`). Running real Docker would require `AdditionalOsCapabilities = ["ALL"]`, which this pattern does not use.
* **Job duration.** A job still running after `microvm_max_duration_seconds` is killed with its MicroVM.
* **Failed webhook deliveries are not retried.** If a delivery fails (for example, before the secrets are stored), redeliver it manually from the repository's webhook settings in GitHub.

### Optional extensions

* Push built images: add a registry login step and `buildah push`, for example to Amazon Elastic Container Registry, with push permissions on the execution role.
* Encrypt the secrets and the S3 bucket with a customer managed AWS KMS key.

### Updating the runner image

After editing `src/microvm-runner/Dockerfile` (for example, to add tools or bump the runner version together with its SHA-256) or the supervisor, rebuild and apply:

```
./src/microvm-runner/build.sh
terraform apply
```

The changed zip gets a new S3 key, so CloudFormation builds a new version of the same image (the ARN does not change) and jobs queued after the build use it. To roll back, check out the previous files and run the same two commands.

### Variables

| Variable | Default | Purpose |
|----------|---------|---------|
| `region` | `"us-east-1"` | Deployment Region |
| `name_prefix` | `"gha-microvm-runner"` | Prefix for every resource name |
| `runner_scope` | `"repo"` | `repo` or `org` |
| `github_owner`, `github_repo` | `""` | Target repository (required for `repo` scope) |
| `github_org` | `""` | Target organization (required for `org` scope) |
| `runner_labels` | `["self-hosted", "lambda"]` | Labels the runner registers with; jobs must request all of them |
| `microvm_max_duration_seconds` | `900` | Maximum MicroVM lifetime in seconds (1–28800) |

## Testing

1. Run the smoke workflow from the Actions tab, or with the GitHub CLI:
    ```
    gh workflow run micro-vm-smoke.yml --repo <owner>/<repo>
    ```
1. Follow the MicroVM output:
    ```
    aws logs tail "$(terraform output -raw microvm_runtime_log_group)" --follow --region "$(terraform output -raw region)"
    ```
1. Expected result: the three matrix jobs succeed, each on its own runner named `lambda-jit-<job id>`, and each MicroVM terminates itself when its job ends. Afterwards this returns an empty list:
    ```
    aws lambda-microvms list-microvms --region "$(terraform output -raw region)" \
      --image-identifier "$(terraform output -raw microvm_image_arn)" \
      --query "items[?state=='RUNNING']"
    ```
1. Run `buildah-build.yml` the same way. The `buildah images` step lists `localhost/hello`.

To test the webhook endpoint from the CLI with the sample events in `events/`, sign each payload with your webhook secret the way GitHub does (HMAC-SHA256 over the exact request body). The sample `workflow_job` event requests the `ubuntu-latest` label, so it passes the signature check but launches nothing:

```bash
cd <pattern directory>      # the folder with main.tf and events/
URL="$(terraform output -raw webhook_url)"
read -rsp 'Webhook secret: ' WEBHOOK_SECRET; echo

# Sends a signed payload and prints the HTTP status code.
send() {  # usage: send <github-event> <file>
  SIG="sha256=$(openssl dgst -sha256 -hmac "$WEBHOOK_SECRET" "$2" | awk '{print $NF}')"
  curl -s -o /dev/null -w '%{http_code}\n' -X POST "$URL" \
    -H "Content-Type: application/json" -H "X-GitHub-Event: $1" \
    -H "X-Hub-Signature-256: $SIG" --data-binary @"$2"
}

send ping events/ping.json                         # expect 200 (pong)
send workflow_job events/workflow_job_queued.json  # expect 204 (labels do not match, nothing launched)

# Without a valid signature the webhook rejects the request:
curl -s -o /dev/null -w '%{http_code}\n' -X POST "$URL" \
  -H "Content-Type: application/json" -H "X-GitHub-Event: workflow_job" \
  --data-binary @events/workflow_job_queued.json   # expect 401
unset WEBHOOK_SECRET
```

If you added AWS WAF with an IP allowlist in front of the API, these requests from your machine return `403`. Run them from an allowed address, or test through GitHub (Settings → Webhooks → Recent Deliveries → Redeliver).

To launch a MicroVM from the CLI instead, change the labels in a copy of the event to your `runner_labels` (for example `["self-hosted", "lambda"]`). The webhook then answers `202`, but GitHub has no matching queued job, so the runner idles until `microvm_max_duration_seconds`. Use a real workflow run for end-to-end tests.

To run the webhook unit tests offline (no AWS or network calls):
```
cd src/webhook
python3 -m venv .venv && .venv/bin/pip install -r requirements.txt pytest
.venv/bin/python -m pytest -v
```

## Cleanup

1. Remove the webhook in the GitHub repository's Settings → Webhooks.
1. Delete the stack. This deletes the MicroVM image stack, the S3 bucket and its objects, and the secrets (immediately, with no recovery window):
    ```
    terraform destroy
    ```
1. Delete the image build log group, which Lambda created outside Terraform:
    ```
    aws logs delete-log-group --log-group-name /aws/lambda-microvms/<name_prefix>-runner-image --region <region>
    ```
1. Optionally, delete the example workflows from the repository's `.github/workflows/`.

----
Copyright 2026 Amazon.com, Inc. or its affiliates. All Rights Reserved.

SPDX-License-Identifier: MIT-0
