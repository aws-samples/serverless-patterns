import { Handler } from 'aws-lambda';
import { Collection, MongoClient, ObjectId } from 'mongodb';
import { SecretsManagerClient, GetSecretValueCommand } from "@aws-sdk/client-secrets-manager"; // ES Modules import

export const handler: Handler = async (event, context) => {
  // Add context parameter to the handler interface

  console.log('Received event:', event);
  console.log('Context:', context);

  // Check if the SecretString field is not undefined before trying to parse it as JSON
  const mongoDbUri = await getMongoDbUri();

  if (!mongoDbUri) {
    console.error('Failed to retrieve MongoDB URI from secret store');
    return {
      statusCode: 500,
      body: 'Internal server error - Failed to retrieve MongoDB URI from secret store',
    };
  }

  const method = event.requestContext.http.method;
  console.log('HTTP Method:', method);

  // Add a default case to the switch statement to handle unexpected HTTP methods
  const client = new MongoClient(mongoDbUri,
    {
      tlsCAFile: `global-bundle.pem` //Specify the DocDB; cert
    },
  );

  try {
    
    await client.connect();

    const db = client.db('mydb');
    const collection = db.collection('mycollection');

    console.log('Connected to MongoDB');

    switch (method) {
      case 'GET':
        return await handleGetRequest(collection);
      case 'POST':
        return await handlePostRequest(event, collection);
      case 'PUT':
        return await handlePutRequest(event, collection);
      case 'DELETE':
        return await handleDeleteRequest(event, collection);
      default:
        return handleUnsupportedMethod();
    }
  } finally {
    await client.close();
    console.log('MongoDB client closed');
  }
};


async function handleGetRequest(collection: Collection) {
  const data = await collection.find({}).toArray();
  console.log('Fetched data:', data);
  return {
    statusCode: 200,
    body: JSON.stringify(data),
  };
}

async function handlePostRequest(event: any, collection: Collection) {
  const payload = event.body ? JSON.parse(event.body) : {};
  console.log('Received payload:', payload);
  const result = await collection.insertOne(payload);
  console.log('Inserted data:', result);
  return {
    statusCode: 201,
    body: JSON.stringify(result),
  };
}

async function handlePutRequest(event: any, collection: Collection) {
  const updatedPayload = event.body ? JSON.parse(event.body) : {};

  console.log('Updated payload:', updatedPayload);
  const filter = { _id: new ObjectId(updatedPayload._id) };

  delete updatedPayload._id; //the _id can not be updated
  
  const result = await collection.updateOne(filter, { $set: updatedPayload });
  console.log('Updated data:', result);

  return {
    statusCode: 200,
    body: JSON.stringify(result.modifiedCount),
  };
}

async function handleDeleteRequest(event: any, collection: Collection) {
  const idToDelete = event.queryStringParameters.id;

  console.log('ID to delete:', idToDelete);

  const filter = { _id: new ObjectId(idToDelete) };

  const result = await collection.deleteOne(filter);
  console.log('Deleted data:', result);
  return {
    statusCode: 200,
    body: JSON.stringify(result.deletedCount),
  };
}

function handleUnsupportedMethod() {
  console.error('Unsupported HTTP method');
  return {
    statusCode: 400,
    body: 'Unsupported HTTP method',
  };
}

async function getMongoDbUri() {

  const secret_name = process.env.DOCUMENTDB_SECRET_NAME;

  const client = new SecretsManagerClient();
  let response;
  const uri = '';

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

    const uri = `mongodb://${DOCDB_USERNAME}:${DOCDB_PASSWORD}@${DOCDB_ENDPOINT}:${DOCDB_PORT}/mydb?tls=true&replicaSet=rs0&readPreference=secondaryPreferred&retryWrites=false`;

    return uri;
  }

  return uri;
}