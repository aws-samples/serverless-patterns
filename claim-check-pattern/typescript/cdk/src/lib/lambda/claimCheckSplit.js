const { DynamoDBClient } = require('@aws-sdk/client-dynamodb');
const { DynamoDBDocumentClient, PutCommand} = require('@aws-sdk/lib-dynamodb');
const tableName = process.env.CLAIM_CHECK_TABLE;

exports.handler = async function (event, context) {
    console.log('Received event:', JSON.stringify(event, null, 2));
    console.log('Records[0]:', event[0]);
    const body = JSON.parse(event[0].body);
    console.log('body:', body);

    // put the message in the table
    const params = {
        TableName: tableName,
        Item: body
    };

    const client = new DynamoDBClient();
    const ddbDocClient = DynamoDBDocumentClient.from(client);
    await ddbDocClient.send(new PutCommand(params));

    const resonse = {
        eventType: "Some_Event_Type",
        id: body.id,
    }
    console.log('response:', resonse);
    return resonse;
}