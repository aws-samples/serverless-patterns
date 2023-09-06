# AWS CLI command to read the 10 messages from the AWS SQS queue
aws sqs receive-message \
    --queue-url https://sqs.us-east-1.amazonaws.com/<REPLACEME>/MyQueue \
    --attribute-names All \
    --message-attribute-names All \
    --max-number-of-messages 10