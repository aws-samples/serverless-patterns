# AWS Kinesis Data Streams to AWS Lambda

This pattern creates an AWS Kinesis Data Stream, a stream consumer, and an AWS Lambda function. When data is added to the stream, the Lambda function is invoked.

Learn more about this pattern at Serverless Land Patterns: [https://serverlessland.com/patterns/kinesis-to-lambda](https://serverlessland.com/patterns/kinesis-to-lambda)

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
    cd kinesis-lambda
    ```
1. From the command line, use AWS SAM to deploy the AWS resources for the pattern as specified in the template.yml file:
    ```
    sam deploy --guided
    ```
1. During the prompts:
    * Enter a stack name
    * Enter the desired AWS Region
    * Allow SAM CLI to create IAM roles with the required permissions.
    
    Once you have run `sam deploy -guided` mode once and saved arguments to a configuration file (samconfig.toml), you can use `sam deploy` in future to use these defaults.
1. Note the outputs from the SAM deployment process. These contain the resource names and/or ARNs which are used for testing.

## Testing

Use the Amazon Kinesis Data Generator for testing. The easiest way to use this tool is to use the [hosted generator](https://awslabs.github.io/amazon-kinesis-data-generator/web/producer.html) and follow the [setup instructions](https://awslabs.github.io/amazon-kinesis-data-generator/web/help.html).

After you have the generator configured, you should have a custom URL to generate data for your Kinesis data stream. In your configuration steps, you created a username and password. Log in to the generator using those credentials.

When you are logged in, you can generate data for your stream test.

1. Choose the region you deployed the application to
1. For Stream/delivery stream, select your stream.
1. For Records per second, keep the default value of 100.
1. On the Template 1 tab, name the template Sensor1.
1. Use the following template:
    ```JSON
    {
        "sensorId": {{random.number(50)}},
        "currentTemperature": {{random.number(
            {
                "min":10,
                "max":150
            }
        )}},
        "status": "{{random.arrayElement(
            ["OK","FAIL","WARN"]
        )}}"
    }
    ```
1. Choose Send Data.
1. After several seconds, choose Stop Sending Data.

## Cleanup

1. Delete the stack
    ```bash
    aws cloudformation delete-stack --stack-name STACK_NAME
    ```
1. Confirm the stack has been deleted
    ```bash
    aws cloudformation list-stacks --query "StackSummaries[?contains(StackName,'STACK_NAME')].StackStatus"
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
Copyright 2021 Amazon.com, Inc. or its affiliates. All Rights Reserved.

SPDX-License-Identifier: MIT-0