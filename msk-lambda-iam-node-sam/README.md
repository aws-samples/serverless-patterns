# Node.js Lambda Kafka Consumer with IAM Auth, using SAM

This pattern is an example of a Lambda function that consumes messages from an Amazon Managed Streaming for Kafka (Amazon MSK) topic, where the MSK Cluster has been configured to use IAM authentication. This pattern assumes you already have an MSK cluster with a topic configured, if you need a sample pattern to deploy an MSK cluster either in Provisioned or Serverless modes please see the [msk-cfn-sasl-lambda pattern](https://serverlessland.com/patterns/msk-cfn-sasl-lambda). 

This project contains source code and supporting files for a serverless application that you can deploy with the AWS Serverless Application Model (AWS SAM) CLI. It includes the following files and folders.

- HandlerKafka - Code for the application's Lambda function.
- events - Invocation events that you can use to invoke the function.
- template.yaml - An AWS SAM template that defines the application's AWS resources.

The application creates a Lambda function that listens to Kafka messages on a topic of an MSK Cluster. These resources are defined in the `template.yaml` file in this project. You can update the template to add AWS resources through the same deployment process that updates your application code.

Important: this application uses various AWS services and there are costs associated with these services after the Free Tier usage - please see the [AWS Pricing page](https://aws.amazon.com/pricing/) for details. You are responsible for any AWS costs incurred. No warranty is implied in this example.

## Requirements

* [Create an AWS account](https://portal.aws.amazon.com/gp/aws/developer/registration/index.html) if you do not already have one and log in. The IAM user that you use must have sufficient permissions to make necessary AWS service calls and manage AWS resources.
* [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html) installed and configured
* [Git installed](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)
* [AWS Serverless Application Model](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-sam-cli-install.html) (AWS SAM) installed
* Create MSK cluster and topic that will be used for testing. It is important to create the topic before deploying the Lambda function, otherwise the event source mapping will stay disabled. 

## Deploy the sample application

The AWS SAM CLI is a serverless tool for building and testing Lambda applications. It uses Docker to locally test your functions in an Amazon Linux environment that resembles the Lambda execution environment. It can also emulate your application's build environment and API.

To use the AWS SAM CLI, you need the following tools.

* AWS SAM CLI - [Install the AWS SAM CLI](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-sam-cli-install.html)
* Docker - [Install Docker community edition](https://hub.docker.com/search/?type=edition&offering=community)

1. Create a new directory, navigate to that directory in a terminal and clone the GitHub repository:
    ``` 
    git clone https://github.com/aws-samples/serverless-patterns.git
    ```
1. Change directory to the pattern directory:
    ```
    cd msk-lambda-iam-node-sam
    ```

1. From the command line, use AWS SAM to deploy the AWS resources for the pattern as specified in the template.yml file:
    ```
    sam build
    sam deploy --guided
    ```

1. During the prompts:
* **Stack Name**: The name of the stack to deploy to CloudFormation. This should be unique to your account and region, and a good starting point would be something matching your project name.
* **AWS Region**: The AWS region you want to deploy your app to.
* **Parameter MSKClusterName**: The name of the MSKCluster, eg. msk-test-cluster

* **Parameter MSKClusterId**: The unique ID of the MSKCluster, eg. a4e132c8-6ad0-4334-a313-123456789012-s2
* **Parameter MSKTopic**: The Kafka topic on which the lambda function will listen on
* **Confirm changes before deploy**: If set to yes, any change sets will be shown to you before execution for manual review. If set to no, the AWS SAM CLI will automatically deploy application changes.
* **Allow SAM CLI IAM role creation**: Many AWS SAM templates, including this example, create AWS IAM roles required for the AWS Lambda function(s) included to access AWS services. By default, these are scoped down to minimum required permissions. To deploy an AWS CloudFormation stack which creates or modifies IAM roles, the `CAPABILITY_IAM` value for `capabilities` must be provided. If permission isn't provided through this prompt, to deploy this example you must explicitly pass `--capabilities CAPABILITY_IAM` to the `sam deploy` command.
* **Disable rollback**: Defaults to No and it preserves the state of previously provisioned resources when an operation fails
* **Save arguments to configuration file**: If set to yes, your choices will be saved to a configuration file inside the project, so that in the future you can just re-run `sam deploy` without parameters to deploy changes to your application.
* **SAM configuration file [samconfig.toml]**: Name of the configuration file to store configuration information locally
* **SAM configuration environment [default]**: Environment for storing deployment information locally

You should get a message "Successfully created/updated stack - <StackName> in <Region>" if all goes well.

Once you have run `sam deploy --guided` mode once and saved arguments to a configuration file (samconfig.toml), you can use `sam deploy` in future to use these defaults.

## How it works

This pattern creates a Lambda function along with a Lambda Event Source Mapping(ESM) resource. This maps a Kafka topic on an MSK Cluster as a trigger to a Lambda function. The ESM takes care of polling the Kafka topic and then invokes the Lambda function with a batch of messages.

## Test the sample application

Once the Lambda function is deployed, send some Kafka messages to the topic that you configured in the Lambda function trigger.

Either send at least 10 messages or wait for 300 seconds (check the values of BatchSize: 10 and MaximumBatchingWindowInSeconds: 300 in the template.yaml file)

Then check Amazon CloudWatch logs and you should see messages in the CloudWatch Log Group with the name of the deployed Lambda function.

The Lambda code parses the Kafka messages and outputs the fields in the Kafka messages to CloudWatch logs.

A single Lambda function receives a batch of messages. The messages are received as a map with each key being a combination of the topic and the partition, as a single batch can receive messages from multiple partitions.

Each key has a list of messages. Each Kafka message has the following properties - `Topic`, `Partition`, `Offset`, `TimeStamp`, `TimeStampType`, `Key`, and `Value`.

The `Key` and `Value` are base64 encoded and have to be decoded. A message can also have a list of headers, each header having a key and a value.

The code in this example prints out the fields in the Kafka message and also decrypts the key and the value and logs them to CloudWatch logs.


### Local development

**You can invoke the function locally using `sam local`**

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
    sam delete
    ```

----
Copyright 2023 Amazon.com, Inc. or its affiliates. All Rights Reserved.

SPDX-License-Identifier: MIT-0
