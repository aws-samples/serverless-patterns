# javaActiveMQLambdaDynamoDB
Java samples for ActiveMQ --> Lambda --> DynamoDB

This repository has code samples for implementing a Lambda function in Java that listens on an Amazon ActiveMQ queue as its event source and upon receipt of messages from the Amazon ActiveMQ queue, the code in the lambda function parses the contents of the message (both metadata as well as payload data) and outputs the contents into an Amazon DynamoDB table

Each example has two Java Maven projects - a Sender Project and a Lambda Receiver Project

The sender project has instructions on how to generate messages on the Amazon ActiveMQ queue such that those messages can then be received by the corresponding lambda receiver

Currently, the following samples exist in this repository

1) JSONMessage - In this example, the sender program generates Amazon ActiveMQ messages with a JSON payload

More examples will be added in the future

In order to run these examples, create the following in an AWS account

1) A VPC with 3 public and 3 private subnets and an internet gateway and 3 NAT gateways for each of the three private subnets - For an example of a Cloudformation template to create a VPC, refer to this document - https://docs.aws.amazon.com/codebuild/latest/userguide/cloudformation-vpc-template.html

2) Create an AWS Cloud9 environment and use one of the public subnets created in the VPC above for creating the Cloud9 environment - For an example of a Cloudformation template to create a Cloud9 environment, refer to the document - https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloud9-environmentec2.html

3) Create a Security Group and assign it to the EC2 instance of the Cloud9 environment

4) Create an IAM role and attach it to the EC2 instance of the Cloud9 environment

5) Under each sample, refer to the README files inside the sender and the receiver folders - For example under the JSONMessage folder, refer to the README files inside the sub-folders activemq_message_sender_json (sender) and activemq_consumer_dynamo_sam (receiver) for instructions