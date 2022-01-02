import { Duration, Stack, StackProps } from 'aws-cdk-lib';
import { Construct } from 'constructs';
import {
  Choice,
  Condition,
  Fail,
  Parallel,
  Pass,
  StateMachine,
  Wait,
  WaitTime
} from 'aws-cdk-lib/aws-stepfunctions';

export class CdkStack extends Stack {
  constructor(scope: Construct, id: string, props?: StackProps) {
    super(scope, id, props);

    // Step function definition
    const startState = new Pass(this, 'StartState');

    const successState = new Pass(this, 'Yes');

    const waitState = new Wait(this, 'Wait 3 Seconds', {
      time: WaitTime.duration(Duration.seconds(3)),
    });

    const failStateParallel = new Fail(this, 'No', {
      error: 'WorkflowFailure',
      cause: "Not hello world state",
    });

    const successStateParallel = new Parallel(this, 'ParallelState');
    successStateParallel.branch(new Pass(this, 'Hello'));
    successStateParallel.branch(new Pass(this, 'World'));
    successStateParallel.addRetry({ maxAttempts: 1 });
    successStateParallel.next(new Pass(this, 'Hello World'));

    successState.next(waitState);
    waitState.next(successStateParallel);

    const definition = startState
      .next(new Choice(this, 'HelloWorldChoice')
        .when(Condition.booleanEquals('$.IsHelloWorldExample', true), successState)
        .when(Condition.booleanEquals('$.IsHelloWorldExample', false), failStateParallel));

    new StateMachine(this, 'StateMachine', {
      definition,
      timeout: Duration.minutes(5),
    });
  }
}
