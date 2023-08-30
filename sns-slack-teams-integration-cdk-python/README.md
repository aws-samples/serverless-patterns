# Amazon SNS integration with slack/teams channels

This pattern demonstrates how you can setup a fully serverless setup to integrate your SNS topic with a Slack/Teams channel. This provisions AWS resources for you and you just need to integrate your Slack/Teams webhooks to get it running.

[Learn more about this pattern at Serverless Land Patterns](https://serverlessland.com/patterns/sns-slack-teams-integration-cdk-python)

[SNS & Slack/Teams integration diagram](https://github.com/ajayv-AWS/Img/blob/870961eb05a4732ea2ee6a36af8ad1fd6a7ef206/SNS-teams-slack.drawio.png?raw=true)

Important: this application uses various AWS services and there are costs associated with these services after the Free Tier usage - please see the [AWS Pricing page](https://aws.amazon.com/pricing/) for details. You are responsible for any AWS costs incurred. No warranty is implied in this example.

## Requirements

* [Create an AWS account](https://portal.aws.amazon.com/gp/aws/developer/registration/index.html) if you do not already have one and log in. The IAM user that you use must have sufficient permissions to make necessary AWS service calls and manage AWS resources.
* [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html) installed and configured
* [Git Installed](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)
* [AWS CDK](https://docs.aws.amazon.com/cdk/latest/guide/cli.html) installed and configured

## Deployment Instructions

1. Create a new directory, navigate to that directory in a terminal and clone the GitHub repository:
   ```bash
   git clone https://github.com/aws-samples/serverless-patterns
   ```
2. Change directory to the pattern directory:
   ```bash
   cd serverless-patterns/sns-slack-teams-integration-cdk-python
   ```
3. To manually create a virtualenv on MacOS and Linux:
    ```bash
    python3 -m venv .venv
    ```
4. After the init process completes and the virtualenv is created, you can use the following
step to activate your virtualenv.
    ```bash
    source .venv/bin/activate
    ```
5. If you are a Windows platform, you would activate the virtualenv like this:
    ```bash
    .venv\Scripts\activate.bat
    ```
6. Once the virtualenv is activated, you can install the required dependencies.
    ```bash
    pip install -r requirements.txt
    ```
7. To deploy the application:
    ```bash
    cdk deploy
    ```

## How it works

This template will create an SNS topic which you can use to publish notifications to your Slack/Teams channel, and a Lambda function which will process the SNS message and pass it to the Slack/Teams webhook. You can customise the code to apply additional formatting as per your usecase.

## Testing

Publish a message from AWS Console or by CLI.

Example using CLI:

aws sns publish --topic-arn ENTER_YOUR_SNS_TOPIC_ARN --subject testSubject --message testMessage

## Cleanup
 
* Delete the stack
    ```bash
    cdk destroy
    ```
----
Copyright 2023 Amazon.com, Inc. or its affiliates. All Rights Reserved.

SPDX-License-Identifier: MIT-0
