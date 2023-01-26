import { util } from '@aws-appsync/utils'

export function request(ctx) {
	return {}
}

export function response(ctx) {
	return ctx.prev.result
}
