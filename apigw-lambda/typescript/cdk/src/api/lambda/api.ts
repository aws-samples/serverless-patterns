import { APIGatewayEvent, Handler } from "aws-lambda";
import config from "../config.json";

export const handler: Handler = async (event: APIGatewayEvent) => {
  return {
    body: `Hello Serverless Citizen, your happy path is: "${event.path} using ${event.httpMethod}"`,
    headers: config.headers,
    statusCode: 200,
  };
};
