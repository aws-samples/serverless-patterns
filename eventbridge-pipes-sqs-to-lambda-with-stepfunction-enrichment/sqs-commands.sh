# Add example order into the database for enrichment
aws dynamodb put-item \
--table-name=TABLE_NAME \
--item '{"Id": {"S": "905fa520-4d4a-4850-97c5-1d429f8c23ba"}, "CustomerId": {"S": "50a69138-f04c-4080-8c86-da34853563bfy"}, "OrderStatus": {"S": "CREATED"}, "OrderTotal": {"N": "85"}}'

 # Trigger SQS message
 aws sqs send-message \
 --queue-url=QUEUE_URL \
 --message-body '{"order_id":"905fa520-4d4a-4850-97c5-1d429f8c23ba"}'



