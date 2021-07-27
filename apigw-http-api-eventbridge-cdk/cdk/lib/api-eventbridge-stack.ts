import * as cdk from '@aws-cdk/core';
import { EventBus, Rule } from '@aws-cdk/aws-events';
import { CfnIntegration, CfnRoute, HttpApi } from '@aws-cdk/aws-apigatewayv2';
import { Effect, PolicyStatement, Role, ServicePrincipal } from '@aws-cdk/aws-iam';
import { LogGroup } from '@aws-cdk/aws-logs';
import { CloudWatchLogGroup } from '@aws-cdk/aws-events-targets';


export class ApiEventbridgeStack extends cdk.Stack {
  constructor(scope: cdk.Construct, id: string, props?: cdk.StackProps) {
    super(scope, id, props);

    const eventBus = new EventBus(this, 'MyEventBus', {
      eventBusName: 'MyEventBus'
    });

    /* LOGGING */
    const eventLoggerRule = new Rule(this, "EventLoggerRule", {
      description: "Log all events",
      eventPattern: {
        region: [ "ap-southeast-2" ]
      },
      eventBus: eventBus
    });

    const logGroup = new LogGroup(this, 'EventLogGroup', {
      logGroupName: '/aws/events/MyEventBus',
    });

    eventLoggerRule.addTarget(new CloudWatchLogGroup(logGroup));
  

    /* API */
    const httpApi = new HttpApi(this, 'MyHttpApi');

    /* There's no Eventbridge integration available as CDK L2 yet, so we have to use L1 and create Role, Integration and Route */
    const apiRole = new Role(this, 'EventBridgeIntegrationRole', {
      assumedBy: new ServicePrincipal('apigateway.amazonaws.com'),
    });

    apiRole.addToPolicy(
      new PolicyStatement({
        effect: Effect.ALLOW,
        resources: [eventBus.eventBusArn],
        actions: ['events:PutEvents'],
      })
    );

    const eventbridgeIntegration = new CfnIntegration(
      this,
      'EventBridgeIntegration',
      {
        apiId: httpApi.httpApiId,
        integrationType: 'AWS_PROXY',
        integrationSubtype: 'EventBridge-PutEvents',
        credentialsArn: apiRole.roleArn,
        requestParameters: {
          Source: 'WebApp',
          DetailType: 'MyDetailType', 
          Detail: '$request.body.Detail',
          EventBusName: eventBus.eventBusArn,
        },
        payloadFormatVersion: '1.0',
        timeoutInMillis: 10000,
      }
    );

    new CfnRoute(this, 'EventRoute', {
      apiId: httpApi.httpApiId,
      routeKey: 'POST /',
      target: `integrations/${eventbridgeIntegration.ref}`,
    });
    
    
    new cdk.CfnOutput(this, 'apiUrl', { value: httpApi.url!, description: "HTTP API endpoint URL" });
  }
}

