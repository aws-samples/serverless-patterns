import { Handler } from 'aws-lambda';
import { SecretsManagerClient, GetSecretValueCommand } from "@aws-sdk/client-secrets-manager"; // ES Modules import

export const handler: Handler = async (event, context) => {

  const secret_name = process.env.DOCUMENTDB_SECRET_NAME;
  const client = new SecretsManagerClient();
  let response;

  try {
    response = await client.send(
      new GetSecretValueCommand({
        SecretId: secret_name,
        VersionStage: "AWSCURRENT", // VersionStage defaults to AWSCURRENT if unspecified
      })
    );
  } catch (error) {
    // For a list of exceptions thrown, see
    // https://docs.aws.amazon.com/secretsmanager/latest/apireference/API_GetSecretValue.html
    throw error;
  }

  if (typeof response.SecretString != "undefined") {
    const { host, password, username, port } = JSON.parse(response.SecretString);
    const DOCDB_ENDPOINT = host || 'DOCDBURL';
    const DOCDB_PASSWORD = encodeURIComponent(password) || 'DOCPASSWORD';
    const DOCDB_USERNAME = username || 'myuser';
    const DOCDB_PORT = port || 'myuser';

    const uri = `mongodb://${DOCDB_USERNAME}:${DOCDB_PASSWORD}@${DOCDB_ENDPOINT}:${DOCDB_PORT}/test?replicaSet=rs0`;
  }

  const method = event.requestContext.http.method;

  const returnBody = { "type": "g", "score": 0, "_id": "links", "coo": [], "data": {} };

  return {
    statusCode: 200,
    body: JSON.stringify(returnBody),
  };

  if (method === 'GET') {
    return await getHello(event)
  } else if (method === 'POST') {
    return await save(event);
  } else {
    return {
      statusCode: 400,
      body: 'Not a valid operation'
    };
  }
};

async function save(event: any) {
  const name = event.queryStringParameters.name;

  const item = {
    name: name,
    date: Date.now(),
  };

  console.log(item);
  const savedItem = await saveItem(item);

  return {
    statusCode: 200,
    body: JSON.stringify(savedItem),
  };
}

async function getHello(event: any) {

}

async function getItem(name: string) {

}

async function saveItem(item: any) {

}