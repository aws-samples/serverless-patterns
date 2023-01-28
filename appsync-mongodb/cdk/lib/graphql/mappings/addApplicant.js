import { util } from '@aws-appsync/utils'

export function request(ctx) {
	const secret = ctx.prev.result
	const document = ctx.stash.applicantData
	console.log('the document', document)
	return {
		method: 'POST',
		version: '2018-05-29',
		//update "data-upuof" with your appID
		resourcePath: '/app/data-upuof/endpoint/data/v1/action/insertOne',
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
				document,
			},
		},
	}
}

export function response(ctx) {
	const res = JSON.parse(ctx.result.body)

	// https://www.mongodb.com/docs/atlas/api/data-api-resources/#response-2
	if (res.insertedId) {
		return ctx.stash.applicantData
	} else {
		util.error('record failed to be inserted')
	}
}
