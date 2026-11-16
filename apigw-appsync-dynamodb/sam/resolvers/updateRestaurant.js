import { util } from '@aws-appsync/utils';
import * as ddb from '@aws-appsync/utils/dynamodb';

export function request(ctx) {
	const { restaurantId, ...values } = ctx.args.input;
	const condition = { restaurantId: { attributeExists: true } };
	return ddb.update({ key: { restaurantId }, update: values, condition });
}

export function response(ctx) {
	const { error, result } = ctx;
	if (error) {
		return util.error(error.message, error.type);
	}
	return result;
}