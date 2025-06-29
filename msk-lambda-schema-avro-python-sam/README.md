# AWS Lambda function subscribed to an Amazon MSK Kafka topic with Avro and Schema Registry (Python)

This pattern is an example of Lambda functions that:
1. Consume messages from an Amazon Managed Streaming for Kafka (Amazon MSK) topic
2. Produce Avro-formatted messages to an Amazon MSK topic using Schema Registry

Both functions use IAM authentication to connect to the MSK Cluster and use AWS Glue Schema Registry for Avro schema management.

This project contains source code and supporting files for a serverless application that you can deploy with the SAM CLI. It includes the following files and folders.

- `kafka_event_consumer_function` - Code for the consumer Lambda function.
- `kafka_event_producer_function` - Code for the Avro producer Lambda function.
- `events` - Invocation events that you can use to invoke the functions.
- `schemas` - Avro schema definitions.
- `kafka_event_consumer_function/tests` - Unit tests for the consumer code.
- `venv/` - Python virtual environment (created after setup).
- `template.yaml` - A template that defines the application's Lambda functions.
- `template_original.yaml` - The original template with placeholders that get replaced during deployment.
- `MSKAndKafkaClientEC2.yaml` - A CloudFormation template file that can be used to deploy an MSK cluster and also deploy an EC2 machine with all pre-requisites already installed, so you can directly build and deploy the lambda functions and test them out.
- `requirements.txt` - Python dependencies for the entire project.
- `setup_venv.sh` - Script to set up the Python virtual environment.

> [!Important] 
> This application uses various AWS services and there are costs associated with these services after the Free Tier usage - please see the [AWS Pricing page](https://aws.amazon.com/pricing/) for details. You are responsible for any AWS costs incurred.

## Requirements

* [Create an AWS account](https://portal.aws.amazon.com/gp/aws/developer/registration/index.html) if you do not already have one and log in. The IAM user that you use must have sufficient permissions to make necessary AWS service calls and manage AWS resources.

## Python Environment Setup

This project requires Python 3.9 or later. Before deploying, you need to set up a Python virtual environment.

### Automatic Setup

Run the setup script to automatically create and configure the virtual environment:

```bash
./setup_venv.sh
```

This script will:
1. Check your Python version (requires 3.9+)
2. Create a virtual environment in the `venv/` directory
3. Install all required dependencies from `requirements.txt`

### Manual Setup

If you prefer to set up the environment manually:

```bash
# Create virtual environment
python3 -m venv venv

# Activate virtual environment
source venv/bin/activate

# Upgrade pip
pip install --upgrade pip

# Install dependencies
pip install -r requirements.txt
```

### Activating the Virtual Environment

Before working with the project, always activate the virtual environment:

```bash
source venv/bin/activate
```

To deactivate when you're done:

```bash
deactivate
```

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
You should see an output such as *Created topic <your-topic-name>.* where the topic name corresponds to what you specified when deploying the CloudFormation stack.

If you are not able to find the file `kafka_topic_creator_output.txt` or if it is blank or you see an error message, then you need to run the file:

```bash
./kafka_topic_creator.sh
```

This file runs a script that creates the Kafka topic that the Lambda function will subscribe to.

## Pre-requisites to Deploy the sample Lambda function

The EC2 machine that was created by running the CloudFormation template has all the software needed to deploy the Lambda functions.

* **[AWS Serverless Application Model](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-sam-cli-install.html) (AWS SAM) CLI**  is a serverless tool for building and testing Lambda applications. It uses Docker to locally test your functions in an Amazon Linux environment that resembles the Lambda execution environment. It can also emulate your application's build environment and API.

* **Python** - Python 3.9 or later is supported by AWS SAM

* **[Docker](https://hub.docker.com/search/?type=edition&offering=community)** - Installed the Docker Community Edition

* The **[serverless-patterns](https://github.com/aws-samples/serverless-patterns) GitHub repository** is cloned on the EC2 machine.

Change directory to the pattern directory:

```bash
cd serverless-patterns/msk-lambda-schema-avro-python-sam
```

## Local Development Setup

If you're developing locally (not on the EC2 instance), follow these steps:

1. **Set up Python virtual environment:**
   ```bash
   ./setup_venv.sh
   ```

2. **Activate the virtual environment:**
   ```bash
   source venv/bin/activate
   ```

3. **Verify installation:**
   ```bash
   python -c "import boto3, kafka, avro; print('All dependencies installed successfully')"
   ```

## Build the application

Make sure your virtual environment is activated, then build your application with the `sam build` command.

```bash
# Activate virtual environment if not already active
source venv/bin/activate

# Build the application
sam build
```

SAM CLI installs dependencies defined in `kafka_event_consumer_function/requirements.txt` and `kafka_event_producer_function/requirements.txt`, creates a deployment package, and saves it in the `.aws-sam/build` folder.

## Deploy the sample application

### Automated Deployment

Use the provided deployment script for automatic parameter detection and deployment:

```bash
# Make sure virtual environment is activated
source venv/bin/activate

# Run the deployment script
./deploy.sh
```

### Manual Deployment

To deploy your application manually for the first time, run the following:

```bash
# Make sure virtual environment is activated
source venv/bin/activate

sam deploy --capabilities CAPABILITY_IAM --no-confirm-changeset --no-disable-rollback --region $AWS_REGION --stack-name msk-lambda-schema-avro-python-sam --guided
```

The `sam deploy` command packages and deploys your application to AWS, with a series of prompts. 

> [!NOTE]
> The deployment script retrieves the required parameters from the CloudFormation outputs in the AWS Console after deploying the `MSKAndKafkaClientEC2.yaml` template. These outputs contain all the necessary information for deploying the Lambda functions. If you connect to a different Kafka cluster, enter the values manually.

* **Stack Name**: The name of the stack to deploy to CloudFormation. This should be unique to your account and region, and a good starting point would be something matching your project name.
* **AWS Region**: The AWS region you want to deploy your app to.
* **Parameter MSKClusterName**: The name of the MSK Cluster. This will be `<stack-name>-cluster` from the CloudFormation template you deployed in the previous step.
* **Parameter MSKClusterId**: The unique ID of the MSK Cluster. This can be found in the MSK console or extracted from the MSK ARN in the CloudFormation outputs.
* **Parameter MSKTopic**: The Kafka topic on which the Lambda functions will produce and consume messages. You can find this in the CloudFormation outputs as `KafkaTopicForLambda`
* **Parameter ContactSchemaName**: The name of the schema to be used for the Avro serialization (default: ContactSchema).
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

Once the Lambda functions are deployed, you can test the application by invoking the producer Lambda function, which generates Avro-formatted messages to the MSK topic. The consumer Lambda function automatically processes these messages.

### Invoke the producer Lambda function

You can invoke the producer Lambda function using AWS SAM CLI with the following command:

```bash
# Make sure virtual environment is activated
source venv/bin/activate

sam remote invoke LambdaMSKProducerPythonFunction --region $AWS_REGION --stack-name msk-lambda-schema-avro-python-sam
```
After invoking the producer function, the CloudWatch logs are displayed.

Look for entries showing:
   - Confirmation that the message was sent to the MSK topic
   - Successful serialization of the message using AVRO format
   - Successful registration or retrieval of the schema from Schema Registry
   - Look for the *ZIP CODE DISTRIBUTION SUMMARY* section, which shows how many messages were generated with zip codes starting with *1000* and how many with *2000*.
   - You should see that the producer generated a mix of both zip code types   

You can also invoke the function using the AWS Console, or AWS CLI.

### Verify the processing results from the consumer Lambda function

View the consumer Lambda function logs using the Amazon CloudWatch logs console or CLI within the EC2 instance:
```bash
sam logs --name LambdaMSKConsumerPythonFunction --stack-name msk-lambda-schema-avro-python-sam --region $AWS_REGION
```
In the consumer logs, look for entries showing:
   - Receipt of the message batch from the MSK topic
   - Successful deserialization of the Avro message
   - The decoded message content and any processing performed on it
   - You should see that the consumer only processed messages with zip codes starting with *2000*
   - Messages with zip codes starting with *1000* are filtered out by the event source mapping and never reached the Lambda function

The consumer Lambda function automatically processes messages from the MSK topic. It parses the Kafka messages and outputs the fields in the Kafka messages to CloudWatch logs.

Each key has a list of messages. Each Kafka message has the following properties *Topic, Partition, Offset, TimeStamp, TimeStampType, Key and Value*

The *Key* and *Value* are base64 encoded and have to be decoded. [AWS Lambda Powertools for Python](https://docs.powertools.aws.dev/lambda/python/latest/) automatically decodes the base64 values. A message can also have a list of headers, each header having a key and a value.

The code in this example prints out the fields in the Kafka message and also decrypts the key and the value and logs them in CloudWatch logs.

This demonstrates how event source mapping filters can be used to efficiently process only the messages that match specific criteria, reducing Lambda invocation costs and processing overhead.

## Running Tests

To run the unit tests for the consumer function:

```bash
# Make sure virtual environment is activated
source venv/bin/activate

# Run tests for consumer function
cd kafka_event_consumer_function
python -m pytest tests/ -v

# Return to project root
cd ..
```

## Development Workflow

When developing locally:

1. **Always activate the virtual environment first:**
   ```bash
   source venv/bin/activate
   ```

2. **Install new dependencies:**
   ```bash
   pip install <new-package>
   pip freeze > requirements.txt  # Update requirements.txt
   ```

3. **Test your changes:**
   ```bash
   # Run unit tests
   cd kafka_event_consumer_function && python -m pytest tests/ -v && cd ..
   
   # Build and test locally
   sam build
   sam local invoke LambdaMSKProducerPythonFunction --event events/event.json
   ```

4. **Deploy changes:**
   ```bash
   sam build
   sam deploy
   ```

## Troubleshooting

### Import Errors
If you encounter import errors:
1. Make sure the virtual environment is activated: `source venv/bin/activate`
2. Verify all dependencies are installed: `pip install -r requirements.txt`
3. Check Python version: `python --version` (should be 3.9+)

### Virtual Environment Issues
If the virtual environment setup fails:
1. Check Python version: `python3 --version`
2. Install Python 3.9+ if needed
3. Try manual setup as described above

### SAM Build Issues
If `sam build` fails:
1. Make sure Docker is running
2. Verify virtual environment is activated
3. Check that all requirements.txt files have compatible versions

## Cleanup

### Delete Lambda  stack
First delete the Lambda functions by running the `sam delete` command

```bash
# Make sure virtual environment is activated
source venv/bin/activate

# Use the cleanup script
./cleanup.sh

# Or manually delete
sam delete --stack-name msk-lambda-schema-avro-python-sam
```

Confirm by pressing `y` for both the questions
The Lambda function are deleted and the tool displays a final confirmation *Deleted successfully* on the command-line

### Delete Amazon MSK cluster
To delete the CloudFormation template that created the Amazon MSK Server and the EC2 machine
1. Navigate to the CloudFormation console and select the stack. 
2. Select the *Delete* button. The deletion process run for some time. Once complete the stack should be removed. 

If you get an error message that says the stack could not be deleted, please retry again and do a *Force Delete*. The reason this may happen is because ENIs created by the deployed Lambda function in your VPC may prevent the VPC from being deleted even after deleting the Lambda function.

### Clean up Virtual Environment
To remove the virtual environment:

```bash
# Deactivate if currently active
deactivate

# Remove the virtual environment directory
rm -rf venv/
```
