# Inbound webhooks for EventBridge

This pattern creates an inbound webhook from Stripe to Amazon EventBridge. The webhook is a Lambda function URL that uses the Stripe Webhook secret to verify the request, then forwards it to EventBridge.

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
- To run the Stripe example, cd to `1-stripe`.
  1. The Stripe Inbound webhook requires a Stripe Signing Secret prior to creating the CloudFormation Stack.
  2. To generate a Stripe Signing Secret, Create an endpoint with a dummy value of the Endpoint URL (This will be updated once the Lambda fURL is available). 
  3. It will create a signing secret which is needed in Step 4 below for parameter StripeWebhookSecret.
  4. After the stack is deployed, replace the dummy value of the Endpoint URL on Stripe with the Lambda fURL.

- To run the GitHub example, cd to `2-github`.
  1. The GitHub Inbound webhook requires a Secret prior to creating the CloudFormation Stack. (You can create a secret phrase of your choice) This secret will later be needed in step 2 bellow along with the Lambda fURL
  2. Setup Webhook for a repository of choice from your GitHub Account [Create GitHub Webhook](https://docs.github.com/en/developers/webhooks-and-events/webhooks/creating-webhooks)
  3. [Set up GitHub Webhook on EventBridge Service Console](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-saas-furls.html#furls-connection-github)
 
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

### Stripe

Stripe emits events for a variety of actions, for example, when a payment was successful or an order was created. Using Inbound webhooks using Lambda fURLs you can send the payloads to EventBridge for processing. Users can extend this example by adding targets to act on Stripe events in real-time.

## Testing

1. After updating the Endpoint URL with the deployed Lambda fURL, select the event types you want to send to EventBridge.
2. Simulate the events using the Stripe Dashboard. For example, the product.created event could be simulated by navigating to the [Products](https://dashboard.stripe.com/products) page and adding a new product.
3. The Cloudwatch Logs for your WebhookFunction will indicate if there were any errors with processing the Stripe event.

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
Copyright 2021 Amazon.com, Inc. or its affiliates. All Rights Reserved.

SPDX-License-Identifier: MIT-0
