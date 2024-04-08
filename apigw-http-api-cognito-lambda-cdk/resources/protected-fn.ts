import { APIGatewayProxyEventV2, APIGatewayProxyResultV2 } from 'aws-lambda'

export async function handler(event: APIGatewayProxyEventV2): Promise<APIGatewayProxyResultV2> {
    console.log(`Event: ${JSON.stringify(event, null, 2)}`);
    return {
        statusCode: 200,
        body: "Hello Protected Space!",
    };
};