import * as cdk from 'aws-cdk-lib';
import * as lambda from 'aws-cdk-lib/aws-lambda';
import * as iam from 'aws-cdk-lib/aws-iam';
import { Construct } from 'constructs';

export class LambdaMcpServerBedrockStack extends cdk.Stack {
  constructor(scope: Construct, id: string, props?: cdk.StackProps) {
    super(scope, id, props);

    const modelId = new cdk.CfnParameter(this, 'BedrockModelId', {
      type: 'String',
      default: 'us.anthropic.claude-sonnet-4-20250514-v1:0',
      description: 'Bedrock model ID (inference profile)',
    });

    // MCP Server Lambda with Function URL (Streamable HTTP transport)
    const mcpFn = new lambda.Function(this, 'McpServerFunction', {
      runtime: lambda.Runtime.NODEJS_22_X,
      handler: 'index.handler',
      code: lambda.Code.fromAsset('src'),
      timeout: cdk.Duration.seconds(60),
      memorySize: 256,
      environment: {
        MODEL_ID: modelId.valueAsString,
      },
    });

    mcpFn.addToRolePolicy(new iam.PolicyStatement({
      actions: ['bedrock:InvokeModel'],
      resources: ['*'],
    }));

    // Function URL for MCP Streamable HTTP transport
    const fnUrl = mcpFn.addFunctionUrl({
      authType: lambda.FunctionUrlAuthType.NONE,
      invokeMode: lambda.InvokeMode.BUFFERED,
    });

    new cdk.CfnOutput(this, 'McpServerUrl', { value: fnUrl.url });
    new cdk.CfnOutput(this, 'McpEndpoint', {
      value: cdk.Fn.join('', [fnUrl.url, 'mcp']),
      description: 'MCP endpoint URL for client configuration',
    });
  }
}
