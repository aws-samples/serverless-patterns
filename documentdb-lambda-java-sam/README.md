# documentdb-lambda-iam-java-sam
# Java AWS Lambda DocumentDB Streams consumer, using AWS SAM

This pattern is an example of a Lambda function written in Java that consumes messages from Amazon DocumentDB Streams

This project contains source code and supporting files for a serverless application that you can deploy with the SAM CLI. It includes the following files and folders.

- documentdb_streams_consumer_dynamo_sam/documentdb_streams_event_consumer_function/src/main/java - Code for the application's Lambda function that will listen for DocumentDB Streams messages and write them to a DynamoDB table
- documentdb_streams_message_sender_json/src/main/java - Code for adding documents in a DocumentDB collection that will in turn generate DocumentDB streams 
- documentdb_streams_consumer_dynamo_sam/template_original.yaml - A template that defines the application's Lambda function to be used by SAM to deploy the lambda function
- DocumentDBAndMongoClientEC2.yaml - A Cloudformation template file that can be used to deploy a DocumentDB cluster and also deploy an EC2 machine with all pre-requisities already installed, so you can directly build and deploy the lambda function and test it out.
- connect_to_mongo_shell.sh - A shell script that can be used to connect to the DocumentDB cluster using the mongosh tool
- docdb_db_collection.sh - A shell script that will be used to create a database and a collection inside the DocumentDB cluster. The lambda function's event listener will be configured to listen for change stream events on this database and collection
- java_keystore_script.sh - A shell script that will be used to create a Java keystore file that will be required by the Sender program that will connect to the DocumentDB cluster and insert JSON documents in the created collection so that DocumentDB streams can then be generated for the lambda function to consume. The Java keystore is required to programmatically connect to the DocumentDB cluster
- mongodb-org-8.0.repo - This file is required in order to be able to install mongosh tool on the EC2 machine. mongosh is a command-line tool that can be used to connect to the DocumentDB cluster to perform administrative tasks as well as to perform CRUD operations on the DocumentDB cluster
- mongodbcolcreate.js - This file will be used to create a database and a collection inside the DocumentDB cluster. In order to programatically use the mongosh tool, a .js file needs to be passed as a --file argument to mongosh.

Important: this application uses various AWS services and there are costs associated with these services after the Free Tier usage - please see the [AWS Pricing page](https://aws.amazon.com/pricing/) for details. You are responsible for any AWS costs incurred. No warranty is implied in this example.

## Requirements

* [Create an AWS account](https://portal.aws.amazon.com/gp/aws/developer/registration/index.html) if you do not already have one and log in. The IAM user that you use must have sufficient permissions to make necessary AWS service calls and manage AWS resources.

## Run the Cloudformation template to create the DocumentDB Cluster and Client EC2 machine

* [Run the Cloudformation template using the file DocumentDBAndMongoClientEC2.yaml] - You can go to the AWS Cloudformation console, create a new stack by specifying the template file. You can keep the defaults for input parameters or modify them as necessary. Wait for the Cloudformation stack to be created. This Cloudformation template will create an Amazon DocumentDB cluster. It will also create an EC2 machine that you can use as a client.

* [Connect to the EC2 machine] - Once the CloudFormation stack is created, you can go to the EC2 console and log into the machine using either "Connect using EC2 Instance Connect" or "Connect using EC2 Instance Connect Endpoint" option under the "EC2 Instance Connect" tab.
Note: You may need to wait for some time after the CloudFormation stack is created, as some UserData scripts continue running after the Cloudformation stack shows Created.

* [Check if the database and cluster have been created inside DocumentDB cluster] - Once you are inside the EC2 machine, you should be in the /home/ec2-user folder. cd to the mongoshell folder and then run ./connect_to_mongo_shell.sh. This should connect the mongosh tool to the DocumentDB cluster that was created by the CloudFormation template. Once inside the mongosh, you can issue commands like show dbs to see if the database was created, use <database name> to switch to the created database, and then show collections to see if the collection was created. If you did not modify the defaults in the CloudFormation template, then the name of the database should be DocumentDBJavaLambdaDB and the name of the collection should be DocumentDBJavaLambdaCollection


## Pre-requisites to Deploy the sample Lambda function

The EC2 machine that was created by running the CloudFormation template has all the software that will be needed to deploy the Lambda function.

The AWS SAM CLI is a serverless tool for building and testing Lambda applications.

* Java - On the EC2 machine, we have installed the version of Java that you selected. We have installed Amazon Corrretto JDK of the version that you had selected at the time of specifying the input parameters in the Cloudformation template. At the time of publishing this pattern, only Java versions 11, 17 and 21 are supported by AWS SAM
* Maven - On the EC2 machine, we have installed Maven (https://maven.apache.org/install.html)
* AWS SAM CLI - We have installed the AWS SAM CLI (https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-sam-cli-install.html)

We have also cloned the Github repository for serverless-patterns on the EC2 machine already by running the below command
    ``` 
    git clone https://github.com/aws-samples/serverless-patterns.git
    ```
Change directory to the pattern directory:
    ```
    cd serverless-patterns/documentdb-lambda-java-sam
    ```

## Use the SAM CLI to build and deploy the lambda function

Build your application with the `sam build` command.

```bash
cd documentdb_streams_consumer_dynamo_sam
sam build
```

The SAM CLI installs dependencies defined in `documentdb_streams_consumer_dynamo_sam/documentdb_streams_event_consumer_function/pom.xml`, creates a deployment package, and saves it in the `.aws-sam/build` folder.

```


## Deploy the sample application


To deploy your application for the first time, run the following in your shell:

```bash
sam deploy --capabilities CAPABILITY_IAM --no-confirm-changeset --no-disable-rollback --region $AWS_REGION --stack-name documentdb-lambda-java-sam --guided
```

The sam deploy command will package and deploy your application to AWS, with a series of prompts. You can accept all the defaults by hitting Enter:

* **Stack Name**: The name of the stack to deploy to CloudFormation. This should be unique to your account and region, and a good starting point would be something matching your project name.
* **AWS Region**: The AWS region you want to deploy your app to.
* **Parameter StreamsProducerDocumentDBCluster**: The name of the DocumentDB Cluster that was created by the CloudFormation template
* **Parameter StreamsProducerDocumentDBDatabase**: The name of the DocumentDB database that will generate streaming events to be consumed by the Lambda function
* **Parameter StreamsProducerDocumentDBCollection**: The name of the DocumentDB collection that will generate streaming events to be consumed by the Lambda function
* **Parameter SecretsManagerARN**: The ARN of the Secrets Manager secret that has the username and password to connect to the DocumentDB cluster
* **Parameter Subnet1**: The first of the three private subnets where the DocumentDB cluster is deployed
* **Parameter Subnet2**: The second of the three private subnets where the DocumentDB cluster is deployed
* **Parameter Subnet3**: The third of the three private subnets where the DocumentDB cluster is deployed
* **Parameter SecurityGroup**: The security group of the lambda function. This can be the same as the security group of the EC2 machine that was created by the CloudFormation template
* **Confirm changes before deploy**: If set to yes, any change sets will be shown to you before execution for manual review. If set to no, the AWS SAM CLI will automatically deploy application changes.
* **Allow SAM CLI IAM role creation**: Many AWS SAM templates, including this example, create AWS IAM roles required for the AWS Lambda function(s) included to access AWS services. By default, these are scoped down to minimum required permissions. To deploy an AWS CloudFormation stack which creates or modifies IAM roles, the `CAPABILITY_IAM` value for `capabilities` must be provided. If permission isn't provided through this prompt, to deploy this example you must explicitly pass `--capabilities CAPABILITY_IAM` to the `sam deploy` command.
* **Disable rollback**: Defaults to No and it preserves the state of previously provisioned resources when an operation fails
* **Save arguments to configuration file**: If set to yes, your choices will be saved to a configuration file inside the project, so that in the future you can just re-run `sam deploy` without parameters to deploy changes to your application.
* **SAM configuration file [samconfig.toml]**: Name of the configuration file to store configuration information locally
* **SAM configuration environment [default]**: Environment for storing deployment information locally

You should get a message "Successfully created/updated stack - <StackName> in <Region>" if all goes well
    
**Note: In case you want to deploy the Lambda function by pointing to an existing DocumentDB Cluster and not the one created by running the CloudFormation template provided in this pattern, you will need to modify the values of the above parameters accordingly**


## Test the application

Once the lambda function is deployed, send some DocumentDB Streams messages by inputting documents in the Database and Collection that have been configured on the lambda function's event listener.

For your convenience, a Java program and a shell script has been created on the EC2 machine that was provisioned using Cloudformation.

cd /home/ec2-user/serverless-patterns/documentdb-lambda-java-sam/documentdb_streams_message_sender_json

You should see a script called commands.sh. Run that script by passing a random string and a number between 1 and 500

```
[ec2-user@ip-10-0-0-126 ~]$ sh ./commands.sh firstBatch 10
Now going to insert a row in DynamoDB for messageID = firstBatch-10-12-2025-08-10-62-1
Now done inserting a row in DynamoDB for messageID = firstBatch-10-12-2025-08-10-62-1
Now going to insert a row in DynamoDB for messageID = firstBatch-10-12-2025-08-10-62-2
Now done inserting a row in DynamoDB for messageID = firstBatch-10-12-2025-08-10-62-2
Now going to insert a row in DynamoDB for messageID = firstBatch-10-12-2025-08-10-62-3
Now done inserting a row in DynamoDB for messageID = firstBatch-10-12-2025-08-10-62-3
Now going to insert a row in DynamoDB for messageID = firstBatch-10-12-2025-08-10-62-4
Now done inserting a row in DynamoDB for messageID = firstBatch-10-12-2025-08-10-62-4
Now going to insert a row in DynamoDB for messageID = firstBatch-10-12-2025-08-10-62-5
Now done inserting a row in DynamoDB for messageID = firstBatch-10-12-2025-08-10-62-5
Now going to insert a row in DynamoDB for messageID = firstBatch-10-12-2025-08-10-62-6
Now done inserting a row in DynamoDB for messageID = firstBatch-10-12-2025-08-10-62-6
Now going to insert a row in DynamoDB for messageID = firstBatch-10-12-2025-08-10-62-7
Now done inserting a row in DynamoDB for messageID = firstBatch-10-12-2025-08-10-62-7
Now going to insert a row in DynamoDB for messageID = firstBatch-10-12-2025-08-10-62-8
Now done inserting a row in DynamoDB for messageID = firstBatch-10-12-2025-08-10-62-8
Now going to insert a row in DynamoDB for messageID = firstBatch-10-12-2025-08-10-62-9
Now done inserting a row in DynamoDB for messageID = firstBatch-10-12-2025-08-10-62-9
Now going to insert a row in DynamoDB for messageID = firstBatch-10-12-2025-08-10-62-10
Now done inserting a row in DynamoDB for messageID = firstBatch-10-12-2025-08-10-62-10
```

Either send at least 10 messages or wait for 300 seconds (check the values of BatchSize: 10 and MaximumBatchingWindowInSeconds: 300 in the template.yaml file)

Then check Cloudwatch logs and you should see messages for the Cloudwatch Log Group with the name of the deployed Lambda function.

When you run the above script, it inputs JSON records into the DocumentDB cluster in the database and collection that were created. This results in the DocumentDB streams publishing every document. The lambda function listens on the published DocumentDB streams messages

The lambda code parses the DocumentDB streams messages and outputs the fields in the messages to Cloudwatch logs

The lambda function also inputs each record into a DynamoDB table called DocumentDBStreamsConsumerDynamoDBTableJava (if you did not modify the default name in the sam template.yaml file)

You can go to the DynamoDB console and view the records.

You can also use the aws cli command below to view the count of records inserted into DynamoDB

```
aws dynamodb scan --table-name DocumentDBStreamsConsumerDynamoDBTableJava --select "COUNT"

```



## Cleanup

You can first clean-up the Lambda function by running the sam delete command

```
cd /home/ec2-user/serverless-patterns/documentdb-lambda-java-sam/documentdb_streams_consumer_dynamo_sam
sam delete

```
confirm by pressing y for both the questions
You should see the lambda function getting deleted and a final confirmation "Deleted successfully" on the command-line

Next you need to delete the Cloudformation template that created the DocumentDB cluster and the EC2 machine by going to the Cloudformation console and selecting the stack and then hitting the "Delete" button. It will run for sometime but eventually you should see the stack getting cleaned up. If you get an error message that says the stack could not be deleted, please retry again and do a Force Delete. The reason this may happen is because ENIs created by the deplayed Lambda function in your VPC may prevent the VPC from being deleted even after deleting the lambda function.