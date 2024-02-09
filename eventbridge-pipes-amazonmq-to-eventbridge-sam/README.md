# Amazon MQ to Amazon EventBridge Message Bus using Amazon EventBridge Pipes

This pattern showcases the use of Amazon EventBridge Pipes to forward events to an Amazon EventBridge custom Message Bus. Using this pattern, events placed on a queue on an Amazon MQ (ActiveMQ) broker are consumed by Amazon EventBridge Pipes which performs a basic transformation and places events on a Amazon EventBridge custom Message Bus. A rule defined on the Amazon EventBridge custom Message Bus writes events received to an Amazon CloudWatch Log Group. This pattern supports an Amazon MQ ActiveMQ broker deployed in a Private VPC (Virtual Private Cloud) or with Public Access enabled however in all cases the Amazon MQ instances must deployed in a subnet with a route to the public Internet.

Learn more about this pattern at Serverless Land Patterns: <https://serverlessland.com/patterns/eventbridge-pipes-amazonmq-to-eventbridge-sam>

Important: this application uses various AWS services and there are costs associated with these services after the Free Tier usage - please see the [AWS Pricing page](https://aws.amazon.com/pricing/) for details. You are responsible for any AWS costs incurred. No warranty is implied in this example.

## Requirements

* [Create an AWS account](https://portal.aws.amazon.com/gp/aws/developer/registration/index.html) if you do not already have one and log in. The IAM user that you use must have sufficient permissions to make necessary AWS service calls and manage AWS resources.
* [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html) installed and configured
* [Git Installed](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)
* [AWS Serverless Application Model](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-sam-cli-install.html) (AWS SAM) installed

## Deployment Instructions

1. First, using the [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html), create a new AWS Secret Manager secret that will hold a credential that will be used to access the Amazon MQ broker in the AWS Region where the pattern will be deployed.

```bash
aws secretsmanager create-secret --name MQaccess --secret-string '{"username": "your-username", "password": "your-password"}'
```

1. Create a new directory, navigate to that directory in a terminal and clone the GitHub repository:

    ```bash
    git clone https://github.com/aws-samples/serverless-patterns
    ```

1. Change directory to the pattern directory:

    ```bash
    cd eventbridge-pipes-amazonmq-to-eventbridge-sam
    ```

1. From the command line, use AWS SAM to deploy the AWS resources for the pattern as specified in the template.yml file:

    ```bash
    sam deploy --guided
    ```

1. During the prompts:
    * Enter a stack name
    * Enter the desired AWS Region
    * Enter the ARN of the AWS Secrets Manager secret created in the first step for the parameter `MQSecretARN`
    * Enter a VPC Id for the parameter `MQVpcId` for the VPC where the Amazon MQ cluster will be deployed
    * Enter a Subnet Id for the  parameter `MQSubnetId` for the Subnet where the Amazon MQ cluster will be deployed
    * Optionally, adjust the default parameters (see `template.yaml` for descriptions of each)
    * Allow SAM CLI to create IAM roles with the required permissions.

    Once you have run `sam deploy --guided` mode once and saved arguments to a configuration file (samconfig.toml), you can use `sam deploy` in future to use these defaults.

1. Note the outputs from the SAM deployment process. These contain the resource names and/or ARNs which are used for testing.

## How it works

![Architecture Overview](./img/arch.png)

Amazon MQ queue is configured as a source for an Amazon EventBridge Pipe. The pipe consumes events placed on the queue and sends these to an Amazon EventBridge custom message bus. Amazon EventBridge Pipe performs a simple transformation of the event payload adding some meta data about the Pipe producing the event during processing. An Amazon EventBridge rule then processes any events produced by the Pipe to a CloudWatch Log Group configured to receive the events. The CloudWatch Log target on the Amazon EventBridge could be replaced with another target to build event-driven services with native AWS integrations reacting to events produced on a queue within an Amazon MQ.

## Testing

To test this pattern you need to open **CloudWatch Logs** with the name provided for the AWS SAM *Parameters* `CloudWatchLogGroup`, by default this Log Group will be `/aws/events/amazonmq-to-eventbridge`.

Next, login to the AmazonMQ Management interface using the address provided in the AWS SAM *Output* `MQBrokerManagementURI` and the credentials you created in the first deployment step.

Whilst logged onto the AmazonMQ Management interface, navigate to *Queues*. Under the *Operations* for the Queue with the name provided for the AWS SAM *Parameters* `MQQueueName` (default: `app-events`) click **Send To**

In the *Message Body* field enter a JSON payload and click **Send** e.g.

```json
{
    "user" : "test",
    "event" : "UserLoggedOut",
    "details" : "This is just an example"
}
```

Switch back to **CloudWatch Logs** and confirm that the event has been written. You should have a payload similar to the following:

```json
{
    "version": "0",
    "id": "11111111-2222-3333-4444-7bd8348cd732",
    "detail-type": "ApplicationStateChanged",
    "source": "myapp.monolith",
    "account": "12345678912",
    "time": "2023-11-10T18:23:39Z",
    "region": "us-east-1",
    "resources": [],
    "detail": {
        "pipeArn": "arn:aws:pipes:us-east-1:12345678912:pipe/amazonmq-to-eventbridge",
        "pipeIngestionTime": "2023-11-10T18:23:38.979Z",
        "Payload": {
            "messageID": "ID:11111111-2222-3333-4444-7bd8348cd732-1-40165-1699640114217-4:1:1:1:1",
            "messageType": "jms/text-message",
            "timestamp": 1699640618566,
            "deliveryMode": 1,
            "correlationID": "",
            "replyTo": "null",
            "destination": {
                "physicalName": "app-events"
            },
            "redelivered": false,
            "type": "",
            "expiration": 0,
            "priority": 0,
            "data": {
                "user": "test",
                "event": "UserLoggedOut",
                "details": "This is just an example"
            },
            "brokerInTime": 1699640618567,
            "brokerOutTime": 1699640618581,
            "eventSourceArn": "arn:aws:mq:us-east-1:12345678912:broker:ActiveMQSAM:11111111-2222-3333-4444-7bd8348cd732",
            "eventSource": "aws:mq"
        }
    }
}
```

Please Note: If deploying this pattern with the AWS SAM *Parameters* `MQPubliclyAccessible` set to `false` (Default behavior), you will need to access the AmazonMQ Management interface from an instance running within the Amazon VPC hosting the broker.

## Cleanup

1. Delete the stack

    ```bash
    sam delete
    ```

1. Confirm the stack has been deleted

    ```bash
    aws cloudformation list-stacks --query "StackSummaries[?contains(StackName,'STACK_NAME')].StackStatus"
    ```

1. Delete the AWS Secret Manager secret created to hold the credentials for the AmazonMQ broker

    ```bash
    aws secretsmanager delete-secret --secret-id arn:aws:secretsmanager:us-east-1:12345678912:secret:MQaccess-ABCD --force-delete-without-recovery 
    ```

----
Copyright 2024 Amazon.com, Inc. or its affiliates. All Rights Reserved.

SPDX-License-Identifier: MIT-0
