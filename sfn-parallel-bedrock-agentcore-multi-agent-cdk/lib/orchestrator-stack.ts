import * as cdk from 'aws-cdk-lib';
import * as sfn from 'aws-cdk-lib/aws-stepfunctions';
import * as iam from 'aws-cdk-lib/aws-iam';
import * as logs from 'aws-cdk-lib/aws-logs';
import { Construct } from 'constructs';

interface OrchestratorStackProps extends cdk.StackProps {
  researchRuntimeArn: string;
  researchEndpointUrl: string;
  synthesisRuntimeArn: string;
  synthesisEndpointUrl: string;
}

/**
 * Creates a single-state branch using JSONata to build the payload inline
 * and reshape the output, eliminating the separate Pass state.
 */
function agentBranch(name: string, runtimeArn: string, role: string) {
  const invokeState = `${name}Agent`;
  return {
    StartAt: invokeState,
    States: {
      [invokeState]: {
        Type: 'Task',
        Resource: 'arn:aws:states:::aws-sdk:bedrockagentcore:invokeAgentRuntime',
        Arguments: {
          AgentRuntimeArn: runtimeArn,
          Payload: `{% $string({'role': '${role}', 'prompt': $states.input.prompt}) %}`,
        },
        Output: {
          role,
          answer: '{% $states.result.Response %}',
        },
        Retry: [{
          ErrorEquals: ['States.TaskFailed', 'States.Timeout'],
          IntervalSeconds: 5,
          MaxAttempts: 2,
          BackoffRate: 2,
        }],
        End: true,
      },
    },
  };
}

export class OrchestratorStack extends cdk.Stack {
  constructor(scope: Construct, id: string, props: OrchestratorStackProps) {
    super(scope, id, props);

    const definition = {
      QueryLanguage: 'JSONata',
      StartAt: 'ParallelResearch',
      States: {
        ParallelResearch: {
          Type: 'Parallel',
          Next: 'SynthesisAgent',
          Branches: [
            agentBranch('MarketData', props.researchRuntimeArn, 'market_data'),
            agentBranch('CompetitiveAnalysis', props.researchRuntimeArn, 'competitive_analysis'),
            agentBranch('News', props.researchRuntimeArn, 'news'),
          ],
          Output: {
            prompt: '{% $states.input.prompt %}',
            researchResults: '{% $states.result %}',
          },
        },
        SynthesisAgent: {
          Type: 'Task',
          Resource: 'arn:aws:states:::aws-sdk:bedrockagentcore:invokeAgentRuntime',
          Arguments: {
            AgentRuntimeArn: props.synthesisRuntimeArn,
            Payload: "{% $string({'role': 'synthesis', 'prompt': 'Synthesize these research findings into an executive report. Market Data: ' & $states.input.researchResults[0].answer & ' Competitive Analysis: ' & $states.input.researchResults[1].answer & ' Recent News: ' & $states.input.researchResults[2].answer & ' Original question: ' & $states.input.prompt}) %}",
          },
          Output: {
            question: '{% $states.input.prompt %}',
            report: '{% $states.result.Response %}',
            timestamp: '{% $now() %}',
          },
          Retry: [{
            ErrorEquals: ['States.TaskFailed', 'States.Timeout'],
            IntervalSeconds: 5,
            MaxAttempts: 2,
            BackoffRate: 2,
          }],
          End: true,
        },
      },
    };

    const logGroup = new logs.LogGroup(this, 'StateMachineLogGroup', {
      logGroupName: '/aws/stepfunctions/multi-agent-orchestrator',
      retention: logs.RetentionDays.ONE_WEEK,
      removalPolicy: cdk.RemovalPolicy.DESTROY,
    });

    const stateMachine = new sfn.StateMachine(this, 'MultiAgentOrchestrator', {
      stateMachineName: 'multi-agent-research-orchestrator',
      definitionBody: sfn.DefinitionBody.fromString(JSON.stringify(definition)),
      timeout: cdk.Duration.minutes(15),
      logs: {
        destination: logGroup,
        level: sfn.LogLevel.ALL,
      },
    });

    stateMachine.addToRolePolicy(
      new iam.PolicyStatement({
        actions: ['bedrock-agentcore:InvokeAgentRuntime'],
        resources: [
          props.researchRuntimeArn, `${props.researchRuntimeArn}/*`,
          props.synthesisRuntimeArn, `${props.synthesisRuntimeArn}/*`,
        ],
      }),
    );

    new cdk.CfnOutput(this, 'StateMachineArn', {
      value: stateMachine.stateMachineArn,
    });
  }
}
