# AWS Step Functions workflow to integrate with AWS Glue Job using CDK.

This CDK application deploys a Step Functions workflow, that takes in a payload and trigger a AWS Glue job synchronously. In this pattern, the state machine does wait for Glue job to finish. The application contains the minimum IAM resources required to run the workflow and Glue job. 



Learn more about this pattern at Serverless Land Patterns: https://serverlessland.com/patterns/sfn-glue-sync-cdk

Important: This application uses various AWS services and there are costs associated with these services after the Free Tier usage - please see the [AWS Pricing page](https://aws.amazon.com/pricing/) for details. You are responsible for any AWS costs incurred. No warranty is implied in this example.

## Requirements

* [Create an AWS account](https://portal.aws.amazon.com/gp/aws/developer/registration/index.html) if you do not already have one and log in. The IAM user that you use must have sufficient permissions to make necessary AWS service calls and manage AWS resources.
* [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html) installed and configured
* [Git Installed](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)
* [AWS Cloud Development Kit](https://docs.aws.amazon.com/cdk/latest/guide/getting_started.html) (AWS CDK >= 1.124.0) Installed

## Deployment Instructions

1. Create a new directory, navigate to that directory in a terminal and clone the GitHub repository:
    ```bash 
    git clone https://github.com/aws-samples/serverless-patterns
    ```
1. Change directory to the pattern directory:
    ```bash
    cd sfn-glue-sync-cdk
    ```
1. Create a virtual environment for python:
    ```bash
    python3 -m venv .venv
    ```
1. Activate the virtual environment:
    ```bash
    source .venv/bin/activate
    ```
1. Install python modules:
    ```bash
    python3 -m pip install -r requirements.txt
    ```
1. From the command line, use CDK to synthesize the CloudFormation template and check for errors:
    ```bash
    cdk synth
    ```
1. From the command line, use CDK to deploy the stack:
    ```bash
    cdk deploy
    ```
1. Note the outputs from the CDK deployment process. These contain the resource names and/or ARNs which are used for testing.

## How it works

The CDK stack deploys the resources and the IAM permissions required to run the application.
This stack will deploy S3 bucket to store glue job scripts, python-shell glue job and state function which executes 'glue:startJobRun.sync' step.


Step Functions supports AWS Glue through the service integration pattern.
You can call the `StartJobRun` API from a Task state with
[Run a Job (.sync)](https://docs.aws.amazon.com/step-functions/latest/dg/connect-to-resource.html#connect-sync) integration pattern.

Task `GlueStartJobRun` defined in the `app.py` triggers a glue job and wait for job completion before transitioning to next step.
Python-shell glue job is defined with `glue.CfnJob` in `app.py` which triggers a python script `hello.py`
 
## Steps for Testing

* Start the Step Function execution with the sample event payload. 
* As part of the execution, part of the payload (the `message` attribute of the payload) is passed as `--message` parameter to the glue job.
* Run the CLI command to check the step execution and glue job execution status.

## Testing

Run the following AWS CLI command to send a 'start-execution` command to start the Step Functions workflow. Note, you must edit the {StateMachineArn} placeholder with the ARN of the deployed Step Functions workflow. This is provided in the stack outputs.

```bash
aws stepfunctions start-execution --state-machine-arn "{StateMachineArn}" --input "{\"message\": \"Hello from sfn glue step\"}"
```
:information_source: Account Number is masked in all the outputs.

### output:

```json
{
    "executionArn": "arn:aws:states:us-east-1:<*AccountNumber*>:execution:GlueJobStateMachineE759615B-t1nYjCro8h5F:36bd81e5-787a-4e34-ac6a-1f21064802ff",
    "startDate": "2021-11-17T22:37:02.301000-06:00"
}
```

Note the `executionArn` from the above output and run the following CLI command to get the status of the execution.

```bash
aws stepfunctions describe-execution --execution-arn  "{executionArn}"
```

### Get execution status output:

```json
{
    "executionArn": "arn:aws:states:us-east-1:<*AccountNumber*>:execution:GlueJobStateMachineE759615B-t1nYjCro8h5F:36bd81e5-787a-4e34-ac6a-1f21064802ff",
    "stateMachineArn": "arn:aws:states:us-east-1:<*AccountNumber*>:stateMachine:GlueJobStateMachineE759615B-t1nYjCro8h5F",
    "name": "36bd81e5-787a-4e34-ac6a-1f21064802ff",
    "status": "RUNNING",
    "startDate": "2021-11-17T22:37:02.301000-06:00",
    "input": "{\"message\": \"Hello from sfn glue step\"}",
    "inputDetails": {
        "included": true
    }
}
```

Run the following AWS CLI command to get the status of the glue job triggred by step function.

```bash
aws glue get-job-runs --job-name "cdk-test-glue-python-job"
```

### Output:

```json
{
    "JobRuns": [
        {
            "Id": "jr_c14390561406a75616f270734b658e17f7175895f3fc3c289279b708840e5584",
            "Attempt": 0,
            "JobName": "cdk-test-glue-python-job",
            "StartedOn": "2021-11-17T22:37:02.488000-06:00",
            "LastModifiedOn": "2021-11-17T22:37:06.008000-06:00",
            "JobRunState": "RUNNING",
            "Arguments": {
                "--message": "Hello from sfn glue step"
            },
            "PredecessorRuns": [],
            "AllocatedCapacity": 0,
            "ExecutionTime": 45,
            "Timeout": 6,
            "MaxCapacity": 0.0625,
            "LogGroupName": "/aws-glue/python-jobs",
            "NotificationProperty": {
                "NotifyDelayAfter": 6
            }
        }
    ]
}
```
Re-run above command again after 5 minutes or until `JobRunState` is `SUCCEEDED`.

Note `JobRunState`  and `LogGroupName` from the above output. Once the `JobRunState` is `SUCCEEDED`, we can verify glue job log by running the following command(append `/output` to the `LogGroupName` value captured from above output).

```bash
aws logs tail "/aws-glue/python-jobs/output"
```

### Log output:

```log
2021-11-18T04:40:18.556000+00:00 jr_c14390561406a75616f270734b658e17f7175895f3fc3c289279b708840e5584 python-shell glue job message - Hello from sfn glue step

```

Re-run the following CLI command to get the latest status of the staefunction execution and confirm the  `status` is `SUCCEEDED`.

:information_source: It might take some time for the statefunction execution to complete after glue job is completed.

```bash
aws stepfunctions describe-execution --execution-arn  "{executionArn}"
```

### Get execution status output:

```bash
{
    "executionArn": "arn:aws:states:us-east-1:<*AccountNumber*>:execution:GlueJobStateMachineE759615B-t1nYjCro8h5F:36bd81e5-787a-4e34-ac6a-1f21064802ff",
    "stateMachineArn": "arn:aws:states:us-east-1:<*AccountNumber*>:stateMachine:GlueJobStateMachineE759615B-t1nYjCro8h5F",
    "name": "36bd81e5-787a-4e34-ac6a-1f21064802ff",
    "status": "SUCCEEDED",
    "startDate": "2021-11-17T22:37:02.301000-06:00",
    "stopDate": "2021-11-17T22:41:08.340000-06:00",
    "input": "{\"message\": \"Hello from sfn glue step\"}",
    "inputDetails": {
        "included": true
    },
    "output": "{\"AllocatedCapacity\":0,\"Arguments\":{\"--message\":\"Hello from sfn glue step\"},\"Attempt\":0,\"CompletedOn\":1637210428964,\"ExecutionTime\":197,\"Id\":\"jr_c14390561406a75616f270734b658e17f7175895f3fc3c289279b708840e5584\",\"JobName\":\"cdk-test-glue-python-job\",\"JobRunState\":\"SUCCEEDED\",\"LastModifiedOn\":1637210428964,\"LogGroupName\":\"/aws-glue/python-jobs\",\"MaxCapacity\":0.0625,\"NotificationProperty\":{\"NotifyDelayAfter\":6},\"PredecessorRuns\":[],\"StartedOn\":1637210222488,\"Timeout\":6}",
    "outputDetails": {
        "included": true
    }
}
```

## Cleanup
 
1. Run the given command to delete the resources that were created. It might take some time for the CloudFormation stack to get deleted. 
    
    :warning: This will delete S3 bucket defind as part of this CDK stack(S3 bucket name is provided in the CDK stack outputs)!

    ```bash
    cdk destroy
    ```
1. Deactivate the virtual environment:
    ```bash
    deactivate
    ```

## Documentation and useful references

- [What Is AWS Glue?](https://docs.aws.amazon.com/glue/latest/dg/what-is-glue.html)
- [Manage AWS Glue Jobs with Step Functions](https://docs.aws.amazon.com/step-functions/latest/dg/connect-glue.html)
- [Service Integration Patterns](https://docs.aws.amazon.com/step-functions/latest/dg/connect-to-resource.html#connect-sync)
- [CDK documentation for Glue](https://docs.aws.amazon.com/cdk/api/latest/docs/aws-glue-readme.html)
- [CDK documentation for Step Functions](https://docs.aws.amazon.com/cdk/api/latest/docs/aws-stepfunctions-readme.html)
- [CDK documentation for Step Functions Tasks](https://docs.aws.amazon.com/cdk/api/latest/docs/aws-stepfunctions-tasks-readme.html)

----
Copyright 2021 Amazon.com, Inc. or its affiliates. All Rights Reserved.

SPDX-License-Identifier: MIT-0