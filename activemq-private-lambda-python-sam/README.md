# Python AWS Lambda ActiveMQ (in private subnets) consumer, using AWS SAM

This pattern is an example of a Lambda function written in Python that consumes messages from Amazon MQ (Apache ActiveMQ), located in an private subnet. The function parses the ActiveMQ messages and stores the results in an Amazon DynamoDB table. The pattern provides an AWS CloudFormation template to install and set-up an Amazon MQ (Apache ActiveMQ) cluster inside private subnets in an Amazon VPC. The CloudFormation template also launches an Amazon EC2 instance with tools necessary to configure the Amazon MQ (Apache ActiveMQ) cluster and generate Amazon MQ (Apache ActiveMQ) messages.

This project contains source code and supporting files for a serverless application that you can deploy with the SAM CLI. It includes the following files and folders.

- activemq_consumer_dynamo_sam/activemq_event_consumer_function/app.py - Code for the application's Lambda function that will listen for Amazon MQ (Apache ActiveMQ) messages and write them to an Amazon DynamoDB table
- activemq_message_sender_json/activemq_producer.py - Code for publishing messages with JSON payload into an Amazon MQ (ActiveMQ cluster)
- activemq_consumer_dynamo_sam/template_original.yaml - A template that defines the application's Lambda function to be used by SAM to deploy the lambda function
- ActiveMQAndClientEC2.yaml - An AWS CloudFormation template file that can be used to deploy an Amazon MQ (Apache ActiveMQ) cluster and also deploy an EC2 instance with all pre-requisities already installed, so you can directly build and deploy the lambda function and test it out.
- activemq_queue_browser.sh - A shell script that can be used to connect to the Amazon MQ (Apache ActiveMQ) brokers using the activemq command-line tool

Important: this application uses various AWS services and there are costs associated with these services after the Free Tier usage - please see the [AWS Pricing page](https://aws.amazon.com/pricing/) for details. You are responsible for any AWS costs incurred. No warranty is implied in this example.

## Requirements

* [Create an AWS account](https://portal.aws.amazon.com/gp/aws/developer/registration/index.html) if you do not already have one and log in. The IAM user that you use must have sufficient permissions to make necessary AWS service calls and manage AWS resources.

## Run the AWS CloudFormation template to create the Amazon MQ (Apache ActiveMQ) Cluster and Client EC2 instance

* [Run the AWS CloudFormation template using the file ActiveMQAndClientEC2.yaml] - You can go to the AWS CloudFormation console, create a new stack by specifying the template file. You can keep the defaults for input parameters or modify them as necessary. Wait for the AWS CloudFormation stack to be created. This AWS CloudFormation template will create an Amazon MQ (Apache ActiveMQ) cluster. It will also create an EC2 instance that you can use as a client.

* [Connect to the EC2 instance] - Once the AWS CloudFormation stack is created, you can go to the EC2 console and log into the instance using either "Connect using EC2 Instance Connect" or "Connect using EC2 Instance Connect Endpoint" option under the "EC2 Instance Connect" tab. In case you are using SSM Instance connect, you are not initially placed in the home directory. If you connect as ssm-user, you need to sudo su to ec2-user for this to work.
Note: You may need to wait for some time after the CloudFormation stack is created, as some UserData scripts continue running post creation.

## Pre-requisites to Deploy the sample Lambda function

The EC2 instance created by the AWS CloudFormation template has all the software required to deploy the Lambda function.

The AWS SAM CLI is a serverless tool for building and testing Lambda applications.

* Python 3 - On the EC2 instance, Python 3 is pre-installed
* pip3 - On the EC2 instance, pip3 is pre-installed
* AWS SAM CLI - We installed the AWS SAM CLI (https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-sam-cli-install.html)

We cloned the serverless-patterns Github repository on the EC2 instance already by running the below command
    ``` 
    git clone https://github.com/aws-samples/serverless-patterns.git
    ```
Change directory to the pattern directory:
    ```
    cd serverless-patterns/activemq-private-lambda-python-sam
    ```

## Use the SAM CLI to build and deploy the lambda function

Build your application with the `sam build` command.

```bash
cd activemq_consumer_dynamo_sam
sam build
```

The SAM CLI installs dependencies defined in `activemq_event_consumer_function/requirements.txt`, creates a deployment package, and saves it in the `.aws-sam/build` folder.


## Test the build locally

Test a single function by invoking it directly with a test event. An event is a JSON document that represents the input that the function receives from the event source. Test events are included in the `events` folder in this project.

Run functions locally and invoke them with the `sam local invoke` command.

```bash
sam local invoke --event events/event.json
```

## Deploy the sample application

To deploy your application for the first time, run the following in your shell. Make sure the shell variable $AWS_REGION is set. If not, replace $AWS_REGION with the region in which you are deploying the AWS Lambda function:

```bash
sam deploy --capabilities CAPABILITY_IAM --no-confirm-changeset --no-disable-rollback --region $AWS_REGION --stack-name activemq-lambda-python-sam --guided
```

The sam deploy command will package and deploy your application to AWS, with a series of prompts. You can accept all the defaults by hitting Enter:

* **Stack Name**: The name of the stack to deploy to CloudFormation. This should be unique to your account and region, and a good starting point would be something matching your project name.
* **AWS Region**: The AWS region you want to deploy your app to.
* **Parameter ActiveMQBrokerArn**: The ARN of the Amazon MQ (Apache ActiveMQ) broker that was created by the AWS CloudFormation template
* **Parameter ActiveMQQueue**: The name of the Amazon MQ (Apache ActiveMQ) queue from which the lambda function will consume messages
* **Parameter SecretsManagerSecretForMQ**: The ARN of the secret that has username/password for Amazon MQ (Apache ActiveMQ)
* **Parameter Subnet1**: The first of the three private subnets where the Amazon MQ (Apache ActiveMQ) cluster is deployed
* **Parameter Subnet2**: The second of the three private subnets where the Amazon MQ (Apache ActiveMQ) cluster is deployed
* **Parameter Subnet3**: The third of the three private subnets where the Amazon MQ (Apache ActiveMQ) cluster is deployed
* **Parameter SecurityGroup**: The security group of the lambda function. This can be the same as the security group of the EC2 instance that was created by the AWS CloudFormation template
* **Confirm changes before deploy**: If set to yes, any change sets will be shown to you before execution for manual review. If set to no, the AWS SAM CLI will automatically deploy application changes.
* **Allow SAM CLI IAM role creation**: Many AWS SAM templates, including this example, create AWS IAM roles required for the AWS Lambda function(s) included to access AWS services. By default, these are scoped down to minimum required permissions. To deploy an AWS CloudFormation stack which creates or modifies IAM roles, the `CAPABILITY_IAM` value for `capabilities` must be provided. If permission isn't provided through this prompt, to deploy this example you must explicitly pass `--capabilities CAPABILITY_IAM` to the `sam deploy` command.
* **Disable rollback**: Defaults to No and it preserves the state of previously provisioned resources when an operation fails
* **Save arguments to configuration file**: If set to yes, your choices will be saved to a configuration file inside the project, so that in the future you can just re-run `sam deploy` without parameters to deploy changes to your application.
* **SAM configuration file [samconfig.toml]**: Name of the configuration file to store configuration information locally
* **SAM configuration environment [default]**: Environment for storing deployment information locally

You should get a message "Successfully created/updated stack - <StackName> in <Region>" if all goes well
    
**Note: In case you want to deploy the Lambda function by pointing to an existing Amazon MQ (Apache ActiveMQ) Cluster and not the one created by running the AWS CloudFormation template provided in this pattern, you will need to modify the values of the above parameters accordingly**


## Test the application

Once the lambda function is deployed, send some messages to the Amazon MQ (Apache ActiveMQ) cluster on the queue that have been configured on the lambda function's event listener.

For your convenience, a Python script and a shell script has been created on the EC2 instance that was provisioned using AWS CloudFormation.

You should see a script called commands.sh. Run that script by passing a random string and a number between 1 and 500. Either send at least 10 messages or wait for 300 seconds (check the values of BatchSize: 100 and MaximumBatchingWindowInSeconds: 5 in the template.yaml file)

```
cd /home/ec2-user/serverless-patterns/activemq-private-lambda-python-sam/activemq_message_sender_json
chmod +x commands.sh
$PYTHON3_VERSION -m venv ./myenv && source ./myenv/bin/activate && pip install -r requirements.txt
sh ./commands.sh firstBatch 100

```


You should see output similar to what is shown below:

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


Once the messages have been sent, check Amazon CloudWatch logs and you should see messages for the Amazon CloudWatch Log Group with the name of the deployed Lambda function.

When you run the above script, it sends messages with JSON records to the Amazon MQ (Apache ActiveMQ) cluster on the queue on which the lambda function is listening on. The Lambda function listens on the published Amazon MQ (Apache ActiveMQ) messages on the queue.

The Lambda function code parses the Amazon MQ (Apache ActiveMQ) messages and outputs the fields in the messages to Amazon CloudWatch logs

The Lambda function also inputs each record into an Amazon DynamoDB table called ActiveMQDynamoDBTablePython (if you did not modify the default name in the sam template.yaml file)

You can go to the Amazon DynamoDB console and view the records.

You can also use the aws cli command below to view the count of records inserted into Amazon DynamoDB

```
aws dynamodb scan --table-name ActiveMQDynamoDBTablePython --select "COUNT"

```



## Cleanup

You can first clean-up the Lambda function by running the `sam delete` command

```
cd /home/ec2-user/serverless-patterns/activemq-private-lambda-python-sam/activemq_consumer_dynamo_sam
sam delete

```
Confirm the delete by selecting Y at both prompts.
AWS SAM confirms the stack deletion with the "Deleted successfully" message in the terminal.

Next you need to delete the AWS CloudFormation template that created the Amazon MQ (Apache ActiveMQ) cluster and the EC2 instance. Open the Amazon CloudFormation console, select the stack, then choose Delete. The delete will take some time.

----
Copyright 2026 Amazon.com, Inc. or its affiliates. All Rights Reserved.

SPDX-License-Identifier: MIT-0
