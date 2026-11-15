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

      // Add a resource for operations on a specific Kinesis Stream
      const singleStreamResource = streamsResource.addResource('{stream-name}');
      const shardIteratorResource = singleStreamResource.addResource('sharditerator');
      const recordsResource = singleStreamResource.addResource('records');

      // Create GET method and related resources to get a shard iterator on a stream

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

      // Create GET method and related resources to get records from a stream

      const getRecordsRequestTemplate = {
        'ShardIterator': "$input.params('Shard-Iterator')",
      };

      const getRecordsMethodOptions = {
        requestParameters: {
          ['method.request.header.Shard-Iterator']: true,
        },
      };

      const getRecordsMethod = recordsResource.addMethod(
        'GET',
        new AwsIntegration({
          service: 'kinesis',
          action: 'GetRecords',
          integrationHttpMethod: 'POST',
          options: {
            credentialsRole: integrationRole,
            passthroughBehavior: PassthroughBehavior.WHEN_NO_TEMPLATES,
            requestParameters: {
              ['integration.request.header.Shard-Iterator']: 'method.request.header.Shard-Iterator',
            },
            requestTemplates: {
              ['application/json']: JSON.stringify(getRecordsRequestTemplate),
            },
            integrationResponses: [
              {
                statusCode: '200',
              },
            ],
          },
        }),
        getRecordsMethodOptions,
      );

      getRecordsMethod.addMethodResponse(methodResponse);
          
      // Create PUT method and related resources to put 1 record from a stream

      const putRecordRequestTemplate = {
        "StreamName": "$input.params('stream-name')",
        "Data": "$util.base64Encode($input.json('$.Data'))",
        "PartitionKey": "$input.path('$.PartitionKey')",
      };

      const putRecordMethodOptions = {
        requestParameters: {
          ['method.request.header.Content-Type']: true,
        },
      };

      const putRecordMethod = recordsResource.addMethod(
        'PUT',
        new AwsIntegration({
          service: 'kinesis',
          action: 'PutRecord',
          integrationHttpMethod: 'POST',
          options: {
            credentialsRole: integrationRole,
            passthroughBehavior: PassthroughBehavior.WHEN_NO_TEMPLATES,
            requestParameters: {
              ['integration.request.header.Content-Type']: 'method.request.header.Content-Type',
            },
            requestTemplates: {
              ['application/json']: JSON.stringify(putRecordRequestTemplate),
            },
            integrationResponses: [
              {
                statusCode: '200',
              },
            ],
          },
        }),
        putRecordMethodOptions,
      );

      putRecordMethod.addMethodResponse(methodResponse);
  }
}
