import { util } from '@aws-appsync/utils'

export function request(ctx) {
    return {
        method: 'POST',
        resourcePath: '/model/anthropic.claude-v2/invoke',
        params: {
            headers: {
                "Content-Type": "application/json",
                "Accept": "application/json"
            },
            body: {
                "prompt": `\n\nHuman:${ctx.args.prompt}\n\nAssistant:`,
                "temperature": 0.5,
                "top_p": 1,
                "top_k": 250,
                "max_tokens_to_sample": 200,
                "stop_sequences": ["\n\nHuman:"]
            }
        }
    }
}
export function response(ctx) {
    if (ctx.error) {
        util.error(ctx.error.message, ctx.error.type);
    }

    return { completion: JSON.parse(ctx.result.body).completion }
}

