import * as cdk from 'aws-cdk-lib';
import * as appsync from 'aws-cdk-lib/aws-appsync';
import * as lambda from 'aws-cdk-lib/aws-lambda';
import * as logs from 'aws-cdk-lib/aws-logs';
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
      timeout: cdk.Duration.seconds(10),
      logRetention: logs.RetentionDays.ONE_WEEK,
    });

    // IAM role for AppSync to invoke Lambda
    const appsyncRole = new iam.Role(this, 'AppSyncLambdaRole', {
      assumedBy: new iam.ServicePrincipal('appsync.amazonaws.com'),
    });
    eventFn.grantInvoke(appsyncRole);

    // IAM role for AppSync to push logs to CloudWatch
    const logsRole = new iam.Role(this, 'ApiLogsRole', {
      assumedBy: new iam.ServicePrincipal('appsync.amazonaws.com'),
      managedPolicies: [
        iam.ManagedPolicy.fromAwsManagedPolicyName('service-role/AWSAppSyncPushToCloudWatchLogs'),
      ],
    });

    // AppSync Events API with unique name derived from stack name
    const api = new appsync.CfnApi(this, 'EventsApi', {
      name: `${cdk.Aws.STACK_NAME}-EventsApi`,
      eventConfig: {
        authProviders: [{ authType: 'API_KEY' }],
        connectionAuthModes: [{ authType: 'API_KEY' }],
        defaultPublishAuthModes: [{ authType: 'API_KEY' }],
        defaultSubscribeAuthModes: [{ authType: 'API_KEY' }],
        logConfig: {
          logLevel: 'INFO',
          cloudWatchLogsRoleArn: logsRole.roleArn,
        },
      },
    });

    // API key with 365-day expiry
    const apiKey = new appsync.CfnApiKey(this, 'EventsApiKey', {
      apiId: api.attrApiId,
      expires: Math.floor(Date.now() / 1000) + 365 * 24 * 60 * 60,
    });

    // Channel namespace wired to Lambda event handler
    new appsync.CfnChannelNamespace(this, 'NotificationsChannel', {
      apiId: api.attrApiId,
      name: 'notifications',
      publishAuthModes: [{ authType: 'API_KEY' }],
      subscribeAuthModes: [{ authType: 'API_KEY' }],
      codeHandlers: "import { util } from '@aws-appsync/utils';\nexport function onPublish(ctx) {\n  return { events: ctx.events };\n}",
    });

    // Second channel namespace
    new appsync.CfnChannelNamespace(this, 'AlertsChannel', {
      apiId: api.attrApiId,
      name: 'alerts',
      publishAuthModes: [{ authType: 'API_KEY' }],
      subscribeAuthModes: [{ authType: 'API_KEY' }],
    });

    new cdk.CfnOutput(this, 'HttpEndpoint', { value: cdk.Fn.getAtt(api.logicalId, 'Dns.Http').toString() });
    new cdk.CfnOutput(this, 'RealtimeEndpoint', { value: cdk.Fn.getAtt(api.logicalId, 'Dns.Realtime').toString() });
    new cdk.CfnOutput(this, 'ApiId', { value: api.attrApiId });
    new cdk.CfnOutput(this, 'ApiKeyValue', { value: apiKey.attrApiKey });
    new cdk.CfnOutput(this, 'FunctionName', { value: eventFn.functionName });
  }
}
