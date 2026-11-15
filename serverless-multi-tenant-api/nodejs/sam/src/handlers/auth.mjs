// Import AWS SDK clients
import { STSClient, AssumeRoleCommand } from "@aws-sdk/client-sts";
import { DynamoDBClient } from "@aws-sdk/client-dynamodb";
import { DynamoDBDocumentClient, GetCommand } from "@aws-sdk/lib-dynamodb";

// Initialize clients
const stsClient = new STSClient({});
const client = new DynamoDBClient({});
const ddbDocClient = DynamoDBDocumentClient.from(client);

// Get environment variables
const itemTableArn = process.env.ITEM_TABLE_ARN;
const authorizerAccessRoleArn = process.env.AUTHORIZER_ACCESS_ROLE_ARN;
const configTableName = process.env.CONFIG_TABLE;

// Lookup tenant ID from API key in config table
const lookupTenantId = async (apiKey) => {
  // Query config table
  var params = {
    TableName: configTableName,
    Key: { PK: `K#${apiKey}` },
  };

  try {
    // Get tenant ID from config table
    const data = await ddbDocClient.send(new GetCommand(params));
    return data.Item?.TENANT_ID || null;
  } catch (err) {
    console.log("Error looking up tenant ID", err);
    return null;
  }
};

// Generate policy document allowing access to tenant's items
const getPolicyForTenant = (tenantId) => {
  // Policy to allow access to items with matching tenant ID
  return {
    Version: "2012-10-17",
    Statement: [
      {
        Action: ["dynamodb:GetItem", "dynamodb:PutItem"],
        Resource: [itemTableArn],
        Effect: "Allow",
        Condition: {
          "ForAllValues:StringLike": {
            "dynamodb:LeadingKeys": [`T#${tenantId}#*`],
          },
        },
      },
    ],
  };
};

// Policy to deny access
const unAuthorizedResponse = () => {
  return {
    principalId: "unauthorized",
    policyDocument: {
      Version: "2012-10-17",
      Statement: [
        {
          Action: "execute-api:Invoke",
          Effect: "Deny",
          Resource: "*",
        },
      ],
    },
  };
};

// Main authorizer function
export const authHandler = async (event, context, callback) => {
  // Get API key from headers
  const apiKey = event.headers["x-api-key"];

  // Lookup tenant ID
  const tenantId = await lookupTenantId(apiKey);

  // Deny access if no tenant ID
  if (!tenantId) {
    return unAuthorizedResponse();
  }

  // Get policy for tenant
  const tenantIamPolicy = getPolicyForTenant(tenantId);

  // Assume role
  const assumedRole = await stsClient.send(
    new AssumeRoleCommand({
      RoleArn: authorizerAccessRoleArn,
      RoleSessionName: "tenant-aware-session",
      Policy: JSON.stringify(tenantIamPolicy),
    })
  );

  // Extract temporary credentials
  const { Credentials } = assumedRole;

  // Allow invoking API
  const policyDocument = {
    Version: "2012-10-17",
    Statement: [
      {
        Action: "execute-api:Invoke",
        Effect: "Allow",
        Resource: event.methodArn.split("/", 2).join("/") + "/*/*",
      },
    ],
  };

  // Return auth response
  return {
    principalId: `${tenantId}`,
    context: {
      accessKey: Credentials.AccessKeyId,
      secretKey: Credentials.SecretAccessKey,
      sessionToken: Credentials.SessionToken,
      tenantId,
    },
    policyDocument,
  };
};
