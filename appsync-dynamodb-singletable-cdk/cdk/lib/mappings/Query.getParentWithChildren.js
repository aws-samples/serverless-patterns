import { util } from '@aws-appsync/utils'

export function request(ctx) {
	return {
		version: '2017-02-28',
		operation: 'Query',
		query: {
			expression: 'PK = :pk',
			expressionValues: {
				':pk': util.dynamodb.toDynamoDB(ctx.args.PK),
			},
		},
	}
}

export function response(ctx) {
	const children = []

	for (item of ctx.result.items) {
		let PK, SK, data, type
		if (item.type === 'parent') {
			PK = item['PK']
			SK = item['SK']
			data = item['data']
			type = item['type']
		}
		if (item.type === 'child') {
			children.push(item)
		}
	}

	return {
		PK,
		SK,
		children,
		data,
		type,
	}
}
