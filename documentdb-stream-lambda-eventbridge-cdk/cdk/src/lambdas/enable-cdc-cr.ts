import { CreateEventSourceMappingCommand, LambdaClient } from '@aws-sdk/client-lambda';
import { fetchSecretValue } from '../clients/secret-manager';
import { initializeMongoClient, enableMongoChangeStream } from '../clients/mongo';

const lambdaClient = new LambdaClient({
  region: process.env.AWS_REGION!,
});

type CdcStream = { cdcFunctionName: string; collectionName: string };

type CdcEvent = {
  cdcStreams: CdcStream[];
  authUri: string;
  secretName: string;
  clusterArn: string;
  databaseName: string;
};

const enableCdcCrHandler = async (event: CdcEvent) => {
  console.log('Event:', event);
  console.log('ENV:', process.env);
  const secret = await fetchSecretValue(event.secretName);

  const mongoClient = await initializeMongoClient(event.databaseName, secret);

  try {
    await mongoClient.connect();

    const mongoCdcStreams = event.cdcStreams.map((stream: CdcStream) =>
      enableMongoChangeStream(mongoClient, event.databaseName, stream.collectionName)
    );
    const responses = await Promise.allSettled(mongoCdcStreams);

    console.log('Mongo CDC Stream Responses:', JSON.stringify(responses, null, 2));
    await mongoClient.close();
  } catch (error: any) {
    await mongoClient.close();
    console.error('Error in enabling CDC on Mongo:', error);
    throw error;
  }
  try {
    const eventSourceMappings = event.cdcStreams.map((stream: CdcStream) =>
      lambdaClient.send(
        new CreateEventSourceMappingCommand({
          FunctionName: stream.cdcFunctionName,
          EventSourceArn: event.clusterArn,
          BatchSize: 100,
          StartingPosition: 'LATEST',
          SourceAccessConfigurations: [{ Type: 'BASIC_AUTH', URI: event.authUri }],
          DocumentDBEventSourceConfig: {
            DatabaseName: event.databaseName,
            CollectionName: stream.collectionName,
            FullDocument: 'UpdateLookup',
          },
        })
      )
    );

    const responses = await Promise.allSettled(eventSourceMappings);

    console.log('Responses:', JSON.stringify(responses, null, 2));
    const errors = responses.filter((response) => response.status === 'rejected' && response.reason.name !== 'ResourceConflictException');
    if (errors.length > 0) {
      const errorsMessages = errors.map((error) => {
        if (error.status === 'rejected') {
          return error?.reason.name;
        }
      });
      throw new Error(errorsMessages.join(','));
    }
    return {
      PhysicalResourceId: '-' + new Date().toISOString(),
    };
  } catch (error: any) {
    console.error('Error in enabling Event Source Mapping on Lambda:', error);
    throw error;
  }
};

export const main = enableCdcCrHandler;
