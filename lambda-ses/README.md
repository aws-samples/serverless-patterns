# AWS Lambda to Amazon SES

This SAM template creates a Lambda function that sends an email with Amazon SES

Learn more about this pattern at Serverless Land Patterns: https://serverlessland.com/patterns/lambda-ses

Important: this application uses various AWS services and there are costs associated with these services after the Free Tier usage - please see the [AWS Pricing page](https://aws.amazon.com/pricing/) for details. You are responsible for any AWS costs incurred. No warranty is implied in this example.

## Requirements

* [Create an AWS account](https://portal.aws.amazon.com/gp/aws/developer/registration/index.html) if you do not already have one and log in. The IAM user that you use must have sufficient permissions to make necessary AWS service calls and manage AWS resources.
* [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html) installed and configured
* [Git Installed](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)
* [AWS Serverless Application Model](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-sam-cli-install.html) (AWS SAM) installed
* [Amazon SES](https://docs.aws.amazon.com/ses/latest/DeveloperGuide/verify-addresses-and-domains.html) verify identities in Amazon SES. Sandbox requires both sender and receiver addresses to be verified identities.

## Deployment Instructions

1. Create a new directory, navigate to that directory in a terminal and clone the GitHub repository:
    ``` 
    git clone https://github.com/aws-samples/serverless-patterns
    ```
1. Change directory to the pattern directory:
    ```
    cd lambda-ses
    ```
    * (optional): change [template.yaml] policy resource to reference the arn of the sender email address or domain
1. From the command line, use AWS SAM to deploy the AWS resources for the pattern as specified in the template.yml file:
    ```
    sam deploy --guided
    ```
1. During the prompts:
    * Enter a stack name
    * Enter the desired AWS Region
    * Allow SAM CLI to create IAM roles with the required permissions.
    * Amazon SES Sender identity - email address that you use to send email. 
    * Amazon SES Receiver identity - email address that will receive email. 

    Once you have run `sam deploy --guided` mode once and saved arguments to a configuration file (samconfig.toml), you can use `sam deploy` in future to use these defaults.

1. Note the outputs from the SAM deployment process. These contain the resource names and/or ARNs which are used for testing.

## How it works

Lambda will be invoked to send an email to Amazon SES.
This email can contain both plain text and HTML rendering.

All new AWS Accounts are placed in the Amazon SES sandbox environment.  While your account is in the sandbox, you can use all of the features of Amazon SES.  However, the following restrictions are applied:
* You can only send mail to verified email addresses and domains, or to the Amazon SES mailbox simulator.
* You can only send mail from verified email addresses and domains. 


## Testing
1. You can test the solution by accessing the Lambda console, finding the Lambda function, and clicking Test in the Code Source section.

1. You can also invoke the function from the CLI using aws lambda invoke --function-name ENTER_FUNCTION_NAME output.txt.



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
