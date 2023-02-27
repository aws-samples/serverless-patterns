import * as cdk from 'aws-cdk-lib';
import { Construct } from 'constructs';
import { CfnPipe } from 'aws-cdk-lib/aws-pipes';
import { EventBus } from 'aws-cdk-lib/aws-events';
import { Role, ServicePrincipal } from 'aws-cdk-lib/aws-iam';
import { AttributeType, BillingMode, StreamViewType, Table } from 'aws-cdk-lib/aws-dynamodb';
import { RemovalPolicy } from 'aws-cdk-lib';
import { NodejsFunction } from 'aws-cdk-lib/aws-lambda-nodejs';
import { Runtime, StartingPosition } from 'aws-cdk-lib/aws-lambda';
import * as path from 'path';

export class EventBridgePipesSplitterPattern extends cdk.Stack {
  constructor(scope: Construct, id: string, props?: cdk.StackProps) {
    super(scope, id, props);

    const tickerOrdersBus = new EventBus(this, 'ticket-orders', {
      eventBusName: 'ticket-orders',
    });

    // table for the orders.
    const ordersTable = new Table(this, 'Orders-Table', {
      partitionKey: { name: 'id', type: AttributeType.STRING },
      billingMode: BillingMode.PAY_PER_REQUEST,
      removalPolicy: RemovalPolicy.DESTROY,
      tableName: 'Orders-Table',
      stream: StreamViewType.NEW_IMAGE,
    });

    // function used to split the order into seperate events.
    const splitterFunc: NodejsFunction = new NodejsFunction(this, 'scheduled-lambda-function', {
      memorySize: 1024,
      runtime: Runtime.NODEJS_18_X,
      handler: 'handler',
      entry: path.join(__dirname, '../src', 'splitter.ts'),
    });

    const pipeRole = new Role(this, 'role', {
      assumedBy: new ServicePrincipal('pipes.amazonaws.com'),
    });

    ordersTable.grantStreamRead(pipeRole);
    tickerOrdersBus.grantPutEventsTo(pipeRole);
    splitterFunc.grantInvoke(pipeRole);

    // Create new Pipe
    const pipe = new CfnPipe(this, 'pipe', {
      roleArn: pipeRole.roleArn,
      //@ts-ignore
      source: ordersTable.tableStreamArn,
      sourceParameters: {
        dynamoDbStreamParameters: {
          startingPosition: StartingPosition.LATEST,
          batchSize: 1,
        },
        filterCriteria: {
          filters: [
            {
              pattern: '{"eventName" : ["INSERT"] }',
            },
          ],
        },
      },
      enrichment: splitterFunc.functionArn,
      target: tickerOrdersBus.eventBusArn,
      targetParameters: {
        eventBridgeEventBusParameters: {
          detailType: 'TicketPurchased',
          source: 'trains.tickets',
        },
      },
    });
  }
}
