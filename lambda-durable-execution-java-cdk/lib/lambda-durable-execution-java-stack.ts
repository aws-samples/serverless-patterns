import * as cdk from "aws-cdk-lib";
import * as lambda from "aws-cdk-lib/aws-lambda";
import * as iam from "aws-cdk-lib/aws-iam";
import { Construct } from "constructs";

export class LambdaDurableExecutionJavaStack extends cdk.Stack {
  constructor(scope: Construct, id: string, props?: cdk.StackProps) {
    super(scope, id, props);

    const fn = new lambda.Function(this, "DurableOrderProcessorFn", {
      runtime: lambda.Runtime.JAVA_17,
      handler: "com.example.OrderProcessor::handleRequest",
      code: lambda.Code.fromAsset("src/target/lambda-durable-execution-java-1.0.0.jar"),
      timeout: cdk.Duration.minutes(15),
      memorySize: 512,
      description: "Durable order processing workflow using Java SDK",
      durableConfig: {
        executionTimeout: cdk.Duration.hours(1),
        retentionPeriod: cdk.Duration.days(7),
      },
    });

    fn.role!.addManagedPolicy(
      iam.ManagedPolicy.fromAwsManagedPolicyName(
        "service-role/AWSLambdaBasicDurableExecutionRolePolicy"
      )
    );

    const alias = new lambda.Alias(this, "ProdAlias", {
      aliasName: "prod",
      version: fn.currentVersion,
    });

    new cdk.CfnOutput(this, "FunctionName", { value: fn.functionName });
    new cdk.CfnOutput(this, "FunctionAliasArn", {
      value: alias.aliasName,
      description: "Use this ARN to invoke the durable function",
    });
  }
}
