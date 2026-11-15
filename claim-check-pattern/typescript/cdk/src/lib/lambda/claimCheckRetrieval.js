const { DynamoDBClient } = require('@aws-sdk/client-dynamodb');
const { DynamoDBDocumentClient, GetCommand } = require("@aws-sdk/lib-dynamodb")
const client = new DynamoDBClient({});
const ddbDocClient = DynamoDBDocumentClient.from(client);
const tableName = process.env.CLAIM_CHECK_TABLE;

exports.handler = async function (event, context) {
    console.log('Received event:', JSON.stringify(event, null, 2));
    const id = JSON.parse(event[0].body).detail.id;
    console.log('id (from event):', id);
    
    const params = {
        TableName: tableName,
        Key: {
         'id': id
        }
    };
    
    const response = await ddbDocClient.send(new GetCommand(params));
    console.log("Success :", response);
    
    return response;
}