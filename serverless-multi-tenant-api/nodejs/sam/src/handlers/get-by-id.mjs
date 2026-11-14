import { DynamoDBClient } from "@aws-sdk/client-dynamodb";
import { DynamoDBDocumentClient, GetCommand } from "@aws-sdk/lib-dynamodb";

// Get the DynamoDB table name from environment variables
const tableName = process.env.ITEM_TABLE;

/**
 * A simple example includes a HTTP get method to get one item by id from a DynamoDB table.
 */
export const getByIdHandler = async (event, context) => {
  if (event.httpMethod !== "GET") {
    throw new Error(
      `getMethod only accept GET method, you tried: ${event.httpMethod}`
    );
  }

  const client = new DynamoDBClient({
    credentials: {
      accessKeyId: event.requestContext.authorizer.accessKey,
      secretAccessKey: event.requestContext.authorizer.secretKey,
      sessionToken: event.requestContext.authorizer.sessionToken,
    },
  });

  const ddbDocClient = DynamoDBDocumentClient.from(client);

  // Get tenantId from request context authorizer
  const tenantId = event.requestContext.authorizer.tenantId;

  // Get id from pathParameters from APIGateway because of `/{id}` at template.yaml
  const id = event.pathParameters.id;

  // Get the item from the table
  // https://docs.aws.amazon.com/AWSJavaScriptSDK/latest/AWS/DynamoDB/DocumentClient.html#get-property
  var params = {
    TableName: tableName,
    Key: { PK: `T#${tenantId}#${id}` },
  };

  try {
    const data = await ddbDocClient.send(new GetCommand(params));
    var item = {
      id: data.Item.id,
      name: data.Item.name,
    };
  } catch (err) {
    console.log("Error", err);
    return {
      statusCode: 500,
      body: JSON.stringify({
        message: "Error",
        error: err.stack,
      }),
    };
  }

  const response = {
    statusCode: 200,
    body: JSON.stringify(item),
  };

  // All log statements are written to CloudWatch
  console.info(
    `response from: ${event.path} statusCode: ${response.statusCode} body: ${response.body}`
  );
  return response;
};
