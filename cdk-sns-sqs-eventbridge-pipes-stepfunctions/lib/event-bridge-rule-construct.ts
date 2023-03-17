import { IEventBus, Rule, RuleTargetInput } from "aws-cdk-lib/aws-events";
import { SfnStateMachine } from "aws-cdk-lib/aws-events-targets";
import { Role, ServicePrincipal } from "aws-cdk-lib/aws-iam";
import { Queue } from "aws-cdk-lib/aws-sqs";
import { IStateMachine } from "aws-cdk-lib/aws-stepfunctions";
import { Construct } from "constructs";

export interface EventBridgeRuleProps {
    bus: IEventBus;
    stateMachine: IStateMachine;
}

export class EventBridgeRuleConstruct extends Construct {
    constructor(scope: Construct, id: string, props: EventBridgeRuleProps) {
        super(scope, id);

        const rule = new Rule(this, "SampleEvent-Rule", {
            eventPattern: {
                detailType: ["SampleEventTriggered"],
            },
            ruleName: "sample-event-triggered-rule",
            eventBus: props.bus,
        });

        const dlq = new Queue(this, "SameEventTriggered-DLQ");

        const role = new Role(this, "SameEventTriggered-Role", {
            assumedBy: new ServicePrincipal("events.amazonaws.com"),
        });

        rule.addTarget(
            new SfnStateMachine(props.stateMachine, {
                input: RuleTargetInput,
                deadLetterQueue: dlq,
                role: role,
            })
        );
    }
}
