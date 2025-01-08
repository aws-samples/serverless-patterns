# Amazon EventBridge Scheduler to AWS Lambda to AWS Secrets Manager

This sample project demonstrates rotating secrets in AWS Secrets Manager using Amazon EventBridge Scheduler and AWS Lambda at desired intervals.

Learn more about this pattern at Serverless Land Patterns: [https://serverlessland.com/patterns/eventbridge-schedule-secret-rotation-cdk](https://serverlessland.com/patterns/eventbridge-schedule-secret-rotation-cdk)

Important: this application uses various AWS services and there are costs associated with these services after the Free Tier usage - please see the [AWS Pricing page](https://aws.amazon.com/pricing/) for details. You are responsible for any AWS costs incurred. No warranty is implied in this example.

## Requirements

* [Create an AWS account](https://portal.aws.amazon.com/gp/aws/developer/registration/index.html) if you do not already have one and log in. The IAM user that you use must have sufficient permissions to make necessary AWS service calls and manage AWS resources.
* [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html) installed and configured
* [Git Installed](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)
* [AWS CDK Toolkit](https://docs.aws.amazon.com/cdk/v2/guide/cli.html) (AWS CDK Toolkit) installed and configured

## Deployment Instructions

1. Create a new directory, navigate to that directory in a terminal and clone the GitHub repository:
    ``` 
    git clone https://github.com/aws-samples/serverless-patterns
    ```

2. Create and activate Python virtual environment. For instructions, please refer this [page](https://python.land/virtual-environments/virtualenv#Python_venv_activation)

3. Install the required pacakages
     ``` 
    pip install -r requirements.txt
    ```

4. Change directory to the pattern directory:
    ```
    cd serverless-patterns/eventbridge-schedule-secret-rotation-cdk
    ```
5. From the command line, use AWS CDK to deploy the AWS resources for the pattern as specified in the [eventbridge_schedule_secret_rotation_stack.py](/cdk/eventbridge_schedule_secret_rotation_stack.py) file:
    ```
    cdk deploy
    ```
    The sample project configures the secret rotation to be triggered every hour. If you wish to use use a different value, you could do so by providing a cron/rate based expression for the *SecretRotationSchedule* param. Please refer AWS [documentation](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-scheduled-rule-pattern.html) about using cron/rate expressions.
    ```
    cdk deploy --parameters SecretRotationSchedule="cron(* 0/1 * * ? *)"
    ```

6. Note the outputs from the CDK deployment process. These contain the arns for the Demo Secret and the rotation lambda.

## How it works

An EventBridge schedule is created based on the 'SecretRotationschedule' CDK parameter with the rotation lambda as the target. Rotation lambda performs the below mentioned steps on the demo secret.

- Creates a new version of the secret with AWSPENDING staging label.
- Updates the new version of the secret with the new value.
- Updates current version of the secret in AWSCURRENT stage to AWSPREVIOUS.
- Updates the staging label on the new version of secret from AWSPENDING to AWSCURRENT

## Testing

- Copy *SecretArn* value from the cdk output.
- Run the following command from the command line to retrive the secret value

    ```
    aws secretsmanager get-secret-value --secret-id="{SecretArn}"
    ```
- Run the following command to view the versions created for the secret as part of rotation process

    ```
    aws secretsmanager describe-secret --secret-id="{SecretArn}"
    ```

## Cleanup
 
1. Delete the stack
    ```
    cdk destroy EventbridgeScheduleSecretRotationCdkStack
    ```
2. Deactivate the Python virtual environment. For instructions, please refer this [page](https://python.land/virtual-environments/virtualenv#Python_venv_activation)
   
----
Copyright 2024 Amazon.com, Inc. or its affiliates. All Rights Reserved.

SPDX-License-Identifier: MIT-0
