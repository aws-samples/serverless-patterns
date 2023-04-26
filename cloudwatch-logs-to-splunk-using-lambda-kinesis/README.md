# Lambda, Kinesis Data Stream, Splunk cloud/Enterprise

This pattern will setup serverless stack with AWS Lambda and Kinesis data stream (KDS) to process continuously streaming CloudWatch logs from different accounts and regions. Lambda receives stream records with CloudWatch log events which it decompress and decode to prepare events to be pushed to Splunk. A log destination ARN need to be configured across all account’s CloudWatch log groups. 

Learn more about this pattern at Serverless Land Patterns: https://github.com/aws-samples/serverless-patterns/issues/1204

Important: this application uses various AWS services and there are costs associated with these services after the Free Tier usage - please see the [AWS Pricing page](https://aws.amazon.com/pricing/) for details. You are responsible for any AWS costs incurred. No warranty is implied in this example.

## Requirements

* [Create an AWS account](https://portal.aws.amazon.com/gp/aws/developer/registration/index.html) if you do not already have one and log in. The IAM user that you use must have sufficient permissions to make necessary AWS service calls and manage AWS resources.
* [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html) installed and configured
* [Git Installed](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)
* [AWS CDK Toolkit Installed]  https://docs.aws.amazon.com/cdk/v2/guide/cli.html
* You have bootstrapped your account with CDK - https://docs.aws.amazon.com/cdk/v2/guide/bootstrapping.html
* Since this pattern will require logs to be ingested in Splunk cloud/enterprise platform. You need to have valid license for the same. For POC purpose you can opt for 14 days trial provided by Splunk with limited functionality. Once you hav valid splunk platform access follow the steps given in below article to create HTTP event collector (HEC) URL and associated token for authentication. Note: Do not opt for indexer acknowledgement while creating HEC.
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


    Once your cloudformation stack with name "KinesisDataStreamLogProcessorStack" is successfully deployed. Navigate to cloudformation console > go to stacks > check for status to confirm

1. Manual steps required after stack deployment
    The stack will create IAM role required for Log Destination but actual log destination currently not supported or working with CDK. Details on creation you can find in this article(https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/CreateDestination.html). Note: Role would have already created by stack only log destination creation will be pending.
    So you need to perform below small step throuw AWS CLI:
    1. copy data stream ARN from cloudformation stack > Resources > Data stream with name like 'clw-log-processor-stream'
        ARN will look like : arn:aws:kinesis:<<Region>>:<<AccountNumber>>:stream/<<data-stream-name>>
    2. copy log destination IAM role ARN from cloudformation stack> resource with name like 'LogDestinationRole*'
    3. Enter above ARN details in below command placeholders and run this command in AWS CLI (Refer this link for configuring up AWS CLI https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-files.html)
    ```
    Run below command in AWS CLI
    aws logs put-destination
        –destination-name “<<LogDestination name you wish to give>>”
        –target-arn “<<Enter kinesis data stream arn created by stack here which is created by stack as part of cdk deploy>>”
        –role-arn “<<Enter log destination role ARN which is created by stack as part of cdk deploy>>”
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
    4. Please note down ARN of log destination which you can use to configure subscription filter across cloudwatch log groups in same or cross account. 
    5. You can also get log destination details using below command if you miss noting down. You can also use this step as verification.
        ```
        aws logs describe-destinations
        ```
    6. you need to configure Splunk HEC URL and Token in Lambda environment variable.

    For more information refer below articles
    Trouble shooting common CDK issues : https://docs.aws.amazon.com/cdk/v2/guide/troubleshooting.html#troubleshooting_app_required
    About HTTP Event Collector Indexer Acknowledgment https://docs.splunk.com/Documentation/Splunk/9.0.4/Data/AboutHECIDXAck


## How it works

1. It will create kinesis data stream which will receive streaming logs from cloudwatch log groups. For this cloud watch log groups need to have subscription filter created to log destination.
2. Kinesis data stream will be trigger or event source for Lambda function. So lambda will receive log streams ingested by various applications via cloudwatch log groups.
3. Lambda will decompress log streams and decode Base64 strings. It will then send log events to splunk using web api URL provided by splunk platform. 
4. Log streams will appear near real time in splunk dashboard (search & reporting)


## Testing

1. Create simple test lambda function which will perform some operations and write some logs.
2. The lambda function logs will be visible initially in "/aws/lambda/<function-name>" log group.
3. Go to cloudwatch console > log groups > click on particular log group > go to subscriptions > create subscription with 'Kinesis Stream' as destination. Use Log destination ARN which you have noted during creating subscription.
4. You can create API gateway in front of test lambda function or call your function from another test function. Do not use test function capability on lambda console as it doesn't generate logs in required format and certain sections are not populated. This will not be the case if you use lambda behind api gateway or invoke it using other lambda or other invoking mechanism except on console testing.
5. You can monitor function for success rate. Once your test function and actual log processor function has sucessful invocations. You can go to splunk platform and use 'search and reporting' module to search your logs. Try to log unique strings from your test function so you can find it in splunk almost near real time.

Congratulations ! You have successfully tested end to end flow after this.

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
1. Confirm the stack has been deleted
    ```bash
    aws cloudformation list-stacks --query "StackSummaries[?contains(StackName,'STACK_NAME')].StackStatus"
    ```
----
Copyright 2023 Amazon.com, Inc. or its affiliates. All Rights Reserved.

SPDX-License-Identifier: MIT-0
