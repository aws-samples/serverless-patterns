# Step Functions with Bedrock AgentCore Multi-Agent Orchestration

This pattern deploys an AWS Step Functions state machine that orchestrates multiple Bedrock AgentCore agents in parallel, then aggregates their responses into a unified summary using Amazon Bedrock Converse.

Learn more about this pattern at Serverless Land Patterns: https://serverlessland.com/patterns/sfn-agentcore-bedrock-cdk

Important: this application uses various AWS services and there are costs associated with these services after the Free Tier usage - please see the [AWS Pricing page](https://aws.amazon.com/pricing/) for details. You are responsible for any AWS costs incurred. No warranty is implied in this example.

## Requirements

* [Create an AWS account](https://portal.aws.amazon.com/gp/aws/developer/registration/index.html) if you do not already have one and log in. The IAM user that you use must have sufficient permissions to make necessary AWS service calls and manage AWS resources.
* [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html) installed and configured
* [Git Installed](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)
* [Node.js 18+](https://nodejs.org/en/download/) installed
* [AWS CDK v2](https://docs.aws.amazon.com/cdk/v2/guide/getting-started.html) installed
* [Amazon Bedrock model access](https://docs.aws.amazon.com/bedrock/latest/userguide/model-access.html) enabled for your chosen model (default: Claude Sonnet) in your target region
* One or more [Bedrock AgentCore agent runtimes](https://docs.aws.amazon.com/bedrock/latest/userguide/agentcore.html) already deployed and accessible

## Architecture

```
┌──────────┐     ┌──────────────────┐     ┌──────────────────────────────────────┐
│  Trigger  │────▶│  Step Functions   │────▶│  Map State (parallel)                │
│  Lambda   │     │  State Machine    │     │                                      │
└──────────┘     └──────────────────┘     │  ┌─────────────────────────────────┐  │
                                           │  │ Invoke Agent Lambda (bundled)    │  │
                                           │  │   → AgentCore Runtime 1          │  │
                                           │  ├─────────────────────────────────┤  │
                                           │  │ Invoke Agent Lambda (bundled)    │  │
                                           │  │   → AgentCore Runtime 2          │  │
                                           │  ├─────────────────────────────────┤  │
                                           │  │ Invoke Agent Lambda (bundled)    │  │
                                           │  │   → AgentCore Runtime N          │  │
                                           │  └─────────────────────────────────┘  │
                                           └───────────────────┬──────────────────┘
                                                               │
                                                               ▼
                                           ┌──────────────────────────────────────┐
                                           │  Aggregate Lambda                     │
                                           │    → Bedrock Converse (summarize)     │
                                           │    → Returns unified summary          │
                                           └──────────────────────────────────────┘
```

## How it works

1. The **Trigger Lambda** receives a prompt and a list of AgentCore runtime ARNs, then starts the Step Functions state machine execution.
2. The **Map state** fans out to invoke each AgentCore agent in parallel. Each iteration calls the **Invoke Agent Lambda**, which uses the bundled `@aws-sdk/client-bedrock-agentcore` SDK to call `InvokeAgentRuntime` and collect the streaming response.
3. After all agents respond, the **Aggregate Lambda** uses Amazon Bedrock Converse (Claude) to synthesize all agent responses into a single coherent summary.
4. The state machine returns the aggregated summary along with the agent count.

## Important Notes

- **Bundled SDK**: The `@aws-sdk/client-bedrock-agentcore` package is not included in the Lambda runtime. The invoke-agent function uses `NodejsFunction` with esbuild bundling to include it.
- **Streaming Response**: `InvokeAgentRuntime` returns a streaming response, which cannot be consumed directly by Step Functions SDK integrations. A Lambda intermediary collects the stream and returns the full response.
- **Enforced Guardrails**: If your account has account-level enforced guardrails configured, all roles that call Bedrock must have `bedrock:ApplyGuardrail` permission — even if your code does not explicitly apply guardrails. The aggregate Lambda role includes this permission.

## Deployment Instructions

1. Clone the repository:
    ```bash
    git clone https://github.com/aws-samples/serverless-patterns
    cd serverless-patterns/sfn-agentcore-bedrock-cdk
    ```

2. Install dependencies:
    ```bash
    npm install
    ```

3. Deploy the stack with your AgentCore runtime ARNs:
    ```bash
    cdk deploy \
      --parameters AgentRuntimeArns=arn:aws:bedrock-agentcore:us-east-1:123456789012:runtime/agent1,arn:aws:bedrock-agentcore:us-east-1:123456789012:runtime/agent2 \
      --parameters BedrockModelId=us.anthropic.claude-sonnet-4-20250514-v1:0
    ```

4. Note the `TriggerFunctionName` from the stack outputs.

## When to use this pattern

Use **SFN-orchestrated multi-agent** when you need:
- **Deterministic execution paths** — you know which agents to call and in what order
- **Parallel fan-out with guaranteed completion** — all agents must respond before aggregation
- **Auditability** — Step Functions provides full execution history, retries, and error handling
- **Cost predictability** — fixed number of agent invocations per execution

Use **single-agent** when one agent with tools can handle the full task. Use **dynamic LLM-driven orchestration** (e.g., a supervisor agent) when the set of agents to invoke depends on runtime context.

## Testing

The pattern is designed for agents with **distinct specializations**. For example, a migration planning scenario:

1. Invoke the trigger function with a domain-specific prompt and specialized agent ARNs:
    ```bash
    aws lambda invoke \
      --function-name <TriggerFunctionName> \
      --payload '{
        "prompt": "We are migrating a 3-tier Java application from on-premises to AWS. What should we consider?",
        "agentRuntimeArns": [
          "arn:aws:bedrock-agentcore:us-east-1:123456789012:runtime/security-agent",
          "arn:aws:bedrock-agentcore:us-east-1:123456789012:runtime/cost-optimization-agent",
          "arn:aws:bedrock-agentcore:us-east-1:123456789012:runtime/architecture-agent"
        ]
      }' \
      --cli-binary-format raw-in-base64-out \
      output.json
    ```

    Each agent responds from its domain expertise (security risks, cost implications, architecture recommendations), and the aggregation Lambda produces a unified migration plan.

2. The trigger returns the Step Functions execution ARN. Monitor the execution:
    ```bash
    aws stepfunctions describe-execution \
      --execution-arn <executionArn-from-output.json>
    ```

3. Once the execution completes (status: `SUCCEEDED`), view the output which contains the aggregated summary from all agents.

## Cleanup

```bash
cdk destroy
```

----
Copyright 2026 Amazon.com, Inc. or its affiliates. All Rights Reserved.

SPDX-License-Identifier: MIT-0
