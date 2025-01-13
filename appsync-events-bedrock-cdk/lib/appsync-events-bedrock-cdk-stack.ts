import * as cdk from 'aws-cdk-lib';
import { Construct } from 'constructs';
import { CfnApiKey } from 'aws-cdk-lib/aws-appsync';
import { NodejsFunction } from 'aws-cdk-lib/aws-lambda-nodejs';
import { Runtime } from 'aws-cdk-lib/aws-lambda';
import { PolicyDocument, PolicyStatement, Role, ServicePrincipal } from 'aws-cdk-lib/aws-iam';
import { CfnApi, CfnChannelNamespace } from "aws-cdk-lib/aws-appsync"
import { CorsHttpMethod, HttpApi, HttpMethod } from 'aws-cdk-lib/aws-apigatewayv2';
import { HttpLambdaIntegration } from 'aws-cdk-lib/aws-apigatewayv2-integrations';
import { Duration, Expiration } from 'aws-cdk-lib';

export class AppsyncEventsBedrockCdkStack extends cdk.Stack {
  constructor(scope: Construct, id: string, props?: cdk.StackProps) {
    super(scope, id, props);

    const eventsApi = new CfnApi(this, 'Events', {
      name: 'bedrock-failover',

      eventConfig: {
        authProviders: [{
          authType: 'API_KEY',
        }],
        connectionAuthModes: [{
          authType: 'API_KEY',
        }],
        defaultPublishAuthModes: [{
          authType: 'API_KEY'
        }],
        defaultSubscribeAuthModes: [{
          authType: 'API_KEY',
        }],
      },
    });

    const channel = new CfnChannelNamespace(this, 'DefaultChannel', {
      name: 'BedrockChat',
      apiId: eventsApi.attrApiId
    })

    const apiKey = new CfnApiKey(this, "AppsyncApiKey", {
        apiId: eventsApi.attrApiId,
        description: "Default API Key",
        expires: Expiration.after(Duration.days(30)).toEpoch(),
       });

    const lambda = new NodejsFunction(this, 'Chat', {
      entry: "src/chat.ts",
      timeout: cdk.Duration.seconds(30),
      runtime: Runtime.NODEJS_20_X,
      memorySize: 2048,
      environment: {
        REGION: this.region,
        EVENTS_API_URL: eventsApi.getAtt('Dns.Http').toString(),
        API_KEY: apiKey.attrApiKey,
        CHANNEL_NAME: channel.name
      },
      role: new Role(this, 'ChatRole', {
        assumedBy: new ServicePrincipal("lambda.amazonaws.com"),
        roleName: "chat-role",
        inlinePolicies: {
          "LambdaPolicy": new PolicyDocument({
            statements: [
              // Grant permissions to call bedrock
              new PolicyStatement({
                resources: ['*'],
                actions: ['bedrock:*']
              }),

              // grant permissions to call appsync events api
              new PolicyStatement({
                resources: ['*'],
                actions: ['appsync:*']
              }),

              // Grant Lambda permissions to write to CloudWatch Logs
              new PolicyStatement({
                resources: [`arn:aws:logs:${this.region}:${this.account}:log-group:*`],
                actions: [
                  "logs:CreateLogGroup",
                  "logs:CreateLogStream",
                  "logs:PutLogEvents",
                ],
              }),
            ]
          })
        }
      }
      )
    })

    const api = new HttpApi(this, 'ChatApi', {
      apiName: "chat-api",
      corsPreflight: {
        allowHeaders: [
          '*',
        ],
        allowMethods: [
          CorsHttpMethod.POST,
          CorsHttpMethod.OPTIONS
        ],
        allowOrigins: [
          '*',
        ],
      },
    })

    api.addRoutes({
      path: '/chat',
      methods: [HttpMethod.POST],
      integration: new HttpLambdaIntegration('LambdaIntegration', lambda)
    })

    new cdk.CfnOutput(this, "EventsApiHttp", {
      value: eventsApi.getAtt('Dns.Http').toString()
    })

    new cdk.CfnOutput(this, "EventsApiRealtime", {
      value: eventsApi.getAtt('Dns.Realtime').toString()
    })

    new cdk.CfnOutput(this, "ApiKey", {
      value: apiKey.attrApiKey
    })

    new cdk.CfnOutput(this, "ChannelName", {
      value: channel.name
    })

    new cdk.CfnOutput(this, "Region", {
      value: this.region
    })

    new cdk.CfnOutput(this, "ChatApiUrl", {
      value: api.apiEndpoint
    })

  }
}
