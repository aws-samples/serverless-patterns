# Lambda Managed Instances with AWS CDK Python

This pattern demonstrates how to create and deploy AWS Lambda Managed Instances using AWS CDK in Python. Lambda Managed Instances allow you to run Lambda functions on dedicated EC2 instances for workloads that require more control over the underlying infrastructure.

Learn more about this pattern at Serverless Land Patterns: [Lambda Managed Instances](https://serverlessland.com/patterns/lambda-managed-instances)

Important: this application uses various AWS services and there are costs associated with these services after the Free Tier usage - please see the [AWS Pricing page](https://aws.amazon.com/pricing/) for details. You are responsible for any AWS costs incurred. No warranty is implied in this example.

## Language

Python

## Framework

CDK

## Services From/To

AWS Lambda Managed Instances

## Requirements

* [Create an AWS account](https://portal.aws.amazon.com/gp/aws/developer/registration/index.html) if you do not already have one and log in. The IAM user that you use must have sufficient permissions to make necessary AWS service calls and manage AWS resources.
* [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html) installed and configured
* [Git Installed](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)
* [AWS Cloud Development Kit](https://docs.aws.amazon.com/cdk/v2/guide/getting_started.html) (AWS CDK >= 2.2.0) Installed

## Architecture

This CDK stack creates:

1. **IAM Roles**: 
   - Lambda execution role with basic execution permissions
   - Capacity provider operator role for managing EC2 instances

2. **VPC Resources**:
   - New VPC with CIDR 10.0.0.0/16
   - Private subnet with NAT Gateway for outbound internet access
   - Security group for Lambda Managed Instances

3. **Lambda Capacity Provider**:
   - Manages EC2 instances (x86_64 architecture)
   - Maximum 30 vCPUs scaling configuration

4. **Lambda Function**:
   - Python 3.13 runtime
   - 2048 MB memory allocation
   - 512 MB ephemeral storage
   - Configured to use the managed instances capacity provider

## Deployment Instructions

1. Clone this repository and navigate to the pattern directory:
    ```bash
    cd lambda-managed-instances-cdk-python
    ```

2. Create a Python virtual environment:
    ```bash
    python3 -m venv .venv
    ```

3. Activate the virtual environment:
    ```bash
    source .venv/bin/activate
    ```

    If you are in Windows platform, you would activate the virtualenv like this:

    ```
    % .venv\Scripts\activate.bat
    ```

4. Install python modules:
    ```bash
    python3 -m pip install -r requirements.txt
    ```

5. From the command line, use CDK to synthesize the CloudFormation template and check for errors:
    ```bash
    cdk synth
    ```

6. From the command line, use CDK to deploy the stack:
    ```bash
    cdk deploy
    ```

    Expected result:

    ```bash
    LambdaManagedInstancesPythonStack

    Outputs:
    LambdaManagedInstancesPythonStack.FunctionName = LambdaManagedInstancesPythonStack-MyLambdaFunction67CCA873-XXXXXXXXXXXXX
    LambdaManagedInstancesPythonStack.FunctionArn = arn:aws:lambda:us-east-1:xxxxxxxxxxxxx:function:my-managed-instance-function
    ```

7. Note the outputs from the CDK deployment process. These contain the resource names and ARNs which are used for testing.

## How it works

1. **Infrastructure Setup**: The CDK creates all necessary infrastructure including VPC, subnets, security groups, and IAM roles.

2. **Capacity Provider**: A Lambda capacity provider is created that manages EC2 instances in your VPC. This provider can scale up to 30 vCPUs based on demand.

3. **Lambda Function**: The Lambda function is configured to use the managed instances capacity provider instead of the standard serverless execution environment.

4. **Function Execution**: When invoked, the Lambda function runs on dedicated EC2 instances managed by the capacity provider, providing more control over the execution environment.

### Testing

Use the [AWS CLI](https://aws.amazon.com/cli/) to invoke the Lambda function and observe the execution on managed instances:

1. Invoke the Lambda function:
    ```bash
    aws lambda invoke \
      --function-name my-managed-instance-function \
      --payload '{"test": "data"}' \
      response.json
    ```

2. Check the response:
    ```bash
    cat response.json
    ```

    Expected result:
    ```json
    {
      "statusCode": 200,
      "body": "{\"message\":\"Hello from Lambda Managed Instances!\",\"event\":{\"test\":\"data\"}}"
    }
    ```

3. Retrieve the logs from the Lambda function:

    List the log streams for that log group:
    ```bash
    aws logs describe-log-streams --log-group-name '/aws/lambda/my-managed-instance-function' --query logStreams[*].logStreamName
    ```

    Expected result:
    ```bash
    [
        "2025/01/15/[$LATEST]6922e90439514d8195e455360917eaa9"
    ]
    ```

    Get the log events for that stream:
    ```bash
    aws logs get-log-events --log-group-name '/aws/lambda/my-managed-instance-function' --log-stream-name '2025/01/15/[$LATEST]6922e90439514d8195e455360917eaa9'
    ```

    Expected result:
    ```json
    {
        "events": [
            {
                "timestamp": 1639828317813,
                "message": "START RequestId: bd3f036b-3bf1-5300-8b05-595cf662119c Version: $LATEST\n",
                "ingestionTime": 1639828322765
            },
            {
                "timestamp": 1639828317815,
                "message": "Hello from Lambda Managed Instances!\n",
                "ingestionTime": 1639828322765
            },
            {
                "timestamp": 1639828317815,
                "message": "END RequestId: bd3f036b-3bf1-5300-8b05-595cf662119c\n",
                "ingestionTime": 1639828322765
            }
        ]
    }
    ```

## Cleanup

1. Delete the stack:
    ```bash
    cdk destroy
    ```

## Tutorial

See [this useful workshop](https://cdkworkshop.com/30-python.html) on working with the AWS CDK for Python projects.

## Useful commands

 * `cdk ls`          list all stacks in the app
 * `cdk synth`       emits the synthesized CloudFormation template
 * `cdk deploy`      deploy this stack to your default AWS account/region
 * `cdk diff`        compare deployed stack with current state
 * `cdk docs`        open CDK documentation

## Notes

- Lambda Managed Instances require VPC configuration and have different networking requirements compared to standard Lambda functions.
- The capacity provider manages EC2 instances automatically, scaling based on function invocation demand.
- This pattern is suitable for workloads that need more control over the execution environment or have specific networking requirements.


Enjoy!

----
Copyright 2025 Amazon.com, Inc. or its affiliates. All Rights Reserved.

SPDX-License-Identifier: MIT-0
