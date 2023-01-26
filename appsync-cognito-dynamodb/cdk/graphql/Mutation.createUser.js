import { util } from '@aws-appsync/utils'

export function request(ctx) {
	const input = ctx.args.input
	input.userId = util.autoId()

	return {
		operation: 'PutItem',
		key: util.dynamodb.toMapValues({ id: input.id }),
		attributeValues: util.dynamodb.toMapValues(input),
	}
}

export function response(ctx) {
	return ctx.prev.result
}
