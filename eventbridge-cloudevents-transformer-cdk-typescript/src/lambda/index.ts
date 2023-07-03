import { CloudEvent } from "cloudevents";

export const handler = async function (event: any) {
  console.log("received event: %s", event);

  try {
    const ce = new CloudEvent(event);
    ce.validate(); // throws if invalid
    console.log("received valid cloudevent: %s", ce)
  }
  catch (e) {
    const msg = `invalid cloudevent: ${e}`
    console.log(msg)
    return {
      statusCode: 400,
      body: msg,
    };
  }
};
