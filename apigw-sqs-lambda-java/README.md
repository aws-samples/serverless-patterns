# AWS API Gateway HTTP APIs to Amazon SQS for buffering

In this pattern, called "Queue based leveling", a serverless queue is introduced between your API Gateway and your workers, a Lambda function in this case. 

The queue acts as a buffer to alleviate traffic spikes and ensure your workload can sustain the arriving load by buffering all the requests durably. It also helps downstream consumers to process the incoming requests at a consistent pace.

This version is a Java port of the [original pattern](https://github.com/aws-samples/serverless-patterns/apigw-sqs-lambda/).

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
    cd apigw-sqs-lambda-java
    ```
1. From the command line, use AWS SAM to deploy the AWS resources for the pattern as specified in the template.yml file:
    ```
    sam deploy --guided
    ```
1. During the prompts:
    * Enter a stack name
    * Enter the desired AWS Region
    * Allow SAM CLI to create IAM roles with the required permissions.

    Once you have run `sam deploy --guided` mode once and saved arguments to a configuration file (samconfig.toml), you can use `sam deploy` in future to use these defaults.

1. Note the outputs from the SAM deployment process. These contain the resource names and/or ARNs which are used for testing.

## How it works

The API Gateway handles incoming requests, but instead of invoking the Lambda function directly, it stores them in an SQS queue which serves as a buffer. The Lambda functions (workers) can now process the requests in a batch manner (10 requests at a time).

## Testing

Run the following command to send an HTTP `POST` request to the HTTP APIs endpoint. Note, you must edit the {MyHttpAPI} placeholder with the URL of the deployed HTTP APIs endpoint. This is provided in the stack outputs.

```bash
curl --location --request POST '{MyHttpAPI}/submit'
> --header 'Content-Type: application/json' \
> --data-raw '{ "isMessageReceived": "Yes" }'
```
Then open SQSLambdaFunction logs on Cloudwatch to notice a log that resembles to the message bellow, which means the message has gone through API Gateway, was pushed to SQS and then consumed by the Lambda function:

```
START RequestId: b311ef02-6f8e-5e09-b755-b5bb8ef2ecec Version: $LATEST
{
    "isMessageReceived": "Yes"
}
END RequestId: b311ef02-6f8e-5e09-b755-b5bb8ef2ecec
REPORT RequestId: b311ef02-6f8e-5e09-b755-b5bb8ef2ecec	Duration: 38.12 ms	Billed Duration: 39 ms	Memory Size: 512 MB	Max Memory Used: 85 MB	Init Duration: 512.08 ms
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
Copyright 2022 Amazon.com, Inc. or its affiliates. All Rights Reserved.

SPDX-License-Identifier: MIT-0
