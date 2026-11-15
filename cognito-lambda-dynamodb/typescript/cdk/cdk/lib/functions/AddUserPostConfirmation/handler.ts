import { PostConfirmationConfirmSignUpTriggerEvent } from "aws-lambda";
import { DynamoDBClient, PutItemCommand } from "@aws-sdk/client-dynamodb";
import { marshall } from "@aws-sdk/util-dynamodb";

// Read environment variables
const dynamoRegion = process.env.REGION;
const tableName = process.env.TABLE_NAME;

// Throw an error if mandatory env variables aren't set
if (!dynamoRegion || !tableName) {
  throw new Error(
    "Missing mandatory environment variables: 'AWS_REGION' or 'TABLE_NAME'."
  );
}

const client = new DynamoDBClient({ region: dynamoRegion });

export const handler = async (
  event: PostConfirmationConfirmSignUpTriggerEvent
) => {
  const date = new Date();
  const isoDate = date.toISOString();

  const params = {
    TableName: tableName,
    Item: marshall({
      UserID: event.request.userAttributes.sub,
      Email: event.request.userAttributes.email,
      firstName:
        event.request.userAttributes["custom:firstName"] ||
        event.request.userAttributes.given_name,
      lastName:
        event.request.userAttributes["custom:lastName"] ||
        event.request.userAttributes.family_name,
      CreatedAt: isoDate,
      __typename: "User",
    }),
  };

  try {
    await client.send(new PutItemCommand(params));
    console.log("User added to DynamoDB successfully");
  } catch (error) {
    console.error("Error adding user to DynamoDB:", error);
    throw error;
  }

  return event;
};
