import { SecretsManagerClient, GetSecretValueCommand } from "@aws-sdk/client-secrets-manager";

// Load the secret on init
const client = new SecretsManagerClient({ region: process.env.AWS_REGION });
const cmd = new GetSecretValueCommand({
  "SecretId": process.env.SECRET_NAME
});

console.log("Loading secret");
const secret = await client.send(cmd);


export const handler = async (event, context) => {
  console.log("Secret is loaded");
  return {
    timestamp: new Date().toISOString(),
    secret: secret.SecretString
  }
};