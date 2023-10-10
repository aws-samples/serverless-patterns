# AWS Lambda to Amazon EventBridge

This pattern creates a Lambda function that publishes an event to EventBridge. 

Learn more about this pattern at the Serverless Land Patterns Collection: [https://serverlessland.com/patterns/lambda-eventbridge-terraform](https://serverlessland.com/patterns/lambda-eventbridge)

Important: this application uses various AWS services and there are costs associated with these services after the Free Tier usage - please see the [AWS Pricing page](https://aws.amazon.com/pricing/) for details.

You are responsible for any AWS costs incurred. No warranty is implied in this example.

## Requirements

* [Create an AWS account](https://portal.aws.amazon.com/gp/aws/developer/registration/index.html) if you do not already have one and log in. The IAM user that you use must have sufficient permissions to make necessary AWS service calls and manage AWS resources.
* [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html) installed and configured
* [Git Installed](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)
* [Terraform](https://learn.hashicorp.com/tutorials/terraform/install-cli?in=terraform/aws-get-started) installed

## Deployment Instructions

1. Create a new directory, navigate to that directory in a terminal and clone the GitHub repository:
    ``` 
    git clone https://github.com/aws-samples/serverless-patterns
    ```
1. Change directory to the pattern directory:
    ```
    cd lambda-eventbridge-terraform
    ```
1. From the command line, initialize terraform to  to downloads and installs the providers defined in the configuration:
    ```
    terraform init
    ```
1. From the command line, apply the configuration in the main.tf file:
    ```
    terraform apply
    ```
1. During the prompts:
    * Enter yes
1. Note the outputs from the deployment process. These contain the resource names and/or ARNs which are used for testing.

## How it works

The Terraform template deploys the following resources:

| Type | Logical ID |
| --- | --- |
| AWS::Lambda::Function | PublisherFunction |
| AWS::IAM::Role | PublisherFunctionRole |

When the Lambda function is invoked, it publishes an event to the default event bus in EventBridge.


## Testing

Use the [AWS CLI](https://aws.amazon.com/cli/) to send a test event to EventBridge and observe the Lambda function logs:

1. Send an event to EventBridge:

```bash
aws lambda invoke --function-name ENTER_YOUR_PUBLISHER_FUNCTION_NAME response.json
```

2. Go to the Lambda function in the console and find the `PublisherFunction`

3. Navigate to the `Monitor` tab and click on the link to CloudWatch

4. You should see an event delivered to the default event bus:
```bash
2022-06-21T19:38:16.457Z	48c3c5b7-3a17-46b8-a049-9a92fc579a6d	INFO	{
  FailedEntryCount: 0,
  Entries: [ { EventId: 'de8a0b13-9512-1656-95d7-55733063f189' } ]
}
```

## Cleanup
 
1. Change directory to the pattern directory:
    ```
    cd serverless-patterns/lambda-eventbridge-terraform
    ```
1. Delete all created resources
    ```bash
    terraform destroy
    ```
1. During the prompts:
    * Enter yes
1. Confirm all created resources has been deleted
    ```bash
    terraform show
    ```
----
Copyright 2021 Amazon.com, Inc. or its affiliates. All Rights Reserved.

SPDX-License-Identifier: MIT-0
