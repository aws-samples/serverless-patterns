import * as cdk from 'aws-cdk-lib';
import * as agentcore from 'aws-cdk-lib/aws-bedrockagentcore';
import * as iam from 'aws-cdk-lib/aws-iam';
import * as lambda from 'aws-cdk-lib/aws-lambda';
import path = require('path');
import { Construct } from 'constructs';

export class AgentcoreWebSearchStack extends cdk.Stack {
  constructor(scope: Construct, id: string, props?: cdk.StackProps) {
    super(scope, id, props);

    // Amazon Bedrock AgentCore Gateway with IAM authorization
    const gateway = new agentcore.Gateway(this, 'WebSearchGateway', {
      gatewayName: 'web-search-gateway',
      description: 'Amazon Bedrock AgentCore Gateway with Web Search Tool connector',
      authorizerConfiguration: agentcore.GatewayAuthorizer.usingAwsIam(),
    });

    // Web Search connector target using CfnResource (L1)
    const webSearchTarget = new cdk.CfnResource(this, 'WebSearchTarget', {
      type: 'AWS::BedrockAgentCore::GatewayTarget',
      properties: {
        GatewayIdentifier: gateway.gatewayId,
        Name: 'web-search-target',
        TargetConfiguration: {
          Mcp: {
            Connector: {
              Source: { ConnectorId: 'web-search' },
              Configurations: [
                {
                  Name: 'WebSearch',
                  ParameterValues: {},
                },
              ],
            },
          },
        },
        CredentialProviderConfigurations: [
          { CredentialProviderType: 'GATEWAY_IAM_ROLE' },
        ],
      },
    });

    // Grant the gateway role permission to invoke web search
    gateway.role.addToPrincipalPolicy(new iam.PolicyStatement({
      actions: ['bedrock-agentcore:InvokeWebSearch'],
      resources: [
        `arn:aws:bedrock-agentcore:${this.region}:aws:tool/web-search.v1`,
      ],
    }));

    // AWS Lambda function to invoke the gateway
    const fn = new lambda.Function(this, 'WebSearchFunction', {
      runtime: lambda.Runtime.PYTHON_3_12,
      handler: 'index.handler',
      code: lambda.Code.fromAsset(path.join(__dirname, '..', '..', 'src', 'handler')),
      timeout: cdk.Duration.seconds(30),
      environment: {
        GATEWAY_ID: gateway.gatewayId,
        GATEWAY_URL: gateway.gatewayUrl ?? '',
      },
    });

    // Grant the AWS Lambda function permission to invoke the gateway
    gateway.grantInvoke(fn);

    // Outputs
    new cdk.CfnOutput(this, 'GatewayId', { value: gateway.gatewayId });
    new cdk.CfnOutput(this, 'FunctionName', { value: fn.functionName });
  }
}
