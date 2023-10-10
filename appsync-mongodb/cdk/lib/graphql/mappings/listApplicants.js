import { util } from '@aws-appsync/utils'

export function request(ctx) {
	const secret = ctx.prev.result
	const limit = ctx.args.limit ? ctx.args.limit : 100
	const skip = ctx.args.skip ? ctx.args.skip : 0
	return {
		method: 'POST',
		version: '2018-05-29',
		//update "data-upuof" with your appID
		resourcePath: '/app/data-upuof/endpoint/data/v1/action/find',
		params: {
			headers: {
				'api-key': secret,
				'Content-Type': 'application/json',
				'Access-Control-Request-Headers': '*',
				Accept: 'application/json',
			},
			body: {
				dataSource: 'Cluster0',
				database: 'applicationEmployment',
				collection: 'employmentForm',
				limit,
				skip,
			},
		},
	}
}

export function response(ctx) {
	console.log(ctx.result.body)
	const records = JSON.parse(ctx.result.body).documents
	return records
}
