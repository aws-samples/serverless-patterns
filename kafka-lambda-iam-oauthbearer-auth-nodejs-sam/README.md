# Node.js AWS Lambda consumer for Apache Kafka with OAuth authentication through AWS IAM

This serverless pattern shows how to deploy and run an AWS Lambda function, written in Node.js, with an Apache Kafka event source that uses OAuth authentication with tokens issued by AWS Identity and Access Management (IAM).

The function consumes records from a self-managed Apache Kafka cluster using SASL/OAUTHBEARER authentication with tokens issued by IAM. With IAM outbound identity federation, the event source mapping obtains a signed web identity token for the function's execution role, using the `IAM_OAUTHBEARER_AUTH` authentication type, so no external identity provider or client secret is involved. The brokers validate the token against the account's AWS STS issuer and authorize the role through Kafka ACLs.

## Architecture

![Architecture diagram](architecture.png)

- A three-broker Apache Kafka cluster (KRaft mode) on Amazon EC2 in private subnets, accepting SASL/OAUTHBEARER over TLS and trusting the account's AWS STS token issuer.
- IAM roles for the admin, producer, and consumer clients, and the execution role for the AWS Lambda function. The brokers authorize each role's ARN through Kafka ACLs.
- An AWS Secrets Manager secret holding the brokers' CA certificate.
- An Amazon EC2 client instance with the Kafka tools, the AWS SAM CLI, and this pattern's scripts preinstalled.
- An AWS Lambda function with a self-managed Apache Kafka event source (`IAM_OAUTHBEARER_AUTH`, `OAUTHBEARER_AUDIENCE`, `SERVER_ROOT_CA_CERTIFICATE`) in the VPC.
- An Amazon DynamoDB table that receives one item per Kafka record.

Each record the producer sends is delivered to the AWS Lambda function in batches. The function logs every record to Amazon CloudWatch Logs and stores its fields, together with the Kafka topic, partition, and offset, in Amazon DynamoDB.

Processing is at least once. If any record in a batch fails, for example because a DynamoDB write fails, the event source mapping retries the whole batch rather than skipping it. The table's key is the topic partition plus the offset, so a retried record overwrites its earlier item instead of creating a duplicate.

## Requirements

- An AWS account and an IAM principal with permissions to create the resources in `KafkaBrokersClientEC2.yaml`, including named IAM roles.
- The [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html), if you deploy the template from the command line. Everything else, including the AWS SAM CLI and the Node.js toolchain, is installed on the Amazon EC2 client instance.

## Files

| File | Description |
|---|---|
| `KafkaBrokersClientEC2.yaml` | AWS CloudFormation template that creates the VPC, the Kafka brokers, the IAM roles (including the AWS Lambda execution role), the AWS Secrets Manager secret, and the Amazon EC2 client instance. |
| `template_original.yaml` | AWS SAM template for the AWS Lambda function, its Apache Kafka event source, and the Amazon DynamoDB table. At boot, the client instance writes `template.yaml` from it with this environment's values. |
| `events/event.json` | Sample Kafka event for `sam local invoke`. |
| `kafka_event_consumer_function/app.mjs` | AWS Lambda function handler. Decodes each Kafka record and writes its fields to Amazon DynamoDB. |
| `kafka_event_consumer_function/package.json` | Node.js package definition of the AWS Lambda function. |
| `kafka_json_apps/producer.mjs` | Producer that publishes sample JSON records to the topic. |
| `kafka_json_apps/consumer.mjs` | Consumer that reads the topic, for testing the cluster without AWS Lambda. |
| `kafka_json_apps/kafkaConfig.mjs` | Kafka client configuration shared by the producer and consumer. |
| `scripts/deploy_lambda_oauth_cli.sh` | Deploys the AWS Lambda function and its event source with the AWS CLI, as an alternative to AWS SAM. |
| `scripts/teardown_lambda_cli.sh` | Deletes the resources that the AWS CLI deploy script created. |
| `scripts/producer_send.sh` | Sends sample JSON records to a topic. |
| `scripts/consumer_receive.sh` | Reads records from a topic. |
| `scripts/admin_create_topic.sh` | Creates the topic and its access rules. The client instance runs it at boot. |
| `scripts/local_dynamodb.sh` | Starts DynamoDB Local for `sam local invoke`. The client instance runs it at boot. |
| `scripts/bad_invalid_credentials.sh`, `scripts/bad_unauthorized_operations.sh` | Negative tests that show the cluster rejecting invalid credentials and unauthorized operations. |
| `architecture.png` | Architecture diagram. |

## Deploy the AWS CloudFormation template

Deploy `KafkaBrokersClientEC2.yaml` from the [AWS CloudFormation console](https://console.aws.amazon.com/cloudformation/) (**Create stack** > **With new resources** > **Upload a template file**, then acknowledge the creation of named IAM resources), or from the AWS CLI on your machine:

```bash
aws cloudformation deploy \
  --template-file KafkaBrokersClientEC2.yaml \
  --stack-name kafka-iam-oauth-nodejs \
  --capabilities CAPABILITY_NAMED_IAM \
  --s3-bucket <amzn-s3-bucket-in-the-same-region>
```

The `NodeVersion` parameter selects the AWS Lambda runtime (default `nodejs22.x`). To clone a fork or branch of this repository onto the client instance, set `ServerlessLandGithubLocation` and `ServerlessLandGithubBranch`. Pass parameters with `--parameter-overrides`, for example `--parameter-overrides NodeVersion=nodejs22.x`.

`KafkaBrokersClientEC2.yaml` is larger than the 51,200-byte limit for inline templates, so the AWS CLI uploads it to the Amazon S3 bucket you name in `--s3-bucket`. The AWS CloudFormation console handles this for you.

> **Note:** IAM outbound identity federation must be enabled in the account. If you leave the `OutboundIssuerUrl` parameter empty, the brokers enable it at boot with `aws iam enable-outbound-web-identity-federation`, an account-wide setting that lets IAM principals request web identity tokens subject to their own permissions.

The stack reaches `CREATE_COMPLETE` only after the brokers and the client instance have finished setting up.

## Connect to the Amazon EC2 client instance

When the stack reaches `CREATE_COMPLETE`, open the [Amazon EC2 console](https://console.aws.amazon.com/ec2/), select the instance named **KafkaClientInstance**, choose **Connect**, and connect with **EC2 Instance Connect**.

The client instance has already created the Kafka topic and written `template.yaml` with this stack's values. Your shell loads the environment from `~/kafka_oauth.env`, including `STACK_NAME`, `KAFKA_TOPIC`, and `AWS_REGION`.

## Deploy the AWS Lambda function

Choose one of the following options.

### Option A: AWS SAM

```bash
cd ~/serverless-patterns/kafka-lambda-iam-oauthbearer-auth-nodejs-sam
sam build
sam deploy --guided --stack-name "$STACK_NAME-sam"
```

Accept the default for every prompt. The parameter defaults already contain this environment's broker endpoints, subnets, security group, and secrets.

To test the function locally before you deploy, run `sam local invoke --event ./events/event.json` after `sam build`. The client instance runs DynamoDB Local at boot, and the function writes to it whenever it runs under `sam local`, so a local test never touches the deployed table.

### Option B: AWS CLI script

```bash
cd ~/serverless-patterns/kafka-lambda-iam-oauthbearer-auth-nodejs-sam/scripts
bash ./deploy_lambda_oauth_cli.sh
```

## Send messages to the topic

```bash
cd ~/serverless-patterns/kafka-lambda-iam-oauthbearer-auth-nodejs-sam/scripts
sh ./producer_send.sh $KAFKA_TOPIC 10
```

## Verify the AWS Lambda function received the messages

Each record appears in the function's Amazon CloudWatch Logs as a `Received this message from Kafka` entry with its topic, partition, and offset. Set `LOG_GROUP` for the option you deployed, then read the logs:

```bash
# Option A (AWS SAM): the template's log group, which keeps logs for 7 days
LOG_GROUP=$(aws cloudformation describe-stacks --stack-name "$STACK_NAME-sam" \
  --query "Stacks[0].Outputs[?OutputKey=='ConsumerLogGroupName'].OutputValue" --output text)

# Option B (AWS CLI script): the script also sets 7-day retention
LOG_GROUP="/aws/lambda/$STACK_NAME-consumer"

aws logs tail "$LOG_GROUP" --since 15m
```

You can also open the log group in the [Amazon CloudWatch console](https://console.aws.amazon.com/cloudwatch/).

## Verify the records in Amazon DynamoDB

The function writes one item per record to the table `<stack-name>-sam-messages` (Option A) or `<stack-name>-messages` (Option B). After sending 10 messages, the table holds 10 new items:

```bash
aws dynamodb scan --table-name "$STACK_NAME-sam-messages" --select COUNT    # Option A
aws dynamodb scan --table-name "$STACK_NAME-messages" --select COUNT        # Option B
```

To browse the items, open the table in the [Amazon DynamoDB console](https://console.aws.amazon.com/dynamodbv2/) and choose **Explore table items**.

## Run the negative tests

The scripts in `scripts/` also show the cluster turning away clients that shouldn't get in:

```bash
cd ~/serverless-patterns/kafka-lambda-iam-oauthbearer-auth-nodejs-sam/scripts
bash ./bad_invalid_credentials.sh
bash ./bad_unauthorized_operations.sh $KAFKA_TOPIC
```

`bad_invalid_credentials.sh` presents a forged web identity token, and the brokers reject it with a SASL/OAUTHBEARER authentication failure. `bad_unauthorized_operations.sh` uses valid tokens for the producer and consumer roles on operations their Kafka ACLs don't allow, such as the producer creating a topic or the consumer writing to one, and each attempt fails with `TopicAuthorizationException`. Each script prints an `>> expected:` line before every attempt, so you can compare the actual error with it.

## Cleanup

These resources bill continuously until you delete the stacks: the three Kafka broker instances, the Amazon EC2 client instance, the NAT gateway, and the event source mapping's provisioned poller, which this sample runs in provisioned mode and which is charged for its minimum pollers whether or not messages arrive.

1. Delete the AWS Lambda function with the tool you deployed it with. Each tool removes only the resources it created.

   - Option A (AWS SAM):

     ```bash
     cd ~/serverless-patterns/kafka-lambda-iam-oauthbearer-auth-nodejs-sam
     sam delete --stack-name "$STACK_NAME-sam"
     ```

   - Option B (AWS CLI script):

     ```bash
     cd ~/serverless-patterns/kafka-lambda-iam-oauthbearer-auth-nodejs-sam/scripts
     bash ./teardown_lambda_cli.sh
     ```

2. Delete the AWS CloudFormation stack from the console or from your machine:

   ```bash
   aws cloudformation delete-stack --stack-name kafka-iam-oauth-nodejs
   ```

3. Optionally, delete the Amazon S3 bucket the brokers use to cache the Kafka download and the broker certificate. It is created outside the stack and reused across deployments:

   ```bash
   aws s3 rb "s3://kafka-oauth-cache-$(aws sts get-caller-identity --query Account --output text)-<region>" --force
   ```

----
Copyright 2026 Amazon.com, Inc. or its affiliates. All Rights Reserved.

SPDX-License-Identifier: MIT-0
