# Contain an AWS Lambda loop with Amazon CloudWatch and AWS Step Functions

This pattern deploys a demo AWS Lambda function that can invoke itself asynchronously, and a containment workflow for it. When Lambda recursive loop detection stops an invocation, it emits the `RecursiveInvocationsDropped` metric. An Amazon CloudWatch alarm on that metric changes state, and an Amazon EventBridge rule then starts an AWS Step Functions workflow that sets the function's reserved concurrency to 0, using an AWS SDK service integration. There is no Lambda function in the remediation path.

Learn more about this pattern at Serverless Land Patterns: https://serverlessland.com/patterns/lambda-recursion-sfn-typescript-cdk

Important: this application uses various AWS services and there are costs associated with these services after the Free Tier usage - please see the [AWS Pricing page](https://aws.amazon.com/pricing/) for details. You are responsible for any AWS costs incurred. No warranty is implied in this example.

## Requirements

* [Create an AWS account](https://portal.aws.amazon.com/gp/aws/developer/registration/index.html) if you do not already have one and log in. The IAM user that you use must have sufficient permissions to make necessary AWS service calls and manage AWS resources.
* [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html) installed and configured
* [Git Installed](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)
* [Node.js](https://nodejs.org/en/download/) 22 or later and npm installed
* [AWS Cloud Development Kit](https://docs.aws.amazon.com/cdk/v2/guide/getting-started.html) (AWS CDK) v2 installed, and the target account and Region [bootstrapped](https://docs.aws.amazon.com/cdk/v2/guide/bootstrapping.html) (`npx cdk bootstrap` once per account and Region)
* An unreserved Lambda concurrency of at least 105 in the Region. The stack reserves 5 for the demo function, and Lambda requires [at least 100 to stay unreserved](https://docs.aws.amazon.com/lambda/latest/api/API_PutFunctionConcurrency.html). Check `UnreservedConcurrentExecutions` in the output of `aws lambda get-account-settings`.

## Supported Regions

The stack has no Region-specific values and takes the account and Region from your AWS CLI environment. The Lambda documentation says: "Lambda recursive loop detection is supported in all commercial Regions." See [Use Lambda recursive loop detection to prevent infinite loops](https://docs.aws.amazon.com/lambda/latest/dg/invocation-recursion.html). This pattern was deployed and tested in us-west-2 and eu-central-1.

## Architecture

```
aws lambda invoke --invocation-type Event (one manual call, payload {"loop":true,"hop":0})
        |
        v
AWS Lambda "looper" --- invokes itself asynchronously (hop plus 1) ---+
        ^                                                              |
        +--------------------------------------------------------------+
        Lambda recursive loop detection stops the chain after approximately 16 invocations
                      |
                      v  metric AWS/Lambda RecursiveInvocationsDropped
Amazon CloudWatch alarm (1-minute period) --> default event bus: "CloudWatch Alarm State Change" (ALARM)
                      |  Amazon EventBridge rule
                      v
AWS Step Functions workflow (AWS SDK integration, no Lambda function)
   lambda:PutFunctionConcurrency      ReservedConcurrentExecutions = 0
```

## How it works

1. `aws lambda invoke` with `--invocation-type Event` sends one event with the payload `{"loop":true,"hop":0}`. The `looper` function invokes itself asynchronously with `hop` plus 1, so the function triggers itself.
1. After approximately 16 invocations in one chain, Lambda stops the next invocation and emits `RecursiveInvocationsDropped` in the `AWS/Lambda` namespace. The Lambda documentation says that Lambda "detects loops comprised only of Lambda Event Functions, which might invoke each other synchronously or asynchronously". The stack leaves the function's recursive loop setting at its default (`Terminate`); the setting `Allow` lets the function be invoked recursively.
1. A CloudWatch alarm on that metric (dimension `FunctionName`, `Sum` >= 1, one 1-minute period, missing data treated as not breaching) enters `ALARM`. The [supported alarm actions](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/alarm-actions.html) do not include starting a state machine, but CloudWatch sends [alarm state changes to Amazon EventBridge](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/cloudwatch-and-eventbridge.html). An Amazon EventBridge rule on the default event bus matches the `CloudWatch Alarm State Change` event for this alarm with state `ALARM` and starts the workflow.
1. The workflow checks that the input is an alarm event in state `ALARM` (otherwise it ends in `Fail` with error `InvalidEvent`) and calls `lambda:PutFunctionConcurrency` with 0. If the call fails (after retries for transient errors, at once for permanent errors), the workflow ends in `Fail` (`ThrottleFailed`); otherwise it ends in `Succeed`.
1. Permanent errors (resource not found, invalid parameter, permissions) are not retried. Throttling, service errors, conflicts and timeouts are retried 3 times. The call is idempotent, so a second alarm event repeats the same result.

Why the workflow matters: Lambda stops the chain that it detects, and the [documentation](https://docs.aws.amazon.com/lambda/latest/dg/invocation-recursion.html) lists reducing concurrency to zero as a step you take yourself to prevent a reoccurrence. The function itself still runs any new event with `"loop":true` while its concurrency is above 0. The detection also notifies by email and the AWS Health Dashboard with a delay of up to 3.5 hours; Lambda emits the metric as soon as it stops the invocation.

The closest patterns here are [cdk-closed-loop-serverless-control](../../../cdk-closed-loop-serverless-control), where a Lambda controller reads alarms on custom third-party metrics to switch calls on and off, and [cloudwatch-log-alarm-lambda-remediation-cdk](../../../cloudwatch-log-alarm-lambda-remediation-cdk), which remediates with Lambda; this pattern triggers on a native Lambda metric and contains the loop with a Step Functions SDK integration that changes the Lambda function.

## Important Notes

* **The loop is a demo.** It starts only when you invoke the function with `"loop":true`. Events without it are handled once. The function also stops a chain after 25 invocations (`MAX_HOPS`), even if detection does not act. Asynchronous invocation can deliver the same event more than once ([documentation](https://docs.aws.amazon.com/lambda/latest/dg/invocation-async-error-handling.html)), and a duplicate delivery runs the function again and can start a second chain, so the total can exceed 25 (not seen in the tests). Detection needs the Node.js SDK v3 3.105.0 or later in the function. The function uses the SDK that its runtime provides, which depends on the runtime version and Region, and the [Lambda documentation](https://docs.aws.amazon.com/lambda/latest/dg/nodejs-handler.html) recommends including the SDK clients that you need in the deployment package. If the count in Testing step 2 is 25, detection did not act.
* **Events sent while the reserved concurrency is 0 do not run.** Lambda accepts an asynchronous call (status 202), but the function does not run. In the tests such an event was counted in the `AsyncEventsDropped` metric within the same minute and did not run when the concurrency was restored seconds later, so do not rely on it running after you restore the concurrency. The function has no retries and a maximum event age of 1 minute (the default is 6 hours, see the [documentation](https://docs.aws.amazon.com/lambda/latest/dg/invocation-async-error-handling.html)).
* **The function stays throttled after a run.** The workflow leaves the concurrency at 0. A redeploy with no template change does not restore it. Use the reset command in Testing.
* **One run per alarm transition.** In the tests the alarm stayed in `ALARM` for 6 minutes after it fired. The rule starts the workflow only when the alarm enters `ALARM`, so a loop that starts again during that time would start no new run and would not be contained (this follows from the rule and was not tested). A run that ends in `ThrottleFailed` is not retried while the alarm stays in `ALARM`. The reset in Testing waits for `OK` before it restores the concurrency.
* **IAM.** The workflow role can call `lambda:PutFunctionConcurrency` on the looper function ARN only. The function role can call `lambda:InvokeFunction` on the function itself; the function has a name built from the stack name so that its policy can refer to it without a circular dependency. The CDK adds CloudWatch Logs delivery actions on `*` for the state machine log group, and the AWS managed policy `AWSLambdaBasicExecutionRole` to the function role. The trust policies of the workflow role and the rule target role have `aws:SourceAccount` conditions and `aws:SourceArn` conditions (`stateMachine:*` and `rule/*` in this account and Region), so they restrict by account and Region, not by individual resource. The template has no resource-based policy that grants outside access and no public endpoint.
* **Starting the workflow by hand.** `states:StartExecution` on the state machine is equivalent to `lambda:PutFunctionConcurrency` on the function, because the workflow does not authenticate its input: anyone who starts it with an alarm-shaped event in state `ALARM` throttles the function (Testing step 6 does exactly this). Only the rule target role has it here; grant it to no one else.
* **No dead-letter queue on the rule.** The rule target retries up to 5 times within 1 hour. The pattern has no dead-letter queue, to keep it to four services, so an alarm event that EventBridge still cannot deliver is dropped, and it has no alarm or notification for an execution that starts and then fails. Check with `aws stepfunctions list-executions --state-machine-arn $SM --status-filter FAILED` (`$SM` is defined in Testing step 0; Testing step 6 creates one failed run on purpose). For production, add a dead-letter queue to the rule target and alarms on the failed executions.
* **Four services.** The stack uses AWS Lambda, Amazon CloudWatch, Amazon EventBridge and AWS Step Functions. The Amazon EventBridge rule is the wiring that starts the workflow, because CloudWatch alarm actions cannot start a state machine.
* The state machine logs at level `ALL` with execution data. The data holds the alarm event, which includes your account ID, for one week.
* **Cost while idle.** The stack has no always-on compute. The CloudWatch alarm is billed per alarm metric for as long as the stack exists ([CloudWatch pricing](https://aws.amazon.com/cloudwatch/pricing/)); the other services bill by use. Delete the stack when you finish testing.

## Deployment Instructions

1. Clone the repository and change into the pattern folder:
    ```bash
    git clone https://github.com/aws-samples/serverless-patterns
    cd serverless-patterns/lambda-recursion-sfn/typescript/cdk
    ```
1. Install the dependencies:
    ```bash
    npm install
    ```
1. Deploy the stack:
    ```bash
    npx cdk deploy
    ```

## Testing

Run the commands in one shell, with your AWS CLI configured for the Region where you deployed. Step 0 re-derives everything from the stack outputs (stack name `LambdaRecursionSfnStack`).

0. Read the outputs and define helpers. `tick` invokes the function asynchronously (`$1` is the `loop` flag) and prints the status code, `count` counts looper invocations in the log since the epoch milliseconds in `$1`.
    ```bash
    out() { aws cloudformation describe-stacks --stack-name LambdaRecursionSfnStack --query "Stacks[0].Outputs[?OutputKey=='$1'].OutputValue" --output text; }
    FN=$(out FunctionName); FN_LOGS=$(out FunctionLogGroup); ALARM=$(out AlarmName); SM=$(out StateMachineArn); SM_LOGS=$(out StateMachineLogGroup)
    tick() { aws lambda invoke --function-name "$FN" --invocation-type Event --cli-binary-format raw-in-base64-out --payload "{\"loop\":$1,\"hop\":0}" --query StatusCode --output text /dev/null; }
    count() { aws logs filter-log-events --log-group-name $FN_LOGS --filter-pattern '"looper hop="' --start-time $1 --query 'length(events)'; }
    aws lambda get-function-concurrency --function-name $FN --query ReservedConcurrentExecutions
    ```
    Look for `5`.
1. Negative case: an event without the loop flag runs the function once.
    ```bash
    T0=$(( $(date +%s) * 1000 )); tick false; sleep 15; count $T0
    ```
    Look for `202` (Lambda accepted the event), then `1`. If the count is `0`, wait a few seconds and run `count $T0` again.
2. Start the loop with one event.
    ```bash
    N0=$(aws stepfunctions list-executions --state-machine-arn $SM --query 'length(executions)')
    T1=$(( $(date +%s) * 1000 )); tick true; sleep 45; count $T1
    ```
    Look for `202`, then a count of approximately 16 (the Lambda documentation says "approximately 16"), well below 25. If the log is empty, wait and run `count $T1` again.
3. Wait for the workflow. The alarm needs the next evaluation after Lambda emits the metric: the workflow started 63 to 104 seconds after the loop event in the tests, so allow a few minutes. This loop checks every 30 seconds for up to 10 minutes and stops when a new execution has finished.
    ```bash
    for i in $(seq 1 20); do N=$(aws stepfunctions list-executions --state-machine-arn $SM --query 'length(executions)'); S=$(aws stepfunctions list-executions --state-machine-arn $SM --query 'executions[0].status' --output text); echo "$(date +%T) executions=$N latest=$S"; [ "$N" -gt "${N0:-0}" ] && [ "$S" != "RUNNING" ] && break; sleep 30; done
    aws cloudwatch list-metrics --namespace AWS/Lambda --metric-name RecursiveInvocationsDropped --dimensions Name=FunctionName,Value=$FN --query 'length(Metrics)'
    ```
    Look for `latest=SUCCEEDED` and a metric count of 1 or more. If the count is 0, wait and run the second command again. If no execution starts, check the alarm with `aws cloudwatch describe-alarms --alarm-names $ALARM --query 'MetricAlarms[0].StateValue' --output text` and the log group `$SM_LOGS`.
4. Read the effect directly, not the workflow status. Invoking the function now must be refused.
    ```bash
    aws lambda get-function-concurrency --function-name $FN --query ReservedConcurrentExecutions
    aws lambda invoke --function-name $FN --cli-binary-format raw-in-base64-out --payload '{"loop":false}' /dev/null
    ```
    Look for `0` and a `TooManyRequestsException` error from the invoke call.
5. Send a second loop event. Lambda accepts it, but the function is throttled, so nothing runs.
    ```bash
    T2=$(( $(date +%s) * 1000 )); tick true; sleep 30; count $T2
    ```
    Look for `202`, then `0`.
6. Negative cases for the workflow. An input that is not an alarm event fails with `InvalidEvent`; an alarm-shaped input succeeds again, which shows that a repeated alarm is safe.
    ```bash
    for IN in '{}' '{"detail":{"state":{"value":"ALARM"}}}'; do EX=$(aws stepfunctions start-execution --state-machine-arn $SM --input "$IN" --query executionArn --output text); sleep 10; aws stepfunctions describe-execution --execution-arn $EX --query '[status,error]' --output text; done
    ```
    Look for `FAILED InvalidEvent`, then `SUCCEEDED None`.
7. Reset, so you can run the test again. Wait until the alarm shows `OK`, because the workflow starts only when the alarm enters `ALARM`; in the tests that took 6 minutes after the alarm fired. Then restore the concurrency.
    ```bash
    for i in $(seq 1 20); do A=$(aws cloudwatch describe-alarms --alarm-names $ALARM --query 'MetricAlarms[0].StateValue' --output text); echo "$(date +%T) $A"; [ "$A" = "OK" ] && break; sleep 30; done
    if [ "$A" = "OK" ]; then aws lambda put-function-concurrency --function-name $FN --reserved-concurrent-executions 5; else echo "The alarm is still $A: wait and run this step again."; fi
    ```
    Look for `OK`, then `ReservedConcurrentExecutions` 5.

## Cleanup

1. Note the log group names (the variables come from Testing step 0: run that step again if you opened a new shell), then delete the stack. The demo resources use the `DESTROY` removal policy and have no deletion protection, so the function logs and the workflow logs are deleted with the stack.
    ```bash
    echo $FN_LOGS $SM_LOGS
    npx cdk destroy
    ```
1. Check that nothing is left. The command should print an empty list for both names. The bootstrap resources of the AWS CDK, which hold the function code asset, stay in your account.
    ```bash
    aws logs describe-log-groups --log-group-name-prefix "$FN_LOGS" --query 'logGroups[].logGroupName'
    aws logs describe-log-groups --log-group-name-prefix "$SM_LOGS" --query 'logGroups[].logGroupName'
    ```

----
Copyright 2026 Amazon.com, Inc. or its affiliates. All Rights Reserved.

SPDX-License-Identifier: MIT-0
