# Amazon API Gateway HTTP API to AWS Simple Queue Service (SQS) to Lambda

This pattern creates an Amazon API Gateway HTTP API with a ```send``` route that send message to a SQS queue. The  Amazon API Gateway HTTP API has basic CORS configured. Upon receiving message, SQS will trigger a Lambda function to process the message. The function will only ```print``` the message only. The function written in Python.

Learn more about this pattern at Serverless Land Patterns: https://serverlessland.com/patterns/apigw-http-sqs-lambda-cdk

Important: this application uses various AWS services and there are costs associated with these services after the Free Tier usage - please see the [AWS Pricing page](https://aws.amazon.com/pricing/) for details. You are responsible for any AWS costs incurred. No warranty is implied in this example.

## Requirements

* [Create an AWS account](https://portal.aws.amazon.com/gp/aws/developer/registration/index.html) if you do not already have one and log in. The IAM user that you use must have sufficient permissions to make necessary AWS service calls and manage AWS resources.
* [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html) installed and configured
* [Git Installed](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)
* [AWS Cloud Development Kit](https://docs.aws.amazon.com/cdk/latest/guide/cli.html) (AWS CDK) installed
* [Python 3.8+](https://www.python.org/downloads/) Installed

## Deployment Instructions

1. Create a new directory, navigate to that directory in a terminal and clone the GitHub repository:
    ``` 
    git clone https://github.com/aws-samples/serverless-patterns
    ```
1. Change directory to the pattern directory:
    ```
    cd apigw-http-api-sqs-lambda-cdk
    ```
1. Create virtualenv
    ```
    python3 -m venv .venv
    ```
1. Activate your virtualenv.
    ```
    source .venv/bin/activate
    ```
1. Once the virtualenv is activated, you can install the required dependencies.
    ```
    pip install -r requirements.txt
    ```
1. At this point you can now synthesize the CloudFormation template for this code.
    ```
    cdk synth
    ```

    ## Useful CDK commands

    * `cdk ls`          list all stacks in the app
    * `cdk synth`       emits the synthesized CloudFormation template
    * `cdk deploy`      deploy this stack to your default AWS account/region
    * `cdk diff`        compare deployed stack with current state
    * `cdk docs`        open CDK documentation

1. Deploy CDK stack
    ```
    cdk deploy
    ```


## How it works

The API Gateway handles the incoming API requests and send the ```$request.body.MessageBody``` as a message to SQS queue. A Lambda function will be trigger upon the message arraived.

## Testing

### Running following cURL command to agaist the HTTP API Endpoint
```
curl -XPOST https://${HTTP_API_ENDPOOINT}/send -d'{"MessageBody":"hello"}'
```
### Expected result
```
<?xml version="1.0"?><SendMessageResponse xmlns="http://queue.amazonaws.com/doc/2012-11-05/">
    <SendMessageResult>
        <MessageId>xxxxxx</MessageId>
        <MD5OfMessageBody>xxxxxx</MD5OfMessageBody>
    </SendMessageResult>
    <ResponseMetadata>
        <RequestId>xxxx</RequestId>
    </ResponseMetadata>
</SendMessageResponse>
```
# Cleanup

```
cdk destroy
```

----
Copyright 2021 Amazon.com, Inc. or its affiliates. All Rights Reserved.

SPDX-License-Identifier: MIT-0
