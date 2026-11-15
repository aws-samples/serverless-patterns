import { Construct } from "constructs";
import * as events from "aws-cdk-lib/aws-events";
// import * as targets from "aws-cdk-lib/aws-events-targets";
import { IQueue, Queue } from "aws-cdk-lib/aws-sqs";
import { ITopic, Topic } from "aws-cdk-lib/aws-sns";
import { SqsSubscription } from "aws-cdk-lib/aws-sns-subscriptions";

export class SnsSqsConstruct extends Construct {
    private readonly _queue: IQueue;
    private readonly _topic: ITopic;

    constructor(scope: Construct, id: string) {
        super(scope, id);

        this._topic = new Topic(scope, "SampleTopic", {
            topicName: "sample-topic",
            displayName: "Sample Topic",
        });

        this._queue = new Queue(scope, "SampleQueue", {
            queueName: `sample-queue`,
        });

        this._topic.addSubscription(
            new SqsSubscription(this._queue, {
                rawMessageDelivery: true,
            })
        );
    }

    get topic(): ITopic {
        return this._topic;
    }

    get queue(): IQueue {
        return this._queue;
    }
}
