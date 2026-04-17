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
      default: "us.anthropic.claude-sonnet-4-20250514",
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
      logRetention: logs.RetentionDays.ONE_WEEK,
    });

    // Enable durable execution via CfnFunction escape hatch
    const cfnFn = fn.node.defaultChild as lambda.CfnFunction;
    cfnFn.addOverride("Properties.DurableExecution", {
      Enabled: true,
    });

    // Bedrock InvokeModel permission
    fn.addToRolePolicy(
      new iam.PolicyStatement({
        actions: ["bedrock:InvokeModel"],
        resources: ["*"],
      })
    );

    // Durable execution permissions
    fn.addToRolePolicy(
      new iam.PolicyStatement({
        actions: [
          "lambda:CheckpointDurableExecution",
          "lambda:GetDurableExecutionState",
        ],
        resources: [fn.functionArn, `${fn.functionArn}:*`],
      })
    );

    // Publish version (durable functions require qualified invocation)
    // Use CfnVersion to avoid CDK validation of DurableExecution property
    const version = new lambda.CfnVersion(this, "DurableVersion", {
      functionName: fn.functionName,
    });
    version.addDependency(cfnFn);

    new cdk.CfnOutput(this, "FunctionName", { value: fn.functionName });
    new cdk.CfnOutput(this, "FunctionArn", { value: fn.functionArn });
    new cdk.CfnOutput(this, "VersionArn", { value: version.attrFunctionArn });
  }
}
