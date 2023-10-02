# EventBridge to Lambda to SNS

This pattern creates an AWS Lambda function that scans the subnet(s) across mutliple regions and vpcs for AWS VPC subnet(s) that are running low on IP addresses and sends alert via SNS topic. Amazon CloudWatch Events rule triggers the Lambda function at a desired interval.

Learn more about this pattern at Serverless Land Patterns: https://serverlessland.com/patterns/eventbridge-lambda-sns 

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
    cd eventbridge-lambda-sns
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

The AWS SAM template deploys the resources and the IAM permissions required to run the application.

The EventBridge rule specified in template.yaml will trigger the function once a week. When the function is triggered it will scan AWS VPC subnet(s) across mutliple regions and vpcs for subnet(s) that are running low on IP addresses as determined by your custom threshold. In this example the threshold is 4000 which is set via Lambda function environment variable named "IP_limit", meaning any subnet(s) with an IP address account less than 4000 IP addresses will be flagged. For each subnet flagged, the following details will sent to an SNS topic:

Region
Subnet ID 
IP address count

You will have to subscribe to the SNS topic using your email of choice.
Note: You must confirm the subscription before the email address can start to receive messages.


## Testing

Tests can be done invoking the Lambda function directly or allowing the EventBridge rule to invoke the function. You can modify "IP_limit" to a number you deem sufficient before receiving notifications when an IP address usage threshold is breached. For example if you have subnets that have 254 available IP addresses, you can modify "IP_limit" to 300, this will allow the function flag all subnets with IP address count under 300.


1.  Invoke the lambda function using AWS CLI

aws lambda invoke \
    --function-name my-function \
    --cli-binary-format raw-in-base64-out \
    --payload '{ }' \
    response.json


2. Invoke via EventBridge rule

You can also modify Eventbridge rule in order to reduce or increase the intervals at which this function run these checks. The below example should trigger the function at 5 minute intervals.

aws events put-rule --name <rule name> --schedule-expression "rate(5 minutes)"

3. You will recieve an alert via SNS topic of VPC details of subnets IP address usage have breached threshold:

Region
Subnet ID 
IP address count

You will have to subscribe to the SNS topic using your email of choice.
Note: You must confirm the subscription before the email address can start to receive messages.

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
