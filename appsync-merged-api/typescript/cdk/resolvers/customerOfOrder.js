import { util, runtime } from '@aws-appsync/utils';

// Resolves Order.customer: the parent Order comes from the orders API, the customer item from this API's table.
export function request(ctx) {
  if (!ctx.source.customerId) {
    runtime.earlyReturn(null);
  }
  return { operation: 'GetItem', key: util.dynamodb.toMapValues({ id: ctx.source.customerId }) };
}

export function response(ctx) {
  if (ctx.error) {
    util.error(ctx.error.message, ctx.error.type);
  }
  return ctx.result;
}
