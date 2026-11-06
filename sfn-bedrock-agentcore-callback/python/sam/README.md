# AWS Step Functions to Amazon Bedrock AgentCore Runtime with a task-token callback

This pattern shows two ways for AWS Step Functions to invoke an Amazon Bedrock AgentCore Runtime agent through the AWS SDK service integration. One state machine uses the Request Response pattern and waits for the agent's HTTP response, for up to 15 minutes. The other uses the Wait for a Callback with a Task Token pattern for agent work that runs longer: the agent returns immediately, does its work in the background, and resumes the workflow with `SendTaskSuccess` or `SendTaskFailure`. One agent serves both state machines.

Important: this application uses various AWS services and there are costs associated with these services after the Free Tier usage - please see the [AWS Pricing page](https://aws.amazon.com/pricing/) for details. You are responsible for any AWS costs incurred. No warranty is implied in this example.

## Requirements

* [Create an AWS account](https://portal.aws.amazon.com/gp/aws/developer/registration/index.html) if you do not already have one and log in. The IAM user that you use must have sufficient permissions to make necessary AWS service calls and manage AWS resources.
* [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html) installed and configured
* [Git Installed](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)
* [AWS Serverless Application Model](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-sam-cli-install.html) (AWS SAM) installed
* Python 3 with `pip`, and `zip`. The build downloads Linux ARM64 wheels, so it works on any operating system and does not need Docker.
* Access to the Amazon Bedrock model that the agent calls. The default is the `global.anthropic.claude-haiku-4-5-20251001-v1:0` inference profile. To use another model, set the `ModelId` parameter during deployment.
* A Region where Amazon Bedrock AgentCore Runtime is available. This pattern was tested in `us-east-1`.

## Deployment Instructions

1. Create a new directory, navigate to that directory in a terminal and clone the GitHub repository:
    ```
    git clone https://github.com/aws-samples/serverless-patterns
    ```
1. Change directory to the pattern directory:
    ```
    cd serverless-patterns/sfn-bedrock-agentcore-callback/python/sam
    ```
1. Create an S3 bucket for the agent code. New buckets block public access by default. Replace `REGION` with your Region:
    ```
    ACCOUNT_ID=$(aws sts get-caller-identity --query Account --output text)
    BUCKET=agentcore-code-$ACCOUNT_ID-REGION
    aws s3 mb s3://$BUCKET --region REGION
    ```
1. Package the agent and upload it. The script prints the S3 key of the zip:
    ```
    ./build.sh $BUCKET
    ```
1. From the command line, use AWS SAM to deploy the AWS resources for the pattern as specified in the template.yaml file:
    ```
    sam deploy --guided
    ```
1. During the prompts:
    * Enter a stack name
    * Enter the desired AWS Region. Use the same Region as the bucket.
    * For `AgentCodeBucket`, enter the bucket name.
    * For `AgentCodeKey`, enter the key that `build.sh` printed.
    * Keep the defaults for `AgentRuntimeName` and `ModelId`, or change them.
    * Allow SAM CLI to create IAM roles with the required permissions.

    Once you have run `sam deploy --guided` mode once and saved arguments to a configuration file (samconfig.toml), you can use `sam deploy` in future to use these defaults. After you change the agent code, run `./build.sh` again and pass the new key with `sam deploy --parameter-overrides AgentCodeKey=NEW_KEY`.

1. Note the outputs from the SAM deployment process. These contain the resource names and/or ARNs which are used for testing.

## How it works

The template creates the following resources:

* **An AgentCore Runtime agent** deployed from the code zip in S3 (direct code deployment, Python 3.13). The agent uses [Strands Agents](https://strandsagents.com/) to call the Amazon Bedrock model.
* **An execution role for the agent** that can invoke Amazon Bedrock models, write to its log group, and call `states:SendTaskSuccess`, `states:SendTaskFailure` and `states:SendTaskHeartbeat`. The task token authorizes the callback calls, so they use `Resource: "*"` instead of a state machine ARN.
* **A Request Response state machine.** The Task state uses `arn:aws:states:::aws-sdk:bedrockagentcore:invokeAgentRuntime`. Step Functions waits for the agent's response, for up to 15 minutes, and parses the JSON response into the state output.
* **A callback state machine.** The Task state appends `.waitForTaskToken` to the same resource and passes `$states.context.Task.Token` in the payload as `task_token`. Step Functions pauses until the agent returns the token. `TimeoutSeconds` is set to 7200, so a lost callback cannot leave an execution waiting for up to a year.

Both state machine roles can call `bedrock-agentcore:InvokeAgentRuntime` on the runtime ARN and on the runtime ARN followed by `/*`. Step Functions authorizes the call against the runtime and against its endpoint (`runtime/NAME/runtime-endpoint/DEFAULT`). If you grant only one of the two, the call fails with `AccessDeniedException`.

The agent code in `agent/main.py` decides the pattern from the payload:

* **No `task_token`:** the agent runs inline and returns `{"result": ...}` in the response.
* **A `task_token`:** the agent starts a background task and returns `{"status": "ACCEPTED"}` immediately. When the work finishes, it sends the result with `SendTaskSuccess`. If the work fails, it sends `SendTaskFailure` with the error `AgentRuntimeError`, so the execution fails at once instead of waiting for its timeout.

A few details in the agent code matter:

* `@app.async_task` marks the background work, so the runtime reports itself busy and AgentCore keeps the session alive. Without it, the platform can stop the session while the work is still running, and the callback never arrives.
* The agent call and the callback calls run in worker threads (`asyncio.to_thread`), so the event loop stays free to answer health checks.
* The agent creates a new `Agent` object for each invocation. Invocations that share a runtime session therefore do not share conversation history.
* `Accept` is set in the Task state's `Arguments`, not in `Payload`. In `Payload` it would be sent to the agent as data instead of as a header.

Choosing a pattern:

* Use Request Response when the agent finishes within 15 minutes. It works in Standard and Express workflows.
* Use the callback pattern when the agent can take longer. It works in Standard workflows only. The callback pattern needs the AWS SDK integration (`aws-sdk:bedrockagentcore`). The optimized Amazon Bedrock AgentCore integration supports only Request Response.

## Testing

1. Set the state machine ARNs from the stack outputs. Replace `STACK_NAME` with your stack name:
    ```bash
    RR_ARN=$(aws cloudformation describe-stacks --stack-name STACK_NAME --query "Stacks[0].Outputs[?OutputKey=='RequestResponseStateMachineArn'].OutputValue" --output text)
    CB_ARN=$(aws cloudformation describe-stacks --stack-name STACK_NAME --query "Stacks[0].Outputs[?OutputKey=='CallbackStateMachineArn'].OutputValue" --output text)
    ```
1. Start the Request Response state machine:
    ```bash
    EXEC=$(aws stepfunctions start-execution --state-machine-arn $RR_ARN --input '{"prompt":"What is the capital of Japan? Answer in one word."}' --query executionArn --output text)
    ```
1. After a few seconds, read the result:
    ```bash
    aws stepfunctions describe-execution --execution-arn $EXEC --query "[status,output]"
    ```
    The status is `SUCCEEDED`, and the output contains the agent's answer:
    ```json
    {"result":{"role":"assistant","content":[{"text":"Tokyo"}], ...}}
    ```
1. Start the callback state machine and read its result the same way:
    ```bash
    EXEC=$(aws stepfunctions start-execution --state-machine-arn $CB_ARN --input '{"prompt":"What is the capital of Egypt? Answer in one word."}' --query executionArn --output text)
    aws stepfunctions describe-execution --execution-arn $EXEC --query "[status,output]"
    ```
    While the agent works, the status is `RUNNING`. After the agent calls `SendTaskSuccess`, the status is `SUCCEEDED` and the output is the JSON that the agent sent:
    ```json
    {"result": {"role": "assistant", "content": [{"text": "Cairo"}], ...}}
    ```
1. To see the failure path, redeploy with a model ID that does not exist, then start the callback state machine again:
    ```bash
    sam deploy --parameter-overrides ModelId=invalid-model-id
    ```
    The execution fails within seconds with the error `AgentRuntimeError` and the cause `The provided model identifier is invalid.` Redeploy with the original `ModelId` value when you are done.

The agent's logs are in the CloudWatch Logs group whose name starts with `/aws/bedrock-agentcore/runtimes/`, followed by the runtime ID.

## Cleanup

1. Delete the stack:
    ```bash
    sam delete
    ```
1. Delete the agent code and the bucket:
    ```bash
    aws s3 rm s3://$BUCKET --recursive
    aws s3 rb s3://$BUCKET
    ```
1. Optionally, delete the agent's log group, which AgentCore creates and the stack does not delete:
    ```bash
    aws logs describe-log-groups --log-group-name-prefix /aws/bedrock-agentcore/runtimes/ --query "logGroups[].logGroupName"
    aws logs delete-log-group --log-group-name LOG_GROUP_NAME
    ```

----
Copyright 2026 Amazon.com, Inc. or its affiliates. All Rights Reserved.

SPDX-License-Identifier: MIT-0
