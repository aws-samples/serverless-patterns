# Lambda function for Node.js using TypeScript with ES modules and ESBuild

This pattern allows you to create a Lambda function for Node.js using TypeScript and CDK. The function is set up for using EcmaScript modules and generate a bundle with minification and tree-shaking active.
This template speeds up the creation of a Lambda function with TypeScript including everything properly configured for leverage the capabilities of ESM such as dynamic imports and top-level await for optimizing your Lambda functions.

Learn more about this pattern at Serverless Land Patterns: https://serverlessland.com/patterns/lambda-node-esm-cdk

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
    cd lambda-node-esm-cdk
    ```
1. From the command line, use AWS CDK to deploy the AWS resources for the pattern as specified in the bin/node-esm.ts file:
    ```
    cdk deploy
    ```
1. During the prompts:
    * Confirm you are provisioning the infrastructure needed to create the Lambda function

1. Note the outputs from the CDK deployment process. These contain the API Gateway URL to invoke the Lambda function

## Testing

1. You can test the solution by accessing the Lambda console, finding the Lambda function, and clicking Test in the Code Source section.

1. Create a new test event and supply the example event

1. You can also invoke the function from the CLI using ```curl``` or ```wget``` + the API endpoint you can find in the output of the CDK deploy command

## Cleanup
 
1. Delete the stack
    ```bash
    cdk destroy
    ```

Copyright 2023 Amazon.com, Inc. or its affiliates. All Rights Reserved.

SPDX-License-Identifier: MIT-0