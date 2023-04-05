import * as cdk from 'aws-cdk-lib';
import { Construct } from 'constructs';
import { CfnPipe } from 'aws-cdk-lib/aws-pipes';
import { EventBus } from 'aws-cdk-lib/aws-events';
import { Rule, Match } from 'aws-cdk-lib/aws-events';
import { Role, ServicePrincipal } from 'aws-cdk-lib/aws-iam';
import { AttributeType, BillingMode, StreamViewType, Table } from 'aws-cdk-lib/aws-dynamodb';
import { RemovalPolicy } from 'aws-cdk-lib';
import { LogGroup, RetentionDays } from 'aws-cdk-lib/aws-logs'
import { NodejsFunction } from 'aws-cdk-lib/aws-lambda-nodejs';
import { Runtime, StartingPosition } from 'aws-cdk-lib/aws-lambda';
import * as path from 'path';
import { CloudWatchLogGroup } from 'aws-cdk-lib/aws-events-targets';

export class EventBridgePipesSplitterPattern extends cdk.Stack {
  constructor(scope: Construct, id: string, props?: cdk.StackProps) {
    super(scope, id, props);

    // log group to see Splitter output
    const ticketLogGroup = new LogGroup(this, 'tickets-log', {
      logGroupName: '/aws/events/tickets',
      retention: RetentionDays.ONE_DAY,
      removalPolicy: RemovalPolicy.DESTROY
    });

    const ticketOrdersBus = new EventBus(this, 'ticket-orders', {
      eventBusName: 'ticket-orders',
    });

    // Rule that matches any incoming event and sends it to a logGroup
    const catchAll = new Rule(this, 'send-to-log', {
      eventBus: ticketOrdersBus,
      ruleName: 'catchall',
      eventPattern: {
        source:  Match.exists()
      },
      targets: [new CloudWatchLogGroup(ticketLogGroup)]
    } );

    const eventBridgeRole = new Role(this, 'events-role', {
      assumedBy: new ServicePrincipal('events.amazonaws.com'),
    });

    ticketLogGroup.grantWrite(eventBridgeRole);

    // table for the orders.
    const ordersTable = new Table(this, 'Orders-Table', {
      partitionKey: { name: 'id', type: AttributeType.STRING },
      billingMode: BillingMode.PAY_PER_REQUEST,
      removalPolicy: RemovalPolicy.DESTROY,
      tableName: 'Orders-Table',
      stream: StreamViewType.NEW_IMAGE,
    });

    // function used to split the order into seperate events.
    const splitterFunc: NodejsFunction = new NodejsFunction(this, 'lambda-function-splitter', {
      memorySize: 1024,
      runtime: Runtime.NODEJS_18_X,
      handler: 'handler',
      entry: path.join(__dirname, '../src', 'splitter.ts'),
    });

    const pipeRole = new Role(this, 'pipe-role', {
      assumedBy: new ServicePrincipal('pipes.amazonaws.com'),
    });

    ordersTable.grantStreamRead(pipeRole);
    ticketOrdersBus.grantPutEventsTo(pipeRole);
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
      target: ticketOrdersBus.eventBusArn,
      targetParameters: {
        eventBridgeEventBusParameters: {
          detailType: 'TicketPurchased',
          source: 'trains.tickets',
        },
      },
    });
  }
}
