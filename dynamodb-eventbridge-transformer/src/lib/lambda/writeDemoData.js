const { DynamoDBClient } = require('@aws-sdk/client-dynamodb');
const { DynamoDBDocumentClient, PutCommand} = require('@aws-sdk/lib-dynamodb');
const tableName = process.env.TABLE_NAME;

const messageWithEmptyList = {
    "id": "111",
    "list": []
};
const messageWithOneItemList = {
    "id": "222",
    "list": ["One"]
};
const messageWithMultipleItemList = {
    "id": "333",
    "list": ["One", "Two", "Three"]
};


async function writeToDb(item) {
    // put the message in the table
    const params = {
        TableName: tableName,
        Item: item
    };

    const client = new DynamoDBClient();
    const ddbDocClient = DynamoDBDocumentClient.from(client);
    return await ddbDocClient.send(new PutCommand(params));
}

exports.handler = async function (event, context) {
    
    var items = [messageWithEmptyList, messageWithOneItemList, messageWithMultipleItemList];

    console.log("items:", items);

    var result = await Promise.all(items.map(writeToDb))
    console.log("Success :", result.map(JSON.stringify));

    const resonse = {
        eventType: "Some_Event_Type",
        ids: items
                .map(element => element.id)
    }
    console.log('response:', resonse);
    return resonse;
}