import { GetSecretValueCommand, SecretsManagerClient } from "@aws-sdk/client-secrets-manager";
const client = new SecretsManagerClient();

const SECRET_PREFIX = process.env.SECRET_PREFIX || "api-key-";

exports.handler = async (event) => {
  // Get API key from request headers
  const apiKey = event.authorizationToken;

  if (!apiKey) {
    throw new Error("Unauthorized: No API key provided");
  }

  try {
    // Validate API key by directly accessing the specific secret
    const tenantData = await validateApiKey(apiKey, event);

    if (tenantData) {
      return generatePolicy(tenantData.tenantId, "Allow", event.methodArn, tenantData.tenantId);
    } else {
      throw new Error("Unauthorized: Invalid API key");
    }
  } catch (error) {
    console.error("Authorization error:", error.message);
    throw new Error("Unauthorized");
  }
};

async function validateApiKey(apiKey, event) {
  try {
    // Get the secret directly using the API key's secret name
    const secretId = `${SECRET_PREFIX}${apiKey}`;

    const secretData = await client.send(
      new GetSecretValueCommand({
        SecretId: secretId,
      }),
    );

    if (secretData.SecretString) {
      const secret = JSON.parse(secretData.SecretString);
      return {
        tenantId: secret.tenantId,
        valid: true,
      };
    }
  } catch (error) {
    // Secret not found or other error - API key is invalid
    if (error.code === "ResourceNotFoundException") {
      console.log("API key not found");
    } else {
      console.error("Error fetching API key secret:", error);
    }
    return null;
  }

  return null;
}

// Helper function to generate IAM policy
function generatePolicy(principalId, effect, resource, tenantId) {
  const authResponse = {
    principalId: principalId,
  };

  if (effect && resource) {
    const policyDocument = {
      Version: "2012-10-17",
      Statement: [
        {
          Effect: effect,
          Resource: resource,
          Action: "execute-api:Invoke",
        },
      ],
    };

    authResponse.policyDocument = policyDocument;

    // Add context with tenant ID for downstream Lambda functions
    authResponse.context = {
      tenantId: tenantId,
    };
  }

  return authResponse;
}
