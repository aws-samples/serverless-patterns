import { ScheduledEvent } from "./schemas/input-request-schema";
import { deleteSchdule } from "./utils/scheduler";

export const handler = async (event: ScheduledEvent): Promise<any> => {
  console.log(`Event: ${JSON.stringify(event, null, 2)}`);

  const schedulerInput: any = {
    Name: event.eventName + "-" + event.id,
    GroupName: event.eventType,
    ClientToken: event.clientToken
  };
  const result = await deleteSchdule(schedulerInput)
    .then((result) => {
      if (result.$metadata.httpStatusCode == 200) {
        return {
          statusCode: 200,
          body: JSON.stringify({
            statusMessage: result.$metadata,
            message: 'Message Deleted!',
          }),
        };
      } else {
        return {
          statusCode: result.$metadata.httpStatusCode || 400,
          body: JSON.stringify({
            statusMessage: result.$metadata,
            statusCode: result.$metadata.httpStatusCode,
          }),
        };
      }
    })
    .catch((err) => {
      return {
        statusCode: 400,
        body: JSON.stringify({
          statusMessage: err,
          statusCode: 404,
        }),
      }
    })
}