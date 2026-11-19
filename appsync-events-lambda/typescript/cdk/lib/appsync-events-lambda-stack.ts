import * as path from 'path';
import * as cdk from 'aws-cdk-lib';
import * as appsync from 'aws-cdk-lib/aws-appsync';
import * as lambda from 'aws-cdk-lib/aws-lambda';
import * as logs from 'aws-cdk-lib/aws-logs';
import * as iam from 'aws-cdk-lib/aws-iam';
import { Construct } from 'constructs';

export class AppsyncEventsLambdaStack extends cdk.Stack {
  constructor(scope: Construct, id: string, props?: cdk.StackProps) {
    super(scope, id, props);

    // Explicit log group for the handler, removed together with the stack
    const eventFnLogGroup = new logs.LogGroup(this, 'EventHandlerLogGroup', {
      retention: logs.RetentionDays.ONE_WEEK,
      removalPolicy: cdk.RemovalPolicy.DESTROY,
    });

    // Lambda handler for event processing
    const eventFn = new lambda.Function(this, 'EventHandlerFn', {
      runtime: lambda.Runtime.NODEJS_24_X,
      handler: 'index.handler',
      code: lambda.Code.fromAsset(path.join(__dirname, '..', 'src')),
      timeout: cdk.Duration.seconds(10),
      logGroup: eventFnLogGroup,
    });

    // Service role AppSync Events assumes to invoke the Lambda data source
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

    // API key with 365-day expiry. The key value is not a stack output
    // (CloudFormation does not redact outputs); the README reads it with
    // aws appsync list-api-keys.
    new appsync.CfnApiKey(this, 'EventsApiKey', {
      apiId: api.attrApiId,
      expires: Math.floor(Date.now() / 1000) + 365 * 24 * 60 * 60,
    });

    // Lambda data source configured on the Events API. The OnPublish handler
    // references this data source by name (through its Name attribute, which
    // also gives CloudFormation the creation order); the ARN lives here.
    const lambdaDataSource = new appsync.CfnDataSource(this, 'LambdaDataSource', {
      apiId: api.attrApiId,
      name: 'LambdaEventHandler',
      type: 'AWS_LAMBDA',
      serviceRoleArn: appsyncRole.roleArn,
      lambdaConfig: {
        lambdaFunctionArn: eventFn.functionArn,
      },
    });

    // Channel namespace with a Direct Lambda OnPublish interceptor. Every event
    // published to this namespace is sent to the Lambda (REQUEST_RESPONSE) for
    // validation/enrichment before AppSync broadcasts it to subscribers.
    new appsync.CfnChannelNamespace(this, 'NotificationsChannel', {
      apiId: api.attrApiId,
      name: 'notifications',
      publishAuthModes: [{ authType: 'API_KEY' }],
      subscribeAuthModes: [{ authType: 'API_KEY' }],
      handlerConfigs: {
        onPublish: {
          behavior: 'DIRECT',
          integration: {
            dataSourceName: lambdaDataSource.attrName,
            lambdaConfig: {
              invokeType: 'REQUEST_RESPONSE',
            },
          },
        },
      },
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
    new cdk.CfnOutput(this, 'FunctionName', { value: eventFn.functionName });
    new cdk.CfnOutput(this, 'LogGroupName', { value: eventFnLogGroup.logGroupName });
  }
}
