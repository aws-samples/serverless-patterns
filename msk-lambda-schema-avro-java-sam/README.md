# msk-lambda-schema-avro-java-sam
# Java AWS Lambda Kafka consumer and AVRO producer with Schema Registry and AVRO, using AWS SAM

This pattern is an example of Lambda functions that:
1. Consume messages from an Amazon Managed Streaming for Kafka (Amazon MSK) topic
2. Produce AVRO-formatted messages to an Amazon MSK topic using Schema Registry

Both functions use IAM authentication to connect to the MSK Cluster and leverage AWS Glue Schema Registry for AVRO schema management.

This project contains source code and supporting files for a serverless application that you can deploy with the SAM CLI. It includes the following files and folders.

- kafka_event_consumer_function/src/main/java - Code for the consumer Lambda function.
- kafka_event_producer_function/src/main/java - Code for the AVRO producer Lambda function.
- events - Invocation events that you can use to invoke the functions.
- kafka_event_consumer_function/src/test/java - Unit tests for the consumer code.
- template_original.yaml - A template that defines the application's Lambda functions.
- MSKAndKafkaClientEC2.yaml - A Cloudformation template file that can be used to deploy an MSK cluster and also deploy an EC2 machine with all pre-requisities already installed, so you can directly build and deploy the lambda functions and test them out.

Important: this application uses various AWS services and there are costs associated with these services after the Free Tier usage - please see the [AWS Pricing page](https://aws.amazon.com/pricing/) for details. You are responsible for any AWS costs incurred. No warranty is implied in this example.

## Requirements

* [Create an AWS account](https://portal.aws.amazon.com/gp/aws/developer/registration/index.html) if you do not already have one and log in. The IAM user that you use must have sufficient permissions to make necessary AWS service calls and manage AWS resources.

## Run the Cloudformation template to create the MSK Cluster and Client EC2 machine

* [Run the Cloudformation template using the file MSKAndKafkaClientEC2.yaml] - You can go to the AWS Cloudformation console, create a new stack by specifying the template file. You can keep the defaults for input parameters or modify them as necessary. Wait for the Cloudformation stack to be created. This Cloudformation template will create an MSK cluster (Provisioned or Serverless based on your selection). It will also create an EC2 machine that you can use as a client.

* [Connect to the EC2 machine] - Once the Cloudformation stack is created, you can go to the EC2 console and log into the machine using either "Connect using EC2 Instance Connect" or "Connect using EC2 Instance Connect Endpoint" option under the "EC2 Instance Connect" tab.
Note: You may need to wait for some time after the Cloudformation stack is created, as some UserData scripts continue running after the Cloudformation stack shows Created.

* [Check if Kafka Topic has been created] - Once you are inside the EC2 machine, you should be in the /home/ec2-user folder. Check to see the contents of the file kafka_topic_creator_output.txt by running the command cat kafka_topic_creator_output.txt. You should see an output such as "Created topic MskIamJavaLambdaTopic."

If you are not able to find the file kafka_topic_creator_output.txt or if it is blank or you see an error message, then you need to run the file ./kafka_topic_creator.sh. This file runs a script that goes and creates the Kafka topic that the Lambda function will subscribe to.

## Pre-requisites to Deploy the sample Lambda function

The EC2 machine that was created by running the Cloudformation template has all the software that will be needed to deploy the Lambda function.

The AWS SAM CLI is a serverless tool for building and testing Lambda applications. It uses Docker to locally test your functions in an Amazon Linux environment that resembles the Lambda execution environment. It can also emulate your application's build environment and API.

* Java - On the EC2 machine, we have installed the version of Java that you selected. We have installed Amazon Corrretto JDK of the version that you had selected at the time of specifying the input parameters in the Cloudformation template. At the time of publishing this pattern, only Java versions 11, 17 and 21 are supported by AWS SAM
* Maven - On the EC2 machine, we have installed Maven (https://maven.apache.org/install.html)
* AWS SAM CLI - We have installed the AWS SAM CLI (https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-sam-cli-install.html)
* Docker - We have installed the Docker Community Edition on the EC2 machine (https://hub.docker.com/search/?type=edition&offering=community)

We have also cloned the Github repository for serverless-patterns on the EC2 machine already by running the below command
    ``` 
    git clone https://github.com/aws-samples/serverless-patterns.git
    ```
Change directory to the pattern directory:
    ```
    cd serverless-patterns/msk-lambda-schema-avro-java-sam
    ```

## Use the SAM CLI to build and test locally

Build your application with the `sam build` command.

```bash
sam build
```

The SAM CLI installs dependencies defined in `kafka_event_consumer_function/pom.xml`, creates a deployment package, and saves it in the `.aws-sam/build` folder.

Test a single function by invoking it directly with a test event. An event is a JSON document that represents the input that the function receives from the event source. Test events are included in the `events` folder in this project.

Run functions locally and invoke them with the `sam local invoke` command.

```bash
sam local invoke --event events/event.json
```

You should see a response such as the below:

```
***** Begin sam local invoke response *****

Invoking com.amazonaws.services.lambda.samples.events.msk.HandlerMSK::handleRequest (java11)                                                           
Local image is up-to-date                                                                                                                              
Using local image: public.ecr.aws/lambda/java:11-rapid-x86_64.                                                                                         
                                                                                                                                                       
Mounting /home/ec2-user/serverless-patterns/msk-lambda-schema-avro-java-sam/.aws-sam/build/LambdaMSKConsumerJavaFunction as /var/task:ro,delegated, inside     
runtime container                                                                                                                                      
START RequestId: 4484bb15-6749-4307-92d1-8ba2221e2218 Version: $LATEST
START RequestId: 4484bb15-6749-4307-92d1-8ba2221e2218 Version: $LATEST
Picked up JAVA_TOOL_OPTIONS: -XX:+TieredCompilation -XX:TieredStopAtLevel=1
Received this message from Kafka - KafkaMessage [topic=myTopic, partition=0, timestamp=1678072110111, timestampType=CREATE_TIME, key=null, value=Zg==, decodedKey=null, decodedValue=f, headers=[]]Message in JSON format : {
  "topic": "myTopic",
  "partition": 0,
  "offset": 250,
  "timestamp": 1678072110111,
  "timestampType": "CREATE_TIME",
  "value": "Zg\u003d\u003d",
  "decodedKey": "null",
  "decodedValue": "f",
  "headers": []
}Received this message from Kafka - KafkaMessage [topic=myTopic, partition=0, timestamp=1678072111086, timestampType=CREATE_TIME, key=null, value=Zw==, decodedKey=null, decodedValue=g, headers=[]]Message in JSON format : {
  "topic": "myTopic",
  "partition": 0,
  "offset": 251,
  "timestamp": 1678072111086,
  "timestampType": "CREATE_TIME",
  "value": "Zw\u003d\u003d",
  "decodedKey": "null",
  "decodedValue": "g",
  "headers": []
}All Messages in this batch = [
  {
    "topic": "myTopic",
    "partition": 0,
    "offset": 250,
    "timestamp": 1678072110111,
    "timestampType": "CREATE_TIME",
    "value": "Zg\u003d\u003d",
    "decodedKey": "null",
    "decodedValue": "f",
    "headers": []
  },
  {
    "topic": "myTopic",
    "partition": 0,
    "offset": 251,
    "timestamp": 1678072111086,
    "timestampType": "CREATE_TIME",
    "value": "Zw\u003d\u003d",
    "decodedKey": "null",
    "decodedValue": "g",
    "headers": []
  }
]END RequestId: fc96203d-e0c0-4c30-b332-d16708b25d3e
REPORT RequestId: fc96203d-e0c0-4c30-b332-d16708b25d3e  Init Duration: 0.06 ms  Duration: 474.31 ms     Billed Duration: 475 ms Memory Size: 512 MB   Max Memory Used: 512 MB
"200 OK"

***** End sam local invoke response *****
```


## Deploy the sample application


To deploy your application for the first time, run the following in your shell:

```bash
sam deploy --capabilities CAPABILITY_IAM --no-confirm-changeset --no-disable-rollback --region $AWS_REGION --stack-name msk-lambda-schema-avro-java-sam --guided
```

The sam deploy command will package and deploy your application to AWS, with a series of prompts. You can accept all the defaults by hitting Enter:

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
    
**Note: In case you want to deploy the Lambda function by pointing to an existing MSK Cluster and not the one created by running the CloudFormation template provided in this pattern, you will need to modify the values of the parameters MSKClusterName and MSKClusterId accordingly**


## Test the sample application

Once the Lambda functions are deployed, you can test the application by invoking the producer Lambda function, which will generate AVRO-formatted messages to the MSK topic. The consumer Lambda function will then automatically process these messages.

### Option 1: Invoke the producer Lambda function using AWS CLI

You can invoke the producer Lambda function using the AWS CLI with the following command:

```bash
aws lambda invoke \
  --function-name msk-lambda-schema-avro-java-sam-LambdaMSKProducerJavaFunction-XXXXXXXXXXXX \
  --payload '{"message": "Test message using AVRO and Schema Registry"}' \
  --cli-binary-format raw-in-base64-out \
  response.json
```

You can find the exact function name in the AWS Lambda console or by running:

```bash
aws lambda list-functions --query "Functions[?contains(FunctionName, 'Producer')].FunctionName"
```

### Option 2: Invoke the producer Lambda function using AWS Console

1. Open the [AWS Lambda Console](https://console.aws.amazon.com/lambda)
2. Find and select your producer Lambda function (it will be named something like `msk-lambda-schema-avro-java-sam-LambdaMSKProducerJavaFunction-XXXXXXXXXXXX`)
3. Click on the "Test" tab
4. Create a new test event with the following JSON payload:
   ```json
   {
     "message": "Test message using AVRO and Schema Registry"
   }
   ```
5. Click "Test" to invoke the function

### Verify the results

After invoking the producer function, check the CloudWatch logs for both Lambda functions:

1. Open the [CloudWatch Logs Console](https://console.aws.amazon.com/cloudwatch/home#logs:)
2. Find the log groups for both your producer and consumer Lambda functions:
   - Producer log group: `/aws/lambda/msk-lambda-schema-avro-java-sam-LambdaMSKProducerJavaFunction-XXXXXXXXXXXX`
   - Consumer log group: `/aws/lambda/msk-lambda-schema-avro-java-sam-LambdaMSKConsumerJavaFunction-XXXXXXXXXXXX`
   
   You can search for these log groups by typing "msk-lambda-schema-avro-java-sam" in the filter box.
   
3. Click on each log group and then select the most recent log stream (typically named with a timestamp and UUID)
4. In the producer logs, look for entries showing:
   - Successful serialization of the message using AVRO format
   - Successful registration or retrieval of the schema from Schema Registry
   - Confirmation that the message was sent to the MSK topic
   
5. In the consumer logs, look for entries showing:
   - Receipt of the message batch from the MSK topic
   - Successful deserialization of the AVRO message
   - The decoded message content and any processing performed on it

The consumer Lambda function will automatically process messages from the MSK topic. It parses the Kafka messages and outputs the fields in the Kafka messages to CloudWatch logs.

Each key has a list of messages. Each Kafka message has the following properties - Topic, Partition, Offset, TimeStamp, TimeStampType, Key and Value

The Key and Value are base64 encoded and have to be decoded. A message can also have a list of headers, each header having a key and a value.

The code in this example prints out the fields in the Kafka message and also decrypts the key and the value and logs them in Cloudwatch logs.

## Cleanup

You can first clean-up the Lambda function by running the sam delete command

```
cd /home/ec2-user/serverless-patterns/msk-lambda-schema-avro-java-sam
sam delete

```
confirm by pressing y for both the questions
You should see the lambda function getting deleted and a final confirmation "Deleted successfully" on the command-line

Next you need to delete the Cloudformation template that created the MSK Server and the EC2 machine by going to the Cloudformation console and selecting the stack and then hitting the "Delete" button. It will run for sometime but eventually you should see the stack getting cleaned up. If you get an error message that says the stack could not be deleted, please retry again and do a Force Delete. The reason this may happen is because ENIs created by the deplayed Lambda function in your VPC may prevent the VPC from being deleted even after deleting the lambda function.