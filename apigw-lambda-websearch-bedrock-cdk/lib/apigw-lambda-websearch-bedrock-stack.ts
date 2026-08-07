import * as cdk from 'aws-cdk-lib';
import { Construct } from 'constructs';
import * as agentcore from 'aws-cdk-lib/aws-bedrockagentcore';
import * as apigateway from 'aws-cdk-lib/aws-apigateway';
import * as iam from 'aws-cdk-lib/aws-iam';
import * as lambda from 'aws-cdk-lib/aws-lambda';

export class ApigwLambdaWebsearchBedrockStack extends cdk.Stack {
  constructor(scope: Construct, id: string, props?: cdk.StackProps) {
    super(scope, id, props);

    // Amazon Bedrock AgentCore Gateway with Web Search connector
    const gateway = new agentcore.Gateway(this, 'WebSearchGateway', {
      gatewayName: 'grounded-search-gateway',
      description: 'Amazon Bedrock AgentCore Gateway with Web Search for grounded AI answers',
      authorizerConfiguration: agentcore.GatewayAuthorizer.usingAwsIam(),
    });

    // Web Search connector target
    new cdk.CfnResource(this, 'WebSearchTarget', {
      type: 'AWS::BedrockAgentCore::GatewayTarget',
      properties: {
        GatewayIdentifier: gateway.gatewayId,
        Name: 'web-search',
        TargetConfiguration: {
          Mcp: {
            Connector: {
              Source: { ConnectorId: 'web-search' },
              Configurations: [{ Name: 'WebSearch', ParameterValues: {} }],
            },
          },
        },
        CredentialProviderConfigurations: [
          { CredentialProviderType: 'GATEWAY_IAM_ROLE' },
        ],
      },
    });

    // Grant gateway role permission to invoke Web Search
    gateway.role.addToPrincipalPolicy(new iam.PolicyStatement({
      actions: ['bedrock-agentcore:InvokeWebSearch'],
      resources: [`arn:aws:bedrock-agentcore:${this.region}:aws:tool/web-search.v1`],
    }));

    // AWS Lambda function that orchestrates Web Search + Amazon Bedrock inference
    const fn = new lambda.Function(this, 'GroundedAnswerFunction', {
      runtime: lambda.Runtime.PYTHON_3_12,
      handler: 'index.handler',
      code: lambda.Code.fromAsset('src/handler'),
      timeout: cdk.Duration.seconds(60),
      memorySize: 256,
      environment: {
        GATEWAY_ID: gateway.gatewayId,
        GATEWAY_URL: gateway.gatewayUrl ?? '',
        MODEL_ID: 'us.anthropic.claude-sonnet-4-20250514-v1:0',
      },
    });

    // Grant the AWS Lambda function permission to invoke the gateway
    gateway.grantInvoke(fn);

    // Grant the AWS Lambda function permission to invoke Amazon Bedrock models
    fn.addToRolePolicy(new iam.PolicyStatement({
      actions: ['bedrock:InvokeModel'],
      resources: [
        `arn:aws:bedrock:*::foundation-model/*`,
        `arn:aws:bedrock:*:${this.account}:inference-profile/*`,
      ],
    }));

    // Amazon API Gateway REST API as the user-facing endpoint
    const api = new apigateway.RestApi(this, 'GroundedSearchApi', {
      restApiName: 'Grounded AI Search',
      description: 'Ask questions grounded in live web data via Amazon Bedrock AgentCore Web Search and Amazon Bedrock',
    });

    const askResource = api.root.addResource('ask');
    askResource.addMethod('POST', new apigateway.LambdaIntegration(fn));

    // Outputs
    new cdk.CfnOutput(this, 'ApiEndpoint', { value: api.url });
    new cdk.CfnOutput(this, 'FunctionName', { value: fn.functionName });
  }
}
