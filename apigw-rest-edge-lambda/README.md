# AWS API Gateway REST Edge-Optimized API to AWS Lambda

This pattern creates an Amazon API Gateway REST Edge-Optimized API with an AWS Lambda function integration.

Learn more about this pattern at Serverless Land Patterns: https://serverlessland.com/patterns/apigw-edge-optimized-lambda-sam

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
2. Change directory to the pattern directory:
    ```
    cd apigw-rest-edge-lambda
    ```
3. From the command line, use AWS SAM to deploy the AWS resources for the pattern as specified in the template.yml file:
    ```
    sam deploy --guided
    ```
4. During the prompts:
    * Enter a stack name
    * Enter the desired AWS Region
    * Allow SAM CLI to create IAM roles with the required permissions.

    Once you have run `sam deploy --guided` mode once and saved arguments to a configuration file (samconfig.toml), you can use `sam deploy` in future to use these defaults.

5. Note the output from the SAM deployment process. It contains the API endpoint.

## How it works

This pattern deploys an Amazon API Gateway Rest Edge-Optimized API with a Lambda integration. The AWS Lambda function is written in Python3.9. The function returns a small message and a status code to the caller.

## Testing

Once the application is deployed, retrieve the API URL provided as output and open it in a new page on the browser. You can also make the request from Postman or from a terminal. The URL should look like this : https://[api-id].execute-api.[api-region].amazonaws.com/

Example
    ```bash
    https://aabbccddee.execute-api.eu-west-1.amazonaws.com/
    ```

OR open a terminal and execute the curl command

Example
    ```bash
    curl https://aabbccddee.execute-api.eu-west-1.amazonaws.com/
    ```
The expected response is : 'Hello World! This is the Edge-Optimized API'


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
Copyright 2023 Amazon.com, Inc. or its affiliates. All Rights Reserved.

SPDX-License-Identifier: MIT-0
