import { Construct } from "constructs";
import * as cdk from "aws-cdk-lib";
import { EventBusOne } from "./event-bus-one";
import { EventBusTwo } from "./event-bus-two";
import { SampleStateMachine } from "./state-machine";
import { EventBridgeRule } from "./event-bridge-rule";

export class MainStack extends cdk.Stack {
    constructor(scope: Construct, id: string) {
        super(scope, id);

        const busOne = new EventBusOne(this, "One");
        const busTwo = new EventBusTwo(this, "Two");
        const stateMachine = new SampleStateMachine(this, "SampleStateMachine");

        // build the rules
        new EventBridgeRule(this, "EventBridgeRules", {
            busOne: busOne.eventBus,
            busTwo: busTwo.eventBus,
            stateMachine: stateMachine.stateMachine,
        });
    }
}
