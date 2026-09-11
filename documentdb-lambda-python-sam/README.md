# Python AWS Lambda Amazon DocumentDB Streams consumer, using AWS SAM

This pattern demonstrates consuming messages from an Amazon DocumentDB stream with AWS Lambda. This Python Lambda function parses the stream data and writes the results to an Amazon DynamoDB table. The pattern provides an AWS CloudFormation template to install and configure an Amazon DocumentDB cluster, configures an Amazon EC2 instance with Amazon DocumentDB tools, and creates a Python producer for generating sample data. 

This project contains source code and supporting files for a serverless application that you can deploy with the SAM CLI. It includes the following files and folders.

- documentdb_streams_consumer_dynamo_sam/documentdb_streams_event_consumer_function/app.py - Code for the application's Lambda function that will listen for Amazon DocumentDB Streams messages and write them to a Amazon DynamoDB table
- documentdb_streams_message_sender_python/documentdb_streams_producer.py - Code for adding documents in a Amazon DocumentDB collection that generate Amazon DocumentDB stream records
- documentdb_streams_consumer_dynamo_sam/template_original.yaml - A template that defines the application's Lambda function to be used by SAM to deploy the function
- DocumentDBAndMongoClientEC2.yaml - An AWS CloudFormation template file that can be used to deploy an Amazon DocumentDB cluster and also deploy an Amazon EC2 instance with all prerequisites installed, so you can directly build and deploy the Lambda function and test it out.
- connect_to_mongo_shell.sh - A shell script that can be used to connect to the Amazon DocumentDB cluster using the mongosh tool
- docdb_db_collection.sh - A shell script that will be used to create a database and a collection inside the Amazon DocumentDB cluster. The lambda function's event listener will be configured to listen for change stream events on this database and collection
- mongodb-org-8.0.repo - This file is required to install mongosh tool on the EC2 instance. mongosh is a command-line tool used to connect to the Amazon DocumentDB cluster to perform administrative tasks, and CRUD operations on the Amazon DocumentDB cluster
- mongodbcolcreate.js - This file will be used to create a database and a collection inside the Amazon DocumentDB cluster. In order to programatically use the mongosh tool, a .js file needs to be passed as a --file argument to mongosh.

Important: this application uses various AWS services and there are costs associated with these services after the Free Tier usage - please see the [AWS Pricing page](https://aws.amazon.com/pricing/) for details. You are responsible for any AWS costs incurred. No warranty is implied in this example.

## Requirements

* [Create an AWS account](https://portal.aws.amazon.com/gp/aws/developer/registration/index.html) if you do not already have one and log in. The IAM user that you use must have sufficient permissions to make necessary AWS service calls and manage AWS resources.

## Deployment instructions
### Run the Cloudformation template to create the Amazon DocumentDB Cluster and Client Amazon EC2 instance

* [Run the Cloudformation template using the file DocumentDBAndMongoClientEC2.yaml] - You can go to the AWS Cloudformation console, create a new stack by specifying the template file. You can keep the defaults for input parameters or modify them as necessary. Wait for the Cloudformation stack to be created. This CloudFormation template will create an Amazon DocumentDB cluster. It will also create an EC2 instance that you can use as a client.

* [Connect to the EC2 instance] - Once the CloudFormation stack is created, you can go to the EC2 console and connect to the instance using either "Connect using EC2 Instance Connect" or "Connect using EC2 Instance Connect Endpoint" option under the "EC2 Instance Connect" tab. In case you are using SSM Instance connect, you are not initially placed in the home directory. If you connect as ssm-user, you need to sudo su to ec2-user for this to work.
Note: You may need to wait for some time after the CloudFormation stack is created, as some UserData scripts continue running post creation. 

The EC2 instance that was created by running the CloudFormation template has all the software that will be needed to deploy the Lambda function.

The AWS SAM CLI is a serverless tool for building and testing Lambda applications.

* [Check if the database and cluster are available] - Once you are inside the EC2 instance, you should be in the /home/ec2-user folder. cd to the mongoshell folder and then run ./connect_to_mongo_shell.sh. This connects the mongosh tool to the Amazon DocumentDB cluster created by the CloudFormation template. Once inside the mongosh, you can issue commands like show dbs to see if the database was created, use <database name> to switch to the created database, and then show collections to see if the collection was created. If you did not modify the defaults in the CloudFormation template, then the name of the database should be DocumentDBPythonLambdaDB and the name of the collection should be DocumentDBPythonLambdaCollection


### Pre-requisites to Deploy the sample Lambda function

* Python 3.12 - On the EC2 machine, Python 3 comes pre-installed with Amazon Linux 2023
* pip - On the EC2 machine, pip3 is installed for package management
* AWS SAM CLI - We have installed the AWS SAM CLI (https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-sam-cli-install.html)

We have also cloned the Github repository for serverless-patterns on the EC2 machine already by running the below command
    ``` 
    git clone https://github.com/aws-samples/serverless-patterns.git
    ```
Change directory to the pattern directory:
    ```
    cd /home/ec2-user/serverless-patterns/documentdb-lambda-python-sam
    ```

### Build the project with SAM CLI

Make sure you are connected to the EC2 instance as mentioned in the "Connect to the EC2 instance" step above

Build your application with the `sam build` command.

```bash
cd /home/ec2-user/serverless-patterns/documentdb-lambda-python-sam/documentdb_streams_consumer_dynamo_sam
sam build
```

The SAM CLI installs dependencies defined in `documentdb_streams_consumer_dynamo_sam/documentdb_streams_event_consumer_function/requirements.txt`, creates a deployment package, and saves it in the `.aws-sam/build` folder.

### Test the build locally

Test a single function by invoking it directly with a test event. An event is a JSON document that represents the input that the function receives from the event source. Test events are included in the `events` folder in this project.

Run functions locally and invoke them with the `sam local invoke` command.

```bash
sam local invoke --event events/event.json
```

### Deploy the sample application


To deploy your application for the first time, run the following in your shell. Make sure the shell variable $AWS_REGION is set. If not, replace $AWS_REGION with the region in which you are deploying the AWS Lambda function:

```bash
cd /home/ec2-user/serverless-patterns/documentdb-lambda-python-sam/documentdb_streams_consumer_dynamo_sam
sam deploy --capabilities CAPABILITY_IAM --no-confirm-changeset --no-disable-rollback --region $AWS_REGION --stack-name documentdb-lambda-python-sam --guided
```

The sam deploy command will package and deploy your application to AWS, with a series of prompts. You can accept all the defaults by hitting Enter:

* **Stack Name**: The name of the stack to deploy to AWS CloudFormation. This should be unique to your account and region, and a good starting point would be something matching your project name.
* **AWS Region**: The AWS region you want to deploy your app to.
* **Parameter StreamsProducerDocumentDBCluster**: The name of the Amazon DocumentDB Cluster that was created by the AWS CloudFormation template
* **Parameter StreamsProducerDocumentDBDatabase**: The name of the Amazon DocumentDB database that will generate streaming events to be consumed by the AWS Lambda function
* **Parameter StreamsProducerDocumentDBCollection**: The name of the Amazon DocumentDB collection that will generate streaming events to be consumed by the AWS Lambda function
* **Parameter SecretsManagerARN**: The ARN of the Amazon Secrets Manager secret that has the username and password to connect to the Amazon DocumentDB cluster
* **Parameter Subnet1**: The first of the three private subnets where the Amazon DocumentDB cluster is deployed
* **Parameter Subnet2**: The second of the three private subnets where the Amazon DocumentDB cluster is deployed
* **Parameter Subnet3**: The third of the three private subnets where the Amazon DocumentDB cluster is deployed
* **Parameter SecurityGroup**: The security group of the AWS Lambda function. This can be the same as the security group of the EC2 machine that was created by the AWS CloudFormation template
* **Confirm changes before deploy**: If set to yes, any change sets will be shown to you before execution for manual review. If set to no, the AWS SAM CLI will automatically deploy application changes.
* **Allow SAM CLI IAM role creation**: Many AWS SAM templates, including this example, create AWS IAM roles required for the AWS Lambda function(s) included to access AWS services. By default, these are scoped down to minimum required permissions. To deploy an AWS CloudFormation stack which creates or modifies IAM roles, the `CAPABILITY_IAM` value for `capabilities` must be provided. If permission isn't provided through this prompt, to deploy this example you must explicitly pass `--capabilities CAPABILITY_IAM` to the `sam deploy` command.
* **Disable rollback**: Defaults to No and it preserves the state of previously provisioned resources when an operation fails
* **Save arguments to configuration file**: If set to yes, your choices will be saved to a configuration file inside the project, so that in the future you can just re-run `sam deploy` without parameters to deploy changes to your application.
* **SAM configuration file [samconfig.toml]**: Name of the configuration file to store configuration information locally
* **SAM configuration environment [default]**: Environment for storing deployment information locally

The message "Successfully created/updated stack - <StackName> in <Region>" indicates a successful deployment.
    
**Note: In case you want to deploy the Lambda function by pointing to an existing DocumentDB Cluster and not the one created by running the CloudFormation template provided in this pattern, you will need to modify the values of the above parameters accordingly**


## Test the application

After deployment, create documents in the Collection to generate stream records.

For your convenience, a Python producer script and a shell script are included on the EC2 instance provisioned by CloudFormation.

You should see a script called commands.sh. Run that script by passing a random string and a number between 1 and 500. Either send at least 10 messages or wait for 300 seconds (check the values of BatchSize: 10 and MaximumBatchingWindowInSeconds: 300 in the template.yaml file)


```
cd /home/ec2-user/serverless-patterns/documentdb-lambda-python-sam/documentdb_streams_message_sender_python

chmod +x commands.sh

$PYTHON3_VERSION -m venv ./myenv && source ./myenv/bin/activate && pip install -r requirements.txt

sh ./commands.sh firstBatch 100

```


The following is sample output:
```
Now going to insert a row in DynamoDB for messageID = firstBatch-06-12-2026-10-30-45-1
Now done inserting a row in DynamoDB for messageID = firstBatch-06-12-2026-10-30-45-1
Now going to insert a row in DynamoDB for messageID = firstBatch-06-12-2026-10-30-45-2
Now done inserting a row in DynamoDB for messageID = firstBatch-06-12-2026-10-30-45-2
Now going to insert a row in DynamoDB for messageID = firstBatch-06-12-2026-10-30-45-3
Now done inserting a row in DynamoDB for messageID = firstBatch-06-12-2026-10-30-45-3
Now going to insert a row in DynamoDB for messageID = firstBatch-06-12-2026-10-30-45-4
Now done inserting a row in DynamoDB for messageID = firstBatch-06-12-2026-10-30-45-4
Now going to insert a row in DynamoDB for messageID = firstBatch-06-12-2026-10-30-45-5
Now done inserting a row in DynamoDB for messageID = firstBatch-06-12-2026-10-30-45-5
Now going to insert a row in DynamoDB for messageID = firstBatch-06-12-2026-10-30-45-6
Now done inserting a row in DynamoDB for messageID = firstBatch-06-12-2026-10-30-45-6
Now going to insert a row in DynamoDB for messageID = firstBatch-06-12-2026-10-30-45-7
Now done inserting a row in DynamoDB for messageID = firstBatch-06-12-2026-10-30-45-7
Now going to insert a row in DynamoDB for messageID = firstBatch-06-12-2026-10-30-45-8
Now done inserting a row in DynamoDB for messageID = firstBatch-06-12-2026-10-30-45-8
Now going to insert a row in DynamoDB for messageID = firstBatch-06-12-2026-10-30-45-9
Now done inserting a row in DynamoDB for messageID = firstBatch-06-12-2026-10-30-45-9
Now going to insert a row in DynamoDB for messageID = firstBatch-06-12-2026-10-30-45-10
Now done inserting a row in DynamoDB for messageID = firstBatch-06-12-2026-10-30-45-10
```

After sending the messages, check Amazon CloudWatch Logs for the AWS Lambda function. The name of the Amazon Cloudwatch Log Group is /aws/lambda/<Name of the AWS Lambda function>.

When you run the above script, it inputs JSON records into the Amazon DocumentDB cluster in the database and collection that were created. This results in the Amazon DocumentDB streams publishing every document. The AWS Lambda function listens on the published Amazon DocumentDB streams messages

The AWS Lambda function parses the Amazon DocumentDB streams messages and outputs the fields to Amazon Cloudwatch logs.

The  function also writes each record into a Amazon DynamoDB table named DocumentDBStreamsConsumerDynamoDBTablePython (if you did not modify the default name in the sam template.yaml file).

You can view the records using the Amazon DynamoDB console, or use the following aws cli command:

```
aws dynamodb scan --table-name DocumentDBStreamsConsumerDynamoDBTablePython --select "COUNT"

```

## Cleanup

First, delete the lambda function stack:
```
cd /home/ec2-user/serverless-patterns/documentdb-lambda-python-sam/documentdb_streams_consumer_dynamo_sam
sam delete

```
Confirm the delete by selecting Y at both prompts.
AWS SAM confirms the stack deletion with the "Deleted successfully" message in the terminal.

Next you need to delete the Amazon CloudFormation template containing the Amazon DocumentDB cluster and the Amazon EC2 instance. Open the Amazon CloudFormation console, select the stack, then choose Delete. The delete will take some time.
