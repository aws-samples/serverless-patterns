import { util } from '@aws-appsync/utils'

export function request(ctx) {
	const topicArn = util.urlEncode(ctx.prev.result.TOPIC_ARN)
	let body = `Action=Publish&Version=2010-03-31&TopicArn=${topicArn}`
	const obj = ctx.args
	const message = util.urlEncode(JSON.stringify(obj))

	body = `${body}&Message=${message}`

	return {
		version: '2018-05-29',
		method: 'POST',
		resourcePath: '/',
		params: {
			body,
			headers: {
				'content-type': 'application/x-www-form-urlencoded',
			},
		},
	}
}

export function response(ctx) {
	if (ctx.result.statusCode === 200) {
		// Because the response is of type XML, we are going to convert
		// the result body as a map and only get the User object.
		return util.xml.toMap(ctx.result.body).PublishResponse.PublishResult
	} else {
		util.appendError(ctx.result.body, ctx.result.statusCode)
	}
}
