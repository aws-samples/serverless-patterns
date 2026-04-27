import * as cdk from 'aws-cdk-lib';
import { Construct } from 'constructs';
import * as lambda from 'aws-cdk-lib/aws-lambda';
import * as lambdaNode from 'aws-cdk-lib/aws-lambda-nodejs';
import * as iam from 'aws-cdk-lib/aws-iam';
import * as sfn from 'aws-cdk-lib/aws-stepfunctions';
import * as path from 'path';

export class SfnAgentcoreBedrockStack extends cdk.Stack {
  constructor(scope: Construct, id: string, props?: cdk.StackProps) {
    super(scope, id, props);

    const agentRuntimeArnsParam = new cdk.CfnParameter(this, 'AgentRuntimeArns', {
      type: 'String',
      default: 'arn:aws:bedrock-agentcore:us-east-1:123456789012:runtime/placeholder-agent',
      description: 'Comma-separated list of AgentCore runtime ARNs',
    });

    const bedrockModelIdParam = new cdk.CfnParameter(this, 'BedrockModelId', {
      type: 'String',
      default: 'us.anthropic.claude-sonnet-4-20250514-v1:0',
      description: 'Bedrock model ID for aggregation',
    });

    // Lambda to invoke a single AgentCore agent (bundled SDK for streaming support)
    const invokeAgentFn = new lambdaNode.NodejsFunction(this, 'InvokeAgentFn', {
      entry: path.join(__dirname, '..', 'src', 'invoke-agent.ts'),
      handler: 'handler',
      runtime: lambda.Runtime.NODEJS_20_X,
      memorySize: 256,
      timeout: cdk.Duration.minutes(3),
      bundling: {
        minify: true,
        sourceMap: false,
      },
    });

    // Note: AgentCore runtime ARNs are user-provided at deploy time via parameter,
    // so resource-level scoping requires wildcard for flexibility
    invokeAgentFn.addToRolePolicy(new iam.PolicyStatement({
      actions: ['bedrock-agentcore:InvokeAgentRuntime'],
      resources: ['*'],
    }));

    // Aggregate Lambda — summarizes multi-agent responses via Bedrock Converse
    const aggregateFn = new lambda.Function(this, 'AggregateFn', {
      runtime: lambda.Runtime.NODEJS_20_X,
      handler: 'aggregate.handler',
      code: lambda.Code.fromAsset('src'),
      memorySize: 256,
      timeout: cdk.Duration.seconds(60),
      environment: {
        BEDROCK_MODEL_ID: bedrockModelIdParam.valueAsString,
      },
    });

    aggregateFn.addToRolePolicy(new iam.PolicyStatement({
      actions: ['bedrock:InvokeModel'],
      resources: [
        `arn:aws:bedrock:${this.region}:${this.account}:inference-profile/${bedrockModelIdParam.valueAsString}`,
        'arn:aws:bedrock:*::foundation-model/*',
      ],
    }));

    // Required when account-level enforced guardrails are active
    aggregateFn.addToRolePolicy(new iam.PolicyStatement({
      actions: ['bedrock:ApplyGuardrail'],
      resources: [`arn:aws:bedrock:${this.region}:${this.account}:guardrail/*`],
    }));

    // SFN IAM Role
    const sfnRole = new iam.Role(this, 'SfnRole', {
      assumedBy: new iam.ServicePrincipal('states.amazonaws.com'),
    });

    sfnRole.addToPolicy(new iam.PolicyStatement({
      actions: ['lambda:InvokeFunction'],
      resources: [invokeAgentFn.functionArn, aggregateFn.functionArn],
    }));

    // State machine: Map → invoke agents in parallel → aggregate
    const definition = {
      Comment: 'Orchestrate multiple AgentCore agents in parallel and aggregate responses with Bedrock',
      StartAt: 'InvokeAgents',
      States: {
        InvokeAgents: {
          Type: 'Map',
          ItemsPath: '$.agentRuntimeArns',
          Parameters: {
            'agentRuntimeArn.$': '$$.Map.Item.Value',
            'prompt.$': '$.prompt',
          },
          Iterator: {
            StartAt: 'CallAgent',
            States: {
              CallAgent: {
                Type: 'Task',
                Resource: 'arn:aws:states:::lambda:invoke',
                Parameters: {
                  FunctionName: invokeAgentFn.functionArn,
                  'Payload.$': '$',
                },
                OutputPath: '$.Payload',
                Retry: [
                  {
                    ErrorEquals: ['States.TaskFailed'],
                    IntervalSeconds: 15,
                    MaxAttempts: 2,
                    BackoffRate: 2,
                  },
                ],
                End: true,
              },
            },
          },
          ResultPath: '$.agentResults',
          Next: 'AggregateResults',
        },
        AggregateResults: {
          Type: 'Task',
          Resource: 'arn:aws:states:::lambda:invoke',
          Parameters: {
            FunctionName: aggregateFn.functionArn,
            'Payload.$': '$',
          },
          OutputPath: '$.Payload',
          End: true,
        },
      },
    };

    const stateMachine = new sfn.CfnStateMachine(this, 'StateMachine', {
      definitionString: JSON.stringify(definition),
      roleArn: sfnRole.roleArn,
      stateMachineType: 'STANDARD',
    });

    // Trigger Lambda
    const triggerFn = new lambda.Function(this, 'TriggerFn', {
      runtime: lambda.Runtime.NODEJS_20_X,
      handler: 'trigger.handler',
      code: lambda.Code.fromAsset('src'),
      memorySize: 256,
      timeout: cdk.Duration.seconds(60),
      environment: {
        STATE_MACHINE_ARN: stateMachine.attrArn,
      },
    });

    triggerFn.addToRolePolicy(new iam.PolicyStatement({
      actions: ['states:StartExecution'],
      resources: [stateMachine.attrArn],
    }));

    new cdk.CfnOutput(this, 'StateMachineArn', {
      value: stateMachine.attrArn,
    });

    new cdk.CfnOutput(this, 'TriggerFunctionName', {
      value: triggerFn.functionName,
    });

    new cdk.CfnOutput(this, 'TriggerFunctionArn', {
      value: triggerFn.functionArn,
    });
  }
}
