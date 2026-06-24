# CI/CD dynamic threat analysis in AWS Lambda MicroVMs

This pattern runs an **untrusted artifact** inside an isolated AWS Lambda MicroVM and decides whether to pass or fail a CI/CD pipeline based on **how the artifact actually behaves** — not on what it claims about itself. A sandbox supervisor launches the artifact and a set of collectors observe it from the outside; a small rule engine turns those observations into a deterministic verdict.

Learn more about this pattern at Serverless Land Patterns: << Add the live URL here >>

Important: this application uses various AWS services and there are costs associated with these services after the Free Tier usage - please see the [AWS Pricing page](https://aws.amazon.com/pricing/) for details. You are responsible for any AWS costs incurred. No warranty is implied in this example.

## The idea

"Did it build and pass unit tests" tells you nothing about what an artifact *does* when it runs — what processes it spawns, what files it writes and executes, what it reads from the environment, where it tries to send data. Commercial **Dynamic Threat Analysis (DTA)** answers that by detonating an artifact in an isolated sandbox and watching its runtime behavior. This pattern demonstrates the same shape as a CI/CD gate, using Lambda MicroVMs as the isolation substrate, while keeping everything safe enough to run in a public sample.

It is intentionally a **skeleton and a way of thinking**, not a product. It is not Aqua DTA, not a malware classifier, and not an AWS service.

## Design philosophy

Five ideas drive the whole design. They are worth understanding before the deployment steps, because they are the point of the sample.

### 1. The target is untrusted, and it never reports on itself

The single most important decision: there is a hard separation between the **artifact being analyzed** (the *target*) and the **code doing the analysis** (the *supervisor*). The supervisor launches the target as a child process and a set of collectors observe it entirely from the outside. Nothing in the final report comes from the target describing its own behavior — every conclusion is an external observation.

This matters because the moment you let an artifact assert its own innocence, you have lost the plot for a threat-analysis tool. A self-reporting runner can be told what to say; a process observed from `/proc`, `strace`, and a filesystem diff cannot lie about the syscalls it made.

### 2. Observe from outside, with mechanisms that fit the environment

Collectors watch the target from the outside using primitives that work cleanly inside a MicroVM today:

| Collector | What it observes |
|---|---|
| `process` (`/proc`) | Process-tree lifecycle: start, child spawns, exit, timeout, nonzero exit. Records env variable *names* only — never values. |
| `filesystem` (diff) | A before/after snapshot diff of the workspace: created / modified / deleted / executable-created files. |
| `canary` | Fake canary files and `DTA_CANARY_*` variables; detects access. High-confidence when `strace` saw the `open`, low-confidence (atime) otherwise. Canary values are never written to the report. |
| `strace` | Wraps the target with `strace -ff` (ptrace, user space) and normalizes process/file/network/privilege syscalls. |
| `network` (`/proc/net`) | Polls `/proc/net/{tcp,udp,...}` for active connections. |

### 3. Be conservative and explainable — never claim to classify malware

The rule engine is deliberately simple, and the verdict vocabulary is deliberately modest: `clean`, `suspicious`, `policy_violation`, `unknown`, `error`. **There is no `malware` verdict.** This is a CI gate that turns observed behavior into a pass/fail with an auditable reason, not a detector pretending to be one. The default rules (e.g. "executable created in workspace → suspicious", "canary read → policy_violation", "target spawned a shell → suspicious") are short, readable, and easy to reason about.

### 4. Know your support boundary, and be honest about it

The collectors above are in scope precisely because they don't require kernel instrumentation that a MicroVM may not provide. **Tracee, Falco, custom eBPF, and packet capture are explicitly out of scope** for this version — not because they're bad, but because they need feature probes (BTF, capabilities, ring buffers) this sample doesn't perform. The sample would rather under-claim and be accurate than oversell.

### 5. Safe by default, fail closed

The default scenarios are benign and canary-based (no real malware, exploits, or secrets). AWS mode is double-gated (`DTA_ALLOW_AWS_MODE=true` **and** `--confirm-sandbox-account`). Every MicroVM run is bounded by a maximum duration, collector failures fail the analysis closed, and the MicroVM is terminated in a `finally` block even when the job fails.

## How it works

A MicroVM image carries the sandbox supervisor. For each analysis the orchestrator:

1. runs a fresh MicroVM from the image (`run-microvm`), bounded by a maximum duration;
2. mints a short-lived endpoint auth token scoped to port 8080 (`create-microvm-auth-token`);
3. calls `POST /analysis/start` on the MicroVM, passing the target config in the request body;
4. the supervisor prepares an isolated workspace, materializes the target, **starts the collectors**, launches the target (argv array, never a shell), then stops the collectors and normalizes everything into `events.jsonl`;
5. the rule engine evaluates the events and produces `report.json` (schema `0.2.0`);
6. the orchestrator downloads the report, applies CI policy, and **terminates the MicroVM**.

## Requirements

* [Create an AWS account](https://portal.aws.amazon.com/gp/aws/developer/registration/index.html) if you do not already have one and log in. The IAM user that you use must have sufficient permissions to make necessary AWS service calls and manage AWS resources. **Use a dedicated sandbox account.**
* [AWS CLI v2 >= 2.35.10](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html) installed and configured. Lambda MicroVMs is GA, but the `aws lambda-microvms` commands are only bundled in AWS CLI v2 >= 2.35.10 (older clients return `Invalid choice: 'lambda-microvms'`).
* A region where AWS Lambda MicroVMs is available.
* [Terraform](https://developer.hashicorp.com/terraform/downloads) installed.
* [Git Installed](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)
* [Python 3.11+](https://www.python.org/downloads/) for the orchestrator CLI.

## Deployment Instructions

1. Create a new directory, navigate to that directory in a terminal and clone the GitHub repository:
    ```
    git clone https://github.com/aws-samples/serverless-patterns
    ```
1. Change directory to the pattern directory:
    ```
    cd lambda-microvm-dta
    ```
1. Deploy the bootstrap resources (the artifact bucket and the least-privilege build/execution IAM roles). This requires no input variables:
    ```
    terraform init && terraform apply
    ```
1. Note the outputs (`artifact_bucket_name`, `build_role_arn`, `execution_role_arn`); they are used by the orchestrator below.
1. Install the orchestrator CLI (from `src/`) and build the MicroVM image. AWS mode is intentionally double-gated:
    ```bash
    cd src && pip install -e ./orchestrator && cd ..
    export DTA_ALLOW_AWS_MODE=true

    microvm-dta package --source-dir src/microvm --output out/microvm-dta.zip
    aws s3 cp out/microvm-dta.zip s3://<artifact_bucket_name>/artifacts/microvm-dta.zip

    microvm-dta --region <REGION> build-image --confirm-sandbox-account \
      --image-name lambda-microvm-dta \
      --artifact-uri s3://<artifact_bucket_name>/artifacts/microvm-dta.zip \
      --base-image-arn arn:aws:lambda:<REGION>:aws:microvm-image:al2023-1 \
      --build-role-arn <build_role_arn>
    microvm-dta --region <REGION> wait-image --confirm-sandbox-account \
      --image-identifier arn:aws:lambda:<REGION>:<ACCOUNT_ID>:microvm-image:lambda-microvm-dta
    ```

> The `main.tf` here deploys only the artifact bucket and the build/execution roles, so `terraform apply` needs no inputs. The optional GitHub Actions OIDC CI role (carrying the verified `lambda:*` MicroVM control-plane policy) and the VPC egress / Flow Logs profile are gated behind `enable_github_oidc_role` and `enable_vpc_egress` and are off by default. The IAM action names were verified against the AWS Service Authorization Reference and applied (then destroyed) against GA Lambda MicroVMs during testing.

## How it works (deployed)

Because the target is launched and observed by the supervisor running *inside* the MicroVM, it cannot assert its own innocence — every conclusion in `report.json` comes from outside observation. The target configuration travels in the `start-analysis` request body, so you can change the target without rebuilding the image.

## Testing

Run a benign target end to end:

```bash
# Start a MicroVM (lifecycle only) and capture its id
MVM=$(microvm-dta --region <REGION> run --confirm-sandbox-account \
  --image-identifier arn:aws:lambda:<REGION>:<ACCOUNT_ID>:microvm-image:lambda-microvm-dta \
  --execution-role-arn <execution_role_arn> | jq -r .microvmId)

# Run the analysis, download the report, and evaluate policy
microvm-dta --region <REGION> start-analysis --confirm-sandbox-account --microvm-identifier "$MVM" \
  --target-config src/examples/targets/benign-command.yaml
microvm-dta --region <REGION> fetch-results --confirm-sandbox-account --microvm-identifier "$MVM" --output-dir out
```

A benign target produces `summary.status: passed` and `summary.verdict: clean`. A target that spawns `/bin/sh` is flagged `suspicious` (rule R004) once the `strace` collector observes the `execve`. You can also run the entire pipeline locally with no AWS account:

```bash
microvm-dta dry-run --target-config src/examples/targets/benign-command.yaml --workspace out/analysis
```

## Cleanup

1. Terminate any running MicroVM (the orchestrator also does this in a `finally` block; `cleanup-stale` is a safety net):
    ```bash
    microvm-dta --region <REGION> terminate --confirm-sandbox-account --microvm-identifier "$MVM"
    microvm-dta --region <REGION> cleanup-stale --confirm-sandbox-account
    ```
1. Delete the MicroVM image:
    ```bash
    aws lambda-microvms delete-microvm-image --region <REGION> \
      --image-identifier arn:aws:lambda:<REGION>:<ACCOUNT_ID>:microvm-image:lambda-microvm-dta
    ```
1. Destroy the Terraform-managed resources:
    ```bash
    terraform destroy
    ```

----
Copyright 2026 Amazon.com, Inc. or its affiliates. All Rights Reserved.

SPDX-License-Identifier: MIT-0
