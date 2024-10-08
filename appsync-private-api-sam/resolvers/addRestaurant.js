import * as ddb from '@aws-appsync/utils/dynamodb';

export function request(ctx) {
	const key = { restaurantId: util.autoId() };
	const item = ctx.args.input;
	const condition = { restaurantId: { attributeExists: false } };
	return ddb.put({ key, item, condition });
}

export const response = (ctx) => ctx.result;