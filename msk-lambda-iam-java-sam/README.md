# Java AWS Lambda Kafka consumer with IAM auth, using AWS SAM

This pattern is an example of a Lambda function that consumes messages from an Amazon Managed Streaming for Kafka (Amazon MSK) topic, where the MSK Cluster has been configured to use IAM authentication. This pattern assumes you already have an MSK cluster with a topic configured, if you need a sample pattern to deploy an MSK cluster either in Provisioned or Serverless modes please see [here](https://github.com/aws-samples/serverless-patterns/tree/main/msk-cfn-sasl-lambda/create-cluster-cfn).

This project contains source code and supporting files for a serverless application that you can deploy with the AWS Serverless Application Model (AWS SAM) CLI. It includes the following files and folders.

The application creates a Lambda function that listens to Kafka messages on a topic of an MSK Cluster. These resources are defined in the `template.yaml` file in this project. You can update the template to add AWS resources through the same deployment process that updates your application code.

Important: this application uses various AWS services and there are costs associated with these services after the Free Tier usage - please see the [AWS Pricing page](https://aws.amazon.com/pricing/) for details. You are responsible for any AWS costs incurred. No warranty is implied in this example.

## Requirements

1. [Create an AWS account](https://portal.aws.amazon.com/gp/aws/developer/registration/index.html) if you do not already have one and log in. The IAM user that you use must have sufficient permissions to make necessary AWS service calls and manage AWS resources.
2. [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html) installed and configured
3. [Git Installed](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)
4. [AWS Serverless Application Model](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-sam-cli-install.html) (AWS SAM) installed
5. Complete the **Basic Set up** and **IAM** steps [here](https://github.com/aws-samples/serverless-patterns/tree/main/msk-cfn-sasl-lambda/create-cluster-cfn) to create the following resources:
   1. An MSK Cluster 
   2. A Kafka topic named `MSKTutorialTopicIAM`
   3. A Cloud9 environment with Kafka CLI installed
6. [Java 21 or above](https://docs.aws.amazon.com/corretto/latest/corretto-21-ug/downloads-list.html) installed
7. [Maven 3.9.6 or above](https://maven.apache.org/download.cgi) installed

## Deployment Instructions

1. Create a new directory, navigate to that directory in a terminal and clone the GitHub repository:
   ```bash
   git clone https://github.com/aws-samples/serverless-patterns
   ```

2. Change directory to the pattern directory:
   ```bash
   cd serverless-patterns/msk-lambda-iam-java-sam
   ```

3. From the command line, execute the below command to build the Java based AWS Lambda function.
   ```bash
   sam build
   ```

4. From the command line, use AWS SAM to deploy the AWS resources for the pattern as specified in the template.yml file:
   ```bash
   sam deploy --guided
   ```
5. During the prompts:

   * **Stack Name**: Enter the stack name as `msk-lambda-iam-java` 
   * **AWS Region**: The AWS region you want to deploy your app to.
   * **Parameter MSKClusterName**: The name of the MSKCluster created by following the **Requirements** section
   * **Parameter MSKClusterId**: The unique ID of the MSKCluster, eg. a4e132c8-6ad0-4334-a313-123456789012-s2. The id can be found in the ARN of the MSK cluster.
   * **Parameter MSKTopic**: Enter `MSKTutorialTopicIAM` or the name of Kafka topic on which the lambda function will listen on
     * **Confirm changes before deploy**: If set to yes, any change sets will be shown to you before execution for manual review. If set to no, the AWS SAM CLI will automatically deploy application changes.
     Accept the defaults for rest of the prompts
  
     Once you have run `sam deploy --guided` mode once and saved arguments to a configuration file (samconfig.toml), you can use `sam deploy` in future to use these defaults.

6. Note the outputs from the SAM deployment process. These contain the resource names and/or ARNs which are used for next step as well as testing.

## How it works

Please refer to the architecture diagram below:

![End to End Architecture](images/architecture.png)

This pattern creates a Lambda function along with a Lambda Event Source Mapping(ESM) resource. This maps a Kafka topic on an MSK Cluster as a trigger to a Lambda function. The ESM takes care of polling the Kafka topic and then invokes the Lambda function with a batch of messages.

## Testing

Once the Lambda function is deployed, send some Kafka messages to the topic that you configured in the Lambda function trigger. You can do this by launching the [Cloud9 instance](https://console.aws.amazon.com/cloud9control/home) created as part of Step 5 of **Requirements** section.

Navigate to the Kafka directory:

   ```shell
   ~/environment/kafka_2.13-3.7.0/
   ```
Create a `client.properties` file:

```shell
echo "security.protocol=SASL_SSL
sasl.mechanism=AWS_MSK_IAM
sasl.jaas.config=software.amazon.msk.auth.iam.IAMLoginModule required;
sasl.client.callback.handler.class=software.amazon.msk.auth.iam.IAMClientCallbackHandler" > client.properties
```

Send at least 10 messages (or wait for 300 seconds), you can find `broker-list` by navigating to your cluster listed in the [MSK Clusters](https://console.aws.amazon.com/msk/home?#/clusters) page and clicking on the "View client information" button:

```shell
./bin/kafka-console-producer.sh --broker-list [broker-list]  --topic MSKTutorialTopicIAM --producer.config bin/client.properties 
>{"message":"interesset eros vel elit salutatus"}
>{"message":"impetus deterruisset per aliquam luctus"}
>{"message":"ridens vocibus feugait vitae cras"}
...

```
Click ctrl+c to exit

Check if the Lambda function was invoked in [Amazon CloudWatch logs](https://console.aws.amazon.com/cloudwatch/home?#logsV2:log-groups). You should see messages in the Log Group with the name of the deployed Lambda function.

The Lambda code parses the Kafka messages and outputs the fields in the Kafka messages to CloudWatch logs.

A single Lambda function receives a batch of messages. The messages are received as a map with each key being a combination of the topic and the partition, as a single batch can receive messages from multiple partitions.

Each key has a list of messages. Each Kafka message has the following properties - `Topic`, `Partition`, `Offset`, `TimeStamp`, `TimeStampType`, `Key`, and `Value`.

The `Key` and `Value` are base64 encoded and have to be decoded. A message can also have a list of headers, each header having a key and a value.

The code in this example prints out the fields in the Kafka message and also decodes the key and the value and logs them to CloudWatch logs. The log entries should look like this:

```shell
[INFO] Topic: MSKTutorialTopicIAM
[INFO] Partition: 0
[INFO] Offset: 95
[INFO] Timestamp: 1719328016122
[INFO] TimestampType: CREATE_TIME
[INFO] Record Value: {"message":"interesset eros vel elit salutatus"}
```


## Cleanup

1. To delete the resources deployed to your AWS account via AWS SAM, run the following command:
    
    ```bash
    sam delete
    ```

2. Also delete the resources created in step 5 of Requirements by deleting the corresponding CloudFormation template.
---

Copyright 2024 Amazon.com, Inc. or its affiliates. All Rights Reserved.

SPDX-License-Identifier: MIT-0
