# AWS Lambda function subscribed to an Amazon MSK Kafka topic with Avro and Schema Registry (Java)

This pattern is an example of Lambda functions that:
1. Consume messages from an Amazon Managed Streaming for Kafka (Amazon MSK) topic
2. Produce Avro-formatted messages to an Amazon MSK topic using Schema Registry

Both functions use IAM authentication to connect to the MSK Cluster and use AWS Glue Schema Registry for Avro schema management. The Glue Schema Registry and Contact Schema are created as part of the SAM deployment.

This project contains source code and supporting files for a serverless application that you can deploy with the SAM CLI. It includes the following files and folders.

- `kafka_event_consumer_function/src/main/java` - Code for the consumer Lambda function.
- `kafka_event_producer_function/src/main/java` - Code for the Avro producer Lambda function.
- `events` - Invocation events that you can use to invoke the functions.
- `kafka_event_consumer_function/src/test/java` - Unit tests for the consumer code.
- `template.yaml` - A template that defines the application's Lambda functions, Glue Schema Registry, and Contact Schema.
- `template_original.yaml` - The original template with placeholders that get replaced during deployment.
- `MSKAndKafkaClientEC2.yaml` - A CloudFormation template file that can be used to deploy an MSK cluster and also deploy an EC2 machine with all pre-requisites already installed, so you can directly build and deploy the lambda functions and test them out.

> [!Important] 
> This application uses various AWS services and there are costs associated with these services after the Free Tier usage - please see the [AWS Pricing page](https://aws.amazon.com/pricing/) for details. You are responsible for any AWS costs incurred.

## Requirements

* [Create an AWS account](https://portal.aws.amazon.com/gp/aws/developer/registration/index.html) if you do not already have one and log in. The IAM user that you use must have sufficient permissions to make necessary AWS service calls and manage AWS resources.

## Create the MSK Cluster and Client EC2 machine using CloudFormation template

There is a CloudFormation template to deploy an Amazon MSK Cluster. You can deploy Amazon MSK to test this pattern or use your existing Kafka cluster. 

### Create Amazon MSK Cluster

* Run the CloudFormation template using the file `MSKAndKafkaClientEC2.yaml`.
* Browse to the Amazon CloudFormation console, create a new stack by specifying the template file. You can keep the defaults for input parameters or modify them as necessary. Wait for the CloudFormation stack to be created. This CloudFormation template will create an MSK cluster (Provisioned or Serverless based on your selection). It will also create an EC2 machine that you can use as a client.

### Connect to the EC2 machine

* Once the CloudFormation stack is created, you can go to the EC2 console and log into the machine using either **Connect using EC2 Instance Connect** or **Connect using EC2 Instance Connect Endpoint** option under the *EC2 Instance Connect* tab.

> [!NOTE]  
> You may need to wait for some time after the CloudFormation stack is created, as some UserData scripts continue running after the CloudFormation stack shows *Created*.

### Check if Kafka Topic has been created
* Once you are connected to the EC2 machine, you should be in the `/home/ec2-user` folder. Check to see the contents of the file `kafka_topic_creator_output.txt` by running the command:

```bash
cat kafka_topic_creator_output.txt
```
You should see an output such as *Created topic MskIamJavaLambdaTopic.*

If you are not able to find the file `kafka_topic_creator_output.txt` or if it is blank or you see an error message, then you need to run the file:

```bash
./kafka_topic_creator.sh
```

This file runs a script that creates the Kafka topic that the Lambda function will subscribe to.

## Pre-requisites to Deploy the sample Lambda function

The EC2 machine that was created by running the CloudFormation template has all the software needed to deploy the Lambda functions.

* **[AWS Serverless Application Model](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-sam-cli-install.html) (AWS SAM) CLI**  is a serverless tool for building and testing Lambda applications. It uses Docker to locally test your functions in an Amazon Linux environment that resembles the Lambda execution environment. It can also emulate your application's build environment and API.

* **Java** - The Amazon Corretto JDK version that you selected when specifying the input parameters in the CloudFormation template. At the time of publishing this pattern, Java versions 11, 17 and 21 are supported by AWS SAM

* **[Maven](https://maven.apache.org/install.html)** installed 

* **[Docker](https://hub.docker.com/search/?type=edition&offering=community)** - Installed ythe Docker Community Edition

* The **[serverless-patterns](https://github.com/aws-samples/serverless-patterns) GitHub repository** is cloned on the EC2 machine.

Change directory to the pattern directory:

```bash
cd serverless-patterns/msk-lambda-schema-avro-java-sam
```

## Build the application

Build your application with the `sam build` command.

```bash
sam build
```

SAM CLI installs dependencies defined in `kafka_event_consumer_function/pom.xml`, creates a deployment package, and saves it in the `.aws-sam/build` folder.

## Deploy the sample application

To deploy your application for the first time, run the following:

```bash
sam deploy --capabilities CAPABILITY_IAM --no-confirm-changeset --no-disable-rollback --region $AWS_REGION --stack-name msk-lambda-schema-avro-java-sam --guided
```

The `sam deploy` command packages and deploys your application to AWS, with a series of prompts. 

> [!NOTE]
> The script retrieves the required parameters from the CloudFormation outputs in the AWS Console after deploying the `MSKAndKafkaClientEC2.yaml` template. These outputs contain the necessary information for deploying the Lambda functions. If you connect to a different Kafka cluster, enter the values manually.

* **Stack Name**: The name of the stack to deploy to CloudFormation. This should be unique to your account and region, and a good starting point would be something matching your project name.
* **AWS Region**: The AWS region you want to deploy your app to.
* **Parameter MSKClusterName**: The name of the MSK Cluster. This will be `<stack-name>-cluster` from the CloudFormation template you deployed in the previous step.
* **Parameter MSKClusterId**: The unique ID of the MSK Cluster. This can be found in the MSK console or extracted from the MSK ARN in the CloudFormation outputs.
* **Parameter MSKTopic**: The Kafka topic on which the Lambda functions will produce and consume messages. You can find this in the CloudFormation outputs as `KafkaTopicForLambda`
* **Parameter GlueSchemaRegistryName**: The name of the Glue Schema Registry to be created (default: GlueSchemaRegistryForMSK).
* **Parameter ContactSchemaName**: The name of the Contact Schema to be created (default: ContactSchema).
* **Parameter VpcId**: The ID of the VPC where the MSK cluster is deployed. You can find this in the CloudFormation outputs as `VPCId`.
* **Parameter SubnetIds**: Comma-separated list of subnet IDs where the MSK cluster is deployed. You can find these in the CloudFormation outputs as `PrivateSubnetMSKOne`, `PrivateSubnetMSKTwo`, and `PrivateSubnetMSKThree`.
* **Parameter SecurityGroupIds**: Comma-separated list of security group IDs that allow access to the MSK cluster. You can find this in the CloudFormation outputs as `SecurityGroupId`.
* **Confirm changes before deploy**: If set to yes, any change sets will be shown to you before execution for manual review.
* **Allow SAM CLI IAM role creation**: Many AWS SAM templates, including this example, create AWS IAM roles required for the AWS Lambda function(s) included to access AWS services. By default, these are scoped down to minimum required permissions.
* **Disable rollback**: Defaults to No and it preserves the state of previously provisioned resources when an operation fails.
* **Save arguments to configuration file**: If set to yes, your choices will be saved to a configuration file inside the project.
* **SAM configuration file [samconfig.toml]**: Name of the configuration file to store configuration information locally.
* **SAM configuration environment [default]**: Environment for storing deployment information locally.

You should get a message "Successfully created/updated stack - <StackName> in <Region>" if all goes well.

## Test the sample application

Once the Lambda functions are deployed, you can test the application by invoking the producer Lambda function, which generates Avro-formatted messages to the MSK topic. The consumer Lambda function will then automatically process these messages.

### Invoke the producer Lambda function using the AWS SAM CLI

You can invoke the producer Lambda function using AWS SAM CLI with the following command:

```bash
sam remote invoke LambdaMSKProducerJavaFunction --region $AWS_REGION --stack-name msk-lambda-schema-avro-java-sam
```
After invoking the producer function, the CloudWatch logs are displayed.

Look for entries showing:
   - Confirmation that the message was sent to the MSK topic
   - Successful serialization of the message using AVRO format
   - Successful registration or retrieval of the schema from Schema Registry
   - Look for the *ZIP CODE DISTRIBUTION SUMMARY* section, which shows how many messages were generated with zip codes starting with *1000* and how many with *2000*.
   - You should see that the producer generated a mix of both zip code types   

You can also invoke the function using the AWS Console, or AWS CLI.

### Verify the results

View the consumer Lambda function logs using the Amazon CloudWatch logs console or CLI within the EC2 instance:
```
sam logs --name LambdaMSKConsumerJavaFunction --stack-name msk-lambda-schema-avro-java-sam --region $AWS_REGION
```
In the consumer logs, look for entries showing:
   - Receipt of the message batch from the MSK topic
   - Successful deserialization of the Avro message
   - The decoded message content and any processing performed on it
   - You should see that the consumer only processed messages with zip codes starting with *1000*
   - Messages with zip codes starting with *2000* are filtered out by the event source mapping and never reached the Lambda function

The consumer Lambda function automatically processes messages from the MSK topic. It parses the Kafka messages and outputs the fields in the Kafka messages to CloudWatch logs.

Each key has a list of messages. Each Kafka message has the following properties *Topic, Partition, Offset, TimeStamp, TimeStampType, Key and Value*

The *Key* and *Value* are base64 encoded and have to be decoded. [Powertools for AWS Lambda (Java)](https://docs.powertools.aws.dev/lambda/java/latest/) automatically decodes the base64 values. A message can also have a list of headers, each header having a key and a value.

The code in this example prints out the fields in the Kafka message and also decrypts the key and the value and logs them in CloudWatch logs.

This demonstrates how event source mapping filters can be used to efficiently process only the messages that match specific criteria, reducing Lambda invocation costs and processing overhead.

## Cleanup

### Delete Lambda  stack
First delete the Lambda functions by running the `sam delete` command

```
cd /home/ec2-user/serverless-patterns/msk-lambda-schema-avro-java-sam
sam delete
```
Confirm by pressing `y` for both the questions
The Lambda function are deleted and the tool displays a final confirmation *Deleted successfully* on the command-line

### Delete Amazon MSK cluster
To delete the CloudFormation template that created the Amazon MSK Server and the EC2 machine
1. Navigate to the CloudFormation console and select the stack. 
2. Select the *Delete* button. The deletion process run for some time. Once complete the stack should be removed. 

If you get an error message that says the stack could not be deleted, please retry again and do a *Force Delete*. The reason this may happen is because ENIs created by the deployed Lambda function in your VPC may prevent the VPC from being deleted even after deleting the Lambda function.