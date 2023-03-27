import {Fn, NestedStack, NestedStackProps} from "aws-cdk-lib";
import {Options} from "../types/options";
import {Construct} from "constructs";
import * as sf from "aws-cdk-lib/aws-stepfunctions";
import {readFileSync} from "fs";
import * as path from "path";
import * as iam from 'aws-cdk-lib/aws-iam'
import {Effect} from "aws-cdk-lib/aws-iam";
import * as logs from 'aws-cdk-lib/aws-logs';
import {IFunction} from "aws-cdk-lib/aws-lambda";
import {EventBus} from "aws-cdk-lib/aws-events";

interface HydratorStateMachineProps extends NestedStackProps {
    patientHydratorFunc: IFunction,
    patientPublisherFunc: IFunction,
    resourceDeduperFunc: IFunction
}

export class HydratorStateMachineStack extends NestedStack {
    private readonly _stateMachine: sf.CfnStateMachine;

    get stateMachine(): sf.CfnStateMachine {
        return this._stateMachine;
    }

    constructor(scope: Construct, id: string, props: HydratorStateMachineProps) {
        super(scope, id);

        const file = readFileSync(path.resolve(__dirname, "state-machine/design.json"));
        const lambdaArns: string[] = [
            props.patientHydratorFunc.functionArn,
            props.patientPublisherFunc.functionArn,
            props.resourceDeduperFunc.functionArn
        ];

        const cloudWatch = new iam.PolicyDocument({
            statements: [
                new iam.PolicyStatement({
                    resources: ['*'],
                    effect: Effect.ALLOW,
                    actions: [
                        'logs:CreateLogGroup',
                        'logs:CreateLogStream',
                        'logs:PutLogEvents',
                        'logs:CreateLogDelivery',
                        'logs:GetLogDelivery',
                        'logs:UpdateLogDelivery',
                        'logs:DeleteLogDelivery',
                        'logs:ListLogDeliveries',
                        'logs:PutResourcePolicy',
                        'logs:DescribeResourcePolicies',
                        'logs:DescribeLogGroups'
                    ]
                })]
        });

        const lambdaInvoke = new iam.PolicyDocument({
            statements: [
                new iam.PolicyStatement({
                    resources: lambdaArns,
                    effect: Effect.ALLOW,
                    actions: ['lambda:InvokeFunction'],
                }),
            ],
        });

        const exportedMdaBusArn = Fn.importValue('main-mda-bus-arn');
        const bus = EventBus.fromEventBusArn(this, 'EventBus', exportedMdaBusArn);

        const role = new iam.Role(this, 'StateMachineRole', {
            assumedBy: new iam.ServicePrincipal(`states.us-west-2.amazonaws.com`),
            inlinePolicies: {
                invokeLambdas: lambdaInvoke,
                cloudwatch: cloudWatch
            },
        });

        bus.grantPutEventsTo(role);

        const logGroup = new logs.LogGroup(this,
            `log-group`,);

        this._stateMachine = new sf.CfnStateMachine(
            this,
            `state-machine`,
            {
                stateMachineName: 'HealthCDCStateMachine',
                stateMachineType: sf.StateMachineType.EXPRESS,
                roleArn: role.roleArn,
                definitionString: file.toString(),
                definitionSubstitutions: {
                    PatientHydratorFunc: props.patientHydratorFunc.functionArn,
                    PatientPublisherFunc: props.patientPublisherFunc.functionArn,
                    ResourceDeduperFunc: props.resourceDeduperFunc.functionArn
                },
                loggingConfiguration: {
                    destinations: [
                        {
                            cloudWatchLogsLogGroup: {
                                logGroupArn: logGroup.logGroupArn,
                            }
                        }
                    ],
                    includeExecutionData: true,
                    level: sf.LogLevel.ALL,
                }
            }
        );


    }
}

