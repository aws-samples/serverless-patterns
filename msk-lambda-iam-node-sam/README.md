# Node.js AWS Lambda Kafka consumer with IAM auth, using AWS SAM

This pattern is an example of a Lambda function that consumes messages from an Amazon Managed Streaming for Kafka (Amazon MSK) topic, where the MSK Cluster has been configured to use IAM authentication.  

This project contains source code and supporting files for a serverless application that you can deploy with the AWS Serverless Application Model (AWS SAM) CLI. It includes the following files and folders.

- HandlerKafka - Code for the application's Lambda function.
- events - Invocation events that you can use to invoke the function.
- template_original.yaml - An AWS SAM template that defines the application's AWS resources.
- MSKAndKafkaClientEC2.yaml - An AWS CloudFormation template file that can be used to deploy an MSK cluster and also deploy an Amazon EC2 instance with all prerequisites already installed, so you can directly build and deploy the Lambda function and test it out.

The application creates a Lambda function that listens to Kafka messages on a topic of an MSK Cluster. These resources are defined in the `template_original.yaml` file in this project. You can update the template to add AWS resources through the same deployment process that updates your application code.

Important: this application uses various AWS services and there are costs associated with these services after the Free Tier usage - please see the [AWS Pricing page](https://aws.amazon.com/pricing/) for details. You are responsible for any AWS costs incurred. No warranty is implied in this example.

## Requirements

* [Create an AWS account](https://portal.aws.amazon.com/gp/aws/developer/registration/index.html) if you do not already have one and log in. The IAM user that you use must have sufficient permissions to make necessary AWS service calls and manage AWS resources.

## Deploy the CloudFormation template to create the MSK Cluster and Client EC2 instance

* [Deploy the CloudFormation template using the file MSKAndKafkaClientEC2.yaml] - You can go to the AWS CloudFormation console, create a new stack by specifying the template file. You can keep the defaults for input parameters or modify them as necessary. Wait for the CloudFormation stack to be created. This CloudFormation template will create an MSK cluster (Provisioned or Serverless based on your selection). It will also create an EC2 instance that you can use as a client.

* [Connect to the EC2 instance] - Once the CloudFormation stack is created, you can go to the EC2 console and log into the instance using either "Connect using EC2 Instance Connect" or "Connect using EC2 Instance Connect Endpoint" option under the "EC2 Instance Connect" tab.
Note: You may need to wait for some time after the CloudFormation stack is created, as some UserData scripts continue running after the CloudFormation stack shows Created.

* [Check if Kafka Topic has been created] - Once you are logged into the EC2 instance, you should be in the `/home/ec2-user` folder. Check to see the contents of the file `kafka_topic_creator_output.txt` by running the command `cat kafka_topic_creator_output.txt`. You should see an output such as "Created topic MskIamNodejsLambdaTopic."

If you are not able to find the file `kafka_topic_creator_output.txt` or if it is blank or you see an error message, then you need to run `./kafka_topic_creator.sh`. This runs a script that creates the Kafka topic that the Lambda function will subscribe to.

## Pre-requisites to Deploy the sample Lambda function

The EC2 instance that was created by running the CloudFormation template has all the software that will be needed to deploy the Lambda function.

The AWS SAM CLI is a serverless tool for building and testing Lambda applications. It uses Docker to locally test your functions in an Amazon Linux environment that resembles the Lambda execution environment. It can also emulate your application's build environment and API.

* Node.js - We have installed the version of Node.js that you picked up at the time of specifying the input parameters to the CloudFormation template
* AWS SAM CLI - We have installed the AWS SAM CLI (https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-sam-cli-install.html)
* Docker - We have installed the Docker Community Edition on the EC2 instance (https://hub.docker.com/search/?type=edition&offering=community)

We have also cloned the Github repository for serverless-patterns on the EC2 instance already by running the below command
    ``` 
    git clone https://github.com/aws-samples/serverless-patterns.git
    ```
Change directory to the pattern directory:
    ```
    cd serverless-patterns/msk-Lambda-iam-node-sam
    ```
## Use the SAM CLI to build and test locally

Build your application with the `sam build` command.

```bash
sam build
```

The SAM CLI creates a deployment package, and saves it in the `.aws-sam/build` folder.

Test a single function by invoking it directly with a test event. An event is a JSON document that represents the input that the function receives from the event source. Test events are included in the `events` folder in this project.

Run functions locally and invoke them with the `sam local invoke` command.

```bash
sam local invoke --event events/event.json
```

You should see a response such as the below:
```
***** Begin sam local invoke response *****

START RequestId: b516e210-3534-443b-bacb-38a16ef5b76c Version: $LATEST
2024-12-09T07:43:02.057Z        05ddf736-39f9-4956-a8b1-d651883cdcba    INFO    Key:  myTopic-0
2024-12-09T07:43:02.058Z        05ddf736-39f9-4956-a8b1-d651883cdcba    INFO    Record:  {
  topic: 'myTopic',
  partition: 0,
  offset: 250,
  timestamp: 1678072110111,
  timestampType: 'CREATE_TIME',
  value: 'Zg==',
  headers: []
}
2024-12-09T07:43:02.060Z        05ddf736-39f9-4956-a8b1-d651883cdcba    INFO    Topic:  myTopic
2024-12-09T07:43:02.060Z        05ddf736-39f9-4956-a8b1-d651883cdcba    INFO    Partition:  0
2024-12-09T07:43:02.060Z        05ddf736-39f9-4956-a8b1-d651883cdcba    INFO    Offset:  250
2024-12-09T07:43:02.060Z        05ddf736-39f9-4956-a8b1-d651883cdcba    INFO    Timestamp:  1678072110111
2024-12-09T07:43:02.060Z        05ddf736-39f9-4956-a8b1-d651883cdcba    INFO    TimestampType:  CREATE_TIME
2024-12-09T07:43:02.060Z        05ddf736-39f9-4956-a8b1-d651883cdcba    INFO    Key: null
2024-12-09T07:43:02.060Z        05ddf736-39f9-4956-a8b1-d651883cdcba    INFO    Value: f
2024-12-09T07:43:02.060Z        05ddf736-39f9-4956-a8b1-d651883cdcba    INFO    Record:  {
  topic: 'myTopic',
  partition: 0,
  offset: 251,
  timestamp: 1678072111086,
  timestampType: 'CREATE_TIME',
  value: 'Zw==',
  headers: []
}
2024-12-09T07:43:02.061Z        05ddf736-39f9-4956-a8b1-d651883cdcba    INFO    Topic:  myTopic
2024-12-09T07:43:02.061Z        05ddf736-39f9-4956-a8b1-d651883cdcba    INFO    Partition:  0
2024-12-09T07:43:02.061Z        05ddf736-39f9-4956-a8b1-d651883cdcba    INFO    Offset:  251
2024-12-09T07:43:02.062Z        05ddf736-39f9-4956-a8b1-d651883cdcba    INFO    Timestamp:  1678072111086
2024-12-09T07:43:02.062Z        05ddf736-39f9-4956-a8b1-d651883cdcba    INFO    TimestampType:  CREATE_TIME
2024-12-09T07:43:02.062Z        05ddf736-39f9-4956-a8b1-d651883cdcba    INFO    Key: null
2024-12-09T07:43:02.062Z        05ddf736-39f9-4956-a8b1-d651883cdcba    INFO    Value: g
END RequestId: 05ddf736-39f9-4956-a8b1-d651883cdcba
REPORT RequestId: 05ddf736-39f9-4956-a8b1-d651883cdcba  Init Duration: 0.10 ms  Duration: 112.94 ms     Billed Duration: 113 ms Memory Size: 128 MB   Max Memory Used: 128 MB

***** End sam local invoke response *****
```

## Deploy the sample application


To deploy your application for the first time, run the following in your shell:

```bash
sam deploy --capabilities CAPABILITY_IAM --no-confirm-changeset --no-disable-rollback --region $AWS_REGION --stack-name msk-Lambda-iam-node-sam --guided
```

The sam deploy command will package and deploy your application to AWS, with a series of prompts. You can accept all the defaults by hitting Enter:

* **Stack Name**: The name of the stack to deploy to CloudFormation. This should be unique to your account and region, and a good starting point would be something matching your project name.
* **AWS Region**: The AWS region you want to deploy your app to.
* **Parameter MSKClusterName**: The name of the MSKCluster
* **Parameter MSKClusterId**: The unique ID of the MSKCluster
* **Parameter MSKTopic**: The Kafka topic on which the Lambda function will listen on
* **Confirm changes before deploy**: If set to yes, any change sets will be shown to you before execution for manual review. If set to no, the AWS SAM CLI will automatically deploy application changes.
* **Allow SAM CLI IAM role creation**: Many AWS SAM templates, including this example, create AWS IAM roles required for the AWS Lambda function(s) included to access AWS services. By default, these are scoped down to minimum required permissions. To deploy an AWS CloudFormation stack which creates or modifies IAM roles, the `CAPABILITY_IAM` value for `capabilities` must be provided. If permission isn't provided through this prompt, to deploy this example you must explicitly pass `--capabilities CAPABILITY_IAM` to the `sam deploy` command.
* **Disable rollback**: Defaults to No and it preserves the state of previously provisioned resources when an operation fails
* **Save arguments to configuration file**: If set to yes, your choices will be saved to a configuration file inside the project, so that in the future you can just re-run `sam deploy` without parameters to deploy changes to your application.
* **SAM configuration file [samconfig.toml]**: Name of the configuration file to store configuration information locally
* **SAM configuration environment [default]**: Environment for storing deployment information locally

You should get a message "Successfully created/updated stack - <StackName> in <Region>" if all goes well
    
**Note: In case you want to deploy the Lambda function by pointing to an existing MSK Cluster and not the one created by running the CloudFormation template provided in this pattern, you will need to modify the values of the parameters MSKClusterName and MSKClusterId accordingly**

Once you have run `sam deploy --guided` mode once and saved arguments to a configuration file (samconfig.toml), you can use `sam deploy` in future to use these defaults.

## How it works

This pattern creates a Lambda function along with a Lambda Event Source Mapping(ESM) resource. This maps a Kafka topic on an MSK Cluster as a trigger to a Lambda function. The ESM takes care of polling the Kafka topic and then invokes the Lambda function with a batch of messages.

## Test the sample application

Once the Lambda function is deployed, send some Kafka messages to the topic that the Lambda function is listening on, on the MSK server.

For your convenience, a script has been created on the EC2 instance that was provisioned using CloudFormation.

`cd /home/ec2-user`

You should see a script called kafka_message_sender.sh. Run that script and you should be able to send a new Kafka message in every line as shown below

```
[ec2-user@ip-10-0-0-126 ~]$ sh kafka_message_sender.sh
>My first message
>My second message
>My third message
>My fourth message
>My fifth message
>My sixth message
>My seventh message
>My eigth message
>My ninth message
>My tenth message
>Ctrl-C
```
Either send at least 10 messages or wait for 300 seconds (check the values of BatchSize: 10 and MaximumBatchingWindowInSeconds: 300 in the template.yaml file)

Then check Amazon CloudWatch logs and you should see messages in the CloudWatch Log Group with the name of the deployed Lambda function.

The Lambda code parses the Kafka messages and outputs the fields in the Kafka messages to CloudWatch logs.

A single Lambda function receives a batch of messages. The messages are received as a map with each key being a combination of the topic and the partition, as a single batch can receive messages from multiple partitions.

Each key has a list of messages. Each Kafka message has the following properties - `Topic`, `Partition`, `Offset`, `TimeStamp`, `TimeStampType`, `Key`, and `Value`.

The `Key` and `Value` are base64 encoded and have to be decoded. A message can also have a list of headers, each header having a key and a value.

The code in this example prints out the fields in the Kafka message and also decrypts the key and the value and logs them to CloudWatch logs.

## Cleanup
 
You can first clean-up the Lambda function by running the `sam delete` command

```
cd /home/ec2-user/serverless-patterns/msk-Lambda-iam-node-sam
sam delete

```
confirm by pressing y for both the questions
You should see the Lambda function getting deleted and a final confirmation "Deleted successfully" on the command line

Next, you delete the CloudFormation template that created the MSK cluster and the EC2 instance by going to the CloudFormation console and selecting the stack. Then select the "Delete" button. Please note that it might take a while to complete.

----
Copyright 2023 Amazon.com, Inc. or its affiliates. All Rights Reserved.

SPDX-License-Identifier: MIT-0
