import * as cdk from 'aws-cdk-lib';
import * as apigatewayv2 from 'aws-cdk-lib/aws-apigatewayv2';
import * as lambda from 'aws-cdk-lib/aws-lambda';
import * as iam from 'aws-cdk-lib/aws-iam';
import { WebSocketLambdaIntegration } from 'aws-cdk-lib/aws-apigatewayv2-integrations';
import { Construct } from 'constructs';
import { RustFunction } from 'cargo-lambda-cdk';

export class BedrockStreamerStack extends cdk.Stack {
  constructor(scope: Construct, id: string, props?: cdk.StackProps) {
    super(scope, id, props);

    // Rust Lambda Functions
    const streamingLambda = new RustFunction(this, 'BedrockStreamer', {
      manifestPath: 'lib/bedrock-streamer-lambda/Cargo.toml',
      bundling: {
        architecture: lambda.Architecture.ARM_64,
        cargoLambdaFlags: [
          '--compiler',
          'cross',
          '--release',
        ],
      },
      timeout: cdk.Duration.seconds(60),
    });

    // Grant Lambda permission to invoke Bedrock
    streamingLambda.addToRolePolicy(new iam.PolicyStatement({
      actions: ['bedrock:InvokeModelWithResponseStream'],
      resources: ['*'],
    }));

    // Create the WebSocket API
    const webSocketApi = new apigatewayv2.WebSocketApi(this, 'WebSocketApi', {
      connectRouteOptions: {
        integration: new WebSocketLambdaIntegration('ConnectIntegration', streamingLambda),
      },
      disconnectRouteOptions: {
        integration: new WebSocketLambdaIntegration('DisconnectIntegration', streamingLambda),
      },
      defaultRouteOptions: {
        integration: new WebSocketLambdaIntegration('DefaultIntegration', streamingLambda),
      },
    });

    // Create a stage for the WebSocket API
    const stage = new apigatewayv2.WebSocketStage(this, 'Stage', {
      webSocketApi,
      stageName: 'prod',
      autoDeploy: true,
    });

    // Grant the Lambda function permission to manage WebSocket connections
    streamingLambda.addToRolePolicy(new iam.PolicyStatement({
      actions: [
        'execute-api:ManageConnections',
      ],
      resources: [
        `arn:aws:execute-api:${this.region}:${this.account}:${webSocketApi.apiId}/${stage.stageName}/*`,
      ],
    }));

    // Output the WebSocket URL
    new cdk.CfnOutput(this, 'WebSocketURL', {
      value: stage.url,
      description: 'WebSocket URL',
    });
  }
}