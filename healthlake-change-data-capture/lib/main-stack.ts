import * as cdk from "aws-cdk-lib";
import { Construct } from "constructs";
import { EventBridgeRuleStack } from "./event-bridge-rule-stack";
import { FunctionsConstruct } from "./functions-stack";
import { HealthlakeConstruct } from "./healthlake-construct";
import { KeyConstruct } from "./key-construct";
import { HydratorStateMachineStack } from "./state-machine-stack";

export class AppStack extends cdk.Stack {
    constructor(scope: Construct, id: string) {
        super(scope, id);

        const key = new KeyConstruct(this, "KeyConstruct");
        const hl = new HealthlakeConstruct(
            this,
            "HealthlakeConstruct",
            key.key
        );

        const func = new FunctionsConstruct(
            this,
            "FunctionsConstruct",
            hl.cfnFHIRDatastore,
            key.key
        );

        // const sm = new HydratorStateMachineStack(this, `StateMachine`, {
        //     patientHydratorFunc: func.patientHydrator,
        //     patientPublisherFunc: func.patientPublisher,
        // });

        // new EventBridgeRuleStack(
        //     this,
        //     "EventBridgeRule",
        //     {
        //         stateMachine: sm.stateMachine,
        //     },
        //     hlStack.cfnFHIRDatastore
        // );
    }
}
