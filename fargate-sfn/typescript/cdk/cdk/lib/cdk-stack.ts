import { Duration, Stack, StackProps } from 'aws-cdk-lib';
import { Construct } from 'constructs';
import { InterfaceVpcEndpointAwsService, Vpc } from 'aws-cdk-lib/aws-ec2';
import { Cluster, ContainerImage } from 'aws-cdk-lib/aws-ecs';
import { ApplicationLoadBalancedFargateService } from 'aws-cdk-lib/aws-ecs-patterns';
import { AnyPrincipal, Effect, PolicyStatement } from 'aws-cdk-lib/aws-iam';
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
import path = require('path');

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

    const stateMachine = new StateMachine(this, 'StateMachine', {
      definition,
      timeout: Duration.minutes(5),
    });

    // Fargate definition
    const vpc = new Vpc(this, 'Vpc', {
      maxAzs: 3,
    });

    const cluster = new Cluster(this, 'Cluster', {
      vpc: vpc,
    });

    const fargate = new ApplicationLoadBalancedFargateService(this, 'FargateService', {
      cluster: cluster,
      cpu: 512,
      desiredCount: 1,
      taskImageOptions: {
        image: ContainerImage.fromAsset(path.join(__dirname, '../src/')),
        environment: {
          region: process.env.CDK_DEFAULT_REGION!,
          stateMachineArn: stateMachine.stateMachineArn,
        },
      },
      assignPublicIp: false,
      memoryLimitMiB: 2048,
    });

    stateMachine.grantStartExecution(fargate.taskDefinition.taskRole);

    // Interface endpoint
    const sfnEndpoint = vpc.addInterfaceEndpoint('SfnInterfaceEndpoint', {
      service: InterfaceVpcEndpointAwsService.STEP_FUNCTIONS,
    });

    // Allow start execution action from the Fargate Task Definition only
    sfnEndpoint.addToPolicy(
      new PolicyStatement({
        effect: Effect.ALLOW,
        principals: [new AnyPrincipal()],
        actions: ['states:StartExecution'],
        resources: [stateMachine.stateMachineArn],
        conditions: {
          ArnEquals: {
            'aws:PrincipalArn': `${fargate.taskDefinition.taskRole.roleArn}`,
          },
        },
      })
    );
  }
}
