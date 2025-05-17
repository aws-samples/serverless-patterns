import {
  DynamoDBClient,
  GetItemCommand,
  ScanCommand,
} from "@aws-sdk/client-dynamodb";
import { unmarshall, marshall } from "@aws-sdk/util-dynamodb";
import { REGION, TABLE_NAME } from "../constants";
const ddbClient = new DynamoDBClient({ region: REGION });
export const user_exists_in_UsersTable = async (
  userSub: string
): Promise<any> => {
  let Item: unknown;
  console.log(`looking for user [${userSub}] in table [${TABLE_NAME}]`);

  // search for UserID  in dynamoDb] Get Item Command
  const getItemCommand = new GetItemCommand({
    TableName: TABLE_NAME,
    Key: {
      UserID: { S: userSub },
    },
  });

  const getItemResponse = await ddbClient.send(getItemCommand);
  console.log("Get Item Command Response ....", getItemResponse);

  if (getItemResponse.Item) {
    Item = unmarshall(getItemResponse.Item); // Get the first matching item
  }

  console.log("found item:", Item);
  expect(Item).toBeTruthy();
  return Item;
};
