# DynamoDB stream to EventBridge bus using EventBridge Pipes and suffix matching

This pattern demonstrates sending DynamoDB Streams directly to Amazon EventBridge bus suffix filtering.

Learn more about this pattern at Serverless Land Patterns:https://serverlessland.com/patterns/eventbridge-pipes-ddbstream-to-eventbridge-suffix-matching

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
    cd eventbridge-pipes-ddbstream-to-eventbridge-suffix-matching
    ```
1. From the command line, use AWS SAM to deploy the AWS resources for the pattern as specified in the template.yml file:
    ```
    sam deploy --guided
    ```
1. During the prompts:
    * Enter a stack name: eg. eventbridge-pipes-ddbstream-to-eventbridge-suffix-matching
    * Enter the desired AWS Region
    * Enter Email ID for SNS to create a topic and subscription.
    * Enter NationalTeam(This is configurable, you can create any parameter name).: eg. Argentina
    * Allow SAM CLI to create IAM roles with the required permissions.

    Once you have run `sam deploy --guided` mode once and saved arguments to a configuration file (samconfig.toml), you can use `sam deploy` in future to use these defaults.

1. Note the outputs from the SAM deployment process. These contain the resource names and/or ARNs which are used for testing.

## How it works

When new items are added into the DynamoDB database, the EventBridge Pipe is triggered. Only events that match the rule will be forwarded onto an EventBridge bus. In this example these are images that end with the `.png` trigger the EventBridge event.

## Testing

Add an item to the DynamoDB stream that contains a `.png` avatarUrl.

```bash
aws dynamodb put-item \
    --table-name Users \
    --item id={S="David"},avatarUrl={S="https://pbs.twimg.com/profile_images/1262283153563140096/DYRDqKg6_400x400.png"}
```

Event will be triggered.

---

Add an item to the DynamoDB stream that contains a `.gif` avatarUrl.

```bash
aws dynamodb put-item \
    --table-name Users \
    --item Name={S="David"},avatarUrl={S="https://pbs.twimg.com/profile_images/1262283153563140096/DYRDqKg6_400x400.gif"}
```

Event is not triggered.

---


## Cleanup
 
1. Delete the stack
    ```bash
    sam delete
    ```

----
Copyright 2023 Amazon.com, Inc. or its affiliates. All Rights Reserved.

SPDX-License-Identifier: MIT-0
