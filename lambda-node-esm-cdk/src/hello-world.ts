import { APIGatewayProxyResultV2, APIGatewayProxyEvent } from 'aws-lambda';

const lambdaHandler = async function (event: APIGatewayProxyEvent): Promise<APIGatewayProxyResultV2> {
    try {
        return {
            statusCode: 200,
            body: JSON.stringify({
                message: "Hello Node ESM Module",
            }),
        };
    } catch (err) {
        console.log(err);
        return {
            statusCode: 500,
            body: JSON.stringify({
                message: 'some error happened',
            }),
        };
    }
};

export const handler = lambdaHandler