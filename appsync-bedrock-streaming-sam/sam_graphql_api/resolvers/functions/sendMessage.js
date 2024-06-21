export function request(ctx) { 
  return {
    operation: "Invoke",
    invocationType: "Event",
    payload: {
      chatId: ctx.args.chatId,
      prompt: ctx.args.prompt
    }
  }
}
export function response(ctx) { return true }