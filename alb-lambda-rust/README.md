# Amazon API Gateway REST API to AWS Lambda

This pattern creates an Application Load Balancer and an AWS Lambda function as target.

Learn more about this pattern at [Serverless Land Patterns](https://serverlessland.com/patterns/alb-lambda-rust).

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
    cd alb-lambda-rust
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

This pattern deploys an Application Load Balancer with an AWS Lambda function written in Rust as target. The function logs the incoming API event and context object to an Amazon CloudWatch Logs log group and returns basic information about the event to the caller.

## Testing

Once the application is deployed, retrieve the Application Load Balancer endpoint value from CloudFormation Outputs. Either use the console or call the endpoint from Postman.

```
curl -X POST -H "content-type:application/json" http://{ALB_ID}.{REGION}.elb.amazonaws.com  -d '{"prop1": "Hello","prop2": "World"}'
```

Response:
```
{
    "message": "Hello World",
    "payload": {
        "prop1": "Hello",
        "prop2": "World"
    }
}
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