import { util } from '@aws-appsync/utils'

export function request(ctx) {
	return {
		version: '2018-05-29',
		operation: 'PutItem',
		key: {
			PK: util.dynamodb.toDynamoDB(ctx.args.PK),
			SK: util.dynamodb.toDynamoDB(ctx.args.SK),
		},

		attributeValues: {
			data: util.dynamodb.toDynamoDB(ctx.args.data),
			type: util.dynamodb.toDynamoDB(ctx.args.type),
		},
	}
}

export function response(ctx) {
	return ctx.result
}
