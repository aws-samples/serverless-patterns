import { util, Context } from '@aws-appsync/utils';

interface ResponseInput {
    userId: string;
    message: string;
}

interface Response extends ResponseInput {
    id: string;
}
export function request(ctx: Context<{response: ResponseInput}>) {
    const { userId, message } = ctx.arguments.response;
    const payload: Response = {
        id: util.autoId(), // additional calculated fields can be added to the payload
        userId,
        message,
    };

    return { payload, };
}

export function response(ctx: Context): Response {
    return ctx.result;
}