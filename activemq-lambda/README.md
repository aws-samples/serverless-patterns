# AmazonMQ ActiveMQ to AWS Lambda

This pattern deploys a Lambda function, an AmazonMQ ActiveMQ , a security group and the IAM permissions required to run the application. ActiveMQ invokes the Lambda function when new messages are available.

Learn more about this pattern at Serverless Land Patterns: [https://serverlessland.com/patterns/activemq-lambda](https://serverlessland.com/patterns/activemq-lambda)

Important: this application uses various AWS services and there are costs associated with these services after the Free Tier usage - please see the [AWS Pricing page](https://aws.amazon.com/pricing/) for details. You are responsible for any AWS costs incurred. No warranty is implied in this example.

## Requirements

* [Create an AWS account](https://portal.aws.amazon.com/gp/aws/developer/registration/index.html) if you do not already have one and log in. The IAM user that you use must have sufficient permissions to make necessary AWS service calls and manage AWS resources.
* [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html) installed and configured
* [Git Installed](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)
* [AWS Serverless Application Model](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-sam-cli-install.html) (AWS SAM) installed

## Deployment Instructions

1. Set up your username and password for RabbitMQ access. In a new terminal window enter:
    ```
    aws secretsmanager create-secret --name MQaccess --secret-string '{"username": "your-username", "password": "your-password"}'

1. Create a new directory, navigate to that directory in a terminal and clone the GitHub repository:
    ``` 
    git clone https://github.com/aws-samples/serverless-patterns
    ```
1. Change directory to the pattern directory:
    ```
    cd activemq-lambda
    ```
1. From the command line, use AWS SAM to deploy the AWS resources for the pattern as specified in the template.yml file:
    ```
    sam deploy --guided
    ```
1. During the prompts:
    * Enter a stack name
    * Enter the desired AWS Region
    * Enter SecretARN for ActiveMQ Admin user
    * Enter SecretName for ActiveMQ Admin user
    * Enter VPC ID for ActiveMQ
    * Enter Subnet ID for ActiveMQ 
    * Allow SAM CLI to create IAM roles with the required permissions.

    Once you have run `sam deploy --guided` mode once and saved arguments to a configuration file (samconfig.toml), you can use `sam deploy` in future to use these defaults.

1. Note the outputs from the SAM deployment process. These contain the resource names and/or ARNs which are used for testing.

## How it works

This template deploy new ActiveMQ Broker and use it as event source for AWS Lambda. Lambda uses Openwire protocol to connect with ActiveMQ

## Testing

1. Navigate to the AmazonMQ console and choose the newly created broker. 

1. In the Connections panel, locate the URL for the ActiveMQ web console.

1. Sign in with the credentials you created and stored in the Secrets Manager earlier.

1. Select Manage ActiveMQ broker > Queues from the top panel 

1. Choose "Send to" at the Operation Column of lambdaQueue1.

1. Provide some text in Message body for testing, Put number of messages to send and click "Send" button 

1. In the MQconsumer Lambda function, select the Monitoring tab and then choose View logs in CloudWatch. The log streams show that the Lambda function is invoked by Amazon MQ and you see the message in the logs.

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
