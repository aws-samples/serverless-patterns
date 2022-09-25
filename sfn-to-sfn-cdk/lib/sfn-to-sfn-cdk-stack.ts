import {
  aws_stepfunctions_tasks as tasks,
  aws_stepfunctions as sfn,
  aws_iam as iam,
  Stack,
  StackProps,
  CfnOutput
} from 'aws-cdk-lib';
import { Construct } from 'constructs';

export class SfnToSfnCdkStack extends Stack {
  constructor(scope: Construct, id: string, props?: StackProps) {
    super(scope, id, props);

    // **********************
    //  Child State machine 
    // **********************
    const wait = new sfn.Wait(this, 'WaitXSeconds', {
      time: sfn.WaitTime.secondsPath('$.waitSeconds'),
    });

    const sendTaskTokenSuccess = new tasks.CallAwsService(this, 'SendTaskTokenSuccess', {
      service: 'sfn',
      action: 'sendTaskSuccess',
      parameters: {
        "TaskToken": sfn.JsonPath.stringAt('$.token'),
        "Output": "{\"status\":\"Success\"}"
      },
      iamResources: ['arn:aws:states:' + Stack.of(this).region + ':' + Stack.of(this).account + ':stateMachine:*']
    });

    const childStateMachine = new sfn.StateMachine(this, 'ChildStateMachine', {
      definition: wait.next(sendTaskTokenSuccess)
    });

    childStateMachine.role?.attachInlinePolicy(
      new iam.Policy(this, 'sendTaskSuccessPermission', {
        statements: [
          new iam.PolicyStatement({
            actions: ['states:SendTaskSuccess'],
            resources: ['arn:aws:states:' + Stack.of(this).region + ':' + Stack.of(this).account + ':stateMachine:*'],
          }),
        ],
      }),
    );

    // ***********************
    //  Parent State machine 
    // ***********************
    const callSubWorkFlow = new tasks.StepFunctionsStartExecution(this, 'StartSubWorkFlow', {
      stateMachine: childStateMachine,
      integrationPattern: sfn.IntegrationPattern.WAIT_FOR_TASK_TOKEN,
      input: sfn.TaskInput.fromObject({
        token: sfn.JsonPath.taskToken,
        waitSeconds: 15,
      }),
    });

    const parentStateMachine = new sfn.StateMachine(this, 'ParentStateMachine', {
      definition: callSubWorkFlow
    });

    // *********
    //  Output
    // *********
    new CfnOutput(this, 'parentStateMachine', {
      value: parentStateMachine.stateMachineName,
      description: 'Parent State Machine',
      exportName: 'parentStateMachine',
    });

    new CfnOutput(this, 'childStateMachine', {
      value: childStateMachine.stateMachineName,
      description: 'Child State Machine',
      exportName: 'childStateMachine',
    });
  }
}
