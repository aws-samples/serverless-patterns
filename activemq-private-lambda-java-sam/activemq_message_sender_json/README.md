# activemq-message-sender-json

This project contains source code and supporting files for a Java application that you can use to generate messages to an ActiveMQ broker queue, that can in turn be consumed by a Lambda function

- activemq_message_sender_json/src/main/java - Code for the application.
- activemq_message_sender_json/Commands - A file that contains the command to run this application so messages can be generated on an ActiveMQ queue, to invoke the corresponding Lambda function

## Set-up and run this application

The steps required before this application can be run are

1) Install and configure an ActiveMQ cluster (use AWS console or a Cloudformation template) - for detailed instructions look at the AWS documentation - https://docs.aws.amazon.com/amazon-mq/latest/developer-guide/amazon-mq-creating-configuring-broker.html. For information on how to use Cloudformation to create an ActiveMQ cluster, take a look at https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-amazonmq-broker.html

2) Create a secret in AWS Secrets Manager called AmazonMQCredentials - Choose a secret of type "Other Type of Secret" when creating the secret. Provide the username and password to connect to the ActiveMQ broker,  as had been specified at the time of cluster creation. Name this secret AmazonMQCredentials

3) After cloning the code for this project from Github, go to the folder where the project was cloned and run the command 'mvn clean install' (without the quotes). Make sure maven is installed on the computer from where you are running this command, prior to running the command

4) If you are running the command to send ActiveMQ messages from a Cloud9 or EC2 instance, make sure that the security group of the ActiveMQ cluster allows inbound traffic from the security group of the Cloud9 or EC2 instance on port 61617. Also make sure that the role associated with the Cloud9 or EC2 instance has policies attached to it that allow the permissions that are needed. For example, you can use the AmazonMQFullAccess policy on the role.

5) Use the command specified in the activemq_message_sender_json/Commands file to generate ActiveMQ queue messages that can be consumed by the Lambda function. The command specified in the Commands file takes four parameters

	a) The ActiveMQ broker URL of the ActiveMQ cluster created in Step 1
	b) The name of the ActiveMQ queue on which messages will be published. This must match the name of the ActiveMQ queue that is configured in the event source of the lambda function
	c) A Unique String that can be used to identify the batch of ActiveMQ queue messages that will be generated
	d) The number of ActiveMQ queue messages to generate as part of this batch
	
6) If a Lambda function consumer of the ActiveMQ queue messages has already been deployed, then you should be able to see the content of the messages in the Lambda function logs in Cloudwatch