# AWS Step Function to Amazon SES with CDK (Typescript)

This pattern demonstrates how to build a AWS Step Function State machine to send email with Amazon Simple Email Service with SDK integration.

Learn more about this pattern at Serverless Land Patterns: https://serverlessland.com/patterns/stepfunction-ses-cdk

Important: this application uses various AWS services and there are costs associated with these services after the Free Tier usage - please see the [AWS Pricing page](https://aws.amazon.com/pricing/) for details. You are responsible for any AWS costs incurred. No warranty is implied in this example.

## Requirements

* [Create an AWS account](https://portal.aws.amazon.com/gp/aws/developer/registration/index.html) if you do not already have one and log in. The IAM user that you use must have sufficient permissions to make necessary AWS service calls and manage AWS resources.
* [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html) installed and configured
* [Git Installed](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)
* [Node and NPM](https://nodejs.org/en/download/) installed
* [AWS Cloud Development Kit](https://docs.aws.amazon.com/cdk/latest/guide/cli.html) (AWS CDK) installed
* Verified [AWS SES](https://docs.aws.amazon.com/ses/) (From address)[https://docs.aws.amazon.com/ses/latest/dg/creating-identities.html#verify-email-addresses-procedure]

## Deployment Instructions

1. Create a new directory, navigate to that directory in a terminal and clone the GitHub repository:
    ``` 
    git clone https://github.com/aws-samples/serverless-patterns
    ```
1. Change directory to the pattern directory:
    ```
    cd stepfunction-ses-cdk
    ```
2. Run below command to install required dependancies:
    ```
    npm install
    ```

3. From the command line, run:
    ```
    cdk deploy --all --parameters sesFromEmail='YOUR_SES_FROM_EMAIL_ADDRESS'
    ```

## Testing

1. In your State Machine, start a new execution with a similar payload below with your email address.
```json
{
    "email": "MY_EMAIL_ADDRESS"
}
```
2. An email should receive into the given email address.

* Please note: By default Amazon SES in a sandbox mode and you cannot send emails to other than verified email addresses. To remove the sending limit, submit a request to AWS support.

## Cleanup
 
1. To delete the stack, run:
    ```bash
    cdk destroy --all
    ```
----
Copyright 2022 Amazon.com, Inc. or its affiliates. All Rights Reserved.

SPDX-License-Identifier: MIT-0
