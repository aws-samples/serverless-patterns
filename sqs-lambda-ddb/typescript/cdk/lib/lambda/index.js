/*! Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
 *  SPDX-License-Identifier: MIT-0
 */

const { DynamoDBClient, PutItemCommand } = require("@aws-sdk/client-dynamodb");
const { marshall } = require("@aws-sdk/util-dynamodb");

// Get destination DynamoDB table name from the environment variables
const tableName = process.env.DESTINATION_TABLE_NAME;

// Create DynamoDB client outside of handler to optimize performance
const ddb = new DynamoDBClient({
    maxAttempts: 0, // disable DynamoDB automated retries (so Lambda fails fast and relies on SQS retry capabilities)
});

// AWS Lambda handler function
exports.handler = async function (event, context) {
    console.log(event);

    // For each message in event
    for (const record of event.Records) {
        try {
            // get the message body (i.e. the record to add to DynamoDB)
            const item = JSON.parse(record.body);

            // try saving the item to destination DynamoDB table
            await ddb.send(
                new PutItemCommand(
                    {
                        TableName: `${tableName}`,
                        Item: marshall(item),
                    }
                )
            );
        } catch (error) { // reoport any error that may come up
            console.error("FAILED TO HANDLE RECORD: ", error, record);
            throw error; // throw to tell to SQS that something went wrong with the record
        }
    }

    // exit with 200
    return {
        statusCode: 200,
    };
};
