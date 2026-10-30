# AWS Step Functions release gate with AWS CodeBuild and AWS CloudFormation change sets

This pattern deploys an AWS Step Functions Standard workflow that gates an AWS CloudFormation deployment. AWS CodeBuild checks the template through the optimized `startBuild.sync` integration, the workflow creates an AWS CloudFormation change set through the AWS SDK integration, and a human approval delivered over Amazon SNS decides whether the change set is executed or deleted. The synthesized template contains no AWS Lambda function.

Learn more about this pattern at Serverless Land Patterns: https://serverlessland.com/patterns/sfn-codebuild-release-gate-typescript-cdk

Important: this application uses various AWS services and there are costs associated with these services after the Free Tier usage - please see the [AWS Pricing page](https://aws.amazon.com/pricing/) for details. You are responsible for any AWS costs incurred. No warranty is implied in this example.

## Requirements

* [Create an AWS account](https://portal.aws.amazon.com/gp/aws/developer/registration/index.html) if you do not already have one and log in. The IAM user that you use must have sufficient permissions to make necessary AWS service calls and manage AWS resources.
* [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html) v2 installed and configured (commands written against 2.31.3)
* [Git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git) installed
* [Node.js 22 or later](https://nodejs.org/en/download/) installed
* [AWS CDK v2](https://docs.aws.amazon.com/cdk/v2/guide/getting_started.html) installed (`npm install -g aws-cdk`)
* [jq](https://jqlang.org/) installed (the `read_token` helper uses it to read the task token from the execution history)

## Supported Regions

Tested in us-east-1, us-west-2 and eu-central-1. The stack has no Region-specific values, so other Regions that offer AWS Step Functions, AWS CodeBuild, AWS CloudFormation and Amazon SNS should work, but they were not tested.

## Architecture

```
Execution input: stackName, changeSetType (CREATE or UPDATE), templateBody
   |
   v
AWS Step Functions (Standard)
   1. codebuild:startBuild.sync ---------> AWS CodeBuild policy check (fails the execution before any change set exists)
   2. cloudformation:createChangeSet ----> poll describeChangeSet
        no changes ---> deleteChangeSet ---> Succeed ("NothingToDeploy")
   3. sns:publish.waitForTaskToken ------> Amazon SNS topic ---> approver (task token + change list)
        send-task-failure or timeout ---> deleteChangeSet ---> Fail
   4. send-task-success ---> executeChangeSet ---> poll the change set ExecutionStatus, then describeStacks
        ---> Succeed or Fail (rollback)
```

## How it works

1. The execution input carries a stack name, a change set type and a small JSON template. AWS CodeBuild runs a project with no source. The template arrives as the `TEMPLATE_BODY` environment variable override, and an inline buildspec rejects templates that contain `AWS::IAM::*` resources or an `AWS::SQS::Queue` without an explicit `DeletionPolicy`. A failed build ends the execution with `PolicyCheckFailed`.
2. The same template body goes to `createChangeSet`. The call returns before the change set is ready, so the workflow waits and polls `describeChangeSet`. A `FAILED` change set whose reason says it contains no changes is deleted and ends in a clean `NothingToDeploy`.
3. The workflow publishes the task token and the list of changes to the Amazon SNS topic and waits. `send-task-failure` or the timeout deletes the change set and fails the execution.
4. `send-task-success` runs `executeChangeSet`. The workflow polls `describeChangeSet` until `ExecutionStatus` is `EXECUTE_COMPLETE` or `EXECUTE_FAILED`, so a stack status from before the update started is never read as the result. It then polls `describeStacks` until the status leaves `*_IN_PROGRESS` and fails the execution on any status other than `CREATE_COMPLETE` or `UPDATE_COMPLETE`.

Use AWS CodePipeline when a pipeline with source stages fits; use this pattern when the gate is one step inside a larger Step Functions workflow. The nearest existing patterns are `stepfunctions-sns-apigw-human-review` (approval only) and `eventbridge-codebuild-sns` (Amazon EventBridge starts CodeBuild). The new part is `startBuild.sync` plus a change set preview inside one workflow.

## Important Notes

* The state machine role can call CloudFormation only on stacks named `release-gate-*`; the workflow names its change sets `gate-<uuid>`. The target stack uses a dedicated CloudFormation service role that can only manage Amazon SQS queues named `release-gate-*`: a template that asks for a queue with another name is refused (the stack rolls back and the execution ends in `StackOperationFailed`). The state machine role may pass only that role, and only to CloudFormation.
* `changeSetType` comes from the input: `CREATE` for a new stack, `UPDATE` for an existing one. Templates must be JSON and small: the body travels in the execution input, in the `createChangeSet` request and in a CodeBuild environment variable override. In the test, a 48,765 byte template passed the policy check and `createChangeSet`; a 64,470 byte template passed the policy check, and `createChangeSet` then refused it because a template body in a request is limited to 51,200 bytes (the execution ended in `CloudFormation.CloudFormationException`). A `CREATE` change set leaves the stack in `REVIEW_IN_PROGRESS` until it is executed or the stack is deleted. A rejected or timed out `CREATE` therefore leaves that empty stack behind; delete it, or a stack in `ROLLBACK_COMPLETE` after a failed create, with `aws cloudformation delete-stack`. All three input fields are required.
* The policy check reads the template text and does not expand a `Transform`. The service role is the real limit: a template with a `Transform` makes the change set fail (the service role has no permission on transforms) and the execution ends in `ChangeSetFailed`.
* The approval timeout is 3600 seconds. Deploy with `-c approvalTimeoutSeconds=<60 to 86400>` to change it, and with `-c approverEmail=<address>` to subscribe an email address (confirm the subscription before starting an execution; the email delivery was not tested).
* `SendTaskSuccess` and `SendTaskFailure` are IAM-authorized, so the token alone approves nothing, but the token and the template can be read by principals that may read the execution history, the CodeBuild build details or the SNS message: grant those separately from `states:SendTaskSuccess`. The topic is not encrypted with an AWS KMS key; use a customer managed key for production.
* The approval state has no retry (a rejection is also a task failure) and no heartbeat; the timeout ends abandoned approvals. Logs use level `ERROR` without execution data, so the token and the template stay out of the state machine log group. Two executions for the same stack are not serialized.
* Cost is close to zero for a test: CodeBuild bills per build minute, Step Functions Standard per state transition, nothing by the hour.

## Deployment Instructions

1. Clone the repository:
    ```bash
    git clone https://github.com/aws-samples/serverless-patterns
    cd serverless-patterns/sfn-codebuild-release-gate/typescript/cdk
    ```

2. Install dependencies:
    ```bash
    npm install
    ```

3. Bootstrap the account and Region once if they have never used the AWS CDK, then deploy (add `-c approverEmail=<address>` to receive the approval message by email). The deployment prints the four stack outputs named under Testing:
    ```bash
    npx cdk bootstrap
    npx cdk deploy
    ```

## Testing

Run the commands from the pattern folder. Stack outputs: `StateMachineArn`, `ApprovalTopicArn`, `BuildLogGroupName`, `StateMachineLogGroupName`. The helpers exist only in the current shell: in a new terminal run the first block of step 1 (the helpers) again. `start_gate` sets `EXEC_ARN` for the new execution and `read_token` resets `TOKEN` for it.

1. Define the helpers:
    ```bash
    SM_ARN=$(aws cloudformation describe-stacks --stack-name SfnCodebuildReleaseGateStack --query "Stacks[0].Outputs[?OutputKey=='StateMachineArn'].OutputValue" --output text)
    start_gate() { EXEC_ARN=$(aws stepfunctions start-execution --state-machine-arn "$SM_ARN" --input "file://$1" --query executionArn --output text); }
    read_token() { TOKEN=""; while [ -z "$TOKEN" ]; do sleep 10
      TOKEN=$(aws stepfunctions get-execution-history --execution-arn "$EXEC_ARN" --query "events[?type=='TaskScheduled' && taskScheduledEventDetails.resourceType=='sns'].taskScheduledEventDetails.parameters | [0]" --output text 2>/dev/null | jq -r '.Message | if type=="string" then fromjson else . end | .taskToken' 2>/dev/null)
      [ -n "$TOKEN" ] && return 0
      [ "$(aws stepfunctions describe-execution --execution-arn "$EXEC_ARN" --query status --output text)" = RUNNING ] || { echo "The execution ended before the approval step:"; wait_gate; return 1; }
    done; }
    wait_gate() { until [ "$(aws stepfunctions describe-execution --execution-arn "$EXEC_ARN" --query status --output text)" != RUNNING ]; do sleep 10; done
      aws stepfunctions describe-execution --execution-arn "$EXEC_ARN" --query "{status:status,error:error}"; }
    ```
   Then start a `CREATE` execution and read its task token from the execution history (or from the email):
    ```bash
    start_gate sample-inputs/create-v1.json
    read_token
    ```

2. Approve, then check the deployed stack independently:
    ```bash
    aws stepfunctions send-task-success --task-token "$TOKEN" --task-output '{}'
    wait_gate
    aws cloudformation describe-stacks --stack-name release-gate-demo-app --query "Stacks[0].StackStatus" --output text
    ```
   Expected: status `SUCCEEDED` and stack status `CREATE_COMPLETE`.

3. Policy violation. `sample-inputs/update-policy-violation.json` has a queue without `DeletionPolicy`:
    ```bash
    start_gate sample-inputs/update-policy-violation.json
    wait_gate
    aws cloudformation list-change-sets --stack-name release-gate-demo-app --query "Summaries[?ExecutionStatus=='AVAILABLE'].ChangeSetName"
    ```
   Expected: status `FAILED` with error `PolicyCheckFailed`, and an empty list. Read the policy check output with `aws logs tail <BuildLogGroupName> --since 15m`.

4. No changes. `sample-inputs/update-v1.json` equals the deployed template:
    ```bash
    start_gate sample-inputs/update-v1.json
    wait_gate
    aws stepfunctions describe-execution --execution-arn "$EXEC_ARN" --query output --output text | jq -r '.cs.StatusReason'
    ```
   Expected: status `SUCCEEDED` without any approval, then the change set status reason: `The submitted information didn't contain changes. Submit different information to create a change set.`

5. Rejection. `sample-inputs/update-v2.json` changes the visibility timeout from 30 to 60:
    ```bash
    start_gate sample-inputs/update-v2.json
    read_token
    aws stepfunctions send-task-failure --task-token "$TOKEN" --error Rejected --cause "not approved"
    wait_gate
    aws cloudformation list-change-sets --stack-name release-gate-demo-app --query "Summaries[?ExecutionStatus=='AVAILABLE'].ChangeSetName"
    ```
   Expected: status `FAILED` with error `NotApproved`, and an empty list.

6. Update. Start the same change again and approve it, then read the result from the queue itself:
    ```bash
    start_gate sample-inputs/update-v2.json
    read_token
    aws stepfunctions send-task-success --task-token "$TOKEN" --task-output '{}'
    wait_gate
    QUEUE_URL=$(aws sqs list-queues --queue-name-prefix release-gate-demo-app --query "QueueUrls[0]" --output text)
    aws sqs get-queue-attributes --queue-url "$QUEUE_URL" --attribute-names VisibilityTimeout --query Attributes
    ```
   Expected: status `SUCCEEDED` and `VisibilityTimeout` of `60`.

## Cleanup

1. Delete the target stack first. Its service role is deleted with the stack below, so the order matters:
    ```bash
    aws cloudformation delete-stack --stack-name release-gate-demo-app
    aws cloudformation wait stack-delete-complete --stack-name release-gate-demo-app
    ```
2. Delete the CDK stack. The queue in the target stack and its messages are gone after step 1; the log groups, the topic and any email subscription are removed here:
    ```bash
    npx cdk destroy
    ```

----
Copyright 2026 Amazon.com, Inc. or its affiliates. All Rights Reserved.

SPDX-License-Identifier: MIT-0
