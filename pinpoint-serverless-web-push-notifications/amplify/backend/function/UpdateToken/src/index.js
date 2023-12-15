/* Amplify Params - DO NOT EDIT
	ENV
	REGION
	STORAGE_USER_ARN
	STORAGE_USER_NAME
	STORAGE_USER_STREAMARN
Amplify Params - DO NOT EDIT */
const AWS = require('aws-sdk');
const dynamoDB = new AWS.DynamoDB();

/**
 * @type {import('@types/aws-lambda').APIGatewayProxyHandler}
 */
exports.handler = async (event) => {
    const body = JSON.parse(event.body)
    const userId = body.id
    const token = body.token

    const updateTokenParams = {
        TableName: 'user',
        Item: {
            id: {
                S: userId
            },
            token: {
                S: token
            }
        }
    }

    await dynamoDB.putItem(updateTokenParams).promise();

    return {
        statusCode: 200,
        headers: {
            "Access-Control-Allow-Origin": "*",
            "Access-Control-Allow-Headers": "*"
        },
    };
};
