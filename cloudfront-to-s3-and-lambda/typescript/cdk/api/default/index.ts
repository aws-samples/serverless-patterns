import {
  APIGatewayProxyEventV2,
  APIGatewayProxyResultV2,
  Context,
} from "aws-lambda";

export const get = async (
  _event: APIGatewayProxyEventV2,
  _context: Context
): Promise<APIGatewayProxyResultV2> => {
  return {
    body: JSON.stringify({ statusCode: 404, msg: "Not found" }),
    statusCode: 404,
  };
};
