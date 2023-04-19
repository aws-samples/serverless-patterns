import * as cdk from 'aws-cdk-lib';
import { RemovalPolicy } from 'aws-cdk-lib';
import { Construct } from 'constructs';
import { AwsIntegration, RestApi, PassthroughBehavior, MethodResponse } from 'aws-cdk-lib/aws-apigateway'
import { Effect, PolicyStatement, Role, ServicePrincipal} from 'aws-cdk-lib/aws-iam'
import { Stream } from 'aws-cdk-lib/aws-kinesis';

export class ApigwKinesisIntegrationStack extends cdk.Stack {
  constructor(scope: Construct, id: string, props?: cdk.StackProps) {
    super(scope, id, props);

      // Create Kinesis Data Stream
      const kinesis = new Stream(this, 'KinesisStream', {
        streamName: 'temp-stream'
      });
      kinesis.applyRemovalPolicy(RemovalPolicy.DESTROY);

      // RestApi
      const restApi = new RestApi(this, 'ApiKinesisRestApi')
      
      // Add a resource for Kinesis Streams
      const streamsResource = restApi.root.addResource('kinesis');

      // Role for API Gateway Service to Assume
      const integrationRole = new Role(this, 'ApiGatewayRole', {
        assumedBy: new ServicePrincipal('apigateway.amazonaws.com'),
      });

      integrationRole.addToPolicy(new PolicyStatement({ 
        effect: Effect.ALLOW,
        resources: ['*'],
        actions: ['kinesis:*'], 
      }));

      // Create GET Method to list Kinesis Data Streams
      const listStreamsMethod = streamsResource.addMethod(
        'GET',
        new AwsIntegration({
          service: 'kinesis',
          action: 'ListStreams',
          integrationHttpMethod: 'POST',
          options: {
            credentialsRole: integrationRole,
            passthroughBehavior: PassthroughBehavior.WHEN_NO_TEMPLATES,
            requestTemplates: {
              ['application/json']: JSON.stringify({}), 
            },
            integrationResponses: [
              {
                statusCode: '200',
              },
            ],
          },
        }),
      );

      const methodResponse: MethodResponse = {
        statusCode: '200'
      };

      listStreamsMethod.addMethodResponse(methodResponse);

      const getShardIteratorRequestTemplate = {
        'ShardId': "$input.params('shard-id')",
        'ShardIteratorType': 'TRIM_HORIZON',
        'StreamName': "$input.params('stream-name')",
      };

      const getShardIteratorMethodOptions = {
        requestParameters: {
          ['method.request.querystring.shard-id']: true,
        },
      };

      const singleStreamResource = streamsResource.addResource('{stream-name}');
      const shardIteratorResource = singleStreamResource.addResource('sharditerator');

      // Create GET Method to get a shard iterator on a stream
      const getShardIteratorMethod = shardIteratorResource.addMethod(
        'GET',
        new AwsIntegration({
          service: 'kinesis',
          action: 'GetShardIterator',
          integrationHttpMethod: 'POST',
          options: {
            credentialsRole: integrationRole,
            passthroughBehavior: PassthroughBehavior.WHEN_NO_TEMPLATES,
            requestParameters: {
              ['integration.request.querystring.shard-id']: 'method.request.querystring.shard-id',
            },
            requestTemplates: {
              ['application/json']: JSON.stringify(getShardIteratorRequestTemplate),
            },
            integrationResponses: [
              {
                statusCode: '200',
              },
            ],
          },
        }),
        getShardIteratorMethodOptions,
      );

      getShardIteratorMethod.addMethodResponse(methodResponse);
  }
}