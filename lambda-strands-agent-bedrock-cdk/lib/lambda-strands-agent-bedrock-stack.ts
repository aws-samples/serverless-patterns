import * as cdk from "aws-cdk-lib";
import * as iam from "aws-cdk-lib/aws-iam";
import * as lambda from "aws-cdk-lib/aws-lambda";
import { Construct } from "constructs";

export class LambdaStrandsAgentBedrockStack extends cdk.Stack {
  constructor(scope: Construct, id: string, props?: cdk.StackProps) {
    super(scope, id, props);

    // Strands Agents official Lambda layer (Python 3.12, ARM64)
    const strandsLayer = lambda.LayerVersion.fromLayerVersionArn(
      this,
      "StrandsAgentsLayer",
      `arn:aws:lambda:${this.region}:856699698935:layer:strands-agents-py3_12-x86_64:1`
    );

    // Agent Lambda function
    const agentFn = new lambda.Function(this, "StrandsAgentFn", {
      runtime: lambda.Runtime.PYTHON_3_12,
      handler: "index.handler",
      code: lambda.Code.fromAsset("src/agent"),
      timeout: cdk.Duration.minutes(2),
      memorySize: 512,
      architecture: lambda.Architecture.X86_64,
      layers: [strandsLayer],
      environment: {
        MODEL_ID: "us.anthropic.claude-sonnet-4-20250514-v1:0",
      },
      description: "Strands Agents SDK agent on Lambda with Bedrock",
    });

    // Bedrock invoke permissions
    agentFn.addToRolePolicy(
      new iam.PolicyStatement({
        actions: [
          "bedrock:InvokeModel",
          "bedrock:InvokeModelWithResponseStream",
        ],
        resources: ["*"],
      })
    );

    // Function URL for easy testing
    const fnUrl = agentFn.addFunctionUrl({
      authType: lambda.FunctionUrlAuthType.AWS_IAM,
    });

    new cdk.CfnOutput(this, "FunctionName", {
      value: agentFn.functionName,
    });
    new cdk.CfnOutput(this, "FunctionUrl", {
      value: fnUrl.url,
    });
  }
}
