import { MongoClient } from 'mongodb';
import { Secret } from './secret-manager';
import axios from 'axios';
import fs = require('fs');
import util = require('util');
const stat = util.promisify(fs.stat);

let client: MongoClient | undefined;

const MONGO_PUBLIC_CERTIFICATE_KEY_URL = 'https://truststore.pki.rds.amazonaws.com/global/global-bundle.pem';
const MONGO_PUBLIC_KEY_FILE_PATH = '/tmp/global-bundle.pem';

export async function initializeMongoClient(databaseName: string, { username, password, host, port }: Secret): Promise<MongoClient> {
  if (!!client) {
    return client;
  }
  const encodedPassword = encodeURIComponent(password);
  // Create the MongoDB connection URI
  const uri = `mongodb://${username}:${encodedPassword}@${host}:${port}/${databaseName}?tls=true&replicaSet=rs0&readPreference=secondaryPreferred&retryWrites=false`;

  await downloadPublicKey();
  // Connect to DocumentDB using the MongoDB driver
  client = new MongoClient(uri, {
    tlsCAFile: `global-bundle.pem`, //Specify the DocDB; cert
  });

  return client;
}

const downloadPublicKey = async () => {
  try {
    // Check if the file already exists
    const publicKeyAlreadyDownloaded = await fileExists(MONGO_PUBLIC_KEY_FILE_PATH);

    if (!!publicKeyAlreadyDownloaded) {
      console.log('mongo public key already exists!');
      return;
    }
    const response = await axios.get(MONGO_PUBLIC_CERTIFICATE_KEY_URL, { responseType: 'stream' });
    const writer = fs.createWriteStream(MONGO_PUBLIC_KEY_FILE_PATH);

    response.data.pipe(writer);

    await new Promise((resolve, reject) => {
      writer.on('finish', resolve);
      writer.on('error', reject);
    });

    console.log('mongo public key downloaded successfully!');
  } catch (error) {
    console.error('Error downloading mongo public key:', error);
    throw error;
  }
};

// Function to check if a file exists
async function fileExists(path: string) {
  try {
    await stat(path);
    return true;
  } catch (error: any) {
    if (error.code === 'ENOENT') {
      return false;
    }
    throw error;
  }
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
