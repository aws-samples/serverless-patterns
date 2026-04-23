import * as cdk from "aws-cdk-lib";
import * as lambda from "aws-cdk-lib/aws-lambda";
import * as iam from "aws-cdk-lib/aws-iam";
import { Construct } from "constructs";

export class LambdaDurableExecutionJavaStack extends cdk.Stack {
  constructor(scope: Construct, id: string, props?: cdk.StackProps) {
    super(scope, id, props);

    // Lambda function
    const fn = new lambda.Function(this, "DurableOrderProcessorFn", {
      runtime: lambda.Runtime.JAVA_17,
      handler: "com.example.OrderProcessor::handleRequest",
      code: lambda.Code.fromAsset("src/target/lambda-durable-execution-java-1.0.0.jar"),
      timeout: cdk.Duration.minutes(15),
      memorySize: 512,
      description: "Durable order processing workflow using Java SDK",
    });

    // Enable durable execution via escape hatch
    const cfnFn = fn.node.defaultChild as lambda.CfnFunction;
    cfnFn.addOverride("Properties.DurableConfig", {
      ExecutionTimeout: 3600,
      RetentionPeriodInDays: 7,
    });

    // Durable execution checkpoint permissions
    fn.addToRolePolicy(
      new iam.PolicyStatement({
        actions: [
          "lambda:CheckpointDurableExecution",
          "lambda:GetDurableExecutionState",
        ],
        resources: ["*"],
      })
    );

    // Version and alias via L1 to avoid CDK version property validation
    const version = new lambda.CfnVersion(this, "FnVersion", {
      functionName: fn.functionName,
      description: "Durable execution version",
    });

    const alias = new lambda.CfnAlias(this, "ProdAlias", {
      functionName: fn.functionName,
      functionVersion: version.attrVersion,
      name: "prod",
    });

    new cdk.CfnOutput(this, "FunctionName", { value: fn.functionName });
    new cdk.CfnOutput(this, "FunctionAliasArn", {
      value: alias.ref,
      description: "Use this ARN to invoke the durable function",
    });
  }
}
