#!/bin/bash

# Get SQS queue URL
echo "Enter SQS target queue URL:" 
read queue_url

# Get the AWS region 
echo "Enter your AWS region:" 
read region

# Get the number of messages in the queue
msg_count=$(aws sqs get-queue-attributes --queue-url $queue_url --attribute-names ApproximateNumberOfMessages --region $region --output text | awk '{print $2}')

# Keep reading messages until the queue is empty
while [ $msg_count -gt 0 ]; do
  aws sqs receive-message --queue-url $queue_url --attribute-names All --message-attribute-names All --max-number-of-messages 1 --visibility-timeout 30 --wait-time-seconds 1 --region $region --output json

  msg_count=$(aws sqs get-queue-attributes --queue-url $queue_url --attribute-names ApproximateNumberOfMessages --region $region --output text | awk '{print $2}')  
done

echo "Queue is now empty"