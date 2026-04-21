import * as cdk from "aws-cdk-lib";
import * as lambda from "aws-cdk-lib/aws-lambda";
import * as iam from "aws-cdk-lib/aws-iam";
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

    // Bedrock InvokeModel — scoped to the specific inference profile and its
    // underlying foundation model rather than a wildcard resource.
    fn.addToRolePolicy(
      new iam.PolicyStatement({
        actions: ["bedrock:InvokeModel"],
        resources: [
          `arn:aws:bedrock:${this.region}:${this.account}:inference-profile/${modelId.valueAsString}`,
          "arn:aws:bedrock:*::foundation-model/*",
        ],
      })
    );

    // Durable execution + CloudWatch Logs permissions via AWS managed policy
    // https://docs.aws.amazon.com/aws-managed-policy/latest/reference/AWSLambdaBasicDurableExecutionRolePolicy.html
    fn.role!.addManagedPolicy(
      iam.ManagedPolicy.fromAwsManagedPolicyName(
        "service-role/AWSLambdaBasicDurableExecutionRolePolicy"
      )
    );

    // Publish a version via L1 — fn.currentVersion doesn't recognise the
    // DurableConfig escape-hatch property on CDK 2.180.
    const cfnVersion = new lambda.CfnVersion(this, "DurableBedrockFnVersion", {
      functionName: fn.functionName,
      description: "Durable execution version",
    });

    new cdk.CfnOutput(this, "FunctionName", { value: fn.functionName });
    new cdk.CfnOutput(this, "FunctionArn", { value: fn.functionArn });
    new cdk.CfnOutput(this, "FunctionVersion", {
      value: cfnVersion.attrVersion,
      description: "Published version number — use as --qualifier value",
    });
  }
}
