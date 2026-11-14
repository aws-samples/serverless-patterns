import { util } from '@aws-appsync/utils'

export function request(ctx) {
	console.log(ctx.info)
	console.log(ctx.args.input)
	switch (ctx.info.fieldName) {
		case 'listApplicants':
			return {}
		case 'addApplicant':
			const applicantData = {
				id: util.autoId(),
				createdAt: util.time.nowISO8601(),
				updatedAt: util.time.nowISO8601(),
				...ctx.args.input,
			}
			console.log(ctx.args.input)
			console.log(applicantData)
			ctx.stash.applicantData = applicantData
			return {}
		default:
			return {}
	}
}

export function response(ctx) {
	console.log(ctx.prev.result)
	return ctx.prev.result
}
