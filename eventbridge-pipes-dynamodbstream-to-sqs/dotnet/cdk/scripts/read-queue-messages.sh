#!/bin/bash

# Usage: This script takes an SQS queue as input, and reads a batch of those messages and prints them to the terminal.

# Define the AWS CLI command to receive messages from an SQS queue
queue_url=$1
receive_message="aws sqs receive-message --max-number-of-messages 10 --queue-url $queue_url"

# Execute the receive-message command and store the result in a variable
result=$(eval $receive_message)

# Extract the messages from the result
messages=$(echo $result | jq -c '.Messages[]')

# Iterate through each message and print the body
for message in $messages
do
    echo $message | jq -cr '.Body' | jq '.'
done