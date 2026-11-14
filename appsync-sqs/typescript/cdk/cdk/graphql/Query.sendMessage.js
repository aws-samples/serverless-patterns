import { util } from '@aws-appsync/utils'

export function request(ctx) {
	const { accountId, queueUrl, queueName } = ctx.prev.result
	let body = 'Action=SendMessage&Version=2012-11-05'
	const messageBody = util.urlEncode(JSON.stringify(ctx.args))
	const queueUrlEncoded = util.urlEncode(queueUrl)
	body = `${body}&MessageBody=${messageBody}&QueueUrl=${queueUrlEncoded}`

	return {
		version: '2018-05-29',
		method: 'POST',
		resourcePath: `/${accountId}/${queueName}`,
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
		//if response is 200
		// Because the response is of type XML, we are going to convert
		// the result body as a map and only get the User object.

		return util.xml.toMap(ctx.result.body).SendMessageResponse.SendMessageResult
	} else {
		//if response is not 200, append the response to error block.
		return util.appendError(ctx.result.body, ctx.result.statusCode)
	}
}
