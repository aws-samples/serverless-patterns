# AWS Lambda, Amazon Kinesis Data Stream, Splunk Cloud/Enterprise

This pattern will set up a serverless stack with AWS Lambda and Amazon Kinesis Data Stream (KDS) to process continuously streaming Amazon CloudWatch logs from different accounts and regions. AWS Lambda receives stream records with CloudWatch log events, which it decompresses and decodes to prepare events to be pushed to Splunk. A log destination Amazon Resource Name (ARN) needs to be configured across all account's CloudWatch log groups.

Learn more about this pattern at Serverless Land Patterns: https://github.com/aws-samples/serverless-patterns/issues/1204

Important: this application uses various AWS services and there are costs associated with these services after the Free Tier usage - please see the [AWS Pricing page](https://aws.amazon.com/pricing/) for details. You are responsible for any AWS costs incurred. No warranty is implied in this example.

## Requirements

* [Create an AWS account](https://portal.aws.amazon.com/gp/aws/developer/registration/index.html) if you do not already have one and log in. The IAM user that you use must have sufficient permissions to make necessary AWS service calls and manage AWS resources.
* [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html) installed and configured
* [Git Installed](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)
* [AWS CDK Toolkit Installed]  https://docs.aws.amazon.com/cdk/v2/guide/cli.html
* You have bootstrapped your account with CDK - https://docs.aws.amazon.com/cdk/v2/guide/bootstrapping.html
* Since this pattern will require logs to be ingested in Splunk cloud/enterprise platform. You need to have a valid license for the same. For POC purpose you can opt for 14 days trial provided by Splunk with limited functionality. Once you have a valid Splunk platform access, follow the steps given in the below article to create an HTTP event collector (HEC) URL and associated token for authentication. Note: Do not opt for indexer acknowledgement while creating HEC.
Set up and use HTTP Event Collector in Splunk Web https://docs.splunk.com/Documentation/Splunk/9.0.4/Data/UsetheHTTPEventCollector

## Deployment Instructions

1. Create a new directory, navigate to that directory in a terminal and clone the GitHub repository:
    ``` 
    git clone https://github.com/aws-samples/serverless-patterns
    ```
1. Change directory to the pattern directory:
    ```
    cd cloudwatch-logs-to-splunk-using-lambda-kinesis
    ```
1. From the command line, use AWS SAM to deploy the AWS resources for the pattern as specified in the template.yml file:
    ```
    cdk deploy
    ```
1. During the prompts:
    * Process will show changes and take confirmation for deployment with something like "Do you wish to deploy these changes y/n?"

    Once your CloudFormation stack with the name "KinesisDataStreamLogProcessorStack" is successfully deployed, navigate to the CloudFormation console > go to stacks > check for status to confirm

1. Manual steps required after stack deployment
    The stack will create the IAM role required for Log Destination, but the actual log destination is currently not supported or working with CDK. Details on creation can be found in this article (https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/CreateDestination.html). Note: The role would have already been created by the stack, and only log destination creation will be pending.
    So you need to perform the below small step through AWS CLI:
    1. Copy the data
stream ARN from CloudFormation stack > Resources > Data stream with a name like 'clw-log-processor-stream'
    ARN will look like : arn:aws:kinesis:<<Region>>:<<AccountNumber>>:stream/<<data-stream-name>>
2. Copy the log destination IAM role ARN from CloudFormation stack > resource with a name like 'LogDestinationRole*'
3. Enter the above ARN details in the below command placeholders and run this command in AWS CLI (Refer to this link for configuring up AWS CLI https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-files.html)
    ```
    Run the below command in AWS CLI
    aws logs put-destination
        –destination-name “<<LogDestination name you wish to give>>”
        –target-arn “<<Enter the Kinesis data stream ARN created by the stack here which is created by the stack as part of cdk deploy>>”
        –role-arn “<<Enter the log destination role ARN which is created by the stack as part of cdk deploy>>”
    ```
    Output should look like below:

    ```
    {
        “destination”: {
        “destinationName”: “LogDestination”,
        “targetArn”: “arn:aws:kinesis:<<Region>>:<<AccountNumber>>:stream/clw-log-processor-stream”,
        “roleArn”: “arn:aws:iam::<<AccountNumber>>:role/LogDestinationRole”,
        “arn”: “arn:aws:logs:<<Region>>:<<AccountNumber>>:destination:LogDestination”,
        “creationTime”: 1680470148411
        }
    }
    ```
    4. Please note down the ARN of the log destination, which you can use to configure the subscription filter across CloudWatch log groups in the same or cross-account. 
    5. You can also get log destination details using the below command if you miss noting it down. You can also use this step as verification.
        ```
        aws logs describe-destinations
        ```
    6. You need to configure the Splunk HEC URL and Token in the Lambda environment variable.

For more information, refer to the below articles:
    Troubleshooting common CDK issues: https://docs.aws.amazon.com/cdk/v2/guide/troubleshooting.html#troubleshooting_app_required
    About HTTP Event Collector Indexer Acknowledgment https://docs.splunk.com/Documentation/Splunk/9.0.4/Data/AboutHECIDXAck

## How it works

1. It will create a Kinesis data stream, which will receive streaming logs from CloudWatch log groups. For this, CloudWatch log groups need to have a subscription filter created to log destination.
2. The Kinesis data stream will be the trigger or event source for the Lambda function. So Lambda will receive log streams ingested by various applications via CloudWatch log groups.
3. Lambda will decompress log streams and decode Base64 strings. It will then send log events to Splunk using the web API URL provided by the Splunk platform. 
4. Log streams will appear near real-time in the Splunk dashboard (search & reporting)

## Testing

1. Create a simple test Lambda function that will perform some operations and write some logs.
2. The Lambda function logs will be visible initially in "/aws/lambda/<function-name>" log group.
3. Go to the CloudWatch console > log groups > click on a particular log group > go to subscriptions > create subscription with 'Kinesis Stream' as the destination. Use the Log destination ARN, which you have noted during creating the subscription.
4. You can create an API Gateway
in front of the test Lambda function or call your function from another test function. Do not use the test function capability on the Lambda console, as it doesn't generate logs in the required format, and certain sections are not populated. This will not be the case if you use Lambda behind an API Gateway or invoke it using another Lambda or other invoking mechanisms except for console testing.
5. You can monitor the function for success rate. Once your test function and actual log processor function have successful invocations, you can go to the Splunk platform and use the 'search and reporting' module to search your logs. Try to log unique strings from your test function so you can find it in Splunk almost near real-time.

Congratulations! You have successfully tested the end-to-end flow after this.

## Cleanup

1. Delete the stack
    ```
    cdk destroy
    ```
    OR
    ```
    bash
    aws cloudformation delete-stack --stack-name STACK_NAME
    ```
2. Confirm the stack has been deleted
    ```bash
    aws cloudformation list-stacks --query "StackSummaries[?contains(StackName,'STACK_NAME')].StackStatus"
    ```
----
Copyright 2023 Amazon.com, Inc. or its affiliates. All Rights Reserved.

SPDX-License-Identifier: MIT-0
