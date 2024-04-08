# AWS API Gateway Private API to AWS Lambda

This pattern creates an Amazon API Gateway Private rest API with an AWS Lambda function integration.

Learn more about this pattern at Serverless Land Patterns: https://serverlessland.com/patterns/apigw-private-lambda

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
    cd apigw-private-lambda 
    ```
1. From the command line, use AWS SAM to deploy the AWS resources for the pattern as specified in the template.yml file:
    ```
    sam deploy --guided
    ```
1. During the prompts:
    * Enter a stack name
    * Enter a VPC endpoint
    * Allow SAM CLI to create IAM roles with the required permissions.

    Once you have run `sam deploy --guided` mode once and saved arguments to a configuration file (samconfig.toml), you can use `sam deploy` in future to use these defaults.

1. Note the outputs from the SAM deployment process. These contain the resource names and/or ARNs which are used for testing.

## How it works

This pattern deploys an Amazon API Gateway Private API with a Lambda integration. The AWS Lambda function is written in Python3.9. The function returns a small message and a status code to the caller.

The private API is created with a resource policy allowing invocations only from a specified VPC endpoint. This VPC endpoint is entered in the paramaters of the template. 


## Testing

To create the private API you need to already have in your environment :
* a VPC with an internet gateway
* a public subnet with a NAT and an EC2 instance
* a Security Group that allows port 443 from anywhere
* a VPC Endpoint for execute-api associated with the private subnet, the security group and with Private DNS names ENABLED
     * see how to create a VPC here -> https://docs.aws.amazon.com/vpc/latest/userguide/what-is-amazon-vpc.html
    * see how to create a VPC Endpoint for APIs here -> https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-private-apis.html#apigateway-private-api-create-interface-vpc-endpoint

To be able to invoke a private API you need to :
* Log into an instance that is in the same VPC and subnet as your VPC Endpoint and in the same security group or which security group is allowed to make requests to the Enpoint's security group
* see how to invoke a private API here -> https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-private-api-test-invoke-url.html
* On the instance, open a terminal and execute the curl command
Eg : 
```bash
curl https://aabbccddee.execute-api.eu-west-1.amazonaws.com/Prod/get
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
Copyright 2023 Amazon.com, Inc. or its affiliates. All Rights Reserved.

SPDX-License-Identifier: MIT-0
