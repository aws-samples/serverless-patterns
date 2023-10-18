#!/bin/bash

# Set the number of messages and queue URL as input
num_messages=10
hp_queue_url=https://sqs.us-east-1.amazonaws.com/123456789012/HighPrioritySqsQueue.fifo
mp_queue_url=https://sqs.us-east-1.amazonaws.com/123456789012/MediumPrioritySqsQueue.fifo
lp_queue_url=https://sqs.us-east-1.amazonaws.com/123456789012/LowPrioritySqsQueue.fifo

# Loop to publish messages using aws cli 
for ((i=1;i<=$num_messages;i++)); do
  aws sqs send-message --queue-url $hp_queue_url --message-group-id "group1" --message-body "High Priority Message $i"
  aws sqs send-message --queue-url $mp_queue_url --message-group-id "group1" --message-body "Medium Priority Message $i"
  aws sqs send-message --queue-url $lp_queue_url --message-group-id "group1" --message-body "Low Priority Message $i"    
done

echo "$num_messages messages sent to each of the queues"