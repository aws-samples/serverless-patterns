
# Amazon SQS to Amazon DynamoDB

This pattern deploys a SQS Queue, a Lambda Function and a DynamoDB allowing batch writes from SQS messages to a DynamoDb Table. The CDK application contains the minimum IAM resources required to run the application.

Learn more about this pattern at: https://serverlessland.com/patterns/sqs-lambda-ddb-cdk

Important: this application uses various AWS services and there are costs associated with these services after the Free Tier usage - please see the AWS Pricing page for details. You are responsible for any AWS costs incurred. No warranty is implied in this example.

## Requirements

* [Create an AWS account](https://portal.aws.amazon.com/gp/aws/developer/registration/index.html) if you do not already have one and log in. The IAM user that you use must have sufficient permissions to make necessary AWS service calls and manage AWS resources.
* [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html) installed and configured
* [Git Installed](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)
* [AWS Cloud Development Kit](https://docs.aws.amazon.com/cdk/latest/guide/getting_started.html) (AWS CDK >= 1.124.0) Installed

## Language
Python

## Framework
CDK

## Services From/To
Amazon SQS to AWS Lambda to Amazon DynamoDb

## Deployment Instructions

1. Create a new directory, navigate to that directory in a terminal and clone the GitHub repository:
    ```bash
    git clone https://github.com/aws-samples/serverless-patterns
    ```
1. Change directory to the pattern directory:
    ```bash
    cd sqs-lambda-dynamodb-cdk
    ```
1. Create a virtual environment for python:
    ```bash
    python3 -m venv .venv
    ```
1. Activate the virtual environment:
    ```bash
    source .venv/bin/activate
    ```

    If you are in Windows platform, you would activate the virtualenv like this:

    ```
    % .venv\Scripts\activate.bat
    ```

1. Install python modules:
    ```bash
    python3 -m pip install -r requirements.txt
    ```
1. From the command line, use CDK to synthesize the CloudFormation template and check for errors:
    ```bash
    cdk synth
    ```
1. From the command line, use CDK to deploy the stack:
    ```bash
    cdk deploy
    ```
1. Note the outputs from the CDK deployment process. These contain the resource names and/or ARNs which are used for testing.

1. Run unit tests:

    ````bash
    python3 -m pytest
    ````


## How it works

The CDK stack deploys the resources and the IAM permissions required to run the application.

The SQS Queue specified in the stack vsam_to_dynamo_stack.py has a Lambda Function responding to the events. The function extracts the body from the message payload and performs a batch write in DynamoDB. The body content must comply with json format expected by DynamoDb (see example below). Messages containing more than 25 itens are not processed by dynamodb.batch_write() as it is limited by DynamoDB.

```
{"CLIENT": [
{
    "PutRequest": {
        "Item": {
            "CLIENT-KEY": {
                "S": "1|0"
            },
            "CLIENT-NAME": {
                "S": "ALBERT EINSTEIN"
            },
            "CLIENT-RECORD-COUNT": {
                "N": "220"
            },
            "FILLER_3": {
                "S": ""
            }
        }
    }
}
,{
    "PutRequest": {
        "Item": {
            "CLIENT-KEY": {
                "S": "1|1"
            },
            "CLIENT-NAME": {
                "S": "HERBERT MOHAMED"
            },
            "CLIENT-BDATE": {
                "S": "1958-08-31"
            },
            "CLIENT-ED-LVL": {
                "S": "BACHELOR"
            },
            "CLIENT-INCOME": {
                "N": "0010000.00"
            },
            "FILLER_1": {
                "S": ""
            }
        }
    }
}
]}
```


## Testing

Tests can be done using aws-cli or directly on the console. Follow the steps below to test from the command line. A file containing a payload with sample records has been provided in the project's root folder, example-message.json.

1. After sucessfully deploying the stack, get the SQS Queue url:

````
aws sqs get-queue-url --queue-name VsamToDynamoQueue
````

Response
````
{
    "QueueUrl": "https://sqs.<your region>.amazonaws.com/<your account>/VsamToDynamoQueue"
}
````

2. Send a message to the queue passing the example file as the message-body parameter value:

````
aws sqs send-message --queue-url <Replace by QueueUrl value> --message-body file://example-message.json
````

3. Scan your table to confirm that items have been recorded:

````
aws dynamodb scan --table-name CLIENT
````

## Cleanup

1. Delete the stack
    ```bash
    aws cloudformation delete-stack --stack-name STACK_NAME
    ```
1. Confirm the stack has been deleted
    ```bash
    aws cloudformation list-stacks --query "StackSummaries[?contains(StackName,'STACK_NAME')].StackStatus"
    ```



## Tutorial
See [this useful workshop](https://cdkworkshop.com/30-python.html) on working with the AWS CDK for Python projects.

## Useful commands

 * `cdk ls`          list all stacks in the app
 * `cdk synth`       emits the synthesized CloudFormation template
 * `cdk deploy`      deploy this stack to your default AWS account/region
 * `cdk diff`        compare deployed stack with current state
 * `cdk docs`        open CDK documentation


Enjoy!
