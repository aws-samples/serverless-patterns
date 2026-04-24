import * as cdk from "aws-cdk-lib";
import * as lambda from "aws-cdk-lib/aws-lambda";
import * as iam from "aws-cdk-lib/aws-iam";
import * as ec2 from "aws-cdk-lib/aws-ec2";
import * as logs from "aws-cdk-lib/aws-logs";
import { Construct } from "constructs";

export class LambdaManagedInstancesBedrockStack extends cdk.Stack {
  constructor(scope: Construct, id: string, props?: cdk.StackProps) {
    super(scope, id, props);

    const modelId = new cdk.CfnParameter(this, "BedrockModelId", {
      type: "String",
      default: "us.anthropic.claude-sonnet-4-20250514-v1:0",
      description: "Bedrock inference profile model ID",
    });

    const functionName = "managed-instances-bedrock-cdk";

    const logGroup = new logs.LogGroup(this, "LogGroup", {
      logGroupName: `/aws/lambda/${functionName}`,
      retention: logs.RetentionDays.TWO_WEEKS,
      removalPolicy: cdk.RemovalPolicy.DESTROY,
    });

    const fn = new lambda.Function(this, "BedrockFn", {
      runtime: lambda.Runtime.NODEJS_24_X,
      handler: "index.handler",
      code: lambda.Code.fromAsset("src"),
      timeout: cdk.Duration.minutes(5),
      memorySize: 2048, // Managed Instances require >= 2048 MB
      architecture: lambda.Architecture.ARM_64,
      functionName,
      description: "Bedrock invocation on Lambda Managed Instances (EC2-backed)",
      loggingFormat: lambda.LoggingFormat.JSON,
      logGroup,
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

    // Lambda Managed Instances: EC2-backed compute with serverless management
    const vpc = new ec2.Vpc(this, "ManagedInstancesVpc", {
      maxAzs: 2,
      natGateways: 1,
    });

    const securityGroup = new ec2.SecurityGroup(this, "SecurityGroup", {
      vpc,
      description: "Lambda Managed Instances security group",
    });

    const capacityProvider = new lambda.CapacityProvider(this, "CapacityProvider", {
      capacityProviderName: "bedrock-capacity-provider",
      subnets: vpc.privateSubnets,
      securityGroups: [securityGroup],
      architectures: [lambda.Architecture.ARM_64],
    });

    capacityProvider.addFunction(fn);

    new cdk.CfnOutput(this, "FunctionName", { value: fn.functionName });
    new cdk.CfnOutput(this, "FunctionArn", { value: fn.functionArn });
    new cdk.CfnOutput(this, "LogGroupName", { value: logGroup.logGroupName });
  }
}
