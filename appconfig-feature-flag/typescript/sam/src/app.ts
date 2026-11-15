import { APIGatewayProxyEvent, APIGatewayProxyResult } from 'aws-lambda';
import fetch from 'node-fetch';

/**
 *
 * Event doc: https://docs.aws.amazon.com/apigateway/latest/developerguide/set-up-lambda-proxy-integrations.html#api-gateway-simple-proxy-for-lambda-input-format
 * @param {Object} event - API Gateway Lambda Proxy Input Format
 *
 * Return doc: https://docs.aws.amazon.com/apigateway/latest/developerguide/set-up-lambda-proxy-integrations.html
 * @returns {Object} object - API Gateway Lambda Proxy Output Format
 *
 */

const configPath = process.env.SAM_CONFIG_PATH!;

export const lambdaHandler = async (event: APIGatewayProxyEvent): Promise<APIGatewayProxyResult> => {
    let response: APIGatewayProxyResult;
    try {

        const configResponse = await fetch(
            "http://localhost:2772/" + configPath,
            {
                method: 'GET',
                headers: {
                    Accept: 'application/json'
                }
            }
        );

        if (!configResponse.ok) {
            throw new Error(`Error! status: ${configResponse.status}`);
        }

        const config = (await configResponse.json());

        const configurationResponse: Configuration = {
            Pagination: {
                Enabled: config.pagination.enabled,
                PageSize: config.pagination.pageSize
            },
            WizardSwitch: {
                Enabled: config.wizardSwitch.enabled
            }
        };

        response = {
            statusCode: 200,
            body: JSON.stringify(configurationResponse),
        };
    } catch (err) {
        console.log(err);
        response = {
            statusCode: 500,
            body: JSON.stringify({
                message: 'some error happened',
            }),
        };
    }

    return response;
};

type Configuration ={
    Pagination: PaginationFeature;
    WizardSwitch: Feature;
};
type PaginationFeature = Feature & {
    PageSize: number
};
type Feature = {
    Enabled: boolean
};