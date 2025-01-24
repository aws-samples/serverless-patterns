# das-lambda-java-sam
# Java AWS Lambda Database Activity Streams Processing, using AWS SAM

This pattern is an example of a Lambda function that consumes messages from an Amazon Kinesis Data Stream created when Database Activity Streams is enabled on an Amazon Aurora Postgres database. This pattern also demonstrates how the records are decrypted, filtered for heartbeat events and then how an OpenSearch Ingestion Pipeline is set-up to send the Database Activity Stream events are sent to an Amazon OpenSearch domain

This project contains source code and supporting files for a serverless application that you can deploy with the SAM CLI. It includes the following files and folders.

- das_consumer_sam_project/database_activity_streams_event_consumer_function/src/main/java - Code for the application's Lambda function.
- das_consumer_sam_project/database_activity_streams_event_consumer_function/pom.xml - Maven file for building the Lambda function.
- das_consumer_sam_project/template.yaml - SAM template for deploying the Lambda function.
- setup-das-cfn.yaml - A Cloudformation template file that can be used to deploy all the resources needed as part of this project. The CloudFormation template also deploys an EC2 machine that builds and deploys the AWS Lambda function and performs other necessary configuration scripts in the UserData section.
- BootStrapFromCloudShell.sh - A shell script that needs to be run as an admin user of the AWS account to create a new IAM user that will be used to run the CloudFormation template to create all the resources for the project.
- IngestionPipelineConfig.yaml - A template for the Amazon OpenSearch Ingestion Pipeline that will be executed in the CloudFormation template to create the Amazon OpenSearch Ingestion Pipeline that will send the Database Activity Streams records to an Amazon OpenSearch domain.
- UpdateOSIRole.sh - A shell script that gets called from within the CloudFormation template to add an IAM role as a backend role in the Amazon OpenSearch domain. This will allow the IAM role to index the incoming records in the Amazon OpenSearch domain.
- RestartOSIPipeline.sh - A utility shell script that has been provided in case the Amazon OpenSearch Ingestion Pipeline needs to be restarted.

Important: this application uses various AWS services and there are costs associated with these services after the Free Tier usage - please see the [AWS Pricing page](https://aws.amazon.com/pricing/) for details. You are responsible for any AWS costs incurred. No warranty is implied in this example.

## Requirements

* [Create an AWS account](https://portal.aws.amazon.com/gp/aws/developer/registration/index.html) if you do not already have one and log in. The IAM user that you use must have sufficient permissions to make necessary AWS service calls and manage AWS resources.

## Run the BootStrapFromCloudShell.sh script

* [Log in to the AWS Account as Admin User] - You need to log in to the AWS Account as either root or as an user with Admin privileges

* [Open AWS CloudShell and checkout BootStrapFromCloudShell.sh script from Github] - Once you are inside AWS Cloudshell in the AWS console, type the following commands

```
git clone -n --depth=1 --filter=tree:0 https://github.com/aws-samples/serverless-patterns.git
cd serverless-patterns
git sparse-checkout set --no-cone /das-lambda-java-sam
git checkout

```

* [Execute the BootStrapFromCloudShell.sh script to create an IAM user and store keys in Secrets Manager] - Once the BootStrapFromCloudShell.sh script has been checked out from Github, execute the following commands in your CloudShell. Substitute the <username> and <password> with values for the IAM user you want to create. The password needs to be at least 8 characters long. 

```
cd das-lambda-java-sam
sh ./BootStrapFromCloudShell.sh <username> <password>

```

Once the above command is done executing, log out of the AWS account and log in to the AWS console using the new <username> and <password>. You will be asked to change the password upon first login. Once you are logged in as the IAM user, follow the next step.
    
** Note: If you do not have AWS console access and would rather run CloudFormation from the command line, do not run the BootStrapFromCloudShell.sh script. Instead run the BootStrapFromCloudShellNoConsoleAccess.sh <username> as shown below ** 

```
cd das-lambda-java-sam
sh ./BootStrapFromCloudShellNoConsoleAccess.sh <username>

```

Once the above command is done running, it is recommended to create an AWS CLI profile on your local machine from where you can deploy the CloudFormation template. In order to do that, you need to run the following commands

```
On the AWS CloudShell, run the following and note down the values of the outputs of each of the commands below

aws configure get aws_access_key_id --profile <username> - where <username> is the same as the <username> parameter that was passed to the BootStrapFromCloudShellNoConsoleAccess.sh command above

aws configure get aws_secret_access_key --profile <username>

aws configure get region --profile <username>

On your local machine, run the following

aws configure set aws_access_key_id <ACCESSKEYID> --profile <username> - where <ACCESSKEYID> is the output of the first command above

aws configure set aws_secret_access_key <SECRETKEYID> --profile <username> - where <SECRETKEYID> is the output of the second command above

aws configure set region <AWS_REGION> --profile <username> - where <AWS_REGION> is the output of the third command above

Once you have configured the AWS profile on your local machine, run the following command to verify the profile has been created correctly

aws sts get-caller-identity --profile <username>

```

## Run the CloudFormation template to create the AWS resources

* [Checkout from Github on your local machine] - Type the following commands from any folder on your local machine to get the CloudFormation template from Github

```
git clone -n --depth=1 --filter=tree:0 https://github.com/aws-samples/serverless-patterns.git
cd serverless-patterns
git sparse-checkout set --no-cone /das-lambda-java-sam
git checkout
cd das-lambda-java-sam

```

The current folder should now contain the CloudFormation template file setup-das-cfn.yaml

You can log in to the AWS console using the new user that was just created and run CloudFormation using the template file setup-das-cfn.yaml

Accept defaults for all the input parameters or modify them as needed.

** Note: If you do not have AWS console access, you can deploy the CloudFormation from your local machine or CloudShell.

Execute the following commands from a terminal on your local machine or CloudShell **

```
aws ec2 create-key-pair --key-name DASKeyPair --key-format pem --key-type rsa --profile <username> --query 'KeyMaterial' --output text > DASKeyPair.pem - Make sure to save this .pem file in a secure location as you will need it later to ssh into the EC2 machine that will be created as part of the CloudFormation stack

chmod 400 DASKeyPair.pem

** If you modify the name of the key-name from DASKeyPair, then make sure to replace it in the CloudFormation template as well **

AWS_REGION=$(aws configure get region --profile <username>)

cd <folder where you had checked out the https://github.com/aws-samples/serverless-patterns.git>

cd /serverless-patterns/das-lambda-java-sam

Now deploy the CloudFormation stack by running the RunCloudformationStack.sh file as follows

sh ./RunCloudformationStack.sh <username> <stackname> <a short unique random string> - replace the value of <username> and provide a value for the name of the CloudFormation stack by replacing <stackname>

```

** If you need to replace the values of any input parameters to the CloudFormation stack, then add those in the --parameter-overrides section of the RunCloudformationStack.sh **

Wait for the Cloudformation stack to be created. This can take a very long time. Even after the CloudFormation template shows a status of "Create Complete", wait at least another 15 minutes, as the UserData scripts inside the CloudFormation tempate continue running.

This Cloudformation template will create multiple AWS resources such as an Amazon Aurora Postgres Database, an Amazon OpenSearch domain, an AWS Lambda function that will process the Database Activity Streams (DAS) events, an S3 bucket to which the Lambda function will write the DAS events records, an OpenSearch Ingestion Pipeline, an SQS queue for triggering the OpenSearch Ingestion Pipeline and other supporting resources. It will also create an EC2 machine that already has the Postgres client installed for you to run SQL commands on the Aurora Postgres database.

* [Connect to the EC2 machine] - Once the Cloudformation stack is created, you can go to the EC2 console and log into the machine using either "Connect using EC2 Instance Connect" or "Connect using EC2 Instance Connect Endpoint" option under the "EC2 Instance Connect" tab.
Note: You may need to wait for some time after the Cloudformation stack is created, as some UserData scripts continue running after the Cloudformation stack shows Created.

** If you are not allowed AWS console access as an IAM user, you can ssh into the EC2 machine by running the command below to get the Public IP address of the EC2 machine **

```
EC2_PUBLIC_IP=$(aws cloudformation describe-stacks --stack-name <stackname> --query "Stacks[*].Outputs[?OutputKey=='ReverseProxyEC2PublicIP'].OutputValue" --output text)

echo $EC2_PUBLIC_IP

To ssh you will need the DASKeyPair.pem file that you had created in an earlier step


```

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
    cd serverless-patterns/msk-lambda-iam-java-sam
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
                                                                                                                                                       
Mounting /home/ec2-user/serverless-patterns/msk-lambda-iam-java-sam/.aws-sam/build/LambdaMSKConsumerJavaFunction as /var/task:ro,delegated, inside     
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
sam deploy --capabilities CAPABILITY_IAM --no-confirm-changeset --no-disable-rollback --region $AWS_REGION --stack-name msk-lambda-iam-java-sam --guided
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


## Test the sample application

Once the lambda function is deployed, send some Kafka messages on the topic that the lambda function is listening on, on the MSK server.

For your convenience, a script has been created on the EC2 machine that was provisioned using Cloudformation.

cd /home/ec2-user

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

Then check Cloudwatch logs and you should see messages for the Cloudwatch Log Group with the name of the deployed Lambda function.

The lambda code parses the Kafka messages and outputs the fields in the Kafka messages to Cloudwatch logs

A single lambda function receives a batch of messages. The messages are received as a map with each key being a combination of the topic and the partition, as a single batch can receive messages from multiple partitions.

Each key has a list of messages. Each Kafka message has the following properties - Topic, Partition, Offset, TimeStamp, TimeStampType, Key and Value

The Key and Value are base64 encoded and have to be decoded. A message can also have a list of headers, each header having a key and a value.

The code in this example prints out the fields in the Kafka message and also decrypts the key and the value and logs them in Cloudwatch logs.

## Cleanup

You can first clean-up the Lambda function by running the sam delete command

```
cd /home/ec2-user/serverless-patterns/msk-lambda-iam-java-sam
sam delete

```
confirm by pressing y for both the questions
You should see the lambda function getting deleted and a final confirmation "Deleted successfully" on the command-line

Next you need to delete the Cloudformation template that created the MSK Server and the EC2 machine by going to the Cloudformation console and selecting the stack and then hitting the "Delete" button. It will run for sometime but eventually you should see the stack getting cleaned up. If you get an error message that says the stack could not be deleted, please retry again and do a Force Delete. The reason this may happen is because ENIs created by the deplayed Lambda function in your VPC may prevent the VPC from being deleted even after deleting the lambda function.