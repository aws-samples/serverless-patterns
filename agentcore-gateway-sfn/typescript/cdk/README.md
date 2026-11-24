# Amazon Bedrock AgentCore Gateway with AWS Step Functions connector target

This pattern deploys an Amazon Bedrock AgentCore Gateway that exposes an AWS Step Functions Standard workflow as MCP tools through the built-in Step Functions connector. A client starts the workflow through the Gateway. The workflow pauses on a `.waitForTaskToken` task that puts the task token in an Amazon SQS queue, and the client completes the task through the same Gateway with `SendTaskSuccess`.

Learn more about this pattern at Serverless Land Patterns: https://serverlessland.com/patterns/agentcore-gateway-sfn-typescript-cdk

Important: this application uses various AWS services and there are costs associated with these services after the Free Tier usage - please see the [AWS Pricing page](https://aws.amazon.com/pricing/) for details. You are responsible for any AWS costs incurred. No warranty is implied in this example.

## Requirements

* [Create an AWS account](https://portal.aws.amazon.com/gp/aws/developer/registration/index.html) if you do not already have one and log in. The IAM user that you use must have sufficient permissions to make necessary AWS service calls and manage AWS resources.
* [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html) installed and configured (the commands below were written with AWS CLI 2.31.3)
* [Git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git) installed
* [Node.js 22 or later](https://nodejs.org/en/download/) installed
* [AWS CDK v2](https://docs.aws.amazon.com/cdk/v2/guide/getting_started.html) installed (`npm install -g aws-cdk`); the commands below use `npx cdk`
* `curl` 7.75 or later (for `--aws-sigv4`), `jq`, and temporary AWS credentials for the Testing section

## Supported Regions

The [documentation](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/gateway-target-connector-step-functions.html) states that the Step Functions connector is available in all Regions where Amazon Bedrock AgentCore Gateway is available. Check the [AgentCore Regions page](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/agentcore-regions.html) for yours. The stack takes its Region from your AWS CLI or CDK environment (profile, `AWS_REGION` or `AWS_DEFAULT_REGION`). It was deployed and tested in us-west-2 and eu-central-1.

## Architecture

```
MCP client (SigV4, bedrock-agentcore:InvokeGateway)
   |  tools/call
   v
Amazon Bedrock AgentCore Gateway (AWS_IAM)
   |-- target "orders": StartExecution (pinned state machine), DescribeExecution
   |-- target "tasks":  SendTaskSuccess, SendTaskFailure
   v
AWS Step Functions Standard workflow
   |  sqs:sendMessage.waitForTaskToken  { taskToken, request }
   v
Amazon SQS queue  --->  client reads the token, then calls tasks___SendTaskSuccess
```

## How it works

1. The Gateway has two targets that use the Step Functions connector (`connectorId` `states`) and authenticates to Step Functions with its service role. There is no AWS Lambda function or MCP server in the tool path.
2. The `orders` target exposes `StartExecution`, pinned to the workflow through `stateMachineArn`, and `DescribeExecution`. The pinned ARN is not in the tool schema ([pinned parameters are removed from it](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/gateway-target-connector-step-functions.html)), and the Gateway rejects a call that sets it.
3. The `tasks` target exposes `SendTaskSuccess` and `SendTaskFailure`. The [connector documentation](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/gateway-target-connector-step-functions.html) recommends adding the task-token operations once per Gateway, on a separate target. Tool names are the target name, three underscores and the operation, for example `orders___StartExecution`.
4. The workflow has one task, `AskApprover`. It sends `{ "taskToken": ..., "request": <execution input> }` to the queue and waits, with a one hour timeout.
5. A client reads the message and calls `tasks___SendTaskSuccess` or `tasks___SendTaskFailure` through the Gateway. The execution resumes with the output the client sent.

Use the callback when a workflow has to wait for a decision or a piece of work from an agent or a person. Unlike the Step Functions patterns that call Amazon Bedrock AgentCore, here the Gateway calls Step Functions. Unlike `stepfunctions-sns-apigw-human-review`, where the approver answers through an email link and Amazon API Gateway, the approver here is an MCP client that completes the token through the same Gateway.

## Important Notes

* The Gateway uses the `AWS_IAM` authorizer. Requests must be signed with SigV4 (service name `bedrock-agentcore`), and the caller needs `bedrock-agentcore:InvokeGateway` on the Gateway ARN (output `GatewayArn`; this comes from the documentation, and the tests used an administrator role, so a least-privilege caller was not tested).
* Task tokens are secrets. IAM has no resource-level permission for `states:SendTaskSuccess` and `states:SendTaskFailure`, so the Gateway role allows them on `*`, as the [connector documentation](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/gateway-target-connector-step-functions.html) requires. Any caller of the Gateway who holds a valid task token can complete that task, so do not add unrelated workflows to this Gateway. The queue is encrypted and denies non-TLS requests.
* The workflow has no Retry on purpose: `States.TaskFailed` matches every error except `States.Timeout` ([error handling](https://docs.aws.amazon.com/step-functions/latest/dg/concepts-error-handling.html)), so a retry would also run after a `SendTaskFailure` from the approver and ask again after a rejection. A timeout is caught and ends in a `Fail` state named `ApprovalTimedOut`; the timeout and `SendTaskFailure` paths were not tested.
* The Gateway uses the L2 `Gateway` construct with an explicit protocol configuration, because the L2 default turns on semantic search. The configuration lists both MCP versions: a request without an `MCP-Protocol-Version` header is treated as 2025-03-26, and the Gateway rejected it when only 2025-06-18 was listed. The targets use the L1 `CfnGatewayTarget`: `aws-cdk-lib` has no L2 class for connector targets.
* Every connector operation entry carries `parameterValues`, `{}` when not pinned. An entry without it makes target creation fail in AWS CloudFormation with "Connector configurations must not be empty".
* See the [Amazon Bedrock AgentCore pricing page](https://aws.amazon.com/bedrock/agentcore/pricing/) for Gateway charges. AWS Step Functions and Amazon SQS charge per state transition and per request.

## Deployment Instructions

1. Clone the repository:
    ```bash
    git clone https://github.com/aws-samples/serverless-patterns
    cd serverless-patterns/agentcore-gateway-sfn/typescript/cdk
    ```

2. Install dependencies and build:
    ```bash
    npm install
    npm run build
    ```

3. If you have not used the AWS CDK in this account and Region before, bootstrap it:
    ```bash
    npx cdk bootstrap
    ```

4. Deploy the stack:
    ```bash
    npx cdk deploy
    ```

5. Note the stack outputs: `GatewayUrl`, `GatewayArn`, `StateMachineArn` and `QueueUrl`. The Testing section reads them from AWS CloudFormation. The deployment took about 2 to 3 minutes in the Regions tested.

## Testing

Run every block in the same terminal. A new terminal needs block 1 again.

1. Set the variables and a helper that sends a SigV4 signed MCP request:
    ```bash
    REGION=${AWS_REGION:-$(aws configure get region)}   # the Region you deployed to
    out() { aws cloudformation describe-stacks --stack-name AgentcoreGatewaySfnStack --region "$REGION" \
      --query "Stacks[0].Outputs[?OutputKey=='$1'].OutputValue" --output text; }
    GATEWAY_URL=$(out GatewayUrl); QUEUE_URL=$(out QueueUrl)
    eval "$(aws configure export-credentials --format env)"
    call() { curl -s -m 90 -X POST "$GATEWAY_URL" \
      --aws-sigv4 "aws:amz:$REGION:bedrock-agentcore" \
      --user "$AWS_ACCESS_KEY_ID:$AWS_SECRET_ACCESS_KEY" \
      -H "x-amz-security-token: $AWS_SESSION_TOKEN" \
      -H 'content-type: application/json' -d "$1"; echo; }
    ```

2. List the tools. Expected, in any order: `orders___StartExecution`, `orders___DescribeExecution`, `tasks___SendTaskSuccess` and `tasks___SendTaskFailure`:
    ```bash
    call '{"jsonrpc":"2.0","id":1,"method":"tools/list"}' | jq -r '.result.tools[].name'
    ```

3. Start the workflow through the Gateway. Expected: a result with `executionArn` and `startDate`:
    ```bash
    EXEC_ARN=$(call '{"jsonrpc":"2.0","id":2,"method":"tools/call","params":{"name":"orders___StartExecution","arguments":{"input":"{\"orderId\":\"42\",\"action\":\"approve\"}"}}}' \
      | jq -r '.result.content[0].text | fromjson | .executionArn')
    echo "$EXEC_ARN"
    ```

4. Read the task token from the queue. `--wait-time-seconds` enables long polling, so one call is enough; if it prints `None`, wait a few seconds and run it again. Expected: a body with `taskToken` and `request`. If you started more than one execution, the queue holds one message per execution; pick the one whose `request` matches. To see how many messages remain, use `aws sqs get-queue-attributes`:
    ```bash
    BODY=$(aws sqs receive-message --queue-url "$QUEUE_URL" --region "$REGION" \
      --wait-time-seconds 20 --max-number-of-messages 1 --query 'Messages[0].Body' --output text)
    echo "$BODY" | jq .
    TOKEN=$(echo "$BODY" | jq -r .taskToken)
    ```

5. Check that the execution is waiting. Expected: status `RUNNING`:
    ```bash
    call "{\"jsonrpc\":\"2.0\",\"id\":3,\"method\":\"tools/call\",\"params\":{\"name\":\"orders___DescribeExecution\",\"arguments\":{\"executionArn\":\"$EXEC_ARN\"}}}" \
      | jq -r '.result.content[0].text | fromjson | .status'
    ```

6. Complete the task through the Gateway. Expected: `isError` is `false` and the text is `{}`:
    ```bash
    call "{\"jsonrpc\":\"2.0\",\"id\":4,\"method\":\"tools/call\",\"params\":{\"name\":\"tasks___SendTaskSuccess\",\"arguments\":{\"taskToken\":\"$TOKEN\",\"output\":\"{\\\"approved\\\":true}\"}}}"
    ```

7. Read the result. Expected: status `SUCCEEDED` and an output of `{"approved":true}`. `includedData` set to `ALL_DATA` is needed to see the input and output:
    ```bash
    call "{\"jsonrpc\":\"2.0\",\"id\":5,\"method\":\"tools/call\",\"params\":{\"name\":\"orders___DescribeExecution\",\"arguments\":{\"executionArn\":\"$EXEC_ARN\",\"includedData\":\"ALL_DATA\"}}}" \
      | jq -r '.result.content[0].text | fromjson | {status, input, output}'
    ```

8. Negative checks. A wrong token should return `isError` `true` with an `InvalidToken` error. A call that sets the pinned `stateMachineArn` should be rejected with `cannot set parameter(s): [/stateMachineArn]`. An unsigned request should return HTTP 401:
    ```bash
    call '{"jsonrpc":"2.0","id":6,"method":"tools/call","params":{"name":"tasks___SendTaskSuccess","arguments":{"taskToken":"invalid","output":"{}"}}}'
    call "{\"jsonrpc\":\"2.0\",\"id\":7,\"method\":\"tools/call\",\"params\":{\"name\":\"orders___StartExecution\",\"arguments\":{\"input\":\"{}\",\"stateMachineArn\":\"$(out StateMachineArn)\"}}}"
    curl -s -o /dev/null -w '%{http_code}\n' -X POST "$GATEWAY_URL" -H 'content-type: application/json' \
      -d '{"jsonrpc":"2.0","id":8,"method":"tools/list"}'
    ```

## Cleanup

1. List executions that are still waiting for a task token (this step and step 3 use the variables from Testing block 1). An open execution ends by itself after one hour:
    ```bash
    aws stepfunctions list-executions --state-machine-arn "$(out StateMachineArn)" --status-filter RUNNING \
      --region "$REGION" --query 'executions[].executionArn' --output text
    ```
    Stop each one with `aws stepfunctions stop-execution --execution-arn <arn>` if you want it gone sooner.

2. Delete the stack. This deletes the Gateway, both targets, the workflow, the queue and any messages in it:
    ```bash
    npx cdk destroy
    ```
    Answer `y` at the prompt, or add `--force`.

3. Confirm the stack is gone. The destroy took 2 to 4 minutes in the tests, because the Gateway targets delete slowly:
    ```bash
    aws cloudformation describe-stacks --stack-name AgentcoreGatewaySfnStack --region "$REGION"
    ```
    Expected: a "does not exist" error. Apart from the CDK bootstrap resources, the stack creates no AWS Lambda functions, buckets or log groups, and the README creates nothing outside the stack.

----
Copyright 2026 Amazon.com, Inc. or its affiliates. All Rights Reserved.

SPDX-License-Identifier: MIT-0
