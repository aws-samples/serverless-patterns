import * as cdk from 'aws-cdk-lib';
import * as iam from 'aws-cdk-lib/aws-iam';
import * as path from 'path';
import { Construct } from 'constructs';
import * as agentcore from '@aws-cdk/aws-bedrock-agentcore-alpha';

export class AgentCoreStack extends cdk.Stack {
  public readonly researchRuntimeArn: string;
  public readonly researchEndpointUrl: string;
  public readonly synthesisRuntimeArn: string;
  public readonly synthesisEndpointUrl: string;

  constructor(scope: Construct, id: string, props?: cdk.StackProps) {
    super(scope, id, props);

    const agentRuntimeArtifact = agentcore.AgentRuntimeArtifact.fromAsset(
      path.join(__dirname, '../agent'),
    );

    const bedrockPolicy = new iam.PolicyStatement({
      effect: iam.Effect.ALLOW,
      actions: [
        'bedrock:InvokeModel',
        'bedrock:InvokeModelWithResponseStream',
      ],
      resources: [
        'arn:aws:bedrock:*::foundation-model/*',
        'arn:aws:bedrock:*:*:inference-profile/*',
      ],
    });

    const ecrPolicy = new iam.PolicyStatement({
      effect: iam.Effect.ALLOW,
      actions: [
        'ecr:GetAuthorizationToken',
        'ecr:BatchGetImage',
        'ecr:GetDownloadUrlForLayer',
        'ecr:BatchCheckLayerAvailability',
      ],
      resources: ['*'],
    });

    // Research runtime — handles market data, competitive analysis, and news roles
    const researchRuntime = new agentcore.Runtime(this, 'ResearchAgentRuntime', {
      runtimeName: 'researchAgent',
      agentRuntimeArtifact,
      description: 'Specialized research agent for market data, competitive analysis, and news',
    });
    researchRuntime.addToRolePolicy(bedrockPolicy);
    researchRuntime.addToRolePolicy(ecrPolicy);

    // Synthesis runtime — combines findings into a final report
    const synthesisRuntime = new agentcore.Runtime(this, 'SynthesisAgentRuntime', {
      runtimeName: 'synthesisAgent',
      agentRuntimeArtifact,
      description: 'Synthesis agent that combines research findings into an executive report',
    });
    synthesisRuntime.addToRolePolicy(bedrockPolicy);
    synthesisRuntime.addToRolePolicy(ecrPolicy);

    this.researchRuntimeArn = researchRuntime.agentRuntimeArn;
    this.researchEndpointUrl = `https://bedrock-agentcore-runtime.${this.region}.amazonaws.com/runtimes/${researchRuntime.agentRuntimeId}/endpoints/DEFAULT`;
    this.synthesisRuntimeArn = synthesisRuntime.agentRuntimeArn;
    this.synthesisEndpointUrl = `https://bedrock-agentcore-runtime.${this.region}.amazonaws.com/runtimes/${synthesisRuntime.agentRuntimeId}/endpoints/DEFAULT`;

    new cdk.CfnOutput(this, 'ResearchRuntimeArn', { value: researchRuntime.agentRuntimeArn });
    new cdk.CfnOutput(this, 'SynthesisRuntimeArn', { value: synthesisRuntime.agentRuntimeArn });
  }
}
