# AWS Lambda to Amazon SES

This SAM template creates a Lambda function that sends an email with Amazon SES.

Learn more about this pattern at Serverless Land Patterns: https://serverlessland.com/patterns/lambda-ses

Important: this application uses various AWS services and there are costs associated with these services after the Free Tier usage - please see the [AWS Pricing page](https://aws.amazon.com/pricing/) for details. You are responsible for any AWS costs incurred. No warranty is implied in this example.

## Requirements

* [Create an AWS account](https://portal.aws.amazon.com/gp/aws/developer/registration/index.html) if you do not already have one and log in. The IAM user that you use must have sufficient permissions to make necessary AWS service calls and manage AWS resources.
* [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html) installed and configured
* [Git Installed](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)
* [AWS Serverless Application Model](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-sam-cli-install.html) (AWS SAM) installed
* [Amazon SES](https://docs.aws.amazon.com/ses/latest/DeveloperGuide/verify-addresses-and-domains.html) verify identities in Amazon SES. Sandbox requires both sender and receiver addresses to be verified identities.

## Deployment Instructions
1. Confirm both Sender and Receiver email addresses are verified in Amazon SES.

1. Create a new directory, navigate to that directory in a terminal and clone the GitHub repository:
    ``` 
    git clone https://github.com/aws-samples/serverless-patterns
    ```
1. Change directory to the pattern directory:
    ```
    cd lambda-ses
    ```
    * (optional): change [template.yaml] policy resource to reference the arn of the sender email address or domain 
    [Line 31 in template.yaml]
    ```
      Policies:
        - SESCrudPolicy: 
          IdentityName: '*' #Specify ARN(s) for identity. If in sandbox, specify both SENDER and RECEIVER ARNs
    ```
1. From the command line, use AWS SAM to deploy the AWS resources for the pattern as specified in the template.yml file:
    ```
    sam deploy --guided
    ```
1. During the prompts:
    * Enter a stack name
    * Enter the desired AWS Region
    * Allow SAM CLI to create IAM roles with the required permissions
    * Amazon SES Sender identity - email address that you use to send email

    Once you have run `sam deploy --guided` mode once and saved arguments to a configuration file (samconfig.toml), you can use `sam deploy` in future to use these defaults.

1. Note the outputs from the SAM deployment process. These contain the resource names and/or ARNs which are used for testing.

## How it works

Lambda will be invoked to send an email to Amazon SES. You will be able to customize the email based on the needs of your application by supplying the function with the event contents.

Email address of the Sender(FROM) was already provide in the sam deploy. 
This email message can contain both plain text and HTML renderings.
The Body and Subject of the email message are passed into the function in an event.
The receiver(TO) email address will also be supplied in the event.


Event will pass the following:
* HTMLBody - HTML email body
* TXTBody - TXT email body
* Subject - Subject of email
* ReceiverAddress - The receiver of the email



All new AWS Accounts are placed in the Amazon SES sandbox environment.  While your account is in the sandbox, you can use all of the features of Amazon SES.  However, the following restrictions are applied:
* You can only send mail to verified email addresses and domains, or to the Amazon SES mailbox simulator.
* You can only send mail from verified email addresses and domains. 



## Testing
1. You can test the solution by accessing the Lambda console, finding the Lambda function, and clicking Test in the Code Source section.

1. Create a new test event and supply the example event

1. You can also invoke the function from the CLI using (replace YOUR_FUNCTION_NAME & TO_EMAIL_ADDRESS) 

```
aws lambda invoke --function-name YOUR_FUNCTION_NAME --invocation-type Event --payload  '{"HTMLBody": "HMTL Body Here","TXTBody": "TXT Body Here","Subject": "Subject Line", "ReceiverAddress": "TO_EMAIL_ADDRESS"}' output.txt
```

Example Event
```
{
  "HTMLBody": "HMTL Body Here",
  "TXTBody": "TXT Body Here",
  "Subject": "Subject Line",
  "ReceiverAddress": "TO_EMAIL_ADDRESS"
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
