import {
  aws_apigateway as apigw,
  aws_sqs as sqs,
  aws_iam as iam,
  CfnOutput as cfnOutput,
} from 'aws-cdk-lib';
import { Construct } from 'constructs';

export interface ApiGwSqsProps {

  /**
   * API Gateway object
   */
  readonly apiGateway? : apigw.IRestApi;

  /**
   * SQS Queue object
   */
  readonly sqsQueue? : sqs.IQueue;

}

/**
* To create an API Gateway that published requests to an SQS queue
*/
export class ApiGwSqsConstruct extends Construct {
  public customApiGateway: apigw.IRestApi;
  public customQueue: sqs.IQueue;

  constructor(scope: Construct, id: string, props: ApiGwSqsProps) {
    super(scope, id);

    // Create SQS queue;
    this.customQueue = props.sqsQueue ?? (new sqs.Queue(this, 'apigwSqs-queue', {queueName: 'MyCustomQueue'}))

    // Create IAM Role for API Gateway
    const integrationRole = new iam.Role(this, 'apigwSqs-integration-role', {
      assumedBy: new iam.ServicePrincipal('apigateway.amazonaws.com'),
    });

    // Grant sqs:SendMessage* to Api Gateway Role
    this.customQueue.grantSendMessages(integrationRole);

    // AWS Integration
    const apiGwSqsIntegration = new apigw.AwsIntegration({
      service: 'sqs',
      path: `${process.env.CDK_DEFAULT_ACCOUNT}/${this.customQueue.queueName}`,
      integrationHttpMethod: 'POST',
      options: {
        credentialsRole: integrationRole,
        requestParameters: {
          'integration.request.header.Content-Type': `'application/x-www-form-urlencoded'`,
        },
        requestTemplates: {
          'application/json': 'Action=SendMessage&MessageBody=$input.body',
        },
        integrationResponses: [
          {
            statusCode: '200',
          },
          {
            statusCode: '400',
          },
          {
            statusCode: '500',
          }
        ]
      },
    });

    // Create REST Api
    this.customApiGateway = props.apiGateway ?? (
      new apigw.RestApi(this, 'apigwSqs-restApi', {
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
        })
      );

      // Post method
      this.customApiGateway.root.addMethod('POST', apiGwSqsIntegration , {
          methodResponses: [
              {
              statusCode: '400',
              },
              { 
              statusCode: '200',
              },
              {
              statusCode: '500',
              }
          ]
      });

      new cfnOutput(this, 'ApiGatewayName', { value: this.customApiGateway.restApiName});
      new cfnOutput(this, 'SqsQueueName', { value: this.customQueue.queueName });
      new cfnOutput(this, 'SqsEndpoint', { value: this.customQueue.queueUrl});

  }
}