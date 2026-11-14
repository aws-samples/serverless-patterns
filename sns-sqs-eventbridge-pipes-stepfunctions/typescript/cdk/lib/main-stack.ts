import { Construct } from "constructs";
import * as cdk from "aws-cdk-lib";
import { SnsSqsConstruct } from "./sns-sqs-construct";
import { EventBusConstruct } from "./event-bus-construct";
import { EventBridgePipeConstruct } from "./event-bridge-pipe-construct";
import { StateMachineConstruct } from "./state-machine-construct";
import { EventBridgeRuleConstruct } from "./event-bridge-rule-construct";

export class MainStack extends cdk.Stack {
    constructor(scope: Construct, id: string) {
        super(scope, id);

        // create the queue/topic
        const comms = new SnsSqsConstruct(this, "SnsSqsConstruct");

        // create the eventbus
        const bus = new EventBusConstruct(this, "EventBusConstruct");

        /* create the pipe
         * listen to the sqs created above
         * target the eventbus created above
         */
        const pipe = new EventBridgePipeConstruct(
            this,
            "EventBridgePipeConstruct",
            {
                bus: bus.eventBus,
                queue: comms.queue,
            }
        );

        // create the state machine
        const sm = new StateMachineConstruct(this, "StateMachinConstruct");

        // create the eventbridge rule to trigger the statemachine
        new EventBridgeRuleConstruct(this, "EventBridgeRuleConstruct", {
            bus: bus.eventBus,
            stateMachine: sm.stateMachine,
        });
    }
}
