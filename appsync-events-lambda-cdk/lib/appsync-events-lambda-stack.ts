import * as cdk from 'aws-cdk-lib';
import * as appsync from 'aws-cdk-lib/aws-appsync';
import * as lambda from 'aws-cdk-lib/aws-lambda';
import * as iam from 'aws-cdk-lib/aws-iam';
import { Construct } from 'constructs';

export class AppsyncEventsLambdaStack extends cdk.Stack {
  constructor(scope: Construct, id: string, props?: cdk.StackProps) {
    super(scope, id, props);

    // Lambda handler for event processing
    const eventFn = new lambda.Function(this, 'EventHandlerFn', {
      runtime: lambda.Runtime.NODEJS_22_X,
      handler: 'index.handler',
      code: lambda.Code.fromAsset('src'),
      timeout: cdk.Duration.seconds(10)
    });

    // AppSync Events API
    const api = new appsync.CfnApi(this, 'EventsApi', {
      name: 'RealTimePubSubApi',
      eventConfig: {
        authProviders: [{ authType: 'API_KEY' }],
        connectionAuthModes: [{ authType: 'API_KEY' }],
        defaultPublishAuthModes: [{ authType: 'API_KEY' }],
        defaultSubscribeAuthModes: [{ authType: 'API_KEY' }]
      }
    });

    const apiKey = new appsync.CfnApiKey(this, 'EventsApiKey', { apiId: api.attrApiId });

    // IAM role for AppSync to invoke Lambda
    const appsyncRole = new iam.Role(this, 'AppSyncLambdaRole', {
      assumedBy: new iam.ServicePrincipal('appsync.amazonaws.com')
    });
    eventFn.grantInvoke(appsyncRole);

    // Channel namespace without handler (simple pub/sub - no Lambda processing)
    // AppSync Events delivers messages directly to subscribers
    new appsync.CfnChannelNamespace(this, 'NotificationsChannel', {
      apiId: api.attrApiId,
      name: 'notifications',
      publishAuthModes: [{ authType: 'API_KEY' }],
      subscribeAuthModes: [{ authType: 'API_KEY' }]
    });

    // Second channel with custom namespace for different topic
    new appsync.CfnChannelNamespace(this, 'AlertsChannel', {
      apiId: api.attrApiId,
      name: 'alerts',
      publishAuthModes: [{ authType: 'API_KEY' }],
      subscribeAuthModes: [{ authType: 'API_KEY' }]
    });

    new cdk.CfnOutput(this, 'HttpEndpoint', { value: cdk.Fn.getAtt(api.logicalId, 'Dns.Http').toString() });
    new cdk.CfnOutput(this, 'RealtimeEndpoint', { value: cdk.Fn.getAtt(api.logicalId, 'Dns.Realtime').toString() });
    new cdk.CfnOutput(this, 'ApiId', { value: api.attrApiId });
    new cdk.CfnOutput(this, 'ApiKeyValue', { value: apiKey.attrApiKey });
    new cdk.CfnOutput(this, 'FunctionName', { value: eventFn.functionName });
  }
}
