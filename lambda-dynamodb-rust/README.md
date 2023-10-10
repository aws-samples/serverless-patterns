# AWS Lambda To Amazon DynamoDB

The SAM template deploys a Lambda function, a DynamoDB table and the minimum IAM resources required to run the application. 

Learn more about this pattern at Serverless Land Patterns: https://serverlessland.com/patterns/lambda-dynamodb-rust

Important: this application uses various AWS services and there are costs associated with these services after the Free Tier usage - please see the [AWS Pricing page](https://aws.amazon.com/pricing/) for details. You are responsible for any AWS costs incurred. No warranty is implied in this example.

## Requirements

* [Create an AWS account](https://portal.aws.amazon.com/gp/aws/developer/registration/index.html) if you do not already have one and log in. The IAM user that you use must have sufficient permissions to make necessary AWS service calls and manage AWS resources.
* [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html) installed and configured
* [Git Installed](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)
* [AWS Serverless Application Model](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-sam-cli-install.html) (AWS SAM) installed
* [Rust](https://www.rust-lang.org/) 1.56.0 or higher
* [cargo-zigbuild](https://github.com/messense/cargo-zigbuild) and [Zig](https://ziglang.org/) for cross-compilation

## Deployment Instructions

1. Create a new directory, navigate to that directory in a terminal and clone the GitHub repository:
    ``` 
    git clone https://github.com/aws-samples/serverless-patterns
    ```
2. Change directory to the pattern directory:
    ```
    cd lambda-dynamodb-rust
    ```
3. Install dependencies and build:
    ```
    make build
    ```
4. From the command line, use AWS SAM to deploy the AWS resources for the pattern as specified in the template.yml file:
    ```
    make deploy
    ```
5. During the prompts:
    * Enter a stack name
    * Enter the desired AWS Region
    * Allow SAM CLI to create IAM roles with the required permissions.

    Once you have run `sam deploy -guided` mode once and saved arguments to a configuration file (samconfig.toml), you can use `sam deploy` in future to use these defaults.

6. Note the outputs from the SAM deployment process. These contain the resource names and/or ARNs which are used for testing.

## How it works

* A Lambda function is invoked by an event integration or CLI command
* The Lambda function "stringifies" the event payload
* The Function uses the AWS SDK to perform a `put` command on a DynamoDB table 
* The name of the DynamoDB table is passed to the Lambda function via an environment variable named `DatabaseTable`
* The Lambda function is granted `PutItem` permissions, defined in the `LambdaExecRole` IAM Role.

## Testing

Run the following Lambda CLI invoke command to invoke the function. Note, you must edit the {LambdaPutDynamoDBArn} placeholder with the ARN of the deployed Lambda function. This is provided in the stack outputs.

```bash
aws lambda invoke --function-name {LambdaPutDynamoDBArn} --invocation-type Event \
--payload '{ "Metadata": "Hello" }' \ response.json --cli-binary-format raw-in-base64-out  
```

## Cleanup
 
1. Delete the stack
    ```bash
    make delete
    ```
2. Confirm the stack has been deleted
    ```bash
    aws cloudformation list-stacks --query "StackSummaries[?contains(StackName,'STACK_NAME')].StackStatus"
    ```
----
Copyright 2021 Amazon.com, Inc. or its affiliates. All Rights Reserved.

SPDX-License-Identifier: MIT-0
