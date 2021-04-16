# AWS API Gateway HTTP APIs to Amazon SQS for buffering

In this pattern, called "Queue based leveling", a serverless queue is introduced between your API Gateway and your workers, a Lambda function in this case. 

The queue acts as a buffer to alleviate traffic spikes and ensure your workload can sustain the arriving load by buffering all the requests durably. It also helps downstream consumers to process the incoming requests at a consistent pace.

Learn more about this pattern at Serverless Land Patterns: https://serverlessland.com/patterns/apigw-sqs.

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
    cd apigw-sqs-lambda
    ```
1. From the command line, use AWS SAM to deploy the AWS resources for the pattern as specified in the template.yml file:
    ```
    sam deploy --guided
    ```
1. During the prompts:
    * Enter a stack name
    * Enter the desired AWS Region
    * Allow SAM CLI to create IAM roles with the required permissions.

    Once you have run `sam deploy -guided` mode once and saved arguments to a configuration file (samconfig.toml), you can use `sam deploy` in future to use these defaults.

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
Then open MyLambdaFunction logs on Cloudwatch to notice a log that resembles to the message bellow, which mean the message has gone through API Gateway, was pushed to SQS and then consumed by the Lambda function:

```
{
    "Records": [
        {
            "messageId": "93ba6855-2690-4d17-80ef-585f47d151fc",
            "receiptHandle": "AQEBi1vefmNSdKdMtCwr33eV/GekQLpsZ6IfFJLQ5DHAyfbDGvY1VvoqMOEF34YIm42XjZO0GDDYPNQ66xA+ax8hdHUchIrMx3PJfkQaQAxQfkGw0SbQx3wchw8gtIqJ+RDz4QFyWjKoeXwJTv",
            "body": "{ \"isMessageReceived\": \"Yes\" }",
            "attributes": {
                "ApproximateReceiveCount": "1",
                "SentTimestamp": "1617397503139",
                "SenderId": "AROASDEO2NWPIG5WZAP3F:1617397503105006814",
                "ApproximateFirstReceiveTimestamp": "1617397503146"
            },
            "messageAttributes": {},
            "md5OfBody": "b62a98ce622eeb04548425913fb29789",
            "eventSource": "aws:sqs",
            "eventSourceARN": "arn:aws:sqs:us-east-1:144180931998:MySqsQueue",
            "awsRegion": "us-east-1"
        }
    ]
}
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
Copyright 2021 Amazon.com, Inc. or its affiliates. All Rights Reserved.

SPDX-License-Identifier: MIT-0
