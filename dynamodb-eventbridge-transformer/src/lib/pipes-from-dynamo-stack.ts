import * as cdk from 'aws-cdk-lib';
import { Construct } from 'constructs';
import * as events from 'aws-cdk-lib/aws-events';
import * as targets from 'aws-cdk-lib/aws-events-targets';
import * as logs from 'aws-cdk-lib/aws-logs';
import * as iam from 'aws-cdk-lib/aws-iam';
import * as pipes from 'aws-cdk-lib/aws-pipes';
import * as lambda from 'aws-cdk-lib/aws-lambda';
import * as dynamodb from 'aws-cdk-lib/aws-dynamodb';

export class PipesFromDynamoStack extends cdk.Stack {
  constructor(scope: Construct, id: string, props?: cdk.StackProps) {
    super(scope, id, props);

    //dynamodb table "dataOrigin" with DynamoDB stream enabled
    const dataOriginTable = new dynamodb.Table(this, 'dataOriginTable', {
      partitionKey: {
        name: 'id',
        type: dynamodb.AttributeType.STRING
      },
      removalPolicy: cdk.RemovalPolicy.DESTROY,
      stream: dynamodb.StreamViewType.NEW_IMAGE
    });

    // lambda function to write to dynamodb 
    const writeDemoData = new lambda.Function(this, 'writeDemoData', {
      functionName: 'writeDemoData',
      runtime: lambda.Runtime.NODEJS_18_X,
      code: lambda.Code.fromAsset('lib/lambda'),
      handler: 'writeDemoData.handler',
      environment: {
        TABLE_NAME: dataOriginTable.tableName,
      }
    });

    // target event bus
    const targetEventBus = new events.EventBus(this, 'targetEventBus', {
      eventBusName: 'targetEventBus'
    });

    // create an Amazon EventBridge rule to send all events to Amazon CloudWatch Logs:
    const targetLogRule = new events.Rule(this, 'targetLogRule', {
      ruleName: 'targetLogRule',
      eventBus: targetEventBus,
      eventPattern: {
        source: events.Match.prefix(''),
      },
      targets: [new targets.CloudWatchLogGroup(new logs.LogGroup(this, 'TargetLogGroup', {
        logGroupName: '/aws/events/targetLog',
        removalPolicy: cdk.RemovalPolicy.DESTROY,
      }))],
    });

    const pipeRole = new iam.Role(this, 'pipeRole', {
      assumedBy: new iam.ServicePrincipal('pipes.amazonaws.com'),
    });

    dataOriginTable.grantReadWriteData(writeDemoData);
    dataOriginTable.grantStreamRead(pipeRole);
    targetEventBus.grantPutEventsTo(pipeRole);

    // create an EventBridge Pipe that streams data from dataOriginTable to targetEventBus
     const pipe = new pipes.CfnPipe(this, 'pipe', {
      roleArn: pipeRole.roleArn,
      source: dataOriginTable.tableStreamArn!,
      target: targetEventBus.eventBusArn,
      sourceParameters: {
        dynamoDbStreamParameters: {
          startingPosition: 'LATEST',
          batchSize: 3,
        },
        filterCriteria: {
          filters: [{
            pattern: '{"eventName" : ["INSERT", "MODIFY"] }',
          }],
        },
      },
      targetParameters: {
        inputTemplate: '{"id": <$.dynamodb.NewImage.id.S>, "list": <$.dynamodb.NewImage.list.L[*].S>}',
      }
    });
  }
}

