# EventBridge to SQS to ECS

This project contains sample AWS CDK code to integrate Amazon EventBridge, Amazon SQS and Amazon Elastic Container Service (ECS). As a new event is sent to EventBridge, it is queued in SQS. SQS, in turn, spins up ECS tasks based on the number of messages available for retrieval from the queue.
Learn more about this pattern at Serverless Land Patterns: https://serverlessland.com/patterns/eventbridge-sqs-ecs-cdk

Important: this application uses various AWS services and there are costs associated with these services after the Free Tier usage - please see the AWS Pricing page (https://aws.amazon.com/pricing/) for details. You are responsible for any AWS costs incurred. No warranty is implied in this example.


## Requirements

* Create an AWS account (https://portal.aws.amazon.com/gp/aws/developer/registration/index.html) if you do not already have one and log in. The IAM user that you use must have sufficient permissions to make necessary AWS service calls and manage AWS resources.
* AWS CLI (https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html) installed and configured
* Git Installed (https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)
* Node and NPM (https://nodejs.org/en/download/) installed
* Docker (https://docs.docker.com/get-started/) installed and configured
* Python, pip (https://docs.aws.amazon.com/cdk/latest/guide/work-with-cdk-python.html) installed
* AWS Cloud Development Kit (https://docs.aws.amazon.com/cdk/latest/guide/cli.html) (AWS CDK) installed

## Deployment Instructions


1. Create a new directory, navigate to that directory in a terminal and clone the GitHub repository:
    ``` 
    git clone https://github.com/aws-samples/serverless-patterns
    ```
2. Change directory to the pattern directory:
    ```
    cd eventbridge-sqs-ecs-cdk/src
    ```
3. From the command line, use npm to install the development dependencies:
    ```
    npm install    
    ```
4. Install the project dependencies
    ```
    python -m pip install -r python-app/requirements.txt
    ```
5. Deploy the stack to your default AWS account and region.
    ```
    cdk deploy
    ```

## How it works

The CDK stack deploys the resources required to run the application. An event stored in a file in json format is sent to EventBridge and queued in a SQS queue which in turn triggers the task execution on ECS. The solution also creates step scaling of ECS tasks based on the number of messages available for retrieval from the queue. After the task is finished, an item from the queue is deleted which automatically scales down the ECS cluster and task.

## Testing

Send custom events to Amazon EventBridge so that they can be matched to rules using put-events command

For an example, an event in event.json file is as follows- 
[
    {
      "EventBusName": "test-bus-cdk",
      "Source": "eb-sqs-ecs",
      "DetailType": "message-for-queue",
      "Detail": "{\"message\":\"Hello CDK world!\"}"
    }
  ]

Execute the following command to put event on EventBridge-

```
aws events put-events --entries file://event.json 

```

After execution, you see output similar to following in the command line-
{
    "FailedEntryCount": 0,
    "Entries": [
        {
            "EventId": "<Event ID created>"
        }
    ]
}

In the AWS Management Console, you’ll notice a new EventBridge event bus, a SQS queue, an ECS cluster and a task. You can monitor CloudWatch logs and notice the log for queue reading, messages read and deleted messages.  


## Cleanup
 
Run the given command to delete the resources that were created. It might take some time for the CloudFormation stack to get deleted.

```
cdk destroy
```
----
Copyright 2023 Amazon.com, Inc. or its affiliates. All Rights Reserved.

SPDX-License-Identifier: MIT-0
