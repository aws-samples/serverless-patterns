import { Duration } from "aws-cdk-lib";
import { Construct } from "constructs";
import * as sf from "aws-cdk-lib/aws-stepfunctions";
import * as logs from "aws-cdk-lib/aws-logs";
import { IFunction } from "aws-cdk-lib/aws-lambda";
import {
    Choice,
    Condition,
    IChainable,
    LogLevel,
    Map,
    StateMachine,
    StateMachineType,
    Succeed,
} from "aws-cdk-lib/aws-stepfunctions";
import { LambdaInvoke } from "aws-cdk-lib/aws-stepfunctions-tasks";
import { Role, ServicePrincipal } from "aws-cdk-lib/aws-iam";

interface HydratorStateMachineProps {
    patientHydratorFunc: IFunction;
    patientPublisherFunc: IFunction;
}

export class HydratorStateMachineConstruct extends Construct {
    private _stateMachine: StateMachine;

    get stateMachine(): StateMachine {
        return this._stateMachine;
    }

    constructor(
        scope: Construct,
        id: string,
        props: HydratorStateMachineProps
    ) {
        super(scope, id);
        this.finalizeStateMachine(scope, props);
    }

    finalizeStateMachine = (
        scope: Construct,
        props: HydratorStateMachineProps
    ) => {
        const logGroup = new logs.LogGroup(this, "CloudwatchLogs", {
            logGroupName: "/aws/vendedlogs/states/sample-state-machine",
        });

        const role = new Role(this, "StateMachineRole", {
            assumedBy: new ServicePrincipal("states.us-west-2.amazonaws.com"),
        });

        const flow = this.buildStateMachine(scope, props);

        this._stateMachine = new StateMachine(this, "StateMachine", {
            role: role,
            stateMachineName: "SampleStateMachine",
            definition: flow,
            stateMachineType: StateMachineType.EXPRESS,
            timeout: Duration.seconds(5),
            logs: {
                level: LogLevel.ALL,
                destination: logGroup,
                includeExecutionData: true,
            },
        });
    };

    buildStateMachine = (
        scope: Construct,
        props: HydratorStateMachineProps
    ) => {
        const patientHydrate = this.buildPatientHydratorStep(
            scope,
            props.patientHydratorFunc
        );

        patientHydrate.next(
            this.buildPublisherStep(scope, props.patientPublisherFunc)
        );
        return this.buildResourceChoice(scope, patientHydrate);
    };

    buildPublisherStep = (scope: Construct, func: IFunction): IChainable => {
        const mapStep = new Map(scope, "Parse Bundle", {
            itemsPath: "$.patients",
            maxConcurrency: 10,
        });

        mapStep.iterator(this.buildPublisherPrepStep(scope, func));

        return mapStep;
    };

    buildPatientHydratorStep = (
        scope: Construct,
        func: IFunction
    ): LambdaInvoke => {
        const liFun = new LambdaInvoke(
            scope,
            "Patient Hydrator from Healtlake",
            {
                comment:
                    "Hydrates the updated patient by brining in the FHIR data from Healthlake",
                outputPath: "$.Payload",
                lambdaFunction: func,
            }
        );

        liFun.addRetry({
            backoffRate: 1,
            maxAttempts: 2,
            interval: Duration.seconds(1),
        });

        return liFun;
    };

    buildPublisherPrepStep = (
        scope: Construct,
        func: IFunction
    ): LambdaInvoke => {
        const liFun = new LambdaInvoke(
            scope,
            "Do something with each Patient",
            {
                comment:
                    "Replace this with whatever you want to do with the patient",
                outputPath: "$.Payload",
                lambdaFunction: func,
            }
        );

        liFun.addRetry({
            backoffRate: 1,
            maxAttempts: 2,
            interval: Duration.seconds(1),
        });

        return liFun;
    };

    buildResourceChoice = (scope: Construct, chain: IChainable): IChainable => {
        return new Choice(scope, "FHIR Resource", {
            comment:
                "For now only supports Patient, can be modified or made generic",
        })
            .when(
                Condition.stringEquals(
                    "$.detail.requestParameters.resourceType",
                    "Patient"
                ),
                chain
            )
            .otherwise(new Succeed(scope, "Nothing to process"));
    };
}
