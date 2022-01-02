# AWS IoT rule with custom authorizer to SQS

This SAM template deploys resources needed to send iot events to IoT Core service to forward these events through an IoT Rule to SQS Queue with bring-your-own custom authozier for device authentication.

## Requirements

* [Create an AWS account](https://portal.aws.amazon.com/gp/aws/developer/registration/index.html) if you do not already have one and log in. The IAM user that you use must have sufficient permissions to make necessary AWS service calls and manage AWS resources.
* [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html) installed and configured
* [Git Installed](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)
* [AWS Serverless Application Model](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-sam-cli-install.html) (AWS SAM) installed
* [Node and NPM](https://nodejs.org/en/download/) installed

## Deployment Instructions

1. Create a new directory, navigate to that directory in a terminal and clone the GitHub repository:
    ``` 
    git clone https://github.com/aws-samples/serverless-patterns
    ```
1. Change directory to the pattern directory:
    ```
    cd iot-mqttoverhttp-customauth
    ```
1. From the command line, use AWS SAM to deploy the AWS resources for the pattern as specified in the template.yml file:
    ```
    sam deploy --guided --capabilities CAPABILITY_NAMED_IAM CAPABILITY_NAMED_IAM 
    ```
1. During the prompts:
    * Enter a stack name
    * Enter the desired AWS Region
    * Allow SAM CLI to create IAM roles with the required permissions.
    * Enter VPC Id
    * Enter Subnet Id

    Once you have run `sam deploy --guided --capabilities CAPABILITY_NAMED_IAM CAPABILITY_NAMED_IAM` mode once and saved arguments to a configuration file (samconfig.toml), you can use `sam deploy --guided --capabilities CAPABILITY_NAMED_IAM CAPABILITY_NAMED_IAM` in future to use these defaults.

1. Note the outputs from the SAM deployment process. These contain the resource names and/or ARNs which are used for testing.

## How it works

Explain how the service interaction works.

## Testing

Use your choise of http client for testing against this endpoint: POST ${IoT Core Data Endpoint}/topics/$aws/rules/device_events with json body (any json data that your device would have sent) and http header 'x-amz-customauthorizer-name: anonymous-authorizer'.

1. where to find IoT core data endpoint
    * go to AWS IoT Core console
    * click on settings on the left panel
    * you will find Endpoint under "Device Data Endpoint section
2. Test example: curl -X POST -v -H 'x-amz-customauthorizer-name: anonymous-authorizer' https://<replace with your iot data endpoint>topics/$aws/rules/device_events

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
