echo "Provide the name of the SQS queue to send messages to"

read queue_name

aws sqs send-message \
    --queue-url $queue_name \
    --message-body file://msg/message-01.json \
    --message-attributes file://msg/attributes-01.json \

aws sqs send-message \
    --queue-url $queue_name \
    --message-body file://msg/message-02.json \
    --message-attributes file://msg/attributes-02.json \

aws sqs send-message \
    --queue-url $queue_name \
    --message-body file://msg/message-03.json \
    --message-attributes file://msg/attributes-03.json \

sleep 5

echo "Provide the name of the SQS queue to receive the aggregated message"

read destination_name

aws sqs receive-message \
    --queue-url $destination_name \