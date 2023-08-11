# Node.js Lambda Kafka Consumer with IAM Auth, using SAM

This pattern is an example of a Lambda function that will consume messages from an Managed Streaming for Kafka(MSK) topic, where the MSK Cluster has been configured to use IAM Authentication. This pattern assumes you already have an MSK Cluster with a Topic configured, if you need a sample pattern to deploy an MSK Cluster either in Provisioned or Serverless modes please see the [msk-cfn-sasl-lambda pattern](https://serverlessland.com/patterns/msk-cfn-sasl-lambda)

This project contains source code and supporting files for a serverless application that you can deploy with the SAM CLI. It includes the following files and folders.

- HandlerKafka - Code for the application's Lambda function.
- events - Invocation events that you can use to invoke the function.
- template.yaml - A template that defines the application's AWS resources.

The application creates a Lambda function that will listen to Kafka messages on a topic linked to an MSK Cluster. These resources are defined in the `template.yaml` file in this project. You can update the template to add AWS resources through the same deployment process that updates your application code.

Important: this application uses various AWS services and there are costs associated with these services after the Free Tier usage - please see the [AWS Pricing page](https://aws.amazon.com/pricing/) for details. You are responsible for any AWS costs incurred. No warranty is implied in this example.

## Requirements

* [Create an AWS account](https://portal.aws.amazon.com/gp/aws/developer/registration/index.html) if you do not already have one and log in. The IAM user that you use must have sufficient permissions to make necessary AWS service calls and manage AWS resources.
* [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html) installed and configured
* [Git Installed](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)
* [AWS Serverless Application Model](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-sam-cli-install.html) (AWS SAM) installed
* Create MSK cluster and topic that will be used for testing. It is important to create the topic before deploying the Lambda function, otherwise the event source mapping will stay disabled. 

## Deploy the sample application

The Serverless Application Model Command Line Interface (SAM CLI) is an extension of the AWS CLI that adds functionality for building and testing Lambda applications. It uses Docker to run your functions in an Amazon Linux environment that matches Lambda. It can also emulate your application's build environment and API.

To use the SAM CLI, you need the following tools.

* SAM CLI - [Install the SAM CLI](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-sam-cli-install.html)
* Node.js - [Install Node.js 18](https://nodejs.org/en/), including the NPM package management tool.
* Docker - [Install Docker community edition](https://hub.docker.com/search/?type=edition&offering=community)

To build and deploy your application for the first time, run the following in your shell:

```bash
sam build
sam deploy --guided
```

The first command will build the source of your application. The second command will package and deploy your application to AWS, with a series of prompts:

* **Stack Name**: The name of the stack to deploy to CloudFormation. This should be unique to your account and region, and a good starting point would be something matching your project name.
* **AWS Region**: The AWS region you want to deploy your app to.
* **Parameter MSKClusterName**: The name of the MSKCluster
* **Parameter MSKClusterId**: The unique ID of the MSKCluster
* **Parameter MSKTopic**: The Kafka topic on which the lambda function will listen on
* **Confirm changes before deploy**: If set to yes, any change sets will be shown to you before execution for manual review. If set to no, the AWS SAM CLI will automatically deploy application changes.
* **Allow SAM CLI IAM role creation**: Many AWS SAM templates, including this example, create AWS IAM roles required for the AWS Lambda function(s) included to access AWS services. By default, these are scoped down to minimum required permissions. To deploy an AWS CloudFormation stack which creates or modifies IAM roles, the `CAPABILITY_IAM` value for `capabilities` must be provided. If permission isn't provided through this prompt, to deploy this example you must explicitly pass `--capabilities CAPABILITY_IAM` to the `sam deploy` command.
* **Disable rollback**: Defaults to No and it preserves the state of previously provisioned resources when an operation fails
* **Save arguments to configuration file**: If set to yes, your choices will be saved to a configuration file inside the project, so that in the future you can just re-run `sam deploy` without parameters to deploy changes to your application.
* **SAM configuration file [samconfig.toml]**: Name of the configuration file to store configuration information locally
* **SAM configuration environment [default]**: Environment for storing deployment information locally

You should get a message "Successfully created/updated stack - <StackName> in <Region>" if all goes well

## Test the sample application

Once the lambda function is deployed, send some Kafka messages on the topic that the lambda function is listening on, on the MSK server.

Either send at least 10 messages or wait for 300 seconds (check the values of BatchSize: 10 and MaximumBatchingWindowInSeconds: 300 in the template.yaml file)

Then check Cloudwatch logs and you should see messages for the Cloudwatch Log Group with the name of the deployed Lambda function.

The lambda code parses the Kafka messages and outputs the fields in the Kafka messages to Cloudwatch logs

A single lambda function receives a batch of messages. The messages are received as a map with each key being a combination of the topic and the partition, as a single batch can receive messages from multiple partitions.

Each key has a list of messages. Each Kafka message has the following properties - Topic, Partition, Offset, TimeStamp, TimeStampType, Key and Value

The Key and Value are base64 encoded and have to be decoded. A message can also have a list of headers, each header having a key and a value.

The code in this example prints out the fields in the Kafka message and also decrypts the key and the value and logs them in Cloudwatch logs.

### Local development

**Invoking function locally using sam local**

```bash
sam local invoke --event=events/event.json
```

You should see a response similar to the below

START RequestId: 2d1041e7-fb49-4181-a8ac-15277f5d2b6c Version: $LATEST
2023-03-31T22:29:21.659Z	2d1041e7-fb49-4181-a8ac-15277f5d2b6c	INFO	Key:  myTopic-0
2023-03-31T22:29:21.699Z	2d1041e7-fb49-4181-a8ac-15277f5d2b6c	INFO	R} headers: []=', 'CREATE_TIME',
2023-03-31T22:29:21.701Z	2d1041e7-fb49-4181-a8ac-15277f5d2b6c	INFO	Topic:  myTopic
2023-03-31T22:29:21.701Z	2d1041e7-fb49-4181-a8ac-15277f5d2b6c	INFO	Partition:  0
2023-03-31T22:29:21.701Z	2d1041e7-fb49-4181-a8ac-15277f5d2b6c	INFO	Offset:  250
2023-03-31T22:29:21.701Z	2d1041e7-fb49-4181-a8ac-15277f5d2b6c	INFO	Timestamp:  1678072110111
2023-03-31T22:29:21.702Z	2d1041e7-fb49-4181-a8ac-15277f5d2b6c	INFO	TimestampType:  CREATE_TIME
2023-03-31T22:29:21.702Z	2d1041e7-fb49-4181-a8ac-15277f5d2b6c	INFO	Key: null
2023-03-31T22:29:21.705Z	2d1041e7-fb49-4181-a8ac-15277f5d2b6c	INFO	Value: f
2023-03-31T22:29:21.710Z	2d1041e7-fb49-4181-a8ac-15277f5d2b6c	INFO	R} headers: []=', 'CREATE_TIME',
2023-03-31T22:29:21.712Z	2d1041e7-fb49-4181-a8ac-15277f5d2b6c	INFO	Topic:  myTopic
2023-03-31T22:29:21.713Z	2d1041e7-fb49-4181-a8ac-15277f5d2b6c	INFO	Partition:  0
2023-03-31T22:29:21.719Z	2d1041e7-fb49-4181-a8ac-15277f5d2b6c	INFO	Offset:  251
2023-03-31T22:29:21.725Z	2d1041e7-fb49-4181-a8ac-15277f5d2b6c	INFO	Timestamp:  1678072111086
2023-03-31T22:29:21.725Z	2d1041e7-fb49-4181-a8ac-15277f5d2b6c	INFO	TimestampType:  CREATE_TIME
2023-03-31T22:29:21.725Z	2d1041e7-fb49-4181-a8ac-15277f5d2b6c	INFO	Key: null
2023-03-31T22:29:21.726Z	2d1041e7-fb49-4181-a8ac-15277f5d2b6c	INFO	Value: g
END RequestId: 2d1041e7-fb49-4181-a8ac-15277f5d2b6c
REPORT RequestId: 2d1041e7-fb49-4181-a8ac-15277f5d2b6c	Init Duration: 11.37 msDuration: 2696.60 ms	Billed Duration: 2697 ms	Memory Size: 128 MB	Max Memory Used: 128 MB

## Cleanup
 
1. Delete the stack
    ```bash
    aws cloudformation delete-stack --stack-name STACK_NAME
    ```
1. Confirm the stack has been deleted
    ```bash
    aws cloudformation list-stacks --query "StackSummaries[?contains(StackName,'STACK_NAME')].StackStatus"
    ```

----
Copyright 2023 Amazon.com, Inc. or its affiliates. All Rights Reserved.

SPDX-License-Identifier: MIT-0
