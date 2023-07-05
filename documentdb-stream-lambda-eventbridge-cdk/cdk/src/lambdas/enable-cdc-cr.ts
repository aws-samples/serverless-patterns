import { CreateEventSourceMappingCommand, LambdaClient } from '@aws-sdk/client-lambda';
const lambdaClient = new LambdaClient({
  region: process.env.AWS_REGION!,
});

type CdcStream = {
  cdcFunctionName: string;
  authUri: string;
  secretName: string;
  clusterArn: string;
  databaseName: string;
  collectionName: string;
};

const enableCdcCrHandler = async (event: any) => {
  console.log('Event:', event);
  console.log('ENV:', process.env);
  try {
    const eventSourceMappings = event.cdcStreams.map((stream: CdcStream) =>
      lambdaClient.send(
        new CreateEventSourceMappingCommand({
          FunctionName: stream.cdcFunctionName,
          EventSourceArn: stream.clusterArn,
          BatchSize: 100,
          StartingPosition: 'TRIM_HORIZON',
          SourceAccessConfigurations: [{ Type: 'BASIC_AUTH', URI: stream.authUri }],
          DocumentDBEventSourceConfig: {
            DatabaseName: stream.databaseName,
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
    console.error('Error in enabling CDC:', error);
    throw error;
  }
};

export const main = enableCdcCrHandler;
