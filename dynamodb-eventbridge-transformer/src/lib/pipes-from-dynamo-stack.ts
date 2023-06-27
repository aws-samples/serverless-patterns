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

    // the DynamoDB table that orders are written to
    const shoppingOrderTable = new dynamodb.Table(this, 'shoppingOrderTable', {
      partitionKey: {
        name: 'orderID',
        type: dynamodb.AttributeType.STRING
      },
      removalPolicy: cdk.RemovalPolicy.DESTROY,
      stream: dynamodb.StreamViewType.NEW_IMAGE
    });

    // the Lambda function that creates three sample orders for testing
    const sampleOrderCreationFunction = new lambda.Function(this, 'sampleOrderCreationFunction', {
      functionName: 'sampleOrderCreationFunction',
      runtime: lambda.Runtime.NODEJS_18_X,
      code: lambda.Code.fromAsset('lib/lambda'),
      handler: 'sampleOrderCreationFunction.handler',
      environment: {
        TABLE_NAME: shoppingOrderTable.tableName,
      }
    });

    const eventBus = new events.EventBus(this, 'pipesFromDynamoStackEventBus', {
      eventBusName: 'pipesFromDynamoStackEventBus'
    });

    // All events on the eventBus are written to Amazon CloudWatch Logs for visualization
    const catchAllLogRule = new events.Rule(this, 'catchAllLogRule', {
      ruleName: 'catchAllLogRule',
      eventBus: eventBus,
      eventPattern: {
        source: events.Match.prefix(''),
      },
      targets: [new targets.CloudWatchLogGroup(new logs.LogGroup(this, 'PipesFromDynamoStackLogGroup', {
        logGroupName: '/aws/events/pipesFromDynamoStackLogGroup/catchallLogGroup',
        removalPolicy: cdk.RemovalPolicy.DESTROY,
      }))],
    });

    const pipeRole = new iam.Role(this, 'pipeRole', {
      assumedBy: new iam.ServicePrincipal('pipes.amazonaws.com'),
    });

    shoppingOrderTable.grantReadWriteData(sampleOrderCreationFunction);
    shoppingOrderTable.grantStreamRead(pipeRole);
    eventBus.grantPutEventsTo(pipeRole);

    const newAndModifiedOrdersPipe = new pipes.CfnPipe(this, 'pipe', {
      roleArn: pipeRole.roleArn,
      source: shoppingOrderTable.tableStreamArn!,
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
      target: eventBus.eventBusArn,
      targetParameters: {
        inputTemplate: '{"orderID": <$.dynamodb.NewImage.orderID.S>, "Items": <$.dynamodb.NewImage.Items.L[*].S>}',
      }
    });
  }
}

