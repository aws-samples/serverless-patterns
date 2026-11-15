import axios, { AxiosInstance } from 'axios';
import {
  SecretsManagerClient,
  GetSecretValueCommand,
  GetSecretValueCommandInput,
  GetSecretValueCommandOutput,
} from '@aws-sdk/client-secrets-manager';

export const handler = async (event) => {
  console.log(event);
  
  const client = new SecretsManagerClient({ region: process.env.AWS_REGION });
  console.log(`Requesting secret ${process.env.SECRET_ARN} in ${process.env.AWS_REGION}`);

  const params: GetSecretValueCommandInput = {
    SecretId: process.env.SECRET_ARN,
  };

  const command: GetSecretValueCommand = new GetSecretValueCommand(params);
  const output: GetSecretValueCommandOutput = await client.send(command);

  // DONT EVER DO THIS IN A REAL APPLICATION
  console.log(JSON.parse(output.SecretString + ''));

  console.log("before axios call", new Date().toLocaleTimeString());
  try {
    // This should succeed. This lambda has full internet access
    await axios({
        method: 'get',
        url: 'http://checkip.amazonaws.com/',
        timeout: 2000 // only wait for 2s
      })
      console.log("axios call passed @ ", new Date().toLocaleTimeString())
    }
    catch (err) {
      console.log("axios call failed @ ", new Date().toLocaleTimeString())
      console.log(err)
    }
}
