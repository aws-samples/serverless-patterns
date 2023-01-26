export function request(ctx) {
	const limit = ctx.args.limit || 200
	const nextToken = ctx.args.nextToken
	const scanUsersRequest = {
		version: '2018-05-29',
		operation: 'Scan',
		limit,
	}

	if (nextToken) {
		scanUsersRequest.nextToken = nextToken
	}
	return scanUsersRequest
}

export function response(ctx) {
	const response = { items: ctx.result.items }
	const nextToken = ctx.result.nextToken
	if (nextToken) {
		response.nextToken = ctx.result.nextToken
	}
	return response
}
