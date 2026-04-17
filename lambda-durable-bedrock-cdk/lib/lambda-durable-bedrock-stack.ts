import * as cdk from "aws-cdk-lib";
import * as lambda from "aws-cdk-lib/aws-lambda";
import * as iam from "aws-cdk-lib/aws-iam";
import * as logs from "aws-cdk-lib/aws-logs";
import { Construct } from "constructs";

export class LambdaDurableBedrockStack extends cdk.Stack {
  constructor(scope: Construct, id: string, props?: cdk.StackProps) {
    super(scope, id, props);

    const modelId = new cdk.CfnParameter(this, "BedrockModelId", {
      type: "String",
      default: "us.anthropic.claude-sonnet-4-20250514-v1:0",
      description: "Bedrock model ID (inference profile) to use",
    });

    // Lambda function with durable execution enabled
    const fn = new lambda.Function(this, "DurableBedrockFn", {
      runtime: lambda.Runtime.NODEJS_20_X,
      handler: "index.handler",
      code: lambda.Code.fromAsset("src"),
      timeout: cdk.Duration.minutes(15),
      memorySize: 256,
      environment: {
        MODEL_ID: modelId.valueAsString,
      },
    });

    // Enable durable execution via CfnFunction escape hatch
    const cfnFn = fn.node.defaultChild as lambda.CfnFunction;
    cfnFn.addOverride("Properties.Runtime", "nodejs24.x");
    cfnFn.addOverride("Properties.DurableConfig", {
      ExecutionTimeout: 900, // 15 minutes max durable execution
      RetentionPeriodInDays: 14,
    });

    // Bedrock InvokeModel permission
    fn.addToRolePolicy(
      new iam.PolicyStatement({
        actions: ["bedrock:InvokeModel"],
        resources: ["*"],
      })
    );

    // Durable execution permissions (wildcard to avoid circular dep)
    fn.addToRolePolicy(
      new iam.PolicyStatement({
        actions: [
          "lambda:CheckpointDurableExecution",
          "lambda:GetDurableExecutionState",
        ],
        resources: ["*"],
      })
    );

    new cdk.CfnOutput(this, "FunctionName", { value: fn.functionName });
    new cdk.CfnOutput(this, "FunctionArn", { value: fn.functionArn });
  }
}
