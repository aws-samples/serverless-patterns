# Python AWS Lambda consumer for Amazon MSK with IAM authentication

This serverless pattern shows how to deploy and run an AWS Lambda function, written in Python, with an Apache Kafka event source that uses AWS Identity and Access Management (IAM) authentication.

The function consumes records from an Amazon Managed Streaming for Apache Kafka (Amazon MSK) cluster using IAM authentication. The cluster is attached to AWS Lambda as a self-managed Apache Kafka event source with the `IAM_AUTH` authentication type, so the event source mapping signs every connection with the function's execution role. No passwords, certificates, or tokens are stored or rotated.

## Architecture

![Architecture diagram](architecture.png)

- An Amazon MSK provisioned cluster in private subnets, with IAM access control on its `:9098` listener.
- An Amazon EC2 client instance with the Kafka tools, the AWS SAM CLI, and this pattern's scripts preinstalled.
- An AWS Lambda function with a self-managed Apache Kafka event source (`IAM_AUTH`) in the VPC. Its execution role holds the `kafka-cluster` permissions for the cluster, topic, and consumer group.
- An Amazon DynamoDB table that receives one item per Kafka record.

Each record the producer sends is delivered to the AWS Lambda function in batches. The function logs every record to Amazon CloudWatch Logs and stores its fields, together with the Kafka topic, partition, and offset, in Amazon DynamoDB.

## Requirements

- An AWS account and an IAM principal with permissions to create the resources in `MSKAndClientEC2.yaml`, including named IAM roles.
- The [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html), if you deploy the template from the command line. Everything else, including the AWS SAM CLI and the Python toolchain, is installed on the Amazon EC2 client instance.

## Files

| File | Description |
|---|---|
| `MSKAndClientEC2.yaml` | AWS CloudFormation template that creates the VPC, the Amazon MSK cluster, the IAM roles, and the Amazon EC2 client instance. |
| `template_original.yaml` | AWS SAM template for the AWS Lambda function, its Apache Kafka event source, and the Amazon DynamoDB table. At boot, the client instance writes `template.yaml` from it with this environment's values. |
| `events/event.json` | Sample Kafka event for `sam local invoke`. |
| `kafka_event_consumer_function/app.py` | AWS Lambda function handler. Decodes each Kafka record and writes its fields to Amazon DynamoDB. |
| `kafka_event_consumer_function/requirements.txt` | Python dependencies of the AWS Lambda function. |
| `kafka_json_apps/producer.py` | Producer that publishes sample JSON records to the topic. |
| `kafka_json_apps/consumer.py` | Consumer that reads the topic, for testing the cluster without AWS Lambda. |
| `kafka_json_apps/kafka_config.py` | Kafka client configuration shared by the producer and consumer. |
| `scripts/deploy_lambda_iam_cli.sh` | Deploys the AWS Lambda function and its event source with the AWS CLI, as an alternative to AWS SAM. |
| `scripts/teardown_lambda_cli.sh` | Deletes the resources that the AWS CLI deploy script created. |
| `scripts/producer_send.sh` | Sends sample JSON records to a topic. |
| `scripts/consumer_receive.sh` | Reads records from a topic. |
| `scripts/admin_create_topic.sh` | Creates the topic and its access rules. The client instance runs it at boot. |
| `scripts/local_dynamodb.sh` | Starts DynamoDB Local for `sam local invoke`. The client instance runs it at boot. |
| `scripts/bad_invalid_credentials.sh`, `scripts/bad_unauthorized_operations.sh` | Negative tests that show the cluster rejecting invalid credentials and unauthorized operations. |
| `MANUAL_EVENT_SOURCE_SETUP.md` | Step-by-step guide to creating the event source mapping by hand in the AWS Management Console or AWS CLI. |
| `architecture.png` | Architecture diagram. |

## Deploy the AWS CloudFormation template

Deploy `MSKAndClientEC2.yaml` from the [AWS CloudFormation console](https://console.aws.amazon.com/cloudformation/) (**Create stack** > **With new resources** > **Upload a template file**, then acknowledge the creation of named IAM resources), or from the AWS CLI on your machine:

```bash
aws cloudformation deploy \
  --template-file MSKAndClientEC2.yaml \
  --stack-name kafka-iam-python \
  --capabilities CAPABILITY_NAMED_IAM
```

The `Python3Version` parameter selects the AWS Lambda runtime (default `python3.13`). To clone a fork or branch of this repository onto the client instance, set `ServerlessLandGithubLocation` and `ServerlessLandGithubBranch`. Pass parameters with `--parameter-overrides`, for example `--parameter-overrides Python3Version=python3.13`.

Creating the Amazon MSK cluster takes 20 to 30 minutes.

## Connect to the Amazon EC2 client instance

When the stack reaches `CREATE_COMPLETE`, open the [Amazon EC2 console](https://console.aws.amazon.com/ec2/), select the instance named **KafkaClientInstance**, choose **Connect**, and connect with **EC2 Instance Connect**.

The client instance has already created the Kafka topic and written `template.yaml` with this stack's values. Your shell loads the environment from `~/kafka_oauth.env`, including `STACK_NAME`, `KAFKA_TOPIC`, and `AWS_REGION`.

## Deploy the AWS Lambda function

Choose one of the following options.

### Option A: AWS SAM

```bash
cd ~/serverless-patterns/kafka-lambda-oauth-python-sam/iam_auth
sam build
sam deploy --guided --stack-name "$STACK_NAME-sam"
```

Accept the default for every prompt. The parameter defaults already contain this environment's broker endpoints, subnets, security group, and secrets.

To test the function locally before you deploy, run `sam local invoke --event ./events/event.json` after `sam build`. The client instance runs DynamoDB Local at boot, and the function writes to it whenever it runs under `sam local`, so a local test never touches the deployed table.

### Option B: AWS CLI script

```bash
cd ~/serverless-patterns/kafka-lambda-oauth-python-sam/iam_auth/scripts
bash ./deploy_lambda_iam_cli.sh
```

## Send messages to the topic

```bash
cd ~/serverless-patterns/kafka-lambda-oauth-python-sam/iam_auth/scripts
sh ./producer_send.sh $KAFKA_TOPIC 10
```

## Verify the AWS Lambda function received the messages

Set `FN` to the name of the function you deployed:

```bash
# Option A (AWS SAM)
FN=$(aws cloudformation describe-stacks --stack-name "$STACK_NAME-sam" \
  --query "Stacks[0].Outputs[?OutputKey=='LambdaKafkaConsumerPythonFunction'].OutputValue" --output text)

# Option B (AWS CLI script)
FN="$STACK_NAME-consumer"
```

Then read the function's logs in Amazon CloudWatch Logs. Each record appears as a `Received this message from Kafka` entry:

```bash
aws logs tail "/aws/lambda/${FN##*:}" --since 15m
```

You can also open the `/aws/lambda/<function-name>` log group in the [Amazon CloudWatch console](https://console.aws.amazon.com/cloudwatch/).

## Verify the records in Amazon DynamoDB

The function writes one item per record to the table `<stack-name>-sam-messages` (Option A) or `<stack-name>-messages` (Option B). After sending 10 messages, the table holds 10 new items:

```bash
aws dynamodb scan --table-name "$STACK_NAME-sam-messages" --select COUNT    # Option A
aws dynamodb scan --table-name "$STACK_NAME-messages" --select COUNT        # Option B
```

To browse the items, open the table in the [Amazon DynamoDB console](https://console.aws.amazon.com/dynamodbv2/) and choose **Explore table items**.

## Cleanup

1. Delete the AWS Lambda function with the tool you deployed it with. Each tool removes only the resources it created.

   - Option A (AWS SAM):

     ```bash
     cd ~/serverless-patterns/kafka-lambda-oauth-python-sam/iam_auth
     sam delete --stack-name "$STACK_NAME-sam"
     ```

   - Option B (AWS CLI script):

     ```bash
     cd ~/serverless-patterns/kafka-lambda-oauth-python-sam/iam_auth/scripts
     bash ./teardown_lambda_cli.sh
     ```

2. Delete the AWS CloudFormation stack from the console or from your machine:

   ```bash
   aws cloudformation delete-stack --stack-name kafka-iam-python
   ```

----
Copyright 2026 Amazon.com, Inc. or its affiliates. All Rights Reserved.

SPDX-License-Identifier: MIT-0
