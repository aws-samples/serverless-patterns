import * as cdk from "aws-cdk-lib";
import * as lambda from "aws-cdk-lib/aws-lambda";
import * as iam from "aws-cdk-lib/aws-iam";
import * as logs from "aws-cdk-lib/aws-logs";
import { Construct } from "constructs";

export class LambdaSnapstartBedrockStack extends cdk.Stack {
  constructor(scope: Construct, id: string, props?: cdk.StackProps) {
    super(scope, id, props);

    const modelId = new cdk.CfnParameter(this, "BedrockModelId", {
      type: "String",
      default: "us.anthropic.claude-sonnet-4-20250514-v1:0",
      description: "Bedrock inference profile model ID",
    });

    const functionName = "snapstart-bedrock-cdk";

    const logGroup = new logs.LogGroup(this, "LogGroup", {
      logGroupName: `/aws/lambda/${functionName}`,
      retention: logs.RetentionDays.TWO_WEEKS,
      removalPolicy: cdk.RemovalPolicy.DESTROY,
    });

    const fn = new lambda.Function(this, "BedrockFn", {
      runtime: lambda.Runtime.PYTHON_3_13,
      handler: "index.handler",
      code: lambda.Code.fromAsset("src"),
      timeout: cdk.Duration.seconds(30),
      memorySize: 512,
      functionName,
      description: "Bedrock invocation with SnapStart for reduced cold starts",
      loggingFormat: lambda.LoggingFormat.JSON,
      logGroup,
      snapStart: lambda.SnapStartConf.ON_PUBLISHED_VERSIONS,
      environment: { MODEL_ID: modelId.valueAsString },
    });

    fn.addToRolePolicy(
      new iam.PolicyStatement({
        actions: ["bedrock:InvokeModel"],
        resources: [
          `arn:aws:bedrock:${this.region}:${this.account}:inference-profile/${modelId.valueAsString}`,
          "arn:aws:bedrock:*::foundation-model/*",
        ],
      })
    );

    // Publish a version to activate SnapStart
    const version = fn.currentVersion;

    // Alias pointing to the SnapStart-optimized version
    const alias = new lambda.Alias(this, "LiveAlias", {
      aliasName: "live",
      version,
    });

    new cdk.CfnOutput(this, "FunctionName", { value: fn.functionName });
    new cdk.CfnOutput(this, "FunctionArn", { value: fn.functionArn });
    new cdk.CfnOutput(this, "AliasArn", { value: alias.functionArn });
    new cdk.CfnOutput(this, "LogGroupName", { value: logGroup.logGroupName });
  }
}
