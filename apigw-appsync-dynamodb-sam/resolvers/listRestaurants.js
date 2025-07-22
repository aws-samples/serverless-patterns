import * as ddb from '@aws-appsync/utils/dynamodb';

export function request(ctx) {
	const { limit = 10, nextToken } = ctx.args;
	return ddb.scan({ limit, nextToken });
}

export function response(ctx) {
	const { items, nextToken } = ctx.result;
	return { items: items ?? [], nextToken };
}