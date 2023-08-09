# Using Amazon EventBridge to route to API Destinations targets

With the new [API destinations feature](https://aws.amazon.com/blogs/compute/using-api-destinations-with-amazon-eventbridge/), EventBridge can now integrate with services outside of AWS using REST API calls.

This patterns configures an EventRule rule that routes to an API Destinations target. It configures a Connection, which contains the authorization for the API endpoint, and the API, which contains the URL, http method, and other configuration information.

Learn more about this pattern at Serverless Land Patterns: https://serverlessland.com/patterns/eventbridge-api-destinations

Important: this application uses various AWS services and there are costs associated with these services after the Free Tier usage - please see the [AWS Pricing page](https://aws.amazon.com/pricing/) for details. You are responsible for any AWS costs incurred. No warranty is implied in this example.

## Requirements

* [Create an AWS account](https://portal.aws.amazon.com/gp/aws/developer/registration/index.html) if you do not already have one and log in. The IAM user that you use must have sufficient permissions to make necessary AWS service calls and manage AWS resources.
* [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html) installed and configured
* [Git Installed](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)
* [AWS Serverless Application Model](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-sam-cli-install.html) (AWS SAM) installed
* To run example #1, an account with [Webhook.site](https://webhook.site/)
* To run example #2, an account with [Slack](http://slack.com). Follow the instructions at [Create a bot for your workspace](https://slack.com/help/articles/115005265703-Create-a-bot-for-your-workspace) and note the bot's token (this code begins with xoxb) and the channel ID. You need both of these values to deploy the solution.
* To run example #3, an account with [Sumologic](https://sumologic.com). Follow the instructions at [Create an HTTP Source ](https://help.sumologic.com/03Send-Data/Sources/02Sources-for-Hosted-Collectors/HTTP-Source) and note the unique URL for your HTTP Source you need this value to deploy the solution.
* To run example #4, an account with [Mongodb](https://www.mongodb.com/). Follow the instructions at [Create an HTTPS Endpoint](https://docs.mongodb.com/realm/endpoints/) and note the unique URL for your API destination endpoint to deploy the solution.
* To run example #5, an account with [Zendesk](https://www.zendesk.com). Follow the instructions to  [Enable Password an API key access](https://support.zendesk.com/hc/en-us/articles/4408836402074-Using-the-API-dashboard#enabling_password_or_token_access_).
* To run example #6, an account with [Freshdesk](https://support.freshdesk.com/support/login). Follow the instructions at [Getting Started](https://developers.freshdesk.com/api/#getting-started) and note the unique URL for your API destination endpoint to deploy the solution.
* To run example #7, an account with [DataDog](hhttps://www.datadoghq.com). Follow the instructions to [Add an API key or client token](https://docs.datadoghq.com/account_management/api-app-keys/#add-an-api-key-or-client-token) and note the api key.
* To run example #9, an account with [Shopify](https://www.shopify.com/). Follow the instructions to [Create an app and configure Admin API Access scopes](https://shopify.dev/apps/auth/admin-app-access-tokens#step-1-create-and-install-the-app). Make sure to note the Admin Key.
* To run example #10, an account with [Stripe](https://dashboard.stripe.com/login). Follow the instructions to [Set up your development environment](https://stripe.com/docs/development/quickstart) and note the api key.
## Deployment Instructions

1. Create a new directory, navigate to that directory in a terminal and clone the GitHub repository:
    ``` 
    git clone https://github.com/aws-samples/serverless-patterns
    ```
1. Change directory to the pattern directory:
    ```
    cd eventbridge-api-destinations
    ```
1. There are several examples in this directory.
- To run the Webhook.test open API example, cd to `1-webhook-site`.
- To run the Slack authenticated API example, cd to `2-slack`.
- To run the sumologic HTTP Source collector example, cd to `3-sumologic`.
- To run the mongoDB API destination example, cd to `4-mongodb`.
- To run the Zendesk API Destination example, cd to `5-zendesk`.
- To run the freshdesk API destination example, cd to `6-freshdesk`.
- To run the Datadog API Destination example, cd to `7-datadog`.
- To run the Shopify API Destination example, cd to `9-shopify`.
- To run the Stripe API Destination example, cd to `10-stripe`.
1. From the command line, use AWS SAM to deploy the AWS resources for the pattern as specified in the template.yml file:
    ```
    sam deploy --guided
    ```
1. During the prompts:
    * Enter a stack name
    * Enter the desired AWS Region
    * Enter the parameters, such as Webhook.site URL, Slack bot token and Channel ID, or sumo logic HTTP Source URL.
    * Allow SAM CLI to create IAM roles with the required permissions.

    Once you have run `sam deploy -guided` mode once and saved arguments to a configuration file (samconfig.toml), you can use `sam deploy` in future to use these defaults.
1. Note the outputs from the SAM deployment process. These contain the resource names and/or ARNs which are used for testing.

## Testing

1. From a command line in this directory, send a test event to EventBridge simulating a "Payment failed" event:
```
aws events put-events --entries file://testEvent.json
```
2. In the Webhook.site example, the API call appears in the dashboard.
3. In the Slack example, a message appears in the specified Slack channel ("Payment failed").
4. For the sumo logic example use the testEvent.json within the 3-sumologic directory
5. For the mongoDB example use the testEvent.json within the 4-mongodb directory
6. For the zendesk example use the testEvent.json within the 5-zendesk directory
7. For the freshdesk example use the testEvent.json within the 6-freshdesk directory
8. For the datadog example use the testEvent.json within the 7-datadog directory
9. For the shopify example use the testEvent.json within the 9-shopify directory
10. For the shopify example use the testEvent.json within the 10-stripe directory
```
aws events put-events --entries file://3-sumologic/testEvent.json
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
