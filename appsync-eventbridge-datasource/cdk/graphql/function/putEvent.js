import { util } from "@aws-appsync/utils";

export function request(ctx) {
  const id = ctx.arguments.event.id;
  const customMessage = ctx.arguments.event.customMessage;

  if (!id) {
    util.error("Id value is required", "Validation Error");
  }

  if (!customMessage) {
    util.error("customMessage value is required", "Validation Error");
  }

  const events = [
    {
      source: "com.custom.message",
      detail: {
        type: "PUT_EVENT",
        name: "INSERT",
        entityType: "MESSAGE",
        id: id,
        customMessage: customMessage,
      },
      detailType: "CustomMessage",
    },
  ];

  return {
    operation: "PutEvents",
    events: events,
  };
}

export function response(ctx) {
  if (ctx.error) {
    util.error(ctx.error.message, ctx.error.type, ctx.result);
  } else {
    ctx.result.status = "ACCEPTED";
    return ctx.result;
  }
}
