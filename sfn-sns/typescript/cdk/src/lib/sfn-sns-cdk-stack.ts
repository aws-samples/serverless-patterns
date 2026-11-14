import * as cdk from 'aws-cdk-lib';
import { Construct } from 'constructs';
import { aws_stepfunctions as sfn, aws_stepfunctions_tasks as tasks, aws_sns as sns, aws_lambda as lambda, CfnOutput } from 'aws-cdk-lib';

export class SfnSnsCdkStack extends cdk.Stack {
  constructor(scope: cdk.App, id: string, props?: cdk.StackProps) {
    super(scope, id, props);

    const convertToSeconds = new tasks.EvaluateExpression(this, 'Convert to seconds', {
      expression: '$.waitMilliseconds / 1000',
      resultPath: '$.waitSeconds',
    });
    
    const wait = new sfn.Wait(this, 'Wait', {
      time: sfn.WaitTime.secondsPath('$.waitSeconds'),
    });

    const snsTopic = new sns.Topic(this, 'state-machine-topic');
    
    const publishMessage = new tasks.SnsPublish(this, 'Publish message', {
      topic: snsTopic,
      message: sfn.TaskInput.fromJsonPathAt("States.Format('Task waited for {} seconds!', $.waitSeconds)"),
      resultPath: '$.sns',
    });
    

    
    const StateMachine = new sfn.StateMachine(this, 'StateMachine', {
      definition: convertToSeconds
        .next(wait)
        .next(publishMessage)
    });
    
    new CfnOutput(this, 'StateMachineARN', { value: StateMachine.stateMachineArn });
    new CfnOutput(this, 'SnsTopicARN', { value: snsTopic.topicArn });
  }
}

