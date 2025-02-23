# AWS API Gateway to AWS SQS

This pattern creates REST API Gateway that directly integrate with AWS SQS.

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
    cd _patterns-model
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

This pattern creates an Amazon API gateway REST API endpoint. The endpoint uses service integrations to directly connect to Amazon SQS that reads messages from the SQS.
Users can simply call the GET Method of invoke URL( API Gateway) that is returned as part of the Stack Output.
Invoke URL can also be used with query string parameters like MaxNumberOfMessages=5 VisibilityTimeout=15 AttributeName=All to get the desired output.

## Testing

Sending a new test message to API Gateway endpoint

To test the endpoint first send data using the following command. Be sure to update the endpoint with endpoint of your stack.
```
curl --location --request GET 'ApiEndpoint output value'
```
OR
```
curl --location --request GET '{ApiEndpoint output value}?MaxNumberOfMessages=5&VisibilityTimeout=15&AttributeName=All'
```

## Expected Output:

```
{"ReceiveMessageResponse":{"ReceiveMessageResult":{"messages":null},"ResponseMetadata":{"RequestId":"RequestId"}}}
```

```
{"ReceiveMessageResponse":{"ReceiveMessageResult":{"messages":[{"Attributes":null,"Body":"messageBody","MD5OfBody":"MD5OfBody","MD5OfMessageAttributes":null,"MessageAttributes":null,"MessageId":"Queue Message ID","ReceiptHandle":"ReceiptHandle"}]},"ResponseMetadata":{"RequestId":"requestID"}}}
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
Copyright 2024 Amazon.com, Inc. or its affiliates. All Rights Reserved.

SPDX-License-Identifier: MIT-0
