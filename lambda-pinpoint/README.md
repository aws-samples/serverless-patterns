# Lambda to Pinpoint

This pattern demonstrates a Lambda function sending SMS via Pinpoint. Deploying the pattern will create 1 Lambda function and 1 Pinpoint project.

Learn more about this pattern at Serverless Land Patterns: https://serverlessland.com/patterns/lambda-pinpoint

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
2. Change directory to the pattern directory:
    ```
    cd lambda-pinpoint
    ```
3. From the command line, use AWS SAM to deploy the AWS resources for the pattern as specified in the template.yml file:
    ```
    sam deploy --guided
    ```
4. During the prompts:
    * Enter a stack name
    * Enter the desired AWS Region
    * Allow SAM CLI to create IAM roles with the required permissions.

    Once you have run `sam deploy --guided` mode once and saved arguments to a configuration file (samconfig.toml), you can use `sam deploy` in future to use these defaults.

5. Note the outputs from the SAM deployment process. These contain the resource names and/or ARNs which are used for testing.

## How it works

1. Request an origination number from Pinpoint after the stack is deployed. See [instructions](https://docs.aws.amazon.com/pinpoint/latest/userguide/settings-sms-request-number.html)
2. If you're using Pinpoint for the first time, your account is sandboxed and can only send messages to verified destination numbers. See [instructions](https://docs.aws.amazon.com/pinpoint/latest/userguide/channels-sms-sandbox.html) on verifying destination numbers in your Pinpoint project.
3. Update the SAM template.yaml file's Lambda function environment variables.
    * ORIGINATION_NUMBER: This is the number you requested from Pinpoint. (phone number from step 1)
    * DESTINATION_NUMBER: This is the number you want to send an SMS to. (phone number from step 2)
4. Deploy the updated application again with `sam deploy`

## Testing

1. You can use the Test button in the Lambda console to send an SMS to the specified destination number. Any test event will work with the default pattern code.
2. After you click the Test button, you'll receive an SMS on the mobile device.

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
