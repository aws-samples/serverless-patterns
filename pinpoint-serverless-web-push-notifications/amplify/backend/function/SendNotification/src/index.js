/* Amplify Params - DO NOT EDIT
	ENV
	REGION
	STORAGE_USER_ARN
	STORAGE_USER_NAME
	STORAGE_USER_STREAMARN
Amplify Params - DO NOT EDIT */
const AWS = require('aws-sdk');
const dynamoDB = new AWS.DynamoDB();
const pinpoint = new AWS.Pinpoint();

/**
 * @type {import('@types/aws-lambda').APIGatewayProxyHandler}
 */
exports.handler = async (event) => {
    const body = JSON.parse(event.body)
    const userId = body.id
    const message = body.message
    const title = body.title
    const applicationId = "6a3dc2995321464e931eb51a139b5ee4"

    const getUserParams = {
        TableName: 'user',
        Key: {
            id: {
                S: userId
            }
        }
    }

    const user = await dynamoDB.getItem(getUserParams).promise();

    const token = user.Item.token.S

    const messageRequest = {
        'Addresses': {
            [token]: {
                'ChannelType': 'GCM'
            }
        },
        'MessageConfiguration': {
            'GCMMessage': {
                'Action': 'URL',
                'Body': message,
                'Priority': 'normal',
                'SilentPush': false,
                'Title': title,
                'TimeToLive': 30,
                'Url': 'https://amazon.com/'
            }
        }
    };

    const pinpointParams = {
        "ApplicationId": applicationId,
        "MessageRequest": messageRequest
    };

    const response = await pinpoint.sendMessages(pinpointParams).promise();

    return {
        statusCode: 200,
        headers: {
            "Access-Control-Allow-Origin": "*",
            "Access-Control-Allow-Headers": "*"
        },
    };
};
