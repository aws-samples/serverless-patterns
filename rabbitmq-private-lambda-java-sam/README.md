# rabbitmq-private-lambda-java-sam
# Java AWS Lambda RabbitMQ (in private subnets) consumer, using AWS SAM

This pattern is an example of a Lambda function written in Java that consumes messages from Amazon MQ (RabbitMQ)

This project contains source code and supporting files for a serverless application that you can deploy with the SAM CLI. It includes the following files and folders.

- rabbitmq_consumer_dynamo_sam/rabbit_event_consumer_function/src/main/java - Code for the application's Lambda function that will listen for Amazon MQ (RabbitMQ) messages and write them to a DynamoDB table
- rabbit_message_sender_json/src/main/java - Code for publishing messages with JSON payload into an Amazon MQ (RabbitMQ cluster), that will in turn be consumed by the Lambda function
- rabbit_consumer_dynamo_sam/template_original.yaml - A template that defines the application's Lambda function to be used by SAM to deploy the lambda function
- RabbitMQAndClientEC2.yaml - A Cloudformation template file that can be used to deploy an Amazon MQ (RabbitMQ) cluster and also deploy an EC2 machine with all pre-requisities already installed, so you can directly build and deploy the lambda function and test it out.
- create_rabbit_queue.sh - A shell script that can be used to connect to the Amazon MQ (RabbitMQ) brokers to create virtualhosts, exchanges and queues, required for the lambda functions event listener

Important: this application uses various AWS services and there are costs associated with these services after the Free Tier usage - please see the [AWS Pricing page](https://aws.amazon.com/pricing/) for details. You are responsible for any AWS costs incurred. No warranty is implied in this example.

## Requirements

* [Create an AWS account](https://portal.aws.amazon.com/gp/aws/developer/registration/index.html) if you do not already have one and log in. The IAM user that you use must have sufficient permissions to make necessary AWS service calls and manage AWS resources.

## Run the Cloudformation template to create the Amazon MQ (RabbitMQ) Cluster and Client EC2 machine

* [Run the Cloudformation template using the file RabbitMQAndClientEC2.yaml] - You can go to the AWS Cloudformation console, create a new stack by specifying the template file. You can keep the defaults for input parameters or modify them as necessary. Wait for the Cloudformation stack to be created. This Cloudformation template will create an Amazon MQ (RabbitMQ) cluster. It will also create an EC2 machine that you can use as a client.

* [Connect to the EC2 machine] - Once the CloudFormation stack is created, you can go to the EC2 console and log into the machine using either "Connect using EC2 Instance Connect" or "Connect using EC2 Instance Connect Endpoint" option under the "EC2 Instance Connect" tab.
Note: You may need to wait for some time after the CloudFormation stack is created, as some UserData scripts continue running after the Cloudformation stack shows Created.

## Pre-requisites to Deploy the sample Lambda function

The EC2 machine that was created by running the CloudFormation template has all the software that will be needed to deploy the Lambda function.

The AWS SAM CLI is a serverless tool for building and testing Lambda applications.

* Java - On the EC2 machine, we have installed the version of Java that you selected. We have installed Amazon Corrretto JDK of the version that you had selected at the time of specifying the input parameters in the Cloudformation template. At the time of publishing this pattern, only Java versions 11, 17 and 21 are supported by AWS SAM
* Maven - On the EC2 machine, we have installed Maven (https://maven.apache.org/install.html)
* AWS SAM CLI - We have installed the AWS SAM CLI (https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-sam-cli-install.html)

We have also cloned the Github repository for serverless-patterns on the EC2 machine already by running the below command
    ``` 
    git clone https://github.com/aws-samples/serverless-patterns.git
    ```
Change directory to the pattern directory:
    ```
    cd serverless-patterns/rabbit-private-lambda-java-sam
    ```

## Use the SAM CLI to build and deploy the lambda function

Build your application with the `sam build` command.

```bash
cd rabbit_consumer_dynamo_sam
sam build
```

The SAM CLI installs dependencies defined in `rabbitmq_consumer_dynamo_sam/rabbit_event_consumer_function/pom.xml`, creates a deployment package, and saves it in the `.aws-sam/build` folder.

```

## Test the build locally

Test a single function by invoking it directly with a test event. An event is a JSON document that represents the input that the function receives from the event source. Test events are included in the `events` folder in this project.

Run functions locally and invoke them with the `sam local invoke` command.

```bash
sam local invoke --event events/event.json
```

You should see a response such as the below:

```
***** Begin sam local invoke response *****

Invoking com.amazonaws.services.lambda.samples.events.rabbitmq.HandlerRabbitMQ::handleRequest (java21)                                                 
Local image is up-to-date                                                                                                                              
Using local image: public.ecr.aws/lambda/java:21-rapid-x86_64.                                                                                         
                                                                                                                                                       
Mounting                                                                                                                                               
/home/ec2-user/serverless-patterns/rabbitmq-private-lambda-java-sam/rabbitmq_consumer_dynamo_sam/.aws-sam/build/LambdaRabbitMQConsumerJavaFunction as  
/var/task:ro,delegated, inside runtime container                                                                                                       
SAM_CONTAINER_ID: 17589682ce0fd9b8172a1cd21fc5bccabb75ba4b27a0be58996c78e4ae7d3341                                                                     
Picked up JAVA_TOOL_OPTIONS: -XX:+TieredCompilation -XX:TieredStopAtLevel=1
Begin Event *************{"eventSource":"aws:rmq","eventSourceArn":"arn:aws:mq:us-west-2:664251831272:broker:ib-rabbitmq-broker:b-22450561-3f76-4004-813d-392346f054fe","rmqMessagesByQueue":{"LambdaRabbitMQQueue::/":[{"basicProperties":{"contentType":"text/plain","contentEncoding":"UTF-8","headers":{"MessageNumberInBatch":1,"MessageBatchIdentifier":{"bytes":[84,101,115,116,77,101,115,115,97,103,101,48,51,45,48,55,45,48,50,45,50,48,50,51,45,48,49,45,48,55,45,50,48]}},"deliveryMode":2,"priority":1,"correlationId":"TestMessage03-07-02-2023-01-07-20-1","replyTo":null,"expiration":60000,"messageId":"TestMessage03-07-02-2023-01-07-20:1","timestamp":"Jul 2, 2023, 1:30:34 AM","type":"JsonRabbitMQProducer","userId":"admin","appId":"rabbitmq.producer.JsonRabbitMQProducer","clusterId":"b-22450561-3f76-4004-813d-392346f054fe.mq.us-west-2.amazonaws.com","bodySize":321},"redelivered":false,"data":"eyJmaXJzdG5hbWUiOiJKb3NlcGhpbmUiLCJsYXN0bmFtZSI6IkRhcmFrankiLCJjb21wYW55IjoiXCJDaGFuYXksIEplZmZyZXkgQSBFc3FcIiIsInN0cmVldCI6IjQgQiBCbHVlIFJpZGdlIEJsdmQiLCJjaXR5IjoiQnJpZ2h0b24iLCJjb3VudHkiOiJMaXZpbmdzdG9uIiwic3RhdGUiOiJNSSIsInppcCI6IjQ4MTE2IiwiaG9tZVBob25lIjoiODEwLTI5Mi05Mzg4IiwiY2VsbFBob25lIjoiODEwLTM3NC05ODQwIiwiZW1haWwiOiJqb3NlcGhpbmVfZGFyYWtqeUBkYXJha2p5Lm9yZyIsIndlYnNpdGUiOiJodHRwOi8vd3d3LmNoYW5heWplZmZyZXlhZXNxLmNvbSJ9"},{"basicProperties":{"contentType":"text/plain","contentEncoding":"UTF-8","headers":{"MessageNumberInBatch":2,"MessageBatchIdentifier":{"bytes":[84,101,115,116,77,101,115,115,97,103,101,48,51,45,48,55,45,48,50,45,50,48,50,51,45,48,49,45,48,55,45,50,48]}},"deliveryMode":2,"priority":1,"correlationId":"TestMessage03-07-02-2023-01-07-20-2","replyTo":null,"expiration":60000,"messageId":"TestMessage03-07-02-2023-01-07-20:2","timestamp":"Jul 2, 2023, 1:30:34 AM","type":"JsonRabbitMQProducer","userId":"admin","appId":"rabbitmq.producer.JsonRabbitMQProducer","clusterId":"b-22450561-3f76-4004-813d-392346f054fe.mq.us-west-2.amazonaws.com","bodySize":297},"redelivered":false,"data":"eyJmaXJzdG5hbWUiOiJBcnQiLCJsYXN0bmFtZSI6IlZlbmVyZSIsImNvbXBhbnkiOiJcIkNoZW1lbCwgSmFtZXMgTCBDcGFcIiIsInN0cmVldCI6IjggVyBDZXJyaXRvcyBBdmUgIzU0IiwiY2l0eSI6IkJyaWRnZXBvcnQiLCJjb3VudHkiOiJHbG91Y2VzdGVyIiwic3RhdGUiOiJOSiIsInppcCI6IjgwMTQiLCJob21lUGhvbmUiOiI4NTYtNjM2LTg3NDkiLCJjZWxsUGhvbmUiOiI4NTYtMjY0LTQxMzAiLCJlbWFpbCI6ImFydEB2ZW5lcmUub3JnIiwid2Vic2l0ZSI6Imh0dHA6Ly93d3cuY2hlbWVsamFtZXNsY3BhLmNvbSJ9"},{"basicProperties":{"contentType":"text/plain","contentEncoding":"UTF-8","headers":{"MessageNumberInBatch":3,"MessageBatchIdentifier":{"bytes":[84,101,115,116,77,101,115,115,97,103,101,48,51,45,48,55,45,48,50,45,50,48,50,51,45,48,49,45,48,55,45,50,48]}},"deliveryMode":2,"priority":1,"correlationId":"TestMessage03-07-02-2023-01-07-20-3","replyTo":null,"expiration":60000,"messageId":"TestMessage03-07-02-2023-01-07-20:3","timestamp":"Jul 2, 2023, 1:30:34 AM","type":"JsonRabbitMQProducer","userId":"admin","appId":"rabbitmq.producer.JsonRabbitMQProducer","clusterId":"b-22450561-3f76-4004-813d-392346f054fe.mq.us-west-2.amazonaws.com","bodySize":302},"redelivered":false,"data":"eyJmaXJzdG5hbWUiOiJMZW5uYSIsImxhc3RuYW1lIjoiUGFwcm9ja2kiLCJjb21wYW55IjoiRmVsdHogUHJpbnRpbmcgU2VydmljZSIsInN0cmVldCI6IjYzOSBNYWluIFN0IiwiY2l0eSI6IkFuY2hvcmFnZSIsImNvdW50eSI6IkFuY2hvcmFnZSIsInN0YXRlIjoiQUsiLCJ6aXAiOiI5OTUwMSIsImhvbWVQaG9uZSI6IjkwNy0zODUtNDQxMiIsImNlbGxQaG9uZSI6IjkwNy05MjEtMjAxMCIsImVtYWlsIjoibHBhcHJvY2tpQGhvdG1haWwuY29tIiwid2Vic2l0ZSI6Imh0dHA6Ly93d3cuZmVsdHpwcmludGluZ3NlcnZpY2UuY29tIn0="},{"basicProperties":{"contentType":"text/plain","contentEncoding":"UTF-8","headers":{"MessageNumberInBatch":4,"MessageBatchIdentifier":{"bytes":[84,101,115,116,77,101,115,115,97,103,101,48,51,45,48,55,45,48,50,45,50,48,50,51,45,48,49,45,48,55,45,50,48]}},"deliveryMode":2,"priority":1,"correlationId":"TestMessage03-07-02-2023-01-07-20-4","replyTo":null,"expiration":60000,"messageId":"TestMessage03-07-02-2023-01-07-20:4","timestamp":"Jul 2, 2023, 1:30:34 AM","type":"JsonRabbitMQProducer","userId":"admin","appId":"rabbitmq.producer.JsonRabbitMQProducer","clusterId":"b-22450561-3f76-4004-813d-392346f054fe.mq.us-west-2.amazonaws.com","bodySize":295},"redelivered":false,"data":"eyJmaXJzdG5hbWUiOiJEb25ldHRlIiwibGFzdG5hbWUiOiJGb2xsZXIiLCJjb21wYW55IjoiUHJpbnRpbmcgRGltZW5zaW9ucyIsInN0cmVldCI6IjM0IENlbnRlciBTdCIsImNpdHkiOiJIYW1pbHRvbiIsImNvdW50eSI6IkJ1dGxlciIsInN0YXRlIjoiT0giLCJ6aXAiOiI0NTAxMSIsImhvbWVQaG9uZSI6IjUxMy01NzAtMTg5MyIsImNlbGxQaG9uZSI6IjUxMy01NDktNDU2MSIsImVtYWlsIjoiZG9uZXR0ZS5mb2xsZXJAY294Lm5ldCIsIndlYnNpdGUiOiJodHRwOi8vd3d3LnByaW50aW5nZGltZW5zaW9ucy5jb20ifQ=="},{"basicProperties":{"contentType":"text/plain","contentEncoding":"UTF-8","headers":{"MessageNumberInBatch":5,"MessageBatchIdentifier":{"bytes":[84,101,115,116,77,101,115,115,97,103,101,48,51,45,48,55,45,48,50,45,50,48,50,51,45,48,49,45,48,55,45,50,48]}},"deliveryMode":2,"priority":1,"correlationId":"TestMessage03-07-02-2023-01-07-20-5","replyTo":null,"expiration":60000,"messageId":"TestMessage03-07-02-2023-01-07-20:5","timestamp":"Jul 2, 2023, 1:30:34 AM","type":"JsonRabbitMQProducer","userId":"admin","appId":"rabbitmq.producer.JsonRabbitMQProducer","clusterId":"b-22450561-3f76-4004-813d-392346f054fe.mq.us-west-2.amazonaws.com","bodySize":292},"redelivered":false,"data":"eyJmaXJzdG5hbWUiOiJTaW1vbmEiLCJsYXN0bmFtZSI6Ik1vcmFzY2EiLCJjb21wYW55IjoiXCJDaGFwbWFuLCBSb3NzIEUgRXNxXCIiLCJzdHJlZXQiOiIzIE1jYXVsZXkgRHIiLCJjaXR5IjoiQXNobGFuZCIsImNvdW50eSI6IkFzaGxhbmQiLCJzdGF0ZSI6Ik9IIiwiemlwIjoiNDQ4MDUiLCJob21lUGhvbmUiOiI0MTktNTAzLTI0ODQiLCJjZWxsUGhvbmUiOiI0MTktODAwLTY3NTkiLCJlbWFpbCI6InNpbW9uYUBtb3Jhc2NhLmNvbSIsIndlYnNpdGUiOiJodHRwOi8vd3d3LmNoYXBtYW5yb3NzZWVzcS5jb20ifQ=="},{"basicProperties":{"contentType":"text/plain","contentEncoding":"UTF-8","headers":{"MessageNumberInBatch":6,"MessageBatchIdentifier":{"bytes":[84,101,115,116,77,101,115,115,97,103,101,48,51,45,48,55,45,48,50,45,50,48,50,51,45,48,49,45,48,55,45,50,48]}},"deliveryMode":2,"priority":1,"correlationId":"TestMessage03-07-02-2023-01-07-20-6","replyTo":null,"expiration":60000,"messageId":"TestMessage03-07-02-2023-01-07-20:6","timestamp":"Jul 2, 2023, 1:30:34 AM","type":"JsonRabbitMQProducer","userId":"admin","appId":"rabbitmq.producer.JsonRabbitMQProducer","clusterId":"b-22450561-3f76-4004-813d-392346f054fe.mq.us-west-2.amazonaws.com","bodySize":289},"redelivered":false,"data":"eyJmaXJzdG5hbWUiOiJNaXRzdWUiLCJsYXN0bmFtZSI6IlRvbGxuZXIiLCJjb21wYW55IjoiTW9ybG9uZyBBc3NvY2lhdGVzIiwic3RyZWV0IjoiNyBFYWRzIFN0IiwiY2l0eSI6IkNoaWNhZ28iLCJjb3VudHkiOiJDb29rIiwic3RhdGUiOiJJTCIsInppcCI6IjYwNjMyIiwiaG9tZVBob25lIjoiNzczLTU3My02OTE0IiwiY2VsbFBob25lIjoiNzczLTkyNC04NTY1IiwiZW1haWwiOiJtaXRzdWVfdG9sbG5lckB5YWhvby5jb20iLCJ3ZWJzaXRlIjoiaHR0cDovL3d3dy5tb3Jsb25nYXNzb2NpYXRlcy5jb20ifQ=="},{"basicProperties":{"contentType":"text/plain","contentEncoding":"UTF-8","headers":{"MessageNumberInBatch":7,"MessageBatchIdentifier":{"bytes":[84,101,115,116,77,101,115,115,97,103,101,48,51,45,48,55,45,48,50,45,50,48,50,51,45,48,49,45,48,55,45,50,48]}},"deliveryMode":2,"priority":1,"correlationId":"TestMessage03-07-02-2023-01-07-20-7","replyTo":null,"expiration":60000,"messageId":"TestMessage03-07-02-2023-01-07-20:7","timestamp":"Jul 2, 2023, 1:30:34 AM","type":"JsonRabbitMQProducer","userId":"admin","appId":"rabbitmq.producer.JsonRabbitMQProducer","clusterId":"b-22450561-3f76-4004-813d-392346f054fe.mq.us-west-2.amazonaws.com","bodySize":293},"redelivered":false,"data":"eyJmaXJzdG5hbWUiOiJMZW90YSIsImxhc3RuYW1lIjoiRGlsbGlhcmQiLCJjb21wYW55IjoiQ29tbWVyY2lhbCBQcmVzcyIsInN0cmVldCI6IjcgVyBKYWNrc29uIEJsdmQiLCJjaXR5IjoiU2FuIEpvc2UiLCJjb3VudHkiOiJTYW50YSBDbGFyYSIsInN0YXRlIjoiQ0EiLCJ6aXAiOiI5NTExMSIsImhvbWVQaG9uZSI6IjQwOC03NTItMzUwMCIsImNlbGxQaG9uZSI6IjQwOC04MTMtMTEwNSIsImVtYWlsIjoibGVvdGFAaG90bWFpbC5jb20iLCJ3ZWJzaXRlIjoiaHR0cDovL3d3dy5jb21tZXJjaWFscHJlc3MuY29tIn0="},{"basicProperties":{"contentType":"text/plain","contentEncoding":"UTF-8","headers":{"MessageNumberInBatch":8,"MessageBatchIdentifier":{"bytes":[84,101,115,116,77,101,115,115,97,103,101,48,51,45,48,55,45,48,50,45,50,48,50,51,45,48,49,45,48,55,45,50,48]}},"deliveryMode":2,"priority":1,"correlationId":"TestMessage03-07-02-2023-01-07-20-8","replyTo":null,"expiration":60000,"messageId":"TestMessage03-07-02-2023-01-07-20:8","timestamp":"Jul 2, 2023, 1:30:34 AM","type":"JsonRabbitMQProducer","userId":"admin","appId":"rabbitmq.producer.JsonRabbitMQProducer","clusterId":"b-22450561-3f76-4004-813d-392346f054fe.mq.us-west-2.amazonaws.com","bodySize":309},"redelivered":false,"data":"eyJmaXJzdG5hbWUiOiJTYWdlIiwibGFzdG5hbWUiOiJXaWVzZXIiLCJjb21wYW55IjoiVHJ1aGxhciBBbmQgVHJ1aGxhciBBdHR5cyIsInN0cmVldCI6IjUgQm9zdG9uIEF2ZSAjODgiLCJjaXR5IjoiU2lvdXggRmFsbHMiLCJjb3VudHkiOiJNaW5uZWhhaGEiLCJzdGF0ZSI6IlNEIiwiemlwIjoiNTcxMDUiLCJob21lUGhvbmUiOiI2MDUtNDE0LTIxNDciLCJjZWxsUGhvbmUiOiI2MDUtNzk0LTQ4OTUiLCJlbWFpbCI6InNhZ2Vfd2llc2VyQGNveC5uZXQiLCJ3ZWJzaXRlIjoiaHR0cDovL3d3dy50cnVobGFyYW5kdHJ1aGxhcmF0dHlzLmNvbSJ9"},{"basicProperties":{"contentType":"text/plain","contentEncoding":"UTF-8","headers":{"MessageNumberInBatch":9,"MessageBatchIdentifier":{"bytes":[84,101,115,116,77,101,115,115,97,103,101,48,51,45,48,55,45,48,50,45,50,48,50,51,45,48,49,45,48,55,45,50,48]}},"deliveryMode":2,"priority":1,"correlationId":"TestMessage03-07-02-2023-01-07-20-9","replyTo":null,"expiration":60000,"messageId":"TestMessage03-07-02-2023-01-07-20:9","timestamp":"Jul 2, 2023, 1:30:34 AM","type":"JsonRabbitMQProducer","userId":"admin","appId":"rabbitmq.producer.JsonRabbitMQProducer","clusterId":"b-22450561-3f76-4004-813d-392346f054fe.mq.us-west-2.amazonaws.com","bodySize":312},"redelivered":false,"data":"eyJmaXJzdG5hbWUiOiJLcmlzIiwibGFzdG5hbWUiOiJNYXJyaWVyIiwiY29tcGFueSI6IlwiS2luZywgQ2hyaXN0b3BoZXIgQSBFc3FcIiIsInN0cmVldCI6IjIyOCBSdW5hbXVjayBQbCAjMjgwOCIsImNpdHkiOiJCYWx0aW1vcmUiLCJjb3VudHkiOiJCYWx0aW1vcmUgQ2l0eSIsInN0YXRlIjoiTUQiLCJ6aXAiOiIyMTIyNCIsImhvbWVQaG9uZSI6IjQxMC02NTUtODcyMyIsImNlbGxQaG9uZSI6IjQxMC04MDQtNDY5NCIsImVtYWlsIjoia3Jpc0BnbWFpbC5jb20iLCJ3ZWJzaXRlIjoiaHR0cDovL3d3dy5raW5nY2hyaXN0b3BoZXJhZXNxLmNvbSJ9"},{"basicProperties":{"contentType":"text/plain","contentEncoding":"UTF-8","headers":{"MessageNumberInBatch":10,"MessageBatchIdentifier":{"bytes":[84,101,115,116,77,101,115,115,97,103,101,48,51,45,48,55,45,48,50,45,50,48,50,51,45,48,49,45,48,55,45,50,48]}},"deliveryMode":2,"priority":1,"correlationId":"TestMessage03-07-02-2023-01-07-20-10","replyTo":null,"expiration":60000,"messageId":"TestMessage03-07-02-2023-01-07-20:10","timestamp":"Jul 2, 2023, 1:30:34 AM","type":"JsonRabbitMQProducer","userId":"admin","appId":"rabbitmq.producer.JsonRabbitMQProducer","clusterId":"b-22450561-3f76-4004-813d-392346f054fe.mq.us-west-2.amazonaws.com","bodySize":300},"redelivered":false,"data":"eyJmaXJzdG5hbWUiOiJNaW5uYSIsImxhc3RuYW1lIjoiQW1pZ29uIiwiY29tcGFueSI6IlwiRG9ybCwgSmFtZXMgSiBFc3FcIiIsInN0cmVldCI6IjIzNzEgSmVycm9sZCBBdmUiLCJjaXR5IjoiS3VscHN2aWxsZSIsImNvdW50eSI6Ik1vbnRnb21lcnkiLCJzdGF0ZSI6IlBBIiwiemlwIjoiMTk0NDMiLCJob21lUGhvbmUiOiIyMTUtODc0LTEyMjkiLCJjZWxsUGhvbmUiOiIyMTUtNDIyLTg2OTQiLCJlbWFpbCI6Im1pbm5hX2FtaWdvbkB5YWhvby5jb20iLCJ3ZWJzaXRlIjoiaHR0cDovL3d3dy5kb3JsamFtZXNqZXNxLmNvbSJ9"}]}}End Event ***************EventSource = aws:rmqEventSourceARN = arn:aws:mq:us-west-2:664251831272:broker:ib-rabbitmq-broker:b-22450561-3f76-4004-813d-392346f054feNow iterating through Map of all queuesCurrent Queue Name = LambdaRabbitMQQueueNow iterating through each message in this queue - LambdaRabbitMQQueueNow logging a new messageEncodedData = eyJmaXJzdG5hbWUiOiJKb3NlcGhpbmUiLCJsYXN0bmFtZSI6IkRhcmFrankiLCJjb21wYW55IjoiXCJDaGFuYXksIEplZmZyZXkgQSBFc3FcIiIsInN0cmVldCI6IjQgQiBCbHVlIFJpZGdlIEJsdmQiLCJjaXR5IjoiQnJpZ2h0b24iLCJjb3VudHkiOiJMaXZpbmdzdG9uIiwic3RhdGUiOiJNSSIsInppcCI6IjQ4MTE2IiwiaG9tZVBob25lIjoiODEwLTI5Mi05Mzg4IiwiY2VsbFBob25lIjoiODEwLTM3NC05ODQwIiwiZW1haWwiOiJqb3NlcGhpbmVfZGFyYWtqeUBkYXJha2p5Lm9yZyIsIndlYnNpdGUiOiJodHRwOi8vd3d3LmNoYW5heWplZmZyZXlhZXNxLmNvbSJ9DecodedData = {"firstname":"Josephine","lastname":"Darakjy","company":"\"Chanay, Jeffrey A Esq\"","street":"4 B Blue Ridge Blvd","city":"Brighton","county":"Livingston","state":"MI","zip":"48116","homePhone":"810-292-9388","cellPhone":"810-374-9840","email":"josephine_darakjy@darakjy.org","website":"http://www.chanayjeffreyaesq.com"}This person = Person [firstname=Josephine, lastname=Darakjy, company="Chanay, Jeffrey A Esq", street=4 B Blue Ridge Blvd, city=Brighton, county=Livingston, state=MI, zip=48116, homePhone=810-292-9388, cellPhone=810-374-9840, email=josephine_darakjy@darakjy.org, website=http://www.chanayjeffreyaesq.com]Whether Redelivered = falseAppID = rabbitmq.producer.JsonRabbitMQProducerBodySize = 321ClusterId = b-22450561-3f76-4004-813d-392346f054fe.mq.us-west-2.amazonaws.comContentEncoding = UTF-8ContentType = text/plainCorrelationId = TestMessage03-07-02-2023-01-07-20-1DeliveryMode = 2Expiration = 60000MessageId = TestMessage03-07-02-2023-01-07-20:1Priority = 1ReplyTo = nullTimestamp = Jul 2, 2023, 1:30:34 AMType = JsonRabbitMQProducerUserId = adminNow iterating through the headers in this messageHeader Name = MessageNumberInBatch and Header Value = 1Header Name = MessageBatchIdentifier and Header Value = TestMessage03-07-02-2023-01-07-20Now done iterating through the headers in this messageNow done logging a new messageNow logging a new messageEncodedData = eyJmaXJzdG5hbWUiOiJBcnQiLCJsYXN0bmFtZSI6IlZlbmVyZSIsImNvbXBhbnkiOiJcIkNoZW1lbCwgSmFtZXMgTCBDcGFcIiIsInN0cmVldCI6IjggVyBDZXJyaXRvcyBBdmUgIzU0IiwiY2l0eSI6IkJyaWRnZXBvcnQiLCJjb3VudHkiOiJHbG91Y2VzdGVyIiwic3RhdGUiOiJOSiIsInppcCI6IjgwMTQiLCJob21lUGhvbmUiOiI4NTYtNjM2LTg3NDkiLCJjZWxsUGhvbmUiOiI4NTYtMjY0LTQxMzAiLCJlbWFpbCI6ImFydEB2ZW5lcmUub3JnIiwid2Vic2l0ZSI6Imh0dHA6Ly93d3cuY2hlbWVsamFtZXNsY3BhLmNvbSJ9DecodedData = {"firstname":"Art","lastname":"Venere","company":"\"Chemel, James L Cpa\"","street":"8 W Cerritos Ave #54","city":"Bridgeport","county":"Gloucester","state":"NJ","zip":"8014","homePhone":"856-636-8749","cellPhone":"856-264-4130","email":"art@venere.org","website":"http://www.chemeljameslcpa.com"}This person = Person [firstname=Art, lastname=Venere, company="Chemel, James L Cpa", street=8 W Cerritos Ave #54, city=Bridgeport, county=Gloucester, state=NJ, zip=8014, homePhone=856-636-8749, cellPhone=856-264-4130, email=art@venere.org, website=http://www.chemeljameslcpa.com]Whether Redelivered = falseAppID = rabbitmq.producer.JsonRabbitMQProducerBodySize = 297ClusterId = b-22450561-3f76-4004-813d-392346f054fe.mq.us-west-2.amazonaws.comContentEncoding = UTF-8ContentType = text/plainCorrelationId = TestMessage03-07-02-2023-01-07-20-2DeliveryMode = 2Expiration = 60000MessageId = TestMessage03-07-02-2023-01-07-20:2Priority = 1ReplyTo = nullTimestamp = Jul 2, 2023, 1:30:34 AMType = JsonRabbitMQProducerUserId = adminNow iterating through the headers in this messageHeader Name = MessageNumberInBatch and Header Value = 2Header Name = MessageBatchIdentifier and Header Value = TestMessage03-07-02-2023-01-07-20Now done iterating through the headers in this messageNow done logging a new messageNow logging a new messageEncodedData = eyJmaXJzdG5hbWUiOiJMZW5uYSIsImxhc3RuYW1lIjoiUGFwcm9ja2kiLCJjb21wYW55IjoiRmVsdHogUHJpbnRpbmcgU2VydmljZSIsInN0cmVldCI6IjYzOSBNYWluIFN0IiwiY2l0eSI6IkFuY2hvcmFnZSIsImNvdW50eSI6IkFuY2hvcmFnZSIsInN0YXRlIjoiQUsiLCJ6aXAiOiI5OTUwMSIsImhvbWVQaG9uZSI6IjkwNy0zODUtNDQxMiIsImNlbGxQaG9uZSI6IjkwNy05MjEtMjAxMCIsImVtYWlsIjoibHBhcHJvY2tpQGhvdG1haWwuY29tIiwid2Vic2l0ZSI6Imh0dHA6Ly93d3cuZmVsdHpwcmludGluZ3NlcnZpY2UuY29tIn0=DecodedData = {"firstname":"Lenna","lastname":"Paprocki","company":"Feltz Printing Service","street":"639 Main St","city":"Anchorage","county":"Anchorage","state":"AK","zip":"99501","homePhone":"907-385-4412","cellPhone":"907-921-2010","email":"lpaprocki@hotmail.com","website":"http://www.feltzprintingservice.com"}This person = Person [firstname=Lenna, lastname=Paprocki, company=Feltz Printing Service, street=639 Main St, city=Anchorage, county=Anchorage, state=AK, zip=99501, homePhone=907-385-4412, cellPhone=907-921-2010, email=lpaprocki@hotmail.com, website=http://www.feltzprintingservice.com]Whether Redelivered = falseAppID = rabbitmq.producer.JsonRabbitMQProducerBodySize = 302ClusterId = b-22450561-3f76-4004-813d-392346f054fe.mq.us-west-2.amazonaws.comContentEncoding = UTF-8ContentType = text/plainCorrelationId = TestMessage03-07-02-2023-01-07-20-3DeliveryMode = 2Expiration = 60000MessageId = TestMessage03-07-02-2023-01-07-20:3Priority = 1ReplyTo = nullTimestamp = Jul 2, 2023, 1:30:34 AMType = JsonRabbitMQProducerUserId = adminNow iterating through the headers in this messageHeader Name = MessageNumberInBatch and Header Value = 3Header Name = MessageBatchIdentifier and Header Value = TestMessage03-07-02-2023-01-07-20Now done iterating through the headers in this messageNow done logging a new messageNow logging a new messageEncodedData = eyJmaXJzdG5hbWUiOiJEb25ldHRlIiwibGFzdG5hbWUiOiJGb2xsZXIiLCJjb21wYW55IjoiUHJpbnRpbmcgRGltZW5zaW9ucyIsInN0cmVldCI6IjM0IENlbnRlciBTdCIsImNpdHkiOiJIYW1pbHRvbiIsImNvdW50eSI6IkJ1dGxlciIsInN0YXRlIjoiT0giLCJ6aXAiOiI0NTAxMSIsImhvbWVQaG9uZSI6IjUxMy01NzAtMTg5MyIsImNlbGxQaG9uZSI6IjUxMy01NDktNDU2MSIsImVtYWlsIjoiZG9uZXR0ZS5mb2xsZXJAY294Lm5ldCIsIndlYnNpdGUiOiJodHRwOi8vd3d3LnByaW50aW5nZGltZW5zaW9ucy5jb20ifQ==DecodedData = {"firstname":"Donette","lastname":"Foller","company":"Printing Dimensions","street":"34 Center St","city":"Hamilton","county":"Butler","state":"OH","zip":"45011","homePhone":"513-570-1893","cellPhone":"513-549-4561","email":"donette.foller@cox.net","website":"http://www.printingdimensions.com"}This person = Person [firstname=Donette, lastname=Foller, company=Printing Dimensions, street=34 Center St, city=Hamilton, county=Butler, state=OH, zip=45011, homePhone=513-570-1893, cellPhone=513-549-4561, email=donette.foller@cox.net, website=http://www.printingdimensions.com]Whether Redelivered = falseAppID = rabbitmq.producer.JsonRabbitMQProducerBodySize = 295ClusterId = b-22450561-3f76-4004-813d-392346f054fe.mq.us-west-2.amazonaws.comContentEncoding = UTF-8ContentType = text/plainCorrelationId = TestMessage03-07-02-2023-01-07-20-4DeliveryMode = 2Expiration = 60000MessageId = TestMessage03-07-02-2023-01-07-20:4Priority = 1ReplyTo = nullTimestamp = Jul 2, 2023, 1:30:34 AMType = JsonRabbitMQProducerUserId = adminNow iterating through the headers in this messageHeader Name = MessageNumberInBatch and Header Value = 4Header Name = MessageBatchIdentifier and Header Value = TestMessage03-07-02-2023-01-07-20Now done iterating through the headers in this messageNow done logging a new messageNow logging a new messageEncodedData = eyJmaXJzdG5hbWUiOiJTaW1vbmEiLCJsYXN0bmFtZSI6Ik1vcmFzY2EiLCJjb21wYW55IjoiXCJDaGFwbWFuLCBSb3NzIEUgRXNxXCIiLCJzdHJlZXQiOiIzIE1jYXVsZXkgRHIiLCJjaXR5IjoiQXNobGFuZCIsImNvdW50eSI6IkFzaGxhbmQiLCJzdGF0ZSI6Ik9IIiwiemlwIjoiNDQ4MDUiLCJob21lUGhvbmUiOiI0MTktNTAzLTI0ODQiLCJjZWxsUGhvbmUiOiI0MTktODAwLTY3NTkiLCJlbWFpbCI6InNpbW9uYUBtb3Jhc2NhLmNvbSIsIndlYnNpdGUiOiJodHRwOi8vd3d3LmNoYXBtYW5yb3NzZWVzcS5jb20ifQ==DecodedData = {"firstname":"Simona","lastname":"Morasca","company":"\"Chapman, Ross E Esq\"","street":"3 Mcauley Dr","city":"Ashland","county":"Ashland","state":"OH","zip":"44805","homePhone":"419-503-2484","cellPhone":"419-800-6759","email":"simona@morasca.com","website":"http://www.chapmanrosseesq.com"}This person = Person [firstname=Simona, lastname=Morasca, company="Chapman, Ross E Esq", street=3 Mcauley Dr, city=Ashland, county=Ashland, state=OH, zip=44805, homePhone=419-503-2484, cellPhone=419-800-6759, email=simona@morasca.com, website=http://www.chapmanrosseesq.com]Whether Redelivered = falseAppID = rabbitmq.producer.JsonRabbitMQProducerBodySize = 292ClusterId = b-22450561-3f76-4004-813d-392346f054fe.mq.us-west-2.amazonaws.comContentEncoding = UTF-8ContentType = text/plainCorrelationId = TestMessage03-07-02-2023-01-07-20-5DeliveryMode = 2Expiration = 60000MessageId = TestMessage03-07-02-2023-01-07-20:5Priority = 1ReplyTo = nullTimestamp = Jul 2, 2023, 1:30:34 AMType = JsonRabbitMQProducerUserId = adminNow iterating through the headers in this messageHeader Name = MessageNumberInBatch and Header Value = 5Header Name = MessageBatchIdentifier and Header Value = TestMessage03-07-02-2023-01-07-20Now done iterating through the headers in this messageNow done logging a new messageNow logging a new messageEncodedData = eyJmaXJzdG5hbWUiOiJNaXRzdWUiLCJsYXN0bmFtZSI6IlRvbGxuZXIiLCJjb21wYW55IjoiTW9ybG9uZyBBc3NvY2lhdGVzIiwic3RyZWV0IjoiNyBFYWRzIFN0IiwiY2l0eSI6IkNoaWNhZ28iLCJjb3VudHkiOiJDb29rIiwic3RhdGUiOiJJTCIsInppcCI6IjYwNjMyIiwiaG9tZVBob25lIjoiNzczLTU3My02OTE0IiwiY2VsbFBob25lIjoiNzczLTkyNC04NTY1IiwiZW1haWwiOiJtaXRzdWVfdG9sbG5lckB5YWhvby5jb20iLCJ3ZWJzaXRlIjoiaHR0cDovL3d3dy5tb3Jsb25nYXNzb2NpYXRlcy5jb20ifQ==DecodedData = {"firstname":"Mitsue","lastname":"Tollner","company":"Morlong Associates","street":"7 Eads St","city":"Chicago","county":"Cook","state":"IL","zip":"60632","homePhone":"773-573-6914","cellPhone":"773-924-8565","email":"mitsue_tollner@yahoo.com","website":"http://www.morlongassociates.com"}This person = Person [firstname=Mitsue, lastname=Tollner, company=Morlong Associates, street=7 Eads St, city=Chicago, county=Cook, state=IL, zip=60632, homePhone=773-573-6914, cellPhone=773-924-8565, email=mitsue_tollner@yahoo.com, website=http://www.morlongassociates.com]Whether Redelivered = falseAppID = rabbitmq.producer.JsonRabbitMQProducerBodySize = 289ClusterId = b-22450561-3f76-4004-813d-392346f054fe.mq.us-west-2.amazonaws.comContentEncoding = UTF-8ContentType = text/plainCorrelationId = TestMessage03-07-02-2023-01-07-20-6DeliveryMode = 2Expiration = 60000MessageId = TestMessage03-07-02-2023-01-07-20:6Priority = 1ReplyTo = nullTimestamp = Jul 2, 2023, 1:30:34 AMType = JsonRabbitMQProducerUserId = adminNow iterating through the headers in this messageHeader Name = MessageNumberInBatch and Header Value = 6Header Name = MessageBatchIdentifier and Header Value = TestMessage03-07-02-2023-01-07-20Now done iterating through the headers in this messageNow done logging a new messageNow logging a new messageEncodedData = eyJmaXJzdG5hbWUiOiJMZW90YSIsImxhc3RuYW1lIjoiRGlsbGlhcmQiLCJjb21wYW55IjoiQ29tbWVyY2lhbCBQcmVzcyIsInN0cmVldCI6IjcgVyBKYWNrc29uIEJsdmQiLCJjaXR5IjoiU2FuIEpvc2UiLCJjb3VudHkiOiJTYW50YSBDbGFyYSIsInN0YXRlIjoiQ0EiLCJ6aXAiOiI5NTExMSIsImhvbWVQaG9uZSI6IjQwOC03NTItMzUwMCIsImNlbGxQaG9uZSI6IjQwOC04MTMtMTEwNSIsImVtYWlsIjoibGVvdGFAaG90bWFpbC5jb20iLCJ3ZWJzaXRlIjoiaHR0cDovL3d3dy5jb21tZXJjaWFscHJlc3MuY29tIn0=DecodedData = {"firstname":"Leota","lastname":"Dilliard","company":"Commercial Press","street":"7 W Jackson Blvd","city":"San Jose","county":"Santa Clara","state":"CA","zip":"95111","homePhone":"408-752-3500","cellPhone":"408-813-1105","email":"leota@hotmail.com","website":"http://www.commercialpress.com"}This person = Person [firstname=Leota, lastname=Dilliard, company=Commercial Press, street=7 W Jackson Blvd, city=San Jose, county=Santa Clara, state=CA, zip=95111, homePhone=408-752-3500, cellPhone=408-813-1105, email=leota@hotmail.com, website=http://www.commercialpress.com]Whether Redelivered = falseAppID = rabbitmq.producer.JsonRabbitMQProducerBodySize = 293ClusterId = b-22450561-3f76-4004-813d-392346f054fe.mq.us-west-2.amazonaws.comContentEncoding = UTF-8ContentType = text/plainCorrelationId = TestMessage03-07-02-2023-01-07-20-7DeliveryMode = 2Expiration = 60000MessageId = TestMessage03-07-02-2023-01-07-20:7Priority = 1ReplyTo = nullTimestamp = Jul 2, 2023, 1:30:34 AMType = JsonRabbitMQProducerUserId = adminNow iterating through the headers in this messageHeader Name = MessageNumberInBatch and Header Value = 7Header Name = MessageBatchIdentifier and Header Value = TestMessage03-07-02-2023-01-07-20Now done iterating through the headers in this messageNow done logging a new messageNow logging a new messageEncodedData = eyJmaXJzdG5hbWUiOiJTYWdlIiwibGFzdG5hbWUiOiJXaWVzZXIiLCJjb21wYW55IjoiVHJ1aGxhciBBbmQgVHJ1aGxhciBBdHR5cyIsInN0cmVldCI6IjUgQm9zdG9uIEF2ZSAjODgiLCJjaXR5IjoiU2lvdXggRmFsbHMiLCJjb3VudHkiOiJNaW5uZWhhaGEiLCJzdGF0ZSI6IlNEIiwiemlwIjoiNTcxMDUiLCJob21lUGhvbmUiOiI2MDUtNDE0LTIxNDciLCJjZWxsUGhvbmUiOiI2MDUtNzk0LTQ4OTUiLCJlbWFpbCI6InNhZ2Vfd2llc2VyQGNveC5uZXQiLCJ3ZWJzaXRlIjoiaHR0cDovL3d3dy50cnVobGFyYW5kdHJ1aGxhcmF0dHlzLmNvbSJ9DecodedData = {"firstname":"Sage","lastname":"Wieser","company":"Truhlar And Truhlar Attys","street":"5 Boston Ave #88","city":"Sioux Falls","county":"Minnehaha","state":"SD","zip":"57105","homePhone":"605-414-2147","cellPhone":"605-794-4895","email":"sage_wieser@cox.net","website":"http://www.truhlarandtruhlarattys.com"}This person = Person [firstname=Sage, lastname=Wieser, company=Truhlar And Truhlar Attys, street=5 Boston Ave #88, city=Sioux Falls, county=Minnehaha, state=SD, zip=57105, homePhone=605-414-2147, cellPhone=605-794-4895, email=sage_wieser@cox.net, website=http://www.truhlarandtruhlarattys.com]Whether Redelivered = falseAppID = rabbitmq.producer.JsonRabbitMQProducerBodySize = 309ClusterId = b-22450561-3f76-4004-813d-392346f054fe.mq.us-west-2.amazonaws.comContentEncoding = UTF-8ContentType = text/plainCorrelationId = TestMessage03-07-02-2023-01-07-20-8DeliveryMode = 2Expiration = 60000MessageId = TestMessage03-07-02-2023-01-07-20:8Priority = 1ReplyTo = nullTimestamp = Jul 2, 2023, 1:30:34 AMType = JsonRabbitMQProducerUserId = adminNow iterating through the headers in this messageHeader Name = MessageNumberInBatch and Header Value = 8Header Name = MessageBatchIdentifier and Header Value = TestMessage03-07-02-2023-01-07-20Now done iterating through the headers in this messageNow done logging a new messageNow logging a new messageEncodedData = eyJmaXJzdG5hbWUiOiJLcmlzIiwibGFzdG5hbWUiOiJNYXJyaWVyIiwiY29tcGFueSI6IlwiS2luZywgQ2hyaXN0b3BoZXIgQSBFc3FcIiIsInN0cmVldCI6IjIyOCBSdW5hbXVjayBQbCAjMjgwOCIsImNpdHkiOiJCYWx0aW1vcmUiLCJjb3VudHkiOiJCYWx0aW1vcmUgQ2l0eSIsInN0YXRlIjoiTUQiLCJ6aXAiOiIyMTIyNCIsImhvbWVQaG9uZSI6IjQxMC02NTUtODcyMyIsImNlbGxQaG9uZSI6IjQxMC04MDQtNDY5NCIsImVtYWlsIjoia3Jpc0BnbWFpbC5jb20iLCJ3ZWJzaXRlIjoiaHR0cDovL3d3dy5raW5nY2hyaXN0b3BoZXJhZXNxLmNvbSJ9DecodedData = {"firstname":"Kris","lastname":"Marrier","company":"\"King, Christopher A Esq\"","street":"228 Runamuck Pl #2808","city":"Baltimore","county":"Baltimore City","state":"MD","zip":"21224","homePhone":"410-655-8723","cellPhone":"410-804-4694","email":"kris@gmail.com","website":"http://www.kingchristopheraesq.com"}This person = Person [firstname=Kris, lastname=Marrier, company="King, Christopher A Esq", street=228 Runamuck Pl #2808, city=Baltimore, county=Baltimore City, state=MD, zip=21224, homePhone=410-655-8723, cellPhone=410-804-4694, email=kris@gmail.com, website=http://www.kingchristopheraesq.com]Whether Redelivered = falseAppID = rabbitmq.producer.JsonRabbitMQProducerBodySize = 312ClusterId = b-22450561-3f76-4004-813d-392346f054fe.mq.us-west-2.amazonaws.comContentEncoding = UTF-8ContentType = text/plainCorrelationId = TestMessage03-07-02-2023-01-07-20-9DeliveryMode = 2Expiration = 60000MessageId = TestMessage03-07-02-2023-01-07-20:9Priority = 1ReplyTo = nullTimestamp = Jul 2, 2023, 1:30:34 AMType = JsonRabbitMQProducerUserId = adminNow iterating through the headers in this messageHeader Name = MessageNumberInBatch and Header Value = 9Header Name = MessageBatchIdentifier and Header Value = TestMessage03-07-02-2023-01-07-20Now done iterating through the headers in this messageNow done logging a new messageNow logging a new messageEncodedData = eyJmaXJzdG5hbWUiOiJNaW5uYSIsImxhc3RuYW1lIjoiQW1pZ29uIiwiY29tcGFueSI6IlwiRG9ybCwgSmFtZXMgSiBFc3FcIiIsInN0cmVldCI6IjIzNzEgSmVycm9sZCBBdmUiLCJjaXR5IjoiS3VscHN2aWxsZSIsImNvdW50eSI6Ik1vbnRnb21lcnkiLCJzdGF0ZSI6IlBBIiwiemlwIjoiMTk0NDMiLCJob21lUGhvbmUiOiIyMTUtODc0LTEyMjkiLCJjZWxsUGhvbmUiOiIyMTUtNDIyLTg2OTQiLCJlbWFpbCI6Im1pbm5hX2FtaWdvbkB5YWhvby5jb20iLCJ3ZWJzaXRlIjoiaHR0cDovL3d3dy5kb3JsamFtZXNqZXNxLmNvbSJ9DecodedData = {"firstname":"Minna","lastname":"Amigon","company":"\"Dorl, James J Esq\"","street":"2371 Jerrold Ave","city":"Kulpsville","county":"Montgomery","state":"PA","zip":"19443","homePhone":"215-874-1229","cellPhone":"215-422-8694","email":"minna_amigon@yahoo.com","website":"http://www.dorljamesjesq.com"}This person = Person [firstname=Minna, lastname=Amigon, company="Dorl, James J Esq", street=2371 Jerrold Ave, city=Kulpsville, county=Montgomery, state=PA, zip=19443, homePhone=215-874-1229, cellPhone=215-422-8694, email=minna_amigon@yahoo.com, website=http://www.dorljamesjesq.com]Whether Redelivered = falseAppID = rabbitmq.producer.JsonRabbitMQProducerBodySize = 300ClusterId = b-22450561-3f76-4004-813d-392346f054fe.mq.us-west-2.amazonaws.comContentEncoding = UTF-8ContentType = text/plainCorrelationId = TestMessage03-07-02-2023-01-07-20-10DeliveryMode = 2Expiration = 60000MessageId = TestMessage03-07-02-2023-01-07-20:10Priority = 1ReplyTo = nullTimestamp = Jul 2, 2023, 1:30:34 AMType = JsonRabbitMQProducerUserId = adminNow iterating through the headers in this messageHeader Name = MessageNumberInBatch and Header Value = 10Header Name = MessageBatchIdentifier and Header Value = TestMessage03-07-02-2023-01-07-20Now done iterating through the headers in this messageNow done logging a new messageNow done iterating through each message in this queueDone iterating through Map of all queuesEND RequestId: 92cccff5-2663-4725-af9a-4a301bcbf777
REPORT RequestId: 92cccff5-2663-4725-af9a-4a301bcbf777  Init Duration: 0.05 ms  Duration: 1155.75 ms    Billed Duration: 1156 ms        Memory Size: 512 MB    Max Memory Used: 512 MB
"200"

***** End sam local invoke response *****
```

## Check RabbitMQ Queue Creation

We have included a shell script file called create_rabbit_queue.sh. This shell script creates a VirtualHost, an Exchange and a Queue in the RabbitMQ cluster. It also binds the queue to the exchange. This step is necessary before the Lambda function can be deployed.

The create_rabbit_queue.sh script is run automatically as part of the CloudFormation script.

There is another shell script file called query_rabbit_queue.sh that has been included. You should find it in the /home/ec2-user/serverless-patterns/rabbitmq-private-lambda-java-sam folder. You can run this script as below to ensure the virtualhost, exhange and queue have been created in the RabbitMQ cluster

```bash
cd /home/ec2-user/serverless-patterns/rabbitmq-private-lambda-java-sam
sh ./query_rabbit_queue.sh
```

The response from running this script will be something like this if all the commands from the create_rabbit_queue.sh ran properly

```
original_broker_endpoint: amqps://b-55617af0-19ff-4939-8702-e5a508977c0b.mq.us-west-2.on.aws:5671
broker_endpoint_without_amqps: b-55617af0-19ff-4939-8702-e5a508977c0b.mq.us-west-2.on.aws:5671
broker_endpoint_without_port: b-55617af0-19ff-4939-8702-e5a508977c0b.mq.us-west-2.on.aws
rabbitmq_https_broker_endpoint=https://b-55617af0-19ff-4939-8702-e5a508977c0b.mq.us-west-2.on.aws
########## Begin verifying if Virtual Host has been created ##########
{
  "name": "RabbitMQVirtualHost",
  "description": "",
  "tags": [],
  "default_queue_type": "undefined",
  "metadata": {
    "description": "",
    "tags": []
  },
  "tracing": false,
  "cluster_state": {
    "rabbit@ip-10-0-12-186.us-west-2.compute.internal": "running",
    "rabbit@ip-10-0-28-241.us-west-2.compute.internal": "running",
    "rabbit@ip-10-0-20-83.us-west-2.compute.internal": "running"
  },
  "messages_ready": 0,
  "messages_ready_details": {
    "rate": 0.0
  },
  "messages_unacknowledged": 0,
  "messages_unacknowledged_details": {
    "rate": 0.0
  },
  "messages": 0,
  "messages_details": {
    "rate": 0.0
  }
}
########## End verifying if Virtual Host has been created ##########
########## Begin verifying if Exchange has been created ##########
{
  "arguments": {},
  "auto_delete": false,
  "durable": true,
  "incoming": [],
  "internal": false,
  "name": "RabbitMQExchange",
  "outgoing": [],
  "type": "fanout",
  "user_who_performed_action": "rabbitmqadmin",
  "vhost": "RabbitMQVirtualHost"
}
########## End verifying if Exchange has been created ##########
########## Begin verifying if Queue has been created ##########
{
  "consumer_details": [],
  "arguments": {},
  "auto_delete": false,
  "consumer_capacity": 0,
  "consumer_utilisation": 0,
  "consumers": 0,
  "deliveries": [],
  "durable": true,
  "effective_policy_definition": {
    "ha-mode": "all",
    "ha-sync-mode": "automatic",
    "queue-version": 2
  },
  "exclusive": false,
  "exclusive_consumer_tag": null,
  "garbage_collection": {
    "fullsweep_after": 65535,
    "max_heap_size": 0,
    "min_bin_vheap_size": 46422,
    "min_heap_size": 233,
    "minor_gcs": 6
  },
  "head_message_timestamp": null,
  "idle_since": "2025-10-25T01:46:54.843+00:00",
  "incoming": [],
  "memory": 6768,
  "message_bytes": 0,
  "message_bytes_paged_out": 0,
  "message_bytes_persistent": 0,
  "message_bytes_ram": 0,
  "message_bytes_ready": 0,
  "message_bytes_unacknowledged": 0,
  "messages": 0,
  "messages_details": {
    "rate": 0.0
  },
  "messages_paged_out": 0,
  "messages_persistent": 0,
  "messages_ram": 0,
  "messages_ready": 0,
  "messages_ready_details": {
    "rate": 0.0
  },
  "messages_ready_ram": 0,
  "messages_unacknowledged": 0,
  "messages_unacknowledged_details": {
    "rate": 0.0
  },
  "messages_unacknowledged_ram": 0,
  "name": "RabbitMQJavaLambdaQueue",
  "node": "rabbit@ip-10-0-12-186.us-west-2.compute.internal",
  "operator_policy": "default_operator_policy_AWS_managed",
  "policy": "ha-all-AWS-OWNED-DO-NOT-DELETE",
  "recoverable_slaves": [
    "rabbit@ip-10-0-28-241.us-west-2.compute.internal",
    "rabbit@ip-10-0-20-83.us-west-2.compute.internal"
  ],
  "reductions": 46934,
  "reductions_details": {
    "rate": 0.0
  },
  "single_active_consumer_tag": null,
  "slave_nodes": [
    "rabbit@ip-10-0-28-241.us-west-2.compute.internal",
    "rabbit@ip-10-0-20-83.us-west-2.compute.internal"
  ],
  "state": "running",
  "storage_version": 2,
  "synchronised_slave_nodes": [
    "rabbit@ip-10-0-28-241.us-west-2.compute.internal",
    "rabbit@ip-10-0-20-83.us-west-2.compute.internal"
  ],
  "type": "classic",
  "vhost": "RabbitMQVirtualHost"
}
########## End verifying if Queue has been created ##########
########## Begin verifying if Queue has been bound to exchange ##########
[
  {
    "source": "RabbitMQExchange",
    "vhost": "RabbitMQVirtualHost",
    "destination": "RabbitMQJavaLambdaQueue",
    "destination_type": "queue",
    "routing_key": "RabbitMQExchange-RabbitMQJavaLambdaQueue",
    "arguments": {},
    "properties_key": "RabbitMQExchange-RabbitMQJavaLambdaQueue"
  }
]
########## End verifying if Queue has been bound to exchange ##########

```

If you see any exceptions when running the above script, please run the below command

```
sh ./create_rabbit_queue.sh

```


## Deploy the sample application


To deploy your application for the first time, run the following in your shell:

```bash
sam deploy --capabilities CAPABILITY_IAM --no-confirm-changeset --no-disable-rollback --region $AWS_REGION --stack-name rabbit-lambda-java-sam --guided
```

The sam deploy command will package and deploy your application to AWS, with a series of prompts. You can accept all the defaults by hitting Enter:

* **Stack Name**: The name of the stack to deploy to CloudFormation. This should be unique to your account and region, and a good starting point would be something matching your project name.
* **AWS Region**: The AWS region you want to deploy your app to.
* **Parameter RabbitMQBrokerArn**: The ARN of the RabbitMQBroker that was created by the CloudFormation template
* **Parameter RabbitMQVirtualHost**: The name of the RabbitMQ virtual host from which the lambda function will consume messages
* **Parameter RabbitMQQueue**: The name of the RabbitMQ queue from which the lambda function will consume messages
* **Parameter SecretsManagerSecretForMQ**: The ARN of the secret that has username/password for Rabbit MQ
* **Parameter Subnet1**: The first of the three private subnets where the RabbitMQ cluster is deployed
* **Parameter Subnet2**: The second of the three private subnets where the RabbitMQ cluster is deployed
* **Parameter Subnet3**: The third of the three private subnets where the RabbitMQ cluster is deployed
* **Parameter SecurityGroup**: The security group of the lambda function. This can be the same as the security group of the EC2 machine that was created by the CloudFormation template
* **Confirm changes before deploy**: If set to yes, any change sets will be shown to you before execution for manual review. If set to no, the AWS SAM CLI will automatically deploy application changes.
* **Allow SAM CLI IAM role creation**: Many AWS SAM templates, including this example, create AWS IAM roles required for the AWS Lambda function(s) included to access AWS services. By default, these are scoped down to minimum required permissions. To deploy an AWS CloudFormation stack which creates or modifies IAM roles, the `CAPABILITY_IAM` value for `capabilities` must be provided. If permission isn't provided through this prompt, to deploy this example you must explicitly pass `--capabilities CAPABILITY_IAM` to the `sam deploy` command.
* **Disable rollback**: Defaults to No and it preserves the state of previously provisioned resources when an operation fails
* **Save arguments to configuration file**: If set to yes, your choices will be saved to a configuration file inside the project, so that in the future you can just re-run `sam deploy` without parameters to deploy changes to your application.
* **SAM configuration file [samconfig.toml]**: Name of the configuration file to store configuration information locally
* **SAM configuration environment [default]**: Environment for storing deployment information locally

You should get a message "Successfully created/updated stack - <StackName> in <Region>" if all goes well
    
**Note: In case you want to deploy the Lambda function by pointing to an existing Amazon MQ (RabbitMQ) Cluster and not the one created by running the CloudFormation template provided in this pattern, you will need to modify the values of the above parameters accordingly**


## Test the application

Once the lambda function is deployed, send some messages to the Amazon MQ (RabbitMQ) cluster on the queue that have been configured on the lambda function's event listener.

For your convenience, a Java program and a shell script has been created on the EC2 machine that was provisioned using Cloudformation.

cd /home/ec2-user/serverless-patterns/rabbit-private-lambda-java-sam/rabbit_message_sender_json

You should see a script called commands.sh. Run that script by passing a random string and a number between 1 and 500

```
[ec2-user@ip-10-0-0-126 ~]$ sh ./commands.sh firstBatch 10
Sent out one message - Number 1 at time = 1760937987906
Sent out one message - Number 2 at time = 1760937987909
Sent out one message - Number 3 at time = 1760937987910
Sent out one message - Number 4 at time = 1760937987911
Sent out one message - Number 5 at time = 1760937987913
Sent out one message - Number 6 at time = 1760937987914
Sent out one message - Number 7 at time = 1760937987915
Sent out one message - Number 8 at time = 1760937987916
Sent out one message - Number 9 at time = 1760937987918
Sent out one message - Number 10 at time = 1760937987919
```

Either send at least 10 messages or wait for 300 seconds (check the values of BatchSize: 10 and MaximumBatchingWindowInSeconds: 300 in the template.yaml file)

Then check Cloudwatch logs and you should see messages for the Cloudwatch Log Group with the name of the deployed Lambda function.

When you run the above script, it sends messages with JSON records to the Amazon MQ (RabbitMQ) cluster on the queue on which the lambda function is listening on. The lambda function listens on the published RabbitMQ messages on the queue.

The lambda code parses the RabbitMQ messages and outputs the fields in the messages to Cloudwatch logs

The lambda function also inputs each record into a DynamoDB table called RabbitMQDynamoDBTableJava (if you did not modify the default name in the sam template.yaml file)

You can go to the DynamoDB console and view the records.

You can also use the aws cli command below to view the count of records inserted into DynamoDB

```
aws dynamodb scan --table-name RabbitMQDynamoDBTableJava --select "COUNT"

```



## Cleanup

You can first clean-up the Lambda function by running the sam delete command

```
cd /home/ec2-user/serverless-patterns/rabbit-private-lambda-java-sam/rabbit_consumer_dynamo_sam
sam delete

```
confirm by pressing y for both the questions
You should see the lambda function getting deleted and a final confirmation "Deleted successfully" on the command-line

Next you need to delete the Cloudformation template that created the Amazon MQ (RabbitMQ) cluster and the EC2 machine by going to the Cloudformation console and selecting the stack and then hitting the "Delete" button. It will run for sometime but eventually you should see the stack getting cleaned up. If you get an error message that says the stack could not be deleted, please retry again and do a Force Delete. The reason this may happen is because ENIs created by the deplayed Lambda function in your VPC may prevent the VPC from being deleted even after deleting the lambda function.