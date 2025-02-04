# API Gateway to SQS with Priority-Based Message Routing

This pattern demonstrates how to implement direct integration between API Gateway and multiple SQS queues using mapping templates, enabling dynamic message routing based on request parameters without using Lambda functions.

## Architecture

[The ServerlessLand team will create this diagram]

## Description

The pattern creates:
- An API Gateway REST API with a POST method
- Three SQS queues (high-priority, default, and low-priority)
- IAM roles and policies for API Gateway to send messages to SQS
- A VTL mapping template for dynamic queue routing

The solution enables:
- Dynamic routing of messages to different queues based on a priority parameter
- Direct integration between API Gateway and SQS without Lambda
- Request transformation using mapping templates

## Important note

Deploying this pattern may incur costs. Be sure to delete the resources after testing to avoid ongoing charges.

## Prerequisites

* AWS CLI installed and configured
* Git

## Deployment Instructions

1. Deploy the AWS CloudFormation template:
```bash
aws cloudformation deploy \
  --template-file template.yaml \
  --stack-name api-priority-sqs \
  --capabilities CAPABILITY_IAM

2. Retrieve the API Gateway endpoint URL from CloudFormation outputs:
```bash
aws cloudformation describe-stacks \
  --stack-name api-priority-sqs \
  --query 'Stacks[0].Outputs[?OutputKey==`ApiEndpoint`].OutputValue' \
  --output text

3. Send a message to the default queue (no priority parameter):
```bash
curl --location --request POST 'YOUR_API_ENDPOINT' \
--header 'Content-Type: application/json' \
--data-raw '{"message": "default priority message"}'

Expected success response:
```bash
{
    "message": "Message sent successfully"
}

You can verify message delivery by checking the respective SQS queues in the AWS Console.
## Example Event
```bash
{
    "message": "test message",
    "timestamp": "2025-01-27T13:20:58Z"
}

## Mapping Template
The following VTL mapping template is used to route messages based on the priority parameter:
```bash
#set($priority = "default-queue")
#if($input.params('priority') == "low")
    #set($priority = "low-queue")
#elseif($input.params('priority') == "high")
    #set($priority = "high-queue")
#end

{
    "QueueUrl": "https://sqs.${context.region}.amazonaws.com/${context.accountId}/$priority",
    "MessageBody": "$util.escapeJavaScript($input.json('$'))"
}

## Cleanup
1. Delete the CloudFormation stack:
```bash
aws cloudformation delete-stack --stack-name api-priority-sqs

2. Confirm the stack has been deleted:
```bash
aws cloudformation list-stacks --query 'StackSummaries[?contains(StackName,`api-priority-sqs`)]'

## Resources

* [API Gateway documentation](https://docs.aws.amazon.com/apigateway/latest/developerguide/welcome.html)
* [Amazon SQS documentation](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/welcome.html)
* [API Gateway Mapping Template Reference](https://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-mapping-template-reference.html)
* [SQS SendMessage API Reference](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/APIReference/API_SendMessage.html)



