# Check IAM role policy changes with AWS IAM Access Analyzer and AWS Step Functions

This pattern checks the inline policy that is written to an IAM role the moment it is written. An Amazon EventBridge rule matches the IAM `PutRolePolicy` call and starts an AWS Step Functions workflow. The workflow sends the policy document from the event to the AWS IAM Access Analyzer `CheckAccessNotGranted` API through an AWS SDK service integration and publishes an Amazon SNS notification when the policy might allow any of a list of actions. The pattern only notifies by default. Removing the inline policy is an opt-in setting.

Learn more about this pattern at Serverless Land Patterns: https://serverlessland.com/patterns/accessanalyzer-sfn-typescript-cdk

Important: this application uses various AWS services and there are costs associated with these services after the Free Tier usage - please see the [AWS Pricing page](https://aws.amazon.com/pricing/) for details. You are responsible for any AWS costs incurred. No warranty is implied in this example.

## Requirements

* [Create an AWS account](https://portal.aws.amazon.com/gp/aws/developer/registration/index.html) if you do not already have one and log in. The IAM user that you use must have sufficient permissions to make necessary AWS service calls and manage AWS resources.
* [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html) installed and configured
* [Git Installed](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)
* [Node.js 22 or later](https://nodejs.org/en/download/) installed
* [AWS Cloud Development Kit](https://docs.aws.amazon.com/cdk/v2/guide/getting_started.html) (AWS CDK) v2 installed
* An AWS CloudTrail trail that logs management events. The EventBridge documentation states that events with the `AWS API Call via CloudTrail` detail type require a trail with logging enabled ([AWS service events delivered via AWS CloudTrail](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-service-event-cloudtrail.html)). This pattern does not create a trail. Check whether your account already has one before you create another.
* A sandbox account. The workflow reads every matching policy change in the account, and the optional removal step deletes IAM policies.

## Supported Regions

Deploy this stack in us-east-1 (US East (N. Virginia)). IAM is a global service, and CloudTrail records its events in us-east-1 ([CloudTrail global service events](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-concepts.html#cloudtrail-concepts-global-service-events)). EventBridge also states that events from API calls to global services such as IAM are only available in that Region ([troubleshooting](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-troubleshooting.html#eb-rule-did-not-trigger-iam)). A rule in another Region would never match, so the stack stops with an error when the Region is not us-east-1. The stack builds its ARNs with the partition of the deployment, but it was only designed for the standard `aws` partition in us-east-1.

## Architecture

```
IAM PutRolePolicy on a role named <prefix>*
        |  recorded by CloudTrail, delivered to the default event bus in us-east-1
        v
Amazon EventBridge rule  ---- failed deliveries ----> Amazon SQS dead-letter queue
        v
AWS Step Functions (Standard)
  HasPolicyDocument            Choice: policyDocument present and a string
  CheckAccessNotGranted        access-analyzer:CheckAccessNotGranted (SDK integration)
  EvaluateResult               Choice: PASS | FAIL | anything else
     PASS  -> PolicyCompliant  (end)
     FAIL  -> NotifyViolation  (Amazon SNS), or with enableRemediation:
              RoleInPrefixScope -> RemoveInlinePolicy -> NotifyRemoved
     other -> MarkNotEvaluated -> NotifyNotEvaluated -> PolicyNotEvaluated (Fail)
  API error (Catch)  ->  NotifyNotEvaluated -> PolicyNotEvaluated (Fail)
  RemoveInlinePolicy error (Catch)  ->  NotifyRemovalFailed -> RemovalFailed (Fail)
```

## How it works

1. A `PutRolePolicy` call on an IAM role whose name starts with the configured prefix is recorded by AWS CloudTrail and delivered to the default event bus in us-east-1.
2. An Amazon EventBridge rule starts an AWS Step Functions Standard workflow. Failed deliveries go to an Amazon SQS dead-letter queue.
3. The workflow passes the policy document from the event to the IAM Access Analyzer `CheckAccessNotGranted` API through an AWS SDK service integration (no AWS Lambda function, no `GetRolePolicy`).
4. `PASS` ends the workflow. `FAIL`, or a policy that cannot be checked, is published to Amazon SNS. With `enableRemediation=true`, a failing inline policy on a role inside the prefix is also deleted.

## Important Notes

* **The decision comes from IAM Access Analyzer.** The `PolicyDocument` parameter of `CheckAccessNotGranted` is the string at `$.detail.requestParameters.policyDocument` of the CloudTrail event. The workflow does not call `GetRolePolicy` and has no AWS Lambda function. The synthesized template contains no Lambda function. The access object is an explicit list of 11 actions in `lib/accessanalyzer-sfn-stack.ts`, such as `iam:CreateAccessKey`, `iam:PassRole` and `iam:PutRolePolicy`. The API documentation describes a `FAIL` result as the policy "might allow some or all" of the actions, so the check errs toward reporting. The API accepts at most one access object. Edit the list for your own standards.
* **Policies that cannot be checked are reported.** A `Choice` state tests that the policy document is present and is a string before the API call, so a missing field cannot cause a `States.Runtime` error, which a `States.ALL` catch does not handle. If the Access Analyzer call fails, or it returns neither `PASS` nor `FAIL`, the execution sends a `POLICY_NOT_EVALUATED` notification and ends in a `Fail` state with an error and a cause. When the API call failed, the notification carries the error name and cause that Step Functions caught from the API. In the other cases it carries a fixed `PolicyNotEvaluated` cause. Validation errors from the API are not retried. Throttling and server errors are retried three times.
* **Notify-only is the default.** With `enableRemediation=false` the state machine contains no IAM state and its role has no IAM permission. With `enableRemediation=true` the role gets `iam:DeleteRolePolicy` on `role/<prefix>*` in this account only, the rule only matches that prefix, and a `Choice` state checks the prefix again before the delete.
* **Removal is not a rollback.** `PutRolePolicy` adds or updates an inline policy by name. The event carries only the new document, so the workflow cannot restore an earlier policy. If the call overwrote a policy with the same name, removal deletes that policy and the role loses its access.
* **Scope and self-triggering.** CloudFormation and the AWS CDK also write inline policies with `PutRolePolicy`, including the policy of this stack's own state machine role. The roles of this stack get names that AWS CloudFormation builds from the stack name, which do not match the default prefix. Keep the prefix specific to your test roles so that no other role is matched.
* **Successful calls only.** The rule requires that the `errorCode` field is absent.
* **Role name case.** IAM documents that role names are not distinguished by case. The rule uses the `equals-ignore-case` form of prefix matching, so a call that writes the name in another case, such as `GUARDRAIL-DEMO-test`, still starts the workflow. The removal branch compares the role name with the prefix case sensitively and the `iam:DeleteRolePolicy` resource ARN is written with the prefix as configured, so in removal mode a differently cased name is expected to end in a notification with `policyRemoved` set to `false` and the policy stays. In a test against a live account, `put-role-policy` on the role `guardrail-demo-test` with `--role-name GUARDRAIL-DEMO-test` started the workflow and it ended in `NotifyViolation`; the removal branch for such a name was not tested. Use a lower-case prefix and lower-case role names.
* **Trust policies.** The state machine role and the rule role trust their service principal only with `aws:SourceAccount` and `aws:SourceArn` conditions. The state machine and the rule get names built from the stack name (`AccessAnalyzerSfnStack-policy-guardrail`) so that the ARNs are known before the resources exist. A second copy of the stack in the same account and Region needs a different stack name in `bin/app.ts`.
* **Roles with a path.** The delete permission is written for `role/<prefix>*`. The ARN of a role that was created with a path, such as `/team/guardrail-demo-x`, contains the path, so that permission does not cover it. In removal mode such a role is expected to end in `NotifyRemovalFailed` and `RemovalFailed`, and its policy stays. This was not tested. Keep the test roles at the root path.
* **Wildcards.** The `access-analyzer:CheckAccessNotGranted` statement uses `Resource: *`, as the AWS managed policy `IAMAccessAnalyzerReadOnlyAccess` does (it allows `access-analyzer:CheckAccessNotGranted` on `*`), because the request names no resource. The log delivery actions that Step Functions needs for logging also use `Resource: *`. The delete statement ends in `*` after the role-name prefix.
* **Encryption and cleanup.** The Amazon SNS topic uses the AWS managed key and denies requests without TLS. The dead-letter queue uses SQS-managed encryption and denies requests without TLS. The log group keeps logs for one week. Nothing is retained on `cdk destroy`.
* **Logs.** Step Functions writes execution logs at level `ALL` without execution data to the log group in the `LogGroupName` output. The input and output of every state are in the execution history in the Step Functions console and API.

### How this differs from other approaches

* **AWS Security Hub and Amazon GuardDuty remediation patterns** react to a finding that a detector has already produced and remediate with a Lambda function. Here no detector is involved. The policy text in the CloudTrail event is checked with an Access Analyzer API at the time of the change, and the Step Functions Choice state acts on the `PASS` or `FAIL` result.
* **AWS Config rules** evaluate the configuration of resources that AWS Config records. This pattern needs no Config recorder. It evaluates the policy text of each change against a list of actions that you choose.
* **IAM Access Analyzer custom policy checks in a pipeline** run before deployment. See [iam-access-analyzer-custom-policy-check-samples](https://github.com/aws-samples/iam-access-analyzer-custom-policy-check-samples). This pattern is the runtime variant that reacts to a change that has already happened. [go-security-toolbox-v2](https://github.com/aws-samples/go-security-toolbox-v2) scans policies on a schedule.
* **This pattern is detective and corrective, not preventive.** The policy is in effect until the event is delivered and the workflow has finished. To prevent a change, use service control policies or permissions boundaries.

### What is not covered

Only `PutRolePolicy` on roles with the prefix is matched. These calls are not: `AttachRolePolicy` (including an AWS managed policy such as `AdministratorAccess`), `CreatePolicyVersion` and `SetDefaultPolicyVersion` for customer managed policies, `PutUserPolicy`, `PutGroupPolicy`, and `UpdateAssumeRolePolicy`. `CheckNoNewAccess` is not used because it needs the existing policy document, which the event does not contain.

### Cost

No resource in this stack bills by the hour. The documented custom policy check price is based on the number of API calls, and the [pricing page](https://aws.amazon.com/iam/access-analyzer/pricing/) example uses $0.0020 per call. Confirm the current price there. One matching policy change makes one check. Step Functions Standard workflows are billed per state transition, and Amazon SNS, Amazon SQS, Amazon EventBridge and Amazon CloudWatch Logs are billed by use. A CloudTrail trail is a separate resource with its own charges.

## Deployment Instructions

1. Clone the repository:
    ```bash
    git clone https://github.com/aws-samples/serverless-patterns
    cd serverless-patterns/accessanalyzer-sfn/typescript/cdk
    ```
2. Install the dependencies:
    ```
    npm install
    ```
3. Use us-east-1 for the AWS CDK commands:
    ```
    export AWS_REGION=us-east-1
    ```
4. If this account and Region have never been used with the AWS CDK, bootstrap them once. The stack needs the bootstrap resources:
    ```
    npx cdk bootstrap
    ```
5. Deploy the stack. It runs in notify-only mode:
    ```
    npx cdk deploy
    ```
6. Note the stack outputs: `StateMachineArn`, `TopicArn`, `LogGroupName`, `RoleNamePrefix` and `Mode`.

Settings are AWS CDK context values, set with `-c name=value` on `cdk deploy` or in `cdk.json`:

| Context value | Default | Meaning |
| --- | --- | --- |
| `roleNamePrefix` | `guardrail-demo-` | Only roles whose name starts with this prefix are checked. The rule matches the prefix regardless of case, because IAM role names are not distinguished by case. The `Choice` state that guards removal compares case sensitively. It must be 4 to 40 IAM role name characters and cannot contain a wildcard. |
| `enableRemediation` | `false` | When `true`, a policy that fails the check is deleted with `iam:DeleteRolePolicy`. Only the exact value `true` turns it on; anything else means notify-only, and the `Mode` output shows which mode is deployed. |

## Testing

Run the commands from the pattern directory. The test files are in the `test` folder. The role name must start with the prefix, `guardrail-demo-` by default. Every command targets `us-east-1` explicitly with `--region`, so the steps also work in a new terminal after you read the stack outputs again:

```
out() { aws cloudformation describe-stacks --region us-east-1 --stack-name AccessAnalyzerSfnStack --query "Stacks[0].Outputs[?OutputKey=='$1'].OutputValue" --output text; }
SM=$(out StateMachineArn); TOPIC=$(out TopicArn)
```

1. Subscribe an email address to the topic and confirm the subscription from the email that Amazon SNS sends:
    ```
    aws sns subscribe --region us-east-1 --topic-arn $TOPIC --protocol email --notification-endpoint you@example.com
    ```
1. Create the test role. `CreateRole` does not start the workflow:
    ```
    aws iam create-role --role-name guardrail-demo-test --assume-role-policy-document file://test/trust-policy.json
    ```
1. Write the compliant policy:
    ```
    aws iam put-role-policy --role-name guardrail-demo-test --policy-name compliant --policy-document file://test/compliant-policy.json
    ```
1. Wait for CloudTrail and EventBridge to deliver the event. In test runs the execution started 3 to 6 seconds after the call, in an account that already had CloudTrail trails, and delivery times can vary, so poll until an execution appears. List the executions and show the states of the latest one (this is the check that the later steps call "the check commands"):
    ```
    aws stepfunctions list-executions --region us-east-1 --state-machine-arn $SM --query 'executions[].[name,status,startDate]' --output table
    EXEC=$(aws stepfunctions list-executions --region us-east-1 --state-machine-arn $SM --query 'executions[0].executionArn' --output text)
    aws stepfunctions get-execution-history --region us-east-1 --execution-arn $EXEC --query 'events[?contains(type, `StateEntered`)].stateEnteredEventDetails.name' --output text
    ```
    Expected: one execution with status `SUCCEEDED` and the states `HasPolicyDocument`, `CheckAccessNotGranted`, `EvaluateResult` and `PolicyCompliant`. No email is sent.
1. Write the blocked policy, which allows `iam:CreateAccessKey`:
    ```
    aws iam put-role-policy --role-name guardrail-demo-test --policy-name blocked --policy-document file://test/blocked-policy.json
    ```
1. Wait for the event to be delivered, then run the check commands from step 4 again. Expected: the newest execution has status `SUCCEEDED` and ends with `EvaluateResult` and `NotifyViolation`, and you receive an email. The email message contains `"status": "POLICY_FAILS_CHECK"`, `"policyRemoved": false`, the role name, the policy name, the CloudTrail event ID and the Access Analyzer result.
1. Confirm that notify-only mode left the policy in place:
    ```
    aws iam list-role-policies --role-name guardrail-demo-test
    ```
    Expected: both `compliant` and `blocked` are listed.
1. Outside the prefix: create a role named `other-demo-test` and write `test/blocked-policy.json` to it:
    ```
    aws iam create-role --role-name other-demo-test --assume-role-policy-document file://test/trust-policy.json
    aws iam put-role-policy --role-name other-demo-test --policy-name blocked --policy-document file://test/blocked-policy.json
    ```
    Expected: no new execution, because the rule does not match. Wait as long as you did in step 4 before you conclude that nothing started, because "no execution" looks the same as "not delivered yet".
1. A policy document that cannot be checked. Start an execution by hand with a document that is not valid JSON:
    ```
    EXEC=$(aws stepfunctions start-execution --region us-east-1 --state-machine-arn $SM --query executionArn --output text --input '{"detail":{"eventID":"manual-1","requestParameters":{"roleName":"guardrail-demo-test","policyName":"x","policyDocument":"not json"}}}')
    sleep 10
    aws stepfunctions describe-execution --region us-east-1 --execution-arn $EXEC --query '{status:status,error:error}'
    aws stepfunctions get-execution-history --region us-east-1 --execution-arn $EXEC --query 'events[?contains(type, `StateEntered`)].stateEnteredEventDetails.name' --output text
    aws stepfunctions get-execution-history --region us-east-1 --execution-arn $EXEC --query "events[?type=='TaskFailed'].taskFailedEventDetails.[error,cause]" --output text
    ```
    Expected: the execution has status `FAILED` with the error `PolicyNotEvaluated`, and the states are `HasPolicyDocument`, `CheckAccessNotGranted`, `NotifyNotEvaluated` and `PolicyNotEvaluated`. The last command prints the failed `CheckAccessNotGranted` task: the error `AccessAnalyzer.ValidationException` and the cause `The policy in policyDocument is invalid.` It fails on the first attempt, because validation errors are not retried.
1. Optional, to test removal: redeploy with `npx cdk deploy -c enableRemediation=true`, write the blocked policy again as in step 5, then wait and run the check commands from step 4 again. Expected: the states `RoleInPrefixScope`, `RemoveInlinePolicy` and `NotifyRemoved`, an email with `"status": "POLICY_REMOVED"`, and `aws iam list-role-policies` no longer lists `blocked`. Redeploy without the flag to return to notify-only mode.

If an execution fails, the `PolicyNotEvaluated` or `RemovalFailed` Fail state carries an error and a cause. For a failed Access Analyzer call, the `POLICY_NOT_EVALUATED` email contains the error name and cause returned by the API. For a missing field or an unexpected result, it contains the fixed `PolicyNotEvaluated` text. Failed deliveries from EventBridge to the state machine are stored in the dead-letter queue.

## Cleanup

1. Delete the test policies and the test roles:
    ```
    aws iam delete-role-policy --role-name guardrail-demo-test --policy-name compliant
    aws iam delete-role-policy --role-name guardrail-demo-test --policy-name blocked
    aws iam delete-role --role-name guardrail-demo-test
    aws iam delete-role-policy --role-name other-demo-test --policy-name blocked
    aws iam delete-role --role-name other-demo-test
    ```
    A command for a policy that no longer exists returns an error. That is expected after removal mode.
1. Delete the stack. The log group and the other resources are removed with it:
    ```
    npx cdk destroy
    ```
1. Confirm that the stack has been deleted:
    ```
    aws cloudformation describe-stacks --region us-east-1 --stack-name AccessAnalyzerSfnStack
    ```
    Expected: an error that the stack does not exist.

----
Copyright 2026 Amazon.com, Inc. or its affiliates. All Rights Reserved.

SPDX-License-Identifier: MIT-0
