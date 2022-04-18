# AWS Lambda to Amazon SQS

This version is a Java port of the [original pattern](https://serverlessland.com/patterns/lambda-sqs/)

The SAM template deploys a Lambda function, an SQS queue and the IAM permissions required to run the application. The Lambda function publishes a message to the SQS queue when invoked.

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
    cd lambda-sqs-java
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

## Example payload from SQS

```
{                                                                                                                   
    "Messages": [
        {
            "MessageId": "12345678-876d-41f7-b32c-1234567890",
            "ReceiptHandle": "AQEBZfn1234567890O78Kn0C1234567890/z1+1234567890f2bQYOvD9RL1234567890Srr7+XQ/U1234567890j7nL+uaDVnJL1234567890mASoiwI/yQ1234567890gv/h17BW12345678908Pry0JM1234567890DfHE1g1234567890aMisj1234567890M+rC+ZF21234567890QdQpEwrX01234567890Fw6w2+Po0OA1234567890DkKgGuEmebp1234567890w7nNXujzSnzIXj1234567890CqfDOb2D1234567890kCk841+01234567890OaYzXV1234567890C+ruRXj1234567890AR5+vj8+U1234567890SJplJLjd1234567890YWV8o1234567890gJXb12345678901234567890",
            "MD5OfBody": "1234567890eb64e60d1234567890",
            "Body": "Message at 2022-04-13T10:25:33.466804Z"
        }
    ]
}

```

### Testing

Use the [AWS CLI](https://aws.amazon.com/cli/) to invoke the Lambda function. The function name is in the outputs of the AWS SAM deployment (the key is `QueuePublisherFunction`):

1. Invoke the Lambda function to publish a message to the SQS queue:

```bash
aws lambda invoke --function-name ENTER_YOUR_FUNCTION_NAME response.json
```
2. Retrieve the message from the SQS queue, using the queue URL from the AWS SAM deployment outputs:
```bash
aws sqs receive-message --queue-url ENTER_YOUR_QUEUE_URL
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
