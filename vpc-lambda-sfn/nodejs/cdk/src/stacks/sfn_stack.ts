import { Stack, RemovalPolicy } from 'aws-cdk-lib';
import { Construct } from 'constructs';
import { LambdaInvoke } from 'aws-cdk-lib/aws-stepfunctions-tasks';
import { StateMachine, LogLevel, IStateMachine } from 'aws-cdk-lib/aws-stepfunctions';
import { LogGroup } from 'aws-cdk-lib/aws-logs';
import { RetentionDays } from 'aws-cdk-lib/aws-logs';

import { lambdaProps } from './lambda_stack';

export class sfnStack extends Stack {

    public readonly testMachine: IStateMachine;

    constructor(scope: Construct, id: string, props: lambdaProps) {
        super(scope, id, props);
        const prefix = 'test-';

        const lStep = new LambdaInvoke(this, `${prefix}stepLambda`, {
            lambdaFunction: props.ltest,
            outputPath: '$.Payload'
        });

        const logGroup = new LogGroup(this, `${prefix}sampleStep1`, {
            logGroupName: `testlambda${prefix}`,
            removalPolicy: RemovalPolicy.DESTROY,
            retention: RetentionDays.ONE_MONTH
        });

        const definition = lStep;

        const testMachineFlow = new StateMachine(this, `${prefix}testMachineFlow`, {
            definition,
            stateMachineName: `${prefix}testMachineFlow`,
            logs: {
                destination: logGroup,
                level: LogLevel.ALL,
            },
        });
        this.testMachine = testMachineFlow;
    }

}
