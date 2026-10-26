# Amazon EventBridge API Destination to Amazon Bedrock AgentCore Runtime

This pattern demonstrates **Lambda-less, event-driven invocation of an AI agent**: an EventBridge rule delivers events directly to an Amazon Bedrock AgentCore Runtime endpoint via an API Destination, authenticated with Amazon Cognito machine-to-machine (M2M) OAuth. No Lambda function, no glue code.

The CDK stack is **fully self-contained** — it builds and deploys the AgentCore Runtime (from the bundled `agent-code/` Docker image) alongside the EventBridge plumbing, so a single `cdk deploy` gives you a working, testable pattern.

![Architecture](architecture.png)

```
EventBridge Rule ──▶ API Destination (HTTPS + OAuth) ──▶ AgentCore Runtime
     │                        │                                 │
custom event bus     Connection: Cognito             async processing
(demo.orders)        client_credentials JWT          (ack < 5s, work in
                                                      background)
```

Learn more about this pattern at Serverless Land Patterns: https://serverlessland.com/patterns/

Important: this application uses various AWS services and there are costs associated with these services after the Free Tier usage - please see the [AWS Pricing page](https://aws.amazon.com/pricing/) for details. You are responsible for any AWS costs incurred. No warranty is implied in this example.

## How it works

1. An event (e.g. `source: demo.orders`, `detail-type: OrderCreated`) is published to a custom event bus.
2. An EventBridge rule matches the event and forwards it to an **API Destination** whose endpoint is the AgentCore Runtime `InvokeAgentRuntime` HTTPS API.
3. The API Destination's **Connection** obtains an OAuth access token from a **Cognito user pool token endpoint** using the `client_credentials` grant, and attaches it as a Bearer token.
4. The AgentCore Runtime validates the JWT against the Cognito user pool (inbound identity / `customJwtAuthorizer`), **acknowledges the request within 5 seconds**, and processes the event **asynchronously**.
5. Failed deliveries (after 3 retries) are sent to an Amazon SQS dead-letter queue.

## Key technical details

### 1. The 5-second timeout → async execution

EventBridge API Destinations enforce a hard **5-second response timeout**. Agent reasoning takes much longer than that, so the agent entrypoint returns an acknowledgment immediately (HTTP 2xx) and continues working in the background.

The background work has to be registered with the runtime. AgentCore Runtime decides whether a session is busy from its `/ping` health status, and a bare `asyncio.create_task` does not change that status, so the runtime could treat the session as idle and stop it before the work finishes. [`agent-code/agent.py`](agent-code/agent.py) uses the [`@app.async_task`](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/runtime-long-run.html) decorator from the AgentCore SDK, which reports `HealthyBusy` while the task runs:

```python
import asyncio
from bedrock_agentcore import BedrockAgentCoreApp
from strands import Agent

app = BedrockAgentCoreApp()
_background_tasks = set()

@app.async_task          # registers the background work with the runtime
async def process_event(payload):
    agent = Agent(model="us.anthropic.claude-haiku-5-5")
    await agent.invoke_async(payload["prompt"])

@app.entrypoint
async def invoke(payload):
    # The runtime tracks this task and stays alive until it finishes,
    # while the response still returns within the 5-second window.
    task = asyncio.create_task(process_event(payload))
    _background_tasks.add(task)  # keep a reference so the task is not garbage collected
    task.add_done_callback(_background_tasks.discard)
    return {"status": "accepted"}
```

### 2. The URL-encoding gotcha → use the agent ID, not the ARN

API Destinations **automatically decode `%XX` sequences** in the endpoint URL. A URL-encoded runtime ARN in the path (containing `:` and `/`) gets decoded back and breaks the request signature/routing.

The fix: use the **agent runtime ID in the path** and pass the **account ID as a query parameter**. Per the AWS docs: *"When you use the agent ID instead of the full ARN, you don't need to URL-encode the identifier."* The stack derives this URL automatically from the runtime it creates (`CfnRuntime.attrAgentRuntimeId`):

```
https://bedrock-agentcore.<region>.amazonaws.com/runtimes/<agentRuntimeId>/invocations?accountId=<accountId>&qualifier=DEFAULT
```

### 3. Authentication → Cognito M2M (client_credentials)

The stack creates:
- A **Cognito user pool** with a hosted domain (provides the `/oauth2/token` endpoint)
- A **resource server** (`agentcore`) with a custom scope (`agentcore/invoke`)
- An **app client** with a secret and the `client_credentials` grant

The EventBridge Connection is configured with OAuth (client credentials) against the Cognito token endpoint. The AgentCore Runtime's `customJwtAuthorizer` is wired to the **same** user pool at creation time (its `discoveryUrl` and `allowedClients` reference the pool and app client this stack creates), so there is no manual post-deploy step.

### 4. Delivery semantics: what the DLQ does and does not catch

Because the runtime acknowledges before the agent runs, EventBridge considers the event delivered as soon as the 2xx response comes back. This has three consequences:

- **Background failures are logged only.** The dead-letter queue captures **delivery** failures: 401/403, 5xx, and timeouts. If the agent fails after the acknowledgment, the exception is written to the runtime's CloudWatch Logs and nothing else happens. EventBridge does not retry it and it never reaches the DLQ.
- **Delivery is at-least-once.** EventBridge can deliver the same event more than once, and this pattern does no deduplication. The rule forwards the EventBridge event ID as `eventId` so you have a key to deduplicate on.
- **No alarms are defined.** A message in the DLQ is not surfaced anywhere unless you look for it.

These are deliberate omissions to keep the pattern minimal. For production:

- Report each background outcome durably: emit a follow-up EventBridge event, write the result or failure to Amazon DynamoDB, or use a callback such as a Step Functions task token with `send_task_success` / `send_task_failure`. The AWS blog post [Asynchronous patterns for calling Amazon Bedrock AgentCore agents in serverless pipelines](https://aws.amazon.com/blogs/machine-learning/asynchronous-patterns-for-calling-amazon-bedrock-agentcore-agents-in-serverless-pipelines/) covers the callback options.
- Check `eventId` against an idempotency store before performing side effects.
- Add a CloudWatch alarm on the DLQ's `ApproximateNumberOfMessagesVisible` metric.

## Prerequisites

- [AWS account](https://portal.aws.amazon.com/gp/aws/developer/registration/index.html) with sufficient permissions
- [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/install-cli.html) installed and configured
- [Node.js 22+](https://nodejs.org/en/download/) and npm
- [AWS CDK CLI](https://docs.aws.amazon.com/cdk/v2/guide/getting_started.html) (`npm i -g aws-cdk`), bootstrapped in the target account and Region (`cdk bootstrap aws://ACCOUNT-ID/REGION`)
- [Docker](https://docs.docker.com/get-docker/) installed and running (the CDK build packages the agent into a container image)
- The bundled agent uses **Claude Haiku 5.5** through the US cross-Region inference profile `us.anthropic.claude-haiku-5-5` (set in [`agent-code/agent.py`](agent-code/agent.py)). Amazon Bedrock enables serverless models automatically, so there is no model access step, but the model must be available in the Region you deploy to. Check the [Claude Haiku 5.5 model card](https://docs.aws.amazon.com/bedrock/latest/userguide/model-card-anthropic-claude-haiku-5-5.html). Outside the US, change `MODEL_ID` to the matching geographic profile (`eu.`, `jp.`, `au.`) or to `global.anthropic.claude-haiku-5-5`.

## Deployment

1. Clone and enter the pattern directory:

   ```bash
   git clone https://github.com/aws-samples/serverless-patterns
   cd serverless-patterns/eventbridge-apidestination-agentcore/typescript/cdk
   npm install
   ```

2. Deploy. The stack builds the agent container image, deploys the AgentCore Runtime, and wires up EventBridge — all in one command:

   ```bash
   cdk deploy
   ```

3. Note the stack outputs — in particular `EventBusName`, `AgentRuntimeId`, and `DeadLetterQueueUrl`. No further configuration is required: the runtime's JWT authorizer already trusts the Cognito app client created by this stack.

## Testing

Publish a test event to the custom bus (`EventBusName` output):

```bash
aws events put-events --entries '[
  {
    "EventBusName": "agentcore-events",
    "Source": "demo.orders",
    "DetailType": "OrderCreated",
    "Detail": "{\"orderId\": \"12345\", \"prompt\": \"Summarize this order and flag any anomalies.\"}"
  }
]'
```

Verify the invocation:

1. **AgentCore Runtime logs** — check Amazon CloudWatch Logs for the runtime (`/aws/bedrock-agentcore/runtimes/<AgentRuntimeId>-DEFAULT`) to see the event arrive and background processing run.
2. **Connection health** — `aws events describe-connection --name agentcore-cognito-oauth` should show `AUTHORIZED`.
3. **Failures** — if delivery fails after retries, events land in the DLQ:

   ```bash
   aws sqs receive-message --queue-url <DeadLetterQueueUrl output>
   ```

Common failure causes:
- HTTP 401/403 in the DLQ → the Connection couldn't obtain or present a valid token (check the Connection status and the Cognito app client secret).
- Timeouts → the agent isn't acknowledging within 5 seconds (keep the entrypoint async; see `agent-code/agent.py`).
- Nothing in the DLQ, but no agent result in the runtime logs → the agent failed after acknowledging. Search the runtime log group for `agent invocation failed`. See [Delivery semantics](#4-delivery-semantics-what-the-dlq-does-and-does-not-catch).

## Cleanup

```bash
cdk destroy
```

---

Copyright 2026 Amazon.com, Inc. or its affiliates. All Rights Reserved.

SPDX-License-Identifier: MIT-0
