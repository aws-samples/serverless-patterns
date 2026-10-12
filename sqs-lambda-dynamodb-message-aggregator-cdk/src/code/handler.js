const { DynamoDBClient } = require('@aws-sdk/client-dynamodb');
const { DynamoDBDocumentClient, GetCommand, PutCommand, DeleteCommand } = require('@aws-sdk/lib-dynamodb');
const { SQSClient, SendMessageCommand } = require('@aws-sdk/client-sqs');

const dynamoDB = DynamoDBDocumentClient.from(new DynamoDBClient({}));
const queue = new SQSClient({});

exports.handler = async (event) => {

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
        const dynamoRecord = await dynamoDB.send(new GetCommand({
            TableName: process.env.DYNAMODB_TABLE_NAME,
            Key: {
                'id': correlationId
            }
        }));
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
        const result = await dynamoDB.send(new PutCommand({
            TableName: process.env.DYNAMODB_TABLE_NAME,
            Item: item,
            ReturnValues: 'ALL_OLD'
        }));

        // if item is last, trigger aggregation
        // and delete item from Dynamo
        if (item.count === total) {
            await queue.send(new SendMessageCommand({
                QueueUrl: process.env.DESTINATION_QUEUE_URL,
                MessageBody: JSON.stringify(item.body)
            }));
            await dynamoDB.send(new DeleteCommand({
                TableName: process.env.DYNAMODB_TABLE_NAME,
                Key: {
                    'id': correlationId
                }
            }));
        }
    }

    //complete
    return {
        statusCode: '200',
        body: JSON.stringify({ 'status': 'complete' })
    };
};
