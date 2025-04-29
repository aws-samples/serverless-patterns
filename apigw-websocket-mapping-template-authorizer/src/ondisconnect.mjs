import { DynamoDBClient, DeleteItemCommand } from "@aws-sdk/client-dynamodb";
const client = new DynamoDBClient({ region: process.env.AWS_REGION });

export const handler = async (event) => {
  const connectionId = event.requestContext.connectionId;
  const deleteParams = {
      "Key": {
        "connectionId": {
          "S": connectionId
        },
      },
      "TableName": process.env.TABLE_NAME
  };

  try {
    const command = new DeleteItemCommand(deleteParams);
    await client.send(command);
  } catch (err) {
    return { statusCode: 500, body: "Failed to disconnect: " + JSON.stringify(err) };
  }

  return { statusCode: 200, body: "Disconnected." };
};