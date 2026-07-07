# Multi-tenant AI agents on AWS Lambda MicroVMs

This pattern runs a self-hosted AI agent ([OpenClaw](https://github.com/openclaw/openclaw)) **one isolated Lambda MicroVM per tenant**, with per-tenant state persisted on Amazon EFS, model calls served by Amazon Bedrock through a VPC endpoint, and an orchestrator Lambda behind API Gateway that cold-starts, resumes, and reaps tenant VMs on demand.

Most AI agents sit idle most of the time, yet an "always-on" deployment bills 24/7. Lambda MicroVMs flip that model: an idle tenant's VM auto-suspends (barely billed), a fully idle tenant is terminated with its state parked on EFS for ≈$0, and a returning tenant resumes from a Firecracker snapshot in seconds — memory intact. Each tenant gets a dedicated micro-VM, so isolation is a hard security boundary by design, and the workload obtains AWS credentials from the MicroVM's IMDSv2 execution role with no static keys.

Learn more about this pattern at Serverless Land Patterns: << Add the live URL here >>

Important: this application uses various AWS services and there are costs associated with these services after the Free Tier usage - please see the [AWS Pricing page](https://aws.amazon.com/pricing/) for details. You are responsible for any AWS costs incurred. No warranty is implied in this example.

## Requirements

* [Create an AWS account](https://portal.aws.amazon.com/gp/aws/developer/registration/index.html) if you do not already have one and log in. The IAM user that you use must have sufficient permissions to make necessary AWS service calls and manage AWS resources.
* [AWS CLI v2 >= 2.35](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html) installed and configured — must include the `lambda-microvms` and `lambda-core` subcommands (check with `aws lambda-microvms help`)
* [Git Installed](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)
* Python 3 and [uv](https://docs.astral.sh/uv/) (or a recent pip), plus the `zip` and `openssl` utilities
* A [Lambda MicroVMs launch region](https://docs.aws.amazon.com/lambda/latest/dg/lambda-microvms.html) (us-east-1, us-east-2, us-west-2, eu-west-1, ap-northeast-1)
* Amazon Bedrock **model access for Anthropic Claude** enabled in the target region

Docker is **not** required locally — the container image build runs on AWS as part of the `AWS::Lambda::MicrovmImage` resource.

## Deployment Instructions

1. Create a new directory, navigate to that directory in a terminal and clone the GitHub repository:
    ```
    git clone https://github.com/aws-samples/serverless-patterns
    ```
1. Change directory to the pattern directory:
    ```
    cd serverless-patterns/lambda-microvms-multi-tenant-ai-agents
    ```
1. Deploy the whole system with one command (takes ~10 minutes: CloudFormation stack + server-side MicroVM image build + VPC egress connector):
    ```
    ./deploy.sh <stack-name> <region>
    # e.g. ./deploy.sh openclaw-mt us-east-1
    ```
    The script pre-flights the CLI and target region, uploads two zip artifacts to S3 (the MicroVM image source and the bundled orchestrator Lambda — both under content-hashed keys, so a code change always reaches AWS and an unchanged redeploy is a true no-op) and then runs a single `aws cloudformation deploy`. Everything else — VPC with NAT internet egress, EFS, Bedrock VPC endpoints (runtime + control plane), IAM roles, DynamoDB tenant registry, the MicroVM image (built server-side by CloudFormation via `AWS::Lambda::MicrovmImage`), the VPC egress connector, the orchestrator Lambda, API Gateway, and the EventBridge sweeper — is declared in `template.yaml`. A random per-checkout gateway token is minted into `.gateway-token` (override with `$GATEWAY_TOKEN`).
1. Register a tenant in the DynamoDB registry:
    ```
    ./add-tenant.sh <stack-name> <region> tenant1
    ```
1. Note the `ApiEndpoint` output printed at the end of the deploy. Tenant webhook URLs take the form `<ApiEndpoint>/tg/<tenantId>`.

## How it works

![Architecture](images/architecture.png)

1. **Image build**: CloudFormation creates the `AWS::Lambda::MicrovmImage` resource. Lambda downloads the zip artifact from S3, executes the Dockerfile server-side (installs the OpenClaw agent, a sidecar, an EFS mount daemon, and a persistent gateway bridge), and takes a Firecracker snapshot.
2. **Message routing**: a message for a tenant arrives at API Gateway and invokes the orchestrator Lambda (router role). The router ACKs immediately and hands the message to an async worker invocation.
3. **Tenant lookup**: the worker checks the DynamoDB tenant registry. If the tenant's MicroVM is alive (RUNNING or SUSPENDED — suspended VMs auto-resume in seconds), the turn is forwarded. If the tenant is cold, the worker calls `run-microvm` (guarded by a conditional-write lock so concurrent messages launch only one VM), waits for the VM to mount the tenant's EFS subdirectory, and then forwards the turn.
4. **Agent turn**: inside the MicroVM, a sidecar receives the turn and passes it to the OpenClaw gateway over a persistent WebSocket bridge — the gateway holds the agent state warm in memory, so a turn takes ~2 seconds instead of re-reading state over NFS on every message. If a long-running turn outlives the worker invocation, the worker relays polling to a fresh async self-invocation, so a turn is bounded by the VM's 8-hour lifetime rather than Lambda's 15 minutes.
5. **Model call**: the agent calls Amazon Bedrock through VPC interface endpoints (runtime for inference, control plane for live model discovery at cold start). General internet egress for the agent's web search/fetch tools goes through a NAT gateway, while Bedrock and EFS traffic stays on the private VPCE/mount-target paths. Credentials come from the MicroVM's IMDSv2 execution role — no static keys anywhere.
6. **State persistence**: the tenant's full agent state (config + conversation memory) lives under `/tenants/<id>` on EFS. It survives suspend, resume, termination, and the MicroVM's 8-hour maximum lifetime — a relaunched VM adopts the existing state and the agent remembers everything.
7. **Lifecycle sweep**: an EventBridge rule invokes the orchestrator (sweeper role) every 10 minutes to terminate VMs idle beyond the threshold and reconcile the registry against ground truth. Tenants flow hot (RUNNING) → warm (SUSPENDED) → cold (TERMINATED, state on EFS) automatically.

## Testing

Chat with a tenant synchronously (bypasses API Gateway's 30s timeout so you can watch a cold start, which takes ~90 seconds; subsequent warm turns take ~2 seconds):

```bash
./chat.sh <stack-name> <region> tenant1 "Remember my lucky number is 7777."
# → cold: True  | reply: (agent confirms)

./chat.sh <stack-name> <region> tenant1 "What's my lucky number?"
# → cold: False | reply: 7777
```

To verify cross-generation persistence, terminate the tenant's MicroVM (`aws lambda-microvms terminate-microvm ...` or simply wait for the sweeper), then ask again — the relaunched VM adopts the EFS state and still answers `7777` with `cold: True`.

Tenant isolation: register a second tenant and confirm it cannot see the first tenant's memory:

```bash
./add-tenant.sh <stack-name> <region> tenant2
./chat.sh <stack-name> <region> tenant2 "What's my lucky number?"
# → the agent does not know — tenant2 has its own EFS subdirectory and its own VM
```

### Optional: Telegram push front-end

Each tenant can be bound to its own Telegram bot. Create a bot with [@BotFather](https://t.me/BotFather) (`/newbot` → token), then register the tenant with the token and a webhook secret of your choosing:

```bash
./add-tenant.sh <stack-name> <region> tenant3 <BOT_TOKEN> <WEBHOOK_SECRET>
```

The script sets the bot's webhook to `<ApiEndpoint>/tg/tenant3`. Messaging the bot then drives the same router → worker → MicroVM flow, and replies are delivered back through the Telegram Bot API. Use a dedicated bot per tenant — registering overwrites the bot's existing webhook.

Over Telegram the worker additionally provides:

* **Streaming replies** — a placeholder message that grows via `editMessageText` while the model generates, with a `▌` cursor until the final edit.
* **Images** — send a photo with or without a caption; the worker pulls it from Telegram, ships it into the VM as a base64 attachment, and the agent answers about what it sees.
* **`/model` switching** — e.g. `/model amazon-bedrock/us.anthropic.claude-sonnet-5`, `/model default` to reset. The model catalog is discovered live from Bedrock at each cold start, so newly launched models are switchable without a redeploy.

## Cleanup

```bash
./teardown.sh <stack-name> <region>
```

The script terminates this stack's running MicroVMs (matched by image ARN, so VMs from other stacks are untouched), deletes the CloudFormation stack (which removes the MicroVM image, network connector, EFS, VPC, IAM roles, DynamoDB table, Lambda, and API Gateway), and finally empties and deletes the artifact bucket.

----
Copyright 2026 Amazon.com, Inc. or its affiliates. All Rights Reserved.

SPDX-License-Identifier: MIT-0
