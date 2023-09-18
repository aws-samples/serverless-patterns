# Pinpoint SMS using API Gateway and Lambda

This pattern shows an example how a phone number can be validated and how a SMS message can be send using Pinpoint APIs which via API Gateway and Lambda deployed using SAM.  

As a pre-requisite, a Pinpoint Application has to be created and its SMS channel should be enabled. Subsequently, this stack can be deployed with pinpoint application id, destination phone number, message that has to be sent, origination number and message type. Please read more about the Pinpoint API calls utilised here:
https://docs.aws.amazon.com/pinpoint/latest/apireference/apps-application-id-messages.html#apps-application-id-messagespost

https://docs.aws.amazon.com/pinpoint/latest/apireference/phone-number-validate.html

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
    cd serverless-patterns/apigw-lambda-pinpoint
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

1. Depending on the country to which SMS messages has to be sent, an [origination number](https://docs.aws.amazon.com/pinpoint/latest/userguide/settings-sms-request-number.html) can be requested accordingly.

2. Next, the SMS message can be sent using the API Gateway deployed via stack.

3. The lambda function's code firstly verify the phone number by using the [phone number validate](https://docs.aws.amazon.com/pinpoint/latest/apireference/phone-number-validate.html) API call.

## Testing

1. You can make a request to API Gateway with the following payload:

```
{
    "destination_number": "",
    "message": "",
    "pinpoint_app_id": "",
    "origination_number": "",
    "message_type": ""
}
```
2. If the message is sent successfully, then you will receive the following response:

```
Message sent! Message ID: <random message id> 
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