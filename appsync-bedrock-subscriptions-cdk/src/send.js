export function request(ctx) {
    return {
        payload: {
            chatId: ctx.args.chatId,
            data: ctx.args.data,
            userId: ctx.args.userId
        }
    };
}

export function response(ctx) {
    const { error, result } = ctx;
    if (error) {
      util.appendError(error.message, error.type, result);
    }
    return ctx.result
}
