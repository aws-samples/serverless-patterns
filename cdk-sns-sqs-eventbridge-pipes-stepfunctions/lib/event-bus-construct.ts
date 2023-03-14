import { Construct } from "constructs";
import * as events from "aws-cdk-lib/aws-events";
import { IEventBus } from "aws-cdk-lib/aws-events";

export class EventBusConstruct extends Construct {
    private readonly _bus: IEventBus;

    constructor(scope: Construct, id: string) {
        super(scope, id);

        this._bus = new events.EventBus(scope, "EventBus", {
            eventBusName: `sample-event-bus`,
        });
    }

    get eventBus(): IEventBus {
        return this._bus;
    }
}
