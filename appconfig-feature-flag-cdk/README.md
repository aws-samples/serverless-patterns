# AWS AppConfig Feature Flag to AWS Lambda with CDK

This pattern demonstrates how to build the AppConfig feature flag with CDK and how to use AppConfig extension for Lambda to retrive the feature flag status.

Learn more about this pattern at Serverless Land Patterns: https://serverlessland.com/patterns/appconfig-feature-flag-cdk

Important: this application uses various AWS services and there are costs associated with these services after the Free Tier usage - please see the [AWS Pricing page](https://aws.amazon.com/pricing/) for details. You are responsible for any AWS costs incurred. No warranty is implied in this example.

## Requirements

* [Create an AWS account](https://portal.aws.amazon.com/gp/aws/developer/registration/index.html) if you do not already have one and log in. The IAM user that you use must have sufficient permissions to make necessary AWS service calls and manage AWS resources.
* [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html) installed and configured
* [Git Installed](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)
* [Node and NPM](https://nodejs.org/en/download/) installed
* [AWS Cloud Development Kit](https://docs.aws.amazon.com/cdk/latest/guide/cli.html) (AWS CDK) installed

## Deployment Instructions

1. Create a new directory, navigate to that directory in a terminal and clone the GitHub repository:
    ``` 
    git clone https://github.com/aws-samples/serverless-patterns
    ```
1. Change directory to the pattern directory:
    ```
    cd appconfig-feature-flag-cdk
    ```
2. Run below command to install required dependancies:
    ```
    npm install && cd ./lambda && npm install && cd ./..
    ```
3. Before proceed:
    * Next command, you need to provide the correct AppConfig Lambda extension layer ARN sepcific to the region you are deploying the stack. Refer here to obtain the ARN for your region: https://docs.aws.amazon.com/appconfig/latest/userguide/appconfig-integration-lambda-extensions-versions.html#appconfig-integration-lambda-extensions-enabling-x86-64

4. From the command line, run:
    ```
    cdk deploy --all --parameters appConfigExtensionArn='[AppConfig Lambda extension layer ARN]'
    ```

## Testing

* Execute the Lambda function and you will see the AppConfig Feature Flag status output.

## Cleanup
 
1. To delete the stack, run:
    ```bash
    cdk destroy --all
    ```
----
Copyright 2022 Amazon.com, Inc. or its affiliates. All Rights Reserved.

SPDX-License-Identifier: MIT-0
