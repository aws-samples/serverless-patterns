const { DynamoDBClient } = require('@aws-sdk/client-dynamodb');
const { DynamoDBDocumentClient, PutCommand} = require('@aws-sdk/lib-dynamodb');
const tableName = process.env.TABLE_NAME;

const testOrderWithoutItem = {
    "orderID": "111",
    "Items": []
};
const testOrderWithOneItem = {
    "orderID": "222",
    "Items": ["One"]
};
const testOrderWithThreeItems = {
    "orderID": "333",
    "Items": ["One", "Two", "Three"]
};


async function writeToDb(item) {
    const params = {
        TableName: tableName,
        Item: item
    };

    const client = new DynamoDBClient();
    const ddbDocClient = DynamoDBDocumentClient.from(client);
    return await ddbDocClient.send(new PutCommand(params));
}

exports.handler = async function (event, context) {
    
    var items = [testOrderWithoutItem, testOrderWithOneItem, testOrderWithThreeItems];
    console.log("items:", items);

    var result = await Promise.all(items.map(writeToDb))
    console.log("Success :", result.map(JSON.stringify));

    const resonse = {
        eventType: "Some_Event_Type",
        ids: items
                .map(element => element.orderID)
    }
    console.log('response:', resonse);
    return resonse;
}