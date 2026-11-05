# Bulk object tagging with Amazon S3 Batch Operations and AWS Step Functions

This pattern deploys an AWS Step Functions workflow that creates an Amazon S3 Batch Operations job through the AWS SDK integration for Amazon S3 Control. S3 generates the object list from a key prefix, so there is no manifest file to build. The workflow polls the job until it ends, then branches on the failed-task count and publishes either a success or a failure message to Amazon SNS.

Learn more about this pattern at Serverless Land Patterns: https://serverlessland.com/patterns/s3-sfn-batch-operations-typescript-cdk

Important: this application uses various AWS services and there are costs associated with these services after the Free Tier usage - please see the [AWS Pricing page](https://aws.amazon.com/pricing/) for details. You are responsible for any AWS costs incurred. No warranty is implied in this example.

## Requirements

* [Create an AWS account](https://portal.aws.amazon.com/gp/aws/developer/registration/index.html) if you do not already have one and log in. The IAM user that you use must have sufficient permissions to make necessary AWS service calls and manage AWS resources.
* [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html) installed and configured
* [Git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git) installed
* [Node.js 22 or later](https://nodejs.org/en/download/) installed
* [AWS CDK v2](https://docs.aws.amazon.com/cdk/v2/guide/getting_started.html) available through `npx` (installed by `npm install` below)

## Supported Regions

Deployed and tested in us-west-2 only. The stack takes the Region from your AWS CLI configuration and has no Region-specific code. The buckets and the job must be in the same Region.

## Architecture

```
Execution input {"prefix": "data/"}
        |
        v
AWS Step Functions
  CreateJob --> Wait --> DescribeJob --> Choice (status, failed tasks)
     |           ^                          |            |
     |           +----- still running ------+            v
     v                                              Amazon SNS: success, or failure
Amazon S3 Batch Operations job                      with job ID and counts
  (S3 generated manifest)
     |
     v
tags matching objects in the source bucket;
writes the manifest and the report to the report bucket
```

## How it works

1. You start an execution with a key prefix, for example `{"prefix": "data/"}`. A Choice state ends the run in an `InvalidInput` Fail state when `prefix` is missing, empty or not a string. Optional `tagKey` and `tagValue` inputs set the tag (default `processed=true`).
2. The `CreateJob` state calls S3 Control `CreateJob` with an `S3PutObjectTagging` operation and an `S3JobManifestGenerator` whose filter is `MatchAnyPrefix` on that prefix. The job role is passed to S3 Batch Operations, and the execution name is the `ClientRequestToken`, an idempotency token, so that a repeated request with the same token does not create a second job (not exercised here).
3. The workflow waits 15 seconds, calls `DescribeJob`, and loops until the job status is `Complete`, `Failed` or `Cancelled`; any other status counts as still running. The loop is bounded at 40 status checks and the state machine has a 20 minute timeout.
4. The Choice state sends the run to Amazon SNS. `Complete` with zero failed tasks publishes a success message and the execution succeeds. Any other end, including `Complete` with failed tasks, publishes a message with the job ID, status and counts, and the execution ends in a Fail state. If the job is still running after the 40th status check, the message says the workflow stopped waiting and the job may still be running; the execution ends in the same Fail state (this path was not exercised).
5. The manifest S3 generated and the completion report (failed tasks only) are written to the report bucket.

The `s3control` SDK integration has no `.sync` variant, which is why the workflow polls. The poll and branch is what turns a single `CreateJob` call into a workflow that reports the outcome.

To run the workflow on a schedule, an Amazon EventBridge Scheduler schedule can target the state machine. This pattern does not deploy one, because each run tags objects again.

## Important Notes

* The job role can tag only objects under `data/` in the source bucket. Running the workflow with another prefix makes the tasks for those objects fail, which exercises the failure branch (see Testing).
* The trust policy of the job role has no `aws:SourceAccount` or `aws:SourceArn` condition, because the S3 documentation for Batch Operations roles shows none.
* The state machine role passes the job role with `iam:PassRole`, limited by `iam:PassedToService` set to `s3.amazonaws.com`. The job role trusts `batchoperations.s3.amazonaws.com`, but in a test `CreateJob` was denied for lack of `iam:PassRole` with that value in the condition and succeeded with `s3.amazonaws.com`.
* Tagging replaces the whole tag set of each matching object: in a test, a run with `tagKey` `stage` and `tagValue` `done` left `stage=done` as the only tag.
* A prefix that matches no object fails the job while S3 generates the manifest (`InvalidManifestContent`, "Manifest generation found no keys matching the filter criteria"), and the execution ends `FAILED` with `JobNotSuccessful`.
* The execution name is the `ClientRequestToken`, which S3 limits to 64 characters. Use execution names of 64 characters or fewer.
* The job entries are not stack resources: `aws s3control list-jobs` still returns them after `cdk destroy`.
* `autoDeleteObjects` adds a helper AWS Lambda function owned by the AWS CDK, so that `cdk destroy` can empty the buckets. There is no Lambda function in the workflow.
* S3 Batch Operations bills per job and per object operation, and nothing in the stack bills by the hour. See the [Amazon S3 pricing page](https://aws.amazon.com/s3/pricing/).

## Deployment Instructions

1. Clone the repository:
    ```bash
    git clone https://github.com/aws-samples/serverless-patterns
    cd serverless-patterns/s3-sfn-batch-operations/typescript/cdk
    ```

2. Install dependencies and check that the project builds:
    ```bash
    npm install
    npm run build
    ```

3. If the account and Region have never been used with the AWS CDK, bootstrap them once:
    ```bash
    npx cdk bootstrap
    ```

4. Deploy the stack:
    ```bash
    npx cdk deploy
    ```

The stack outputs `StateMachineArn`, `StateMachineLogGroupName`, `SourceBucketName`, `ReportBucketName` and `TopicArn`. The Testing commands read them with the helper below.

## Testing

Commands use the AWS CLI v2 (tested with 2.31.3). The Expected results were observed in us-west-2.

1. Define the helpers and the variables. Run this block again in every new terminal:
    ```bash
    out() { aws cloudformation describe-stacks --stack-name S3SfnBatchOperationsStack \
      --query "Stacks[0].Outputs[?OutputKey=='$1'].OutputValue" --output text; }
    SM_ARN=$(out StateMachineArn); SRC=$(out SourceBucketName); REPORT=$(out ReportBucketName); TOPIC=$(out TopicArn)
    run() { # usage: run <name> <input json>; starts an execution, waits for it to end, prints status, error and output
      local arn; arn=$(aws stepfunctions start-execution --state-machine-arn "$SM_ARN" --name "$1-$(date +%s)" \
        --input "$2" --query executionArn --output text)
      until [ "$(aws stepfunctions describe-execution --execution-arn "$arn" --query status --output text)" != RUNNING ]; do sleep 10; done
      aws stepfunctions describe-execution --execution-arn "$arn" --query '{status:status,error:error,output:output}'
    }
    ```

2. Subscribe to the topic and confirm the subscription from your inbox, so the messages arrive during the runs. Replace `you@example.com` with your own address:
    ```bash
    aws sns subscribe --topic-arn "$TOPIC" --protocol email --notification-endpoint you@example.com
    ```

3. Upload three objects under `data/` and one under `private/`:
    ```bash
    for i in 1 2 3; do echo "sample $i" | aws s3 cp - "s3://$SRC/data/object-$i.txt"; done
    echo "sample" | aws s3 cp - "s3://$SRC/private/object-1.txt"
    ```

4. Success run. The job runs asynchronously, so the wait takes a while (about a minute in the test runs, longer for more objects):
    ```bash
    run run-ok '{"prefix": "data/"}'
    ```
   Expected: status `SUCCEEDED` and an output like `{"JobId":"<job id>","Status":"Complete","TasksSucceeded":3,"TasksFailed":0}`. Amazon SNS publishes the subject `S3 Batch Operations job succeeded` with the message `Job <job id> completed: 3 of 3 tasks succeeded, 0 failed.` to every subscriber (in the test runs it was read from an Amazon SQS queue subscribed to the topic).

5. Read the effect on the objects, independent of the workflow output:
    ```bash
    for k in data/object-1.txt data/object-3.txt private/object-1.txt; do
      echo "$k"; aws s3api get-object-tagging --bucket "$SRC" --key "$k" --query TagSet
    done
    aws s3 ls "s3://$REPORT/manifests/" --recursive
    ```
   Expected: `processed=true` on the `data/` objects, an empty tag set (`[]`) on `private/object-1.txt`, and the files of the generated manifest (`manifest.json`, a `.csv.gz` object and others) listed under `manifests/`.

6. Failure run. The job role cannot tag objects outside `data/`, so the tasks for `private/` should fail:
    ```bash
    run run-fail '{"prefix": "private/"}'
    aws s3 ls "s3://$REPORT/reports/" --recursive
    ```
   Expected: status `FAILED` with error `JobNotSuccessful`. SNS publishes the subject `S3 Batch Operations job needs attention` with the message `Job <job id> ended with status Complete: 1 of 1 tasks failed.` The job itself ends `Complete` with one failed task, which is why the workflow checks the failed-task count and not only the status. The completion report is a CSV under `reports/job-<job id>/results/` that lists the failed task.

To read errors from the state machine, use the log group in the `StateMachineLogGroupName` output.

## Cleanup

1. Delete the stack. This also deletes both buckets with every object in them, including the manifest and the reports:
    ```bash
    npx cdk destroy
    ```

2. The `autoDeleteObjects` helper function can leave its log group behind. List it and delete it:
    ```bash
    aws logs describe-log-groups --log-group-name-prefix /aws/lambda/S3SfnBatchOperationsStack-CustomS3AutoDelete \
      --query 'logGroups[].logGroupName' --output text | tr '\t' '\n' | \
      while read -r g; do [ -n "$g" ] && aws logs delete-log-group --log-group-name "$g"; done
    ```

----
Copyright 2026 Amazon.com, Inc. or its affiliates. All Rights Reserved.

SPDX-License-Identifier: MIT-0
