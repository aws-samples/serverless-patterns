import * as cdk from "aws-cdk-lib";
import { Construct } from "constructs";
import { EventBridgeRuleConstruct } from "./event-bridge-rule-construct";
import { FunctionsConstruct } from "./functions-contruct";
import { HealthlakeConstruct } from "./healthlake-construct";
import { KeyConstruct } from "./key-construct";
import { HydratorStateMachineConstruct } from "./state-machine-construct";

export class AppStack extends cdk.Stack {
    constructor(scope: Construct, id: string) {
        super(scope, id);

        // create the KMS that encrypts healthlake data
        const key = new KeyConstruct(this, "KeyConstruct");

        // build the healthlake store
        const hl = new HealthlakeConstruct(
            this,
            "HealthlakeConstruct",
            key.key
        );

        // funcs used in the state machine
        const func = new FunctionsConstruct(
            this,
            "FunctionsConstruct",
            hl.cfnFHIRDatastore,
            key.key
        );

        // state machine for working "what" changed
        const sm = new HydratorStateMachineConstruct(this, `StateMachine`, {
            patientHydratorFunc: func.patientHydrator,
            patientPublisherFunc: func.patientPublisher,
        });

        // listens to cloudtrail and pushes to the state machine
        new EventBridgeRuleConstruct(this, "EventBridgeRule", {
            stateMachine: sm.stateMachine,
            dataStore: hl.cfnFHIRDatastore,
        });
    }
}
