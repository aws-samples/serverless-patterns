import { DynamoDBClient } from "@aws-sdk/client-dynamodb";
import { DynamoDBDocumentClient, PutCommand } from "@aws-sdk/lib-dynamodb";

// Get the DynamoDB table name from environment variables
const tableName = process.env.ITEM_TABLE;

/**
 * A simple example includes a HTTP post method to add one item to a DynamoDB table.
 */
export const putItemHandler = async (event, context) => {
  if (event.httpMethod !== "POST") {
    throw new Error(
      `postMethod only accepts POST method, you tried: ${event.httpMethod} method.`
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

  // Get id and name from the body of the request
  const body = JSON.parse(event.body);
  const id = body.id;
  const name = body.name;

  // Creates a new item, or replaces an old item with a new item
  // https://docs.aws.amazon.com/AWSJavaScriptSDK/latest/AWS/DynamoDB/DocumentClient.html#put-property
  var params = {
    TableName: tableName,
    Item: {
      PK: `T#${tenantId}#${id}`,
      id: id,
      name: name,
    },
  };

  try {
    const data = await ddbDocClient.send(new PutCommand(params));
    console.log("Success - item added or updated", data);
  } catch (err) {
    console.log("Error", err.stack);
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
    body: JSON.stringify(body),
  };

  // All log statements are written to CloudWatch
  console.info(
    `response from: ${event.path} statusCode: ${response.statusCode} body: ${response.body}`
  );
  return response;
};
