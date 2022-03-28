import { Stack, StackProps, CfnOutput } from 'aws-cdk-lib';
import { Construct } from 'constructs';
import { EventBus, Rule } from 'aws-cdk-lib/aws-events';
import { CfnIntegration, CfnRoute } from 'aws-cdk-lib/aws-apigatewayv2';
import { HttpApi } from '@aws-cdk/aws-apigatewayv2-alpha';
import { Effect, PolicyStatement, Role, ServicePrincipal } from 'aws-cdk-lib/aws-iam';
import { LogGroup } from 'aws-cdk-lib/aws-logs';
import { CloudWatchLogGroup } from 'aws-cdk-lib/aws-events-targets';


export class ApiEventbridgeStack extends Stack {
  constructor(scope: Construct, id: string, props?: StackProps) {
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
          Detail: '$request.body',
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
    
    
    new CfnOutput(this, 'apiUrl', { value: httpApi.url!, description: "HTTP API endpoint URL" });
  }
}

