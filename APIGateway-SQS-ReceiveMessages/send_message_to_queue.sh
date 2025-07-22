#!/bin/bash
# Configuration
MESSAGE_PREFIX="Test message"
NUM_MESSAGES=5
DELAY_SECONDS=0.1

# Color codes
RED='\033[0;31m'
GREEN='\033[0;32m'
NC='\033[0m' # No Color

# Check if queue URL is provided
if [ -z "$1" ]; then
    echo -e "${RED}Error:${NC} Queue URL is required"
    echo -e "${GREEN}Usage:${NC} $0 <queue-url> [number-of-messages]"
    exit 1
fi

QUEUE_URL="$1"

# Check if number of messages is provided as second argument
if [ ! -z "$2" ]; then
    NUM_MESSAGES=$2
fi

echo "Sending $NUM_MESSAGES messages to SQS queue: $QUEUE_URL"

for i in $(seq 1 $NUM_MESSAGES)
do
    MESSAGE="$MESSAGE_PREFIX #$i: This is the $i message sent at $(date '+%Y-%m-%d %H:%M:%S')"
    
    # Capture both stdout and stderr
    output=$(aws sqs send-message \
        --queue-url "$QUEUE_URL" \
        --message-body "$MESSAGE" \
        --message-attributes "{
            \"SequenceNumber\": {
                \"DataType\": \"Number\",
                \"StringValue\": \"$i\"
            }
        }" 2>&1)
    
    # Check if command was successful
    if [ $? -ne 0 ]; then
        echo -e "${RED}Error:${NC} $output"
        exit 1
    fi
    
    echo "Sent message $i"
    sleep $DELAY_SECONDS
done

echo "Completed sending $NUM_MESSAGES messages"

