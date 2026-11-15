 # Send SQS message to be sent to EventBridge using the filter.
 aws sqs send-message \
 --queue-url=SQS_URL \
 --message-body '{"orderId":"125a2e1e-d420-482e-8008-5a606f4b2076, "customerId": "a48516db-66aa-4dbc-bb66-a7f058c5ec24", "type": "NEW"}'

# Send SQS message that will be ignored due to filter
aws sqs send-message \
 --queue-url=SQS_URL \
 --message-body '{"orderId":"125a2e1e-d420-482e-8008-5a606f4b2076, "customerId": "a48516db-66aa-4dbc-bb66-a7f058c5ec24", "type": "OLD"}'