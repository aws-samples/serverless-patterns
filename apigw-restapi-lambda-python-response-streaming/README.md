# Amazon Gateway REST API to AWS Lambda Python function

This pattern demonstrates how to use an Amazon API Gateway REST API with response streaming to a Python Lambda function.
This template includes an response streaming enabled Amazon API Gateway REST API that invokes a Python Lambda function
that uses Lambda Web Adaptor with Fast API to enable response streaming.

Learn more about this pattern at Serverless Land Patterns: << Add the live URL here >>

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
    cd apigw-restapi-lambda-python-response-streaming
    ```
1. From the command line, use AWS SAM to deploy the AWS resources for the pattern as specified in the template.yml file:
    ```
    sam deploy --guided
    ```
1. During the prompts:
    * Enter a stack name
    * Enter the desired AWS Region
    * Allow SAM CLI to create IAM roles with the required permissions
    * Allow API Gateway API without any authentication

    Once you have run `sam deploy --guided` mode once and saved arguments to a configuration file (samconfig.toml), you can use `sam deploy` in future to use these defaults.

1. Note the outputs from the SAM deployment process. These contain the resource names and/or ARNs which are used for testing.

## How it works

Response streaming allows you to incrementally stream responses back to clients rather than waiting for the entire response to be buffered first, reducing Time to First Byte, and making your applications more responsive to users. [Amazon API Gateway REST APIs support response streaming](https://aws.amazon.com/blogs/compute/building-responsive-apis-with-amazon-api-gateway-response-streaming/).
[AWS Lambda supports response streaming natively for Nodejs](https://aws.amazon.com/blogs/compute/introducing-aws-lambda-response-streaming/) (native support for [Python in the Lambda roadmap](https://github.com/orgs/aws/projects/286/views/1?pane=issue&itemId=129507898&issue=aws%7Caws-lambda-roadmap%7C39)), so to enable response streaming with a Python Lambda function, we use [Lambda Web Adaptor](https://aws.amazon.com/blogs/compute/using-response-streaming-with-aws-lambda-web-adapter-to-optimize-performance/) and [Fast API](https://github.com/awslabs/aws-lambda-web-adapter/tree/main/examples/fastapi-response-streaming-zip). The Lambda function takes the topic from the API Gateway request, and sends a request to Bedrock, using the `InvokeModelWithResponseStream` call, to generate a bedtime story for that topic. 

## Testing

To test response streaming, you can call the API Gateway REST API URL included in the SAM output. You may use `curl` with the `no-buffer` parameter to send in a topic, to which you will receive a bedtime story for. E.g. 
```
curl --no-buffer --json '{"topic":"response streaming with AWS serverless"}' https://<abc123.execute-api.us-eas>t-1.amazonaws.com/prod/story
```

## Cleanup
 
1. Delete the stack
    ```bash
    sam delete
    ```
1. Confirm the stack has been deleted
    ```bash
    aws cloudformation list-stacks --query "StackSummaries[?contains(StackName,'STACK_NAME')].StackStatus"
    ```
----
Copyright 2025 Amazon.com, Inc. or its affiliates. All Rights Reserved.

SPDX-License-Identifier: MIT-0
