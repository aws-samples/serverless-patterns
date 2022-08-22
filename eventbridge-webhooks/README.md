# Inbound webhooks for EventBridge

This pattern creates an inbound webhook from Stripe to Amazon EventBridge. The webhook is a Lambda function URL that verifies the inbound request then forwards it to EventBridge.

Learn more about this pattern at Serverless Land Patterns: https://serverlessland.com/patterns/eventbridge-webhook-stripe

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
    cd eventbridge-webhooks
    ```
3. There are several examples in this directory.
- To run the GitHub example, cd to `2-github`.
  1. The GitHub Inbound webhook requires a Secret prior to creating the CloudFormation Stack. [Create Encrypted Secret](https://docs.github.com/en/actions/security-guides/encrypted-secrets)
  2. Deploy the cloudformation template. You’ll need the secret you created in step 1 (See step 4, on how to deploy the cloudformation template)
  3. Finally, create the webhook on GitHub. You’ll need the secret you created in step 1 and the Lambda function URL you created in step 2 to complete this step. [Set up GitHub Webhook](https://docs.github.com/en/developers/webhooks-and-events/webhooks/creating-webhooks)
 
4. From the command line, use AWS SAM to deploy the AWS resources for the pattern as specified in the template.yml file:
    ```
    sam deploy --guided
    ```
5. During the prompts:
    * Enter a stack name
    * Enter the desired AWS Region
    * Allow SAM CLI to create IAM roles with the required permissions.
    Once you have run `sam deploy --guided` mode once and saved arguments to a configuration file (samconfig.toml), you can use `sam deploy` in future to use these defaults.

6. Note the outputs from the SAM deployment process. These contain the resource names and/or ARNs which are used for testing.

## How it works

GitHub emits events for a variety of actions, for example, when a repository was created or the status of a commit changed. Using Inbound webhooks using Lambda function URLs you can send the payloads to EventBridge for processing. More info on GitHub Webhooks can be found [here](https://docs.github.com/en/developers/webhooks-and-events/webhooks/about-webhooks).

## Testing

1. After updating the Endpoint URL in the SaaS application with the deployed Lambda fURL, select the event types you want to send to EventBridge.
2. Test the webhook by simulating or performing actions in the SaaS application.
3. The Cloudwatch Logs for your WebhookFunction will indicate if there were any errors with processing the inbound event.

## Cleanup
 
1. Delete the stack
    ```bash
    aws cloudformation delete-stack --stack-name STACK_NAME
    ```
2. Confirm the stack has been deleted
    ```bash
    aws cloudformation list-stacks --query "StackSummaries[?contains(StackName,'STACK_NAME')].StackStatus"
    ```
----
Copyright 2022 Amazon.com, Inc. or its affiliates. All Rights Reserved.

SPDX-License-Identifier: MIT-0
