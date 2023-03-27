import { Construct } from "constructs";
import * as sqs from "aws-cdk-lib/aws-sqs";
import * as cdk from "aws-cdk-lib";
import * as events from "aws-cdk-lib/aws-events";
import { CfnFHIRDatastore } from "aws-cdk-lib/aws-healthlake";
import { IStateMachine } from "aws-cdk-lib/aws-stepfunctions";
import * as targets from "aws-cdk-lib/aws-events-targets";
import { RuleTargetInput } from "aws-cdk-lib/aws-events";
import { Role, ServicePrincipal } from "aws-cdk-lib/aws-iam";

export interface EventBridgeRuleConstructProps {
    stateMachine: IStateMachine;
    dataStore: CfnFHIRDatastore;
}

export class EventBridgeRuleConstruct extends Construct {
    constructor(
        scope: Construct,
        id: string,
        props: EventBridgeRuleConstructProps
    ) {
        super(scope, id);

        const rule = new events.Rule(this, "DefaultChangeRule", {
            eventPattern: {
                source: ["aws.healthlake"],
                detailType: ["AWS API Call via CloudTrail"],
                detail: {
                    eventSource: ["healthlake.amazonaws.com"],
                    eventName: ["CreateResource", "UpdateResource"],
                    requestParameters: {
                        datastoreId: [props.dataStore.attrDatastoreId],
                    },
                    responseElements: {
                        statusCode: [200, 201],
                    },
                },
            },
            ruleName: "capture-healthlake-events",
        });

        const queue = new sqs.Queue(this, "Queue", {
            queueName: `rule-event-dlq`,
        });

        const role = new Role(this, "SampleEventSM-Role", {
            assumedBy: new ServicePrincipal("events.amazonaws.com"),
        });

        rule.addTarget(
            new targets.SfnStateMachine(props.stateMachine, {
                input: RuleTargetInput,
                deadLetterQueue: queue,
                role: role,
            })
        );
    }
}
