import { DynamoDBClient, GetItemCommand } from "@aws-sdk/client-dynamodb";
import { CognitoJwtVerifier } from "aws-jwt-verify";

const client = new DynamoDBClient();
const TABLE_NAME = process.env.TABLE_NAME;

const verifier = CognitoJwtVerifier.create({
  userPoolId: process.env.USER_POOL_ID,
  tokenUse: "id",
  clientId: process.env.CLIENT_ID,
});

export const handler = async (event) => {
  const token = event.authorizationToken;

  if (!token) {
    throw new Error("Unauthorized: No token provided");
  }

  try {
    const payload = await verifier.verify(token.replace(/^Bearer\s+/i, ""));
    const tenantId = payload["custom:tenantId"];

    if (!tenantId) {
      throw new Error("Unauthorized: No tenant ID in claims");
    }

    const result = await client.send(
      new GetItemCommand({
        TableName: TABLE_NAME,
        Key: { tenantId: { S: tenantId } },
      }),
    );

    if (!result.Item || !result.Item.apiKey) {
      throw new Error("Unauthorized: Tenant not found");
    }

    const apiKey = result.Item.apiKey.S;

    return {
      principalId: tenantId,
      policyDocument: {
        Version: "2012-10-17",
        Statement: [
          {
            Effect: "Allow",
            Resource: event.methodArn,
            Action: "execute-api:Invoke",
          },
        ],
      },
      context: { tenantId },
      usageIdentifierKey: apiKey,
    };
  } catch (error) {
    console.error("Authorization error:", error.message);
    throw new Error("Unauthorized");
  }
};
