# AWS DynamoDB Streams to Event Bridge using Input Transformer.

This pattern takes a change data capture event from DynamoDB, removes the data type descriptors and sends the simplified event to an EventBridge bus.

The key components of this architecture are DynamoDB as source and EventBridge as target, connected by a pipe.

To demonstrate the end-to-end message flow, the Lambda function writes sample data to the DynamoDB table.

The pattern uses an input transformer to change the event's structure from DynamoDB's response format, which includes data type descriptors, to a simpler JSON structure. The input transformer also allows us to transform the list using the following notation: `<$.dynamodb.NewImage.list.L[*].S>`