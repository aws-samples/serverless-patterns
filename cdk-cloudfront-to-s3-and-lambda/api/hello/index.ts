import {
  APIGatewayProxyEventV2,
  APIGatewayProxyResultV2,
  Context,
} from "aws-lambda";
import cool from "cool-ascii-faces";

export const get = async (
  _event: APIGatewayProxyEventV2,
  _context: Context
): Promise<APIGatewayProxyResultV2> => {
  return {
    headers: {
      "Content-Type": "text/plain; charset=UTF-8",
    },
    body: cool(),
    statusCode: 200,
  };
};
