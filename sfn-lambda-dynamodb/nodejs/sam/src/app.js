const { DynamoDBClient } = require('@aws-sdk/client-dynamodb');
const { DynamoDBDocumentClient, PutCommand } = require('@aws-sdk/lib-dynamodb');

exports.handler =  async (event) => {
    var docClient = DynamoDBDocumentClient.from(new DynamoDBClient())
    const params = {
        TableName: process.env.TableName,
        Item: {
            "transaction_id": event.transaction_id
        }
    }
    await docClient.send(new PutCommand(params))
}
