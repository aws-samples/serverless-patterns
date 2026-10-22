import * as cdk from "aws-cdk-lib";
import * as lambda from "aws-cdk-lib/aws-lambda";
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
        // Lambda only accepts a synchronous invoke when this is 15 minutes or less
        executionTimeout: cdk.Duration.minutes(15),
        retentionPeriod: cdk.Duration.days(7),
      },
    });

    const alias = new lambda.Alias(this, "ProdAlias", {
      aliasName: "prod",
      version: fn.currentVersion,
    });

    new cdk.CfnOutput(this, "FunctionName", { value: fn.functionName });
    new cdk.CfnOutput(this, "FunctionAliasArn", {
      value: alias.functionArn,
      description: "Use this ARN to invoke the durable function",
    });
  }
}
