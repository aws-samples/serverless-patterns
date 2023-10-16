# Transactional Outbox Microservice Pattern implementation with Amazon DynamoDB

The transactional outbox pattern resolves the dual write operations issue that occurs in distributed systems when a single operation involves both a database write operation and a message or event notification. A dual write operation occurs when an application writes to two different systems; for example, when a microservice needs to persist data in the database and send a message to notify other systems. A failure in one of these operations might result in inconsistent data.

Learn more about this pattern at Serverless Land Patterns: << Add the live URL here >>

Important: this application uses various AWS services and there are costs associated with these services after the Free Tier usage - please see the [AWS Pricing page](https://aws.amazon.com/pricing/) for details. You are responsible for any AWS costs incurred. No warranty is implied in this example.

## Requirements

* [Create an AWS account](https://portal.aws.amazon.com/gp/aws/developer/registration/index.html) if you do not already have one and log in. The IAM user that you use must have sufficient permissions to make necessary AWS service calls and manage AWS resources.
* [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html) installed and configured
* [Git Installed](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)
* [AWS Serverless Application Model](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-sam-cli-install.html) (AWS SAM) installed
* [Create MSK Cluster and order-notification-event-topic topic](https://docs.aws.amazon.com/msk/latest/developerguide/create-cluster.html)

## Deployment Instructions

1. Create a new directory, navigate to that directory in a terminal and clone the GitHub repository:
    ``` 
    git clone https://github.com/aws-samples/serverless-patterns
    ```
1. #### Deploying order-service, order-event-outbox-service and  notification-service microservices
1. Go inside the directory using ```cd dynamodb-streams-to-msk-outbox-pattern-java``` command.
2. Edit the template.yaml provide SecurityGroupIds and SubnetIds in VpcConfig section, bootstrap_server url of MSK Cluster Endpoint, update Policies section for Resource MSK cluster, topic and group arn and update Stream property in Events section with MSK cluster arn
3. Use AWS SAM to build the application:
    ```
   sam build
    ```
4. Use AWS SAM to deploy the AWS resources
    ```
   sam deploy --guided
    ```
5. During the prompts:
    * Enter a stack name
    * Enter the desired AWS Region
    * Allow SAM CLI to create IAM roles with the required permissions.

    Once you have run `sam deploy --guided` mode and saved arguments to a configuration file (samconfig.toml), you can use `sam deploy` in future to use these defaults.
6. Copy the value of `Rest POST endpoint URL` from the output once SAM executes successfully.


1. Note the outputs from the SAM deployment process. These contain the resource names and/or ARNs which are used for testing.

## How it works

1. In this sample implementation, Amazon API Gateway makes a POST call to the AWS Lambda with Customer and Order details.
2. Lambda receive the Order request and make call to DynamoDB to update the Order Order Item detail items and  OrderOutbox table with  TransactWriteItems. Amazon DynamoDB supports transaction and TransactWriteItems is a synchronous write operation that groups up to 100 action requests.
3. DynamoDB Streams is enabled on the OrderOutbox table, which captures a time-ordered sequence of item-level modifications in the DynamoDB table in near real time.
4. Amazon DynamoDB is integrated with AWS Lambda so that you can create triggers—pieces of code that automatically respond to events in DynamoDB Streams. With triggers, you can build applications that react to data modifications in DynamoDB tables.
5. OrderOutboxEventHandler Lambda in order-event-outbox-service microservice listens to Outbox DynamoDB Stream and reads event and pusblish the message to Amazon MSK order-notification-event-topic.
6. Amazon MSK as an event source operates similarly to using Amazon Simple Queue Service (Amazon SQS) or Amazon Kinesis. Lambda internally polls for new messages from the event source and then synchronously invokes the target Lambda function. Lambda reads the messages in batches and provides these to your function as an event payload.
7. Notification service Lambda listening to MSK order-notification-event-topic for order confirmation event and  process the message.

## Testing

This solution is tested using Postman, cli or any rest client.
1. Post the message to create the order, url is output of order-service SAM deployment
```
{
	"customerId": "1d4e4c4d-76df-4146-8545-4b01cd4747a7",
	"price": 2,
	"items": [{
		"productId": "1234",
		"quantity": 4,
		"price": 2
	}]
}
```

2. On making the create order it will make enter into Order, OrderItem and OrderNotificationOutbox table, Login to AWS account and check the item entries into DynamoDB tables.
3. OrderNotificationOutbox table has DynamoDB streams enabled and  Order-event-notification-service Lambda integrated with OrderNotificationOutbox table Stream
4. Once Order-event-notification-service Lambda receive the stream Event it publish to MSK
5. Notification-service Lambda is integrated with MSK which listen to order-notification-event-topic and process the notification events.

## Cleanup
 
1. Delete the all three stacks
    ```bash
    sam delete --stack-name STACK_NAME
    ```
1. Confirm the stack has been deleted
    ```bash
    aws cloudformation list-stacks --query "StackSummaries[?contains(StackName,'STACK_NAME')].StackStatus"
    ```
----
Copyright 2023 Amazon.com, Inc. or its affiliates. All Rights Reserved.

SPDX-License-Identifier: MIT-0