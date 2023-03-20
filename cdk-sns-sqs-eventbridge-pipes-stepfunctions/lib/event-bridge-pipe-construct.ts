import * as pipes from "aws-cdk-lib/aws-pipes";
import {
    PolicyDocument,
    PolicyStatement,
    Effect,
    Role,
    ServicePrincipal,
} from "aws-cdk-lib/aws-iam";
import { IQueue } from "aws-cdk-lib/aws-sqs";
import { Construct } from "constructs";
import { IEventBus } from "aws-cdk-lib/aws-events";

interface PipeProps {
    bus: IEventBus;
    queue: IQueue;
}

export class EventBridgePipeConstruct extends Construct {
    constructor(scope: Construct, id: string, props: PipeProps) {
        super(scope, id);

        // Create the role
        const pipeRole = this.pipeRole(
            scope,
            this.sourcePolicy(props.queue),
            this.targetPolicy(props.bus)
        );

        const pipe = new pipes.CfnPipe(this, "Pipe", {
            name: "SampleEvent-Pipe",
            roleArn: pipeRole.roleArn,
            source: props.queue.queueArn,
            target: props.bus.eventBusArn,
            sourceParameters: this.sourceParameters(),
            targetParameters: this.targetParameters(),
        });
    }

    /*
        Builds the IAM Policy for putting events on the bus
    */
    targetPolicy = (bus: IEventBus): PolicyDocument => {
        return new PolicyDocument({
            statements: [
                new PolicyStatement({
                    resources: [bus.eventBusArn],
                    actions: ["events:PutEvents"],
                    effect: Effect.ALLOW,
                }),
            ],
        });
    };

    /*
        Builds the IAM Policy for reading events from SQS
    */
    sourcePolicy = (queue: IQueue): PolicyDocument => {
        return new PolicyDocument({
            statements: [
                new PolicyStatement({
                    resources: [queue.queueArn],
                    actions: [
                        "sqs:ReceiveMessage",
                        "sqs:DeleteMessage",
                        "sqs:GetQueueAttributes",
                    ],
                    effect: Effect.ALLOW,
                }),
            ],
        });
    };

    /*
        Builds the IAM Role that combines the source and target policy 
        with the ServicePrincipal for AWS Pipes
    */
    pipeRole = (
        scope: Construct,
        sourcePolicy: PolicyDocument,
        targetPolicy: PolicyDocument
    ): Role => {
        return new Role(scope, "PipeRole", {
            assumedBy: new ServicePrincipal("pipes.amazonaws.com"),
            inlinePolicies: {
                sourcePolicy,
                targetPolicy,
            },
        });
    };

    /*
        Input parameters.  Leveraging the Message Body from the SQS receiveMessage
        By using filter criteria the developer can keep downstream systems from 
        receiving unecassary messages from upstream noise
    */
    sourceParameters = () => {
        return {
            sqsQueueParameters: {
                batchSize: 1,
            },
            filterCriteria: {
                filters: [
                    {
                        pattern: `
                {
                    "body": {
                        "eventType": ["SampleEvent"]
                    }
                  }                            
                `,
                    },
                ],
            },
        };
    };

    /*
        Target parameters.  Transforms the input from the queue into something
        that is suitable for the downstream event bus to read.  Transforms give
        the developer the ability to manipulate the output before it is written out
    */
    targetParameters = () => {
        return {
            eventBridgeEventBusParameters: {
                detailType: "SampleEventTriggered",
                source: "com.binaryheap.sample-source",
            },
            inputTemplate: `
            {
                "metaBody": {
                    "correlationId": <$.messageId>
                },
                "messageBody": {
                    "field1": <$.body.field1>,
                    "field2": <$.body.field2>,
                    "field3": <$.body.field3>
                }
            }`,
        };
    };
}
