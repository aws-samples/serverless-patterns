import * as cdk from "aws-cdk-lib";
import * as lambda from "aws-cdk-lib/aws-lambda";
import * as iam from "aws-cdk-lib/aws-iam";
import * as ec2 from "aws-cdk-lib/aws-ec2";
import * as logs from "aws-cdk-lib/aws-logs";
import { Construct } from "constructs";

export class LambdaManagedInstancesBedrockStack extends cdk.Stack {
  constructor(scope: Construct, id: string, props?: cdk.StackProps) {
    super(scope, id, props);

    // The inference profile and the foundation-model ARNs in the IAM policy below
    // are derived from this one model ID. The us. profile routes to us-east-1,
    // us-east-2 and us-west-2 when called from one of those Regions, so deploy there.
    const baseModelId = "anthropic.claude-sonnet-4-6";
    const inferenceProfileId = `us.${baseModelId}`;

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
      environment: { MODEL_ID: inferenceProfileId },
    });

    fn.addToRolePolicy(
      new iam.PolicyStatement({
        actions: ["bedrock:InvokeModel"],
        resources: [
          `arn:${this.partition}:bedrock:${this.region}:${this.account}:inference-profile/${inferenceProfileId}`,
          `arn:${this.partition}:bedrock:us-east-1::foundation-model/${baseModelId}`,
          `arn:${this.partition}:bedrock:us-east-2::foundation-model/${baseModelId}`,
          `arn:${this.partition}:bedrock:us-west-2::foundation-model/${baseModelId}`,
        ],
      })
    );

    // Published version required for Managed Instances execution
    const version = fn.currentVersion;
    const alias = new lambda.Alias(this, "ProdAlias", {
      aliasName: "prod",
      version,
    });

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
      subnets: vpc.privateSubnets,
      securityGroups: [securityGroup],
      architectures: [lambda.Architecture.ARM_64],
    });

    capacityProvider.addFunction(fn);

    new cdk.CfnOutput(this, "FunctionName", { value: fn.functionName });
    new cdk.CfnOutput(this, "FunctionArn", { value: fn.functionArn });
    new cdk.CfnOutput(this, "AliasArn", { value: alias.functionArn, description: "Invoke this ARN to run on Managed Instances" });
    new cdk.CfnOutput(this, "LogGroupName", { value: logGroup.logGroupName });
  }
}
