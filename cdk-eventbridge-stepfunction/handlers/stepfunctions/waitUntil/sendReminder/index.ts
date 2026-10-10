import { EventBridgeEvent, Context } from "aws-lambda";
import { EventBridgeClient, PutEventsCommand } from "@aws-sdk/client-eventbridge";

const eventBridge = new EventBridgeClient({});

export enum EventBridgeTypes {
  StartReminder = "StartReminder",
  Reminder = "Reminder",
}

export interface Reminder {
  at: Date;
}

export const handler = async (
  event: EventBridgeEvent<EventBridgeTypes.StartReminder, Reminder>,
  _context: Context
): Promise<EventBridgeEvent<EventBridgeTypes.StartReminder, Reminder>> => {
  const eventBusName = process.env.EVENT_BUS;
  // Publish to EventBridge.
  await publish<Reminder>(
    "waitUntil",
    EventBridgeTypes.Reminder,
    event.detail,
    eventBusName
  );
  // Return the input as the output.
  return event;
};

export const publish = async <TEvent>(
  source: string,
  detailType: string,
  detail: TEvent,
  eventBusName: string = "default"
) => {
  const res = await eventBridge.send(
    new PutEventsCommand({
      Entries: [
        {
          EventBusName: eventBusName,
          Source: source,
          DetailType: detailType,
          Detail: typeof detail === "string" ? detail : JSON.stringify(detail),
        },
      ],
    })
  );
  const errors: string[] = [];
  res.Entries?.forEach((entry) => {
    if (entry.ErrorMessage) {
      errors.push(entry.ErrorMessage);
      return;
    }
  });
  if (errors.length > 0) {
    throw new Error(errors.join(", "));
  }
};
