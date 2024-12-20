import * as ddb from '@aws-appsync/utils/dynamodb';

export const request = (ctx) => ddb.get({ key: { restaurantId: ctx.args.restaurantId } });

export const response = (ctx) => ctx.result;