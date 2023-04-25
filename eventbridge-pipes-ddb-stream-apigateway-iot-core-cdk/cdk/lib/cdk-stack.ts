import * as cdk from 'aws-cdk-lib';
import { RestApi, EndpointType, AwsIntegration } from 'aws-cdk-lib/aws-apigateway';
import { AttributeType, BillingMode, StreamViewType, Table } from 'aws-cdk-lib/aws-dynamodb';
import { EventBus } from 'aws-cdk-lib/aws-events';
import { Role, ServicePrincipal } from 'aws-cdk-lib/aws-iam';
import { StartingPosition } from 'aws-cdk-lib/aws-lambda';
import { CfnPipe } from 'aws-cdk-lib/aws-pipes';
import { AwsCustomResource, PhysicalResourceId, AwsCustomResourcePolicy } from 'aws-cdk-lib/custom-resources';
import { Construct } from 'constructs';

export interface EventBridgePipesIotCoreStackProps extends cdk.StackProps {
  iotTopicName: string;
  dynamoDbTableName: string;
  apiGateway: {
    restApiName: string;
    apiResource: string;
  };
  pipeName: string;
}
export class EventBridgePipesIotCoreStack extends cdk.Stack {
  constructor(scope: Construct, id: string, props?: EventBridgePipesIotCoreStackProps) {
    super(scope, id, props);

    // The code that defines your stack goes here
    const eventsTable = new Table(this, 'Iot-Table', {
      tableName: props?.dynamoDbTableName,
      partitionKey: { name: 'pk', type: AttributeType.STRING },
      sortKey: { name: 'sk', type: AttributeType.STRING },
      billingMode: BillingMode.PAY_PER_REQUEST,
      removalPolicy: cdk.RemovalPolicy.DESTROY,
      stream: StreamViewType.NEW_AND_OLD_IMAGES,
    });

    // default event bus
    const defaultEventBus = EventBus.fromEventBusName(this, 'Default-Event-Bus', 'default');

    const iotTopicApi = new RestApi(this, 'Iot-Rest-Api', {
      restApiName: props?.apiGateway.restApiName,
      endpointTypes: [EndpointType.REGIONAL],
      defaultCorsPreflightOptions: { allowOrigins: ['*'] },
      deployOptions: {
        stageName: 'dev',
      },
    });

    const getIoTEndpoint = new AwsCustomResource(this, 'IoT-Endpoint', {
      onCreate: {
        service: 'Iot',
        action: 'describeEndpoint',
        physicalResourceId: PhysicalResourceId.fromResponse('endpointAddress'),
        parameters: {
          endpointType: 'iot:Data-ATS',
        },
      },
      policy: AwsCustomResourcePolicy.fromSdkCalls({ resources: AwsCustomResourcePolicy.ANY_RESOURCE }),
    });

    const IOT_DATA_ENDPOINT = getIoTEndpoint.getResponseField('endpointAddress');

    const iotTopicApiEndpoint = iotTopicApi.root.addResource(props?.apiGateway.apiResource!);
    const iotTopicEndpointSubdomain = IOT_DATA_ENDPOINT.split('.')[0];
    const iotServiceIntegration = new AwsIntegration({
      service: 'iotdata',
      proxy: false,
      subdomain: iotTopicEndpointSubdomain,
      path: `topics/${props?.iotTopicName}`,
      integrationHttpMethod: 'POST',
      options: {
        credentialsRole: new Role(this, 'Iot-Topic-Endpoint-Role', {
          assumedBy: new ServicePrincipal('apigateway.amazonaws.com'),
          managedPolicies: [
            { managedPolicyArn: 'arn:aws:iam::aws:policy/AWSIoTDataAccess' },
            { managedPolicyArn: 'arn:aws:iam::aws:policy/service-role/AmazonAPIGatewayPushToCloudWatchLogs' },
          ],
        }),
        integrationResponses: [
          {
            statusCode: '200',
            responseParameters: { 'method.response.header.Content-Type': 'integration.response.header.Content-Type' },
          },
        ],
      },
    });
    const methodResponses = [
      {
        statusCode: '200',
        responseParameters: {
          'method.response.header.Content-Type': true,
        },
      },
    ];
    iotTopicApiEndpoint.addMethod('POST', iotServiceIntegration, { methodResponses });

    const pipeRole = new Role(this, 'Events-Role', {
      assumedBy: new ServicePrincipal('pipes.amazonaws.com'),
    });

    eventsTable.grantStreamRead(pipeRole);
    defaultEventBus.grantPutEventsTo(pipeRole);

    const { account, region } = cdk.Stack.of(this);
    const apiStage = iotTopicApi.deploymentStage.stageName;
    const apiId = iotTopicApi.restApiId;
    const apiMethod = 'POST';
    const apiPath = props?.apiGateway.apiResource;
    const targetEndpointArn = `arn:aws:execute-api:${region}:${account}:${apiId}/${apiStage}/${apiMethod}/${apiPath}`;
    // Create new Pipe
    const eventsPipe = new CfnPipe(this, 'Events-Pipe', {
      name: props?.pipeName,
      roleArn: pipeRole.roleArn,
      //@ts-ignore
      source: eventsTable.tableStreamArn,
      sourceParameters: {
        dynamoDbStreamParameters: {
          startingPosition: StartingPosition.LATEST,
          batchSize: 1,
        },
        filterCriteria: {
          filters: [
            {
              pattern: '{"eventName" : ["INSERT", "MODIFY"] }',
            },
          ],
        },
      },
      target: targetEndpointArn,
    });

    new cdk.CfnOutput(this, 'IotDataEndpoint', {
      value: IOT_DATA_ENDPOINT,
    });
    new cdk.CfnOutput(this, 'IotTopicName', {
      value: props?.iotTopicName!,
    });

    new cdk.CfnOutput(this, 'DynamoDBTableName', {
      value: eventsTable.tableName,
    });
  }
}
