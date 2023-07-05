import { MongoClient } from 'mongodb';
import { Secret } from './secret-manager';

export function initializeMongoClient(databaseName: string, { username, password, host, port }: Secret): MongoClient {
  // Create the MongoDB connection URI
  const uri = `mongodb+srv://${username}:${password}@${host}:${port}/${databaseName}?retryWrites=true&w=majority`;

  // Connect to DocumentDB using the MongoDB driver
  const client = new MongoClient(uri, {
    tlsCAFile: `global-bundle.pem`, //Specify the DocDB; cert
  });

  return client;
}

export async function enableMongoChangeStream(mongoClient: MongoClient, databaseName: string, collectionName: string) {
  // Access the database and collection
  const db = mongoClient.db(databaseName);

  // Perform database operations or other logic here...
  const result = await db.admin().command({ modifyChangeStreams: 1, database: databaseName, collection: collectionName, enable: true });
  console.log('modified Change Streams for mongo:', JSON.stringify(result, null, 2));
}

// try {
//   return {
//     statusCode: 200,
//     body: 'Connection to DocumentDB established successfully',
//   };
// } catch (error) {
//   console.error('Error:', error);
//   return {
//     statusCode: 500,
//     body: 'Failed to connect to DocumentDB',
//   };
// }
// return;
