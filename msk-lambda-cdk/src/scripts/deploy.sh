#!/usr/bin/env bash
# export AWS_PROFILE=<REPLACE WITH YOUR AWS PROFILE NAME> or alternatively follow instructions on https://docs.aws.amazon.com/cdk/latest/guide/getting_started.html#getting_started_prerequisites

cd ../ || exit
echo "Deploying VpcStack..."

cdk deploy VpcStack --require-approval never --verbose

# echo "Deploying DynamoDbStack..."
# cdk deploy DynamoDbStack --require-approval never --verbose
echo "Deploying KafkaStack..."
cdk deploy KafkaStack --require-approval never --verbose

kafka_arn=$(aws kafka list-clusters --output text --query 'ClusterInfoList[0].ClusterArn') && echo "$kafka_arn"
kafka_brokers=$(aws kafka get-bootstrap-brokers --cluster-arn $kafka_arn --output text --query '*') && echo "$kafka_brokers"
topicName="transactions"

echo "Deploying KafkaTopicStack"
cdk deploy KafkaTopicStack --parameters KafkaTopicStack:bootstrapAddress="$kafka_brokers" --parameters KafkaTopicStack:topicName="$topicName" --require-approval never

echo "Deploying LambdaStack..."
cdk deploy LambdaStack --parameters LambdaStack:topicName="$topicName" --parameters LambdaStack:kafkaArn="$kafka_arn" --require-approval never --verbose

#to install Maven run:  sudo apt install maven
# echo "Installing Maven project..."
# cd ../consumer || exit
# mvn clean install

# cd ../amazon-msk-java-app-cdk || exit
# echo "Deploying FargateStack..."
# cdk deploy FargateStack --parameters FargateStack:bootstrapAddress="$kafka_brokers" --parameters FargateStack:topicName="$topicName" --require-approval never --verbose

# To trigger lambda function to send message to Kafka queue you can use below command line. Alternatively you can trigger lambda function from AWS console.
# aws lambda invoke --cli-binary-format raw-in-base64-out --function-name TransactionHandler --log-type Tail --payload '{ "accountId": "account_123", "value": 456}' /dev/stdout --query 'LogResult' --output text
#
# To view content of DynamoDB table you can use below line. Alternatively you can view table content in AWS console.
# aws dynamodb scan --table-name Accounts --query "Items[*].[id.S,Balance.N]" --output text
#
#