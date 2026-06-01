import * as cdk from 'aws-cdk-lib';
import * as iam from 'aws-cdk-lib/aws-iam';
import * as path from 'path';
import { Construct } from 'constructs';
import * as agentcore from '@aws-cdk/aws-bedrock-agentcore-alpha';

export class AgentCoreStrandsStack extends cdk.Stack {
  public readonly runtimeArn: string;
  public readonly runtimeEndpointUrl: string;

  constructor(scope: Construct, id: string, props?: cdk.StackProps) {
    super(scope, id, props);

    // Build the agent container from the local Dockerfile
    const agentRuntimeArtifact = agentcore.AgentRuntimeArtifact.fromAsset(
      path.join(__dirname, '../agent'),
    );

    // Create the AgentCore Runtime (L2 construct handles ECR + IAM automatically)
    const runtime = new agentcore.Runtime(this, 'StrandsAgentRuntime', {
      runtimeName: 'strandsPromptAgent',
      agentRuntimeArtifact,
      description: 'Strands SDK agent that answers prompts via Bedrock',
    });

    // Grant Bedrock model invocation permissions to the runtime's execution role
    runtime.addToRolePolicy(
      new iam.PolicyStatement({
        effect: iam.Effect.ALLOW,
        actions: [
          'bedrock:InvokeModel',
          'bedrock:InvokeModelWithResponseStream',
        ],
        resources: [
          `arn:aws:bedrock:*::foundation-model/*`,
          "arn:aws:bedrock:*:*:inference-profile/*",
        ],
      }),
    );

    runtime.addToRolePolicy(
          new iam.PolicyStatement({
            effect: iam.Effect.ALLOW,
            actions: [
              'lambda:SendDurableExecutionCallbackSuccess',
              'lambda:SendDurableExecutionCallbackFailure',
              'lambda:SendDurableExecutionCallbackHeartbeat',
            ],
            resources: ["*"],
          }),
        );

    this.runtimeArn = runtime.agentRuntimeArn;
    this.runtimeEndpointUrl = `https://bedrock-agentcore-runtime.${this.region}.amazonaws.com/runtimes/${runtime.agentRuntimeId}/endpoints/DEFAULT`;

    new cdk.CfnOutput(this, 'RuntimeArn', {
      value: runtime.agentRuntimeArn,
      description: 'ARN of the AgentCore Runtime',
    });

    new cdk.CfnOutput(this, 'RuntimeId', {
      value: runtime.agentRuntimeId,
      description: 'ID of the AgentCore Runtime',
    });

    new cdk.CfnOutput(this, 'RuntimeEndpointUrl', {
      value: this.runtimeEndpointUrl,
      description: 'AgentCore Runtime DEFAULT endpoint URL',
    });
  }
}
