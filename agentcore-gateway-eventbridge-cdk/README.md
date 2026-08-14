# Amazon Bedrock AgentCore Runtime to Amazon EventBridge via AgentCore Gateway

This pattern demonstrates how an AI agent on **AgentCore Runtime** emits structured business events to **EventBridge** through a governed **AgentCore Gateway MCP tool**, authenticated with **IAM (SigV4)**. The Gateway provides governance, observability, and schema control over what the agent can emit — without the agent needing direct access to the EventBridge SDK.

The CDK stack is **fully self-contained**: it builds and deploys the agent container, the Gateway with its Lambda tool backend, and an EventBridge custom bus.

![Architecture](architecture.png)

```
Strands Agent (AgentCore Runtime)
    │  MCP Streamable HTTP, SigV4-signed
    ▼
AgentCore Gateway (authorizerType=AWS_IAM)
    │  emit_event tool
    ▼
Lambda tool backend (validates + PutEvents)
    │
    ▼
EventBridge Custom Bus
```

Learn more about this pattern at Serverless Land Patterns: https://serverlessland.com/patterns/

Important: this application uses various AWS services and there are costs associated with these services after the Free Tier usage - please see the [AWS Pricing page](https://aws.amazon.com/pricing/) for details. You are responsible for any AWS costs incurred. No warranty is implied in this example.

## Why route through AgentCore Gateway instead of calling EventBridge directly?

In a mesh of tens or hundreds of agents, Gateway acts as a governed chokepoint between agent reasoning and infrastructure side effects. Three properties make it worth the extra hop:

- **Policy-based access control** — Cedar policies attached to the Gateway evaluate every tool call against its input before it reaches the Lambda target. You can restrict which agents emit which event types, or block specific `detail_type` values during a production freeze, without redeploying any agent.
- **Per-caller rate limiting** — set different throughput budgets per agent identity so a misbehaving agent can't flood the bus while high-priority agents keep running.
- **Single IAM blast radius** — only the Gateway's Lambda backend holds `events:PutEvents`. Agents authenticate with scoped, revocable credentials (JWT or IAM/SigV4), and the Gateway centrally logs every tool invocation for audit.

The tradeoff is roughly 200ms of added latency per emission — negligible for asynchronous event-driven workflows, and often more than offset by removing per-agent IAM churn as the mesh grows.

| Concern | Direct SDK | Via AgentCore Gateway |
|---------|-----------|----------------------|
| Governance | Agent can emit any event schema | Gateway tool definition constrains allowed schemas |
| Observability | Must instrument yourself | Gateway logs every tool invocation automatically |
| Schema evolution | Redeploy agent container to change | Update Gateway tool definition only |
| Multi-agent consistency | Each agent implements PutEvents differently | All agents use the same governed tool |

## How it works

1. The agent (Strands, Claude Haiku 4.5) connects to the AgentCore Gateway via the **MCP Streamable HTTP transport** (2025-03-26 spec).
2. The Gateway's inbound authorization is **`AWS_IAM`** — every request must carry a valid AWS SigV4 signature (service `bedrock-agentcore`). The Runtime's execution role is granted `bedrock-agentcore:InvokeGateway` scoped to the Gateway ARN.
3. **No MCP client SDK signs streamable-HTTP requests with SigV4 natively.** This pattern signs requests manually: [`agent-code/sigv4.py`](agent-code/sigv4.py) wraps `botocore.auth.SigV4Auth` as an `httpx.Auth` implementation and passes it to `streamablehttp_client(url, auth=sigv4_auth)`.
4. The Gateway exposes an `emit_event` tool backed by a Lambda function.
5. When the agent decides to emit an event, it calls `emit_event` with `source`, `detail_type`, and `detail`.
6. The Lambda validates the source prefix (`agent.*` only) and calls `events:PutEvents` on the custom bus.

## Prerequisites

- [AWS account](https://portal.aws.amazon.com/gp/aws/developer/registration/index.html) with sufficient permissions
- [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/install-cli.html) installed and configured
- [Node.js 20+](https://nodejs.org/en/download/) and npm
- [AWS CDK CLI](https://docs.aws.amazon.com/cdk/v2/guide/getting_started.html) (`npm i -g aws-cdk`), bootstrapped in the target account/region
- [Docker](https://docs.docker.com/get-docker/) installed and running
- Access to the Amazon Bedrock Claude Haiku 4.5 model (enable in the Amazon Bedrock console)

## Deployment

```bash
git clone https://github.com/aws-samples/serverless-patterns
cd serverless-patterns/agentcore-gateway-eventbridge-cdk/cdk
npm install
cdk deploy
```

Note the stack outputs — in particular `AgentRuntimeArn`.

## Testing

Invoke the agent with a prompt that triggers the `emit_event` tool:

```bash
RUNTIME_ARN="<AgentRuntimeArn from stack outputs>"

aws bedrock-agentcore invoke-agent-runtime \
  --agent-runtime-arn "$RUNTIME_ARN" \
  --qualifier DEFAULT \
  --runtime-session-id "test-session-$(uuidgen | tr -d '-')" \
  --payload '{"prompt": "Use the emit_event tool to emit an event with source=agent.claims-processor, detail_type=ClaimApproved, detail={claimId: CLM-001, decision: approved, confidence: 0.94}"}' \
  --region us-east-1
```

Verify success in the Runtime's CloudWatch Logs (`/aws/bedrock-agentcore/runtimes/<AgentRuntimeId>-DEFAULT`):

- `POST https://<gateway-url>/mcp "HTTP/1.1 200 OK"` confirms the SigV4-signed request to the Gateway succeeded.
- The agent's response includes the EventBridge `Event ID` and a `Failed Count: 0`.

Common failure causes:
- `403 Forbidden` from the Gateway → the Runtime role is missing `bedrock-agentcore:InvokeGateway` on the Gateway ARN, or the SigV4 signature is malformed (check that the `connection` header was stripped before signing).
- `AttributeError` on tool listing → ensure `strands-agents` and `mcp` package versions are compatible (see `agent-code/requirements.txt`).

## Cleanup

```bash
cdk destroy
```

---

Copyright 2026 Amazon.com, Inc. or its affiliates. All Rights Reserved.

SPDX-License-Identifier: MIT-0
