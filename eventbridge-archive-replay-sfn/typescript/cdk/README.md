# Amazon EventBridge archive replay started by AWS Step Functions

This pattern recovers Amazon EventBridge events that were lost while a rule target was failing. A custom event bus archives its events, and an Amazon CloudWatch alarm watches the failed deliveries of one rule. When the alarm goes from ALARM to OK, an AWS Step Functions workflow works out the outage window from the alarm history, calls `StartReplay` for that rule only, polls `DescribeReplay` until it finishes, and publishes the result to Amazon Simple Notification Service (Amazon SNS). The workflow uses AWS SDK integrations only, and the synthesized template contains no AWS Lambda function. An Amazon Simple Queue Service (Amazon SQS) queue is the demo target that is made to fail.

Learn more about this pattern at Serverless Land Patterns: https://serverlessland.com/patterns/eventbridge-archive-replay-sfn-typescript-cdk

Important: this application uses various AWS services and there are costs associated with these services after the Free Tier usage - please see the [AWS Pricing page](https://aws.amazon.com/pricing/) for details. You are responsible for any AWS costs incurred. No warranty is implied in this example.

## Requirements

* [Create an AWS account](https://portal.aws.amazon.com/gp/aws/developer/registration/index.html) if you do not already have one and log in. The IAM user that you use must have sufficient permissions to make necessary AWS service calls and manage AWS resources.
* [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html) v2 installed and configured (commands written against 2.31.3)
* [Git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git) installed
* [Node.js 22 or later](https://nodejs.org/en/download/) installed
* [AWS CDK v2](https://docs.aws.amazon.com/cdk/v2/guide/getting_started.html) bootstrapped in the target account and Region (`npx cdk bootstrap`)

## Supported Regions

The stack takes the Region from your AWS CLI configuration or environment and has no Region-specific ARNs. It was tested in us-west-2 and eu-central-1. Another Region needs Amazon EventBridge archive and replay, AWS Step Functions JSONata and Amazon CloudWatch alarm state change events.

## Architecture

```
PutEvents --> custom bus --> archive (all demo.orders events)
                 |
                 +--> OrdersRule --> Amazon SQS queue (no queue policy: delivery fails, 0 retries, no DLQ)
                          |
                          +--> FailedInvocations --> CloudWatch alarm --- ALARM to OK (default bus event) ---+
                                                                                                            v
Amazon SNS <-- DescribeReplay poll <-- StartReplay (FilterArns = OrdersRule) <-- wait 10 min <-- DescribeAlarmHistory
                                          (AWS Step Functions, SDK integrations only)
replayed events (carry replay-name, not archived again) --> OrdersRule --> queue (policy fixed)
```

## How it works

1. Events with source `demo.orders` sent to the custom bus are copied to an archive with one day of retention.
2. `OrdersRule` sends each event to the queue. The stack creates no queue policy that allows `events.amazonaws.com` (and sets no `enforceSSL`, which would add one), and the target has `MaximumRetryAttempts` 0, a 60 second `MaximumEventAgeInSeconds` and no dead-letter queue. Every delivery fails and the events never reach the queue, but they stay in the archive.
3. The alarm sums `FailedInvocations` (namespace `AWS/Events`, dimensions `EventBusName` and `RuleName`) over 60 seconds and goes to ALARM at 1 or more. Missing data counts as not breaching.
4. After the queue policy is fixed and the failures stop, the alarm returns to OK. A rule on the default bus matches only `previousState` ALARM and `state` OK for this alarm and starts the state machine, so INSUFFICIENT_DATA to OK is ignored. The rule has a dead-letter queue and 3 retries.
5. The state machine reads the alarm history (`cloudwatch:DescribeAlarmHistory`) and takes the newest transition into ALARM at or before the OK event as the outage start, because the OK event does not carry it. If none is found, it publishes that and ends in a Fail state.
6. It waits 10 minutes, the delay the EventBridge documentation recommends before a replay. It then calls `eventbridge:StartReplay` from 5 minutes before the outage start to 2 minutes after the OK event, with `Destination.FilterArns` set to `OrdersRule` only. The replay name is `sfn-replay-` plus the outage start in epoch seconds, so a second execution for the same outage gets `ResourceAlreadyExistsException` and ends without a second replay.
7. It polls `eventbridge:DescribeReplay` every 30 seconds, at most 60 times, until the state is not STARTING, RUNNING or CANCELLING. Task errors go to the same result step.
8. It publishes the replay state and window to the Amazon SNS topic. Apart from the duplicate-run path in step 6, which succeeds without publishing, the execution succeeds only when the replay state is COMPLETED.

Without the state machine the archive is passive: replay has no CloudFormation resource, and nothing in EventBridge starts one when a target recovers.

### How is this different from a dead-letter queue and retry policy?

EventBridge retries a failed delivery for up to 24 hours by default, and a dead-letter queue keeps events that exhausted their retries. Use those first. This pattern is for events that were dropped or exhausted their retries, or for a target repaired after its events aged out, when you want to re-deliver a time window from a durable archive to one rule. The nearest existing pattern, `eventbridge-sfn-redrive`, redrives failed AWS Step Functions executions; it does not replay events.

## Important Notes

* Replayed events carry a `replay-name` field, and a managed rule on the archive's source bus keeps them out of the archive. The next window starts from the next ALARM transition, so a replay does not start another one unless the target is still broken (next note).
* The workflow does not check target health. ALARM to OK also follows a quiet period. If the target is still broken when the replay runs, the replay still reports COMPLETED, the deliveries fail again, and the alarm returns to ALARM for a window that no longer covers the original events. Fix the target first, or start a manual replay.
* The window starts 5 minutes before the alarm entered ALARM, so failures that began earlier are not replayed; widen `LOOKBACK_MS` in the stack or start a replay by hand.
* Events sent inside the 5 minute and 2 minute margins can be delivered twice, and so can events in overlapping windows if the alarm flaps within one outage (not tested), so a real target must tolerate duplicates.
* `FailedInvocations` is sparse, so the alarm can take several minutes to return to OK. Wait for OK before repeating a test.
* `Resource: *` appears only for the Amazon CloudWatch Logs delivery actions that AWS Step Functions logging needs. The replay, alarm history and publish actions are scoped to the archive, bus, replay name prefix, alarm and topic.
* Archive processing, storage and replay, one CloudWatch alarm and AWS Step Functions state transitions are billed; see the pricing pages. EventBridge deletes replays after 90 days.

## Deployment Instructions

1. Clone the repository:
    ```bash
    git clone https://github.com/aws-samples/serverless-patterns
    cd serverless-patterns/eventbridge-archive-replay-sfn/typescript/cdk
    ```

2. Install dependencies and build:
    ```bash
    npm install
    npm run build
    ```

3. Bootstrap the account and Region once, then deploy:
    ```bash
    npx cdk bootstrap
    npx cdk deploy
    ```

4. Read the stack outputs that the Testing section uses:
    ```bash
    STACK=EventbridgeArchiveReplaySfnStack
    out() { aws cloudformation describe-stacks --stack-name "$STACK" --query "Stacks[0].Outputs[?OutputKey=='$1'].OutputValue" --output text; }
    BUS=$(out EventBusName); ARCHIVE=$(out ArchiveName); QUEUE_URL=$(out QueueUrl); QUEUE_ARN=$(out QueueArn)
    RULE_ARN=$(out OrdersRuleArn); ALARM=$(out AlarmName); SM=$(out StateMachineArn); TOPIC=$(out ResultTopicArn)
    ```

## Testing

In a new terminal, run Deployment step 4 again first. Replace `you@example.com` with your address. In the tests the alarm reached ALARM within 2 minutes of the events and returned to OK about 6 minutes later, and the workflow finished about 11 minutes after OK (it waits 10 minutes), so allow about 20 minutes.

**1. Subscribe to the result topic** (confirm the email you receive):

```bash
aws sns subscribe --topic-arn "$TOPIC" --protocol email --notification-endpoint you@example.com
```

**2. Send three events while the target cannot receive them.** Expected: `0` three times, then `None` from the queue.

```bash
for i in 1 2 3; do
  aws events put-events --query FailedEntryCount --entries "[{\"EventBusName\":\"$BUS\",\"Source\":\"demo.orders\",\"DetailType\":\"OrderPlaced\",\"Detail\":\"{\\\"seq\\\":$i}\"}]"
done
aws sqs receive-message --queue-url "$QUEUE_URL" --wait-time-seconds 10 --query 'Messages[].Body' --output text
```

**3. Wait for ALARM** (can take several minutes; repeat until it prints `ALARM`):

```bash
aws cloudwatch describe-alarms --alarm-names "$ALARM" --query 'MetricAlarms[0].StateValue' --output text
```

**4. Fix the target** by allowing the rule to send to the queue (this replaces the queue policy):

```bash
cat > /tmp/queue-policy-attributes.json <<EOF
{"Policy": "{\"Version\":\"2012-10-17\",\"Statement\":[{\"Effect\":\"Allow\",\"Principal\":{\"Service\":\"events.amazonaws.com\"},\"Action\":\"sqs:SendMessage\",\"Resource\":\"$QUEUE_ARN\",\"Condition\":{\"ArnEquals\":{\"aws:SourceArn\":\"$RULE_ARN\"}}}]}"}
EOF
aws sqs set-queue-attributes --queue-url "$QUEUE_URL" --attributes file:///tmp/queue-policy-attributes.json
```

**5. Wait for OK** (several minutes without new failures), then list the execution it started. It waits 10 minutes before `StartReplay`; do not send more events to the bus meanwhile.

```bash
aws cloudwatch describe-alarms --alarm-names "$ALARM" --query 'MetricAlarms[0].StateValue' --output text
aws stepfunctions list-executions --state-machine-arn "$SM" --max-results 5 --query 'executions[].[name,status]' --output text
```

**6. When the execution is no longer RUNNING**, read its output and the replay. Expected: status `SUCCEEDED` with an output like `{"replayName":"sfn-replay-...","replayState":"COMPLETED","messageId":"..."}`, then a replay `COMPLETED` whose window starts 5 minutes before the alarm entered ALARM and ends 2 minutes after the OK, with the `OrdersRule` ARN as the filter. The Amazon SNS message carries the same result (the tests read it through a queue subscription instead of email).

```bash
EXEC=$(aws stepfunctions list-executions --state-machine-arn "$SM" --max-results 1 --query 'executions[0].executionArn' --output text)
aws stepfunctions describe-execution --execution-arn "$EXEC" --query '[status,output]' --output text
REPLAY=$(aws stepfunctions describe-execution --execution-arn "$EXEC" --query output --output text | sed -E 's/.*"replayName":"([^"]+)".*/\1/')
aws events describe-replay --replay-name "$REPLAY" --query '[State,EventStartTime,EventEndTime,Destination.FilterArns[0]]' --output text
```

**7. Read the queue.** Expected: bodies for `seq` 1, 2 and 3, each with `"replay-name":"sfn-replay-..."`, although the queue was empty before the replay. One call can return fewer than three messages, and the messages it returns stay hidden for 30 seconds, so the loop reads three times. If fewer than three bodies appear, run it again.

```bash
for i in 1 2 3; do
  aws sqs receive-message --queue-url "$QUEUE_URL" --max-number-of-messages 10 --wait-time-seconds 10 --query 'Messages[].Body' --output text | tr '\t' '\n'
done
```

Workflow errors are logged to the log group named in the `StateMachineLogGroupName` output.

## Cleanup

1. Delete the stack (in a new terminal, run Deployment step 4 first: step 2 needs its variables, and the stack outputs are gone after the destroy). This also deletes the custom bus, the archive with every event in it, the queue with its messages, the topic and its subscription, and the log group. If an execution is still in its 10 minute wait, the state machine finishes deleting at that execution's next state transition:
    ```bash
    npx cdk destroy
    ```
    Answer `y` at the prompt, or add `--force`.

2. Remove the local policy file and confirm the stack, the archive and the bus are gone. Expected: each command reports that the resource does not exist. Replays are not stack resources and EventBridge deletes them after 90 days.
    ```bash
    rm -f /tmp/queue-policy-attributes.json
    aws cloudformation describe-stacks --stack-name "$STACK"
    aws events describe-archive --archive-name "$ARCHIVE"
    aws events describe-event-bus --name "$BUS"
    ```

----
Copyright 2026 Amazon.com, Inc. or its affiliates. All Rights Reserved.

SPDX-License-Identifier: MIT-0
