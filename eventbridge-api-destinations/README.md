# Using Amazon EventBridge to route to API Destinations targets

With the new [API destinations feature](https://aws.amazon.com/blogs/compute/using-api-destinations-with-amazon-eventbridge/), EventBridge can now integrate with services outside of AWS using REST API calls.

This patterns configures an EventRule rule that routes to an API Destinations target. It configures a Connection, which contains the authorization for the API endpoint, and the API, which contains the URL, http method, and other configuration information.

Learn more about this pattern at Serverless Land Patterns: << Add the live URL here >>

Important: this application uses various AWS services and there are costs associated with these services after the Free Tier usage - please see the [AWS Pricing page](https://aws.amazon.com/pricing/) for details. You are responsible for any AWS costs incurred. No warranty is implied in this example.

## Requirements

* [Create an AWS account](https://portal.aws.amazon.com/gp/aws/developer/registration/index.html) if you do not already have one and log in. The IAM user that you use must have sufficient permissions to make necessary AWS service calls and manage AWS resources.
* [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html) installed and configured
* [Git Installed](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)
* [AWS Serverless Application Model](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-sam-cli-install.html) (AWS SAM) installed
* To run example #1, an account with [Webhook.site](https://webhook.site/)
* To run example #2, an account with [Slack](http://slack.com). Follow the instructions at [Create a bot for your workspace](https://slack.com/help/articles/115005265703-Create-a-bot-for-your-workspace) and note the bot's token (this code begins with xoxb) and the channel ID. You need both of these values to deploy the solution.

## Deployment Instructions

1. Create a new directory, navigate to that directory in a terminal and clone the GitHub repository:
    ``` 
    git clone https://github.com/aws-samples/serverless-patterns
    ```
1. Change directory to the pattern directory:
    ```
    cd eventbridge-api-destinations
    ```
1. There are two examples in this directory.
- To run the Webhook.test open API example, cd to `1-webhook-site`.
- To run the Slack authenticated API example, cd to `2-slack`.
1. From the command line, use AWS SAM to deploy the AWS resources for the pattern as specified in the template.yml file:
    ```
    sam deploy --guided
    ```
1. During the prompts:
    * Enter a stack name
    * Enter the desired AWS Region
    * Enter the parameters, such as Webhook.site URL or Slack bot token and Channel ID.
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
