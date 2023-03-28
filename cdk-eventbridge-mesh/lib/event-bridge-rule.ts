import { EventBus, Rule, RuleTargetInput } from "aws-cdk-lib/aws-events";
import { Role, ServicePrincipal } from "aws-cdk-lib/aws-iam";
import { Queue } from "aws-cdk-lib/aws-sqs";
import { StateMachine } from "aws-cdk-lib/aws-stepfunctions";
import { Construct } from "constructs";
import * as targets from "aws-cdk-lib/aws-events-targets";

export interface EventBridgeRuleStackProps {
    busOne: EventBus;
    busTwo: EventBus;
    stateMachine: StateMachine;
}

export class EventBridgeRule extends Construct {
    constructor(
        scope: Construct,
        id: string,
        props: EventBridgeRuleStackProps
    ) {
        super(scope, id);
        this.buildBusOneRule(scope, props);
        this.buildBusTwoRule(scope, props);
    }

    private buildBusOneRule = (
        scope: Construct,
        props: EventBridgeRuleStackProps
    ) => {
        const rule = new Rule(this, "BusOne-BusTwo-Rule", {
            eventPattern: {
                detailType: ["Busing"],
            },
            ruleName: "bus-two-mesh",
            eventBus: props.busOne,
        });

        const dlq = new Queue(this, "BusOneBusTwoMesh-DLQ");

        const role = new Role(this, "BusOneBusTwoMesh-Role", {
            assumedBy: new ServicePrincipal("events.amazonaws.com"),
        });

        rule.addTarget(
            new targets.EventBus(props.busTwo, {
                deadLetterQueue: dlq,
                role: role,
            })
        );
    };

    private buildBusTwoRule = (
        scope: Construct,
        props: EventBridgeRuleStackProps
    ) => {
        const rule = new Rule(this, "SampleEventSM-Rule", {
            eventPattern: {
                detailType: ["Busing"],
            },
            ruleName: "bus-two-busing",
            eventBus: props.busTwo,
        });

        const dlq = new Queue(this, "SampleEventSM-DLQ");

        const role = new Role(this, "SampleEventSM-Role", {
            assumedBy: new ServicePrincipal("events.amazonaws.com"),
        });

        rule.addTarget(
            new targets.SfnStateMachine(props.stateMachine, {
                input: RuleTargetInput,
                deadLetterQueue: dlq,
                role: role,
            })
        );
    };
}
