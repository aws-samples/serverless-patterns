# AWS Lambda to AWS IoT Core

This pattern deploys an AWS Lambda function, which publishes a message to an AWS IoT Core topic. The topic is watched by a rule which will trigger an action when the condition is met. The action calls an AWS Lambda function.

Learn more about this pattern at Serverless Land Patterns: << Add the live URL here >>

Important: this application uses various AWS services and there are costs associated with these services after the Free Tier usage - please see the [AWS Pricing page](https://aws.amazon.com/pricing/) for details. You are responsible for any AWS costs incurred. No warranty is implied in this example.

## Requirements

* [Create an AWS account](https://portal.aws.amazon.com/gp/aws/developer/registration/index.html) if you do not already have one and log in. The IAM user that you use must have sufficient permissions to make necessary AWS service calls and manage AWS resources.
* [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html) installed and configured
* [Git Installed](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)
* [AWS Cloud Development Kit (AWS CDK) installed](https://docs.aws.amazon.com/cdk/v2/guide/getting_started.html)

## Architecture diagram
![Architecture diagram](./doc/architecture-diagram.png)

## Deployment Instructions

1. Create a new directory, navigate to that directory in a terminal and clone the GitHub repository:
    ``` 
    git clone https://github.com/aws-samples/serverless-patterns
    ```
1. Change directory to the pattern directory:
    ```
    cd iot-lambda-pub-receiver-cdk
    ```
1. Install dependencies
    ```bash
    npm install
    ```
1. From the command line, use AWS SAM to deploy the AWS resources for the pattern as specified in the template.yml file:
    ```
    cdk deploy
    ```

2. Note the outputs from the CDK deployment process. These contain the IoT endpoint address which is not relevant if you have only one account. However, in multi-accounts deployment, especially when the IoT resources are not in the same as the lambdas, then the endpoint address has to be specified in the functions' code.

## How it works

Explain how the service interaction works.

## Testing

Provide steps to trigger the integration and show what should be observed if successful.

## Cleanup
 
Run the given command to delete the resources that were created. It might take some time for the CloudFormation stack to get deleted.
```bash
cdk destroy
```
    ```
----
Copyright 2024 Amazon.com, Inc. or its affiliates. All Rights Reserved.

SPDX-License-Identifier: MIT-0
