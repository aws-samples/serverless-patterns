import * as cdk from '@aws-cdk/core';
import { AwsIntegration, RestApi, PassthroughBehavior } from '@aws-cdk/aws-apigateway'
import { Table, BillingMode, AttributeType } from '@aws-cdk/aws-dynamodb'
import { Role, ServicePrincipal} from '@aws-cdk/aws-iam'

export class ApiDynamoStack extends cdk.Stack {
  constructor(scope: cdk.Construct, id: string, props?: cdk.StackProps) {
    super(scope, id, props);

    // DynamoDB Table
    const ddbTable = new Table(this, 'ApiDynamoTable', {
      partitionKey: {name:'pk', type: AttributeType.STRING},
      billingMode: BillingMode.PAY_PER_REQUEST,
      removalPolicy: cdk.RemovalPolicy.DESTROY,
    });

    // RestApi
    const restApi = new RestApi(this, 'ApiDynamoRestApi')
    const resource = restApi.root.addResource('{id}')

    // Allow the RestApi to access DynamoDb by assigning the integration this role
    const integrationRole = new Role(this, 'IntegrationRole', {
      assumedBy: new ServicePrincipal('apigateway.amazonaws.com'),
    })
    ddbTable.grantReadWriteData(integrationRole)

    // POST Integration to DynamoDb
    const dynamoPutIntegration = new AwsIntegration({
      service: 'dynamodb',
      action: 'PutItem',
      options: {
        passthroughBehavior: PassthroughBehavior.WHEN_NO_TEMPLATES,
        credentialsRole: integrationRole,
        requestTemplates: {
          'application/json': JSON.stringify({
              'TableName': ddbTable.tableName,
              'Item': {
                'pk': {'S': "$input.path('$.pk')"},
                'data': {'S': "$input.path('$.data')"},
              }
          }),
        },
        integrationResponses: [
          {
            statusCode: '200',
            responseTemplates: {
              'application/json': JSON.stringify({})
            }
          }
        ],
      }
    })
    resource.addMethod('POST', dynamoPutIntegration, {
      methodResponses: [{statusCode: '200'}],
    })

    // GET Integration with DynamoDb
    const dynamoQueryIntegration = new AwsIntegration({
      service: 'dynamodb',
      action: 'Query',
      options: {
        passthroughBehavior: PassthroughBehavior.WHEN_NO_TEMPLATES,
        credentialsRole: integrationRole,
        requestParameters: {
          'integration.request.path.id': 'method.request.path.id'
        },
        requestTemplates: {
          'application/json': JSON.stringify({
              'TableName': ddbTable.tableName,
              'KeyConditionExpression': 'pk = :v1',
              'ExpressionAttributeValues': {
                  ':v1': {'S': "$input.params('id')"}
              }
          }),
        },
        integrationResponses: [{ statusCode: '200' }],
      }
    })
    resource.addMethod('GET', dynamoQueryIntegration, {
      methodResponses: [{ statusCode: '200' }],
      requestParameters: {
        'method.request.path.id': true
      }
    })
  }
}
