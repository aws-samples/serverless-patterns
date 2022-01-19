const AWS = require('aws-sdk');

exports.handler =  async (event) => {
    var docClient = new AWS.DynamoDB.DocumentClient()
    const params = {
        TableName: process.env.TableName,
        Item: {
            "transaction_id": event.transaction_id
        }
    }
    await docClient.put(params).promise()
}
