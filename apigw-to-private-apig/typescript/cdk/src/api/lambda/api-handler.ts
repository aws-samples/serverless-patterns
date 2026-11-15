
import { Handler } from "aws-lambda";
import config from "../config.json";

export const handler: Handler = async (event) => {
  return {
    body: `Success path: "${event.path}"`,
    headers: config.headers,
    statusCode: 200,
  };
};