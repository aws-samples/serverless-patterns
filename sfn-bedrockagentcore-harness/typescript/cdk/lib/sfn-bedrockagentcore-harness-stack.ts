import * as cdk from 'aws-cdk-lib';
import { Construct } from 'constructs';
import * as sfn from 'aws-cdk-lib/aws-stepfunctions';
import * as iam from 'aws-cdk-lib/aws-iam';

export class SfnBedrockagentcoreHarnessStack extends cdk.Stack {
  constructor(scope: Construct, id: string, props?: cdk.StackProps) {
    super(scope, id, props);

    const harnessArn = new cdk.CfnParameter(this, 'HarnessArn', {
      type: 'String',
      description: 'ARN of the Amazon Bedrock AgentCore harness to invoke',
    });

    // Step Functions execution role with AgentCore permissions
    const sfnRole = new iam.Role(this, 'SfnExecutionRole', {
      assumedBy: new iam.ServicePrincipal('states.amazonaws.com'),
      inlinePolicies: {
        AgentCoreInvoke: new iam.PolicyDocument({
          statements: [
            new iam.PolicyStatement({
              actions: [
                'bedrock-agentcore:InvokeHarness',
                'bedrock-agentcore:InvokeAgentRuntime',
              ],
              resources: [harnessArn.valueAsString],
            }),
          ],
        }),
      },
    });

    // State machine definition using the optimized integration
    // arn:aws:states:::bedrockagentcore:invokeHarness (NOT the SDK integration)
    const definition = {
      Comment: 'Invoke Amazon Bedrock AgentCore harness using Step Functions optimized integration',
      StartAt: 'InvokeHarness',
      States: {
        InvokeHarness: {
          Type: 'Task',
          Resource: 'arn:aws:states:::bedrockagentcore:invokeHarness',
          Parameters: {
            'HarnessArn': harnessArn.valueAsString,
            'RuntimeSessionId.$': '$$.Execution.Name',
            'Messages': [
              {
                'Content': [{ 'Text.$': '$.prompt' }],
                'Role': 'user',
              },
            ],
            'SystemPrompt': [{ 'Text': 'You are a helpful AI assistant. Answer concisely and accurately.' }],
            'MaxIterations': 50,
            'TimeoutSeconds': 600,
          },
          Retry: [
            {
              ErrorEquals: ['BedrockAgentCore.ThrottlingException'],
              IntervalSeconds: 2,
              MaxAttempts: 3,
              BackoffRate: 2.0,
            },
          ],
          Catch: [
            {
              ErrorEquals: ['BedrockAgentCore.ResourceNotFoundException'],
              Next: 'HarnessNotFound',
            },
            {
              ErrorEquals: ['States.ALL'],
              Next: 'HandleError',
            },
          ],
          Next: 'FormatResponse',
        },
        FormatResponse: {
          Type: 'Pass',
          Parameters: {
            'response.$': '$.Output.Message.Content[0].Text',
            'stopReason.$': '$.StopReason',
            'tokensUsed.$': '$.Usage.TotalTokens',
            'latencyMs.$': '$.Metrics.LatencyMs',
          },
          End: true,
        },
        HarnessNotFound: {
          Type: 'Fail',
          Error: 'HarnessNotFound',
          Cause: 'The specified Amazon Bedrock AgentCore harness was not found. Verify the HarnessArn parameter.',
        },
        HandleError: {
          Type: 'Fail',
          Error: 'InvocationFailed',
          Cause: 'Amazon Bedrock AgentCore harness invocation failed.',
        },
      },
    };

    const stateMachine = new sfn.CfnStateMachine(this, 'HarnessStateMachine', {
      definitionString: JSON.stringify(definition),
      roleArn: sfnRole.roleArn,
      stateMachineType: 'STANDARD',
    });

    new cdk.CfnOutput(this, 'StateMachineArn', {
      value: stateMachine.attrArn,
      description: 'AWS Step Functions state machine ARN',
    });

    new cdk.CfnOutput(this, 'HarnessArnOutput', {
      value: harnessArn.valueAsString,
      description: 'Amazon Bedrock AgentCore harness ARN',
    });
  }
}
