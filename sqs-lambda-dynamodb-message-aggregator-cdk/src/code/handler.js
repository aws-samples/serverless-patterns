const AWS = require('aws-sdk');

exports.handler = async (event, context, callback) => {

    // retrieve dynamo name from environment variable
    const dynamoDB = new AWS.DynamoDB.DocumentClient();
    const queue = new AWS.SQS();

    // loop through all sqs records
    for (const record of event.Records) {

        // create dynamo record
        const correlationId = record.messageAttributes.CorrelationId.stringValue;
        const total = Number(record.messageAttributes.Total.stringValue);
        const body = JSON.parse(record.body);
        let item = {
            id: correlationId,
            body: body,
            count: 0
        };

        // check if item exists in dynamo
        const dynamoRecord = await dynamoDB.get({
            TableName: process.env.DYNAMODB_TABLE_NAME,
            Key: {
                'id': correlationId
            }
        }).promise();
        // if item exists, update item
        if (dynamoRecord.Item) {
            item.body = Object.assign(dynamoRecord.Item.body, item.body);
            item.count = dynamoRecord.Item.count + 1;
        } else {
            // if item doesn't exist, create item
            item.body = item.body;
            item.count = 1;
        }
        // put item in dynamo
        const result = await dynamoDB.put({
            TableName: process.env.DYNAMODB_TABLE_NAME,
            Item: item,
            ReturnValues: 'ALL_OLD'
        }).promise();

        // if item is last, trigger aggregation
        // and delete item from Dynamo
        if (item.count === total) {
            await queue.sendMessage({
                QueueUrl: process.env.DESTINATION_QUEUE_URL,
                MessageBody: JSON.stringify(item.body)
            }).promise();
            await dynamoDB.delete({
                TableName: process.env.DYNAMODB_TABLE_NAME,
                Key: {
                    'id': correlationId
                }
            }).promise();
        }
    }

    //complete
    callback(null, {
        statusCode: '200',
        body: JSON.stringify({ 'status': 'complete' })
    });
};