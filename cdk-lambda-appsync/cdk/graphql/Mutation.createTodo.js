import { util } from '@aws-appsync/utils'

export function request(ctx) {
	const nowISO = util.time.nowISO8601()

	ctx.args.id = ctx.args.id || util.autoId()
	ctx.args.createdAt = nowISO
	ctx.args.updatedAt = nowISO

	return {
		version: '2017-02-28',
		payload: ctx.args,
	}
}

export function response(ctx) {
	return ctx.result
}
