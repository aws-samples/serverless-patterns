# Amazon EventBridge Scheduler to AWS Systems Manager State Manager Associations

This pattern demonstrates how to create an Amazon EventBridge scheduler to run AWS Systems Manager State Manager Associations using AWS Cloud Development Kit (CDK) for Python.

Important: this application uses various AWS services and there are costs associated with these services after the Free Tier usage - please see the [AWS Pricing page](https://aws.amazon.com/pricing/) for details. You are responsible for any AWS costs incurred. No warranty is implied in this example.

## Requirements

* [Create an AWS account](https://portal.aws.amazon.com/gp/aws/developer/registration/index.html) if you do not already have one and log in. The IAM user that you use must have sufficient permissions to make necessary AWS service calls and manage AWS resources.
* [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html) installed and configured
* [Git Installed](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)
* [AWS CDK Toolkit](https://docs.aws.amazon.com/cdk/latest/guide/cli.html) installed and configured
* [Python 3.9+](https://www.python.org/downloads/) installed

## Deployment Instructions

1. Create a new directory, navigate to that directory in a terminal and clone the GitHub repository:
    ``` 
    git clone https://github.com/aws-samples/serverless-patterns
    ```
2. Change directory to the pattern directory:
    ```
    cd eventbridge-scheduler-ssm-cdk-python
    ```
3. From the command line, bootstrap the CDK if you haven't already done so:
    ```
    cdk bootstrap
    ```
4. Install the Python required dependencies:
    ```
    pip install -r requirements.txt
    ```
5. Deploy the CDK stack to your default AWS account and region. 
    ```
    cdk deploy
    ```

## How it works

In this example we deploy an Amazon EventBridge Scheduler that runs every Sunday at 2:00 AM UTC and runs an association that updates SSM agent on all EC2 instances.

## Testing

1. To test the pattern, create an EC2 instance in your account: https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/EC2_GetStarted.html

2. Get a list of associations:
```bash
aws ssm list-associations --association-filter-list "key=AssociationName,value=UpdateSSMAgent"
```
3. Describe association executions:
```bash
aws ssm describe-association-executions --association-id "<association-id-from-previous-step>"
```
This command should return the association execution details, similar to the following:
```json
{
    "AssociationExecutions": [
        {
            "AssociationId": "<association-id>",
            "AssociationVersion": "1",
            "ExecutionId": "<execution-id>",
            "Status": "Success",
            "DetailedStatus": "Success",
            "CreatedTime": "2023-04-15T21:59:31.708000+00:00",
            "ResourceCountByStatus": "{Success=1}"
        }
    ]
}
```
## Cleanup
 
1. Delete the stack
    ```bash
    cdk destroy
    ```
2. Terminate the EC2 instance: https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/terminating-instances.html

----
Copyright 2023 Amazon.com, Inc. or its affiliates. All Rights Reserved.

SPDX-License-Identifier: MIT-0