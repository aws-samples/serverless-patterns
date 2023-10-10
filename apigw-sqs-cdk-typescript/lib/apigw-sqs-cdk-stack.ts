import * as cdk from 'aws-cdk-lib';
import { Construct } from 'constructs';
import * as apigwsqs from './apigw-sqs';

export class ApigwSqsCdkStack extends cdk.Stack {
  constructor(scope: Construct, id: string, props?: cdk.StackProps) {
    super(scope, id, props);

    // Create custom sqs queue
    const customQueue = new cdk.aws_sqs.Queue(this, 'apigwSqs-queue', {
      queueName: 'MyQueueName',
    });

    // Create custom api gateway
    const customApiGateway = new cdk.aws_apigateway.RestApi(this, 'apigwSqs-restApi', {
      description: 'APIGW-SQS REST API Gateway',
      deployOptions: {
        stageName: 'dev',
      },
      // Enable CORS
      defaultCorsPreflightOptions: {
        allowHeaders: [
          'Content-Type',
          'X-Amz-Date',
          'Authorization',
          'X-Api-Key',
        ],
        allowMethods: ['OPTIONS', 'GET', 'POST', 'PUT', 'PATCH', 'DELETE'],
        allowOrigins: ['*'],
      },
    });

    // Integrate api gateway and sqs queue
    new apigwsqs.ApiGwSqsConstruct(this, 'apiGwSqs', {
      apiGateway: customApiGateway,
      sqsQueue: customQueue
    })
  }
}
