# Amazon API Gateway to AWS Lambda durable function to AWS Lambda MicroVM

This pattern runs one job per ephemeral MicroVM. A `POST /jobs` request to
Amazon API Gateway starts an AWS Lambda durable function, which boots an AWS
Lambda MicroVM from a snapshot, hands it a command, and suspends with no compute
billed until the MicroVM posts its result back through API Gateway. The durable
function then terminates the MicroVM and records the result, which `GET
/jobs/{jobId}` returns. The whole round trip took 3 to 10 seconds in testing.

Learn more about this pattern at Serverless Land Patterns: << Add the live URL here >>

Important: this application uses various AWS services and there are costs associated with these services after the Free Tier usage - please see the [AWS Pricing page](https://aws.amazon.com/pricing/) for details. You are responsible for any AWS costs incurred. No warranty is implied in this example.

## Requirements

* [Create an AWS account](https://portal.aws.amazon.com/gp/aws/developer/registration/index.html) if you do not already have one and log in. The IAM user that you use must have sufficient permissions to make necessary AWS service calls and manage AWS resources.
* [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html) installed and configured
* [Git Installed](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)
* [AWS Serverless Application Model](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-sam-cli-install.html) (AWS SAM) installed
* Lambda MicroVMs available in your Region (check with `aws lambda-microvms list-managed-microvm-images`)
* An S3 bucket in the same Region for the MicroVM image zip
* The `zip` command line utility

## Deployment Instructions

1. Create a new directory, navigate to that directory in a terminal and clone the GitHub repository:
    ```
    git clone https://github.com/aws-samples/serverless-patterns
    ```
1. Change directory to the pattern directory:
    ```
    cd apigw-lambda-durable-microvm/python/sam
    ```
1. Zip the MicroVM application (the `Dockerfile` must be at the zip root) and upload it to your bucket. Use a new key each time you change `src/vm/`, because `AWS::Lambda::MicrovmImage` only rebuilds when a property such as the key changes:
    ```
    cd src/vm && zip -j ../../vm.zip Dockerfile app.py && cd ../..
    aws s3 cp vm.zip s3://YOUR_BUCKET/microvm-jobs/vm-$(date +%Y%m%d%H%M).zip
    ```
1. From the command line, use AWS SAM to build and deploy the AWS resources for the pattern as specified in the template.yaml file:
    ```
    sam build
    sam deploy --guided
    ```
1. During the prompts:
    * Enter a stack name
    * Enter the desired AWS Region
    * Enter your bucket name for `CodeArtifactBucket` and the key you uploaded for `CodeArtifactKey`
    * Accept the defaults for `JobTimeoutSeconds` and `VmMemoryMiB`
    * Allow SAM CLI to create IAM roles with the required permissions
    * Answer `y` to `ApiFunction has no authentication. Is this okay?` (see Testing for why)

    Once you have run `sam deploy --guided` mode once and saved arguments to a configuration file (samconfig.toml), you can use `sam deploy` in future to use these defaults.

    CloudFormation builds the MicroVM image during the deploy and waits for it to become active, so the first deploy takes a few minutes longer than usual.

1. Note the outputs from the SAM deployment process. `JobsEndpoint` is the URL used for testing.

## How it works

```
client --POST /jobs--> API Gateway --> ApiFunction --Invoke (Event, alias live)--> OrchestratorFunction (durable)
                                                                                       |  step run-microvm
                                                                                       v
                                                                                   MicroVM (from JobImage snapshot)
                                                                                       |  runs the command
client <--GET /jobs/{id}-- API Gateway <-- ApiFunction                                  |
                                              ^                                        v
                                              +----POST /callback----- API Gateway <---+
                                      SendDurableExecutionCallbackSuccess/Failure
                                                                                       |
                                                                 OrchestratorFunction resumes, step terminate-microvm
```

1. `POST /jobs` with a JSON body `{"command": "..."}`. `ApiFunction` generates a job id, and invokes the orchestrator asynchronously through its `live` alias with that id as the durable execution name. It also passes its own `/callback` URL in the payload, which avoids a circular reference in the template (the API would otherwise depend on the orchestrator's environment and vice versa).
2. `OrchestratorFunction` is a durable function. It creates a callback, then in a durable step calls `RunMicrovm` on the image the stack built, passing the command, the callback id and the callback URL in `runHookPayload`. `maximumDurationInSeconds` is set to the same value as the durable execution timeout, so a MicroVM can never outlive the execution that owns it. No idle policy is set: idle is measured on inbound traffic and this MicroVM receives only the run hook, so an idle policy would suspend it mid-job.
3. The orchestrator calls `callback.result()` and suspends. No Lambda compute is billed while it waits.
4. The MicroVM resumes from its snapshot. The platform POSTs the run hook to the app in `src/vm/app.py`, which parses `runHookPayload`, runs the command with a 600 second limit, and POSTs `{"callbackId", "status", "result"}` to the callback URL. The image is built with the `INTERNET_EGRESS` network connector so it can reach API Gateway.
5. `POST /callback` reaches `ApiFunction`, which calls `SendDurableExecutionCallbackSuccess` or `SendDurableExecutionCallbackFailure` with the callback id. The orchestrator resumes, records the result or the failure, and in a final durable step calls `TerminateMicrovm`. Teardown runs on both the success and the failure path.
6. `GET /jobs/{jobId}` calls `ListDurableExecutionsByFunction` with the job id as the execution name and `GetDurableExecution` for the status and result. No database is needed: the durable execution is the record.

IAM: `ApiFunction` may invoke and read executions of the orchestrator only, and send callbacks to it. The orchestrator may run, read and terminate MicroVMs (a MicroVM has no ARN until `RunMicrovm` returns, so these three actions are not resource-scoped; the image and execution role it may use are fixed by its environment and by the `iam:PassRole` statement, which is scoped to the one execution role). The image build role may read the one zip key and write build logs. The MicroVM execution role may write runtime logs. SAM attaches `AWSLambdaBasicDurableExecutionRolePolicy` to the orchestrator for checkpointing.

`AutoPublishAlias: live` publishes a new version on every code change and moves the alias, which is required because durable executions are bound to a function version.

## Testing

The endpoint is unauthenticated so the test is a plain HTTP call; add an authorizer before using this beyond a test account.

1. Start a job:
    ```bash
    JOBS=$(aws cloudformation describe-stacks --stack-name STACK_NAME --query "Stacks[0].Outputs[?OutputKey=='JobsEndpoint'].OutputValue" --output text)
    curl -s -X POST "$JOBS" -H 'Content-Type: application/json' -d '{"command": "uname -m; nproc; python3 --version"}'
    ```
    Expected: `{"jobId": "<uuid>"}` with HTTP 202.

1. Read the result (allow about 5 to 10 seconds for the MicroVM to resume, run the command and call back):
    ```bash
    curl -s "$JOBS/<jobId>"
    ```
    Expected:
    ```json
    {"jobId": "<uuid>", "status": "SUCCEEDED",
     "result": {"status": "completed", "microvmId": "microvm-...",
                "result": {"exitCode": 0, "stdout": "aarch64\n1\nPython 3.13.x\n", "stderr": ""}}}
    ```
    While the job is running the status is `RUNNING` and there is no `result` key.

1. A failing command is reported, not swallowed:
    ```bash
    curl -s -X POST "$JOBS" -H 'Content-Type: application/json' -d '{"command": "echo boom >&2; exit 3"}'
    ```
    The execution still reaches `SUCCEEDED` (the orchestration completed), with `result.status` of `failed` and the exit code and stderr under `result.result.data`.

1. A freshly deployed API can answer a few early requests with `403 {"message":"Forbidden"}` (`x-amzn-ErrorType: ForbiddenException`). This is the response API Gateway gives when it cannot map the request to a stage, and it was observed only within about two minutes of the stage being created, never afterwards (0 in 3,478 requests from 10 seconds onward on one fresh API, 0 in 3,200 on another after 7 minutes). The MicroVM app retries the callback with backoff, so a job started right after deploy still completes; if your first `curl` gets a 403, wait a minute and retry.

1. If the MicroVM never calls back (for example the command hangs), the execution ends with status `TIMED_OUT` after `JobTimeoutSeconds` and the MicroVM is terminated by the platform at the same moment, because `maximumDurationInSeconds` is set to the same value. Verified in testing: a job whose callback was lost reported `TIMED_OUT` at 900 seconds with no MicroVM left running.

1. Confirm the MicroVM was terminated:
    ```bash
    aws lambda-microvms list-microvms --query "microvms[?state!='TERMINATED'].microvmId"
    ```
    Expected: `[]`.

## Cleanup

1. Delete the stack. Deleting the `AWS::Lambda::MicrovmImage` resource deletes the image and its versions.
    ```bash
    sam delete --stack-name STACK_NAME
    ```
1. Delete the image zip from your bucket:
    ```bash
    aws s3 rm s3://YOUR_BUCKET/microvm-jobs/ --recursive
    ```
1. Confirm the stack has been deleted
    ```bash
    aws cloudformation list-stacks --query "StackSummaries[?contains(StackName,'STACK_NAME')].StackStatus"
    ```
----
Copyright 2026 Amazon.com, Inc. or its affiliates. All Rights Reserved.

SPDX-License-Identifier: MIT-0
