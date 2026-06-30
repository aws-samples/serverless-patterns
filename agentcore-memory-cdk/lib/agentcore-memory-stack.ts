import * as cdk from 'aws-cdk-lib';
import { Construct } from 'constructs';
import * as agentcore from 'aws-cdk-lib/aws-bedrockagentcore';
import * as iam from 'aws-cdk-lib/aws-iam';
import * as lambda from 'aws-cdk-lib/aws-lambda';

export class AgentcoreMemoryStack extends cdk.Stack {
  constructor(scope: Construct, id: string, props?: cdk.StackProps) {
    super(scope, id, props);

    // Amazon Bedrock AgentCore Memory with built-in semantic extraction
    const memory = new agentcore.Memory(this, 'AgentMemory', {
      memoryName: 'agent_memory',
      memoryStrategies: [
        agentcore.MemoryStrategy.usingBuiltInSemantic(),
      ],
    });

    // AWS Lambda function: personalized AI assistant with persistent memory
    const fn = new lambda.Function(this, 'MemoryFunction', {
      runtime: lambda.Runtime.PYTHON_3_12,
      handler: 'index.handler',
      code: lambda.Code.fromAsset('src/handler'),
      timeout: cdk.Duration.seconds(60),
      environment: {
        MEMORY_ID: memory.memoryId,
        MODEL_ID: 'us.anthropic.claude-sonnet-4-20250514-v1:0',
      },
    });

    // Grant permissions to use Amazon Bedrock AgentCore Memory
    fn.addToRolePolicy(new iam.PolicyStatement({
      actions: [
        'bedrock-agentcore:CreateEvent',
        'bedrock-agentcore:GetEvent',
        'bedrock-agentcore:ListEvents',
        'bedrock-agentcore:RetrieveMemoryRecords',
        'bedrock-agentcore:ListMemoryRecords',
      ],
      resources: [memory.memoryArn, `${memory.memoryArn}/*`],
    }));

    // Grant permission to invoke Amazon Bedrock models
    fn.addToRolePolicy(new iam.PolicyStatement({
      actions: ['bedrock:InvokeModel'],
      resources: [
        `arn:aws:bedrock:*::foundation-model/*`,
        `arn:aws:bedrock:*:${this.account}:inference-profile/*`,
      ],
    }));

    // Outputs
    new cdk.CfnOutput(this, 'MemoryId', { value: memory.memoryId });
    new cdk.CfnOutput(this, 'FunctionName', { value: fn.functionName });
  }
}
