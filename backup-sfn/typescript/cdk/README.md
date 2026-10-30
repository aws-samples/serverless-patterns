# AWS Backup restore testing validated by AWS Step Functions

This pattern deploys an AWS Backup restore testing plan for an Amazon DynamoDB table and an AWS Step Functions workflow that validates each restored copy. When a restore test job completes, Amazon EventBridge starts the workflow. The workflow counts the items in the restored table and writes a `SUCCESSFUL` or `FAILED` validation result back to AWS Backup with the `PutRestoreValidationResult` API, so the result appears on the restore job.

Learn more about this pattern at Serverless Land Patterns: https://serverlessland.com/patterns/backup-sfn-typescript-cdk

Important: this application uses various AWS services and there are costs associated with these services after the Free Tier usage - please see the [AWS Pricing page](https://aws.amazon.com/pricing/) for details. You are responsible for any AWS costs incurred. No warranty is implied in this example.

## Requirements

* [Create an AWS account](https://portal.aws.amazon.com/gp/aws/developer/registration/index.html) if you do not already have one and log in. The IAM user that you use must have sufficient permissions to make necessary AWS service calls and manage AWS resources. Creating the restore testing plan also creates the service-linked role `AWSServiceRoleForBackupRestoreTesting` if it does not exist, so the deploying identity needs `iam:CreateServiceLinkedRole`.
* [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html) installed and configured
* [Git Installed](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)
* [Node.js](https://nodejs.org/en/download/) 22 or later and npm installed
* [AWS Cloud Development Kit](https://docs.aws.amazon.com/cdk/v2/guide/getting-started.html) (AWS CDK) installed, and the target account and Region [bootstrapped](https://docs.aws.amazon.com/cdk/v2/guide/bootstrapping.html) (`npx cdk bootstrap` once per account and Region)

## Supported Regions

The stack contains no Region-specific values or hardcoded account IDs, and its ARNs use the partition, Region and account of the stack. It was tested in us-west-2. Deploy it to a Region where AWS Backup restore testing, Amazon DynamoDB and AWS Step Functions are available (see the [AWS Backup feature availability](https://docs.aws.amazon.com/aws-backup/latest/devguide/backup-feature-availability.html) page).

## Architecture

```
AWS Backup restore testing plan (runs on a schedule)
   |  restores the latest recovery point of the Amazon DynamoDB table
   v
Restore job COMPLETED ---- "Restore Job State Change" event ----> Amazon EventBridge rule
                                                                        |
                                                                        v
                                                       AWS Step Functions workflow (no AWS Lambda function)
                                                          1. dynamodb:Scan on the restored table (Select COUNT, Limit 3)
                                                          2. backup:PutRestoreValidationResult: SUCCESSFUL or FAILED
                                                                        |
                                                                        v
                                      the validation result shows up on the restore job in AWS Backup
```

## How it works

The stack creates the following resources:

* **Amazon DynamoDB**: a small on-demand table (`pk` partition key) that is the protected resource.
* **AWS Backup**: a backup vault, an IAM role for backup jobs, an IAM role for restores (each with the matching AWS managed policy), a restore testing plan and a restore testing selection that picks the DynamoDB table. The plan restores the latest snapshot recovery point in the vault from the last day. The selection keeps the restored table for 2 hours (`ValidationWindowHours`) so that the workflow can read it. The plan name is built from the stack name (`BackupSfnRestoreValidationStack_restore_test`) and must be unique in an account and Region, so a second copy of this stack in the same account and Region needs a different stack name in `bin/app.ts`. The selection is named `source_table`. The window for eligible recovery points (`selectionWindowDays`) is 1 day, which suits the one-off backup in Testing. With a real backup plan, set it to more than the backup interval plus the start window, as the [AWS Backup documentation](https://docs.aws.amazon.com/aws-backup/latest/devguide/restore-testing.html) recommends. Restore testing in the AWS CDK is available only as L1 constructs (`CfnRestoreTestingPlan` and `CfnRestoreTestingSelection`).
* **Amazon EventBridge**: a rule for `Restore Job State Change` events from `aws.backup` with status `COMPLETED`, a resource type that starts with `DynamoDB` and this plan's ARN. AWS Backup reports the resource type of a DynamoDB restore job as `DynamoDB.FullyManaged` in this event, not as `DynamoDB`, so a rule that matches `DynamoDB` exactly never fires. The target is the state machine, with retries and an encrypted Amazon SQS dead-letter queue for events that cannot be delivered.
* **AWS Step Functions**: a Standard state machine with execution logging to an Amazon CloudWatch Logs log group (1 week retention).

The workflow:

1. A `Choice` state checks that the event has `detail.restoreJobId`. Without it no result can be recorded, so the execution ends in a `Fail` state (`InvalidEvent`).
1. A second `Choice` state checks that `detail.createdResourceArn` is a DynamoDB table ARN. If not, the verdict is `FAILED`.
1. A `Pass` state takes the table name from the end of `createdResourceArn`.
1. `CountRestoredItems` calls `dynamodb:Scan` with `Select` set to `COUNT` and `Limit` set to 3, so it reads at most 3 items. It uses a consistent read. `DescribeTable` is not used because its `ItemCount` is refreshed only about every six hours, which is too slow for a table that was just restored.
1. A `Choice` state compares `Count` with 3. At least 3 items gives `SUCCESSFUL`, otherwise `FAILED`. If the scan itself fails (for example the table cannot be read), the verdict is `FAILED` with the error name in the message.
1. One of four task states calls `backup:PutRestoreValidationResult`. **An execution writes at most one result**: the [documentation](https://docs.aws.amazon.com/aws-backup/latest/devguide/restore-testing-validation.html) says that once a validation status is set it cannot be changed, so there is no `VALIDATING` write first and no branch that writes twice. If the write itself fails, the execution ends in a `Fail` state (`ValidationNotRecorded`) and does not try another write. EventBridge delivers events at least once, so a duplicate event would start a second execution that tries to write again. Because a status cannot be changed once set, treat a `ValidationNotRecorded` execution for a restore job that already has a result as expected.
1. When a verdict (success or failure) has been recorded, the execution ends in `Succeed`. An execution in `FAILED` status therefore means "no verdict could be recorded", which is the status to alarm on.

Retries are limited to transient errors: `Backup.ServiceUnavailableException` for the `PutRestoreValidationResult` call, and throttling, request limit and internal server errors for the DynamoDB `Scan`. Permanent errors, such as an unknown restore job or a missing table, have a retry entry with zero attempts ahead of the transient entry and go straight to the next step.

The fields that the workflow and the rule use in the `Restore Job State Change` event (`detail.status`, `detail.resourceType`, `detail.restoreTestingPlanArn`, `detail.restoreJobId` and `detail.createdResourceArn`) were checked against the events of a real restore test job. In the events captured in testing, these fields were present from the `PENDING` state on, except `createdResourceArn` (and `completionDate`), which first appear with `COMPLETED`.

The item count check is deliberately simple. It shows the wiring; replace it with your own checks (for example a read of a known key). A count over a table larger than one Scan page is only a lower bound, which is enough for a minimum-size check.

## Why this pattern

AWS Backup restore testing restores a recovery point on a schedule and deletes the restored resource afterwards. Validating the restored data is optional and is something you supply: the [documentation](https://docs.aws.amazon.com/aws-backup/latest/devguide/restore-testing.html) says that validation can be run programmatically but not from the AWS Backup console. The [validation example in the AWS Backup documentation](https://docs.aws.amazon.com/aws-backup/latest/devguide/restore-testing-validation.html) uses an AWS Lambda function and notes that `PutRestoreValidationResult` is not available through the Lambda SDK, so a Lambda layer with a newer SDK is needed.

This pattern takes a different route. The workflow calls Amazon DynamoDB and AWS Backup directly through [AWS SDK service integrations](https://docs.aws.amazon.com/step-functions/latest/dg/supported-services-awssdk.html), so the synthesized template contains no Lambda function and no custom resources. The check (the item count of the restored table) decides the verdict that is written back to the originating service.

The closest pattern in this repository is [securityhub-finding-sfn-remediation-cdk](../../../securityhub-finding-sfn-remediation-cdk), which also starts a Step Functions workflow from an EventBridge event but remediates AWS Security Hub findings with AWS Lambda functions. This pattern reports a validation verdict to AWS Backup and has no Lambda function.

## Important Notes

### IAM

* The state machine role can call `dynamodb:Scan` only on tables whose names start with `awsbackup-restore-test-`, the name prefix that AWS Backup [infers for restored DynamoDB tables](https://docs.aws.amazon.com/aws-backup/latest/devguide/restore-testing-inferred-metadata.html). Its trust policy has `aws:SourceAccount` and `aws:SourceArn` conditions.
* `backup:PutRestoreValidationResult` is allowed on `*`, because the action has no resource types in the [IAM service reference](https://servicereference.us-east-1.amazonaws.com/v1/backup/backup.json). The statement on `*` with CloudWatch Logs delivery actions is added by the AWS CDK for the state machine log group.
* The roles for AWS Backup use the standard trust policy for `backup.amazonaws.com`. The AWS Backup documentation does not describe source condition keys for these role trust policies, so none are added.
* Nothing in the stack is reachable from outside the account: there is no API, listener or public resource. Inside the account, any principal that may call `states:StartExecution` on the state machine can start an execution with an arbitrary `restoreJobId`, and the workflow will try to write a verdict for that restore job, because `backup:PutRestoreValidationResult` cannot be limited to a resource. Restrict who can start the state machine accordingly.
* The rule matches `COMPLETED` only, so a restore job that ends in another state (for example `FAILED`) does not start the workflow and gets no validation result.
* The state machine logs at level `ALL` with execution data, so the execution log holds the events, which contain your account ID and resource ARNs. The log group keeps them for one week.

### Cleanup behaviour and what stays behind

* All demo resources use `DESTROY` removal policies and the table has no deletion protection, so `cdk destroy` removes them, with one exception: **a backup vault that contains recovery points cannot be deleted**, so delete the recovery points first (see Cleanup).
* AWS Backup deletes the restored table by name once the validation result is set or the validation window ends. The [restore testing documentation](https://docs.aws.amazon.com/aws-backup/latest/devguide/restore-testing.html) says that restores of DynamoDB do not support tag-on-restore, so AWS Backup deletes the table by name and the table does not carry the `awsbackup-restore-test` tag.
* The service-linked role `AWSServiceRoleForBackupRestoreTesting` is not part of the stack and stays after `cdk destroy`.

### Cost

Nothing in this pattern bills by the hour. AWS Backup charges for each restore test, for backup storage and for the restored data, DynamoDB charges for the table, and Step Functions charges per state transition. See [AWS Backup pricing](https://aws.amazon.com/backup/pricing/). The restore test runs at every schedule match (daily with the cron used in Deployment Instructions) for as long as the stack exists and an eligible recovery point is in the vault. The on-demand recovery point in Testing expires after one day, so later runs have nothing to restore. Run the cleanup steps when you are done.

## Deployment Instructions

1. Clone the repository:
    ```bash
    git clone https://github.com/aws-samples/serverless-patterns
    cd serverless-patterns/backup-sfn/typescript/cdk
    ```
2. Install the dependencies:
    ```
    npm install
    ```
3. Choose when the restore test runs. A restore testing plan has no "run now" call: it runs on a cron schedule (UTC unless you set a time zone), and AWS Backup starts the restore at a random time within the plan's start window, which this stack sets to 1 hour. The command below builds a schedule 30 minutes from now. That leaves time to seed the table and take a backup first (see Testing).
    ```
    CRON=$(node -e 'const d=new Date(Date.now()+30*60000);console.log(`cron(${d.getUTCMinutes()} ${d.getUTCHours()} * * ? *)`)')
    echo $CRON
    ```
4. Deploy the stack:
    ```
    npx cdk deploy -c restoreTestCron="$CRON"
    ```
    Without `-c restoreTestCron` the plan uses `cron(0 5 ? * * *)`, which is 05:00 UTC every day.
5. Note the outputs from the deployment: the table name and ARN, the backup vault name, the ARN of the IAM role for the on-demand backup, the restore testing plan ARN, and the state machine ARN and log group name. They are used for testing.

## Testing

All commands run from the pattern directory and assume that you deployed the stack with the name `BackupSfnRestoreValidationStack` to the Region that your AWS CLI uses.

Plan for up to two hours of wall-clock time for the first real result: the 30 minutes until the cron time, then a random start of up to 1 hour inside the start window, then a restore of a tiny table (minutes), then the event, which AWS Backup emits on a best-effort basis. In two test runs the restore job started within 26 minutes after the cron time and the restore took about 5 minutes. In the second run the `COMPLETED` event reached EventBridge about 4 minutes after the job completed, and the workflow recorded the result in the same second. Steps 4 and 5 give an immediate check of the wiring while you wait.

1. Read the stack outputs into variables:
    ```bash
    out() { aws cloudformation describe-stacks --stack-name BackupSfnRestoreValidationStack --query "Stacks[0].Outputs[?OutputKey=='$1'].OutputValue" --output text; }
    TABLE=$(out TableName); TABLE_ARN=$(out TableArn); VAULT=$(out VaultName); ROLE=$(out BackupRoleArn)
    PLAN_ARN=$(out RestoreTestingPlanArn); SM=$(out StateMachineArn)
    ```
1. Put five items into the table. Expected: the count is `5`.
    ```bash
    for i in 1 2 3 4 5; do aws dynamodb put-item --table-name $TABLE --item "{\"pk\":{\"S\":\"item-$i\"}}"; done
    aws dynamodb scan --table-name $TABLE --select COUNT --consistent-read --query Count --output text
    ```
1. Take an on-demand backup (the restore test needs an existing recovery point). The identity that runs this command needs `iam:PassRole` on the backup role. The lifecycle makes AWS Backup delete the recovery point after one day. Wait for the state `COMPLETED` (about 2 to 3 minutes in tests) before the cron time passes. A restore test uses the latest recovery point that exists when its restore job starts, and the job can start at any time after the cron time:
    ```bash
    JOB=$(aws backup start-backup-job --backup-vault-name $VAULT --resource-arn $TABLE_ARN --iam-role-arn $ROLE --lifecycle DeleteAfterDays=1 --query BackupJobId --output text)
    aws backup describe-backup-job --backup-job-id $JOB --query State --output text
    ```
    If the backup finishes after the cron time, run `npx cdk deploy -c restoreTestCron="$CRON"` again with a new `CRON` value from the deployment step.
1. Check the wiring without waiting. Start the workflow with an event that has an unknown restore job and a table that does not exist. Expected: the execution ends with status `FAILED` and error `ValidationNotRecorded`, because AWS Backup rejects the made-up job ID:
    ```bash
    EX=$(aws stepfunctions start-execution --state-machine-arn $SM --query executionArn --output text \
      --input "{\"detail\":{\"restoreJobId\":\"aaaaaaaa-bbbb-cccc-dddd-eeeeeeeeeeee\",\"createdResourceArn\":\"${TABLE_ARN%/*}/awsbackup-restore-test-doesnotexist\"}}")
    sleep 45
    aws stepfunctions describe-execution --execution-arn $EX --query '{status:status,error:error}'
    aws stepfunctions get-execution-history --execution-arn $EX --query "events[?type=='TaskFailed'].taskFailedEventDetails.{resource:resource,error:error}"
    ```
    The history shows two failed tasks: the `scan` call (the table does not exist) and the `putRestoreValidationResult` call (the job does not exist). A rejection of the job ID by AWS Backup shows that the state machine reached the API with permission to call it. An `AccessDenied` error on the second call would mean the role is missing the permission.
1. Start the workflow with an event that has no restore job ID. Expected: status `FAILED` and error `InvalidEvent`:
    ```bash
    EX=$(aws stepfunctions start-execution --state-machine-arn $SM --input '{"detail":{}}' --query executionArn --output text)
    sleep 10
    aws stepfunctions describe-execution --execution-arn $EX --query '{status:status,error:error}'
    ```
1. Wait for the restore test, then list the restore jobs of the plan. Expected: no jobs until the plan starts one, then `PENDING`, `RUNNING` and `COMPLETED` (`validation` prints `None` until the workflow has written its result), and a few minutes later (about 4 minutes in test runs) a `ValidationStatus` of `SUCCESSFUL`:
    ```bash
    aws backup list-restore-jobs --by-restore-testing-plan-arn $PLAN_ARN \
      --query "RestoreJobs[].{id:RestoreJobId,status:Status,validation:ValidationStatus,table:CreatedResourceArn}"
    ```
1. Read the validation result from AWS Backup, not from the state machine. Expected: `status` is `COMPLETED`, `validation` is `SUCCESSFUL` and the message reads `Restored table awsbackup-restore-test-... holds at least 3 items.`:
    ```bash
    RJ=$(aws backup list-restore-jobs --by-restore-testing-plan-arn $PLAN_ARN --query "sort_by(RestoreJobs,&CreationDate)[-1].RestoreJobId" --output text)
    aws backup describe-restore-job --restore-job-id $RJ \
      --query '{status:Status,validation:ValidationStatus,message:ValidationStatusMessage,deletion:DeletionStatus}'
    ```
1. Check the workflow execution that recorded it. Expected: one `SUCCEEDED` execution that started in the same minute as the `COMPLETED` event, next to the two `FAILED` executions from the wiring checks in steps 4 and 5. The log group (name in the `StateMachineLogGroup` output) holds the execution events, including the `Count` that the scan returned:
    ```bash
    aws stepfunctions list-executions --state-machine-arn $SM --query "executions[].{name:name,status:status}"
    ```
1. To see a `FAILED` verdict, delete three of the five items, then repeat step 3 to take another backup and deploy again with a new `CRON` value (Deployment steps 3 and 4) so that you do not wait a day:
    ```bash
    for i in 1 2 3; do aws dynamodb delete-item --table-name $TABLE --key "{\"pk\":{\"S\":\"item-$i\"}}"; done
    ```
    When that restore test has run, repeat step 7. Expected: `ValidationStatus` is `FAILED` and the message reads `Restored table awsbackup-restore-test-... holds fewer than 3 items.`

## Cleanup

1. Read the values that the next steps use. Skip this if you are still in the shell from Testing. In a new shell, do it before `cdk destroy`, because the stack outputs are gone afterwards:
    ```bash
    out() { aws cloudformation describe-stacks --stack-name BackupSfnRestoreValidationStack --query "Stacks[0].Outputs[?OutputKey=='$1'].OutputValue" --output text; }
    VAULT=$(out VaultName); PLAN_ARN=$(out RestoreTestingPlanArn)
    ```
1. Make sure no restore job is still running, and that the restored table has been deleted by AWS Backup (`DeletionStatus` is `SUCCESSFUL` in `describe-restore-job`). The restored table is deleted once a result is recorded or after the 2-hour validation window:
    ```bash
    aws backup list-restore-jobs --by-restore-testing-plan-arn $PLAN_ARN --query "RestoreJobs[].{id:RestoreJobId,status:Status,deletion:DeletionStatus}"
    aws dynamodb list-tables --query "TableNames[?starts_with(@, 'awsbackup-restore-test-')]"
    ```
1. Delete the recovery points in the vault. The stack cannot delete a vault that still holds them. Deletion is asynchronous, so run the `list-recovery-points-by-backup-vault` command from this loop again and continue when it returns nothing:
    ```bash
    for RP in $(aws backup list-recovery-points-by-backup-vault --backup-vault-name $VAULT --query "RecoveryPoints[].RecoveryPointArn" --output text); do
      aws backup delete-recovery-point --backup-vault-name $VAULT --recovery-point-arn $RP
    done
    ```
1. Delete the stack:
    ```bash
    npx cdk destroy
    ```
1. Confirm the stack has been deleted:
    ```bash
    aws cloudformation list-stacks --query "StackSummaries[?contains(StackName,'BackupSfnRestoreValidationStack')].StackStatus"
    ```
    The output shows `DELETE_COMPLETE` for the stack.

----
Copyright 2026 Amazon.com, Inc. or its affiliates. All Rights Reserved.

SPDX-License-Identifier: MIT-0
