# AWS Step Functions to AWS Lambda or Amazon ECS

This pattern creates an AWS Step Function, AWS Lambda function and an Amazon ECS Fargate task. The state machine can then invoke either. The template creates all the required networking and uses VPC endpoints instead of Nat Gateways for the Fargate networking requirements.

Learn more about this pattern at Serverless Land Patterns: https://serverlessland.com/patterns/stepfunction-fargate-lambda

Important: this application uses various AWS services and there are costs associated with these services after the Free Tier usage - please see the [AWS Pricing page](https://aws.amazon.com/pricing/) for details. You are responsible for any AWS costs incurred. No warranty is implied in this example.

## Requirements

* [Create an AWS account](https://portal.aws.amazon.com/gp/aws/developer/registration/index.html) if you do not already have one and log in. The IAM user that you use must have sufficient permissions to make necessary AWS service calls and manage AWS resources.
* [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html) installed and configured
* [Git Installed](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)
* [AWS Serverless Application Model](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-sam-cli-install.html) (AWS SAM) installed

## Deployment Instructions

### Application stack

1. Create a new directory, navigate to that directory in a terminal and clone the GitHub repository:
    ``` 
    git clone https://github.com/aws-samples/serverless-patterns
    ```
1. Change directory to the pattern directory:
    ```
    cd stepfunction-fargate-lambda
    ```
1. From the command line, use AWS SAM to deploy the AWS resources for the pattern as specified in the template.yaml file:
    ```
    sam deploy --guided
    ```
1. During the prompts:
    * Enter a stack name
    * Enter the desired AWS Region
    * Allow SAM CLI to create IAM roles with the required permissions.

    Once you have run `sam deploy --guided` mode once and saved arguments to a configuration file (samconfig.toml), you can use `sam deploy` in future to use these defaults.

1. Note the outputs from the SAM deployment process. These contain the resource names and/or ARNs which are used for testing.

### Container image
The stack creates a new ECR container repo and outputs the repo in the stack outputs. Refer to the repo direction to deploy the container image. Run the Docker commands from within the `fargate` folder.

## How it works

When a new file is uploaded to the bucket, the Step Function invokes to process the file. Based on the file type, the Step Function will invoke either the Lambda function for image jobs or the Fargate task for video jobs.

## Testing

Upload either an image or video to the created bucket. Images should go in a folder called `images` and videos go in a folder called `videos`. The step function will then invoke either the Lambda function or the ECS Fargate task. Both will simply return a hello world and submit the successful completion token task to the Step Function.
* Image: `aws s3 cp ./my/image/file s3:bucket-name/images/`
* Video: `aws s3 cp ./my/video/file s3:bucket-name/videos/`

## Cleanup
 
Delete the stack
```bash
sam delete --stack-name STACK_NAME
```
----
Copyright 2023 Amazon.com, Inc. or its affiliates. All Rights Reserved.

SPDX-License-Identifier: MIT-0
