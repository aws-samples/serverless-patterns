# AWS Lambda function subscribed to an Amazon MSK Kafka topic with Avro and Schema Registry (Python)

This pattern demonstrates Lambda functions that:
1. Consume messages from an Amazon Managed Streaming for Kafka (Amazon MSK) topic
2. Produce Avro-formatted messages to an Amazon MSK topic using Schema Registry

Both functions use IAM authentication to connect to the MSK Cluster and use AWS Glue Schema Registry for Avro schema management.

This project contains source code and supporting files for a serverless application that you can deploy with the SAM CLI. It includes the following files and folders:

- `kafka_event_consumer_function` - Code for the consumer Lambda function.
- `kafka_event_producer_function` - Code for the Avro producer Lambda function.
- `events` - Invocation events that you can use to invoke the functions.
- `schemas` - Avro schema definitions.
- `kafka_event_consumer_function/tests` - Unit tests for the consumer code.
- `template.yaml` - A template that defines the application's Lambda functions.
- `MSKAndKafkaClientEC2.yaml` - A CloudFormation template file that can be used to deploy an MSK cluster and also deploy an EC2 machine with all pre-requisites already installed, so you can directly build and deploy the lambda functions and test them out.
- `requirements.txt` - Python dependencies for the entire project.
- `deploy.sh` - Automated deployment script that detects MSK CloudFormation stack and deploys Lambda functions.

> [!Important] 
> This application uses various AWS services and there are costs associated with these services after the Free Tier usage - please see the [AWS Pricing page](https://aws.amazon.com/pricing/) for details. You are responsible for any AWS costs incurred.

## Requirements

* [Create an AWS account](https://portal.aws.amazon.com/gp/aws/developer/registration/index.html) if you do not already have one and log in. The IAM user that you use must have sufficient permissions to make necessary AWS service calls and manage AWS resources.
* [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html) installed and configured
* [Git Installed](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)
* [AWS Serverless Application Model](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-sam-cli-install.html) (AWS SAM) installed

## Deployment Options

You have two options to deploy and test this pattern:

### Option A: Using EC2 Instance (Recommended for Testing)
- **Best for**: Quick testing and evaluation
- **Includes**: Pre-configured MSK cluster, EC2 instance with all tools installed
- **Setup time**: ~15-20 minutes

### Option B: Local Development Environment
- **Best for**: Development and customization
- **Requires**: Local setup of Python, SAM CLI, Docker
- **Setup time**: ~10-15 minutes

---

## Option A: EC2 Instance Setup

### Step 1: Deploy MSK Cluster and EC2 Instance

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

### Step 2: Connect to EC2 Instance

1. **Connect to the EC2 instance**:
   - Go to the EC2 console
   - Find your instance and click "Connect"
   - Use **EC2 Instance Connect** or **EC2 Instance Connect Endpoint**

### Step 3: Navigate and Deploy

```bash
# Change to the pattern directory
cd serverless-patterns/msk-lambda-schema-avro-python-sam

# Deploy using the automated script
./deploy.sh
```

The deploy script will automatically detect your MSK CloudFormation stack and configure all parameters.

---

## Option B: Local Development Setup

### Step 1: Clone and Navigate

```bash
# Clone the serverless patterns repository
git clone https://github.com/aws-samples/serverless-patterns.git
cd serverless-patterns/msk-lambda-schema-avro-python-sam
```

### Step 2: Deploy

#### Automated Deployment (If using MSKAndKafkaClientEC2 stack)

```bash
# Run the automated deployment script
./deploy.sh
```

#### Manual Deployment

```bash
# Build the application
sam build

# Deploy with guided prompts
sam deploy --capabilities CAPABILITY_IAM --guided
```

During deployment, you'll be prompted for:
* **Stack Name**: `msk-lambda-schema-avro-python-sam`
* **AWS Region**: Your current region
* **Parameter MSKClusterName**: The name of the MSK Cluster
* **Parameter MSKClusterId**: The unique ID of the MSK Cluster
* **Parameter MSKTopic**: The Kafka topic name
* **Parameter ContactSchemaName**: The name of the schema (default: ContactSchema)
* **Parameter VpcId**: The VPC ID
* **Parameter SubnetIds**: Comma-separated subnet IDs
* **Parameter SecurityGroupIds**: Security group IDs

---

## Testing the Application

### Invoke the Producer Function

```bash
sam remote invoke LambdaMSKProducerPythonFunction --region <YOUR_REGION> --stack-name msk-lambda-schema-avro-python-sam
```

### Verify Consumer Processing

```bash
# View consumer function logs
sam logs --name LambdaMSKConsumerPythonFunction --stack-name msk-lambda-schema-avro-python-sam --region <YOUR_REGION>
```

### Expected Behavior

- **Producer**: Generates messages with zip codes starting with both "1000" and "2000"
- **Consumer**: Only processes messages with zip codes starting with "2000" (filtered by event source mapping)
- **Schema Registry**: Handles Avro serialization/deserialization automatically

---

## How it works

The producer Lambda function generates sample contact data and publishes it to the MSK topic using Avro serialization with AWS Glue Schema Registry. The consumer Lambda function is triggered by messages from the MSK topic and processes only messages with zip codes starting with "2000" due to event source mapping filters.

This demonstrates how event source mapping filters can be used to efficiently process only messages that match specific criteria, reducing Lambda invocation costs and processing overhead.

---

## Cleanup

Delete the Lambda stack:

```bash
sam delete --stack-name msk-lambda-schema-avro-python-sam
```

If you deployed the MSK cluster using the CloudFormation template, delete that stack from the AWS Console.

---

## Additional Resources

- [AWS Lambda Developer Guide](https://docs.aws.amazon.com/lambda/latest/dg/)
- [Amazon MSK Developer Guide](https://docs.aws.amazon.com/msk/latest/developerguide/)
- [AWS Glue Schema Registry](https://docs.aws.amazon.com/glue/latest/dg/schema-registry.html)
- [AWS Lambda Powertools Python](https://awslabs.github.io/aws-lambda-powertools-python/)
- [AWS SAM Developer Guide](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/)

----

Copyright 2021 Amazon.com, Inc. or its affiliates. All Rights Reserved.

SPDX-License-Identifier: MIT-0
