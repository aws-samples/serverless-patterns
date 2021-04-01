
import { Handler } from "aws-lambda";
import config from "../config.json";

export const handler: Handler = async (event) => {
  return {
    body: `Hello Serverless Citizen, your happy path is: "${event.path}"`,
    headers: config.headers,
    statusCode: 200,
  };
};