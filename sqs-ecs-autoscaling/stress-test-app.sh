#!/bin/bash

# Configuration
STACK_NAME=${STACK_NAME:-sqs-ecs-app}
QUEUE_URL=$(aws cloudformation describe-stacks --stack-name $STACK_NAME --query "Stacks[0].Outputs[?OutputKey=='QueueURL'].OutputValue" --output text)
TOTAL_MESSAGES=1500
PARALLEL_JOBS=5

# Function to send messages
send_messages() {
    for i in {1..300}; do
        MESSAGE="{\"message\": \"HelloMessage-$i\"}"
        aws sqs send-message \
            --queue-url $QUEUE_URL \
            --message-body "$MESSAGE" \
            --delay-seconds 0        
        echo "Sent message $i"
    done
}

# Start time
start_time=$(date +%s)

# Run multiple processes in parallel
for i in $(seq 1 $PARALLEL_JOBS); do
    send_messages &
done

# Wait for all background processes to complete
wait

# Calculate statistics
end_time=$(date +%s)
duration=$((end_time - start_time))
messages_per_second=$(bc <<< "scale=2; $TOTAL_MESSAGES / $duration")

echo "Test completed!"
echo "Total messages sent: $TOTAL_MESSAGES"
echo "Duration: $duration seconds"
echo "Rate: $messages_per_second messages/second"