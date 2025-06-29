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

## Prerequisites

* [Create an AWS account](https://portal.aws.amazon.com/gp/aws/developer/registration/index.html) if you do not already have one and log in. The IAM user that you use must have sufficient permissions to make necessary AWS service calls and manage AWS resources.

## Deployment Options

You have two options to deploy and test this pattern:

### Option A: Using EC2 Instance (Recommended for Testing)
- **Best for**: Quick testing and evaluation
- **Includes**: Pre-configured MSK cluster, EC2 instance with all tools installed
- **Setup time**: ~15-20 minutes
- **Go to**: [EC2 Instance Setup](#option-a-ec2-instance-setup)

### Option B: Local Development Environment
- **Best for**: Development and customization
- **Requires**: Local setup of Python, SAM CLI, Docker
- **Setup time**: ~10-15 minutes
- **Go to**: [Local Development Setup](#option-b-local-development-setup)

---

# Option A: EC2 Instance Setup

This option deploys everything you need including an MSK cluster and a pre-configured EC2 instance.

## Step 1: Deploy MSK Cluster and EC2 Instance

1. **Deploy the CloudFormation template**:
   - Browse to the Amazon CloudFormation console
   - Create a new stack using the file `MSKAndKafkaClientEC2.yaml`
   - Keep the defaults for input parameters or modify them as necessary
   - Wait for the CloudFormation stack to be created (~15-20 minutes)

2. **What gets created**:
   - MSK cluster (Provisioned or Serverless based on your selection)
   - EC2 instance with all pre-requisites installed
   - VPC, subnets, and security groups
   - Kafka topic for Lambda functions

## Step 2: Connect to EC2 Instance

1. **Connect to the EC2 instance**:
   - Go to the EC2 console
   - Find your instance and click "Connect"
   - Use **EC2 Instance Connect** or **EC2 Instance Connect Endpoint**

> [!NOTE]  
> You may need to wait for some time after the CloudFormation stack is created, as some UserData scripts continue running after the CloudFormation stack shows *Created*.

## Step 3: Verify Kafka Topic Creation

Once connected to the EC2 instance:

```bash
# Check if Kafka topic was created successfully
cat kafka_topic_creator_output.txt
```

You should see an output such as *Created topic <your-topic-name>.* where the topic name corresponds to what you specified when deploying the CloudFormation stack.

If the file is missing or shows an error:

```bash
# Manually create the Kafka topic
./kafka_topic_creator.sh
```

## Step 4: Navigate to Project Directory

```bash
# Change to the pattern directory
cd serverless-patterns/msk-lambda-schema-avro-python-sam
```

## Step 5: Build and Deploy Lambda Functions

The EC2 instance has all required tools pre-installed:
- AWS SAM CLI
- Python 3.9+
- Docker
- All project dependencies

```bash
# Build the application
sam build

# Deploy the application (guided mode for first time)
sam deploy --capabilities CAPABILITY_IAM --no-confirm-changeset --no-disable-rollback --region $AWS_REGION --stack-name msk-lambda-schema-avro-python-sam --guided
```

### Deployment Parameters

During deployment, you'll be prompted for these parameters (most will be auto-filled from CloudFormation outputs):

* **Stack Name**: `msk-lambda-schema-avro-python-sam`
* **AWS Region**: Your current region
* **Parameter MSKClusterName**: The name of the MSK Cluster (from CloudFormation)
* **Parameter MSKClusterId**: The unique ID of the MSK Cluster (from CloudFormation)
* **Parameter MSKTopic**: The Kafka topic name (from CloudFormation outputs as `KafkaTopicForLambda`)
* **Parameter ContactSchemaName**: The name of the schema (default: ContactSchema)
* **Parameter VpcId**: The VPC ID (from CloudFormation outputs as `VPCId`)
* **Parameter SubnetIds**: Comma-separated subnet IDs (from CloudFormation outputs)
* **Parameter SecurityGroupIds**: Security group IDs (from CloudFormation outputs as `SecurityGroupId`)

## Step 6: Test the Application

```bash
# Test the producer function
sam remote invoke LambdaMSKProducerPythonFunction --region $AWS_REGION --stack-name msk-lambda-schema-avro-python-sam

# View consumer logs
sam logs --name LambdaMSKConsumerPythonFunction --stack-name msk-lambda-schema-avro-python-sam --region $AWS_REGION
```

---

# Option B: Local Development Setup

This option is for developers who want to work locally and connect to an existing MSK cluster.

## Step 1: Prerequisites

Ensure you have the following installed locally:

* **[AWS Serverless Application Model](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-sam-cli-install.html) (AWS SAM) CLI**
* **Python 3.9 or later**
* **[Docker](https://hub.docker.com/search/?type=edition&offering=community)** - Docker Community Edition
* **AWS CLI** configured with appropriate credentials

## Step 2: Clone the Repository

```bash
# Clone the serverless patterns repository
git clone https://github.com/aws-samples/serverless-patterns.git
cd serverless-patterns/msk-lambda-schema-avro-python-sam
```

## Step 3: Set Up Python Environment

### Automatic Setup (Recommended)

```bash
# Run the setup script
./setup_venv.sh
```

This script will:
1. Check your Python version (requires 3.9+)
2. Create a virtual environment in the `venv/` directory
3. Install all required dependencies from `requirements.txt`

### Manual Setup

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

## Step 4: Activate Virtual Environment

**Important**: Always activate the virtual environment before working with the project:

```bash
source venv/bin/activate
```

To deactivate when you're done:

```bash
deactivate
```

## Step 5: Verify Installation

```bash
# Test that all dependencies are installed
python -c "import boto3, kafka, avro; print('All dependencies installed successfully')"
```

## Step 6: Configure for Your MSK Cluster

You'll need an existing MSK cluster. Update the deployment parameters to match your environment:

- MSK Cluster Name and ID
- VPC ID and Subnet IDs
- Security Group IDs
- Kafka Topic Name

## Step 7: Build and Deploy

```bash
# Make sure virtual environment is activated
source venv/bin/activate

# Build the application
sam build

# Deploy with your parameters
sam deploy --capabilities CAPABILITY_IAM --no-confirm-changeset --no-disable-rollback --region <YOUR_REGION> --stack-name msk-lambda-schema-avro-python-sam --guided
```

---

# Testing the Application

Once deployed (using either option), test the application:

## Invoke the Producer Function

```bash
# Make sure you're in the project directory
# For EC2: already in the right directory
# For local: cd to your project directory

sam remote invoke LambdaMSKProducerPythonFunction --region <YOUR_REGION> --stack-name msk-lambda-schema-avro-python-sam
```

### Expected Producer Output

Look for entries showing:
- Confirmation that the message was sent to the MSK topic
- Successful serialization of the message using AVRO format
- Successful registration or retrieval of the schema from Schema Registry
- ZIP CODE DISTRIBUTION SUMMARY showing messages with zip codes starting with *1000* and *2000*
- The producer should generate a mix of both zip code types

## Verify Consumer Processing

```bash
# View consumer function logs
sam logs --name LambdaMSKConsumerPythonFunction --stack-name msk-lambda-schema-avro-python-sam --region <YOUR_REGION>
```

### Expected Consumer Output

In the consumer logs, look for:
- Receipt of the message batch from the MSK topic
- Successful deserialization of the Avro message
- The decoded message content and processing
- **Important**: Consumer only processes messages with zip codes starting with *2000*
- Messages with zip codes starting with *1000* are filtered out by the event source mapping

### How Event Filtering Works

The consumer Lambda function automatically processes messages from the MSK topic. Each Kafka message has properties: *Topic, Partition, Offset, TimeStamp, TimeStampType, Key and Value*

The *Key* and *Value* are base64 encoded and automatically decoded by [AWS Lambda Powertools for Python](https://docs.powertools.aws.dev/lambda/python/latest/).

This demonstrates how event source mapping filters can be used to efficiently process only messages that match specific criteria, reducing Lambda invocation costs and processing overhead.

---

# Development Workflow (Local Development Only)

When developing locally:

## Daily Development

```bash
# 1. Always activate virtual environment first
source venv/bin/activate

# 2. Make your code changes

# 3. Run unit tests
cd kafka_event_consumer_function
python -m pytest tests/ -v
cd ..

# 4. Build and test locally
sam build
sam local invoke LambdaMSKProducerPythonFunction --event events/event.json

# 5. Deploy changes
sam deploy
```

## Adding Dependencies

```bash
# Activate virtual environment
source venv/bin/activate

# Install new package
pip install <new-package>

# Update requirements file
pip freeze > requirements.txt
```

---

# Troubleshooting

## Common Issues

### Import Errors
```bash
# Make sure virtual environment is activated
source venv/bin/activate

# Reinstall dependencies
pip install -r requirements.txt

# Check Python version
python --version  # Should be 3.9+
```

### Virtual Environment Issues
```bash
# Check Python version
python3 --version

# Remove and recreate virtual environment
rm -rf venv/
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### SAM Build Issues
```bash
# Make sure Docker is running
docker --version

# For EC2 instances, Docker should already be running
# For local development, start Docker Desktop

# Clean build
sam build --use-container
```

### EC2 Instance Issues
```bash
# If Kafka topic creation failed
./kafka_topic_creator.sh

# Check if all services are running
sudo systemctl status docker

# Verify AWS CLI configuration
aws sts get-caller-identity
```

---

# Cleanup

## Delete Lambda Stack

```bash
# Option 1: Use cleanup script (if available)
./cleanup.sh

# Option 2: Manual deletion
sam delete --stack-name msk-lambda-schema-avro-python-sam
```

Confirm by pressing `y` for both questions.

## Delete MSK Cluster (EC2 Option Only)

1. Navigate to the CloudFormation console
2. Select the MSK stack
3. Click "Delete"
4. If deletion fails, use "Force Delete" option

> [!NOTE]
> ENIs created by Lambda functions in your VPC may prevent VPC deletion. If this happens, wait a few minutes and retry, or use Force Delete.

## Clean Up Local Environment

```bash
# Deactivate virtual environment
deactivate

# Remove virtual environment (optional)
rm -rf venv/
```

---

# Additional Resources

- [AWS Lambda Developer Guide](https://docs.aws.amazon.com/lambda/latest/dg/)
- [Amazon MSK Developer Guide](https://docs.aws.amazon.com/msk/latest/developerguide/)
- [AWS Glue Schema Registry](https://docs.aws.amazon.com/glue/latest/dg/schema-registry.html)
- [AWS Lambda Powertools Python](https://awslabs.github.io/aws-lambda-powertools-python/)
- [AWS SAM Developer Guide](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/)
