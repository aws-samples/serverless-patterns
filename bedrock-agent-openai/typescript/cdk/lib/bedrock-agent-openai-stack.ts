import * as cdk from "aws-cdk-lib";
import * as bedrock from "aws-cdk-lib/aws-bedrock";
import * as iam from "aws-cdk-lib/aws-iam";
import * as lambda from "aws-cdk-lib/aws-lambda";
import { Construct } from "constructs";

export class BedrockAgentOpenaiStack extends cdk.Stack {
  constructor(scope: Construct, id: string, props?: cdk.StackProps) {
    super(scope, id, props);

    const modelId = new cdk.CfnParameter(this, "ModelId", {
      type: "String",
      default: "openai.gpt-oss-20b-1:0",
      description: "Bedrock foundation model ID (OpenAI GPT OSS)",
      allowedValues: [
        "openai.gpt-oss-20b-1:0",
        "openai.gpt-oss-120b-1:0",
      ],
    });

    // Lambda action group handler
    const actionFn = new lambda.Function(this, "ActionGroupFn", {
      runtime: lambda.Runtime.NODEJS_22_X,
      handler: "index.handler",
      code: lambda.Code.fromAsset("src"),
      timeout: cdk.Duration.seconds(30),
      memorySize: 256,
      description: "Bedrock Agent action group handler",
    });

    // Agent execution role
    const agentRole = new iam.Role(this, "AgentRole", {
      assumedBy: new iam.ServicePrincipal("bedrock.amazonaws.com"),
      description: "Role for Bedrock Agent with OpenAI model",
    });

    agentRole.addToPolicy(
      new iam.PolicyStatement({
        actions: ["bedrock:InvokeModel"],
        resources: [
          `arn:aws:bedrock:${this.region}::foundation-model/${modelId.valueAsString}`,
        ],
      })
    );

    // Bedrock Agent
    const agent = new bedrock.CfnAgent(this, "Agent", {
      agentName: `openai-assistant-${cdk.Names.uniqueId(this).slice(-8).toLowerCase()}`,
      foundationModel: modelId.valueAsString,
      agentResourceRoleArn: agentRole.roleArn,
      instruction:
        "You are a helpful assistant that answers questions about weather and time. " +
        "Use the provided action group tools to look up current weather and time for any city.",
      idleSessionTtlInSeconds: 600,
      actionGroups: [
        {
          actionGroupName: "CityInfoActions",
          actionGroupExecutor: { lambda: actionFn.functionArn },
          apiSchema: {
            payload: JSON.stringify({
              openapi: "3.0.0",
              info: { title: "City Info API", version: "1.0.0" },
              paths: {
                "/getWeather": {
                  get: {
                    operationId: "getWeather",
                    description: "Get current weather for a city",
                    parameters: [
                      {
                        name: "city",
                        in: "query",
                        required: true,
                        schema: { type: "string" },
                        description: "City name",
                      },
                    ],
                    responses: {
                      "200": {
                        description: "Weather info",
                        content: {
                          "application/json": {
                            schema: { type: "object" },
                          },
                        },
                      },
                    },
                  },
                },
                "/getTime": {
                  get: {
                    operationId: "getTime",
                    description: "Get current time for a city",
                    parameters: [
                      {
                        name: "city",
                        in: "query",
                        required: true,
                        schema: { type: "string" },
                        description: "City name",
                      },
                    ],
                    responses: {
                      "200": {
                        description: "Time info",
                        content: {
                          "application/json": {
                            schema: { type: "object" },
                          },
                        },
                      },
                    },
                  },
                },
              },
            }),
          },
        },
      ],
      autoPrepare: true,
    });

    // Allow Bedrock to invoke the Lambda
    actionFn.addPermission("BedrockInvoke", {
      principal: new iam.ServicePrincipal("bedrock.amazonaws.com"),
      sourceArn: agent.attrAgentArn,
    });

    // Agent alias for invocation
    const alias = new bedrock.CfnAgentAlias(this, "AgentAlias", {
      agentId: agent.attrAgentId,
      agentAliasName: "live",
    });

    new cdk.CfnOutput(this, "AgentId", { value: agent.attrAgentId });
    new cdk.CfnOutput(this, "AgentAliasId", { value: alias.attrAgentAliasId });
    new cdk.CfnOutput(this, "FunctionName", { value: actionFn.functionName });
  }
}
