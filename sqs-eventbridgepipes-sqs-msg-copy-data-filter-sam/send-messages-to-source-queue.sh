#!/bin/bash

# Prompt for SQS queue URL 
echo "Enter the SQS source queue URL:"
read sqsUrl

# Prompt for AWS region 
echo "Enter your AWS region:"
read region

# Messages
msg1='{"id":1, "color":"red"}'
msg2='{"id":2, "color":"blue"}' 
msg3='{"id":3, "color":"yellow"}'
msg4='{"id":4, "color":"green"}'

# Send messages
aws sqs send-message --queue-url $sqsUrl --message-body "$msg1" --region $region
aws sqs send-message --queue-url $sqsUrl --message-body "$msg2" --region $region
aws sqs send-message --queue-url $sqsUrl --message-body "$msg3" --region $region 
aws sqs send-message --queue-url $sqsUrl --message-body "$msg4" --region $region

echo "4 messages sent to SQS queue: $sqsUrl"