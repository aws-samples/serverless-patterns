# AWS Step Functions with Amazon Bedrock AgentCore Harness Optimized Integration (CDK)

This pattern invokes an Amazon Bedrock AgentCore harness directly from AWS Step Functions using the optimized integration — no AWS Lambda function required. The harness handles model inference, tool use, and multi-turn conversations, returning a Converse-shaped response with aggregated token metrics.

Learn more about this pattern at Serverless Land Patterns: https://serverlessland.com/patterns/sfn-bedrockagentcore-harness-cdk

Important: this application uses various AWS services and there are costs associated with these services after the Free Tier usage - please see the [AWS Pricing page](https://aws.amazon.com/pricing/) for details. You are responsible for any AWS costs incurred. No warranty is implied in this example.

## Requirements

* [Create an AWS account](https://portal.aws.amazon.com/gp/aws/developer/registration/index.html) if you do not already have one and log in. The IAM user that you use must have sufficient permissions to make necessary AWS service calls and manage AWS resources.
* [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html) installed and configured
* [Git Installed](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)
* [Node.js 20+](https://nodejs.org/en/download/) installed
* [AWS CDK v2](https://docs.aws.amazon.com/cdk/v2/guide/getting_started.html) installed and bootstrapped
* An existing Amazon Bedrock AgentCore harness (see [Creating a harness](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/harness-create.html))

## Deployment Instructions

1. Create a new directory, navigate to that directory in a terminal and clone the GitHub repository:
    ```
    git clone https://github.com/aws-samples/serverless-patterns
    ```
2. Change directory to the pattern directory:
    ```
    cd serverless-patterns/sfn-bedrockagentcore-harness-cdk
    ```
3. Install dependencies:
    ```
    npm install
    ```
4. Deploy the stack with your harness ARN:
    ```
    cdk deploy --parameters HarnessArn=arn:aws:bedrock-agentcore:us-east-1:ACCOUNT_ID:harness/YOUR-HARNESS-NAME
    ```

## How it works

This pattern creates an AWS Step Functions state machine that:

1. **Invokes the harness** using the optimized integration (`arn:aws:states:::bedrockagentcore:invokeHarness`) — no AWS Lambda in the path
2. **Receives a Converse-shaped response** with the agent's final text, stop reason, token usage, and latency metrics
3. **Formats the output** extracting just the response text, token count, and latency
4. **Handles errors** with specific catches for throttling (exponential backoff) and missing harness

### Key differences from SDK integration

| Feature | SDK Integration | Optimized Integration (this pattern) |
|---|---|---|
| Resource URI | `arn:aws:states:::aws-sdk:bedrockagentcore:InvokeHarness` | `arn:aws:states:::bedrockagentcore:invokeHarness` |
| AWS Lambda required | Yes (for streaming/parsing) | No |
| Response format | Raw API response | Converse-shaped (text only, tool use omitted) |
| Token metrics | Manual calculation | Aggregated across all turns automatically |
| CloudWatch traces | Not available | Turn-by-turn reasoning deep-links |
| Max timeout | AWS Lambda timeout (15 min) | 15 minutes (Task state limit) |

### Architecture

```
User Input → AWS Step Functions → Amazon Bedrock AgentCore Harness
                                        ↓
                              Model inference + tool use
                                        ↓
                              Converse-shaped response
                                        ↓
                           Step Functions → Formatted Output
```

## Testing

1. Start an execution:
    ```bash
    SM_ARN=$(aws cloudformation describe-stacks \
      --stack-name SfnBedrockagentcoreHarnessStack \
      --query 'Stacks[0].Outputs[?OutputKey==`StateMachineArn`].OutputValue' \
      --output text)

    EXEC_ARN=$(aws stepfunctions start-execution \
      --state-machine-arn $SM_ARN \
      --input '{"prompt": "What is Amazon Bedrock AgentCore and how does a harness work?"}' \
      --query 'executionArn' --output text)

    echo "Execution: $EXEC_ARN"
    ```

2. Wait 10-30 seconds for the agent to reason, then check output:
    ```bash
    aws stepfunctions describe-execution \
      --execution-arn $EXEC_ARN \
      --query '{status: status, output: output}'
    ```

3. Expected output format:
    ```json
    {
      "response": "Amazon Bedrock AgentCore is...",
      "stopReason": "end_turn",
      "tokensUsed": 1523,
      "latencyMs": 8421
    }
    ```

## Cleanup

```bash
cdk destroy
```

----
Copyright 2026 Amazon.com, Inc. or its affiliates. All Rights Reserved.

SPDX-License-Identifier: MIT-0
