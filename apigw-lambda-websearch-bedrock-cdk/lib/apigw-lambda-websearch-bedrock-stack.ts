import * as cdk from 'aws-cdk-lib';
import { Construct } from 'constructs';
import * as agentcore from 'aws-cdk-lib/aws-bedrockagentcore';
import * as apigateway from 'aws-cdk-lib/aws-apigateway';
import * as iam from 'aws-cdk-lib/aws-iam';
import * as lambda from 'aws-cdk-lib/aws-lambda';

export class ApigwLambdaWebsearchBedrockStack extends cdk.Stack {
  constructor(scope: Construct, id: string, props?: cdk.StackProps) {
    super(scope, id, props);

    // Amazon Bedrock AgentCore Gateway with Web Search Tool connector
    const gateway = new agentcore.Gateway(this, 'WebSearchGateway', {
      gatewayName: 'grounded-search-gateway',
      description: 'Amazon Bedrock AgentCore Gateway with Web Search Tool for grounded AI answers',
      authorizerConfiguration: agentcore.GatewayAuthorizer.usingAwsIam(),
    });

    // Web Search Tool connector target
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

    // Grant gateway role permission to invoke Web Search Tool
    gateway.role.addToPrincipalPolicy(new iam.PolicyStatement({
      actions: ['bedrock-agentcore:InvokeWebSearch'],
      resources: [`arn:aws:bedrock-agentcore:${this.region}:aws:tool/web-search.v1`],
    }));

    // AWS Lambda function that orchestrates Web Search Tool + Amazon Bedrock inference
    const fn = new lambda.Function(this, 'GroundedAnswerFunction', {
      runtime: lambda.Runtime.PYTHON_3_12,
      handler: 'index.handler',
      code: lambda.Code.fromAsset('src/handler'),
      timeout: cdk.Duration.seconds(28),
      memorySize: 256,
      environment: {
        GATEWAY_ID: gateway.gatewayId,
        GATEWAY_URL: gateway.gatewayUrl ?? '',
        MODEL_ID: 'us.anthropic.claude-sonnet-4-6',  // Update to a newer model as needed; also update the two InvokeModel ARNs below and the fallback in src/handler/index.py
      },
    });

    // Grant the AWS Lambda function permission to invoke the gateway
    gateway.grantInvoke(fn);

    // Grant the AWS Lambda function permission to invoke Amazon Bedrock models.
    // ApplyGuardrail is included because some accounts enforce an organization- or
    // account-level default guardrail, which Amazon Bedrock applies automatically on
    // every InvokeModel call. Without it, InvokeModel fails with AccessDeniedException
    // in guardrail-enforced accounts even though the pattern configures no guardrail.
    fn.addToRolePolicy(new iam.PolicyStatement({
      actions: ['bedrock:InvokeModel'],
      resources: [
        `arn:${this.partition}:bedrock:*::foundation-model/anthropic.claude-sonnet-4-6`,
        `arn:${this.partition}:bedrock:${this.region}:${this.account}:inference-profile/us.anthropic.claude-sonnet-4-6`,
      ],
    }));
    fn.addToRolePolicy(new iam.PolicyStatement({
      actions: ['bedrock:ApplyGuardrail'],
      resources: [`arn:aws:bedrock:*:${this.account}:guardrail/*`],
    }));

    // Amazon API Gateway REST API as the user-facing endpoint
    const api = new apigateway.RestApi(this, 'GroundedSearchApi', {
      restApiName: 'Grounded AI Search',
      description: 'Ask questions grounded in live web data via the Web Search Tool on Amazon Bedrock AgentCore Gateway and Amazon Bedrock',
    });

    const askResource = api.root.addResource('ask');
    askResource.addMethod('POST', new apigateway.LambdaIntegration(fn));

    // Outputs
    new cdk.CfnOutput(this, 'ApiEndpoint', { value: api.url });
    new cdk.CfnOutput(this, 'FunctionName', { value: fn.functionName });
  }
}
