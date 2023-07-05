import { GetSecretValueCommand, SecretsManagerClient } from '@aws-sdk/client-secrets-manager';

const secretsManagerClient = new SecretsManagerClient({ region: process.env.AWS_REGION! });

export type Secret = { username: string; password: string; host: string; port: number };

let secret: Secret | undefined;

export async function fetchSecretValue(secretName: string): Promise<Secret> {
  if (!!secret?.password) {
    return secret;
  }

  // Fetch the secret value from Secrets Manager
  const getSecretValueCommand = new GetSecretValueCommand({ SecretId: secretName });
  const secretValue = await secretsManagerClient.send(getSecretValueCommand);

  // Parse the secret value as JSON
  secret = JSON.parse(secretValue.SecretString || '') as Secret;

  // Retrieve the required connection parameters from the secret
  return secret;
}
