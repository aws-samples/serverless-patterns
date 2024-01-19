import * as cdk from 'aws-cdk-lib';
import { Construct } from 'constructs';
import * as events from 'aws-cdk-lib/aws-events';
import * as targets from 'aws-cdk-lib/aws-events-targets';
import * as logs from 'aws-cdk-lib/aws-logs';
import * as iam from 'aws-cdk-lib/aws-iam';
import * as pipes from 'aws-cdk-lib/aws-pipes';
import * as lambda from 'aws-cdk-lib/aws-lambda';
import * as dynamodb from 'aws-cdk-lib/aws-dynamodb';
import { NodejsFunction } from 'aws-cdk-lib/aws-lambda-nodejs';
import * as path from 'path';
import { CfnScheduleGroup } from 'aws-cdk-lib/aws-scheduler';
import { LambdaTarget } from 'aws-cdk-lib/aws-elasticloadbalancingv2-targets';

export class DynamicEventBridgeSchedulesStack extends cdk.Stack {
  constructor(scope: Construct, id: string, props?: cdk.StackProps) {
    super(scope, id, props);

    // The DynamoDB table for users
    const usersTable = new dynamodb.Table(this, 'usersTable', {
      tableName: 'ServerlessLandUsers',
      partitionKey: {
        name: 'userId',
        type: dynamodb.AttributeType.STRING,
      },
      removalPolicy: cdk.RemovalPolicy.DESTROY,
      stream: dynamodb.StreamViewType.NEW_IMAGE,
    });

    // Event Bus used for application
    const eventBus = new events.EventBus(this, 'ServerlessLandEventBus', {
      eventBusName: 'ServerlessLandEventBus',
    });

    // Schedule group for all the user schedules
    const userScheduleGroup = new CfnScheduleGroup(this, 'UserScheduleGroup', {
      name: 'UserScheduleGroup',
    });

    // Example function that would be the email service.
    const emailService: NodejsFunction = new NodejsFunction(this, 'email-service', {
      memorySize: 1024,
      timeout: cdk.Duration.seconds(5),
      runtime: lambda.Runtime.NODEJS_18_X,
      handler: 'handler',
      entry: path.join(__dirname, '../src/email-service/index.ts'),
    });

    const scheduleRole = new iam.Role(this, 'scheduleRole', {
      assumedBy: new iam.ServicePrincipal('scheduler.amazonaws.com'),
    });

    emailService.grantInvoke(scheduleRole);

    // Example function that will create schedules for users
    const scheduleCreator: NodejsFunction = new NodejsFunction(this, 'schedule-creator', {
      memorySize: 1024,
      timeout: cdk.Duration.seconds(5),
      runtime: lambda.Runtime.NODEJS_18_X,
      handler: 'handler',
      entry: "./src/schedule-creator/index.ts",
      bundling: {
        nodeModules: ['@aws-sdk/client-scheduler']
      },
      environment: {
        SCHEDULE_GROUP_NAME: userScheduleGroup.name || '',
        EMAIL_SERVICE_ARN: emailService.functionArn,
        SCHEDULE_ROLE_ARN: scheduleRole.roleArn
      },
      initialPolicy: [
        // Give lambda permission to create group, schedule and pass IAM role to the scheduler
        new iam.PolicyStatement({
          // actions: ['scheduler:CreateSchedule', 'iam:PassRole', 'scheduler:CreateScheduleGroup'],
          actions: ['scheduler:CreateSchedule', 'iam:PassRole'],
          resources: ['*'],
        }),
      ],
    });

    // CloudWatch Log group to catch all events through this event bus, for debugging.
    new events.Rule(this, 'catchAllLogRule', {
      ruleName: 'catch-all',
      eventBus: eventBus,
      eventPattern: {
        source: events.Match.prefix(''),
      },
      targets: [
        new targets.CloudWatchLogGroup(
          new logs.LogGroup(this, 'ServerlessLandEventBusAllEvents', {
            logGroupName: '/aws/events/ServerlessLandEventBus/logs',
            removalPolicy: cdk.RemovalPolicy.DESTROY,
          })
        ),
      ],
    });

    // Create a rule. Listen for event and trigger lambda to create schedule
    new events.Rule(this, 'create-schedules', {
      ruleName: 'create-schedules-on-new-user',
      eventBus: eventBus,
      eventPattern: {
        source: events.Match.exactString('serverlessland.users'),
        detailType: events.Match.exactString('NewUserCreated'),
      },
      targets: [
        new targets.LambdaFunction(scheduleCreator)
      ]
    });

    const pipeRole = new iam.Role(this, 'pipeRole', {
      assumedBy: new iam.ServicePrincipal('pipes.amazonaws.com'),
    });

 

    usersTable.grantReadWriteData(scheduleCreator);
    usersTable.grantStreamRead(pipeRole);
    eventBus.grantPutEventsTo(pipeRole);

    // Create EventBridge Pipe, to connect new DynamoDB items to EventBridge.
    new pipes.CfnPipe(this, 'pipe', {
      roleArn: pipeRole.roleArn,
      source: usersTable.tableStreamArn!,
      sourceParameters: {
        dynamoDbStreamParameters: {
          startingPosition: 'LATEST',
          batchSize: 3,
        },
        filterCriteria: {
          filters: [
            {
              pattern: '{"eventName" : ["INSERT"] }',
            },
          ],
        },
      },
      target: eventBus.eventBusArn,
      targetParameters: {
        eventBridgeEventBusParameters: {
          detailType: 'NewUserCreated',
          source: 'serverlessland.users',
        },
        inputTemplate: '{"userId": <$.dynamodb.NewImage.userId.S>}',
      },
    });
  }
}
