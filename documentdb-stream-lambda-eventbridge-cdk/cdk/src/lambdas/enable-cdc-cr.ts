import { CreateEventSourceMappingCommand, LambdaClient } from '@aws-sdk/client-lambda';
const lambdaClient = new LambdaClient({
  region: process.env.AWS_REGION!,
});

const enableCdcCr = async (event: any) => {
  console.log('Event:', event);
  console.log('ENV:', process.env);
  try {
    // const eventSourceMappings = event.cdcStreams.map((stream: { cdcFunctionName: string; collectionName: string }) =>
    //   lambdaClient.send(
    //     new CreateEventSourceMappingCommand({
    //       FunctionName: stream.cdcFunctionName,
    //       EventSourceArn: event.clusterArn,
    //       BatchSize: 100,
    //       StartingPosition: 'AT_TIMESTAMP',
    //       StartingPositionTimestamp: new Date(),
    //       SourceAccessConfigurations: [{ Type: 'BASIC_AUTH', URI: event.authUri }],
    //       DocumentDBEventSourceConfig: {
    //         DatabaseName: event.databaseName,
    //         CollectionName: stream.collectionName,
    //         FullDocument: 'UpdateLookup',
    //       },
    //     })
    //   )
    // );

    // const responses = await Promise.all(eventSourceMappings);

    const command = new CreateEventSourceMappingCommand({
      FunctionName: 'DocumentDbStreamLambdaEve-ProductsCdcLambda99D0665-lFE5awQFpaNO',
      EventSourceArn: 'arn:aws:rds:us-east-2:640999649296:cluster:docdbcluster',
      BatchSize: 100,
      StartingPosition: 'LATEST',
      SourceAccessConfigurations: [
        { Type: 'BASIC_AUTH', URI: 'arn:aws:secretsmanager:us-east-2:640999649296:secret:DocumentDBSecret-HMIA1G' },
      ],
      DocumentDBEventSourceConfig: {
        DatabaseName: 'docdb',
        CollectionName: 'products',
        FullDocument: 'UpdateLookup',
      },
    });
    const responses = await lambdaClient.send(command);
    console.log('Responses:', JSON.stringify(responses, null, 2));
    // const errors = responses.filter(
    //   (response) => response.status === 'rejected' && response.reason.name !== 'ResourceConflictException'
    // );
    // if (errors.length > 0) {
    //   const errorsMessages = errors.map((error) => {
    //     if (error.status === 'rejected') {
    //       return error?.reason.name;
    //     }
    //   });
    //   throw new Error(errorsMessages.join(','));
    // }
    return {
      PhysicalResourceId: '-' + new Date().toISOString(),
    };
  } catch (error: any) {
    console.error('Error in enabling CDC:', error);
    throw error;
  }
};

export const main = enableCdcCr;
