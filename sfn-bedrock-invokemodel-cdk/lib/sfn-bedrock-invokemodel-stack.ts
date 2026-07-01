import * as cdk from "aws-cdk-lib";
import * as sfn from "aws-cdk-lib/aws-stepfunctions";
import * as tasks from "aws-cdk-lib/aws-stepfunctions-tasks";
import * as bedrock from "aws-cdk-lib/aws-bedrock";
import * as logs from "aws-cdk-lib/aws-logs";
import * as iam from "aws-cdk-lib/aws-iam";
import { Construct } from "constructs";

export class SfnBedrockInvokemodelStack extends cdk.Stack {
  constructor(scope: Construct, id: string, props?: cdk.StackProps) {
    super(scope, id, props);

    const modelId = new cdk.CfnParameter(this, "BedrockModelId", {
      type: "String",
      default: "us.anthropic.claude-sonnet-4-20250514-v1:0",
      description: "Bedrock inference profile model ID",
    });

    // Construct inference profile ARN for the model
    const inferenceProfileArn = `arn:aws:bedrock:${this.region}:${this.account}:inference-profile/${modelId.valueAsString}`;
    const model = bedrock.ProvisionedModel.fromProvisionedModelArn(
      this,
      "Model",
      inferenceProfileArn
    );

    // Step Functions task: invoke Bedrock directly (no Lambda needed)
    const invokeModel = new tasks.BedrockInvokeModel(this, "InvokeModel", {
      model,
      body: sfn.TaskInput.fromObject({
        anthropic_version: "bedrock-2023-05-31",
        max_tokens: 1024,
        messages: [
          {
            role: "user",
            content: sfn.JsonPath.stringAt("$.prompt"),
          },
        ],
      }),
      resultSelector: {
        "response.$": "$.Body.content[0].text",
        "model.$": "$.Body.model",
        "usage.$": "$.Body.usage",
      },
    });

    // Add retry for transient failures
    invokeModel.addRetry({
      errors: ["States.TaskFailed"],
      interval: cdk.Duration.seconds(20),
      maxAttempts: 3,
      backoffRate: 2,
    });

    const logGroup = new logs.LogGroup(this, "LogGroup", {
      logGroupName: "/aws/stepfunctions/sfn-bedrock-invokemodel",
      retention: logs.RetentionDays.TWO_WEEKS,
      removalPolicy: cdk.RemovalPolicy.DESTROY,
    });

    const stateMachine = new sfn.StateMachine(this, "StateMachine", {
      stateMachineName: "sfn-bedrock-invokemodel",
      definitionBody: sfn.DefinitionBody.fromChainable(invokeModel),
      stateMachineType: sfn.StateMachineType.EXPRESS,
      timeout: cdk.Duration.minutes(5),
      logs: {
        destination: logGroup,
        level: sfn.LogLevel.ALL,
        includeExecutionData: true,
      },
    });

    // Grant Bedrock access (inference profile + foundation model)
    stateMachine.addToRolePolicy(
      new iam.PolicyStatement({
        actions: ["bedrock:InvokeModel"],
        resources: [
          `arn:aws:bedrock:${this.region}:${this.account}:inference-profile/${modelId.valueAsString}`,
          "arn:aws:bedrock:*::foundation-model/*",
        ],
      })
    );

    new cdk.CfnOutput(this, "StateMachineArn", { value: stateMachine.stateMachineArn });
    new cdk.CfnOutput(this, "StateMachineName", { value: stateMachine.stateMachineName! });
    new cdk.CfnOutput(this, "LogGroupName", { value: logGroup.logGroupName });
  }
}
