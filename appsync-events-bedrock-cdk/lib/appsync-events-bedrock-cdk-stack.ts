import * as cdk from 'aws-cdk-lib';
import { CfnInclude } from 'aws-cdk-lib/cloudformation-include';
import { Construct } from 'constructs';
import { CfnApiKey } from 'aws-cdk-lib/aws-appsync';
import { NodejsFunction } from 'aws-cdk-lib/aws-lambda-nodejs';
import { Runtime } from 'aws-cdk-lib/aws-lambda';
import { PolicyDocument, PolicyStatement, Role, ServicePrincipal } from 'aws-cdk-lib/aws-iam';
import { CorsHttpMethod, HttpApi, HttpMethod } from 'aws-cdk-lib/aws-apigatewayv2';
import { HttpLambdaIntegration } from 'aws-cdk-lib/aws-apigatewayv2-integrations';

export class AppsyncEventsBedrockCdkStack extends cdk.Stack {
  constructor(scope: Construct, id: string, props?: cdk.StackProps) {
    super(scope, id, props);

    // L1 constructs not available yet
    const template = new CfnInclude(this, "EventsApiCfnTemplate", {
      templateFile: './lib/events-api-cfn.yaml'
    })

    const eventsApi = template.getResource('EventsApi') as cdk.CfnResource

    const channel = template.getResource('Channel') as cdk.CfnResource
    const channelName = "BedrockChat"

    const apiKey = template.getResource('ApiKey') as CfnApiKey

    const lambda = new NodejsFunction(this, 'Chat', {
      entry: "src/chat.ts",
      timeout: cdk.Duration.seconds(30),
      runtime: Runtime.NODEJS_20_X,
      memorySize: 2048,
      environment: {
        REGION: this.region,
        EVENTS_API_URL: eventsApi.getAtt('Dns.Http').toString(),
        API_KEY: apiKey.attrApiKey,
        CHANNEL_NAME: channelName
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
      value: channelName
    })

    new cdk.CfnOutput(this, "Region", {
      value: this.region
    })

    new cdk.CfnOutput(this, "ChatApiUrl", {
      value: api.apiEndpoint
    })

  }
}
