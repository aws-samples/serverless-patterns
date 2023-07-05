import { MongoClient } from 'mongodb';
import { Secret } from './secret-manager';

import { writeFile } from 'node:fs/promises';
import { MONGO_PUBLIC_KEY_CERTIFICATE } from '../certificates/global-bundle.pem';

const MONGO_PUBLIC_KEY_FILE_PATH = '/tmp/global-bundle.pem';

let client: MongoClient | undefined;

export async function initializeMongoClient(databaseName: string, { username, password, host, port }: Secret): Promise<MongoClient> {
  if (!!client) {
    return client;
  }
  const encodedPassword = encodeURIComponent(password);
  // Create the MongoDB connection URI
  const uri = `mongodb://${username}:${encodedPassword}@${host}:${port}/${databaseName}?tls=true&replicaSet=rs0&readPreference=secondaryPreferred&retryWrites=false`;
  await writeMongoPublicKeyToTmp();

  // Connect to DocumentDB using the MongoDB driver
  client = new MongoClient(uri, {
    tlsCAFile: MONGO_PUBLIC_KEY_FILE_PATH, //Specify the DocDB; cert
  });

  return client;
}

const writeMongoPublicKeyToTmp = async () => {
  try {
    await writeFile(MONGO_PUBLIC_KEY_FILE_PATH, MONGO_PUBLIC_KEY_CERTIFICATE);
    console.log('mongo public key was written to /tmp successfully!');
  } catch (error) {
    console.error('Error downloading mongo public key:', error);
    throw error;
  }
};

export async function enableMongoChangeStream(mongoClient: MongoClient, databaseName: string, collectionName: string) {
  const db = mongoClient.db(databaseName);
  return db.admin().command({ modifyChangeStreams: 1, database: databaseName, collection: collectionName, enable: true });
}
