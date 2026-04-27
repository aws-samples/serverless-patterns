import * as cdk from "aws-cdk-lib";
import * as lambda from "aws-cdk-lib/aws-lambda";
import * as apigateway from "aws-cdk-lib/aws-apigateway";
import * as iam from "aws-cdk-lib/aws-iam";
import * as logs from "aws-cdk-lib/aws-logs";
import { Construct } from "constructs";

export class ApigwStreamingLambdaBedrockStack extends cdk.Stack {
  constructor(scope: Construct, id: string, props?: cdk.StackProps) {
    super(scope, id, props);

    const modelId = new cdk.CfnParameter(this, "BedrockModelId", {
      type: "String",
      default: "us.anthropic.claude-sonnet-4-20250514-v1:0",
      description: "Bedrock model ID (inference profile) to use",
    });

    // Streaming Lambda function
    const fn = new lambda.Function(this, "StreamingBedrockFn", {
      runtime: lambda.Runtime.NODEJS_20_X,
      handler: "index.handler",
      code: lambda.Code.fromAsset("src"),
      timeout: cdk.Duration.minutes(5),
      memorySize: 256,
      environment: {
        MODEL_ID: modelId.valueAsString,
      },
      logRetention: logs.RetentionDays.ONE_WEEK,
    });

    fn.addToRolePolicy(
      new iam.PolicyStatement({
        actions: ["bedrock:InvokeModelWithResponseStream"],
        resources: [
          `arn:aws:bedrock:${this.region}:${this.account}:inference-profile/${modelId.valueAsString}`,
          "arn:aws:bedrock:*::foundation-model/*",
        ],
      })
    );

    // REST API with streaming integration
    const api = new apigateway.RestApi(this, "StreamingApi", {
      restApiName: "Bedrock Streaming API",
      description: "API Gateway REST API with response streaming to Bedrock",
      deployOptions: { stageName: "prod" },
    });

    const chatResource = api.root.addResource("chat");

    // Add POST method with standard Lambda proxy integration
    const method = chatResource.addMethod(
      "POST",
      new apigateway.LambdaIntegration(fn, { timeout: cdk.Duration.minutes(5) })
    );

    // Override integration URI to use response-streaming-invocations path
    const cfnMethod = method.node.defaultChild as apigateway.CfnMethod;
    cfnMethod.addPropertyOverride(
      "Integration.Uri",
      `arn:aws:apigateway:${this.region}:lambda:path/2021-11-15/functions/${fn.functionArn}/response-streaming-invocations`
    );
    cfnMethod.addPropertyOverride(
      "Integration.ResponseTransferMode",
      "STREAM"
    );
    cfnMethod.addPropertyOverride("Integration.TimeoutInMillis", 300000);

    new cdk.CfnOutput(this, "ApiEndpoint", {
      value: api.urlForPath("/chat"),
      description: "POST your prompt to this URL to stream Bedrock responses",
    });
    new cdk.CfnOutput(this, "FunctionName", { value: fn.functionName });
  }
}
