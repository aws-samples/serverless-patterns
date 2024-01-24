import * as cdk from 'aws-cdk-lib';
import { AuthorizationType, FieldLogLevel, GraphqlApi, SchemaFile } from 'aws-cdk-lib/aws-appsync';
import { EventBus, Rule } from 'aws-cdk-lib/aws-events';
import { Effect, Policy, PolicyStatement, Role, ServicePrincipal } from 'aws-cdk-lib/aws-iam';
import { Construct } from 'constructs';
import { join } from 'path';
import { } from 'aws-cdk-lib/aws-events-targets';

export class EventbridgeToAppsyncStack extends cdk.Stack {
  constructor(scope: Construct, id: string, props?: cdk.StackProps) {
    super(scope, id, props);

    // Define the event bus
    const eventBus = new EventBus(this, 'bus', {
      eventBusName: 'AppSyncEventBus',
    });

    const api = new GraphqlApi(this, 'Api', {
      name: 'AppSyncEventBridgeAPI',
      schema: SchemaFile.fromAsset(join(__dirname, '../graphql/schema.graphql')),
      authorizationConfig: {
        defaultAuthorization: {
          authorizationType: AuthorizationType.IAM,
        },
      },
      logConfig: {
        excludeVerboseContent: false,
        fieldLogLevel: FieldLogLevel.ALL,
      },
    });

    const role = new Role(this, 'test', {
      assumedBy: new ServicePrincipal('events.amazonaws.com'),
    });

    new Policy(this, 'stest', {
      policyName: 'EventBridgeToAppSync',
      roles: [role],
      statements: [
        new PolicyStatement({
          effect: Effect.ALLOW,
          actions: ['appsync:GraphQL'],
          resources: [api.arn],
        }),
      ],
    });

     // EventBridge rule to listen to UserCreated so we can process it and create schedule
     const rule = new Rule(this, 'EventBridgeToAppSyncRule', {
      description: 'Connect AppSync to EventBridge events',

      // chanage this to your desired pattern
      eventPattern: {
        source: ['myapp.users'],
        detailType: ['UserCreated'],
      },
      eventBus,
    });

    rule.node.defaultChild?.node.addDependency()


    // The code that defines your stack goes here

    // example resource
    // const queue = new sqs.Queue(this, 'EventbridgeToAppsyncQueue', {
    //   visibilityTimeout: cdk.Duration.seconds(300)
    // });
  }
}
