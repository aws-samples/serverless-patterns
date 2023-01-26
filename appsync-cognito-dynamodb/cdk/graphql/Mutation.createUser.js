import { util } from '@aws-appsync/utils'

export function request(ctx) {
	const input = ctx.args.input
	input.userId = util.autoId()

	return {
		operation: 'PutItem',
		key: util.dynamodb.toMapValues({ userId: input.userId }),
		attributeValues: util.dynamodb.toMapValues(input),
	}
}

export function response(ctx) {
	return ctx.result
}
