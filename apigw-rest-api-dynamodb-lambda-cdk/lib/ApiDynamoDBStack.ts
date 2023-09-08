import { RemovalPolicy, Stack, StackProps } from 'aws-cdk-lib';
import { AwsIntegration, Cors, RestApi } from 'aws-cdk-lib/aws-apigateway';
import { Table, BillingMode, AttributeType, StreamViewType } from 'aws-cdk-lib/aws-dynamodb';
import { Effect, Policy, PolicyStatement, Role, ServicePrincipal } from 'aws-cdk-lib/aws-iam';
import { Construct } from 'constructs';
import * as lambda from "aws-cdk-lib/aws-lambda";
import { DynamoEventSource } from 'aws-cdk-lib/aws-lambda-event-sources';
import * as path from 'path';

export class ApiDynamoDBStack extends Stack {
  constructor(scope: Construct, id: string, props?: StackProps) {
    super(scope, id, props);

    const modelName = 'AWSomeDynamoDB';
    const dynamoDBTable = new Table(this, modelName, {
      billingMode: BillingMode.PAY_PER_REQUEST,
      partitionKey: {
        name:`${modelName}Id`,
        type: AttributeType.STRING
      },
      removalPolicy: RemovalPolicy.DESTROY,
      tableName: modelName,
      stream: StreamViewType.NEW_AND_OLD_IMAGES
    });
    
    const lambdaFunction = new lambda.Function(this, 'Function', {
      code: lambda.Code.fromAsset(path.join(__dirname, '../src')),
      handler: 'messageHandler.lambda_handler',
      functionName: 'TableStreamHandler',
      runtime: lambda.Runtime.PYTHON_3_10,
    });

    lambdaFunction.addEventSource(new DynamoEventSource(dynamoDBTable, {
      startingPosition: lambda.StartingPosition.LATEST,
    }));

    dynamoDBTable.grantStreamRead(lambdaFunction);

    const getPolicy = new Policy(this, 'getPolicy', {
      statements: [
        new PolicyStatement({
          actions: ['dynamodb:GetItem'],
          effect: Effect.ALLOW,
          resources: [dynamoDBTable.tableArn],
        }),
      ],
    });

    const putPolicy = new Policy(this, 'putPolicy', {
      statements: [
        new PolicyStatement({
          actions: ['dynamodb:PutItem'],
          effect: Effect.ALLOW,
          resources: [dynamoDBTable.tableArn],
        }),
      ],
    });

    const scanPolicy = new Policy(this, 'scanPolicy', {
      statements: [
        new PolicyStatement({
          actions: ['dynamodb:Scan'],
          effect: Effect.ALLOW,
          resources: [dynamoDBTable.tableArn],
        }),
      ],
    });

    const api = new RestApi(this, `${modelName}Api`,{
      defaultCorsPreflightOptions:{
        allowOrigins: Cors.ALL_ORIGINS
      },
      restApiName:`${modelName} Service`
    })
   
    const getRole = new Role(this, 'getRole', {
      assumedBy: new ServicePrincipal('apigateway.amazonaws.com'),
    });
    getRole.attachInlinePolicy(getPolicy);

    const putRole = new Role(this, 'putRole', {
      assumedBy: new ServicePrincipal('apigateway.amazonaws.com'),
    });
    putRole.attachInlinePolicy(putPolicy);

    const scanRole = new Role(this, 'scanRole', {
      assumedBy: new ServicePrincipal('apigateway.amazonaws.com'),
    });
    scanRole.attachInlinePolicy(scanPolicy);


    const errorResponses = [
      {
        selectionPattern: '400',
        statusCode: '400',
        responseTemplates: {
          'application/json': `{
            "error": "Bad input!"
          }`,
        },
      },
      {
        selectionPattern: '5\\d{2}',
        statusCode: '500',
        responseTemplates: {
          'application/json': `{
            "error": "Internal Service Error!"
          }`,
        },
      },
    ];

    const integrationResponses = [
      {
        statusCode: '200',
      },
      ...errorResponses,
    ];

    const getIntegration = new AwsIntegration({
      action: 'GetItem',
      options: {
        credentialsRole: getRole,
        integrationResponses,
        requestTemplates: {
          'application/json': `{
              "Key": {
                "${modelName}Id": {
                  "S": "$method.request.path.id"
                }
              },
              "TableName": "${modelName}"
            }`,
        },
      },
      service: 'dynamodb',
    });

    const createIntegration = new AwsIntegration({
      action: 'PutItem',
      options: {
        credentialsRole: putRole,
        integrationResponses: [
          {
            statusCode: '200',
            responseTemplates: {
              'application/json': `{
                "requestId": "$context.requestId"
              }`,
            },
          },
          ...errorResponses,
        ],
        requestTemplates: {
          'application/json': `{
              "Item": {
                "${modelName}Id": {
                  "S": "$context.requestId"
                },
                "Name": {
                  "S": "$input.path('$.name')"
                },
                "Description": {
                  "S": "$input.path('$.description')"
                },
                "Customer": {
                  "S": "$input.path('$.customer')"
                },
                "Id": {
                  "S": "$input.path('$.id')"
                }
              },
              "TableName": "${modelName}"
            }`,
        },
      },
      service: 'dynamodb',
    });

    const getAllIntegration = new AwsIntegration({
      action: 'Scan',
      options: {
        credentialsRole: scanRole,
        integrationResponses,
        requestTemplates: {
          'application/json': `{
              "TableName": "${modelName}"
            }`,
        },
      },
      service: 'dynamodb',
    });

    const methodOptions = { methodResponses: [{ statusCode: '200' }, { statusCode: '400' }, { statusCode: '500' }] };
    const allResources = api.root.addResource(modelName.toLocaleLowerCase());
    const oneResource = allResources.addResource('{id}');

    allResources.addMethod('GET', getAllIntegration, methodOptions);
    allResources.addMethod('POST', createIntegration, methodOptions);
    oneResource.addMethod('GET', getIntegration, methodOptions);
  }
}
