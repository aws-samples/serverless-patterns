import * as cdk from 'aws-cdk-lib';
import { Duration } from 'aws-cdk-lib';
import { AttributeType, BillingMode, StreamViewType, Table } from 'aws-cdk-lib/aws-dynamodb';
import { EventBus, Rule } from 'aws-cdk-lib/aws-events';
import { LambdaFunction } from 'aws-cdk-lib/aws-events-targets';
import { Runtime, StartingPosition } from 'aws-cdk-lib/aws-lambda';
import { DynamoEventSource } from 'aws-cdk-lib/aws-lambda-event-sources';
import { NodejsFunction } from 'aws-cdk-lib/aws-lambda-nodejs';
import { Construct } from 'constructs';
import * as path from 'path';

export class EventbridgeOutboxPatternWithDdbStack extends cdk.Stack {
  constructor(scope: Construct, id: string, props?: cdk.StackProps) {
    super(scope, id, props);

    const eventBus = new EventBus(this, 'MainBus', {
      eventBusName: 'MyMainBus',
    });

    // DDB table that stores information
    const userTable = new Table(this, 'UsersTable', {
      billingMode: BillingMode.PAY_PER_REQUEST,
      removalPolicy: cdk.RemovalPolicy.DESTROY,
      partitionKey: { name: 'id', type: AttributeType.STRING },
      stream: StreamViewType.NEW_IMAGE,
    });

    // Example function that will write to DDB
    const writeToDDBFunction: NodejsFunction = new NodejsFunction(this, 'write-to-ddb', {
      memorySize: 1024,
      timeout: Duration.seconds(5),
      runtime: Runtime.NODEJS_16_X,
      handler: 'handler',
      entry: path.join(__dirname, '../src/write-to-ddb/index.ts'),
      environment: {
        TABLE_NAME: userTable.tableName,
      },
    });

    userTable.grantWriteData(writeToDDBFunction);

    // Event source function that reads the data capture change events and forwards them to eventbridge
    const streamToEventBridge: NodejsFunction = new NodejsFunction(this, 'streamToEventBridge', {
      memorySize: 1024,
      timeout: Duration.seconds(5),
      runtime: Runtime.NODEJS_16_X,
      handler: 'handler',
      entry: path.join(__dirname, '../src/ddb-stream-into-eventbridge-events/index.ts'),
      environment: {
        TABLE_NAME: userTable.tableName,
        EVENT_BUS_NAME: eventBus.eventBusName
      },
    });

    // grant processor put events access
    eventBus.grantPutEventsTo(streamToEventBridge);

    // stream change events to the lambda function
    streamToEventBridge.addEventSource(
      new DynamoEventSource(userTable, {
        startingPosition: StartingPosition.LATEST,
        batchSize: 10,
      })
    );

    // Example consumer for the UserCreated event.
    const userCreatedConsumer: NodejsFunction = new NodejsFunction(this, 'userCreatedConsumer', {
      memorySize: 1024,
      timeout: Duration.seconds(5),
      runtime: Runtime.NODEJS_16_X,
      handler: 'handler',
      entry: path.join(__dirname, '../src/consumers/user-created/index.ts')
    });

    // Rule to match UserCreated events for consumer
    new Rule(this, 'UserCreatedRule', {
      description: 'Listen to all UserCreated events',
      eventPattern: {
        source: ['myapp.users'],
        detailType: ['UserCreated']
      },
      eventBus,
    }).addTarget(new LambdaFunction(userCreatedConsumer));

  }
}
