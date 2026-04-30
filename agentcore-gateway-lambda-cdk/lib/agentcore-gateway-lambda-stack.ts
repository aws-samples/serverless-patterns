import * as cdk from "aws-cdk-lib";
import * as agentcore from "aws-cdk-lib/aws-bedrockagentcore";
import * as iam from "aws-cdk-lib/aws-iam";
import * as lambda from "aws-cdk-lib/aws-lambda";
import { Construct } from "constructs";

export class AgentcoreGatewayLambdaStack extends cdk.Stack {
  constructor(scope: Construct, id: string, props?: cdk.StackProps) {
    super(scope, id, props);

    // Lambda tool handler
    const toolFn = new lambda.Function(this, "ToolFn", {
      runtime: lambda.Runtime.NODEJS_22_X,
      handler: "index.handler",
      code: lambda.Code.fromAsset("src/tool-lambda"),
      timeout: cdk.Duration.seconds(30),
      memorySize: 256,
      description: "AgentCore Gateway Lambda tool target",
    });

    // Gateway IAM role
    const gatewayRole = new iam.Role(this, "GatewayRole", {
      assumedBy: new iam.ServicePrincipal("bedrock-agentcore.amazonaws.com"),
      description: "Role for AgentCore Gateway to invoke Lambda tools",
    });
    toolFn.grantInvoke(gatewayRole);

    // AgentCore Gateway (MCP protocol, IAM auth)
    const gateway = new agentcore.CfnGateway(this, "Gateway", {
      name: `tool-gateway-${cdk.Names.uniqueId(this).slice(-8).toLowerCase()}`,
      protocolType: "MCP",
      authorizerType: "AWS_IAM",
      roleArn: gatewayRole.roleArn,
      description: "MCP Gateway exposing Lambda tools",
    });

    // Gateway target — Lambda with inline tool definitions
    const target = new agentcore.CfnGatewayTarget(this, "ToolTarget", {
      gatewayIdentifier: gateway.attrGatewayIdentifier,
      name: "city-tools",
      description: "Weather and time tools backed by Lambda",
      credentialProviderConfigurations: [
        {
          credentialProviderType: "GATEWAY_IAM_ROLE",
        },
      ],
      targetConfiguration: {
        mcp: {
          lambda: {
            lambdaArn: toolFn.functionArn,
            toolSchema: {
              inlinePayload: [
                {
                  name: "get_weather",
                  description: "Get current weather for a city",
                  inputSchema: {
                    type: "object",
                    properties: {
                      city: {
                        type: "string",
                        description: "City name (e.g. Tokyo, London)",
                      },
                    },
                    required: ["city"],
                  },
                },
                {
                  name: "get_time",
                  description: "Get current UTC time for a city",
                  inputSchema: {
                    type: "object",
                    properties: {
                      city: {
                        type: "string",
                        description: "City name",
                      },
                    },
                    required: ["city"],
                  },
                },
              ],
            },
          },
        },
      },
    });

    new cdk.CfnOutput(this, "GatewayId", {
      value: gateway.attrGatewayIdentifier,
    });
    new cdk.CfnOutput(this, "GatewayUrl", {
      value: gateway.attrGatewayUrl,
    });
    new cdk.CfnOutput(this, "TargetId", {
      value: target.attrTargetId,
    });
    new cdk.CfnOutput(this, "FunctionName", {
      value: toolFn.functionName,
    });
  }
}
