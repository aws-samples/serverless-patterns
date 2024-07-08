echo "Provide the name of the SQS queue to send messages to"

read queue_name

aws sqs send-message \
    --queue-url $queue_name \
    --message-body file://msg/message-03.json \
    --message-attributes file://msg/attributes-03.json > /dev/null

aws sqs send-message \
    --queue-url $queue_name \
    --message-body file://msg/message-02.json \
    --message-attributes file://msg/attributes-02.json > /dev/null

aws sqs send-message \
    --queue-url $queue_name \
    --message-body file://msg/message-01.json \
    --message-attributes file://msg/attributes-01.json > /dev/null

echo "Provide the name of the SQS queue to receive the messages in the correct order"

sleep 5

#read destination_name

#aws sqs receive-message \
#    --queue-url $destination_name --max-number-of-messages 10 --output text --query 'Messages'