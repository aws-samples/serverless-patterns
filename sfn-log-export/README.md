# AWS Step Functions Workflow to archive CloudWatch logs

The Step Functions Workflow can be used to automate monthly export of CloudWatch logs into a S3 bucket for long term retention prior to logs being expired by a retention policy.

The SAM template deploys a Step Functions workflow that invokes a Lambda function to query log groups with matching tags and then uses another Lambda function to export these to target S3 bucket one at a time. One at a time export is necessary due to service limit of one concurrent export per account.

Important: this application uses various AWS services and there are costs associated with these services after the Free Tier usage - please see the [AWS Pricing page](https://aws.amazon.com/pricing/) for details. You are responsible for any AWS costs incurred. No warranty is implied in this example.

## Requirements

* [Create an AWS account](https://portal.aws.amazon.com/gp/aws/developer/registration/index.html) if you do not already have one and log in. The IAM user that you use must have sufficient permissions to make necessary AWS service calls and manage AWS resources.
* [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html) installed and configured
* [Git Installed](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)
* [AWS Serverless Application Model](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-sam-cli-install.html) (AWS SAM) installed

## Deployment Instructions

1. Create a new directory, navigate to that directory in a terminal and clone the GitHub repository:
    ``` 
    git clone https://github.com/aws-samples/serverless-patterns
    ```
1. Change directory to the pattern directory:
    ```
    cd sfn-log-export
    ```
1. From the command line, use AWS SAM to deploy the AWS resources for the pattern as specified in the template.yml file:
    ```
    sam deploy --guided
    ```
1. During the prompts:
    * Enter a stack name
    * Enter the desired AWS Region
    * Enter log group tags - only log groups with matching tags will be exported
    * Enter the archive bucket name
    * Enter archive prefix
    * Allow SAM CLI to create IAM roles with the required permissions.

   Once you have run `sam deploy -guided` mode once and saved arguments to a configuration file (samconfig.toml), you can use `sam deploy` in future to use these defaults.

1. Note the outputs from the SAM deployment process. These contain the resource names and/or ARNs which are used for testing.

## How it works

* On monthly schedule, an EventBridge rule will trigger the workflow and initiate the export.
* The workflow invokes a lambda function to query log groups with matching tags.
* The workflow will export found log groups one at a time into the archive bucket.
* If there's another export (unrelated to export) in progress within account, the workflow will wait and re-try the export.
* If the Lambda function fails or the workflow reaches maximum number of retries, the workflow will exit with a `status:FAILED` response.


## Testing

Run the following AWS CLI command to send a 'start-sync-execution` command to start the Step Functions workflow. Note, you must edit the {ArchiveLogsStateMachine} placeholder with the ARN of the deployed Step Functions workflow. This is provided in the stack outputs.

```bash
aws stepfunctions start-execution --state-machine-arn "{ArchiveLogsStateMachine}" --input "{}"
```

### Example output:

```bash
{
    "executionArn": "arn:aws:states:us-east-1:0123456789:execution:ArchiveLogsStateMachine-KU0AKB3vvHoa:a9fd62f6-beac-43bf-84c5-ab83d3594187",
    "startDate": "2021-11-26T12:50:15.315000-05:00"
}
```

## Inspect log archives exported to S3
Run the following AWS CLI command to query the S3 bucket to see exported logs. Note, you must edit {archive_bucket_name} and {archive_prefix} placeholders with parameters of the deployed SAM application. These are the parameter you provided when deploying SAM application.
```bash
aws s3 ls {archive_bucket_name}/{archive_prefix}/
```

## Cleanup

1. Delete the stack
    ```bash
    aws cloudformation delete-stack --stack-name STACK_NAME
    ```
1. Confirm the stack has been deleted
    ```bash
    aws cloudformation list-stacks --query "StackSummaries[?contains(StackName,'STACK_NAME')].StackStatus"
    ```
----
Copyright 2021 Amazon.com, Inc. or its affiliates. All Rights Reserved.

SPDX-License-Identifier: MIT-0