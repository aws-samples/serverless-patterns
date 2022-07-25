# Amazon EventBridge to Amazon SNS

This pattern is multiple EventBridge Buses to multiple SNS Topics.  The AWS SAM template deploys three EventBridge Buses, six EventBridge Rules (2 per Bus),  four SNS Topics, three SQS queues and a Lambda function.  The lambda function is an event generator which sends events to EventBridge Buses that trigger appropriate Rules sending the payload to the appropriate SNS Topic.  SQS queues are attached to the Rules as Dead Letter Queues. Appropriate permissions are granted to EventBridge to trigger the SNS Topics and the Lambda function to put events in the EventBridge.

Learn more about this pattern at Serverless Land Patterns: [<< Add the live URL here >>](https://serverlessland.com/patterns/eventbridge-sns.)

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
    cd _patterns-model
    ```
1. From the command line, use AWS SAM to deploy the AWS resources for the pattern as specified in the template.yml file:
    ```
    sam deploy --guided
    ```
1. During the prompts:
    * Enter a stack name
    * Enter the desired AWS Region
    * Allow SAM CLI to create IAM roles with the required permissions.

    Once you have run `sam deploy --guided` mode once and saved arguments to a configuration file (samconfig.toml), you can use `sam deploy` in future to use these defaults.

1. Note the outputs from the SAM deployment process. These contain the resource names and/or ARNs which are used for testing.

## How it works

To make this easier to understand, here is an example.  Countries report cross-border transactions to their respective Reserve/Central Bank.  For simplicity, transactions originate from bank branches or ATM (automatic teller machines) as sub-domains (source) from all banks.  For simplicity we use three EventBridge Buses - (bluebank, redbank and greenbank).  The "DetailType" is filtering for "transaction type" and the "Detail" section filters the "Yes/No" reportable field.  Based on these combinations, events trigger different rules and send transaction payloads to SNS Topics of the ReserveBank and/or the Transaction Warehouses of the respective bank's SNS Topics.

## Testing

1. From the output, get the 4 SNS Topic ARNs and subscribe 4 email addresses to the SNS Topics using this command structure.

aws sns subscribe --topic-arn ENTER_YOUR_TOPIC_ARN --protocol email-json --notification-endpoint ENTER_YOUR_EMAIL_ADDRESS

2. Click the confirmation link delivered to your emails to verify the endpoint.

3. Send an event to EventBridge using the Lamdba function:
- Get the 3 ARNs of the EventBridge Buses from the Output.
- Open the Lambda function code in your Lambda console and replace "bus_a", "bus_b" and "bus_c" with the ARNs of the Buses created the SAM template.
- Deploy the function and "Test" on the Console
- Alternatively, get the function name from the Cloud Formation Output and use the following CLI command to invoke the function a few times:

aws lambda invoke \
    --function-name myfunction \
    response.json

4. The function will randomly choose any of the 3 Buses and send an event.  The events will be classified "reportable" or "non-reportable".  All "reportable" events trigger notification with the payload to the "ReserveBank SNS Topic" and another notification to the appropriate Bank Warehouse matching the Bus selected.  All "non-reportable" events do not trigger the ReserveBank SNS Topic but trigger the respective Bank Warehouse matching the Bus selected.


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
Additional resources
Permissions for Amazon EventBridge event buses
 - https://docs.amazonaws.cn/en_us/eventbridge/latest/userguide/eb-event-bus-perms.html#eb-event-bus-example-policy-cross-account
Content filtering in Amazon EventBridge event patterns - https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-event-patterns-content-based-filtering.html


Copyright 2021 Amazon.com, Inc. or its affiliates. All Rights Reserved.

SPDX-License-Identifier: MIT-0
