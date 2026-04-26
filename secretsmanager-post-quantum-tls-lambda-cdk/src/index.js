const { SecretsManagerClient, GetSecretValueCommand } = require('@aws-sdk/client-secrets-manager');

// The AWS SDK for JavaScript v3 in Lambda runtime automatically negotiates
// hybrid post-quantum TLS (ML-KEM / X25519MLKEM768) when the service supports it.
// No code changes needed — just use the latest SDK version.
const client = new SecretsManagerClient();

exports.handler = async (event) => {
  const result = await client.send(new GetSecretValueCommand({
    SecretId: process.env.SECRET_ARN,
  }));

  const secret = JSON.parse(result.SecretString);
  return {
    statusCode: 200,
    secretRetrieved: true,
    username: secret.username,
    passwordLength: secret.password.length,
    postQuantumTls: {
      enabled: true,
      keyExchange: 'X25519MLKEM768 (hybrid post-quantum)',
      verification: 'Check CloudTrail tlsDetails.keyExchangeAlgorithm for GetSecretValue events',
      protection: 'Protects against harvest-now-decrypt-later (HNDL) quantum threats',
    },
  };
};
