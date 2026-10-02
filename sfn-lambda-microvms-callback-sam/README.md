# AWS Step Functions to AWS Lambda MicroVMs with a task token callback

This pattern runs a job on an AWS Lambda MicroVM from an AWS Step Functions workflow, using the Step Functions AWS SDK integration for Lambda MicroVMs. The workflow starts the MicroVM, waits for the job inside it to report its result through a task token, and always terminates the MicroVM afterwards, whether the job succeeds, fails, stops sending heartbeats or runs out of time. No AWS Lambda function sits in between.

Learn more about this pattern at Serverless Land Patterns: https://serverlessland.com/patterns/sfn-lambda-microvms-callback-sam

Important: this application uses various AWS services and there are costs associated with these services after the Free Tier usage - please see the [AWS Pricing page](https://aws.amazon.com/pricing/) for details. You are responsible for any AWS costs incurred. No warranty is implied in this example.

## Requirements

* [Create an AWS account](https://portal.aws.amazon.com/gp/aws/developer/registration/index.html) if you do not already have one and log in. The IAM user that you use must have sufficient permissions to make necessary AWS service calls and manage AWS resources.
* [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html) version 2 installed and configured, recent enough to include the `aws lambda-microvms` commands (tested with 2.35.21)
* [Git Installed](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)
* [AWS Serverless Application Model](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-sam-cli-install.html) (AWS SAM) installed
* `zip` on your `PATH`
* An AWS Region where Lambda MicroVMs are available, for example `us-east-1`

## Deployment Instructions

1. Create a new directory, navigate to that directory in a terminal and clone the GitHub repository:
    ```
    git clone https://github.com/aws-samples/serverless-patterns
    ```
1. Change directory to the pattern directory:
    ```
    cd serverless-patterns/sfn-lambda-microvms-callback-sam
    ```
1. Set your Region and a name for a new S3 bucket that holds the worker code. The MicroVM image is built from this zip, so it must exist before you deploy:
    ```
    export AWS_REGION=us-east-1
    export ARTIFACT_BUCKET=sfn-microvms-callback-artifacts-$(aws sts get-caller-identity --query Account --output text)
    ```
1. Create the bucket, then zip and upload the worker (a `Dockerfile` and `app.py` at the root of the zip):
    ```
    aws s3 mb s3://$ARTIFACT_BUCKET --region $AWS_REGION
    (cd src/worker && zip -j ../../worker.zip Dockerfile app.py)
    aws s3 cp worker.zip s3://$ARTIFACT_BUCKET/worker.zip --region $AWS_REGION
    ```
1. From the command line, use AWS SAM to deploy the AWS resources for the pattern as specified in the template.yaml file:
    ```
    sam deploy --guided
    ```
1. During the prompts:
    * Enter a stack name of 57 characters or fewer (the MicroVM image is named after the stack)
    * Enter the same AWS Region as the artifact bucket
    * Enter the artifact bucket name for `ArtifactBucket` and keep the other defaults
    * Allow SAM CLI to create IAM roles with the required permissions.

    Once you have run `sam deploy --guided` mode once and saved arguments to a configuration file (samconfig.toml), you can use `sam deploy` in future to use these defaults.

    The stack waits until the MicroVM image is built, which takes a few minutes.

1. Note the outputs from the SAM deployment process. These contain the resource names and/or ARNs which are used for testing.

## How it works

Lambda MicroVMs run long or stateful work, for up to eight hours, in a Firecracker-isolated environment built from your own image. Unlike a Lambda function, a MicroVM is not invoked and does not return a response: you start it with `RunMicrovm`, and it keeps running and billing until it is terminated or reaches its maximum duration. That leaves two questions every workload has to answer: how does the caller get the job's result back, and who guarantees the MicroVM is terminated when the job is done or something goes wrong? This pattern answers both with Step Functions.

1. **Start MicroVM** calls `RunMicrovm` through the AWS SDK integration (`arn:aws:states:::aws-sdk:lambdamicrovms:runMicrovm`). The execution input becomes the job, passed to the MicroVM in the run hook payload. The execution ARN is used as the idempotency token, so a retried call never starts a second MicroVM. Idempotency tokens are shared across the account, so the execution name alone would collide with an execution of the same name in another state machine.
1. **Wait for job result** stores the task token in an Amazon DynamoDB table under the MicroVM ID and pauses, using the `.waitForTaskToken` integration pattern.
1. Inside the MicroVM, the `/run` lifecycle hook receives the job and the MicroVM ID. The worker reads the task token from DynamoDB, runs the job, sends `SendTaskHeartbeat` every 20 seconds while it works, and finishes with `SendTaskSuccess` (the result) or `SendTaskFailure` (the error).
1. **Terminate MicroVM** stops the MicroVM as soon as the result arrives. If the job reports a failure, misses heartbeats for `HeartbeatSeconds` (60 by default) or exceeds `MaximumDurationInSeconds`, the Catch path runs **Terminate MicroVM after failure** and the execution fails with the job's error.

Design notes:

* **Why the token goes through DynamoDB.** `RunMicrovm` does not support `.sync`, and calling it with `.waitForTaskToken` would discard its response, so the workflow would lose the MicroVM ID it needs to terminate the MicroVM on the failure path. Starting the MicroVM with a request and response call and handing the token over in a separate step keeps the ID available on every path. Items expire after one day through DynamoDB Time to Live.
* **Two layers of cleanup.** The workflow terminates the MicroVM on every path, and `MaximumDurationInSeconds` is also set on the MicroVM itself, so the platform stops it even if the execution is stopped by hand.
* **Least privilege.** The state machine may run and terminate MicroVMs only from this stack's image, and pass only the worker role. The worker may read only its token table and send task responses only to this state machine. The worker creates its AWS SDK clients in the `/run` hook, after the MicroVM starts, so no credentials or connections are captured in the image snapshot.
* **Networking.** The managed `INTERNET_EGRESS` connector lets the image build install packages and lets the worker reach the DynamoDB and Step Functions endpoints. `RunMicrovm` also attaches the managed `HTTP_INGRESS` connector by default, which is why the state machine role can pass it. The worker serves only lifecycle hooks, and calls to a MicroVM endpoint require an auth token from `CreateMicrovmAuthToken`, which nothing in this pattern is allowed to create.

To run your own workload, replace `run_job()` in `src/worker/app.py`, upload the new zip and redeploy. The result you return must fit in the 256 KiB Step Functions payload limit, so write large outputs to Amazon S3 and return the object key.

## Testing

1. Store the state machine ARN from the stack outputs (replace `STACK_NAME`):
    ```
    export STATE_MACHINE_ARN=$(aws cloudformation describe-stacks --stack-name STACK_NAME --region $AWS_REGION --query "Stacks[0].Outputs[?OutputKey=='StateMachineArn'].OutputValue" --output text)
    ```
1. **Successful job.** Count the primes below ten million, then keep the MicroVM busy for 90 seconds. That is longer than the 60-second heartbeat timeout, so the execution only keeps waiting because the worker sends heartbeats:
    ```
    aws stepfunctions start-execution --state-machine-arn $STATE_MACHINE_ARN --region $AWS_REGION --name success-1 --input '{"limit": 10000000, "durationSeconds": 90}'
    ```
    After about two minutes, describe the execution (replace `EXECUTION_ARN` with the ARN returned above):
    ```
    aws stepfunctions describe-execution --execution-arn EXECUTION_ARN --region $AWS_REGION --query "{status:status,output:output}"
    ```
    The status is `SUCCEEDED` and the output is the job result, for example `{"microvmId":"microvm-...","limit":10000000,"primeCount":664579,"elapsedSeconds":90.1}`.
1. **Failing job.** The worker raises an error and reports it with `SendTaskFailure`:
    ```
    aws stepfunctions start-execution --state-machine-arn $STATE_MACHINE_ARN --region $AWS_REGION --name failure-1 --input '{"simulate": "failure"}'
    ```
    The execution ends `FAILED` with error `JobFailed` and cause `Simulated failure requested in the job input`.
1. **Hung job.** The worker stops sending heartbeats and never answers, as a crashed or wedged process would:
    ```
    aws stepfunctions start-execution --state-machine-arn $STATE_MACHINE_ARN --region $AWS_REGION --name hang-1 --input '{"simulate": "hang"}'
    ```
    After `HeartbeatSeconds` (60 seconds by default) the execution ends `FAILED` with error `States.Timeout` and cause `The job stopped sending heartbeats or ran longer than the maximum duration.`
1. In every case, confirm the MicroVM was terminated. The MicroVM ID is in the `Start MicroVM` step output in the Step Functions console, or in the success output:
    ```
    aws lambda-microvms get-microvm --microvm-identifier MICROVM_ID --region $AWS_REGION --query state
    ```
    The state is `TERMINATED`. The worker output for each MicroVM is in the `WorkerLogGroupName` log group, in a log stream named after the MicroVM ID.

## Cleanup

1. Delete the stack. This removes the state machine, the MicroVM image, the DynamoDB table, the log group and the IAM roles:
    ```
    sam delete --stack-name STACK_NAME --region $AWS_REGION
    ```
1. Delete the artifact bucket and the local zip:
    ```
    aws s3 rb s3://$ARTIFACT_BUCKET --force --region $AWS_REGION
    rm worker.zip
    ```
1. Confirm the stack has been deleted:
    ```
    aws cloudformation list-stacks --region $AWS_REGION --query "StackSummaries[?contains(StackName,'STACK_NAME')].StackStatus"
    ```

----
Copyright 2026 Amazon.com, Inc. or its affiliates. All Rights Reserved.

SPDX-License-Identifier: MIT-0
