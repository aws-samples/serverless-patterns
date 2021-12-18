#!/usr/bin/env bash
# export AWS_PROFILE=<REPLACE WITH YOUR AWS PROFILE NAME> or alternatively follow instructions on https://docs.aws.amazon.com/cdk/latest/guide/getting_started.html#getting_started_prerequisites

cd ../ || exit

echo "Destroying KafkaStack..."
cdk destroy KafkaStack --force --verbose

echo "Destroying KafkaTopicStack"
cdk destroy KafkaTopicStack --force --verbose

echo "Deploying LambdaStack..."
cdk destroy LambdaStack --force --verbose

echo "Destroying VpcStack..."
cdk destroy VpcStack --force --verbose