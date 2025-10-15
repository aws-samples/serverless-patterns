#!/bin/bash

# Deploy VPC first
aws cloudformation deploy \
  --template-file VPCOnly.yaml \
  --stack-name activemq-vpc \
  --region us-west-2 \
  --profile indranil8724

# Get VPC outputs
VPC_ID=$(aws cloudformation describe-stacks --stack-name activemq-vpc --region us-west-2 --profile indranil8724 --query 'Stacks[0].Outputs[?OutputKey==`VPCId`].OutputValue' --output text)
SUBNET1=$(aws cloudformation describe-stacks --stack-name activemq-vpc --region us-west-2 --profile indranil8724 --query 'Stacks[0].Outputs[?OutputKey==`PrivateSubnetOne`].OutputValue' --output text)
SUBNET2=$(aws cloudformation describe-stacks --stack-name activemq-vpc --region us-west-2 --profile indranil8724 --query 'Stacks[0].Outputs[?OutputKey==`PrivateSubnetTwo`].OutputValue' --output text)
SG_ID=$(aws cloudformation describe-stacks --stack-name activemq-vpc --region us-west-2 --profile indranil8724 --query 'Stacks[0].Outputs[?OutputKey==`SecurityGroupId`].OutputValue' --output text)

# Create MQ Configuration
CONFIG_ID=$(aws mq create-configuration \
  --name activemq-config \
  --engine-type ACTIVEMQ \
  --engine-version 5.18 \
  --region us-west-2 \
  --profile indranil8724 \
  --query 'Id' --output text)

# Create MQ Broker
aws mq create-broker \
  --broker-name ActiveMQJavaLambdaBroker \
  --engine-type ACTIVEMQ \
  --engine-version 5.18 \
  --host-instance-type mq.t3.micro \
  --deployment-mode ACTIVE_STANDBY_MULTI_AZ \
  --users Username=activemqadmin,Password=activemqPassword123,ConsoleAccess=true \
  --subnet-ids $SUBNET1 $SUBNET2 \
  --security-groups $SG_ID \
  --configuration Id=$CONFIG_ID,Revision=1 \
  --region us-west-2 \
  --profile indranil8724

echo "MQ Broker creation initiated. Check AWS Console for status."
