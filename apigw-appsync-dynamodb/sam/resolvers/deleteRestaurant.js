import * as ddb from '@aws-appsync/utils/dynamodb';

export const request = (ctx) => ddb.remove({ key: { restaurantId: ctx.args.input.restaurantId } });
export const response = (ctx) => ctx.result;