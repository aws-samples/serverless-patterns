import { util } from '@aws-appsync/utils'

export function request(ctx) {
	return {
		version: '2018-05-29',
		method: 'POST',
		resourcePath: '/',
		params: {
			headers: {
				'content-type': 'application/x-amz-json-1.0',
				'x-amz-target': 'AWSStepFunctions.StartSyncExecution',
			},
			body: {
				stateMachineArn: ctx.prev.result.STATE_MACHINE_ARN,
				name: ctx.args.execution.name,
				input: JSON.stringify({ input: ctx.args.execution.input }),
			},
		},
	}
}

export function response(ctx) {
	// ## Raise a GraphQL field error in case of a datasource invocation error
	if (ctx.error) util.error(ctx.error.message, ctx.error.type)

	// ## if the response status code is not 200, then return an error. Else return the body **
	if (ctx.result.statusCode === 200)
		// ## If response is 200, return the body.
		return JSON.parse(ctx.result.body)
	// ## If response is not 200, append the response to error block.
	else util.appendError(ctx.result.body, ctx.result.statusCode)
}
